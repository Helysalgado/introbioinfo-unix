# REPORTE DE ANALISIS DEL miRNAs

Autor: Karen Monserrat Ávila López.  
Fecha: 12/08/2022

## INTRODUCCIÓN

El presente reporte hace una análisis de los miRNAs del genoma humano. Las preguntas a contestar son las siguientes: 

¿Qué tipos de evidencia existen para los miRNAs? ¿Cuántos hay de cada tipo?

¿Cuál es el cromosoma con el mayor número de miRNAs y cuántos tiene?

¿Cuál es el miRNA más pequeño y el más grande en el genoma completo de tu organismo?

¿Cuál es el miRNA más pequeño y el más grande para el cromosoma con el mayor número de miRNAs?

¿Cuál es el número promedio de miRNAs por gene?


## METODOLOGÍA

### Requisitos

#### Requerimientos de software

Para el presente análisis se requiere:

1. Tener acceso a internet

2. Contar con el sistema operativo tipo unix o un emulador.


#### Organización del proyecto

Para crear el repositorio para el proyecto, ejecuta las sig. instrucciones en linea de comando de unix. Si cuentas con la carpeta de proyectos debes moverte dentro de ella.

```
cd proyectos
mkdir cromosoma11_miRNAs
de cromosoma11_miRNAs
mkdir  data bin results
```

#### Datos de entrada para el proyecto

Desde la página web de biomart, descargar los datos de miRNAs

Pasos a seguir.

1. Entra a la página de BioMart - ensembl https://www.ensembl.org/info/data/biomart/index.html
2. Ir a La opción de Genes
3. Descargar `mart_export.txt`


## ANÁLISIS y RESULTADOS

Se lista cada pregunta con los pasos que la resuelven y el comando que se debe ejecutar para obtener la respuesta. Además se listan los resultados obtenidos.

### ¿Qué tipos de evidencia existen para los miRNAs? ¿Cuántos hay de cada tipo?

Datos: 

- Archivo `mart_export.txt`

Análisis:

- Filtrar la columna 6 que contenía los tipos de evidencia, 
- limpiamos la fila que indica que son las evidencias, }
- posteriormente contamos la cantidad de datos que son por cada tipo.

```bash
awk -F "\t" '{print $6}' mart_export.txt | grep -v "Evidence" | uniq -c

```

Respuesta: 

Son 163,319 unicamente de tipo Experimental



### ¿Cuál es el cromosoma con el mayor número de miRNAs y cuántos tiene?

Datos: 

- Archivo `mart_export.txt`

Análisis:

- Separamos los resultados de la primera columna, 
- los ordenamos, contamos la cantidad que son por cada cromosoma, 
- ordenamos por valores numéricos y 
- vemos cual es que tiene la mayor cantidad.

```
awk -F "\t" '{print $1}' mart_export.txt | grep -v "Chromosome/scaffold name" | sort | uniq -c | sort -rn

```

Respuesta: 

El cromosoma 11 con un total de 14444 miRNAs


### Estructura final del proyecto

La estructura del proyecto final queda de la siguiente manera

```
+--- cromosoma11_miRNAs
|   +--- bin
|   +--- data
|   |   +--- mart_export.txt
|   +--- README.md
|   +--- results

```

## CONCLUSIONES

Hay un total de 163,319 miRNAs, y el cromosoma 11 cuenta con 14,444 de los cuales todos tienen evidencia experimental. Esto nos indica la calidad de los datos, ninguno es predicción sino que todos provienen de experimentos. 


## BIBLIOGRAFIA

Ensembl.org. 2022. \[online\] Available at: https://www.ensembl.org/biomart/martview/b9cafb3cb9414aacdbe3ab69c3ef6ef0 \[Accessed 10 October 2022\].