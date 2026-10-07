# Cómo actualizar la normativa de la guía

La web (`index.html`) se genera a partir de:

- `build/sources/*.txt` → textos oficiales convertidos a texto plano.
- `build/build.py` → parsea esos textos, genera `build/normdata.json` e
  inyecta `window.NORMDATA` dentro de `index.html`.
- El lector de texto literal (script al final de `index.html`) resuelve las
  etiquetas de las fichas a partes concretas de cada norma.

Todo el contenido visible de las fichas (las tarjetas de «Qué dice la norma»)
se edita a mano directamente en `index.html`.

---

## 1. Actualizar una norma existente (p. ej. nuevas Instrucciones de curso)

1. Descarga el PDF oficial (DOGV/BOE) de la nueva resolución.
2. Conviértelo a texto plano y guárdalo en `build/sources/`:
   ```bash
   pdftotext -layout resolución.pdf build/sources/instr2728.txt
   ```
   Conviene limpiar cabeceras y pies de página (CVE, «Núm. X / DD.MM.AAAA»,
   números de página…) con el patrón que ya usa `prefilter()`.
3. En `build/build.py`, dentro de `DOCS`, ajusta la entrada correspondiente
   (`short`, `title`, `source`, `url`, `file`, `parser`).
4. Si cambia la posición por rango, reordena `ORDER` (las claves).
5. Regenera los datos:
   ```bash
   python3 build/build.py
   ```
6. Si cambian las referencias de las fichas (p. ej. «Instrucciones 2026-27
   §9.6» → «Instrucciones 2027-28 §9.6»), actualiza:
   - las etiquetas de las tarjetas en `index.html`, y
   - el patrón en la función `resolve()` del lector si el nombre cambia.

El script es **idempotente**: si los datos no cambian, termina sin error.

## 2. Añadir una norma nueva con texto íntegro

1. Salva el texto en `build/sources/<clave>.txt` (ver paso 1.2).
2. Añade su entrada en `DOCS` de `build/build.py`:
   - `parser="instr"` si es un documento con apartados numerados `1., 1.1…`
     (como las Instrucciones de curso).
   - `parser="art"` si es un articulado (Ley, Real Decreto, Orden…).
   - Para los Decretos de currículo con anexos enormes usa
     `cut_annex=True`.
3. Indica su rango en `DOC_PRIO` (y, si quieres una etiqueta propia, en
   `PRIO_LABEL`). Los rangos posibles están en `TIERS` (1 = Ley Orgánica … 7 =
   Resolución/Instrucciones).
4. Añade la clave a `ORDER` en su posición por rango.
5. Si quieres que las fichas enlacen a partes concretas, añade el patrón de
   resolución en `resolve()` dentro de `index.html`.
6. `python3 build/build.py`.

## 3. Añadir una norma citada SIN texto íntegro

Si la norma solo se cita (p. ej. «RD 278/2023») y no quieres incrustar su
texto:

1. Añade una entrada en `EXTRAS` (clave, `short`, `title`, `source`, `url` y
   `prio`).
2. Añade la clave a `EXTRA_ORDER` por rango.
3. Añade su patrón en `resolve()` (devuelve `docCite("<clave>")`) para que la
   etiqueta sea clicable.
4. `python3 build/build.py`.

Aparecerá en la biblioteca en «Otras normas citadas» con su enlace oficial.

## 4. Referencias rápidas

| Acción | Comando |
|---|---|
| Regenerar datos e inyectar en la web | `python3 build/build.py` |
| Ver el JSON intermedio | `build/normdata.json` |
| Servir la web localmente | `python3 -m http.server 8765` → `http://127.0.0.1:8765` |

## Notas

- Los rangos y colores de prioridad se definen en `TIERS` (`build.py`) y en
  la tabla `PRIO` del lector (`index.html`).
- Las secciones «Partes citadas en esta guía» y «Otros elementos de interés»
  de cada documento se calculan automáticamente al cargar la página, a partir
  de las etiquetas de las tarjetas.
- El idioma de las instrucciones de curso puede venir en valenciano en el
  DOGV; el parseo (`parse_instructions`) busca «^1\. Ámbito de aplicación»,
  ajústalo si el encabezado cambia.