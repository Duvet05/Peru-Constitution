# Demo de blame

El historial reconstruido se puede generar con:

```sh
./scripts/build_history.py reformas.csv build/Peru-Constitution-history
```

En el estado actual, el historial generado tiene seis hitos:

- 2013-05-01: texto actualizado del Archivo Digital de la Legislacion del Peru.
- 2015-03-10: Ley 30305, sobre denominacion y no reeleccion inmediata de autoridades regionales y alcaldes.
- 2017-05-09: Ley 30558, sobre detencion policial en el literal f del inciso 24 del articulo 2.
- 2017-06-22: Ley 30588, que incorpora el articulo 7-A sobre acceso al agua.
- 2017-08-20: Ley 30650, sobre prescripcion de delitos contra la Administracion Publica.
- 2024-12-11: edicion oficial del Congreso de la Republica, diciembre de 2024.

Ejemplo:

```sh
cd build/Peru-Constitution-history
git blame -L 1723,1733 constitucion.md
```

Ese rango muestra lineas que permanecen desde el hito 2013, lineas introducidas por la Ley 30305 y notas editoriales posteriores de la Ley 31988. El objetivo final es reemplazar los saltos grandes restantes por commits individuales de cada Ley de Reforma Constitucional.

Otro ejemplo:

```sh
git blame -L 109,116 constitucion.md
```

Ese rango muestra el literal f del inciso 24 del articulo 2 atribuido a la Ley 30558.

Para ver un articulo completo nacido por reforma:

```sh
git blame -L 140,146 constitucion.md
```

Ese rango muestra el articulo 7-A atribuido a la Ley 30588.

Para ver una modificacion puntual dentro de un articulo:

```sh
git blame -L 339,348 constitucion.md
```

Ese rango muestra el cuarto parrafo del articulo 41 atribuido a la Ley 30650.
