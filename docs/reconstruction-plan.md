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
- Snapshot 2015-03-10: Ley 30305 reconstruida y auditada como primer paso individual posterior a 2013.
- Snapshot 2017-05-09: Ley 30558 reconstruida y auditada.
- Snapshot 2017-06-22: Ley 30588 reconstruida y auditada.
- Snapshot 2017-08-20-30650: Ley 30650 reconstruida y auditada.
- Snapshot 2017-08-20-30651: Ley 30651 reconstruida y auditada.
- Snapshot 2018-03-14: Ley 30738 reconstruida y auditada.
- Snapshot 2019-01-10-30904: Ley 30904 reconstruida y auditada.
- Snapshot 2019-01-10-30905: Ley 30905 reconstruida y auditada.
- Snapshot 2019-01-10-30906: Ley 30906 reconstruida y auditada.
- Snapshot 2020-09-15: Ley 31042 reconstruida y auditada.
- Snapshot 2020-12-29: Ley 31097 reconstruida y auditada.
- Snapshot 2021-02-06: Ley 31118 reconstruida y auditada.
- Snapshot 2021-02-10: Ley 31122 reconstruida y auditada.
- Snapshot 2021-07-16: Ley 31280 reconstruida y auditada; pendiente registrar la sentencia 918/2021 del Tribunal Constitucional como reversion historica junto con Ley 31304 y Ley 31305.
- Inventario de 36 reformas: completo segun el portal oficial de Leyes de Reforma Constitucional del Congreso revisado en mayo de 2026.
