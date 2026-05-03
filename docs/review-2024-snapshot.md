# Revision del snapshot 2024

Fuente: edicion oficial del Congreso de la Republica, diciembre de 2024.

Comandos ejecutados:

```sh
./scripts/validate_snapshot.py constitucion.md
./scripts/audit_snapshot.py constitucion.md
```

Resultado:

- Articulos detectados: 213.
- Articulos base faltantes: ninguno.
- Articulos especiales faltantes: ninguno.
- Articulos especiales detectados: 7-A, 14-A, 34-A, 39-A, 90-A, 102-A y 102-B.
- Artefactos de pagina detectados: 0.
- Lineas con notas editoriales `(*)`: 122.
- Lineas con corte por guion: 6.

Lineas con corte por guion pendientes de revision manual:

- 102
- 1614
- 3329
- 3331
- 3553
- 4259

Decision editorial: no corregir automaticamente cortes por guion ni notas editoriales en el texto legal. Esos cambios deben hacerse en commits separados, con verificacion contra fuente oficial, para que `git blame` no oculte diferencias de contenido.

