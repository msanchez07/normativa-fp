#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construye los datos de normativa (window.NORMDATA) a partir de los textos
oficiales descargados en build/sources/ y los inyecta en index.html.

Uso:  python3 build/build.py

Cómo actualizar la normativa (p. ej. nuevas Instrucciones de curso)
--------------------------------------------------------------------
1. Descarga el PDF oficial (DOGV/BOE) y conviértelo a texto plano, p. ej.:
     pdftotext -layout norma.pdf build/sources/<clave>.txt
   (conveniente limpiar cabeceras/pies de página: CVE, números de página…).
2. Edita este archivo:
   - En DOCS: ajusta short/title/source/url/file/parser de la norma.
   - En ORDER: colócala según su rango (ver TIERS) si cambia la posición.
   - Para una norma nueva, añade su entrada en DOCS y un .txt en sources/.
3. Regenera e inyecta los datos (también regenera build/normdata.json):
     python3 build/build.py
4. Si hay enlaces nuevos en las fichas, añade el patrón correspondiente en
   la función resolve() del lector de texto literal dentro de index.html.

Normas citadas sin texto íntegro (solo ficha + enlace oficial): defínelas
en EXTRAS (con su rango en TIERS) y no necesitan archivo en sources/.
"""
import json
import os
import re
import unicodedata

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
SRC = os.path.join(BASE, "sources")
INDEX = os.path.join(ROOT, "index.html")

ART_RE = re.compile(r"(?m)^\s*(?:Art[íi]culo|Articulo)\s+(\d+)\b[^\n]*")
DISP_RE = re.compile(
    r"(?mi)^\s*(Disposici[óo]n\s+(?:adicional|transitoria|derogatoria|final)\s+[^\n.]{0,40}"
    r"|Disposiciones\s+(?:adicionales|transitorias|derogatorias|finales)(?:\s+[a-záéíóúñ]+)?)")


def sanitize_chars(t):
    """Normaliza glifos y espacios que arrastran los PDF oficiales.

    - Los ``§`` de la sección «Análisis jurídico» vienen codificados en la
      fuente Symbol como U+F0A7 (área de uso privado) y el navegador los pinta
      como un símbolo roto. Se convierten en un espacio.
    - Los espacios EM/EN/NBSP/NARROW de la maquetación se muestran como huecos
      extraños en el texto literal (``white-space:pre-wrap``); se normalizan a
      un espacio normal.
    """
    t = t.replace("\uf0a7", " ").replace("\ufffd", " ")
    out = []
    for ch in t:
        if ch in "\n\t":
            out.append(ch)
        elif unicodedata.category(ch) in ("Co", "Zs", "Cf"):
            out.append(" ")
        else:
            out.append(ch)
    return "".join(out)


def prefilter(t):
    """Limpieza línea a línea conservando saltos de línea."""
    t = t.replace("\ufeff", " ").replace("\x0c", " ")
    t = sanitize_chars(t)
    t = re.sub(r"(?m)^===== PAGE \d+ =====\s*$", " ", t)
    t = re.sub(r"(?m)^\s*Núm\.\s*\d+\s*/\s*\d{2}\.\d{2}\.\d{4}\s+\d+\s*/\s*\d+\s*$", " ", t)
    t = re.sub(r"(?m)^\s*CVE:\s*DOGV-[A-Za-z]-\d{4}-\d+\s+\S*\s*$", " ", t)
    t = re.sub(r"(?m)^\s*https?://\S+\s*$", " ", t)
    t = re.sub(r"(?m)^\s*BOLET[ÍI]N OFICIAL DEL ESTADO.*$", " ", t)
    t = re.sub(r"(?m)^\s*(?:Núm|Pág)\.?\s*\d+\s*$", " ", t)
    t = re.sub(r"(?m)^\s*[IVXLC]{1,6}\s*$", " ", t)          # numeración romana suelta (páginas)
    t = re.sub(r"-\s*\n\s*(?=[a-záéíóúüñ])", "", t)          # palabras partidas
    t = "\n".join(re.sub(r"[ \t]+", " ", ln).strip() for ln in t.split("\n"))
    return t


def clean_frag(t):
    """Convierte un fragmento en texto legible: un párrafo, con saltos antes de listas."""
    t = re.sub(r"\s*\n\s*(?=(?:\d{1,2}\.\s|[a-z]\)\s|–\s))", "\x00", t)
    t = re.sub(r"\s*\n\s*", " ", t)
    t = t.replace("\x00", "\n")
    t = re.sub(r"[ ]{2,}", " ", t)
    t = re.sub(r"\n{2,}", "\n", t)
    t = re.sub(r"\s+([,.;:])", r"\1", t)
    return t.strip()


def parse_articles(raw, cut_annex=False):
    t = prefilter(raw)
    if cut_annex:
        m = re.search(r"(?m)^\s*ANEXO\b", t)
        if m:
            t = t[: m.start()]
    matches = []
    for m in ART_RE.finditer(t):
        matches.append((m.start(), "art", m.group(1), m.group(0).strip()))
    for m in DISP_RE.finditer(t):
        matches.append((m.start(), "disp", None, m.group(1).strip()))
    matches.sort(key=lambda x: x[0])
    best = {}
    for i, (pos, kind, num, heading) in enumerate(matches):
        end = matches[i + 1][0] if i + 1 < len(matches) else len(t)
        body = clean_frag(t[pos + len(heading):end])
        if kind == "art":
            ref = "Artículo " + num
            title = re.sub(r"^Art[íi]culo\s+\d+\s*\.?\s*", "", heading).strip(" .")
            key = num
        else:
            ref = heading
            title = ""
            key = "disp-" + re.sub(r"\W+", "-", heading.lower()).strip("-")[:40]
        cand = {"num": key, "ref": ref, "title": title, "text": body}
        if key not in best or len(body) > len(best[key][1]["text"]):
            best[key] = (pos, cand)
    ordered = [c for _, c in sorted(best.values(), key=lambda x: x[0])]
    return ordered


def parse_instructions(raw):
    t = prefilter(raw)
    lines = t.split("\n")
    body_line = None
    for i, ln in enumerate(lines):
        if re.match(r"^1\.\s+Ámbito de aplicación\s*$", ln):
            body_line = i
    if body_line is None:
        body_line = 0
    toc_lines = lines[:body_line]
    body_start = sum(len(l) + 1 for l in lines[:body_line])
    toc, seen = [], set()
    for ln in toc_lines:
        m = re.match(r"^(\d{1,2}(?:\.\d{1,2})*)\.\s+(.+?)\s*$", ln)
        if m and m.group(1) not in seen:
            seen.add(m.group(1))
            toc.append((m.group(1), m.group(2)))
    body = t[body_start:]
    m = re.search(r"(?m)^\s*ANEXO\b", body)
    if m:
        body = body[: m.start()]
    positions = []
    for num, title in toc:
        prefix = re.sub(r"\s+", " ", title)[:10].lower()
        pos = None
        for m in re.finditer(r"(?m)^" + re.escape(num) + r"\.\s+", body):
            nxt = re.sub(r"\s+", " ", body[m.end(): m.end() + 90]).lower()
            if prefix and (prefix in nxt[:50] or nxt.startswith(prefix[:6])):
                pos = m.start()
                break
        if pos is None:
            mm = re.search(r"(?m)^" + re.escape(num) + r"\.\s+", body)
            if mm:
                pos = mm.start()
        if pos is not None:
            positions.append((pos, num, title))
    positions.sort()
    frags = []
    for i, (pos, num, title) in enumerate(positions):
        end = positions[i + 1][0] if i + 1 < len(positions) else len(body)
        chunk = body[pos:end]
        chunk = re.sub(r"^\s*" + re.escape(num) + r"\.\s+[^\n]*\n?", "", chunk, count=1)
        frags.append({"num": num, "ref": "§" + num, "title": title, "text": clean_frag(chunk)})
    return frags


# Jerarquía normativa (rango jurídico) y color usado para ordenar/etiquetar.
# Orden de prioridad de mayor a menor rango; n es el nivel mostrado.
TIERS = {
    1: "Ley Orgánica",
    2: "Ley Ordinaria",
    3: "Real Decreto-Ley",
    4: "Real Decreto Legislativo",
    5: "Real Decreto / Decreto",
    6: "Orden",
    7: "Resolución / Instrucciones / Circular",
}

# Nivel de rango de cada documento con texto íntegro (clave DOCS -> nivel).
DOC_PRIO = {
    "lo3": 1,
    "rd659": 5,
    "dec114": 5, "dec117": 5, "dec95": 5, "dec74": 5,
    "orden8": 6, "orden10": 6, "orden78": 6, "orden79": 6,
    "orden12": 6, "orden5": 6,
    "instr2627": 7,
}
# Etiqueta específica del rango por documento (si difiere de la genérica).
PRIO_LABEL = {
    "lo3": "Ley Orgánica",
    "rd659": "Real Decreto",
    "dec114": "Decreto del Consell", "dec117": "Decreto del Consell",
    "dec95": "Decreto del Consell", "dec74": "Decreto del Consell",
    "orden8": "Orden de Conselleria", "orden10": "Orden de Conselleria",
    "orden78": "Orden de Conselleria", "orden79": "Orden de Conselleria",
    "orden12": "Orden de Conselleria", "orden5": "Orden de Conselleria",
    "instr2627": "Instrucciones / Resolución",
    # normas citadas (ficha sin texto íntegro)
    "ley39": "Ley Ordinaria",
    "rd278": "Real Decreto", "rd497": "Real Decreto", "rd1085": "Real Decreto",
    "dec107": "Decreto del Consell", "dec72": "Decreto del Consell",
    "dec47": "Decreto del Consell", "dec51": "Decreto del Consell",
    "orden17": "Orden de Conselleria", "orden32": "Orden de Conselleria",
    "orden20": "Orden de Conselleria",
    # ampliación: aspectos normativos de la web de FP
    "rd1147": "Real Decreto",
    "dec135": "Decreto del Consell", "dec36": "Decreto del Consell",
    "dec95corr": "Decreto del Consell",
    "orden1_2014": "Orden de Conselleria",
    "res2023esp": "Resolución / Instrucciones",
    "res2024ects": "Resolución / Instrucciones",
    "instr2019extr": "Resolución / Instrucciones",
    "cal2026": "Resolución / Instrucciones",
    "desdobles": "Resolución / Instrucciones",
    "optatividad": "Resolución / Instrucciones",
}

DOCS = {
    "instr2627": dict(
        short="Instrucciones 2026-27",
        title="Resolución de 16 de julio de 2026, de la Secretaría Autonómica de Educación, por la que se dictan instrucciones sobre ordenación académica y organización de los centros que impartan los grados D y E de Formación Profesional durante el curso 2026-2027",
        source="DOGV 20.07.2026 · CVE DOGV-C-2026-24495",
        url="https://dogv.gva.es/datos/2026/07/20/pdf/2026_24495_es.pdf",
        file="instr2627.txt", parser="instr"),
    "orden8": dict(
        short="Orden 8/2025",
        title="Orden 8/2025, de 22 de abril, de la Conselleria de Educación, Cultura, Universidades y Empleo, por la que se regula la evaluación del proceso de enseñanza-aprendizaje en ciclos formativos y cursos de especialización derivados de la Ley orgánica 3/2022 (modificada por la Orden 5/2026, de 1 de abril)",
        source="DOGV 30.04.2025 · CVE DOGV-C-2025-13083",
        url="https://dogv.gva.es/datos/2025/04/30/pdf/2025_13083_es.pdf",
        file="orden8.txt", parser="art"),
    "rd659": dict(
        short="RD 659/2023",
        title="Real Decreto 659/2023, de 18 de julio, por el que se desarrolla la ordenación del Sistema de Formación Profesional",
        source="BOE núm. 174, de 22.07.2023 · BOE-A-2023-16889",
        url="https://www.boe.es/eli/es/rd/2023/07/18/659/con",
        file="rd659.txt", parser="art"),
    "lo3": dict(
        short="LO 3/2022",
        title="Ley Orgánica 3/2022, de 31 de marzo, de ordenación e integración de la Formación Profesional",
        source="BOE núm. 78, de 01.04.2022 · BOE-A-2022-5139",
        url="https://www.boe.es/eli/es/lo/2022/03/31/3/con",
        file="lo3.txt", parser="art"),
    "orden10": dict(
        short="Orden 10/2024",
        title="Orden 10/2024, de 10 de mayo, de la Conselleria de Educación, Universidades y Empleo, por la que se regula el acceso, la admisión y matrícula a ciclos formativos de grado básico, grado medio y grado superior y cursos de especialización de Formación Profesional",
        source="DOGV 14.05.2024 · 2024/4272",
        url="https://dogv.gva.es/datos/2024/05/14/pdf/2024_4272.pdf",
        file="orden10.txt", parser="art"),
    "dec114": dict(
        short="Decreto 114/2025",
        title="Decreto 114/2025, de 29 de julio, del Consell, por el que se establecen los currículos de los ciclos formativos de grado medio y de grado superior de Formación Profesional (articulado; anexos en el PDF oficial)",
        source="DOGV 04.08.2025 · CVE DOGV-C-2025-29742",
        url="https://dogv.gva.es/es/eli/es-vc/d/2025/07/29/114",
        file="dec114.txt", parser="art", cut_annex=True),
    "dec117": dict(
        short="Decreto 117/2025",
        title="Decreto 117/2025, de 5 de agosto, del Consell, por el que se establecen los currículos de los ciclos formativos de Grado Básico de Formación Profesional (articulado; anexos en el PDF oficial)",
        source="DOGV 13.08.2025 · CVE DOGV-C-2025-32763",
        url="https://dogv.gva.es/es/eli/es-vc/d/2025/08/05/117",
        file="dec117.txt", parser="art", cut_annex=True),
    "dec95": dict(
        short="Decreto 95/2026",
        title="Decreto 95/2026, de 19 de junio, del Consell, por el que se establecen los currículos de los cursos de especialización de Formación Profesional para la Comunitat Valenciana (articulado; anexos en el PDF oficial)",
        source="DOGV 25.06.2026 · CVE DOGV-C-2026-21170",
        url="https://dogv.gva.es/es/eli/es-vc/d/2026/06/19/95",
        file="dec95.txt", parser="art", cut_annex=True),
    "dec74": dict(
        short="Decreto 74/2013",
        title="Decreto 74/2013, de 14 de junio, del Consell, por el que se regula la Formación Profesional Dual del sistema educativo en la Comunitat Valenciana (texto consolidado)",
        source="DOGV 18.06.2013 · 2013/6399",
        url="https://dogv.gva.es/auto/dogv/docvpub/rlgv/2013/D_2013_074_ca_D_2024_066.pdf",
        file="dec74.txt", parser="art"),
    "orden78": dict(
        short="Orden 78/2010",
        title="Orden 78/2010, de 27 de agosto, de la Conselleria de Educación, por la que se regulan determinados aspectos de la ordenación y organización académica de los ciclos formativos de Formación Profesional",
        source="DOGV 03.09.2010 · 2010/9539",
        url="https://dogv.gva.es/datos/2010/09/03/pdf/2010_9539.pdf",
        file="orden78.txt", parser="art"),
    "orden79": dict(
        short="Orden 79/2010",
        title="Orden 79/2010, de 27 de agosto, de la Conselleria de Educación, por la que se regula la evaluación del alumnado de los ciclos formativos de Formación Profesional del sistema educativo (aplicable a ciclos LOGSE)",
        source="DOGV 06.09.2010",
        url="https://dogv.gva.es/es/web/formacion-profesional/avaluacio",
        file="orden79.txt", parser="art"),
    "orden12": dict(
        short="Orden 12/2022",
        title="Orden 12/2022, de 9 de marzo, de la Conselleria de Educación, Cultura y Deporte, por la que se regula el módulo profesional de Formación en Centros de Trabajo (FCT) de los ciclos formativos de grado medio y superior, FP Básica, Programas Formativos de Cualificación Básica, cursos de especialización y Bloque de Formación Práctica (BFP)",
        source="DOGV 16.03.2022 · 2022/2086",
        url="https://dogv.gva.es/datos/2022/03/16/pdf/2022_2086.pdf",
        file="orden12.txt", parser="art"),
    "orden5": dict(
        short="Orden 5/2022",
        title="Orden 5/2022, de 15 de febrero, de la Conselleria de Educación, Cultura y Deporte, por la cual se regulan determinados aspectos de la ordenación de la Formación Profesional Dual del sistema educativo en la Comunitat Valenciana",
        source="DOGV 22.02.2022 · 2022/1272",
        url="https://dogv.gva.es/datos/2022/02/22/pdf/2022_1272.pdf",
        file="orden5.txt", parser="art"),
}

ORDER = ["lo3", "rd659", "dec114", "dec117", "dec95", "dec74",
         "orden8", "orden10", "orden78", "orden79", "orden12", "orden5",
         "instr2627"]

# Normas citadas en la guía sin texto íntegro incrustado: ficha con rango,
# descripción y enlace oficial. No requieren archivo en sources/.
EXTRAS = {
    "ley39": dict(
        short="Ley 39/2015",
        title="Ley 39/2015, de 1 de octubre, del Procedimiento Administrativo Común de las Administraciones Públicas",
        source="BOE núm. 236, de 02.10.2015 · BOE-A-2015-10565",
        url="https://www.boe.es/eli/es/l/2015/10/01/39/con", prio=2),
    "rd278": dict(
        short="RD 278/2023",
        title="Real Decreto 278/2023, de 11 de abril, por el que se establece el calendario de implantación del Sistema de Formación Profesional establecido por la Ley Orgánica 3/2022, de 31 de marzo, de ordenación e integración de la Formación Profesional",
        source="BOE núm. 87, de 12.04.2023 · BOE-A-2023-9045",
        url="https://www.boe.es/eli/es/rd/2023/04/11/278/con", prio=5),
    "rd497": dict(
        short="RD 497-500/2024",
        title="Reales Decretos 497/2024, 498/2024, 499/2024 y 500/2024, de 21 de mayo, por los que se modifican determinados reales decretos por los que se establecen títulos y cursos de especialización de Formación Profesional y se fijan sus enseñanzas mínimas (497: cursos de especialización; 498: grado básico; 499: grado medio; 500: grado superior)",
        source="BOE 22.05.2024 · BOE-A-2024-10682 y siguientes",
        url="https://www.boe.es/eli/es/rd/2024/05/21/497/con", prio=5),
    "rd1085": dict(
        short="RD 1085/2020",
        title="Real Decreto 1085/2020, de 9 de diciembre, por el que se establecen convalidaciones de módulos profesionales de los títulos de Formación Profesional del sistema educativo español y las medidas para su aplicación",
        source="BOE núm. 334, de 22.12.2020 · BOE-A-2020-17274",
        url="https://www.boe.es/eli/es/rd/2020/12/09/1085/con", prio=5),
    "dec107": dict(
        short="Decreto 107/2022",
        title="Decreto 107/2022, de 5 de agosto, del Consell, por el que se establece la ordenación y el currículo de la Educación Secundaria Obligatoria",
        source="DOGV · 2022/7748",
        url="https://dogv.gva.es/es/eli/es-vc/d/2022/08/05/107", prio=5),
    "dec72": dict(
        short="Decreto 72/2021",
        title="Decreto 72/2021, de 21 de mayo, del Consell, de organización de la orientación educativa y profesional en el sistema educativo valenciano",
        source="DOGV · 2021/6157",
        url="https://dogv.gva.es/es/eli/es-vc/d/2021/05/21/72", prio=5),
    "dec47": dict(
        short="Decreto 47/2021",
        title="Decreto 47/2021, de 26 de marzo, del Consell, de modificación del Decreto 74/2013, por el que se regula la Formación Profesional Dual del sistema educativo en la Comunitat Valenciana",
        source="DOGV · 2021/2975",
        url="https://dogv.gva.es/es/eli/es-vc/d/2021/03/26/47", prio=5),
    "dec51": dict(
        short="Decreto 51/2011",
        title="Decreto 51/2011, de 13 de mayo, del Consell, sobre el sistema de comunicación de datos a la conselleria competente en materia de educación, a través del sistema informático ITACA",
        source="DOGV · 2011/5616",
        url="https://dogv.gva.es/es/eli/es-vc/d/2011/05/13/51", prio=5),
    "orden17": dict(
        short="Orden 17/2022",
        title="Orden 17/2022, de 25 de marzo, de la Conselleria de Educación, Cultura y Deporte, por la que se regula la oferta parcial de las enseñanzas de los ciclos formativos de Formación Profesional",
        source="DOGV · 2022/2646",
        url="https://dogv.gva.es/es/eli/es-vc/o/2022/03/25/17", prio=6),
    "orden32": dict(
        short="Orden 32/2011",
        title="Orden 32/2011, de 20 de diciembre, de la Conselleria de Educación, Formación y Empleo, por la que se regula el derecho del alumnado a la objetividad en la evaluación y el procedimiento de reclamación de las calificaciones obtenidas",
        source="DOGV · 2011/12526",
        url="https://dogv.gva.es/es/eli/es-vc/o/2011/12/20/32", prio=6),
    "orden20": dict(
        short="Orden 20/2019",
        title="Orden 20/2019, de 30 de abril, de la Conselleria de Educación, Investigación, Cultura y Deporte, por la que se regula la organización de la respuesta educativa para la inclusión del alumnado en los centros docentes sostenidos con fondos públicos del sistema educativo valenciano",
        source="DOGV · 2019/4443",
        url="https://dogv.gva.es/es/eli/es-vc/o/2019/04/30/20", prio=6),
    # --- Ampliación: resto de aspectos normativos de la web de FP ---
    "rd1147": dict(
        short="RD 1147/2011",
        title="Real Decreto 1147/2011, de 29 de julio, por el que se establece la ordenación general de la Formación Profesional del sistema educativo (aplicable a los ciclos LOE)",
        source="BOE núm. 182, de 30.07.2011 · BOE-A-2011-13118",
        url="https://www.boe.es/eli/es/rd/2011/07/29/1147/con", prio=5),
    "dec135": dict(
        short="Decreto 135/2014",
        title="Decreto 135/2014, de 8 de agosto, del Consell, por el que se regulan las condiciones y el procedimiento para la implantación y desarrollo de los ciclos de Formación Profesional Básica en la Comunitat Valenciana",
        source="DOGV · 2014/7965",
        url="https://dogv.gva.es/es/eli/es-vc/d/2014/08/08/135", prio=5),
    "dec36": dict(
        short="Decreto 36/2020",
        title="Decreto 36/2020, de 13 de marzo, del Consell, de modificación del Decreto 135/2014, por el que se regulan los ciclos de Formación Profesional Básica en la Comunitat Valenciana",
        source="DOGV · 2020/3397",
        url="https://dogv.gva.es/es/eli/es-vc/d/2020/03/13/36", prio=5),
    "dec95corr": dict(
        short="Corrección de errores Dto. 95/2026",
        title="Corrección de errores del Decreto 95/2026, de 19 de junio, del Consell, por el que se establecen los currículos de los cursos de especialización de Formación Profesional para la Comunitat Valenciana",
        source="DOGV 29.06.2026",
        url="https://dogv.gva.es/va/eli/es-vc/d/2026/06/19/95/corrigendum/20260629", prio=5),
    "orden1_2014": dict(
        short="Orden 1/2014",
        title="Orden 1/2014, de 8 de agosto, de la Conselleria de Educación, Cultura y Deporte, por la que se regula la certificación de la formación en prevención de riesgos laborales y de su nivel básico para el alumnado de Formación Profesional",
        source="DOGV 13.08.2014 · 2014/7666",
        url="https://dogv.gva.es/datos/2014/08/13/pdf/2014_7666.pdf", prio=6),
    "res2023esp": dict(
        short="Resolución 26/04/2023",
        title="Resolución de 26 de abril de 2023, de la Dirección General de Formación Profesional y Enseñanzas de Régimen Especial, sobre los cursos de especialización de Formación Profesional",
        source="DOGV 11.05.2023",
        url="https://dogv.gva.es/datos/2023/05/11/pdf/2023_4695.pdf", prio=7),
    "res2024ects": dict(
        short="Resolución 26/04/2024",
        title="Resolución de 26 de abril de 2024, por la que se establecen las correspondencias entre los títulos de Técnico/a Superior de FP, los títulos universitarios de grado de las universidades de la Comunitat Valenciana y los títulos de grado en enseñanzas artísticas superiores, así como el reconocimiento de créditos ECTS",
        source="DOGV 30.04.2024",
        url="https://dogv.gva.es/datos/2024/04/30/pdf/2024_3733.pdf", prio=7),
    "instr2019extr": dict(
        short="Instrucciones 16/07/2019",
        title="Instrucciones de 16 de julio de 2019 del SAEFP, por las que se establecen directrices sobre el alumnado que se incorpora al sistema educativo español procedente de centros de titularidad extranjera o sistemas educativos de otros países",
        source="Conselleria de Educación",
        url="https://ceice.gva.es/documents/162640733/168227315/Instruccions+del+SAEFP_centres+extrangers_signada.pdf", prio=7),
    "cal2026": dict(
        short="Calendario escolar 2026-27",
        title="Resolución de 15 de junio de 2026, de la Dirección General de Centros Docentes, por la que se fija el calendario escolar del curso académico 2026-2027 en la Comunitat Valenciana",
        source="DOGV 18.06.2026",
        url="https://dogv.gva.es/datos/2026/06/18/pdf/2026_20810_es.pdf", prio=7),
    "desdobles": dict(
        short="Desdobles de profesorado",
        title="Resoluciones de desdobles de profesorado de FP: Resolución de 2 de diciembre de 2022 (especialidades susceptibles de desdoble), Resolución de 19 de junio de 2023 (actualización; corrección de 05.07.2023) y Resolución de 16 de noviembre de 2023 (nuevos desdobles por matrícula definitiva)",
        source="DOGV 09.12.2022 · 22.06.2023 · 23.11.2023",
        url="https://dogv.gva.es/datos/2023/06/22/pdf/2023_7061.pdf", prio=7),
    "optatividad": dict(
        short="Optatividad · Instrucciones",
        title="Instrucciones sobre la oferta de módulos optativos de Formación Profesional (curso 2025-2026) y listados de módulos optativos presentados por los centros",
        source="Conselleria de Educación",
        url="https://ceice.gva.es/documents/388109149/392955746/Instrucciones_optativas_FP_definitivas_firmado_.pdf/317a5dfd-f363-f237-30ef-2863c616b747?t=1750251622911", prio=7),
}

EXTRA_ORDER = ["ley39", "rd278", "rd497", "rd1085", "rd1147", "dec107", "dec72",
               "dec47", "dec51", "dec135", "dec36", "dec95corr", "orden1_2014",
               "orden17", "orden32", "orden20", "res2023esp", "res2024ects",
               "instr2019extr", "cal2026", "desdobles", "optatividad"]


def prio_of(key, n):
    return {"n": n, "tier": PRIO_LABEL.get(key, TIERS.get(n, "Norma"))}


def build():
    docs = {}
    for key in ORDER:
        meta = DOCS[key]
        raw = open(os.path.join(SRC, meta["file"]), encoding="utf-8").read()
        frags = parse_instructions(raw) if meta["parser"] == "instr" else parse_articles(raw, meta.get("cut_annex", False))
        arts = {f["num"]: f for f in frags}
        docs[key] = {
            "short": meta["short"],
            "title": meta["title"],
            "source": meta["source"],
            "url": meta["url"],
            "frags": frags,
            "arts": arts,
            "prio": prio_of(key, DOC_PRIO[key]),
        }
        print(f"{key:10s} {meta['short']:22s} {PRIO_LABEL.get(key, ''):26s} {len(frags):4d} apartados  {sum(len(f['text']) for f in frags):8d} car")
    for key in EXTRA_ORDER:
        m = EXTRAS[key]
        docs[key] = {
            "short": m["short"],
            "title": m["title"],
            "source": m["source"],
            "url": m["url"],
            "frags": [],
            "arts": {},
            "prio": prio_of(key, m["prio"]),
        }
        print(f"{key:10s} {m['short']:22s} {PRIO_LABEL.get(key, ''):26s} ficha · enlace oficial")
    return {"order": ORDER, "extra": EXTRA_ORDER, "docs": docs}


def inject(data):
    js = json.dumps(data, ensure_ascii=False)
    js = js.replace("</", "<\\/").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    html = open(INDEX, encoding="utf-8").read()
    found = [False]
    def repl(m):
        found[0] = True
        return "/* NORM_DATA_START */\nwindow.NORMDATA = " + js + ";\n/* NORM_DATA_END */"
    new = re.sub(
        r"/\* NORM_DATA_START \*/.*?/\* NORM_DATA_END \*/",
        repl, html, count=1, flags=re.S)
    if not found[0]:
        raise SystemExit("No se encontraron los marcadores NORM_DATA en index.html")
    open(INDEX, "w", encoding="utf-8").write(new)
    print("index.html actualizado:", len(new), "bytes")


if __name__ == "__main__":
    data = build()
    with open(os.path.join(BASE, "normdata.json"), "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
    inject(data)
