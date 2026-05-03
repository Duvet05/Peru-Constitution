# Politica editorial

## Objetivo

Este repositorio representa la Constitucion Politica del Peru como texto versionado en Git.

La salida principal debe ser una Constitucion vigente y anotada, parecida a la edicion oficial del Congreso, pero con una historia reconstruida por reformas constitucionales para que `git blame` sea informativo.

## Texto principal

`constitucion.md` conserva:

- texto constitucional vigente;
- disposiciones finales y transitorias;
- disposiciones transitorias especiales;
- declaracion final;
- notas editoriales del Congreso que expliquen modificaciones, derogaciones, vigencia futura o sentencias relevantes.

## Historia

La reconstruccion historica debe cubrir todas las reformas constitucionales listadas por el Congreso, incluyendo reformas posteriores a la ultima edicion PDF disponible.

Cada reforma debe ser un commit separado con:

- fecha de publicacion de la ley;
- ley en el titulo del commit;
- articulos modificados en el cuerpo del commit;
- fuente usada para verificar el texto.

## Correcciones

Las correcciones de extraccion PDF, espacios, guiones de corte o puntuacion deben ir en commits separados. No deben mezclarse con commits de reforma constitucional.

Mientras el proyecto este en construccion, se permite reescribir historia para corregir commits historicos. Cuando haya una version publica estable, se debe preferir un commit correctivo nuevo salvo errores graves.
