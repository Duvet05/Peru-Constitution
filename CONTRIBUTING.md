# Contribuir

Este proyecto necesita precision historica. Antes de agregar una reforma:

1. Usa una fuente oficial o archivada.
2. Guarda el texto normalizado en `snapshots/YYYY-MM-DD.md`.
3. Agrega una fila en `reformas.csv`.
4. Reconstruye el historial con `scripts/build_history.py`.
5. Revisa el diff y el blame antes de publicar.

Los cambios de formato deben ir separados de los cambios de contenido para que `git blame` siga siendo util.

