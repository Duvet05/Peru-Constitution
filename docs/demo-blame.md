# Demo de blame

El historial reconstruido se puede generar con:

```sh
./scripts/build_history.py reformas.csv build/Peru-Constitution-history
```

En el estado actual, el historial generado tiene 40 hitos: texto original reconstruido de 1993, 36 leyes de reforma constitucional, la STC 918/2021, el checkpoint oficial del Archivo Digital actualizado al 1 de mayo de 2013 y la edicion oficial del Congreso de diciembre de 2024.

Ejemplos estables:

```sh
cd build/Peru-Constitution-history
git log --oneline --reverse
git blame constitucion.md
```

Para ver una reforma temprana sobre garantias constitucionales:

```sh
git blame -L '/Artículo 200/',+18 constitucion.md
```

Ese rango muestra los incisos de amparo y habeas data modificados por la Ley 26470.

Para ver la reforma de descentralizacion:

```sh
git blame -L '/Artículo 188/',+80 constitucion.md
```

Ese rango muestra el Capitulo XIV reconstruido desde la Ley 27680, con cambios posteriores sobre gobiernos regionales y locales.

Para ver un articulo incorporado por reforma posterior:

```sh
git blame -L '/Artículo 7-A/',+4 constitucion.md
```

Ese rango muestra el articulo 7-A atribuido a la Ley 30588.

Para ver una reforma historica expulsada por sentencia constitucional:

```sh
git log --oneline --grep 'STC 918/2021'
git show --stat <commit>
```

Ese commit retira del texto historico los cambios de las Leyes 31280, 31304 y 31305.

Para ver bicameralidad de vigencia diferida:

```sh
git blame -L '/Artículo 102-A/',+34 constitucion.md
```

Ese rango muestra los articulos 102-A y 102-B incorporados como texto diferido por la Ley 31988.

Para ver la restitucion de firma de 2025:

```sh
git blame -L 1,4 constitucion.md
```

Ese rango muestra la firma restituida por la Ley 32265.
