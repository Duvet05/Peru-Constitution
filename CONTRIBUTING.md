# Contribuir

Este proyecto necesita precision historica. Antes de agregar una reforma:

1. Usa una fuente oficial o archivada.
2. Guarda el texto normalizado en `snapshots/YYYY-MM-DD.md`.
3. Agrega una fila en `reformas.csv`.
4. Reconstruye el historial con `scripts/build_history.py`.
5. Revisa el diff y el blame antes de publicar.

Los cambios de formato deben ir separados de los cambios de contenido para que `git blame` siga siendo util.

Para extracciones desde PDF, revisa por lo menos:

- que esten los articulos 1 al 206;
- que aparezcan articulos incorporados como 7-A, 14-A, 34-A, 39-A, 90-A, 102-A y 102-B;
- que las disposiciones finales, transitorias, transitorias especiales y la declaracion final no se hayan cortado;
- que no queden cabeceras, pies de pagina o numeros de pagina mezclados con el texto.
