# Demo de blame

El historial reconstruido se puede generar con:

```sh
./scripts/build_history.py reformas.csv build/Peru-Constitution-history
```

En el estado actual, el historial generado tiene veintiseis hitos:

- 2013-05-01: texto actualizado del Archivo Digital de la Legislacion del Peru.
- 2015-03-10: Ley 30305, sobre denominacion y no reeleccion inmediata de autoridades regionales y alcaldes.
- 2017-05-09: Ley 30558, sobre detencion policial en el literal f del inciso 24 del articulo 2.
- 2017-06-22: Ley 30588, que incorpora el articulo 7-A sobre acceso al agua.
- 2017-08-20: Ley 30650, sobre prescripcion de delitos contra la Administracion Publica.
- 2017-08-20: Ley 30651, sobre legitimacion activa del Presidente del Poder Judicial en procesos de inconstitucionalidad.
- 2018-03-14: Ley 30738, sobre nacionalidad peruana por nacimiento.
- 2019-01-10: Ley 30904, sobre la Junta Nacional de Justicia.
- 2019-01-10: Ley 30905, sobre financiamiento de organizaciones politicas.
- 2019-01-10: Ley 30906, sobre prohibicion de reeleccion inmediata de parlamentarios.
- 2020-09-15: Ley 31042, sobre impedimentos para postular o ejercer funcion publica.
- 2020-12-29: Ley 31097, sobre inversion publica en educacion.
- 2021-02-06: Ley 31118, sobre eliminacion de la inmunidad parlamentaria.
- 2021-02-10: Ley 31122, sobre doble empleo publico remunerado de personal medico en emergencia sanitaria.
- 2021-07-16: Ley 31280, sobre residencia temporal del expresidente; declarada inconstitucional por la sentencia 918/2021 del Tribunal Constitucional.
- 2021-07-23: Ley 31304, sobre patrimonio cultural de la Nacion; declarada inconstitucional por la sentencia 918/2021 del Tribunal Constitucional.
- 2021-07-23: Ley 31305, sobre secreto bancario y reserva tributaria; declarada inconstitucional por la sentencia 918/2021 del Tribunal Constitucional.
- 2021-11-27: STC 918/2021, que deja sin efecto historico las Leyes 31280, 31304 y 31305.
- 2022-02-12: Ley 31414, sobre patrimonio cultural de la Nacion.
- 2022-07-03: Ley 31507, sobre secreto bancario y reserva tributaria.
- 2023-09-23: Ley 31878, sobre TIC e internet libre.
- 2024-03-20: Ley 31988, sobre bicameralidad con vigencia diferida.
- 2024-10-15: Ley 32135, sobre la cuarta disposicion transitoria especial.
- 2024-10-29: Ley 32145, sobre doble empleo publico remunerado en servicios de salud.
- 2024-12-11: Ley 32188, sobre discapacidad en los articulos 7 y 23.
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

Para ver una reforma que sustituye un articulo completo:

```sh
git blame -L 1905,1926 constitucion.md
```

Ese rango muestra el articulo 203 despues de la Ley 30651, con la nota posterior de la Ley 31988 todavia atribuida al hito 2024.

Para ver una modificacion de una sola linea:

```sh
git blame -L 389,397 constitucion.md
```

Ese rango muestra el primer parrafo del articulo 52 atribuido a la Ley 30738.

Para ver una reforma institucional grande:

```sh
git blame -L 1441,1502 constitucion.md
```

Ese rango muestra los articulos 154, 155 y 156 atribuidos a la Ley 30904; la nota posterior del articulo 157 sigue atribuida al hito 2024.

Para ver una reforma sobre financiamiento politico:

```sh
git blame -L 299,315 constitucion.md
```

Ese rango muestra los nuevos parrafos del articulo 35 atribuidos a la Ley 30905.

Para ver un articulo incorporado y luego anotado como derogado:

```sh
git blame -L 681,687 constitucion.md
```

Ese rango muestra el articulo 90-A atribuido a la Ley 30906 y la nota de derogacion atribuida al hito 2024.

Para ver impedimentos incorporados por sentencia condenatoria:

```sh
git blame -L 299,336 constitucion.md
```

Ese rango muestra los articulos 34-A y 39-A atribuidos a la Ley 31042.

Para ver una reforma presupuestal educativa:

```sh
git blame -L 179,189 constitucion.md
```

Ese rango muestra el ultimo parrafo del articulo 16 atribuido a la Ley 31097.

Para ver la eliminacion de la inmunidad parlamentaria:

```sh
git blame -L 733,752 constitucion.md
```

Ese rango muestra los parrafos nuevos del articulo 93 atribuidos a la Ley 31118 y la nota de bicameralidad atribuida al hito 2024.

Para ver una regla historica luego reemplazada:

```sh
git blame HEAD~1 -L '/Artículo 40/',+10 constitucion.md
```

Ese rango muestra el parrafo incorporado por la Ley 31122 antes de que el hito 2024 refleje reformas posteriores sobre el articulo 40.

Para ver una reforma historica luego expulsada del ordenamiento:

```sh
git blame HEAD~9 -L '/Artículo 21/',+8 constitucion.md
```

Ese rango muestra el articulo 21 atribuido a la Ley 31304 antes de su posterior declaracion de inconstitucionalidad.

Para ver el levantamiento del secreto bancario y reserva tributaria incorporado historicamente:

```sh
git blame HEAD~9 -L 31,49 constitucion.md
```

Ese rango muestra el inciso 5 del articulo 2 atribuido a la Ley 31305 antes de su posterior declaracion de inconstitucionalidad.

Para ver la reversion por sentencia constitucional:

```sh
git show --stat HEAD~8
```

Ese commit muestra la STC 918/2021 retirando del texto historico los cambios de las Leyes 31280, 31304 y 31305 antes del hito 2024.

Para ver la reforma posterior sobre patrimonio cultural:

```sh
git blame HEAD~7 -L '/Artículo 21/',+6 constitucion.md
```

Ese rango muestra el articulo 21 despues de la Ley 31414.

Para ver la reforma vigente sobre secreto bancario y reserva tributaria:

```sh
git blame HEAD~6 -L 31,49 constitucion.md
```

Ese rango muestra el inciso 5 del articulo 2 despues de la Ley 31507.

Para ver el nuevo derecho de acceso a internet libre:

```sh
git blame HEAD~5 -L '/Artículo 14-A/',+4 constitucion.md
```

Ese rango muestra el articulo 14-A incorporado por la Ley 31878.

Para ver la bicameralidad de vigencia diferida:

```sh
git blame HEAD~4 -L '/Artículo 102-A/',+34 constitucion.md
```

Ese rango muestra los articulos 102-A y 102-B incorporados como texto diferido por la Ley 31988.

Para ver la cuarta disposicion transitoria especial:

```sh
git blame HEAD~3 -L '/CUARTA\\./',+5 constitucion.md
```

Ese rango muestra la disposicion incorporada por la Ley 32135.

Para ver la regla vigente de doble empleo en salud:

```sh
git blame HEAD~2 -L '/Artículo 40/',+6 constitucion.md
```

Ese rango muestra el primer parrafo del articulo 40 modificado por la Ley 32145.

Para ver el cambio terminologico sobre discapacidad:

```sh
git blame HEAD~1 -L '/Artículo 7/',+4 constitucion.md
```

Ese rango muestra el articulo 7 modificado por la Ley 32188.
