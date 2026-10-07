# -*- coding: utf-8 -*-
"""Contenido del curso intensivo de normativa de FP (Comunitat Valenciana).

Editado a mano a partir de la guía y de las fuentes oficiales del DOGV/BOE.
Este módulo solo contiene datos: no genera nada por sí mismo.
"""

INTRO = ("Método intensivo: primero entiende la estructura, luego memoriza los números y las "
         "distinciones, y por último compruébalo con tests y examen. Cada día: una lección nueva, "
         "el repaso de fichas pendientes y un test. Con constancia, en dos semanas tienes la base sólida.")

# ---------------------------------------------------------------------------
# Plan intensivo de 12 días
# ---------------------------------------------------------------------------
PLAN = [
    {"title": "Cimientos del sistema", "tasks": [
        "Lección 1 (fundamentos) + fichas",
        "Lección 2 (arquitectura normativa) + fichas",
        "Test módulos 1 y 2",
    ]},
    {"title": "Acceso y matrícula", "tasks": [
        "Lección 3 (acceso, admisión, matrícula)",
        "Taller de números: fechas clave",
        "Test módulo 3 + repaso SRS",
    ]},
    {"title": "Anulación y asistencia", "tasks": [
        "Lección 4 (anulación y pérdida)",
        "Memoriza: 15% / 10 días · 5% / 8 días · 85%",
        "Test módulo 4",
    ]},
    {"title": "Evaluación", "tasks": [
        "Lección 5 (evaluación)",
        "Fichas del módulo 5 hasta caja ≥3",
        "Test módulo 5 + repaso SRS",
    ]},
    {"title": "Convocatorias y renuncias", "tasks": [
        "Lección 6 (convocatorias)",
        "Memoriza plazos de 10 días hábiles y 2 meses",
        "Test módulo 6",
    ]},
    {"title": "Promoción", "tasks": [
        "Lección 7 (promoción y recuperación)",
        "Usa la calculadora de promoción de la guía",
        "Test módulo 7 + repaso SRS",
    ]},
    {"title": "Calificaciones y título", "tasks": [
        "Lección 8 (calificaciones y titulación)",
        "Memoriza: 1-10 sin decimales · MH 10% · MH honor 2/3",
        "Test módulo 8",
    ]},
    {"title": "Convalidaciones", "tasks": [
        "Lección 9 (convalidaciones y exenciones)",
        "Fichas del módulo 9 hasta caja ≥3",
        "Test módulo 9 + repaso SRS",
    ]},
    {"title": "FE, FCT y Dual", "tasks": [
        "Lección 10 (FE, FCT y Dual)",
        "Memoriza: 100 h · 25-35% · 35% centro · 6 meses/1 año",
        "Test módulo 10",
    ]},
    {"title": "NEE y repaso duro", "tasks": [
        "Lección 11 (necesidades específicas)",
        "Test módulo 11",
        "Repaso de TODAS las fichas",
    ]},
    {"title": "Otros aspectos I (ordenación y currículo)", "tasks": [
        "Lección 13 (RD 1147/2011, Grado Básico anterior, especialización)",
        "Fichas del módulo 13 hasta caja ≥3",
        "Test módulo 13",
    ]},
    {"title": "Otros aspectos II (alumnado y organización)", "tasks": [
        "Lección 14 (extranjeros, PRL, ECTS, intermodular, calendario, desdobles, optatividad, anexos)",
        "Fichas del módulo 14",
        "Test módulo 14 + repaso SRS",
    ]},
    {"title": "Trampas y números", "tasks": [
        "Lección 12 (trampas y repaso integral)",
        "Taller de números completo",
        "Test módulo 12",
    ]},
    {"title": "Examen final", "tasks": [
        "Repaso de fichas pendientes",
        "Examen final (objetivo: ≥80%)",
        "Repite el examen si no llegas al 80%",
    ]},
]

MODULES = []

# ===========================================================================
# MÓDULO 1 · FUNDAMENTOS
# ===========================================================================
MODULES.append(dict(
    id="m1", title="Fundamentos del sistema de FP", tagline="Qué es la FP, los grados A-E y las leyes que la ordenan.",
    objetivos=[
        "Distinguir los cinco grados (A, B, C, D, E).",
        "Situar LO 3/2022, RD 659/2023 y RD 278/2023.",
        "Explicar qué cambia con la LFP y qué ciclos quedan en LOGSE.",
    ],
    lesson="""
<h3>1. La idea de fondo</h3>
<p>La Formación Profesional se organiza en un <b>sistema único e integrado</b>. Todo lo que se aprende es <b>acreditable, acumulable y capitalizable</b>: se puede reconocer, sumar y reutilizar a lo largo de la vida.</p>

<h3>2. Los cinco grados</h3>
<table>
<tr><th>Grado</th><th>Qué es</th></tr>
<tr><td><b>A</b></td><td>Acreditaciones parciales de competencia.</td></tr>
<tr><td><b>B</b></td><td>Certificados de competencia profesional.</td></tr>
<tr><td><b>C</b></td><td>Certificados profesionales.</td></tr>
<tr><td><b>D</b></td><td>Títulos de <b>Técnico Básico</b>, <b>Técnico</b> y <b>Técnico Superior</b> (los ciclos formativos).</td></tr>
<tr><td><b>E</b></td><td>Cursos de especialización.</td></tr>
</table>
<div class="callout tip"><b>Truco A-B-C-D-E:</b> A = <i>a</i>proximación (parcial), B = <i>b</i>ásico (certificado de competencia), C = <i>c</i>ertificado profesional, D = <i>d</i>iploma/título (los ciclos), E = <i>e</i>specialización.</div>

<h3>3. Leyes estatales que tienes que saber</h3>
<ul>
<li><b>LO 3/2022</b>, de 31 de marzo, de ordenación e integración de la FP: es la <b>ley paraguas</b>.</li>
<li><b>RD 659/2023</b>, de 18 de julio: <b>desarrolla la ordenación</b> del sistema (el desarrollo reglamentario).</li>
<li><b>RD 278/2023</b>, de 11 de abril: <b>calendario de implantación</b>.</li>
<li>Enseñanzas mínimas: <b>RD 497/2024</b> (especialización), <b>498/2024</b> (básico), <b>499/2024</b> (medio) y <b>500/2024</b> (superior).</li>
</ul>

<h3>4. Normativa de la Comunitat Valenciana</h3>
<ul>
<li><b>Decreto 114/2025</b>: currículos de Grado Medio y Superior (modificado por el <b>Decreto 95/2026</b>).</li>
<li><b>Decreto 117/2025</b>: currículos de Grado Básico.</li>
<li><b>Decreto 95/2026</b>: currículos de los cursos de especialización.</li>
<li><b>Orden 8/2025</b> (modificada por la <b>Orden 5/2026</b>): <b>evaluación</b> de ciclos y cursos de especialización LFP.</li>
<li><b>Orden 10/2024</b>: acceso, admisión y matrícula.</li>
<li>Ciclos <b>LOGSE</b> (antiguos): <b>Orden 78/2010</b> (ordenación) y <b>Orden 79/2010</b> (evaluación).</li>
</ul>

<h3>5. Implantación en el curso 2026-27</h3>
<ul>
<li>Toda la oferta se cursa según el nuevo plan de la LFP, <b>excepto</b> los ciclos LOGSE.</li>
<li><b>Excepción</b>: alumnado que en 2025-26 cursó terceros cursos LOE (nocturnos o de tres años) o segundos de doble titulación y en 2026-27 tenga módulos pendientes (incluida la FCT).</li>
<li>Quien tenga FCT y Proyecto pendientes de 2025-26 y no esté en esa excepción deberá matricularse por LFP para finalizar.</li>
</ul>
    """,
    trucos=[
        "<b>A-B-C-D-E:</b> de menos a más. D son los ciclos de siempre (Básico, Medio, Superior). E es especialización.",
        "<b>3/2022 → ley · 659/2023 → desarrollo · 278/2023 → calendario.</b> Fechas: 31/03, 18/07, 11/04.",
        "En la Comunitat: <b>Decretos para currículos (114, 117, 95) y Órdenes para gestión (8 y 10).</b>",
    ],
    trampas=[
        "El Decreto 95/2026 aparece <b>dos veces</b>: modifica el 114/2025 y regula los cursos de especialización. No lo confundas.",
        "La Orden 8/2025 deroga la Orden 79/2010 <b>salvo para ciclos LOGSE</b>.",
    ],
    normas=[("LO 3/2022", "https://www.boe.es/eli/es/lo/2022/03/31/3/con"),
            ("RD 659/2023", "https://www.boe.es/eli/es/rd/2023/07/18/659/con"),
            ("RD 278/2023", "https://www.boe.es/eli/es/rd/2023/04/11/278/con")],
    cards=[
        ("¿Qué significa que el sistema es «único e integrado»?",
         "Que toda la formación es acreditable, acumulable y capitalizable: se reconoce, se suma y se reutiliza.", "LO 3/2022"),
        ("Enumera los cinco grados de la FP (A-E).",
         "A: acreditaciones parciales de competencia. B: certificados de competencia profesional. C: certificados profesionales. D: títulos de Técnico Básico, Técnico y Técnico Superior. E: cursos de especialización.", "LO 3/2022"),
        ("¿Qué grado son los ciclos formativos de Básico, Medio y Superior?",
         "Grado D.", "LO 3/2022"),
        ("¿Qué es el Grado E?",
         "Los cursos de especialización.", "LO 3/2022"),
        ("¿Qué ley es la «ley paraguas» de la FP?",
         "La LO 3/2022, de 31 de marzo, de ordenación e integración de la Formación Profesional.", "LO 3/2022"),
        ("¿Qué hace el RD 659/2023?",
         "Desarrolla la ordenación del Sistema de Formación Profesional.", "RD 659/2023"),
        ("¿Qué fija el RD 278/2023?",
         "El calendario de implantación del Sistema de FP.", "RD 278/2023"),
        ("¿Qué reales decretos fijan las enseñanzas mínimas?",
         "RD 497/2024 (especialización), 498/2024 (básico), 499/2024 (medio) y 500/2024 (superior).", "RD 497-500/2024"),
        ("¿Qué norma regula la evaluación en la Comunitat Valenciana?",
         "La Orden 8/2025, modificada por la Orden 5/2026.", "Orden 8/2025"),
        ("¿Qué norma regula el acceso, la admisión y la matrícula?",
         "La Orden 10/2024.", "Orden 10/2024"),
        ("¿Qué normativa se sigue para los ciclos LOGSE?",
         "Orden 78/2010 (ordenación) y Orden 79/2010 (evaluación).", "Orden 78/2010"),
        ("Excepción a la implantación LFP en 2026-27: ¿quién puede seguir con el plan anterior?",
         "El alumnado que en 2025-26 cursó terceros cursos LOE (nocturnos o de tres años) o segundos de doble titulación y en 2026-27 tenga módulos pendientes, incluida la FCT.", "Instrucciones 2026-27 §9.2"),
    ],
    quiz=[
        ("¿Cuál de estos NO es un grado del sistema de FP?",
         ["Grado A: acreditaciones parciales de competencia", "Grado B: certificados de competencia profesional", "Grado F: máster profesional", "Grado E: cursos de especialización"], 2,
         "Los grados son A, B, C, D y E.", "LO 3/2022"),
        ("Los ciclos de Técnico Básico, Técnico y Técnico Superior son…",
         ["Grado A", "Grado C", "Grado D", "Grado E"], 2,
         "El Grado D son los títulos de Técnico Básico, Técnico y Técnico Superior.", "LO 3/2022"),
        ("¿Qué norma desarrolla la ordenación del Sistema de FP?",
         ["LO 3/2022", "RD 659/2023", "Orden 8/2025", "RD 278/2023"], 1,
         "El RD 659/2023 desarrolla la ordenación; el RD 278/2023 fija el calendario.", "RD 659/2023"),
        ("¿Qué norma modificó la Orden 8/2025 de evaluación?",
         ["La Orden 5/2026", "El Decreto 95/2026", "La Orden 10/2024", "La Orden 79/2010"], 0,
         "La Orden 8/2025 fue modificada por la Orden 5/2026.", "Orden 8/2025"),
        ("Los cursos de especialización son el Grado…",
         ["A", "C", "D", "E"], 3,
         "Los cursos de especialización son el Grado E.", "LO 3/2022"),
        ("En 2026-27, ¿qué ciclos siguen rigiéndose por la normativa anterior?",
         ["Todos los ciclos LFP", "Los ciclos LOGSE", "Solo los de Grado Básico", "Ninguno"], 1,
         "Toda la oferta va por LFP excepto los ciclos LOGSE.", "Instrucciones 2026-27 §9.2"),
    ],
))

# ===========================================================================
# MÓDULO 2 · ARQUITECTURA NORMATIVA
# ===========================================================================
MODULES.append(dict(
    id="m2", title="Arquitectura normativa y fuentes", tagline="Jerarquía, BOE/DOGV, cómo citar y las 24 normas del curso.",
    objetivos=[
        "Ordenar las normas por rango jurídico de mayor a menor.",
        "Saber si una materia es estatal (BOE) o autonómica (DOGV).",
        "Citar correctamente una norma y un artículo.",
    ],
    lesson="""
<h3>1. ¿Quién manda? Jerarquía normativa</h3>
<p>Una norma de rango inferior no puede contradecir a otra de rango superior. Este es el orden, de mayor a menor rango:</p>
<table>
<tr><th>Nivel</th><th>Rango</th><th>Ejemplos del curso</th></tr>
<tr><td>1</td><td>Ley Orgánica</td><td>LO 3/2022</td></tr>
<tr><td>2</td><td>Ley ordinaria</td><td>Ley 39/2015</td></tr>
<tr><td>3</td><td>Real Decreto-Ley</td><td>—</td></tr>
<tr><td>4</td><td>Real Decreto Legislativo</td><td>—</td></tr>
<tr><td>5</td><td>Real Decreto / Decreto</td><td>RD 659/2023, Decretos 114/117/95/74/…</td></tr>
<tr><td>6</td><td>Orden</td><td>Orden 8/2025, Orden 10/2024, 12/2022, 5/2022…</td></tr>
<tr><td>7</td><td>Resolución / Instrucciones / Circular</td><td>Instrucciones 2026-27</td></tr>
</table>
<div class="callout info"><b>Regla de oro:</b> <b>ley → real decreto / decreto → orden → instrucciones.</b> Cuanto más abajo, más concreta y más fácil de cambiar.</div>

<h3>2. Estatal vs autonómico</h3>
<ul>
<li><b>Estatal (BOE):</b> bases, ordenación del sistema, enseñanzas mínimas, títulos, convalidaciones generales.</li>
<li><b>Autonómico (DOGV):</b> desarrollo del currículo, admisión y matrícula, evaluación, organización de centros, instrucciones de curso.</li>
</ul>
<p>Por eso las reglas «de números» (15%, 240 h, convocatorias…) suelen estar en normativa <b>autonómica</b>: Órdenes e Instrucciones de la Conselleria.</p>

<h3>3. Cómo se cita</h3>
<ul>
<li>Norma: <b>«LO 3/2022»</b>, <b>«RD 659/2023»</b>, <b>«Orden 8/2025»</b>, <b>«Decreto 114/2025»</b>.</li>
<li>Parte concreta: <b>«Orden 8/2025 art. 14»</b>, <b>«RD 659/2023 art. 125»</b>, <b>«Instrucciones 2026-27 §9.6»</b>.</li>
<li>El símbolo <b>§</b> se usa para los apartados numerados de las Instrucciones de curso.</li>
</ul>

<h3>4. Vigencia y derogación</h3>
<ul>
<li>La norma posterior deroga la anterior de igual o inferior rango.</li>
<li>Caso típico: la <b>Orden 8/2025</b> deroga la <b>Orden 79/2010</b> <b>salvo</b> para ciclos LOGSE.</li>
<li>Un <b>texto consolidado</b> incluye las modificaciones posteriores (ojo: puede traer apéndices de «análisis jurídico» que no son articulado).</li>
</ul>
    """,
    trucos=[
        "<b>LE-RE-DE-OR-RE:</b> LEy Orgánica → Real decreto → DEcreto → ORden → REsolución/Instrucciones.",
        "Estatal = BOE = bases y títulos. Autonómico = DOGV = currículo, matrícula, evaluación.",
        "«§» solo en Instrucciones; «art.» para leyes, reales decretos, decretos y órdenes.",
    ],
    trampas=[
        "Una Orden <b>no puede</b> contradecir un Real Decreto ni una Ley.",
        "Las <b>Instrucciones</b> son el rango más bajo: cambian cada curso, pero siempre dentro de lo que dicen las Órdenes.",
    ],
    normas=[("Normativa FP (Conselleria)", "https://ceice.gva.es/es/web/formacion-profesional/normativa-sobre-ordenacion-y-organizacion-academica-de-los-ciclos-formativos")],
    cards=[
        ("Ordena de mayor a menor rango: Orden, Ley Orgánica, Real Decreto, Resolución/Instrucciones.",
         "Ley Orgánica > Real Decreto > Orden > Resolución/Instrucciones.", "Jerarquía"),
        ("¿Dónde se publica la normativa estatal y dónde la autonómica?",
         "Estatal en el BOE; autonómica en el DOGV.", "Fuentes"),
        ("¿Qué normativa suele contener las reglas «de números» de admisión, evaluación y convocatorias?",
         "La autonómica: Órdenes e Instrucciones de la Conselleria (DOGV).", "Fuentes"),
        ("¿Cómo se cita un apartado numerado de las Instrucciones de curso?",
         "Con el símbolo §, por ejemplo «Instrucciones 2026-27 §9.6».", "Cita"),
        ("¿Qué relación tiene la Orden 8/2025 con la Orden 79/2010?",
         "La Orden 8/2025 deroga la Orden 79/2010, salvo para ciclos LOGSE.", "Orden 8/2025"),
        ("¿Puede una Orden contradecir un Real Decreto?",
         "No: rigen la jerarquía normativa y el principio de competencia.", "Jerarquía"),
        ("¿Qué es un texto consolidado?",
         "El texto de una norma con sus modificaciones incorporadas; puede incluir apéndices (análisis jurídico) que no forman parte del articulado.", "Fuentes"),
        ("¿Qué rango tiene una Resolución o Instrucción de curso?",
         "El más bajo de la escala (nivel 7): concreta cada curso lo previsto en normas superiores.", "Jerarquía"),
    ],
    quiz=[
        ("¿Cuál es el rango correcto de mayor a menor?",
         ["Orden > Real Decreto > Ley Orgánica", "Ley Orgánica > Real Decreto > Orden > Instrucciones", "Instrucciones > Orden > Ley", "Real Decreto > Ley Orgánica > Orden"], 1,
         "Ley Orgánica → Real Decreto → Orden → Resolución/Instrucciones.", "Jerarquía"),
        ("La admisión y matrícula en FP de la Comunitat se regula por…",
         ["Una ley orgánica estatal", "Una orden autonómica (Orden 10/2024)", "Un real decreto-ley", "Una directiva europea"], 1,
         "La Orden 10/2024 (DOGV) regula acceso, admisión y matrícula.", "Orden 10/2024"),
        ("El símbolo § en este curso sirve para citar…",
         ["Artículos de leyes", "Apartados numerados de las Instrucciones de curso", "Anexos", "Disposiciones"], 1,
         "§ se usa para los apartados (1, 2, 9.6…) de las Instrucciones 2026-27.", "Cita"),
        ("¿Qué norma deroga la Orden 79/2010 salvo para LOGSE?",
         ["La Orden 8/2025", "El Decreto 114/2025", "La LO 3/2022", "El RD 278/2023"], 0,
         "La Orden 8/2025 deja la Orden 79/2010 solo para ciclos LOGSE.", "Orden 8/2025"),
        ("Señala el nivel 5 de la jerarquía:",
         ["Orden", "Real Decreto / Decreto", "Ley ordinaria", "Instrucciones"], 1,
         "El nivel 5 son el Real Decreto y el Decreto.", "Jerarquía"),
    ],
))

# ===========================================================================
# MÓDULO 3 · ACCESO, ADMISIÓN Y MATRÍCULA
# ===========================================================================
MODULES.append(dict(
    id="m3", title="Acceso, admisión y matrícula", tagline="Compatibilidades, plazas, oferta modular y grados C→D.",
    objetivos=[
        "Saber cuándo dos matrículas son compatibles.",
        "Recordar las fechas de la oferta modular 2026-27.",
        "Explicar el paso de los grados C al Grado D.",
    ],
    lesson="""
<h3>1. ¿Puedo estar matriculado en dos sitios a la vez?</h3>
<ul>
<li>La matrícula presencial en un ciclo <b>es compatible</b> con otro ciclo, curso u otras enseñanzas <b>si hay compatibilidad de horarios</b>.</li>
<li><b>No</b> se puede simultanear el <b>mismo módulo</b> en varios regímenes (presencial, semipresencial de oferta completa u oferta modular).</li>
<li>La matrícula en un ciclo <b>no es compatible</b> con las pruebas para obtener el título del <b>mismo módulo</b> el mismo año (salvo anulación previa).</li>
<li>Solo se puede estar matriculado de un <b>mismo ciclo en un único centro, régimen y modalidad</b>.</li>
</ul>

<h3>2. Una plaza por oferta completa</h3>
<ul>
<li>En un mismo curso <b>no</b> se puede obtener plaza en oferta completa en más de un ciclo (salvo módulos coincidentes).</li>
<li>Se puede pedir admisión en otros ciclos <b>si hay vacantes</b> tras el periodo de matrícula, renunciando antes a la plaza adjudicada.</li>
<li>Es compatible obtener plaza en oferta completa y, complementariamente, en <b>oferta modular</b>.</li>
</ul>

<h3>3. Oferta modular (opción A): fechas clave 2026-27</h3>
<table>
<tr><th>Trámite</th><th>Fecha</th></tr>
<tr><td>Publicación del listado de vacantes por módulo</td><td><b>Antes del 15 de octubre de 2026</b></td></tr>
<tr><td>Matrícula</td><td><b>Antes del 11 de diciembre de 2026</b></td></tr>
<tr><td>Después</td><td>La admisión sigue abierta con evaluación continua e <b>informe favorable</b> de la Comisión Sectorial de escolarización</td></tr>
</table>

<h3>4. De los grados C al Grado D</h3>
<ul>
<li>Quien haya superado uno o varios <b>grados C</b> integrados en un ciclo formativo puede acceder al ciclo para completar el <b>grado D</b>.</li>
<li>Se pueden aumentar plazas <b>hasta un 10%</b>, con aprobación de la comisión de escolarización sectorial de FP.</li>
</ul>
<div class="callout tip">La regulación completa está en la <b>Orden 10/2024</b> y en el portal de FP (sección Alumnado).</div>
    """,
    trucos=[
        "<b>Compatible:</b> presencial + presencial (con horarios) y oferta completa + modular.",
        "<b>Incompatible:</b> el mismo módulo en dos regímenes; y el mismo ciclo en dos centros/régimen/modalidad.",
        "Fechas oferta modular: <b>15 de octubre</b> (vacantes) y <b>11 de diciembre</b> (matrícula).",
    ],
    trampas=[
        "Oferta completa: <b>una sola plaza</b>. Pero sí puedes <b>añadir</b> oferta modular.",
        "El 10% de ampliación de plazas es para quienes vienen de <b>grados C</b> y lo aprueba la comisión sectorial.",
    ],
    normas=[("Orden 10/2024 (DOGV)", "https://dogv.gva.es/datos/2024/05/14/pdf/2024_4272.pdf")],
    cards=[
        ("¿Cuándo son compatibles dos matrículas presenciales?",
         "Cuando hay compatibilidad de horarios.", "Instrucciones 2026-27 §2"),
        ("¿Se puede cursar el mismo módulo en dos regímenes a la vez?",
         "No: es incompatible simultanear el mismo módulo en presencial, semipresencial de oferta completa u oferta modular.", "Instrucciones 2026-27 §2"),
        ("¿Se puede estar matriculado del mismo ciclo en dos centros?",
         "No: un mismo ciclo solo en un centro, régimen y modalidad.", "Instrucciones 2026-27 §2"),
        ("¿Cuántas plazas de oferta completa se pueden obtener por curso?",
         "Una, salvo módulos coincidentes.", "Instrucciones 2026-27 §2.6"),
        ("¿Es compatible la oferta completa con la oferta modular?",
         "Sí, complementariamente.", "Instrucciones 2026-27 §2.6"),
        ("¿Cuándo se publican las vacantes de la oferta modular 2026-27?",
         "Antes del 15 de octubre de 2026.", "Instrucciones 2026-27 §2.7"),
        ("¿Hasta cuándo se puede formalizar la matrícula de oferta modular 2026-27?",
         "Antes del 11 de diciembre de 2026.", "Instrucciones 2026-27 §2.7"),
        ("¿Qué se exige para matricularse en oferta modular después del plazo?",
         "Informe favorable de la Comisión Sectorial de escolarización, con evaluación continua.", "Instrucciones 2026-27 §2.7"),
        ("¿Se pueden ampliar plazas para quien viene de un grado C?",
         "Sí, hasta un 10%, con aprobación de la comisión de escolarización sectorial de FP.", "Instrucciones 2026-27 §2.8"),
    ],
    quiz=[
        ("Dos matrículas presenciales en ciclos distintos son…",
         ["Siempre incompatibles", "Compatibles si hay compatibilidad de horarios", "Compatibles solo en Grado Básico", "Posibles solo por la tarde"], 1,
         "La compatibilidad depende de los horarios.", "Instrucciones 2026-27 §2"),
        ("¿Qué NO se puede simultanear?",
         ["Dos ciclos distintos", "El mismo módulo en varios regímenes", "Oferta completa y modular", "FP y otras enseñanzas"], 1,
         "El mismo módulo no puede cursarse en varios regímenes.", "Instrucciones 2026-27 §2"),
        ("Las vacantes de oferta modular 2026-27 se publican…",
         ["Antes del 15 de octubre de 2026", "Antes del 11 de diciembre de 2026", "En septiembre", "En enero"], 0,
         "Vacantes antes del 15/10/2026; matrícula antes del 11/12/2026.", "Instrucciones 2026-27 §2.7"),
        ("La ampliación de plazas por venir de un grado C es de hasta…",
         ["5%", "10%", "20%", "25%"], 1,
         "Hasta un 10%, con aprobación de la comisión sectorial.", "Instrucciones 2026-27 §2.8"),
        ("¿Con qué es compatible obtener plaza en oferta completa?",
         ["Con otra oferta completa", "Con oferta modular", "Con pruebas libres del mismo módulo", "Con nada"], 1,
         "Oferta completa + oferta modular sí; dos ofertas completas no.", "Instrucciones 2026-27 §2.6"),
        ("¿Qué norma regula el acceso, la admisión y la matrícula?",
         ["Orden 8/2025", "Orden 10/2024", "Decreto 114/2025", "RD 278/2023"], 1,
         "La Orden 10/2024.", "Orden 10/2024"),
    ],
))

# ===========================================================================
# MÓDULO 4 · ANULACIÓN Y PÉRDIDA DE MATRÍCULA
# ===========================================================================
MODULES.append(dict(
    id="m4", title="Anulación y pérdida de matrícula", tagline="Anexo I, cómputo de matrícula, 15% / 10 días, faltas y 85%.",
    objetivos=[
        "Diferenciar anulación de matrícula y renuncia a convocatoria.",
        "Memorizar los umbrales de inasistencia (15%, 10, 5%, 8).",
        "Saber qué faltas no cuentan.",
    ],
    lesson="""
<div class="callout trap"><b>Importante.</b> Anular o perder la matrícula implica <b>perder la plaza del curso y de todos los módulos</b>. Para continuar hay que volver a participar en la admisión.</div>

<h3>1. Anulación a instancia de la persona interesada</h3>
<ul>
<li>Se solicita con el modelo del <b>anexo I</b> de las instrucciones, ante la dirección del centro.</li>
<li><b>Computa como matrícula consumida</b>, salvo si se pide:
  <ul><li>antes del mes de <b>enero</b> del curso, o</li>
      <li>antes de iniciar el <b>tercer trimestre</b>, por alguno de los motivos justificados de <b>renuncia a convocatoria</b>.</li></ul>
</li>
<li>La dirección resuelve en el plazo de <b>1 mes</b>; el <b>silencio es estimatorio</b>.</li>
<li>Si se concede la anulación del curso (o de todos los módulos en semipresencial): <b>no computan las convocatorias</b>, pero se pierde la reserva de plaza.</li>
<li>La anulación <b>es independiente</b> de la renuncia a convocatorias concretas.</li>
</ul>

<h3>2. Pérdida de matrícula por inasistencia</h3>
<ul>
<li>Se pierde la matrícula al alcanzar el <b>15% de horas de inasistencia por faltas injustificadas</b> del curso matriculado, o por <b>no asistir 10 días lectivos consecutivos</b>.</li>
<li>En oferta modular o régimen no presencial, el <b>15% se calcula sobre el módulo</b>.</li>
<li>No se cuentan como base los módulos pendientes de cursos anteriores, los convalidados ni los renunciados.</li>
<li>El centro avisa de la <b>posibilidad</b> de pérdida al llegar al <b>5%</b> o a <b>8 días lectivos consecutivos</b>.</li>
<li>La resolución se notifica por <b>ITACA / Web Familia</b> u otro medio válido; cabe recurso de alzada en <b>1 mes</b>.</li>
</ul>

<h3>3. Faltas que no cuentan (justificadas)</h3>
<ul>
<li>Ausencias por <b>enfermedad o accidente</b> del alumnado.</li>
<li>Atención a <b>familiares de primer grado</b> de consanguinidad.</li>
<li><b>Violencia de género</b>, violencia contra menores o <b>acoso escolar</b>.</li>
<li>Otras circunstancias individualizadas de <b>fuerza mayor</b> valoradas por la dirección y recogidas en las normas del centro.</li>
</ul>

<h3>4. Asistencia mínima exigible</h3>
<ul>
<li><b>Presencial</b>: presencialidad mínima del <b>85%</b>.</li>
<li><b>Semipresencial</b>: mantener la matrícula exige tutorías colectivas, actividades de autoaprendizaje, acceso regular al aula virtual y participación en foros; al menos el <b>85%</b> de la presencialidad exigible en módulos asociados a estándares.</li>
<li><b>Grado Básico</b>: si se anula por inasistencia y el alumnado está en edad de escolarización obligatoria, se le da plaza de oficio en un centro de ESO con vacantes.</li>
</ul>
    """,
    trucos=[
        "<b>15 / 10 — 5 / 8:</b> pérdida de matrícula al <b>15%</b> o <b>10 días</b>; aviso al <b>5%</b> o <b>8 días</b>.",
        "<b>85% = 15%.</b> Presencialidad mínima 85% ⇔ puedes faltar 15%.",
        "Anular = dejar el ciclo (anexo I). Renunciar = solo a una convocatoria. ¡No son lo mismo!",
        "Anulación: resuelve en <b>1 mes</b> con <b>silencio estimatorio</b> (positivo).",
    ],
    trampas=[
        "El <b>15% de matrícula</b> (avisos 5% y 8 días) NO es el mismo que el <b>15% de evaluación continua</b> (aviso 10%).",
        "En modular o no presencial, el 15% se calcula <b>sobre el módulo</b>, no sobre el curso.",
        "No cuentan como base los módulos <b>pendientes, convalidados ni renunciados</b>.",
    ],
    normas=[("Orden 8/2025 (DOGV)", "https://dogv.gva.es/datos/2025/04/30/pdf/2025_13083.pdf")],
    cards=[
        ("¿Qué anexo se usa para solicitar la anulación de matrícula?",
         "El anexo I de las Instrucciones 2026-27.", "Instrucciones 2026-27 §8.1"),
        ("¿Cuándo NO computa como matrícula consumida la anulación?",
         "Si se pide antes de enero, o antes de iniciar el tercer trimestre por motivos justificados de renuncia a convocatoria.", "Instrucciones 2026-27 §8.1"),
        ("¿En qué plazo resuelve la dirección una anulación y qué efecto tiene el silencio?",
         "En 1 mes; el silencio es estimatorio (se entiende concedida).", "Instrucciones 2026-27 §8.1"),
        ("¿Cuánta inasistencia injustificada hace perder la matrícula?",
         "El 15% de las horas del curso matriculado, o no asistir 10 días lectivos consecutivos.", "Instrucciones 2026-27 §8.2-8.3"),
        ("¿Sobre qué se calcula el 15% en oferta modular o no presencial?",
         "Sobre el módulo.", "Instrucciones 2026-27 §8.2"),
        ("¿Cuándo avisa el centro de la posibilidad de pérdida de matrícula?",
         "Al llegar al 5% de inasistencia o a 8 días lectivos consecutivos.", "Instrucciones 2026-27 §8.2"),
        ("Cita tres tipos de faltas justificadas que no cuentan.",
         "Enfermedad o accidente; atención a familiares de primer grado; violencia de género, violencia contra menores o acoso escolar (y fuerza mayor).", "Instrucciones 2026-27 §8.2"),
        ("¿Cuál es la presencialidad mínima en régimen presencial?",
         "El 85%.", "Instrucciones 2026-27 §8.4"),
        ("¿Qué pasa en Grado Básico si se anula la matrícula por inasistencia y el alumno está en edad obligatoria?",
         "Se le proporciona plaza de oficio en un centro de ESO con vacantes.", "Instrucciones 2026-27 §8.4-8.5"),
        ("¿Cómo se notifica la pérdida de matrícula y qué recurso cabe?",
         "Por ITACA/Web Familia u otro medio válido; cabe recurso de alzada en 1 mes.", "Instrucciones 2026-27 §8.3"),
    ],
    quiz=[
        ("Para anular la matrícula se presenta…",
         ["El anexo I", "El anexo III", "El anexo IV", "Una instancia genérica"], 0,
         "El anexo I es la solicitud de anulación de matrícula.", "Instrucciones 2026-27 §8.1"),
        ("La pérdida de matrícula por faltas injustificadas se produce al…",
         ["10% u 8 días", "15% o 10 días lectivos consecutivos", "20% o 15 días", "50%"], 1,
         "15% de horas o 10 días lectivos consecutivos.", "Instrucciones 2026-27 §8.2"),
        ("El aviso de posible pérdida de matrícula se da al…",
         ["5% u 8 días consecutivos", "10% o 10 días", "15% u 8 días", "No hay aviso"], 0,
         "Aviso al 5% o a 8 días lectivos consecutivos.", "Instrucciones 2026-27 §8.2"),
        ("¿Cuál es la presencialidad mínima exigible?",
         ["75%", "80%", "85%", "90%"], 2,
         "El 85% en régimen presencial; en semipresencial, el 85% de la presencialidad exigible.", "Instrucciones 2026-27 §8.4"),
        ("¿Cuál de estas NO es falta justificada?",
         ["Enfermedad del alumnado", "Atención a familiares de primer grado", "Ir de viaje con amigos", "Violencia de género"], 2,
         "Solo cuentan enfermedad/accidente, familiares de 1.er grado, violencia/acoso y fuerza mayor.", "Instrucciones 2026-27 §8.2"),
        ("El plazo para resolver la anulación de matrícula y su silencio son…",
         ["1 mes / estimatorio", "2 meses / desestimatorio", "10 días / estimatorio", "1 mes / desestimatorio"], 0,
         "1 mes y silencio estimatorio.", "Instrucciones 2026-27 §8.1"),
        ("Anular la matrícula y renunciar a una convocatoria…",
         ["Son lo mismo", "Son cosas distintas: anular deja el ciclo; renunciar es solo a una convocatoria", "Solo existen en LOGSE", "Las dos requieren anexo IV"], 1,
         "La anulación es independiente de la renuncia a convocatorias concretas.", "Instrucciones 2026-27 §8.1"),
    ],
))

# ===========================================================================
# MÓDULO 5 · EVALUACIÓN
# ===========================================================================
MODULES.append(dict(
    id="m5", title="Evaluación", tagline="Evaluación continua, sesiones, FE y pérdida de evaluación continua.",
    objetivos=[
        "Definir evaluación continua, formativa e integradora.",
        "Ordenar las sesiones de evaluación.",
        "Distinguir la pérdida de evaluación continua de la pérdida de matrícula.",
    ],
    lesson="""
<h3>1. Cómo se evalúa</h3>
<ul>
<li>Ciclos LFP: <b>RD 659/2023</b> + <b>Orden 8/2025</b> (modificada por la Orden 5/2026).</li>
<li>Ciclos LOGSE: <b>Orden 79/2010</b>.</li>
<li>Evaluación <b>continua, formativa e integradora</b>, centrada en los <b>resultados de aprendizaje (RA)</b> y criterios de evaluación.</li>
<li>Derecho a una <b>evaluación objetiva</b>; el alumnado ha de conocer los criterios con antelación.</li>
<li>En semipresencial y virtual, la evaluación final requiere <b>pruebas presenciales</b>.</li>
</ul>

<h3>2. Cuándo se evalúa (sesiones)</h3>
<table>
<tr><th>Sesión</th><th>Momento</th></tr>
<tr><td><b>Inicial</b></td><td>Antes de terminar el 2.º mes lectivo (<b>no califica</b>)</td></tr>
<tr><td><b>Parciales</b></td><td>Mínimo 2: final del 1.er y del 2.º trimestre</td></tr>
<tr><td><b>Ordinaria</b></td><td>Al finalizar las actividades lectivas del curso</td></tr>
<tr><td><b>Extraordinaria</b></td><td>Después de la ordinaria (puede ser en el curso siguiente)</td></tr>
</table>

<h3>3. Evaluación final y formación en empresa</h3>
<ul>
<li>La evaluación final comprende <b>todos los módulos</b>, incluidos los RA cursados en la empresa.</li>
<li>La calificación de cada módulo es responsabilidad del <b>docente</b> que lo imparte; con <b>personal experto</b>, la evaluación va acompañada de la firma del tutor o tutora del grupo.</li>
<li>Si la FE no finaliza con éxito, el equipo docente decide módulo a módulo según el grado de consecución de los RA.</li>
</ul>

<h3>4. Pérdida del derecho a la evaluación continua</h3>
<ul>
<li>Se pierde <b>por módulo</b> al superar el <b>15% de inasistencia</b> a las actividades de formación.</li>
<li>Cada docente comunica a la tutoría la posible pérdida cuando se alcanza el <b>10%</b> de inasistencia.</li>
<li>En <b>Grado Básico</b> solo puede perderse en módulos profesionales; los <b>ámbitos</b> se rigen por la normativa de ESO (Decreto 107/2022) y no contemplan esa pérdida.</li>
</ul>

<h3>5. Reclamaciones y acceso a la universidad</h3>
<ul>
<li>Reclamaciones y garantías: <b>Orden 32/2011</b>, título IV del <b>Decreto 107/2022</b> y <b>Ley 39/2015</b>.</li>
<li>Para quien se presenta a la <b>PAU</b>, el equipo docente <b>adelanta</b> la evaluación final para que las calificaciones estén en ITACA en plazo.</li>
</ul>
    """,
    trucos=[
        "Sesiones en orden: <b>I-P-O-E</b> (Inicial, Parciales, Ordinaria, Extraordinaria).",
        "Evaluación continua: <b>15%</b> con aviso al <b>10%</b>.",
        "Inicial <b>no califica</b>; la extraordinaria puede caer ya en el curso siguiente.",
    ],
    trampas=[
        "Pérdida de matrícula: aviso <b>5%</b>. Pérdida de evaluación continua: aviso <b>10%</b>. ¡No los mezcles!",
        "En Grado Básico, los <b>ámbitos</b> (ESO) no pierden evaluación continua; solo los módulos profesionales.",
        "La evaluación final incluye los RA hechos en la <b>empresa</b>.",
    ],
    normas=[("Orden 8/2025 (DOGV)", "https://dogv.gva.es/datos/2025/04/30/pdf/2025_13083.pdf"),
            ("Evaluación FP (Conselleria)", "https://ceice.gva.es/es/web/formacion-profesional/avaluacio")],
    cards=[
        ("¿Cómo es la evaluación en LFP?",
         "Continua, formativa e integradora, centrada en resultados de aprendizaje (RA) y criterios de evaluación.", "Orden 8/2025 arts. 2-4"),
        ("¿Qué normativa regula la evaluación de ciclos LFP en la Comunitat?",
         "La Orden 8/2025, modificada por la Orden 5/2026.", "Instrucciones 2026-27 §9"),
        ("¿Qué normativa rige la evaluación de ciclos LOGSE?",
         "La Orden 79/2010.", "Orden 79/2010"),
        ("¿Cuándo es la sesión de evaluación inicial y califica?",
         "Antes de terminar el 2.º mes lectivo; NO califica.", "Orden 8/2025 art. 12"),
        ("¿Cuántas sesiones parciales hay como mínimo?",
         "Dos: al final del 1.er y del 2.º trimestre.", "Orden 8/2025 art. 12"),
        ("¿La evaluación final incluye lo aprendido en la empresa?",
         "Sí, comprende todos los módulos, incluidos los RA cursados en la empresa.", "Instrucciones 2026-27 §9.6"),
        ("¿Quién califica un módulo impartido por personal experto?",
         "El docente responsable, con la firma del tutor o tutora del grupo.", "Orden 8/2025 art. 2.5"),
        ("¿Cuánta inasistencia hace perder la evaluación continua de un módulo?",
         "Superar el 15% de inasistencia a las actividades de formación del módulo.", "Orden 8/2025 art. 7"),
        ("¿Cuándo se avisa de la posible pérdida de evaluación continua?",
         "Al alcanzar el 10% de inasistencia.", "Orden 8/2025 art. 7"),
        ("¿En qué asignaturas de Grado Básico NO se pierde la evaluación continua?",
         "En los ámbitos, que se rigen por la normativa de ESO (Decreto 107/2022).", "Instrucciones 2026-27 §9.5"),
        ("En semipresencial y virtual, ¿qué exige la evaluación final?",
         "Pruebas presenciales.", "Instrucciones 2026-27 §9"),
        ("¿Qué se hace con la PAU y las calificaciones?",
         "El equipo docente adelanta la evaluación final para que las notas estén en ITACA a tiempo.", "Instrucciones 2026-27 §9.3-9.4"),
    ],
    quiz=[
        ("La evaluación en LFP es…",
         ["Solo final", "Continua, formativa e integradora", "Únicamente con exámenes", "Automática"], 1,
         "Continua, formativa e integradora, basada en los RA.", "Orden 8/2025"),
        ("La sesión de evaluación inicial…",
         ["Califica el primer trimestre", "No califica y es antes del 2.º mes lectivo", "Sustituye a los parciales", "Es en junio"], 1,
         "La inicial no califica y se celebra antes de terminar el 2.º mes lectivo.", "Orden 8/2025 art. 12"),
        ("La pérdida de evaluación continua de un módulo se produce al…",
         ["10% de inasistencia", "15% de inasistencia", "20% de inasistencia", "No existe"], 1,
         "Al superar el 15%; el aviso es al 10%.", "Orden 8/2025 art. 7"),
        ("En Grado Básico, ¿dónde no se pierde la evaluación continua?",
         ["En los módulos profesionales", "En los ámbitos", "En ninguno", "En la FE"], 1,
         "Los ámbitos siguen la normativa de ESO y no contemplan esa pérdida.", "Instrucciones 2026-27 §9.5"),
        ("¿Qué exige la evaluación final en semipresencial y virtual?",
         ["Nada especial", "Pruebas presenciales", "Solo trabajos", "Una entrevista"], 1,
         "La evaluación final requiere pruebas presenciales.", "Instrucciones 2026-27 §9"),
        ("Si la FE no finaliza con éxito, ¿quién decide?",
         ["La empresa", "El equipo docente, módulo a módulo", "La Inspección", "El tutor de empresa solo"], 1,
         "El equipo docente decide módulo a módulo según la consecución de los RA.", "Instrucciones 2026-27 §9.6"),
    ],
))

# ===========================================================================
# MÓDULO 6 · CONVOCATORIAS Y RENUNCIAS
# ===========================================================================
MODULES.append(dict(
    id="m6", title="Convocatorias, renuncias y documentos", tagline="4/2 convocatorias, permanencia, gracia y documentos oficiales.",
    objetivos=[
        "Recordar cuántas convocatorias hay en Grado D y E.",
        "Explicar la renuncia y la convocatoria de gracia.",
        "Identificar los documentos oficiales de evaluación.",
    ],
    lesson="""
<h3>1. Cuántas convocatorias tengo</h3>
<ul>
<li><b>Grado D</b>: máximo <b>4 convocatorias por módulo</b> (2 por curso académico).</li>
<li><b>Grado E</b> (cursos de especialización): máximo <b>2 convocatorias por módulo</b>.</li>
<li><b>Permanencia</b>: como máximo el <b>doble de cursos</b> del ciclo en presencial; hasta <b>6 cursos consecutivos</b> en modalidad virtual.</li>
</ul>

<h3>2. Cuándo se celebran</h3>
<ul>
<li><b>Ordinaria</b>: al finalizar el tercer trimestre del 1.º o 2.º curso.</li>
<li><b>Segunda convocatoria</b>: tras la primera, para módulos pendientes de 1.º; al final del tercer trimestre, para pendientes de 2.º.</li>
<li><b>Extraordinaria</b>: quien no supera un módulo en la primera convocatoria tiene una extraordinaria en el mismo curso, con <b>programa formativo específico</b>.</li>
</ul>

<h3>3. Renuncia a convocatoria (no agotar)</h3>
<ul>
<li>Se puede renunciar a la <b>convocatoria ordinaria</b> justificando: <b>enfermedad</b> acreditada, <b>conciliación laboral</b> u otras circunstancias valoradas por la dirección.</li>
<li>Plazo: <b>antes de 10 días hábiles</b> a la evaluación correspondiente.</li>
<li>Resuelve la dirección en un máximo de <b>10 días hábiles</b>; cabe recurso de alzada.</li>
<li>Si no se supera la ordinaria, el profesorado informa si se puede afrontar la extraordinaria; si no, se puede renunciar para <b>no agotar</b> convocatorias.</li>
</ul>

<h3>4. Si agoto las convocatorias</h3>
<ul>
<li><b>Pruebas libres</b> para la obtención del título (convocatoria anual).</li>
<li><b>Convocatoria extraordinaria de gracia</b>.</li>
<li>Cursar los módulos no superados en <b>oferta modular</b>.</li>
</ul>

<h3>5. Convocatoria extraordinaria de gracia</h3>
<ul>
<li>Para quien ha agotado las convocatorias por <b>enfermedad o discapacidad</b> acreditada, o <b>situaciones sobrevenidas</b>.</li>
<li>Se solicita a la <b>Dirección Territorial</b>; resuelve en un plazo no superior a <b>2 meses</b>.</li>
<li>Se concede <b>una sola vez por módulo</b> y, una vez autorizada, <b>no se puede renunciar ni anular</b> matrícula.</li>
</ul>

<h3>6. Documentos oficiales</h3>
<ul>
<li><b>Expediente académico</b>, <b>actas de evaluación</b> y <b>certificado académico oficial</b>.</li>
<li>Los custodian los centros públicos; en centros privados se supervisan y visan a través del centro público de adscripción.</li>
<li>Las <b>unidades formativas</b> son certificables; superar todas las de un módulo da derecho a la certificación del módulo (válida en todo el Estado).</li>
</ul>
    """,
    trucos=[
        "<b>D = 4, E = 2.</b> El doble de cursos para permanecer; <b>6</b> seguidos en virtual.",
        "<b>10 días hábiles</b> para renunciar (y para que resuelvan). Gracia: <b>2 meses</b> y <b>1 vez</b>.",
        "Agotado: <b>libres · gracia · modular</b>.",
    ],
    trampas=[
        "La gracia se concede <b>una vez por módulo</b> y después es <b>irrenunciable</b>.",
        "Renuncia a convocatoria ≠ anulación de matrícula.",
        "El máximo de convocatorias es por <b>módulo</b>, no por curso.",
    ],
    normas=[("Orden 8/2025 (DOGV)", "https://dogv.gva.es/datos/2025/04/30/pdf/2025_13083.pdf")],
    cards=[
        ("¿Cuántas convocatorias por módulo hay en Grado D?",
         "Máximo 4 (2 por curso académico).", "Instrucciones 2026-27 §12"),
        ("¿Cuántas convocatorias por módulo hay en Grado E?",
         "Máximo 2.", "Instrucciones 2026-27 §12"),
        ("¿Cuál es el límite de permanencia en un ciclo?",
         "El doble de cursos del ciclo en presencial; hasta 6 cursos consecutivos en modalidad virtual.", "Instrucciones 2026-27 §12"),
        ("¿Cómo se llama la convocatoria por suspender un módulo en la primera?",
         "Convocatoria extraordinaria, con programa formativo específico.", "Instrucciones 2026-27 §12.3-12.4"),
        ("¿Qué motivos permiten renunciar a la convocatoria ordinaria?",
         "Enfermedad acreditada, conciliación laboral u otras circunstancias individualizadas valoradas por la dirección.", "Orden 8/2025 art. 9"),
        ("¿Con cuánta antelación se renuncia a la convocatoria?",
         "Antes de 10 días hábiles a la evaluación correspondiente.", "Instrucciones 2026-27 §12.5"),
        ("¿En qué plazo resuelve la dirección una renuncia?",
         "En un máximo de 10 días hábiles; cabe recurso de alzada.", "Instrucciones 2026-27 §12.5"),
        ("Si agoto las convocatorias, ¿qué tres salidas tengo?",
         "Pruebas libres, convocatoria extraordinaria de gracia y oferta modular.", "Instrucciones 2026-27 §12.2"),
        ("¿Quién resuelve la convocatoria de gracia y en qué plazo?",
         "La Dirección Territorial de la provincia, en un máximo de 2 meses.", "Orden 8/2025 art. 10"),
        ("¿Cuántas veces se concede la gracia y se puede renunciar después?",
         "Una sola vez por módulo; una vez autorizada no se puede renunciar ni anular matrícula.", "Orden 8/2025 art. 10"),
        ("¿Qué documentos oficiales de evaluación hay?",
         "Expediente académico, actas de evaluación y certificado académico oficial.", "Orden 8/2025 arts. 16-19"),
        ("¿Qué valor tienen las unidades formativas?",
         "Son certificables; superar todas las de un módulo da derecho a certificar el módulo (válido en todo el Estado).", "Orden 8/2025 arts. 16-19"),
    ],
    quiz=[
        ("Convocatorias máximas por módulo en Grado D y Grado E:",
         ["2 y 2", "4 y 2", "4 y 4", "6 y 4"], 1,
         "Grado D: 4 (2 por curso). Grado E: 2.", "Instrucciones 2026-27 §12"),
        ("La permanencia máxima en modalidad virtual es de…",
         ["4 cursos", "5 cursos", "6 cursos consecutivos", "8 cursos"], 2,
         "Hasta 6 cursos consecutivos en virtual; en presencial, el doble de cursos del ciclo.", "Instrucciones 2026-27 §12"),
        ("El plazo para renunciar a una convocatoria es…",
         ["24 horas antes", "Antes de 10 días hábiles", "1 mes antes", "El mismo día"], 1,
         "Antes de 10 días hábiles; la dirección resuelve en otros 10 días hábiles.", "Instrucciones 2026-27 §12.5"),
        ("La convocatoria de gracia se solicita a…",
         ["El centro", "La Dirección Territorial", "El Ministerio", "La Inspección"], 1,
         "A la Dirección Territorial de la provincia; resuelve en ≤ 2 meses.", "Orden 8/2025 art. 10"),
        ("La gracia se concede…",
         ["Tantas veces como haga falta", "Una vez por módulo", "Una vez por curso", "Dos veces por módulo"], 1,
         "Una sola vez por módulo y después es irrenunciable.", "Orden 8/2025 art. 10"),
        ("¿Cuál NO es una salida tras agotar convocatorias?",
         ["Pruebas libres", "Convocatoria de gracia", "Oferta modular", "Repetir el curso completo gratis sin límite"], 3,
         "Las salidas son pruebas libres, gracia y oferta modular.", "Instrucciones 2026-27 §12.2"),
    ],
))

# ===========================================================================
# MÓDULO 7 · PROMOCIÓN Y RECUPERACIÓN
# ===========================================================================
MODULES.append(dict(
    id="m7", title="Promoción y recuperación", tagline="240 h, 80%, 20% del horario semanal y programas de recuperación.",
    objetivos=[
        "Aplicar los criterios de promoción de GM/GS y de Grado Básico.",
        "Recordar la regla de las 240 h y la del 80%.",
        "Explicar el programa de recuperación individual.",
    ],
    lesson="""
<h3>1. Grado medio y superior</h3>
<ul>
<li>Para cursar los módulos de 2.º hay que <b>superar todos los de 1.º</b>.</li>
<li><b>No obstante</b>, si el equipo docente lo aconseja, se puede promocionar cuando los pendientes de 1.º sumen <b>no más de 240 horas</b> (Instrucciones 2026-27 §10.1.b).</li>
<li>La Orden 8/2025 (art. 14) lo formula como: superar al menos el <b>80% de las horas lectivas</b> del primer curso.</li>
<li>Quien supere <b>más del 50%</b> de las horas de 1.º puede matricularse de módulos de 2.º <b>hasta 1000 horas</b>, si hay disponibilidad y con autorización de la <b>Inspección de Educación</b>.</li>
</ul>
<div class="callout info"><b>Las dos caras de la misma moneda:</b> ≤ 240 h pendientes ≈ ≥ 80% de horas superadas. Memoriza ambas formulaciones.</div>

<h3>2. Grado básico</h3>
<ul>
<li>Se promociona cuando los módulos pendientes asociados a estándares de competencia <b>no superan el 20% del horario semanal</b>.</li>
<li>Además, hay que tener superado al menos <b>un ámbito distinto del profesional</b>, si el equipo docente ve garantías de éxito.</li>
</ul>

<h3>3. Si no puedo ir a la empresa en 1.º</h3>
<ul>
<li>Si el alumnado de 1.º no se incorpora a la FE por causas justificadas y acreditadas, <b>desarrolla el curso completo en el centro</b> y realiza actividades complementarias, extraescolares o de refuerzo.</li>
<li>En 2.º se aplica el <b>art. 9 del RD 659/2023</b>.</li>
</ul>

<h3>4. Programa de recuperación individual</h3>
<ul>
<li>Quien no supere algún módulo o RA tendrá un <b>programa de recuperación individual</b> con actividades, momentos y criterios de evaluación, recogido en la <b>PGA</b> y en las programaciones docentes.</li>
<li>Se diseña de forma diferenciada: tras la ordinaria de 1.º o 2.º, y para alumnado de 2.º con módulos de 1.º pendientes (se simultanea; <b>no se garantiza</b> la asistencia a las clases del módulo pendiente).</li>
</ul>
    """,
    trucos=[
        "<b>240 h ≈ 80%.</b> Son dos formas de decir lo mismo para GM/GS.",
        "<b>50% → 1000 h.</b> Superas más de la mitad y puedes coger módulos de 2.º hasta 1000 h (con Inspección).",
        "Básico: <b>20% del horario semanal</b> + <b>un ámbito no profesional</b> superado.",
    ],
    trampas=[
        "El 20% del Básico es <b>semanal</b>, no del curso.",
        "El 50% → 1000 h exige <b>disponibilidad</b> y <b>autorización de la Inspección</b>; no es automático.",
        "El programa de recuperación va en la <b>PGA</b> y en las programaciones.",
    ],
    normas=[("Orden 8/2025 (DOGV)", "https://dogv.gva.es/datos/2025/04/30/pdf/2025_13083.pdf")],
    cards=[
        ("¿Cuál es la regla general para pasar a 2.º en GM/GS?",
         "Superar todos los módulos de 1.º.", "Instrucciones 2026-27 §10"),
        ("¿Cuál es la excepción para promocionar en GM/GS?",
         "Si el equipo docente lo aconseja y los pendientes suman no más de 240 horas.", "Instrucciones 2026-27 §10.1.b"),
        ("¿Cómo formula la Orden 8/2025 el criterio de promoción?",
         "Superar al menos el 80% de las horas lectivas del primer curso (art. 14).", "Orden 8/2025 art. 14"),
        ("Si supero más del 50% de las horas de 1.º, ¿qué puedo hacer?",
         "Matricularme de módulos de 2.º hasta 1000 horas, con disponibilidad y autorización de la Inspección.", "Instrucciones 2026-27 §10"),
        ("¿Cuándo se promociona en Grado Básico?",
         "Cuando los pendientes asociados a estándares no superan el 20% del horario semanal y se ha superado al menos un ámbito no profesional.", "Orden 8/2025 art. 14.1.a"),
        ("¿Qué hace el alumnado de 1.º que no puede ir a la empresa?",
         "Con causas justificadas, cursa el curso completo en el centro con actividades complementarias, extraescolares o de refuerzo.", "Instrucciones 2026-27 §10.3"),
        ("¿Qué es el programa de recuperación individual?",
         "El plan con actividades, momentos y criterios de evaluación para quien no supera un módulo o RA, recogido en la PGA y las programaciones.", "Instrucciones 2026-27 §10.4"),
        ("Si estoy en 2.º con módulos de 1.º pendientes, ¿tengo garantizada la asistencia a esas clases?",
         "No: se simultanea y no se garantiza la asistencia a las clases del módulo pendiente.", "Instrucciones 2026-27 §10.4"),
    ],
    quiz=[
        ("En GM/GS, para promocionar con pendientes estos deben sumar como máximo…",
         ["120 h", "240 h", "300 h", "No hay límite"], 1,
         "No más de 240 h (equivalente a superar ≥ 80% de las horas).", "Instrucciones 2026-27 §10.1.b"),
        ("Superar más del 50% de las horas de 1.º permite matricularse de 2.º hasta…",
         ["500 h", "800 h", "1000 h", "Sin límite"], 2,
         "Hasta 1000 h, con disponibilidad y autorización de Inspección.", "Instrucciones 2026-27 §10"),
        ("En Grado Básico se promociona si los pendientes no superan…",
         ["El 10% del curso", "El 20% del horario semanal", "El 20% del curso", "El 240%"], 1,
         "El 20% del horario semanal, más un ámbito no profesional superado.", "Orden 8/2025 art. 14.1.a"),
        ("El límite de 240 h equivale a superar al menos…",
         ["El 50% de las horas", "El 60%", "El 80%", "El 90%"], 2,
         "240 h pendientes ≈ haber superado el 80% de las horas lectivas.", "Orden 8/2025 art. 14"),
        ("¿Dónde se recoge el programa de recuperación individual?",
         ["Solo en ITACA", "En la PGA y las programaciones docentes", "En el expediente", "No se recoge"], 1,
         "Se recoge en la PGA y en las programaciones docentes.", "Instrucciones 2026-27 §10.4"),
    ],
))

# ===========================================================================
# MÓDULO 8 · CALIFICACIONES Y TITULACIÓN
# ===========================================================================
MODULES.append(dict(
    id="m8", title="Calificaciones, menciones y titulación", tagline="1-10 sin decimales, MH, media con 2 decimales y requisitos de título.",
    objetivos=[
        "Calificar módulos y ámbitos de Grado Básico.",
        "Calcular la nota final y saber cuándo es 5.",
        "Distinguir mención honorífica y Matrícula de Honor.",
    ],
    lesson="""
<h3>1. Calificaciones</h3>
<ul>
<li>Módulos profesionales: numérica de <b>1 a 10, sin decimales</b>. Son positivas las <b>≥ 5</b>.</li>
<li>En <b>Grado Básico</b>, los ámbitos de Comunicación y Ciencias Sociales y de Ciencias Aplicadas se califican de forma <b>no numérica</b>: <b>IN</b> (Insuficiente), <b>SU</b> (Suficiente), <b>BI</b> (Bien), <b>NT</b> (Notable), <b>SB</b> (Sobresaliente). Estos ciclos <b>no tienen nota final de ciclo</b>.</li>
<li>La <b>nota final</b> de GM, GS y cursos de especialización es la <b>media aritmética con 2 decimales</b> de todos los módulos.</li>
<li>No se tiene en cuenta la calificación «<b>convalidado sin nota</b>». Si todos los módulos fueran «convalidado sin nota», la nota final es <b>5</b>.</li>
</ul>

<h3>2. Menciones y matrículas de honor</h3>
<ul>
<li><b>Mención honorífica</b>: por obtener un <b>10</b> en un módulo. Máximo el <b>10% del alumnado</b> del módulo en cada grupo. Se anota «MH» tras el 10.</li>
<li><b>Matrícula de Honor</b> (GM y GS): con <b>nota final ≥ 9</b>. Máximo <b>2 por ciclo de grado medio</b> y <b>3 por ciclo de grado superior</b>; si hay menos de 20 estudiantes, solo <b>1</b>.</li>
</ul>

<h3>3. Requisitos para titular</h3>
<ul>
<li>Calificación positiva en <b>todos los módulos</b> del ciclo o curso.</li>
<li>Haber superado <b>todas las horas de Formación en Empresa</b>.</li>
<li>Acreditar los <b>requisitos académicos de acceso</b>.</li>
<li>La decisión se adopta de forma <b>colegiada</b> por el equipo educativo, atendiendo a la competencia general y a las competencias profesionales y para la empleabilidad.</li>
<li>Los <b>cursos de especialización</b> pueden conducir a título o a certificado, según su real decreto.</li>
</ul>

<h3>4. Un módulo superado se reutiliza</h3>
<ul>
<li>Un módulo cursado y superado se considera «<b>aprobado</b>» con la calificación obtenida en cualquier otro ciclo donde se curse.</li>
<li>Puede usarse para futuras convalidaciones, pero <b>un módulo convalidado no sirve para convalidar a su vez otros módulos</b>.</li>
</ul>
    """,
    trucos=[
        "Módulos: <b>1-10 enteros</b>, aprueba ≥5. Ámbitos de Básico: <b>IN-SU-BI-NT-SB</b> y sin nota de ciclo.",
        "<b>MH</b> (mención) = 10 y máx <b>10%</b> del grupo. <b>Matrícula de Honor</b> ≥9 y máx <b>2 GM / 3 GS</b> (si &lt;20 alumnos, 1).",
        "Si <b>todo</b> es «convalidado sin nota» → nota final <b>5</b>.",
    ],
    trampas=[
        "«Convalidado sin nota» <b>no</b> cuenta para la media.",
        "Un módulo <b>convalidado</b> no sirve para convalidar otros módulos.",
        "Los ciclos de Grado Básico <b>no tienen nota final de ciclo</b>.",
    ],
    normas=[("Orden 8/2025 (DOGV)", "https://dogv.gva.es/datos/2025/04/30/pdf/2025_13083.pdf")],
    cards=[
        ("¿Cómo se califican los módulos profesionales?",
         "Numérica de 1 a 10, sin decimales; son positivas las ≥ 5.", "Orden 8/2025 art. 5"),
        ("¿Cómo se califican los ámbitos de Grado Básico?",
         "De forma no numérica: Insuficiente (IN), Suficiente (SU), Bien (BI), Notable (NT) y Sobresaliente (SB).", "Orden 8/2025 art. 5"),
        ("¿Los ciclos de Grado Básico tienen nota final de ciclo?",
         "No.", "Orden 8/2025 art. 5"),
        ("¿Cómo se calcula la nota final de GM/GS/E?",
         "Media aritmética con 2 decimales de todos los módulos.", "Orden 8/2025 art. 5"),
        ("¿Cuánto vale «convalidado sin nota» en la media?",
         "No computa. Si todos los módulos fueran «convalidado sin nota», la nota final es 5.", "Orden 8/2025 art. 5"),
        ("¿Qué es la mención honorífica y cuántas se pueden dar?",
         "Un 10 en un módulo; máximo el 10% del alumnado del módulo en cada grupo. Se anota «MH».", "Orden 8/2025 art. 6"),
        ("¿Qué nota hace falta para la Matrícula de Honor y cuántas hay?",
         "Nota final ≥ 9; máximo 2 por ciclo de GM y 3 por ciclo de GS (si hay menos de 20 estudiantes, solo 1).", "Orden 8/2025 art. 6"),
        ("¿Qué tres requisitos principales hay para titular?",
         "Positiva en todos los módulos, haber superado todas las horas de FE y acreditar los requisitos académicos de acceso.", "Orden 8/2025 art. 15"),
        ("¿Cómo se decide la titulación?",
         "De forma colegiada por el equipo educativo.", "Orden 8/2025 art. 15"),
        ("¿Los cursos de especialización conducen siempre a título?",
         "No: pueden conducir a título o a certificado, según su real decreto.", "Instrucciones 2026-27 §13"),
        ("Si supero un módulo, ¿se puede reutilizar en otro ciclo?",
         "Sí, se considera «aprobado» con la calificación obtenida en cualquier otro ciclo donde se curse.", "Orden 8/2025 arts. 5.7 y 20.4-20.5"),
        ("¿Puedo convalidar un módulo a partir de otro que ya convalidé?",
         "No: un módulo convalidado no sirve para convalidar a su vez otros módulos.", "Orden 8/2025 art. 20.5"),
    ],
    quiz=[
        ("Los módulos profesionales se califican…",
         ["Con decimales", "De 1 a 10 sin decimales", "De 0 a 100", "Como Apto/No apto"], 1,
         "Numérica de 1 a 10, sin decimales; positiva ≥ 5.", "Orden 8/2025 art. 5"),
        ("La nota final de GM/GS se calcula…",
         ["Con la nota más alta", "Como media aritmética con 2 decimales", "Solo con los módulos de 2.º", "Promediando ámbitos"], 1,
         "Media aritmética con 2 decimales de todos los módulos.", "Orden 8/2025 art. 5"),
        ("Si TODOS los módulos son «convalidado sin nota», la nota final es…",
         ["0", "5", "No hay nota", "9"], 1,
         "La nota final es 5.", "Orden 8/2025 art. 5"),
        ("La mención honorífica se asocia a…",
         ["Nota final ≥9", "Un 10 en un módulo (máx. 10% del grupo)", "Asistencia perfecta", "La FE"], 1,
         "Mención honorífica: 10 en un módulo, máximo 10% del alumnado del grupo.", "Orden 8/2025 art. 6"),
        ("Matrícula de Honor: máximo por ciclo de GM y GS, respectivamente:",
         ["2 y 3", "3 y 2", "1 y 1", "5 y 5"], 0,
         "2 en GM y 3 en GS; si hay menos de 20 estudiantes, solo 1.", "Orden 8/2025 art. 6"),
        ("Un módulo convalidado…",
         ["Sirve para convalidar otros módulos", "No sirve para convalidar a su vez otros módulos", "Cuenta siempre como 10", "Equivale a la FE"], 1,
         "Un convalidado no convalida otros módulos.", "Orden 8/2025 art. 20.5"),
    ],
))

# ===========================================================================
# MÓDULO 9 · CONVALIDACIONES Y EXENCIONES
# ===========================================================================
MODULES.append(dict(
    id="m9", title="Convalidaciones y exenciones", tagline="Plazos, módulos idénticos, puntuación y vía Ministerio.",
    objetivos=[
        "Saber el plazo y el procedimiento de convalidación.",
        "Diferenciar «convalidado sin nota» de certificado B/C (5).",
        "Explicar la convalidación de módulos idénticos y la vía Ministerio.",
    ],
    lesson="""
<h3>1. Cómo y cuándo se solicita</h3>
<ul>
<li>Es requisito <b>estar matriculado</b> en el módulo que se pretende convalidar.</li>
<li>Mientras no se resuelva, hay que <b>asistir a clase y presentarse</b> a las evaluaciones.</li>
<li>Plazo: durante <b>septiembre</b> para los matriculados en julio; quienes se matriculen después disponen de <b>1 mes</b> desde la matrícula.</li>
<li>Resuelve la dirección del centro público en un máximo de <b>1 mes</b> (modelo del anexo IV).</li>
</ul>

<h3>2. Módulos idénticos y traslado de notas</h3>
<ul>
<li>Son <b>idénticos</b> los módulos con mismos códigos, denominaciones, capacidades terminales o RA, contenidos y duración, sea cual sea el ciclo.</li>
<li>Se <b>trasladan las calificaciones</b> de los módulos superados a cualquier ciclo o curso donde estén incluidos.</li>
</ul>

<h3>3. Qué puntuación tiene una convalidación</h3>
<ul>
<li>«<b>Convalidado sin nota</b>» (estudios universitarios o anteriores a la LOGSE): <b>no</b> computa para la nota media.</li>
<li>Convalidación aportando un <b>certificado de competencia (grado B)</b> o un <b>certificado profesional (grado C)</b>: computa como <b>5</b> en la nota media.</li>
<li>Las convalidaciones entre títulos LOGSE y LOE se rigen por el <b>RD 1085/2020</b> y los anexos de cada título.</li>
</ul>

<h3>4. Convalidaciones del Ministerio e inglés</h3>
<ul>
<li>Las que no son competencia del centro se tramitan ante el <b>Ministerio</b> (portal todofp). Solo <b>una solicitud por curso académico</b>.</li>
<li>La convalidación del <b>inglés profesional</b> de GM y GS con el <b>inglés técnico LOE</b> se rige por las Instrucciones de 4 de noviembre de 2024 de la DGFP.</li>
</ul>

<h3>5. Experiencia laboral y formación no formal</h3>
<ul>
<li>Solo pueden aportarse para convalidar módulos si han sido reconocidas mediante un <b>procedimiento de acreditación de competencias profesionales</b>.</li>
<li>Quien tenga acreditado un estándar de competencia del <b>CNECP</b> tendrá convalidados los módulos correspondientes según la norma de cada título.</li>
</ul>
    """,
    trucos=[
        "Convalidar exige <b>matrícula + asistencia</b> hasta que se resuelva.",
        "Plazo: <b>septiembre</b> (matriculados en julio) o <b>1 mes</b> desde la matrícula. Resuelve en <b>1 mes</b> (anexo IV).",
        "B o C → <b>5</b>. Universidad o pre-LOGSE → <b>sin nota</b>.",
    ],
    trampas=[
        "«Convalidado sin nota» <b>no</b> cuenta para la media; el certificado B/C sí (como 5).",
        "La vía Ministerio admite <b>una sola solicitud por curso</b>.",
        "La experiencia laboral por sí sola no basta: requiere <b>acreditación de competencias</b> (CNECP).",
    ],
    normas=[("Convalidaciones (Conselleria)", "https://ceice.gva.es/es/web/formacion-profesional/convalidaciones"),
            ("RD 1085/2020", "https://www.boe.es/eli/es/rd/2020/12/09/1085/con")],
    cards=[
        ("¿Cuál es el requisito básico para solicitar una convalidación?",
         "Estar matriculado en el módulo que se pretende convalidar.", "Instrucciones 2026-27 §14.2-14.3"),
        ("Mientras se resuelve la convalidación, ¿qué debo hacer?",
         "Asistir a clase y presentarme a las evaluaciones.", "Instrucciones 2026-27 §14.3"),
        ("¿Cuál es el plazo general para pedir la convalidación?",
         "Durante septiembre para los matriculados en julio; si te matriculas después, 1 mes desde la matrícula.", "Instrucciones 2026-27 §14.3"),
        ("¿En qué plazo y con qué modelo resuelve la dirección?",
         "En un máximo de 1 mes, con el modelo del anexo IV.", "Orden 8/2025 art. 20"),
        ("¿Cuándo dos módulos son idénticos?",
         "Cuando tienen mismos códigos, denominaciones, capacidades terminales o RA, contenidos y duración, sea cual sea el ciclo.", "Instrucciones 2026-27 §14.2"),
        ("¿Qué ocurre con las calificaciones de módulos idénticos superados?",
         "Se trasladan a cualquier ciclo o curso donde estén incluidos.", "Instrucciones 2026-27 §14.2"),
        ("¿Cuánto computa «convalidado sin nota» en la media?",
         "Nada: no computa para la nota media.", "Instrucciones 2026-27 §14.2"),
        ("¿Cuánto computa un certificado de competencia B o un certificado profesional C?",
         "Como 5 en la nota media.", "Instrucciones 2026-27 §14.2"),
        ("¿Qué norma rige las convalidaciones entre títulos LOGSE y LOE?",
         "El RD 1085/2020 y los anexos de cada título.", "RD 1085/2020"),
        ("Las convalidaciones que no puede resolver el centro se tramitan…",
         "Ante el Ministerio (portal todofp); solo una solicitud por curso académico.", "Instrucciones 2026-27 §14.4"),
        ("¿Cómo se convalida la experiencia laboral?",
         "Solo si ha sido reconocida por un procedimiento de acreditación de competencias profesionales (estándares del CNECP).", "Orden 8/2025 art. 20.6"),
    ],
    quiz=[
        ("Para convalidar un módulo hay que…",
         ["Solo presentar el título", "Estar matriculado y asistir a clase mientras se resuelve", "Esperar a junio", "Pedirlo al Ministerio siempre"], 1,
         "Matrícula + asistencia mientras se resuelve.", "Instrucciones 2026-27 §14.2-14.3"),
        ("El plazo de resolución de la convalidación por la dirección es…",
         ["10 días", "1 mes", "2 meses", "6 meses"], 1,
         "1 mes, con el modelo del anexo IV.", "Orden 8/2025 art. 20"),
        ("Un certificado de competencia (grado B) convalidado computa como…",
         ["Nada", "5", "9", "10"], 1,
         "B y C computan como 5; «sin nota» no computa.", "Instrucciones 2026-27 §14.2"),
        ("«Convalidado sin nota» procede de…",
         ["Un certificado profesional C", "Estudios universitarios o anteriores a la LOGSE", "La experiencia laboral", "La FCT"], 1,
         "Estudios universitarios o anteriores a la LOGSE.", "Instrucciones 2026-27 §14.2"),
        ("Las convalidaciones no competencia del centro:",
         ["No se pueden pedir", "Se tramitan ante el Ministerio, una solicitud por curso", "Las resuelve la Inspección", "Son automáticas"], 1,
         "Vía Ministerio (todofp), una solicitud por curso académico.", "Instrucciones 2026-27 §14.4"),
        ("Para convalidar por experiencia laboral, esta debe…",
         ["Bastar con un contrato", "Estar reconocida mediante acreditación de competencias", "Ser de 10 años", "Ser en el extranjero"], 1,
         "Requiere procedimiento de acreditación de competencias profesionales (CNECP).", "Orden 8/2025 art. 20.6"),
    ],
))

# ===========================================================================
# MÓDULO 10 · FE, FCT Y FP DUAL
# ===========================================================================
MODULES.append(dict(
    id="m10", title="Formación en Empresa, FCT y FP Dual", tagline="100 h, dualización, requisitos, exención y Seguridad Social.",
    objetivos=[
        "Describir la FE en Grado D y la dualización.",
        "Recordar los requisitos para iniciar la FE.",
        "Explicar la exención y quién paga la Seguridad Social.",
    ],
    lesson="""
<h3>1. Formación en Empresa (FE): lo básico</h3>
<ul>
<li>Se puede realizar en <b>cualquier empresa u organismo equiparado</b>, incluidos autónomos sin trabajadores a su cargo.</li>
<li>En <b>Grado D</b>, el plan de formación se elabora en el <b>1.er trimestre</b>; la FE puede empezar al inicio del <b>2.º trimestre de 1.º</b> y en 2.º puede desarrollarse a lo largo de los tres trimestres.</li>
<li>El alumnado de 1.º de Grado D realiza un <b>mínimo de 100 horas</b> de FE.</li>
<li>Forma parte de los módulos profesionales: la empresa emite un informe y el profesorado califica teniendo en cuenta al tutor de empresa.</li>
</ul>

<h3>2. Dualización y duración</h3>
<table>
<tr><th>Régimen</th><th>Estancia en empresa</th><th>RA en empresa</th></tr>
<tr><td>General (GM/GS/E)</td><td><b>25-35%</b> de la formación</td><td>10-20%</td></tr>
<tr><td>Intensivo</td><td>&gt;35% hasta <b>50%</b></td><td>&gt;30%</td></tr>
<tr><td>Grado Básico</td><td><b>20%</b> de las horas</td><td>10-20% (ámbito profesional)</td></tr>
</table>
<p>Se pueden dualizar todos los módulos <b>excepto el Proyecto Intermodular</b>, y debe impartirse <b>al menos el 35%</b> del módulo en el centro.</p>

<h3>3. Requisitos para iniciar la FE</h3>
<ul>
<li>Tener cumplidos los <b>16 años</b>.</li>
<li>Haber adquirido las competencias de <b>prevención de riesgos laborales (PRL)</b> del perfil profesional.</li>
<li>Tener registrados en ITACA el <b>NUSS como titular</b> (no beneficiario) y el <b>DNI/NIE/Pasaporte</b>.</li>
<li>La DGFP mantiene el <b>seguro de accidentes y responsabilidad civil</b>.</li>
</ul>

<h3>4. Exención de la FE / FCT</h3>
<ul>
<li>Se acredita experiencia laboral de <b>6 meses</b> (grados C y E) o <b>1 año a tiempo completo</b> o equivalente (grados D), correspondiente a la formación cursada, en los <b>5 años anteriores</b>.</li>
<li>Si se acredita un mínimo del <b>10% de los RA</b> de módulos asociados a estándares, la exención es <b>total</b> (1.º y 2.º). Si no, puede ser <b>parcial</b>.</li>
<li>Solicitud durante todo el curso y, con carácter general, <b>al menos 30 días antes</b> del inicio de la FE (salvo quien espera cumplir la experiencia: hasta antes de la evaluación final).</li>
<li>Resuelve la dirección en un máximo de <b>2 meses</b>, a propuesta del equipo docente.</li>
<li>Si se solicita en 2.º tras hacer parte de la FE en 1.º, solo puede ser <b>parcial</b>.</li>
</ul>

<h3>5. Seguimiento, cese y regímenes</h3>
<ul>
<li>Supervisión: <b>tutor/a del grupo</b> + <b>profesorado del módulo</b>, coordinados con el <b>tutor de empresa</b>, a través de ITACA y SAÓ Gestión. El tutor de empresa valora los RA como «superado» o «no superado».</li>
<li>El alumnado que cesa <b>se reincorpora al centro</b>; la FE puede realizarse en un <b>máximo de 2 ocasiones</b> por oferta formativa. Si no puede hacerse en 1.º, se <b>acumula en 2.º</b>.</li>
<li><b>FCT</b>: se rige por la <b>Orden 12/2022</b>; en semipresencial se realiza siempre de forma <b>presencial</b>.</li>
<li><b>FP Dual</b>: <b>Decreto 74/2013</b> (mod. por Decreto 47/2021), <b>Orden 5/2022</b> y Resolución de 11/03/2022.</li>
</ul>

<h3>6. ¿Quién paga la Seguridad Social?</h3>
<ul>
<li><b>Dirección General de FP</b>: FE general y FCT (centros públicos y privados concertados).</li>
<li><b>Empresa</b>: FE intensiva y FP Dual (beca o contrato de formación en alternancia).</li>
<li>Excepción: las desarrolladas en <b>administraciones y entidades públicas</b> las liquida la DGFP.</li>
</ul>
    """,
    trucos=[
        "FE en 1.º de Grado D: mínimo <b>100 horas</b>; empieza como pronto al inicio del <b>2.º trimestre</b>.",
        "Dual: <b>25-35%</b> (general) o <b>&gt;35-50%</b> (intensivo); en Básico <b>20%</b>. Siempre <b>≥35%</b> del módulo en el centro.",
        "Exención: <b>6 meses (C/E)</b> o <b>1 año (D)</b> en los <b>5 años</b> anteriores; <b>≥10% RA</b> → total.",
        "Paga: DGFP (general/FCT) · Empresa (intensiva/Dual).",
    ],
    trampas=[
        "El <b>Proyecto Intermodular</b> no se puede dualizar.",
        "Solicitar la exención en 2.º tras hacer FE en 1.º solo permite la exención <b>parcial</b>.",
        "La FCT en semipresencial es <b>siempre presencial</b>.",
        "En administraciones públicas la Seguridad Social la paga la <b>DGFP</b>, no la empresa.",
    ],
    normas=[("FE, FCT y Dual (Conselleria)", "https://ceice.gva.es/es/web/formacion-profesional/formacio-en-empresa-fct-i-dual"),
            ("Orden 12/2022 (DOGV)", "https://dogv.gva.es/datos/2022/03/16/pdf/2022_2086.pdf")],
    cards=[
        ("¿Dónde se puede realizar la FE?",
         "En cualquier empresa u organismo equiparado, incluidos autónomos sin trabajadores a su cargo.", "Instrucciones 2026-27 §15.1"),
        ("¿Cuándo se elabora el plan de formación y cuándo puede empezar la FE en Grado D?",
         "El plan en el 1.er trimestre; la FE puede empezar al inicio del 2.º trimestre de 1.º.", "Instrucciones 2026-27 §15.1"),
        ("¿Cuántas horas mínimas de FE hace el alumnado de 1.º de Grado D?",
         "Un mínimo de 100 horas.", "Instrucciones 2026-27 §15.1"),
        ("¿Qué porcentaje de formación se hace en la empresa en régimen general?",
         "Entre el 25% y el 35%, con un 10-20% de RA en empresa.", "Instrucciones 2026-27 §15.1.1"),
        ("¿Y en régimen intensivo?",
         "Más del 35% hasta el 50%, con más del 30% de RA en empresa.", "Instrucciones 2026-27 §15.1.1"),
        ("¿Qué porcentaje de estancia en empresa tiene el Grado Básico?",
         "El 20% de las horas, con 10-20% de RA del ámbito profesional.", "Instrucciones 2026-27 §15.1.1"),
        ("¿Qué módulo NO se puede dualizar?",
         "El Proyecto Intermodular.", "Instrucciones 2026-27 §15.1.1"),
        ("¿Qué porcentaje del módulo debe impartirse en el centro?",
         "Al menos el 35%.", "Instrucciones 2026-27 §15.1.1"),
        ("Requisitos para iniciar la FE:",
         "16 años, competencias de PRL, NUSS como titular y DNI/NIE/Pasaporte en ITACA; la DGFP mantiene el seguro.", "Instrucciones 2026-27 §15.1.2"),
        ("Experiencia para exención de FE/FCT según grado:",
         "6 meses en grados C y E; 1 año a tiempo completo o equivalente en grados D, en los 5 años anteriores.", "Instrucciones 2026-27 §15.1.3"),
        ("¿Cuándo la exención de FE/FCT es total?",
         "Cuando se acredita al menos el 10% de los RA de módulos asociados a estándares de competencia.", "Instrucciones 2026-27 §15.1.3"),
        ("Plazo de solicitud y de resolución de la exención:",
         "Con carácter general, al menos 30 días antes del inicio de la FE; resuelve la dirección en ≤ 2 meses.", "Instrucciones 2026-27 §15.1.3"),
        ("Si pido la exención en 2.º tras hacer FE en 1.º, ¿cómo puede ser?",
         "Solo parcial.", "Instrucciones 2026-27 §15.1.3"),
        ("¿Quién supervisa y evalúa la FE en la empresa?",
         "El tutor/a del grupo y el profesorado del módulo, coordinados con el tutor de empresa (ITACA y SAÓ).", "Instrucciones 2026-27 §15.1.4"),
        ("¿Cuántas ocasiones puede realizarse la FE por oferta formativa?",
         "Un máximo de 2 ocasiones.", "Instrucciones 2026-27 §15.1.6-15.1.7"),
        ("¿Quién paga la Seguridad Social en la FE general y la FCT?",
         "La Dirección General de FP (también en intensiva/Dual hecha en administraciones públicas).", "Instrucciones 2026-27 §15.4"),
        ("¿Quién paga la Seguridad Social en FE intensiva y FP Dual?",
         "La empresa (beca o contrato de formación en alternancia).", "Instrucciones 2026-27 §15.4"),
        ("¿Qué norma regula la FCT y cómo es en semipresencial?",
         "La Orden 12/2022; en semipresencial el módulo de FCT es siempre presencial.", "Instrucciones 2026-27 §15.2"),
    ],
    quiz=[
        ("En Grado D, la FE de 1.º tiene un mínimo de…",
         ["50 h", "100 h", "200 h", "400 h"], 1,
         "Mínimo de 100 horas.", "Instrucciones 2026-27 §15.1"),
        ("La estancia en empresa en régimen general es del…",
         ["10-20%", "25-35%", "40-50%", "60%"], 1,
         "25-35% de la formación, con 10-20% de RA.", "Instrucciones 2026-27 §15.1.1"),
        ("¿Qué módulo no se puede dualizar?",
         ["Sostenibilidad", "Digitalización", "Proyecto Intermodular", "Inglés profesional"], 2,
         "El Proyecto Intermodular no se dualiza.", "Instrucciones 2026-27 §15.1.1"),
        ("Requisito para iniciar la FE que se suele preguntar:",
         ["Tener 18 años", "Tener 16 años y PRL", "Carné de conducir", "Nivel B2 de inglés"], 1,
         "16 años, PRL y NUSS como titular + DNI/NIE/Pasaporte.", "Instrucciones 2026-27 §15.1.2"),
        ("La exención de FE por experiencia en grados D exige…",
         ["6 meses", "1 año a tiempo completo o equivalente", "2 años", "3 años"], 1,
         "1 año en grados D; 6 meses en C y E; en los 5 años anteriores.", "Instrucciones 2026-27 §15.1.3"),
        ("La exención es TOTAL si se acredita…",
         ["Cualquier experiencia", "Al menos 10% de los RA de módulos asociados a estándares", "Un contrato indefinido", "50% de los RA"], 1,
         "≥10% de los RA → exención total; si no, parcial.", "Instrucciones 2026-27 §15.1.3"),
        ("El plazo general para pedir la exención de FE es…",
         ["El mismo día", "Al menos 30 días antes del inicio", "1 semana antes", "No hay plazo"], 1,
         "Al menos 30 días antes; resuelve en ≤ 2 meses.", "Instrucciones 2026-27 §15.1.3"),
        ("En FE intensiva y FP Dual, la Seguridad Social la paga…",
         ["La DGFP", "La empresa", "El alumno", "El centro"], 1,
         "La empresa (beca o contrato de formación en alternancia).", "Instrucciones 2026-27 §15.4"),
        ("En régimen semipresencial, la FCT se realiza…",
         ["A distancia", "De forma presencial", "En el centro solo", "No se realiza"], 1,
         "Siempre de forma presencial.", "Instrucciones 2026-27 §15.2"),
    ],
))

# ===========================================================================
# MÓDULO 11 · NECESIDADES ESPECÍFICAS DE APOYO
# ===========================================================================
MODULES.append(dict(
    id="m11", title="Alumnado con necesidades específicas de apoyo", tagline="6/4 convocatorias, adaptaciones sin minorar y flexibilización.",
    objetivos=[
        "Recordar el número de convocatorias ampliadas.",
        "Explicar las adaptaciones sin minorar la calificación.",
        "Saber la flexibilización de la lengua extranjera.",
    ],
    lesson="""
<h3>1. Más convocatorias</h3>
<ul>
<li>El alumnado con <b>necesidades educativas especiales</b> puede presentarse a un mismo módulo hasta <b>6 veces en Grado D</b> y <b>4 veces en Grado E</b>.</li>
<li>Si agota las convocatorias, se le puede <b>ampliar</b> para los módulos pendientes si favorece terminar el ciclo.</li>
</ul>

<h3>2. Adaptaciones sin bajar la nota</h3>
<ul>
<li>Se aplican las adaptaciones necesarias en metodología, <b>ampliación de tiempos y recursos</b>, sin que puedan minorar las calificaciones.</li>
<li>Los referentes siguen siendo los mismos <b>RA, criterios de evaluación y competencias generales</b>.</li>
<li>Respuesta educativa para la inclusión: <b>Orden 20/2019</b> y <b>Decreto 72/2021</b>.</li>
</ul>

<h3>3. Lengua extranjera y Grado Básico</h3>
<ul>
<li>Para alumnado con discapacidad, y en especial con dificultades de <b>expresión oral</b>, se establecen medidas de flexibilización y alternativas metodológicas en la lengua extranjera, que no minoren la calificación.</li>
<li>En <b>Grado Básico</b> se elabora un <b>informe de orientación individualizado</b> (confidencial y no prescriptivo) con especial atención a la orientación profesional.</li>
<li>Reserva de plaza para personas con discapacidad: <b>Orden 10/2024</b>, art. 15.3.</li>
</ul>

<div class="callout tip"><b>Números:</b> 6 (D) y 4 (E). Ampliables. Y adaptaciones <b>sin minorar</b> la calificación, con los mismos RA.</div>
    """,
    trucos=[
        "<b>6 (Grado D) y 4 (Grado E).</b> Como las convocatorias normales (4/2) pero dobladas.",
        "Adaptar no es bajar el nivel: mismos RA y criterios, <b>sin minorar</b> la nota.",
        "Discapacidad + expresión oral → flexibilización de lengua extranjera (art. 42.6 LOE).",
    ],
    trampas=[
        "Las adaptaciones <b>nunca</b> pueden minorar la calificación.",
        "El informe de orientación de Grado Básico es <b>confidencial y no prescriptivo</b>.",
        "La reserva de plaza para discapacidad está en la Orden 10/2024, art. 15.3.",
    ],
    normas=[("Orden 20/2019 (DOGV)", "https://dogv.gva.es/es/eli/es-vc/o/2019/04/30/20"),
            ("Decreto 72/2021 (DOGV)", "https://dogv.gva.es/es/eli/es-vc/d/2021/05/21/72")],
    cards=[
        ("¿Cuántas convocatorias puede agotar el alumnado con NEE en Grado D y E?",
         "Hasta 6 en Grado D y 4 en Grado E.", "Orden 8/2025 art. 9.7"),
        ("Si se agotan las convocatorias con NEE, ¿qué se puede hacer?",
         "Ampliarlas para los módulos pendientes si favorece terminar el ciclo.", "Instrucciones 2026-27 §16"),
        ("¿Qué tipo de adaptaciones se aplican y con qué límite?",
         "Metodología, ampliación de tiempos y recursos, sin que puedan minorar las calificaciones.", "Orden 8/2025 art. 2.4"),
        ("¿Cambian los referentes con las adaptaciones?",
         "No: siguen siendo los mismos RA, criterios de evaluación y competencias generales.", "Instrucciones 2026-27 §16"),
        ("¿Qué normas rigen la respuesta educativa para la inclusión?",
         "La Orden 20/2019 y el Decreto 72/2021.", "Orden 20/2019"),
        ("¿Qué medida hay para la lengua extranjera?",
         "Flexibilización y alternativas metodológicas para alumnado con discapacidad, en especial con dificultades de expresión oral, sin minorar la calificación.", "Instrucciones 2026-27 §16"),
        ("¿Qué informe se elabora en Grado Básico?",
         "Un informe de orientación individualizado, confidencial y no prescriptivo.", "Instrucciones 2026-27 §16"),
        ("¿Dónde está la reserva de plaza para personas con discapacidad?",
         "En la Orden 10/2024, art. 15.3.", "Orden 10/2024"),
    ],
    quiz=[
        ("Convocatorias máximas con NEE:",
         ["4 D / 2 E", "6 D / 4 E", "8 D / 6 E", "Ilimitadas"], 1,
         "6 en Grado D y 4 en Grado E, ampliables.", "Orden 8/2025 art. 9.7"),
        ("Las adaptaciones pueden…",
         ["Bajar la nota", "Aplicarse sin minorar las calificaciones", "Cambiar los RA", "Sustituir la evaluación"], 1,
         "No pueden minorar las calificaciones; los referentes son los mismos.", "Orden 8/2025 art. 2.4"),
        ("La flexibilización de lengua extranjera se centra en dificultades de…",
         ["Lectura", "Expresión oral", "Escritura", "Cálculo"], 1,
         "Especialmente en expresión oral (art. 42.6 LOE).", "Instrucciones 2026-27 §16"),
        ("El informe de orientación de Grado Básico es…",
         ["Público y vinculante", "Confidencial y no prescriptivo", "Numérico", "Solo para familias"], 1,
         "Confidencial y no prescriptivo.", "Instrucciones 2026-27 §16"),
        ("¿En qué norma está la reserva de plaza para discapacidad?",
         ["Orden 8/2025", "Orden 10/2024 art. 15.3", "RD 659/2023", "LO 3/2022"], 1,
         "Orden 10/2024, art. 15.3.", "Orden 10/2024"),
    ],
))

# ===========================================================================
# MÓDULO 12 · TRAMPAS Y REPASO INTEGRAL
# ===========================================================================
MODULES.append(dict(
    id="m12", title="Trampas y repaso integral", tagline="Las confusiones que más fallan y las tablas comparativas definitivas.",
    objetivos=[
        "Evitar las confusiones típicas entre cifras y trámites.",
        "Comparar de un vistazo todas las reglas «de números».",
        "Tener un método de repaso final antes del examen.",
    ],
    lesson="""
<h3>1. Parecidos que NO son lo mismo</h3>
<table>
<tr><th>Concepto A</th><th>Concepto B</th><th>Clave para no confundirlos</th></tr>
<tr><td>Anular matrícula (anexo I)</td><td>Renunciar a convocatoria (anexo III)</td><td>Anular = dejar el ciclo; renunciar = solo una convocatoria.</td></tr>
<tr><td>15% (matrícula)</td><td>15% (evaluación continua)</td><td>Matrícula: aviso 5%/8 días. Eval. continua: aviso 10%, por módulo.</td></tr>
<tr><td>240 h pendientes</td><td>80% de horas superadas</td><td>Son dos formas de decir lo mismo en GM/GS.</td></tr>
<tr><td>4 convocatorias (D)</td><td>2 convocatorias (E)</td><td>D = doble de E.</td></tr>
<tr><td>6 (D) / 4 (E) con NEE</td><td>4 (D) / 2 (E) normales</td><td>Con NEE, el doble.</td></tr>
<tr><td>Mención honorífica (módulo, 10%)</td><td>Matrícula de Honor (ciclo, ≥9)</td><td>Una es de módulo; la otra, de ciclo.</td></tr>
<tr><td>1 mes (anulación, convalidación)</td><td>2 meses (exención FE, gracia)</td><td>Gracia y exención: 2 meses.</td></tr>
<tr><td>5% / 8 días</td><td>10% / —</td><td>5% es matrícula; 10% es evaluación continua.</td></tr>
</table>

<h3>2. Tabla maestra de cifras</h3>
<table>
<tr><th>Tema</th><th>Cifra</th></tr>
<tr><td>Inasistencia que pierde la matrícula</td><td>15% o 10 días lectivos consecutivos (aviso 5% / 8 días)</td></tr>
<tr><td>Inasistencia que pierde la evaluación continua</td><td>15% por módulo (aviso 10%)</td></tr>
<tr><td>Presencialidad mínima</td><td>85%</td></tr>
<tr><td>Promoción GM/GS</td><td>≤ 240 h pendientes / ≥ 80% horas; >50% → 1000 h</td></tr>
<tr><td>Promoción Grado Básico</td><td>≤ 20% del horario semanal + un ámbito no profesional</td></tr>
<tr><td>Convocatorias</td><td>4 (D) / 2 (E); NEE 6 (D) / 4 (E)</td></tr>
<tr><td>Permanencia</td><td>Doble de cursos; 6 seguidos en virtual</td></tr>
<tr><td>Renuncia a convocatoria</td><td>Antes de 10 días hábiles (resuelve en 10 días hábiles)</td></tr>
<tr><td>Gracia</td><td>Dirección Territorial · ≤ 2 meses · 1 vez por módulo</td></tr>
<tr><td>Calificaciones de módulos</td><td>1-10 sin decimales (positiva ≥ 5); media con 2 decimales</td></tr>
<tr><td>Mención honorífica</td><td>10 en módulo · máximo 10% del grupo</td></tr>
<tr><td>Matrícula de Honor</td><td>≥ 9 · 2 GM / 3 GS (si &lt;20 alumnos, 1)</td></tr>
<tr><td>FE en 1.º de Grado D</td><td>Mínimo 100 h; plan en 1.er trimestre; inicio 2.º trimestre</td></tr>
<tr><td>Dualización</td><td>25-35% general · &gt;35-50% intensivo · 20% Básico · ≥35% en centro</td></tr>
<tr><td>Exención FE</td><td>6 meses (C/E) · 1 año (D) · 5 años · ≥10% RA → total</td></tr>
<tr><td>Ampliación plazas grados C</td><td>Hasta 10%</td></tr>
</table>

<h3>3. Método de repaso final</h3>
<ol>
<li><b>Recita las cifras</b> en voz alta con el taller de números hasta que no falles ninguna.</li>
<li><b>Repasa las fichas</b> en cajas bajas (0 y 1); son las que olvidas.</li>
<li><b>Haz los tests</b> de los módulos con dominio &lt; 80%.</li>
<li><b>Haz el examen final</b> hasta superar el 80% de forma estable.</li>
</ol>
    """,
    trucos=[
        "Cuando dudes entre dos cifras, pregúntate: <b>¿matrícula (5%) o evaluación continua (10%)?</b>",
        "Si es gracia o exención de FE → <b>2 meses</b>. Si es anulación o convalidación → <b>1 mes</b>.",
        "NEE siempre es <b>el doble</b> de las convocatorias normales.",
    ],
    trampas=[
        "El 15% de evaluación continua es <b>por módulo</b>; el 15% de matrícula, del curso (o del módulo en modular/no presencial).",
        "La mención honorífica y la Matrícula de Honor <b>no son lo mismo</b>.",
        "Un módulo convalidado <b>no</b> convalida otros módulos.",
    ],
    normas=[("Guía de referencia", "../index.html")],
    cards=[
        ("¿Qué diferencia hay entre anular matrícula y renunciar a una convocatoria?",
         "Anular (anexo I) deja el ciclo y pierde la plaza; renunciar (anexo III) solo afecta a una convocatoria concreta.", "Repaso"),
        ("¿Qué aviso se da en cada umbral de inasistencia?",
         "Pérdida de matrícula: aviso al 5% o 8 días. Pérdida de evaluación continua: aviso al 10%.", "Repaso"),
        ("¿Cómo se relacionan 240 h pendientes y 80% de horas superadas?",
         "Son dos fórmulas equivalentes del criterio de promoción en GM/GS.", "Repaso"),
        ("Convocatorias normales y con NEE, en D y E:",
         "Normal: 4 (D) / 2 (E). Con NEE: 6 (D) / 4 (E), ampliables.", "Repaso"),
        ("Diferencia entre mención honorífica y Matrícula de Honor:",
         "La mención es por un 10 en un módulo (máx. 10% del grupo); la Matrícula de Honor es por nota final ≥9 (2 GM / 3 GS).", "Repaso"),
        ("¿Qué trámites se resuelven en 1 mes y cuáles en 2?",
         "1 mes: anulación de matrícula y convalidación. 2 meses: exención de FE/FCT y convocatoria de gracia.", "Repaso"),
        ("¿Quién paga la Seguridad Social de la FE general y de la FCT?",
         "La Dirección General de FP (también las hechas en administraciones públicas).", "Repaso"),
        ("¿Cuál es el porcentaje mínimo del módulo que se imparte en el centro al dualizar?",
         "El 35%; y el Proyecto Intermodular no se dualiza.", "Repaso"),
    ],
    quiz=[
        ("¿Cuál de estos trámites se resuelve en 2 meses?",
         ["Anulación de matrícula", "Convalidación", "Exención de FE/FCT", "Renuncia a convocatoria"], 2,
         "Exención de FE/FCT y gracia: 2 meses. Anulación y convalidación: 1 mes.", "Repaso"),
        ("El aviso al 10% de inasistencia corresponde a…",
         ["La pérdida de matrícula", "La pérdida de evaluación continua", "La renuncia a convocatoria", "La gracia"], 1,
         "Evaluación continua: pierde al 15%, aviso al 10%.", "Repaso"),
        ("Con NEE, las convocatorias en Grado D y E son…",
         ["4 y 2", "6 y 4", "6 y 6", "Ilimitadas"], 1,
         "6 en Grado D y 4 en Grado E.", "Repaso"),
        ("¿Qué módulo no se puede dualizar?",
         ["Digitalización", "Sostenibilidad", "Proyecto Intermodular", "Inglés profesional"], 2,
         "El Proyecto Intermodular queda fuera de la dualización.", "Repaso"),
        ("¿Cuál de estas afirmaciones es FALSA?",
         ["Un módulo convalidado no convalida otros módulos", "«Convalidado sin nota» no cuenta para la media", "La mención honorífica es lo mismo que la Matrícula de Honor", "La nota final de GM/GS es la media con 2 decimales"], 2,
         "Mención honorífica (módulo, 10) y Matrícula de Honor (ciclo, ≥9) son cosas distintas.", "Repaso"),
        ("¿Cuántas horas mínimas de FE hace 1.º de Grado D?",
         ["50", "100", "200", "240"], 1,
         "Mínimo 100 horas.", "Repaso"),
        ("La estancia en empresa en FP Dual intensiva es…",
         ["10-20%", "25-35%", ">35% hasta 50%", ">50%"], 2,
         "Intensiva: >35% hasta 50%, con >30% de RA en empresa.", "Repaso"),
        ("¿Qué porcentaje de ampliación de plazas permite venir de un grado C?",
         ["5%", "10%", "20%", "No se permite"], 1,
         "Hasta un 10%, con la comisión sectorial.", "Repaso"),
    ],
))

# ===========================================================================
# MÓDULO 13 · OTROS ASPECTOS I (ORDENACIÓN Y CURRÍCULO)
# ===========================================================================
MODULES.append(dict(
    id="m13", title="Otros aspectos I: ordenación y currículo", tagline="FP LOE y LOGSE, Grado Básico anterior y cursos de especialización.",
    objetivos=[
        "Situar el RD 1147/2011 y la FP de ciclos LOE junto a LOGSE y LFP.",
        "Recordar la normativa anterior del Grado Básico y de la especialización.",
        "Identificar correcciones y modificaciones recientes.",
    ],
    lesson="""
<h3>1. Tres generaciones de FP que conviven</h3>
<table>
<tr><th>Generación</th><th>Norma clave</th><th>Qué ordena</th></tr>
<tr><td><b>LFP</b> (nueva)</td><td>LO 3/2022 + RD 659/2023</td><td>Grados A-E; el Grado D son los ciclos actuales.</td></tr>
<tr><td><b>LOE</b></td><td><b>RD 1147/2011</b>, de 29 de julio</td><td>Ordenación general de la FP; se aplica a los <b>ciclos LOE</b>.</td></tr>
<tr><td><b>LOGSE</b> (antigua)</td><td>Orden 78/2010 y Orden 79/2010</td><td>Ordenación y evaluación de los ciclos LOGSE.</td></tr>
</table>
<div class="callout info">La web de la Conselleria mantiene una <b>tabla de familias profesionales LOGSE</b> con los títulos antiguos y el curso en que fueron sustituidos. Es material <b>histórico</b> de consulta, no temario nuevo.</div>

<h3>2. Grado Básico: normativa anterior</h3>
<ul>
<li>En la Comunitat, el Grado Básico se desarrolló con el <b>Decreto 135/2014</b>, de 8 de agosto, modificado por el <b>Decreto 36/2020</b>, de 13 de marzo.</li>
<li>Hoy los currículos de Grado Básico están en el <b>Decreto 117/2025</b> (modificado por el <b>Decreto 95/2026</b>).</li>
</ul>

<h3>3. Cursos de especialización</h3>
<ul>
<li>Primera ordenación autonómica: <b>Resolución de 26 de abril de 2023</b> (DOGV 11/05/2023).</li>
<li>Hoy: <b>Decreto 95/2026</b>, de 19 de junio (currículos), con <b>Corrección de errores</b> publicada el 29/06/2026.</li>
</ul>

<h3>4. Modificaciones recientes que debes tener presentes</h3>
<ul>
<li>El <b>Decreto 95/2026</b> modifica los Decretos <b>114/2025</b> y <b>117/2025</b> y, a la vez, regula los currículos de especialización.</li>
<li>La <b>Orden 5/2026</b> modifica la Orden 8/2025 de evaluación.</li>
<li>Existe una <b>corrección de errores</b> del Decreto 95/2026: conviene mirar el texto consolidado con la corrección incorporada.</li>
</ul>
    """,
    trucos=[
        "<b>LOGSE → Orden 78/79 de 2010. LOE → RD 1147/2011. LFP → Grado D (LO 3/2022).</b>",
        "Grado Básico antiguo: <b>Decreto 135/2014</b> (mod. <b>36/2020</b>). Actual: <b>117/2025</b>.",
        "Especialización: de <b>Resolución 26/04/2023</b> a <b>Decreto 95/2026</b> (+ corrección de errores).",
    ],
    trampas=[
        "El <b>RD 1147/2011</b> NO es la norma de los ciclos actuales: es la ordenación de los ciclos <b>LOE</b>.",
        "El Decreto 95/2026 tiene <b>corrección de errores</b> (29/06/2026); no cites solo la versión inicial.",
        "La tabla de familias LOGSE son títulos <b>sustituidos</b>: es histórico, no normativa vigente.",
    ],
    normas=[("RD 1147/2011", "https://www.boe.es/eli/es/rd/2011/07/29/1147/con"),
            ("Decreto 135/2014", "https://dogv.gva.es/es/eli/es-vc/d/2014/08/08/135"),
            ("Resolución 26/04/2023", "https://dogv.gva.es/datos/2023/05/11/pdf/2023_4695.pdf"),
            ("Corrección Decreto 95/2026", "https://dogv.gva.es/va/eli/es-vc/d/2026/06/19/95/corrigendum/20260629")],
    cards=[
        ("¿Qué norma ordena la FP de los ciclos LOE?",
         "El RD 1147/2011, de 29 de julio, por el que se establece la ordenación general de la FP.", "RD 1147/2011"),
        ("¿Qué normativa rige los ciclos LOGSE en la Comunitat?",
         "La Orden 78/2010 (ordenación) y la Orden 79/2010 (evaluación).", "Orden 78/2010"),
        ("¿Qué información contiene la tabla de familias profesionales LOGSE de la web?",
         "Los títulos LOGSE antiguos y el curso en que fueron sustituidos por los nuevos; es material histórico.", "Web Conselleria"),
        ("¿Con qué decreto se desarrolló el Grado Básico en la Comunitat antes?",
         "El Decreto 135/2014, de 8 de agosto, modificado por el Decreto 36/2020.", "Decreto 135/2014"),
        ("¿Qué norma regula hoy los currículos de Grado Básico?",
         "El Decreto 117/2025 (modificado por el Decreto 95/2026).", "Decreto 117/2025"),
        ("¿Qué Resolución ordenó por primera vez los cursos de especialización en la Comunitat?",
         "La Resolución de 26 de abril de 2023 (DOGV 11/05/2023).", "Resolución 26/04/2023"),
        ("¿Qué norma regula hoy los currículos de los cursos de especialización?",
         "El Decreto 95/2026, de 19 de junio.", "Decreto 95/2026"),
        ("¿Qué particularidad tiene el Decreto 95/2026?",
         "Modifica los Decretos 114/2025 y 117/2025 y regula los currículos de especialización; además tiene corrección de errores.", "Corrección 29/06/2026"),
    ],
    quiz=[
        ("¿Qué norma se aplica a los ciclos LOE?",
         ["LO 3/2022", "RD 1147/2011", "Orden 8/2025", "Decreto 95/2026"], 1,
         "El RD 1147/2011 es la ordenación general aplicable a los ciclos LOE.", "RD 1147/2011"),
        ("El Decreto 135/2014 se refiere a…",
         ["Los cursos de especialización", "El Grado Básico (normativa anterior)", "La FP Dual", "La admisión"], 1,
         "Desarrollaba el Grado Básico y fue modificado por el Decreto 36/2020.", "Decreto 135/2014"),
        ("¿Qué norma modificó los Decretos 114/2025 y 117/2025?",
         ["La Orden 5/2026", "El Decreto 95/2026", "El RD 278/2023", "La Orden 10/2024"], 1,
         "El Decreto 95/2026, que además regula la especialización.", "Decreto 95/2026"),
        ("¿Qué documento corrige el Decreto 95/2026?",
         ["Una Orden posterior", "La Corrección de errores (29/06/2026)", "Un real decreto", "Nada"], 1,
         "Existe corrección de errores publicada el 29/06/2026.", "Corrección 29/06/2026"),
        ("La tabla de familias LOGSE de la web es…",
         ["Normativa vigente", "Material histórico con títulos sustituidos", "Un listado de becas", "Un calendario"], 1,
         "Recoge títulos LOGSE sustituidos por los nuevos; es histórico.", "Web Conselleria"),
    ],
))

# ===========================================================================
# MÓDULO 14 · OTROS ASPECTOS II (ALUMNADO, TÍTULOS Y ORGANIZACIÓN)
# ===========================================================================
MODULES.append(dict(
    id="m14", title="Otros aspectos II: alumnado, títulos y organización", tagline="Extranjeros, PRL, ECTS, intermodular, calendario, desdobles, optatividad y anexos.",
    objetivos=[
        "Conocer las vías de incorporación y de acceso a la universidad.",
        "Situar la PRL, el Proyecto intermodular y el calendario escolar.",
        "Manejar desdobles, optatividad y anexos frecuentes.",
    ],
    lesson="""
<h3>1. Alumnado procedente de sistemas extranjeros</h3>
<p>Las <b>Instrucciones de 16 de julio de 2019</b> del SAEFP establecen directrices para el <b>alumnado que se incorpora al sistema educativo español</b> procedente de centros de titularidad extranjera o de sistemas educativos de otros países.</p>

<h3>2. Prevención de riesgos laborales (PRL)</h3>
<p>La <b>Orden 1/2014</b>, de 8 de agosto, regula la <b>certificación de la formación en prevención de riesgos laborales</b> y de su nivel básico para el alumnado de FP. Es la base del requisito de PRL para iniciar la FE.</p>

<h3>3. Acceso a la universidad desde Grado Superior y créditos ECTS</h3>
<ul>
<li><b>Resolución de 26 de abril de 2024</b>: correspondencias entre los títulos de <b>Técnico/a Superior</b>, los títulos universitarios de grado de las universidades de la Comunitat y los títulos de grado en <b>enseñanzas artísticas superiores</b>, así como el reconocimiento de <b>créditos ECTS</b>.</li>
<li><b>Art. 130 del RD 659/2023</b>: regula el reconocimiento de créditos entre el Sistema de FP y el Sistema Universitario. Las titulaciones figuran en el <b>Anexo XI</b> del RD 659/2023.</li>
<li>Para la <b>PAU</b>, el equipo docente adelanta la evaluación final (ya visto en el módulo 5).</li>
</ul>

<h3>4. Proyecto intermodular y documentos de trabajo</h3>
<ul>
<li>La DGFP publica una <b>guía para la elaboración del Proyecto intermodular</b>.</li>
<li>Sobre la pérdida de evaluación continua hay un <b>modelo de comunicación</b> oficial.</li>
<li><b>Secuenciación y horarios</b> de los ciclos: se publican en la web de FP en aplicación del <b>RD 659/2023</b>.</li>
</ul>

<h3>5. Calendario escolar 2026-27</h3>
<ul>
<li><b>Resolución de 15 de junio de 2026</b> (DOGV 18/06/2026): fija el calendario escolar del curso 2026-2027 en la Comunitat.</li>
<li>Los <b>cursos de especialización</b> se iniciaron el <b>1 de octubre</b> y finalizan como máximo el <b>18 de junio de 2027</b>.</li>
</ul>

<h3>6. Profesorado y centro: desdobles y optatividad</h3>
<ul>
<li><b>Desdobles de profesorado</b>:
  <ul>
    <li><b>Resolución de 2 de diciembre de 2022</b>: publica la relación de especialidades por ciclos cuya dedicación es susceptible de desdoble en centros públicos.</li>
    <li><b>Resolución de 19 de junio de 2023</b>: la actualiza (con corrección de errores de 05/07/2023).</li>
    <li><b>Resolución de 16 de noviembre de 2023</b>: autoriza nuevos desdobles en función de la matrícula definitiva.</li>
  </ul>
</li>
<li><b>Optatividad</b>: existen <b>instrucciones sobre la oferta de módulos optativos</b> (curso 2025-2026) y los listados de módulos optativos presentados por los centros.</li>
</ul>

<h3>7. Anexos frecuentes de la web</h3>
<table>
<tr><th>Anexo</th><th>Contenido</th></tr>
<tr><td><b>VII</b></td><td>Solicitud de anulación de matrícula.</td></tr>
<tr><td><b>IX</b></td><td>Solicitud de renuncia de convocatorias.</td></tr>
<tr><td><b>X</b></td><td>Solicitud de exención de FCT.</td></tr>
<tr><td><b>XIII</b></td><td>Solicitud de aplazamiento de calificación de FCT.</td></tr>
</table>
<div class="callout warn"><b>Ojo con la numeración:</b> las <b>Instrucciones 2026-27</b> usan <b>I</b> (anulación), <b>III</b> (renuncia) y <b>IV</b> (convalidación). Los anexos VII/IX/X/XIII son los de la sección general de la web.</div>

<h3>8. Otras secciones normativas de la web</h3>
<p>Además de «Aspectos normativos», la web de FP agrupa: <b>Evaluación</b>, <b>Convalidaciones</b>, <b>Convocatorias</b>, <b>Oferta integrada</b>, <b>Acceso a la universidad desde Grado Superior</b>, <b>Planificación</b>, <b>Guías y manuales de centros</b> y <b>Formación en Empresa, FCT y Dual</b>.</p>
    """,
    trucos=[
        "Extranjeros → <b>Instrucciones 16/07/2019</b>. PRL → <b>Orden 1/2014</b>.",
        "TS ↔ universidad: <b>Resolución 26/04/2024</b> + <b>art. 130 RD 659/2023</b> (Anexo XI).",
        "Anexos web: <b>VII anular · IX renunciar · X exención FCT · XIII aplazar FCT</b>.",
        "Calendario 2026-27: <b>Resolución 15/06/2026</b>; especialización del 1/10 al 18/06/2027.",
    ],
    trampas=[
        "Los anexos <b>I/III/IV</b> (Instrucciones 2026-27) NO son los mismos que <b>VII/IX/X/XIII</b> (web).",
        "El reconocimiento de créditos FP-universidad está en el <b>art. 130</b> del RD 659/2023, no en la LO 3/2022.",
        "La PRL no es solo un contenido: su certificación se regula en la <b>Orden 1/2014</b>.",
    ],
    normas=[("Orden 1/2014", "https://dogv.gva.es/datos/2014/08/13/pdf/2014_7666.pdf"),
            ("Resolución 26/04/2024", "https://dogv.gva.es/datos/2024/04/30/pdf/2024_3733.pdf"),
            ("Calendario escolar 2026-27", "https://dogv.gva.es/datos/2026/06/18/pdf/2026_20810_es.pdf"),
            ("Normativa FP (Conselleria)", "https://ceice.gva.es/es/web/formacion-profesional/normativa-sobre-ordenacion-y-organizacion-academica-de-los-ciclos-formativos")],
    cards=[
        ("¿Qué instrucciones rigen para el alumnado que llega de centros o sistemas extranjeros?",
         "Las Instrucciones de 16 de julio de 2019 del SAEFP, sobre incorporación al sistema educativo español.", "Instrucciones 16/07/2019"),
        ("¿Qué norma regula la certificación de la formación en PRL del alumnado de FP?",
         "La Orden 1/2014, de 8 de agosto (PRL y su nivel básico).", "Orden 1/2014"),
        ("¿Qué regula la Resolución de 26 de abril de 2024?",
         "Las correspondencias entre títulos de Técnico Superior, grados universitarios y enseñanzas artísticas superiores, y el reconocimiento de ECTS.", "Resolución 26/04/2024"),
        ("¿Dónde se regula el reconocimiento de créditos entre FP y Universidad?",
         "En el art. 130 del RD 659/2023 (titulaciones del Anexo XI).", "RD 659/2023 art. 130"),
        ("¿Qué documento guía el Proyecto intermodular?",
         "La guía para la elaboración del Proyecto intermodular de la DGFP.", "Guía DGFP"),
        ("¿Qué fija la Resolución de 15 de junio de 2026?",
         "El calendario escolar del curso 2026-2027 en la Comunitat Valenciana.", "Resolución 15/06/2026"),
        ("¿Cuándo se inician y cuándo acaban como máximo los cursos de especialización?",
         "Se inician el 1 de octubre y finalizan como máximo el 18 de junio de 2027.", "Instrucciones 2026-27 §17.3"),
        ("¿Qué resoluciones afectan a los desdobles de profesorado?",
         "La de 2/12/2022 (especialidades), la de 19/06/2023 (actualización, con corrección de 05/07/2023) y la de 16/11/2023 (nuevos desdobles por matrícula).", "Resoluciones de desdobles"),
        ("¿Qué son las instrucciones de optatividad?",
         "Las que regulan la oferta de módulos optativos (curso 2025-2026) y los listados presentados por los centros.", "Optatividad"),
        ("¿Qué es el anexo VII?",
         "Solicitud de anulación de matrícula (sección general de la web).", "Anexo VII"),
        ("¿Qué es el anexo IX?",
         "Solicitud de renuncia de convocatorias.", "Anexo IX"),
        ("¿Qué es el anexo X?",
         "Solicitud de exención de FCT.", "Anexo X"),
        ("¿Qué es el anexo XIII?",
         "Solicitud de aplazamiento de calificación de FCT.", "Anexo XIII"),
        ("¿Qué otras secciones normativas agrupa la web de FP?",
         "Evaluación, Convalidaciones, Convocatorias, Oferta integrada, Acceso a la universidad desde GS, Planificación, Guías y manuales de centros y FE/FCT/Dual.", "Web Conselleria"),
    ],
    quiz=[
        ("El alumnado procedente de sistemas educativos extranjeros se rige por…",
         ["La Orden 1/2014", "Las Instrucciones de 16/07/2019 del SAEFP", "El Decreto 95/2026", "La Orden 5/2022"], 1,
         "Instrucciones de 16 de julio de 2019 sobre incorporación al sistema educativo español.", "Instrucciones 16/07/2019"),
        ("La certificación de PRL para el alumnado de FP está en…",
         ["El RD 659/2023", "La Orden 1/2014", "La LO 3/2022", "La Orden 8/2025"], 1,
         "Orden 1/2014, de 8 de agosto.", "Orden 1/2014"),
        ("Las correspondencias TS-universidad y ECTS se recogen en…",
         ["La LO 3/2022", "La Resolución de 26/04/2024", "El Decreto 135/2014", "La Orden 78/2010"], 1,
         "Resolución de 26/04/2024, junto con el art. 130 del RD 659/2023.", "Resolución 26/04/2024"),
        ("El reconocimiento de créditos entre FP y Universidad se regula en…",
         ["El art. 130 del RD 659/2023", "El art. 42.6 de la LOE", "La Orden 10/2024", "El Decreto 117/2025"], 0,
         "Art. 130 del RD 659/2023 (Anexo XI).", "RD 659/2023 art. 130"),
        ("¿Qué anexo corresponde a la solicitud de aplazamiento de calificación de FCT?",
         ["VII", "IX", "X", "XIII"], 3,
         "Anexo XIII. VII: anulación; IX: renuncia; X: exención de FCT.", "Anexo XIII"),
        ("El calendario escolar 2026-27 se fija por…",
         ["Resolución de 15/06/2026", "Orden 8/2025", "Decreto 95/2026", "RD 278/2023"], 0,
         "Resolución de 15 de junio de 2026 (DOGV 18/06/2026).", "Resolución 15/06/2026"),
        ("Los desdobles de profesorado se autorizan por…",
         ["Resoluciones de la Conselleria", "La LO 3/2022", "El RD 1147/2011", "Un decreto ley"], 0,
         "Resoluciones de 2/12/2022, 19/06/2023 (con corrección) y 16/11/2023.", "Desdobles"),
    ],
))

# ===========================================================================
# TALLER DE NÚMEROS CLAVE
# ===========================================================================
NUMBERS = [
    {"q": "Inasistencia que hace PERDER LA MATRÍCULA", "a": "15% o 10 días lectivos consecutivos"},
    {"q": "Aviso de posible pérdida de matrícula", "a": "5% o 8 días lectivos consecutivos"},
    {"q": "Inasistencia que hace perder la EVALUACIÓN CONTINUA de un módulo", "a": "15% (aviso al 10%)"},
    {"q": "Presencialidad mínima exigible", "a": "85%"},
    {"q": "Plazo para renunciar a una convocatoria", "a": "Antes de 10 días hábiles"},
    {"q": "Plazo de resolución de una renuncia de convocatoria", "a": "10 días hábiles"},
    {"q": "Plazo de resolución de una anulación de matrícula", "a": "1 mes (silencio estimatorio)"},
    {"q": "Plazo de resolución de una convalidación", "a": "1 mes (anexo IV)"},
    {"q": "Plazo de resolución de una exención de FE/FCT", "a": "2 meses"},
    {"q": "Plazo de resolución de la convocatoria de gracia", "a": "Máximo 2 meses"},
    {"q": "Horas de solicitud de exención de FE antes del inicio", "a": "Al menos 30 días antes"},
    {"q": "Experiencia para exención en grados C y E", "a": "6 meses"},
    {"q": "Experiencia para exención en grados D", "a": "1 año a tiempo completo o equivalente"},
    {"q": "RA necesarios para exención TOTAL de FE", "a": "≥ 10% de los RA de módulos asociados a estándares"},
    {"q": "Años en que debe acreditarse la experiencia de exención", "a": "5 años anteriores"},
    {"q": "Convocatorias máximas por módulo en Grado D", "a": "4 (2 por curso)"},
    {"q": "Convocatorias máximas por módulo en Grado E", "a": "2"},
    {"q": "Convocatorias con NEE en Grado D y E", "a": "6 y 4 (ampliables)"},
    {"q": "Permanencia máxima en modalidad virtual", "a": "6 cursos consecutivos"},
    {"q": "Módulos pendientes máximos para promocionar en GM/GS", "a": "240 horas"},
    {"q": "Porcentaje de horas de 1.º que hay que superar (Orden 8/2025)", "a": "80%"},
    {"q": "Horas superadas de 1.º que permiten matricularse de 2.º hasta 1000 h", "a": "Más del 50%"},
    {"q": "Pendientes máximos en Grado Básico", "a": "20% del horario semanal"},
    {"q": "Calificación de los módulos profesionales", "a": "1 a 10, sin decimales (positiva ≥ 5)"},
    {"q": "Decimales de la nota final de GM/GS", "a": "2 decimales"},
    {"q": "Nota final si TODO es «convalidado sin nota»", "a": "5"},
    {"q": "Porcentaje máximo de menciones honoríficas por grupo", "a": "10% del alumnado del módulo"},
    {"q": "Matrículas de Honor máximas en GM y GS", "a": "2 en GM y 3 en GS (si <20 alumnos, 1)"},
    {"q": "Nota mínima para Matrícula de Honor", "a": "≥ 9"},
    {"q": "Horas mínimas de FE en 1.º de Grado D", "a": "100 horas"},
    {"q": "Estancia en empresa en FP Dual general", "a": "25-35% (RA 10-20%)"},
    {"q": "Estancia en empresa en FP Dual intensiva", "a": ">35% hasta 50% (RA >30%)"},
    {"q": "Estancia en empresa en Grado Básico", "a": "20% de las horas"},
    {"q": "Porcentaje mínimo del módulo que se imparte en el centro", "a": "35%"},
    {"q": "Ampliación de plazas por venir de un grado C", "a": "Hasta 10%"},
    {"q": "Vacantes de oferta modular 2026-27", "a": "Antes del 15 de octubre de 2026"},
    {"q": "Matrícula de oferta modular 2026-27", "a": "Antes del 11 de diciembre de 2026"},
    {"q": "Norma que ordena la FP de los ciclos LOE", "a": "RD 1147/2011"},
    {"q": "Normas de ordenación y evaluación de los ciclos LOGSE", "a": "Orden 78/2010 y Orden 79/2010"},
    {"q": "Norma anterior del Grado Básico (Comunitat)", "a": "Decreto 135/2014 (mod. por Decreto 36/2020)"},
    {"q": "Norma que regula la certificación de PRL del alumnado", "a": "Orden 1/2014"},
    {"q": "Artículo del RD 659/2023 sobre créditos FP-Universidad", "a": "Art. 130 (Anexo XI)"},
    {"q": "Calendario escolar del curso 2026-27", "a": "Resolución de 15 de junio de 2026"},
    {"q": "Inicio y fin máximo de los cursos de especialización 2026-27", "a": "1 de octubre a 18 de junio de 2027"},
    {"q": "Anexos: anulación / renuncia / exención FCT / aplazamiento FCT", "a": "VII / IX / X / XIII"},
    {"q": "Plazo de corrección de errores del Decreto 95/2026", "a": "29 de junio de 2026"},
]

