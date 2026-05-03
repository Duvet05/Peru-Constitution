# Historical Edits of the Peru Constitution

La Constitucion Politica del Peru ha sido modificada muchas veces desde 1993. Esas reformas normalmente aparecen como leyes, notas editoriales y textos actualizados en PDF.

Este repositorio intenta responder una pregunta simple: como se ve la Constitucion vigente si tratamos cada reforma constitucional como un commit?

La meta es que `git blame constitucion.md` muestre que ley introdujo o modifico cada linea.

## Estado

Proyecto inicial. Incluye:

- fuentes oficiales conocidas;
- scripts para descargar y normalizar texto;
- un inventario completo de reformas constitucionales;
- un manifest editable para reconstruir commits historicos;
- snapshots reconstruidos por reforma individual desde 2015: leyes 30305, 30558, 30588 y 30650;
- una herramienta para reconstruir un repo historico desde snapshots.

La fuente oficial vigente usada como referencia inicial es la edicion del Congreso de la Republica de diciembre de 2024. El primer snapshot completo proviene de ese PDF oficial y conserva las anotaciones editoriales del Congreso, porque el objetivo es publicar una Constitucion vigente y anotada.

## Fuentes oficiales

- Constitucion vigente, pagina del Congreso: `https://www.congreso.gob.pe/datos-generales/constitucion-del-peru-y-reglamento/`
- PDF oficial, edicion diciembre 2024: `https://www3.congreso.gob.pe/Docs/files/constitucion/constitucion-12-2024.pdf`
- Biblioteca del Congreso, constituciones historicas: `https://www.congreso.gob.pe/biblioteca/constituciones_peru/`
- Texto HTML historico de 1993, si vuelve a estar disponible: `https://www.congreso.gob.pe/Docs/sites/webs/quipu/constitu/1993.htm`

## Estructura

```text
sources/              fuentes descargadas, no editadas
snapshots/            textos normalizados por fecha
reformas.csv          manifest de reformas y snapshots
metadata/             inventario historico y fuentes
constitucion.md       texto vigente que queda versionado por Git
scripts/              utilidades de descarga, normalizacion e historial
```

## Uso

Descargar fuentes:

```sh
./scripts/fetch_sources.sh
```

Normalizar un HTML oficial:

```sh
./scripts/html_to_text.py sources/archivo-oficial.html snapshots/YYYY-MM-DD.md
```

Extraer un snapshot desde el PDF oficial del Congreso:

```sh
./scripts/pdf_to_snapshot.py sources/constitucion-12-2024.pdf snapshots/2024-12-11.md
./scripts/canonicalize_snapshot.py snapshots/2024-12-11.md snapshots/2024-12-11.md
```

Validar que el snapshot contenga los articulos esperados:

```sh
./scripts/validate_snapshot.py snapshots/2024-12-11.md
./scripts/validate_snapshot.py snapshots/2024-12-11.md --current
```

Auditar detalles de extraccion del PDF:

```sh
./scripts/audit_snapshot.py constitucion.md --current
```

Reconstruir el historial en un repo nuevo:

```sh
./scripts/build_history.py reformas.csv build/constitucion-peru-history
```

Luego puedes inspeccionar:

```sh
cd build/constitucion-peru-history
git log --oneline
git blame constitucion.md
```

## Como completar el proyecto

1. Usa `metadata/reformas-constitucionales.csv` como checklist de reformas.
2. Coloca en `snapshots/` un archivo por cada reforma constitucional relevante.
3. Registra cada snapshot listo para reconstruccion en `reformas.csv` con fecha, norma, fuente y descripcion.
4. Ejecuta `scripts/build_history.py` para crear un repo historico limpio.
5. Revisa `git diff` entre commits para detectar errores de OCR, saltos de linea o notas editoriales.

## Blame

Cuando el historial este construido, `git blame` permite ver que reforma introdujo cada linea:

```sh
git blame constitucion.md
git blame -w constitucion.md
```

La opcion `-w` ignora cambios de espacios y ayuda cuando hubo normalizacion de formato.

El historial ya incluye un hito oficial de 2013, las leyes 30305, 30558, 30588 y 30650 como commits reconstruidos por reforma individual, y la edicion anotada de diciembre de 2024. El siguiente trabajo es seguir reemplazando el salto 2017-2024 por commits individuales de cada Ley de Reforma Constitucional.

## Criterio editorial

- Mantener la Constitucion vigente y anotada en `constitucion.md`.
- Conservar notas editoriales del Congreso cuando aclaran reformas, vigencia o textos futuros.
- Usar fechas de publicacion/promulgacion de la norma reformadora.
- No mezclar cambios de formato con reformas de contenido si se quiere un `blame` util.
- Corregir extracciones PDF solo en commits separados y auditables.
