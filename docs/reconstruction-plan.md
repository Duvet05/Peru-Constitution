# Plan de reconstruccion historica

## Objetivo

Reconstruir la Constitucion Politica del Peru desde 1993 hasta la edicion oficial de diciembre de 2024, con commits por reforma constitucional.

## Fuentes base

- 1993: texto original reconstruido desde el checkpoint oficial 2013, leyes oficiales pre-2013 y fuentes anotadas de contraste.
- Contraste 1993-2011: copias anotadas de referencia usadas solo para verificar texto cuando los PDF oficiales escaneados no producen OCR confiable: OAS/TC y Justia Peru.
- 2013-05-01: Archivo Digital de la Legislacion del Peru, texto actualizado al 1 de mayo de 2013.
- 2024-12-11: edicion oficial del Congreso de la Republica, diciembre de 2024.
- Reformas: portal oficial de Leyes de Reforma Constitucional del Congreso, registrado en `metadata/reform-source-pages.csv`.

## Estrategia

1. Usar `snapshots/1993-12-30.md` como texto original reconstruido.
2. Reconstruir las reformas 1 a 11 hasta llegar al hito oficial `snapshots/2013-05-01.md`.
3. Usar `snapshots/2013-05-01.md` como checkpoint oficial intermedio.
4. Reconstruir hacia adelante las reformas 12 a 36 hasta llegar al texto vigente.
5. Reescribir historia generada cuando haya correcciones de extraccion o de fuente.

## Estado

- Snapshot 1993-12-30: texto original reconstruido y validado como base historica.
- Snapshots 1995-2009: Leyes 26470, 26472, 27365, 27680, 28389, 28390, 28480, 28484, 28607, 29401 y 29402 reconstruidas y validadas.
- Snapshot 2013: completo, canonico y auditado; coincide con el resultado reconstruido tras Ley 29402.
- Snapshot 2024: completo, canonico y auditado; no incluye la Ley 32265 de 2025.
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
- Snapshot 2021-07-16: Ley 31280 reconstruida y auditada.
- Snapshot 2021-07-23-31304: Ley 31304 reconstruida y auditada.
- Snapshot 2021-07-23-31305: Ley 31305 reconstruida y auditada.
- Snapshot 2021-11-27-stc-918-2021: sentencia 918/2021 del Tribunal Constitucional reconstruida y auditada como reversion historica de las Leyes 31280, 31304 y 31305.
- Snapshot 2022-02-12: Ley 31414 reconstruida y auditada.
- Snapshot 2022-07-03: Ley 31507 reconstruida y auditada.
- Snapshot 2023-09-23: Ley 31878 reconstruida y auditada.
- Snapshot 2024-03-20: Ley 31988 reconstruida como reforma de vigencia diferida; revisada para separar normalizaciones editoriales evidentes del cambio sustantivo.
- Snapshot 2024-10-15: Ley 32135 reconstruida; la discrepancia con la edicion oficial de diciembre de 2024 sobre la tercera disposicion transitoria especial queda documentada en `reformas/32135/README.md`.
- Snapshot 2024-10-29: Ley 32145 reconstruida y auditada.
- Snapshot 2024-12-11-32188: Ley 32188 reconstruida y auditada.
- Snapshot 2024-12-11-32189: Ley 32189 reconstruida y auditada.
- Snapshot 2025-03-22: Ley 32265 reconstruida como restitucion de firma en el texto constitucional.
- Inventario de 36 reformas: completo segun el portal oficial de Leyes de Reforma Constitucional del Congreso revisado en mayo de 2026.
