# Introducción a la bioinformática.

## EXAMEN 1


>  Nombre:   
>  Nombre de usuario (tepeu) :   


### Instrucciones

- Edita este archivo en StackEdit o algún editor Markdown.
- Lee con cuidado cada pregunta y contesta lo que se pide.
- El archivo final con las respuestas súbelo a la plataforma del curso en la tarea que dice "Examen 1".
- Puedes usar cualquier recurso disponible, como el asistente "Profe Unix" compartido en chatgpt, buscar en google, sacar tus notas. **Exámenes idénticos** en respuestas son **cancelados** sin opción de volverlo a presentar.
- Todas las respuestas (instrucciones) deberás ejecutarlas en tepeu, por lo que al final debe existir una carpetas y documentos del proceso que vayas haciendo.


**SELECCIONA UN GENOMA DE TU INTERES (No debe ser E. coli) para este exámen.**


## SECCION TEORICA [ 25% ]

1. ¿Cuál es la estructura recomendada para un proyecto, de acuerdo a las buenas prácticas ? [Clase 1]

2. Para que un experimento o un análisis computacional sea confiable, ¿qué tiene que cumplir?  [lectura del capítulo 1, clase 1]

3. ¿Qué es un patrón? puedes dar dos ejemplos. [Clase de Patrones con grep]

4. ¿Menciona 2 formatos usados para manejar las secuencias de DNA o proteínas y sus features o propiedades?

5. Menciona que es una base de datos y dá algunos ejemplos.

6. Explica la diferencia entre un alineamiento global y un alineamiento local. Da un ejemplo de cuándo usarías cada uno.

7. ¿Por qué son importantes las matrices de sustitución en los alineamientos de proteínas? 

8. Explica la diferencia entre homología, identidad y similitud en el análisis de secuencias.


## Buenas Prácticas

### Estructura del Repositorio. [ 5% ]
Crea una estructura de directorios para un proyecto de análisis de genomas con el nombre del organismo, que incluya carpetas para datos brutos, scripts, análisis, y resultados. Muestra los comandos usados para crear esta estructura.



### Nombre Adecuado de Archivos [ 5% ]
Descarga el archivo FASTA de NCBI del genoma seleccionado y nómbralo siguiendo un esquema de nombres adecuado (por ejemplo, GENUS_species_VERSION.fasta).
En esta pregunta, deberas indicar el algoritmo o los pasos a seguir para que cualquier usuario pueda ir y descargar los datos del genoma.

Algoritmo:

1. Abrir un navegador y buscar NCBI genomes.
2. 


Solución:

```bash
```


### Adición de Metadatos [ 5% ]
Añade un archivo metadata.md usando un editor (nano / vi) que proporcione información básica sobre los archivos del directorio de datos y sus fuentes. Muestra el contenido del archivo.

Ejemplo de archivo `metadata.md`. Este archivo tiene que estar en el directorio de datos descargados.

```
# Metadatos del Proyecto Genoma

Este directorio contiene los archivos descargados para el análisis del genoma de * <!-- nombre del genoma--> *.

## Archivos
<!-- Tabla de archivos y una breve descripción -->



## Fuente de Datos
- NCBI - National Center for Biotechnology Information

```

###  Verificación de Integridad de Datos [ 5% ]

Realiza la verificación de integridad DE UN SOLO archivo descargado usando checksum. 
nota: aunque debe hacerse para cualquier archivo que se descargue y se vaya a usar, por cuestiones de tiempo solo se pedirá las instrucciones para uno de ellos.

Algoritmo:

1. 
2. 


Solución:

```bash
```



### Protección de datos críticos [ 5% ]

Queremos proteger los datos que hemos descargado, para que no se puedan borrar o modificar. Entonces protege el DIRECTORIO donde estan los datos para que sólo sea de LECTURA y de ACCESO A ÉL. Los archivos dentro del directorio sólo deben tener permisos de lectura.


## Análisis de datos

Para esta parte, para la respuesta a cada pregunta, deberás indicar el algoritmo y posteriormente indicar los comandos que lo solucionan. 

**IMPORTANTE!!!**: 

> Todas las instrucciones se asumirán que estas en el directorio de trabajo del genoma. Deberas indicar los paths relativos.

1. **Total de features**. [ 10% ].  
Usando el archivo de features del genoma, queremos saber CUANTOS TIPOS de features tiene anotados el genoma de estudio.

Algoritmo:

1. 
2. 


Solución:

```bash
```



2. **Total por tipo de feature**. [ 10% ]  

Queremos saber el total por cada tipo de feature, es decir cuántos genes hay, cuántos CDS, etc... y queremos ordenarlos de mayor a menor. Manda el resultado a un archivo.

Un ejemplo de salida seria 

```
   4419 gene
   4379 CDS
    697 repeat_region
    180 exon
    166 pseudogene
     86 tRNA
     72 ncRNA
     49 mobile_genetic_element
     48 sequence_feature
     22 rRNA
      1 region
      1 recombination_feature
      1 origin_of_replication
```

Algoritmo:

1. 
2. 


Solución:

```bash
```


3. **Features ordenados**. [ 15% ]

Genera un nuevo archivo GFF llamado genoma_ordenado.txt , ordenado por tipo de feature y después por posición genómica de manera mumérica ( toma la posición izquierda/la menor). No olvides quitar los comentarios.

Algoritmo:

1. 
2. 


Solución:

```bash
```


4. **tRNAs** [ 15% ] 

Descarga el archivo `*rna_from_genomic.fna.gz` de tu genoma. Queremos saber si todos los tRNAs del archivo (gbkey=tRNA) `*rna_from_genomic.fna.gz`, se encuentran en el archivo GFF.  Mánda los resultados de los tRNAs a un archivo. Y responde si todos los tRNAs fueron encontrados.


Algoritmo:

1. 
2. 


Solución:

```bash
```


