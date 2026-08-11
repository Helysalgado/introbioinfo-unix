# EXAMEN

Edita este archivo en StackEdit. Lee con cuidado cada pregunta. El archivo final con las respuestas súbelo a la plataforma en la tarea que dice Examen 1.


## Buenas Prácticas

### Estructura del Repositorio. [ 5% ]
Crea una estructura de directorios para un proyecto de análisis de genomas que incluya carpetas para datos brutos, scripts, análisis, y resultados. Muestra los comandos usados para crear esta estructura.

**Algoritmo**
1. Crear la carpeta del proyecto
2. Crear las carpetas de un proyecto siguiendo las buenas practicas
3. Verificar la estructura

**Solución**

```bash
mkdir Buchnera_aphidicola
cd Buchnera_aphidicola
mkdir data bin doc results
cd..
tree
```

**Resultados**

```
.
└── Buchnera_aphidicola
    ├── bin
    ├── data
    ├── doc
    └── results
```

### Nombre Adecuado de Archivos [ 5% ]
Descarga el archivo FASTA de NCBI del genoma asignado y nómbralo siguiendo un esquema de nombres adecuado (por ejemplo, GENUS_species_VERSION.fasta).
En esta pregunta, deberas indicar el algoritmo o los pasos a seguir para que cualquier usuario pueda ir y descargar los datos del genoma.

Algoritmo:

1. Abrir un navegador y buscar `NCBI genomes`.
2. En la caja de busqueda dar el nombre del organismo `Buchnera aphidicola` y asegurarse que en la opción de base de datos este seleccionada `genomes`
3. En la página de resultados, ir a la liga del genoma de referencia, (generalmente es el que tiene la palomita verde)
4. En el menu superior de la página del genoma, ir a la liga `FTP`.
5. Seleccionar el archivo *.gff.gz, *.fna.gz y *rna.gz, uno por uno. Dar botón derecho y copiar el link.
6. En el servidor, moverse a la carpeta `data`
7. Con `wget` descargar cada uno de los archivos
8. Descomprimir el archivo y renombrarlo.

Solución:

```bash
cd data
wget -O Buchnera_aphidicola.gff.gz https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/007/365/GCF_000007365.1_ASM736v1/GCF_000007365.1_ASM736v1_genomic.gff.gz
wget -O Buchnera_aphidicola_rna_from_genomic.fna.gz https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/007/365/GCF_000007365.1_ASM736v1/GCF_000007365.1_ASM736v1_rna_from_genomic.fna.gz
wget -O Buchnera_aphidicola_genomic.fna.gz https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/007/365/GCF_000007365.1_ASM736v1/GCF_000007365.1_ASM736v1_genomic.fna.gz

gunzip *
```

**Resultados**

```
data/
├── Buchnera_aphidicola_genomic.fna
├── Buchnera_aphidicola.gff
└── Buchnera_aphidicola_rna_from_genomic.fna
```

###  Verificación de Integridad de Datos [ 3% ]
Realiza la verificación de integridad de un archivo descargado usando checksum. 

**Algoritmo**

1. Visualizar o descargar el archivo `uncompressed_checksums.txt` de Buchnera aphidicola por FTP
2. Genera la suma de los archivos descargados y descomprimidos para verificar la integridad
3. Compara los resultados con el `uncompressed_checksums.txt`

**Solución**

```
#file	md5sum	crc32	size
./GCF_000007365.1_ASM736v1_genomic.fna	a955f51c63f6abf0f60d3820a760d05f	8bf1dc10	649555
./GCF_000007365.1_ASM736v1_genomic.gbff	934b2bf8fbe700b074cb256f6fc7e69b	12cbe20c	1851632
./GCF_000007365.1_ASM736v1_genomic.gff	e67d2b4157b007903a4141997c0344ed	c65f2396	456397
./GCF_000007365.1_ASM736v1_protein.faa	b2dcffb0db36bd1800a05a52635d28cd	9a97c63b	225582
./GCF_000007365.1_ASM736v1_cds_from_genomic.fna	2c90399ea1acb3ac91b150915ea84b7c	a85d3d2e	705586
./GCF_000007365.1_ASM736v1_rna_from_genomic.fna	91e74c14336e70c549536eed4839cf18	03eb94fd	14048
./GCF_000007365.1_ASM736v1_translated_cds.faa	8b21b26e787e3fbab6dfa23e712d640e	13323603	320477
./GCF_000007365.1_ASM736v1_genomic.gtf	45db00da93ba5471b48e0d8c94f19d3d	2dcab328	1277759
```


**Solución**

```bash
md5sum *.fna *.gff
md5sum *
```
**Resultados**

```
e67d2b4157b007903a4141997c0344ed  Buchnera_aphidicola.gff
e67d2b4157b007903a4141997c0344ed
a955f51c63f6abf0f60d3820a760d05f  Buchnera_aphidicola_genomic.fna
a955f51c63f6abf0f60d3820a760d05f
91e74c14336e70c549536eed4839cf18  Buchnera_aphidicola_rna_from_genomic.fna
91e74c14336e70c549536eed4839cf18
```

### Adición de Metadatos [ 5% ]
Añade un archivo README.md usando un editor (nano, vi) que proporcione información básica sobre los archivos del directorio de datos y sus fuentes. Muestra el contenido del archivo.

Ejemplo:

```
# Metadatos del Proyecto Genoma

Este directorio contiene los archivos descargados para el análisis del genoma de * <!-- nombre del genoma--> *.

## Archivos
<!-- Tabla de archivos y una breve descripción -->

## Fuente de Datos
- NCBI - National Center for Biotechnology Information

```

|Nombre  | Descripción |
|:--|:--|
|   |. |



### Protección de datos críticos [ 2% ]
Queremos proteger los datos que hemos descargado, para que no se puedan borrar o modificar. Entonces protege este directorio para que sólo sea de lectura y de acceso. Los archivos sólo deben ser de lectura.

**Solución**

```
chmod u-wx *
cd ..
chmod u-w data
```


## Análisis de datos

Para esta parte, para la respuesta a cada pregunta, deberás indicar el algoritmo y posteriormente indicar los comandos que lo solucionan. 

**IMPORTANTE!!!: Todas las soluciones deberan ser contestadas partiendo que estas colocado en la carpeta de RESULTADOS.**

1. **Total de features**. [ 10% ].  
Usando el archivo de features del genoma, queremos saber cuántos tipos de features tiene anotados el genoma de estudio.

Algoritmo:

1. Limpiar el archivo *.gff, quitando las líneas de comentarios.
2. Cortar la columna 3, que indica el tipo de feature.
3. Ordenar los datos para poder quitar repeticiones de features.
4. Quitar repeticiones de features.
5. Contar las líneas que nos indica el tipo de features diferentes.

Solución:

```bash
grep -v "#" ../data/Buchnera_aphidicola.gff | cut -f3 | sort -u | wc -l
```

**Resultados**

```
CDS
exon
gene
pseudogene
region
RNase_P_RNA
rRNA
SRP_RNA
tmRNA
tRNA
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

1. Limpiar el archivo *.gff, quitando las líneas de comentarios.
2. Cortar la columna 3, que indica el tipo de feature.
3. Ordenar los datos 
4. Contar repeticiones de features.
5. Ordenar la frecuencia de manera númerica de mayor a menor


Solución:

```bash
grep -v "#" ../data/Buchnera_aphidicola.gff | cut -f3 | sort | uniq -c | sort -nr
```

**Resultados**

```
606 gene
    593 CDS
     38 exon
     32 tRNA
     24 pseudogene
      3 rRNA
      1 tmRNA
      1 SRP_RNA
      1 RNase_P_RNA
      1 region
```

3. **Features ordenados**. [ 30% ]

Genera un nuevo archivo GFF llamado genoma_ordenado.txt , ordenado por tipo de feature y después por posición genómica de manera mumérica ( toma la posición izquierda/la menor). No olvides quitar los comentarios.

Algoritmo:

1. Quitar los comentarios del archivo de features
2. Ordenar por la columna 3 (tipo de feature) y por la columna 4 (posición genómica izquierda del feature). 
3. Mandar la salida del ordenamiento a un archivo 

Solución

```
grep -v "#" ../data/Buchnera_aphidicola.gff | sort -t $'\t' -k3,3 -k4,4n  > Buchnera_aphidicola_ordenado.gff
```


4. **tRNAs** [ 30% ] 

Descarga el archivo `*rna_from_genomic.fna.gz` de tu genoma. Queremos saber si todos los tRNAs del archivo (gbkey=tRNA) `*rna_from_genomic.fna.gz`, se encuentran en el archivo GFF.  Mánda los resultados de los tRNAs a un archivo. Y responde si todos los tRNAs fueron encontrados.


Algoritmo:

`*rna_from_genomic.fna.gz` 
1. Filtra las lineas que contengan el patrón `gbkey=tRNA` del archivo `*rna_from_genomic.fna.gz` 
2. Cortar el ID de los tRNAs que serviran como patrones de busqueda
3. Redirecciona la salida a un archivo 
3. Buscar los IDs de los tRNAS del archivo, en el archivo GFF
4. Filtar solo aquellas líneas que el feature sea `tRNA` 
5. Contamos las lineas del resultado
6. Contamos las lineas del archivo de patrones y comparamos resultados


Solución:

```bash
# opcion 1
grep "gbkey=tRNA" ../data/Buchnera_aphidicola_rna_from_genomic.fna | cut -d " " -f1 | cut -c23-34 | grep -f - ../data/Buchnera_aphidicola.gff | grep -P  "\ttRNA\t" | wc

#opcion 2
grep "gbkey=tRNA" ../data/Buchnera_aphidicola_rna_from_genomic.fna | cut -d " " -f1 | cut -c23-34 > patrones.txt
grep -f patrones.txt ../data/Buchnera_aphidicola.gff | grep -P  "\ttRNA\t" | wc
```


