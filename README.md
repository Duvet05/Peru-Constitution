# Constitucion Politica del Peru en Git

Este repo busca representar la Constitucion Politica del Peru como texto versionado, con commits fechados por promulgacion y reforma constitucional para que `git blame` muestre que ley introdujo o modifico cada linea.

## Estado

Proyecto inicial. Incluye:

- fuentes oficiales conocidas;
- scripts para descargar y normalizar texto;
- un manifest editable de reformas constitucionales;
- una herramienta para reconstruir un repo historico desde snapshots.

La fuente oficial vigente usada como referencia inicial es la edicion del Congreso de la Republica de diciembre de 2024. El repo todavia no incluye un texto constitucional validado; primero se debe extraer y revisar el texto para no publicar OCR o HTML defectuoso como si fuera fuente legal.

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

1. Coloca en `snapshots/` un archivo por cada reforma constitucional relevante.
2. Registra cada snapshot en `reformas.csv` con fecha, norma, fuente y descripcion.
3. Ejecuta `scripts/build_history.py` para crear un repo historico limpio.
4. Revisa `git diff` entre commits para detectar errores de OCR, saltos de linea o notas editoriales.

## Blame

Cuando el historial este construido, `git blame` permite ver que reforma introdujo cada linea:

```sh
git blame constitucion.md
git blame -w constitucion.md
```

La opcion `-w` ignora cambios de espacios y ayuda cuando hubo normalizacion de formato.

## Criterio editorial

- Mantener solo texto constitucional en `constitucion.md`.
- Mover notas editoriales, llamadas y fuentes a `metadata/` o al commit message.
- Usar fechas de publicacion/promulgacion de la norma reformadora.
- No mezclar cambios de formato con reformas de contenido si se quiere un `blame` util.
