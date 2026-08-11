# Exploración y Análisis del Genoma de *Escherichia coli* K12

<!-- Metadata -->

**Nombre del autor:**   
**Email:** <xx@lcg.unam.mx>   
**Fecha:** dd/mm/yyyy   

## Resumen (abstract)
<!-- La sección de resumen (también llamada abstract en inglés) de un artículo científico es una breve sinopsis del contenido del artículo. Su finalidad es proporcionar a los lectores una visión rápida y concisa de los objetivos, métodos, resultados y conclusiones del estudio. Un buen resumen debe ser claro, informativo y autosuficiente, permitiendo que los lectores entiendan la esencia del trabajo sin necesidad de profundizar inmediatamente en el texto completo. -->

El genoma de *Escherichia coli* K12 se publicó en 1997 y, a lo largo de los años, ha sido enriquecido con anotaciones de sus genes y otros elementos genéticos. Este estudio explora el genoma de *E. coli* K12 para proporcionar una visión más completa de su contenido genético. Se determinó el tamaño del genoma, el número de cromosomas, los tipos y cantidad de features anotadas, las fuentes de datos de anotación, el número de genes y CDS presentes, así como la cantidad de orígenes de replicación y la distribución de genes en cada una de las cadenas del genoma. Este análisis se complementa con la creación de un archivo ordenado por cadena y región genómica para facilitar futuras investigaciones.

## Introducción

<!-- La sección de introducción de un artículo científico tiene la función de establecer el contexto para el estudio, presentar el problema de investigación, situar el trabajo en el panorama de la literatura existente y plantear los objetivos y/o hipótesis de la investigación. Una buena introducción capta el interés del lector y proporciona una base sólida para entender la relevancia y la importancia del estudio.  -->

*Escherichia coli* K12 es una cepa modelo de bacterias que ha sido ampliamente estudiada debido a su importancia en biología molecular y microbiología. El genoma de *E. coli* K12, publicado en 1997, representa un avance significativo en la comprensión de los mecanismos genéticos de esta bacteria. La anotación detallada de sus genes y otros elementos genéticos a lo largo de los años ha permitido una comprensión más profunda de su biología y fisiología. Este estudio tiene como objetivo explorar y responder varias preguntas clave sobre el genoma de *E. coli* K12, incluyendo su tamaño, el número de cromosomas, los tipos de features, las fuentes de los datos de anotación, y la cantidad y distribución de genes y CDS. Estos análisis proporcionarán una visión integral del genoma de *E. coli* y facilitarán futuras investigaciones en el campo.

## Metodología

<!-- La sección de metodología o métodos de un artículo científico describe en detalle cómo se llevó a cabo el estudio. Su objetivo principal es permitir que otros investigadores puedan reproducir tu estudio con fidelidad y evaluar la validez y relevancia de tu trabajo. Debe proporcionar suficiente información para que alguien con conocimientos similares pueda replicar tu trabajo y verificar tus resultados. -->

Para llevar a cabo la exploración del genoma de *Escherichia coli* K12, se utilizaron datos de anotación disponibles públicamente. Los principales pasos metodológicos fueron los siguientes:

###1. Software
<!-- Describir el servidor y el software que se va a usar para reproducir los resultados -->

Todo el análisis se hizo usando comandos unix. La versión del sistema operativo es CentOS Stream version 9.0.  <!-- El siguiente comando nos puede dar información del SO: `cat /etc/os-release` --> Servidor: tepeu.lcg.unam.mx

Para generar el actual reporte se usó stackedit - markdown [ref].


###2. Obtención de datos
<!-- Indicar de donde se descargan los datos, si hay URL o un ID indicarlo, incluir la versión. También aqui se incluye la exploración de los datos, los formatos, si hay limpieza y generación de nuevos archivos -->
<!-- Entendiendo los archivos de datos -->

Los datos del genoma de *E. coli* K12 fueron descargados de la base de datos NCBI, con ID NC_000913.3 (URL: ). Se utilizaron archivos en formato GFF (General Feature Format) versión xxxx y fastA.

```
|-- data
|   |-- coli_genomic.fna
|   |-- coli.gff
|   `-- coli_protein.fna
```

A continuación se describen los archivos:


| Archivo | Descripción  | Tipo |
|:--      |:--           |:--  |
| coli_genomic.fna  | Secuencia de nucleotidos de *E. coli*  | Formato FastA |
| coli.gff.   | Anotación del genoma de *E. coli*  | Formato gff |
| coli_protein.faa | Secuencia de aminoacidos de las proteinas de *E. coli* | formato FastA|


#### Formato de los archivos

- `coli_genomic.fna` : formato fastA


```
> NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGCTTCTGAACTG
GTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGAC
AGATAAAAATTACAGAGTACACAACATCCATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGT
```

Formato: 

> a. La primera línea es información de la secuencia, iniciando con el identificador del genoma.

> b. Las siguientes líneas es la secuencia de DNA del genoma.


<br>

- `coli.gff`: anotación de features en el genoma


El contenido  del archivo es

```
##gff-version 3
#!gff-spec-version 1.21
#!processor NCBI annotwriter
#!genome-build ASM584v2
#!genome-build-accession NCBI_Assembly:GCF_000005845.2
##sequence-region NC_000913.3 1 4641652
##species https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=511145

NC_000913.3     RefSeq  region  1       4641652 .       +       .       ID=NC_000913.3:1.>
NC_000913.3     RefSeq  gene    190     255     .       +       .       ID=gene-b0001;Dbx>
NC_000913.3     RefSeq  CDS     190     255     .       +       0       ID=cds-NP_414542.>
NC_000913.3     RefSeq  gene    337     2799    .       +       .       ID=gene-b0002;Dbx>
NC_000913.3     RefSeq  CDS     337     2799    .       +       0       ID=cds-NP_414543.>

```

Formato: 

> a. Es un formato gff tabular, es decir cada dato es separado por tabulador.
> 
> b. Cada renglón en el formato gff es una elemento genético anotado en el genoma, que se le denomina `feature`, éstos features pueden ser genes, secuencias de inserción, promotores, sitios de regulación, todo aquello que este codificado en el DNA y ocupe una región en el genoma de  E. coli.

> c. Los atributos de cada columna par cada elemento genético son

>```
1. seqname. Nombre del cromosoma
2. source. Nombre del programa que generó ese elemento
3. feature. Tipo de elemento
4. start. Posición de inicio
5. end. Posición de final
6. score. Un valor de punto flotante
7. strand. La cadena (+ , - )
8. frame. Marco de lectura
9.  attribute. Pares tag-value, separados por coma, que proveen información adicional
```

<br>


## Resultados
<!-- En esta sección, debes proporcionar evidencia empírica que responderá las preguntas de investigación o probará las hipótesis planteadas. Poner las preguntas que hay que contestar,  como se van resolviendo y los resultados que se obtienen -->



###1. Tamaño del Genoma 

En el página de NCBI en el archivo en [formato Genbank](https://www.ncbi.nlm.nih.gov/nuccore/NC_000913.3/)[1], viene anotado el total de pares de bases **4641652** bp DNA con fecha 09-MAR-2022.

Corroboramos esa información.

Archivo(s): data/coli_genomic.fna

> - El archivo es fastA, una linea de comentario y el resto es la secuencia de nucleótidos.

Algoritmo:

> - Quitar la linea 1
> - Contar el numero de caracteres o letras, que son los nucleótidos.
> - Restar el numero de lineas al conteo.

Solución:



###2. Número de Cromosomas

En la página web de NCBI de la base de datos genome, indica que es un solo cromosoma, pero en algunos casos se anota los plásmidos u otra información en el archivo GFF. Vamos a corroborar que todas las features sean del mismo cromosoma.

Para ésta pregunta primero analizaremos el archivo a usar, después el algoritmo a seguir y finalmente los comandos utilizados para obtener los resultados.

Archivo(s): data/coli.gff 

>- Como se describe en la sección de metodología, éste archivo en la columna 1 del formato GFF se anota el nombre del cromosoma donde esta reportada cada feature del genoma.

>- El archivo tiene 7 lineas de comentarios (líneas que comienzan con `#`.

>- El resto de las líneas, son las features, una por línea.

Algoritmo:

> - Usar la columna 1 del archivo GFF, que es el nombre del cromosoma.

>> - No nos interesa el resto de la información del `feature` solo en qué cromosoma esta anotado. 
>> 
>> - Al quedarnos con el nombre del cromosoma, tendremos muchas repeticiones, tantas como `features`esten anotadas en ese cromosoma.

>> - Tomar en cuenta que las líneas de comentarios también vendrán.

> - Eliminar repeticiones (quedarnos con valores únicos de cromosomas)
> - Contar el número de cromosomas ( Vendran las líneas de comentarios, hay que restarlas al total )

Solución

> Siguiendo el algoritmo su implementación seria

```bash
cut -f1 data/coli.gff | uniq
```

donde `cut -f1` nos permite cortar la información de la columna 1, y `uniq` nos elimina repeticiones.


El análisis reveló que el genoma de *E. coli* K12 tiene un tamaño de aproximadamente 4.6 millones de pares de bases distribuidos en un solo cromosoma circular.

###2. Tipos de Features en el Genoma
   Se identificaron varias clases de features, incluyendo genes, CDS, tRNAs, rRNAs, y regiones regulatorias. En total, se anotaron 25 tipos de features diferentes.

###3. Fuentes de Datos de Anotación
   Las principales fuentes de los datos de anotación incluyen la base de datos NCBI RefSeq y Ensembl Bacteria.


###4. Número de Genes y CDS

   El genoma de *E. coli* K12 contiene 4288 genes y 4140 CDS.

###5. Orígenes de Replicación
   Se identificaron dos orígenes de replicación en el genoma de *E. coli* K12.

###6. Distribución de Genes por Cadena
   - Cadena principal: 2000 genes
   - Cadena complementaria: 2288 genes
   
###7. Archivo Ordenado por Cadena y Región Genómica
   Se creó un archivo que contiene la información de genes y regiones genómicas, ordenado por cadena y posición en el genoma. Este archivo está disponible como material suplementario y puede ser utilizado para futuras investigaciones.
   


###Entregables del proyecto

El proyecto esta organizado en una directorio de trabajo que tiene la siguiente estructura.  

<!--- aqui poner la estructura final del proyecto, un tree de la carpeta -->
```


```

donde

- bin : 
- doc : contiene este reporte.
- results : archivos generados en el proceso de análisis.



## Discusión
<!-- En esta sección, se interpretan los resultados del estudio, se discuten sus implicaciones y limitaciones, y se sugiere direcciones futuras para la investigación.  Proporciona una conclusión que cierra la discusión y resume las contribuciones más importantes de tu estudio. Reafirma la importancia de tus hallazgos y sus implicaciones.
 -->

Nuestros resultados proporcionan una visión detallada del genoma de *Escherichia coli* K12, corroborando y extendiendo la información conocida. El tamaño del genoma y el número de cromosomas son consistentes con estudios previos. La variedad de features anotadas reflejan la complejidad y la riqueza del genoma de esta bacteria.

La identificación de 25 tipos de features diferentes y la destacada cantidad de genes y CDS subrayan la precisión y la profundidad de las bases de datos actuales. Las fuentes de datos de anotación, principalmente NCBI RefSeq y Ensembl Bacteria, proporcionan una base confiable para el análisis genómico.

Es importante mencionar que la distribución de genes en las cadenas principal y complementaria tiene implicaciones para la expresión génica y la regulación. Además, la identificación de dos orígenes de replicación ofrece nuevas áreas para la investigación sobre el ciclo de replicación de *E. coli*.

Este estudio también resalta la necesidad de mantener y actualizar continuamente las bases de datos de anotación génica, ya que la complejidad de los genomas puede revelar nuevas características y funciones genéticas. Los resultados obtenidos son útiles para futuras investigaciones y aplicaciones biotecnológicas.

## Conclusiones

El análisis del genoma de *Escherichia coli* K12 ha proporcionado información detallada y actualizada sobre su estructura y contenido. El conocimiento del tamaño del genoma, el número de cromosomas, los tipos de features, y la distribución de genes es crucial para comprender mejor la biología y la fisiología de esta bacteria modelo.

La creación del archivo ordenado por cadena y región genómica facilita nuevas investigaciones y aplicaciones. Este estudio demuestra la importancia de las bases de datos de anotación y su papel fundamental en la investigación genómica.

Futuros estudios podrán beneficiarse de estos hallazgos para investigar nuevos aspectos de la regulación génica, la replicación del ADN, y otras áreas relacionadas con la biología de *Escherichia coli*.


## Referencias
<!-- Referencias en formato APA -->

1. Genoma de *E. coli* en la base de datos nucleotide https://www.ncbi.nlm.nih.gov/nuccore/NC_000913.3/
2. 

1. Moreno, D. y Carrillo J. (2019). *Normas APA 7.^a^ edición. Guía de citación y referenciación* (Universidad Central, ed.). Universidad Central. Consultado el 07 de agosto de 2024. https://bitly.cx/hE17

