# Plan de reconstruccion historica

## Objetivo

Reconstruir la Constitucion Politica del Peru desde 1993 hasta la edicion oficial de diciembre de 2024, con commits por reforma constitucional.

## Fuentes base

- 1993: edicion oficial historica de la Biblioteca del Congreso. Pendiente de OCR/revision manual.
- 2013-05-01: Archivo Digital de la Legislacion del Peru, texto actualizado al 1 de mayo de 2013.
- 2024-12-11: edicion oficial del Congreso de la Republica, diciembre de 2024.
- Reformas: portal oficial de Leyes de Reforma Constitucional del Congreso, registrado en `metadata/reform-source-pages.csv`.

## Estrategia

1. Usar `snapshots/2013-05-01.md` como hito oficial intermedio.
2. Reconstruir hacia atras las reformas 1 a 11 hasta llegar al texto de 1993.
3. Reconstruir hacia adelante las reformas 12 a 36 hasta llegar al texto vigente.
4. Reescribir historia generada cuando haya correcciones de extraccion o de fuente.

## Estado

- Snapshot 2024: completo, canonico y auditado; no incluye la Ley 32265 de 2025.
- Snapshot 2013: completo, canonico y auditado.
- Inventario de 36 reformas: completo segun el portal oficial de Leyes de Reforma Constitucional del Congreso revisado en mayo de 2026.
