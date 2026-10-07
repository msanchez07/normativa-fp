# Curso intensivo de normativa de FP

Web autónoma para **aprender y memorizar** la normativa de Formación Profesional
de la Comunitat Valenciana (curso 2026-27).

## Cómo usarla

Abre `curso/index.html` con doble clic. No necesita servidor.

Si tu navegador bloquea algo al abrirlo como archivo, sirve la carpeta:

```bash
python3 -m http.server 8765
# http://127.0.0.1:8765/curso/index.html
```

## Qué incluye

- **Plan y progreso**: dominio por módulo, repaso pendiente y plan intensivo de 14 días.
- **Lecciones** (14): fundamentos, arquitectura normativa, acceso y matrícula,
  anulación y pérdida, evaluación, convocatorias, promoción, calificaciones y
  titulación, convalidaciones, FE/FCT/Dual, NEE, repaso integral con trampas y dos
  módulos de otros aspectos normativos (LOE/LOGSE, PRL, extranjeros, ECTS,
  Proyecto intermodular, calendario, desdobles, optatividad y anexos).
- **Fichas con repetición espaciada (SRS)**: cajas de 0 a 16 días; repasa solo lo
  que toca cada día. 150 fichas en total.
- **Tests por módulo** con corrección y explicación. 87 preguntas.
- **Examen final**: 30 preguntas aleatorias, 25 minutos, se aprueba con 80%.
- **Taller de 46 números clave**: las cifras que más se fallan, con modo interrogatorio.

El progreso se guarda en el navegador (`localStorage`).

## Mantenimiento

El contenido está en `build/curso_data.py` (módulos, fichas, preguntas, números y
plan) y el motor en `build/build_curso.py`. Para regenerar:

```bash
python3 build/build_curso.py
```

Esto reescribe `curso/index.html`. No usa datos de `build/normdata.json` salvo
para estadísticas; el contenido se edita a mano.
