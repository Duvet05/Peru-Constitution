# Revision del snapshot 2024

Fuente: edicion oficial del Congreso de la Republica, diciembre de 2024.

Comandos ejecutados:

```sh
./scripts/validate_snapshot.py constitucion.md
./scripts/validate_snapshot.py constitucion.md --current
./scripts/audit_snapshot.py constitucion.md --current
```

Resultado:

- Articulos detectados: 213.
- Articulos base faltantes: ninguno.
- Articulos especiales faltantes: ninguno.
- Articulos especiales detectados: 7-A, 14-A, 34-A, 39-A, 90-A, 102-A y 102-B.
- Artefactos de pagina detectados: 0.
- Lineas con notas editoriales `(*)`: 121.
- Lineas con corte por guion: 0.

Decision editorial: conservar las notas editoriales del Congreso en el texto anotado. La canonicalizacion elimina saltos de linea del PDF y cortes por guion, pero no modifica contenido legal de fondo.
