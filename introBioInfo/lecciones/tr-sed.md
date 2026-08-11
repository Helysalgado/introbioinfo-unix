## tr

```
echo "este es un ejemplo"
echo "este es un ejemplo" | tr 'euo' 'EUO'
```

Si tengo un archivo

```
tr -f seq.txt 'at' 'ta'.   # error, porque no es standar input
cat seq.txt | tr 'at' 'ta'
```

Con expresiones regulares 

```
echo "este es un ejemplo" | tr 'euo' 'EUO' | tr -d '[s]'
echo "este es un ejemplo" | tr 'euo' 'EUO' | tr -d '[:lower:]'
echo "este es un ejeeeeemplo" | tr 'euo' 'EUO' | tr -d '[stj]'
```

pero los cuantificadores no los acepta

```
echo "este es un ejeeeeemplo" | tr 'euo' 'EUO' | tr -d 'E+'
```

reverse complement de una secuencia

```
echo "aggcacgcacatcatc"
echo "aggcacgcacatcatc" | tr 'actg' 'TGAC'
echo "aggcacgcacatcatc" | tr 'actg' 'TGAC' | rev
```

usar tr tantas veces como queramos

```
echo "agg---cacgcacatcatc" | tr 'actg' 'TGAC' | rev
echo "agg---cacgcacatcatc" | tr 'actg' 'TGAC' | rev | tr -d '-'
```


-------

## sed

```
man sed
```


sustituir primera ocurrencia, es el default

```
sed 's/linea/n/' test.txt

```

Todas las lineas

```
sed 's/linea/n/g' test.txt

```

Eligiendo el numero de linea

```
sed '2s/linea/n/g' test.txt
```

Eligiendo un rango de lineas

```
sed '2,4s/linea/n/g' test.txt
```


sed toma una instrucción y la aplica en cada línea del input, imprimiendo una línea de output por cada línea del input

Para inhabilitar este comportamiento default existe la opci ́on -n

Elegir un rango de lineas a imprimir
 
```
sed -n '2,4p' test.txt
```

Imprimir las lineas que contienen un patron

```
sed -n '/tercer/p' test.txt
```

Imprimir las lineas que NO contienen un patron

```
sed -n '/tercer/!p' test.txt
```


Utilizando subexpresiones y sustituciones

```
primer linea
linea-segunda prueba linea
linea-tercer linea
cuarta linea
```

hagamos el patrón de busqueda 

```
sed -n -E '/^([a-z]+) ([a-z]+) /p' test.tx
```

con sustitución y vamos invertir el match primero 2 y luego 1

```
sed -E 's/^([a-z]+) ([a-z]+) /\2-\1/' test.txt
```

