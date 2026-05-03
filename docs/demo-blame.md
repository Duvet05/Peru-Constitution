# Demo de blame

El historial reconstruido se puede generar con:

```sh
./scripts/build_history.py reformas.csv build/Peru-Constitution-history
```

En el estado actual, el historial generado tiene tres hitos:

- 2013-05-01: texto actualizado del Archivo Digital de la Legislacion del Peru.
- 2015-03-10: Ley 30305, sobre denominacion y no reeleccion inmediata de autoridades regionales y alcaldes.
- 2024-12-11: edicion oficial del Congreso de la Republica, diciembre de 2024.

Ejemplo:

```sh
cd build/Peru-Constitution-history
git blame -L 1723,1733 constitucion.md
```

Ese rango muestra lineas que permanecen desde el hito 2013, lineas introducidas por la Ley 30305 y notas editoriales posteriores de la Ley 31988. El objetivo final es reemplazar los saltos grandes restantes por commits individuales de cada Ley de Reforma Constitucional.
