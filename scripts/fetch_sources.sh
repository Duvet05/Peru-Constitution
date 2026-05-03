#!/usr/bin/env sh
set -eu

mkdir -p sources snapshots build

curl -L \
  "https://www3.congreso.gob.pe/Docs/files/constitucion/constitucion-12-2024.pdf" \
  -o sources/constitucion-12-2024.pdf

curl -L \
  "https://leyes.congreso.gob.pe/Documentos/constituciones_ordenado/CONSTIT_1993/Texto_actualizado_CONS_1993.pdf" \
  -o sources/constitucion-2013-05-01.pdf

curl -L \
  "https://www.congreso.gob.pe/datos-generales/constitucion-del-peru-y-reglamento/" \
  -o sources/congreso-constitucion-y-reglamento.html

printf '%s\n' "Fuentes descargadas en sources/"
