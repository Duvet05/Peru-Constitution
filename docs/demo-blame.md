# Demo de blame

El historial reconstruido se puede generar con:

```sh
./scripts/build_history.py reformas.csv build/Peru-Constitution-history
```

En el estado actual, el historial generado tiene dos hitos:

- 2013-05-01: texto actualizado del Archivo Digital de la Legislacion del Peru.
- 2024-12-11: edicion oficial del Congreso de la Republica, diciembre de 2024.

Ejemplo:

```sh
cd build/Peru-Constitution-history
git blame -L 21,40 constitucion.md
```

Ese rango muestra lineas que permanecen desde el hito 2013 y lineas introducidas por reformas posteriores, como las notas de la Ley 31988. El objetivo final es reemplazar esos hitos grandes por commits individuales de cada Ley de Reforma Constitucional.

