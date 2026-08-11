# Introducción a la bioinformática.

## EXAMEN 1


>  Nombre:   
>  Nombre de usuario (tepeu) :   

> Genoma: Buchnera_aphidicola

### Instrucciones

- Edita este archivo en StackEdit o algún editor Markdown.
- Lee con cuidado cada pregunta y contesta lo que se pide.
- El archivo final con las respuestas súbelo a la plataforma del curso en la tarea que dice "Examen 1".
- Puedes usar cualquier recurso disponible, como el asistente "Profe Unix" compartido en chatgpt, buscar en google, sacar tus notas. Lo que NO SE PERMITE, es preguntar a otros, por ningún medio. Si se te descubre enviando mensaje por algún chat, el examen queda cancelado, sin opción de volverlo a presentar.
- Las respuestas del examen deben ser con los comandos vistos en clase. En caso de que pongas comandos más avanzados, se te pedirá que expliques el funcionamiento del comando.
- Todas las respuestas (instrucciones) deberás ejecutarlas en el servidor tepeu, por lo que al final debe existir una carpeta y documentos del proceso que vayas haciendo.


## SECCIÓN TEÓRICA [ 15% ]

1. ¿Cuál es la estructura recomendada para un proyecto, de acuerdo a las buenas prácticas? [Clase 1]

```
bin/        # scripts ejecutables (bash, python)
data/       # datos (raw/ originales; external/ de terceros; processed/ derivados)
doc/        # documentación y apuntes del proyecto
results/    # resultados (tablas/figuras) listos para reporte
```

2. Para que un experimento o un análisis computacional sea confiable, ¿qué tiene que cumplir?  [lectura del capítulo 1, clase 1]

Ante todo tiene que ser reproducible.

<!-- Pueden ser estas palabras o algo similar. El punto es que los datos deben ser verificados los que se usen, documentarlos con metadatos, y si hay programas e incluso los datos saber las versiones  -->

Y eso se logra:   
- Trazabilidad (origen de datos y versiones).
- Reproducibilidad (scripts + parámetros versionados).
- Control de versiones (Git).
- Estructura y metadatos claros.
- Automatización (pipelines) y registros (logs).
- Verificación de integridad (checksums).


3. ¿Qué es un patrón? puedes dar dos ejemplos. [Clase de Patrones con grep]

Una expresión (texto) que describe lo que queremos localizar/filtrar en archivos.

4. Menciona 2 formatos usados para manejar las secuencias de DNA o proteínas y sus features o propiedades

FASTA (secuencia) y GFF3 (anotaciones/features).
(Otros válidos: GenBank/GBK, EMBL; para proteínas FASTA; para features GTF/GFF3.)

5. Menciona qué es una base de datos y dá algunos ejemplos.

Conjunto organizado de información con reglas de acceso/actualización.
Ejemplos: NCBI (Nucleotide/Genomes/Protein), RefSeq, GenBank, Ensembl, UniProt.


## Buenas Prácticas

### Estructura del Repositorio. [ 5% ]
Crea una estructura de directorios para un proyecto de análisis de genomas con el nombre del organismo, que incluya carpetas para datos brutos, scripts, análisis, y resultados. Muestra los comandos usados para crear esta estructura.

**Algoritmo**  
1. Crear directorios base del proyecto con el nombre del organismo.  
2. Incluir carpetas para datos brutos, scripts, análisis y resultados.  
3. Verificar estructura.

**Solución**

<!-- una alternativa de solución el nombre de la carpeta puede ser proyecto_Buchnera_aphidicola o Buchnera_aphidicola -->

```bash
# 1) Crear proyecto
mkdir -p Buchnera_aphidicola
cd Buchnera_aphidicola

# 2) Estructura recomendada
mkdir bin/ src/ doc/ results/ 

# 3) Verificar (sin tree): listado recursivo
ls -lt
```



### Nombre Adecuado de Archivos [ 5% ]
Descarga el archivo FASTA de NCBI del genoma asignado y nómbralo siguiendo un esquema de nombres adecuado (por ejemplo, GENUS_species_VERSION.fasta).
En esta pregunta, deberas indicar el algoritmo o los pasos a seguir para que cualquier usuario pueda ir y descargar los datos del genoma.

**Algoritmo (vía navegador)**  
1. Abrir navegador → buscar “NCBI genomes”.  
2. Entrar a “NCBI Datasets → Genomes”.  
3. Buscar **Buchnera aphidicola** (escoger ensamblado RefSeq si es posible).  
4. Abrir el ensamblado elegido y **copiar el accession** (ej. `GCF_XXXXXXXXX.Y`).  
5. En la página FTP/Download, localizar el archivo **genomic.fna.gz**.  
6. Copiar la URL directa de descarga.  
7. En el servidor, colocar el archivo en `data/` y **nombrar** como `GENUS_species_VERSION.fasta.gz`. O bien dejar el nombre tal y como se descarga.



Solución:

```bash

cd Buchnera_aphidicola/data

# descargando los archivos
wget -O  Buchnera_aphidicola_genomic.fna.gz https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/007/365/GCF_000007365.1_ASM736v1/GCF_000007365.1_ASM736v1_genomic.fna.gz

# Estos no se piden en esta pregunta pero los vaos a necesitar
wget -O  Buchnera_aphidicola_genomic.gff.gz  https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/007/365/GCF_000007365.1_ASM736v1/GCF_000007365.1_ASM736v1_genomic.gff.gz

wget -O Buchnera_aphidicola_rna_from_genomic.fna.gz https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/007/365/GCF_000007365.1_ASM736v1/GCF_000007365.1_ASM736v1_rna_from_genomic.fna.gz

# descomprimir el archivo
gunzip *

ls -l
```



### Adición de Metadatos [ 5% ]

Añade un archivo metadata.md usando un editor (nano / vi) que proporcione información básica sobre los archivos del directorio de datos y sus fuentes. Muestra el contenido del archivo.

Ejemplo de archivo `metadata.md`. Este archivo tiene que estar en el directorio de datos descargados.


```bash
nano data/metadata.md
```

**Contenido sugerido:**

```
# Metadatos del Proyecto Genoma

Este directorio contiene los archivos descargados para el análisis del genoma de *Buchnera aphidicola*.

## Archivos
- Buchnera_aphidicola_GCF_XXXXXXXXX.Y.fasta.gz : Secuencia genómica en formato FASTA (comprimido).

## Fuente de Datos
- NCBI - National Center for Biotechnology Information
  - Ensamblado: GCF_XXXXXXXXX.Y
  - URL FTP del ensamblado: (pegar aquí la URL del directorio FTP)
  - Fecha de descarga: YYYY-MM-DD

```

###  Verificación de Integridad de Datos [ 3% ]

Realiza la verificación de integridad DE UN SOLO archivo descargado usando checksum. 
nota: aunque debe hacerse para cualquier archivo que se descargue y se vaya a usar, por cuestiones de tiempo solo se pedirá las instrucciones para uno de ellos.

Algoritmo:

1. 
2. 


Solución:

```bash
md5sum  Buchnera_aphidicola_genomic.fna  # suma del archivo descomprimido
```

<!-- NOTA: Un archivo comprimido vs descomprimido NO tienen los mismos check sum, por lo que en NCBI se indica la suma tanto de archivos comprimidos y descomprimidos. Si el alumno descomprimió los archivos deberá compararlo con las sumas de archivos descomprimidos que muestra NCBI. Por lo que el valor de abajo en el ejemplo  no será el mismo, porque se muestra la suma de un .gz. -->

Te dará un valor o string que debe ser idéntico al que esta en la página FTP del genoma descargado, que tiene el nombre de `md5checksums.txt`. 

Por ejemplo:

file:md5checksums.txt

```
2238238dd39e11329547d26ab138be41  ./GCF_000005845.2_ASM584v2_genomic.gff.gz
```

```bash
md5sum  GCF_000005845.2_ASM584v2_genomic.gff.gz
```

El valor que genere debe ser `2238238dd39e11329547d26ab138be41` indicando que se descargó de manera completa.

### Protección de datos críticos [ 2% ]

Queremos proteger los datos que hemos descargado, para que no se puedan borrar o modificar. Entonces protege el DIRECTORIO donde estan los datos para que sólo sea de LECTURA y de ACCESO A ÉL. Los archivos dentro del directorio sólo deben tener permisos de lectura.


```bash
chmod u-wx *
cd ..
chmod a-w data
```
o tambien 

```bash
cd .. 
pwd  # estamos en el directorio del proyecto
chmod 555 data/  # todos tienen lectura y ejecución, 
chmod a-w data/*
chmod a+r data/
ls -l data/raw
```

se ve asi :

```
dr-xr-xr-x  2 user user 4096 Oct  2 19:00 data/
```

## Análisis de datos

Para esta parte, para la respuesta a cada pregunta, deberás indicar el algoritmo y posteriormente indicar los comandos que lo solucionan. 

**IMPORTANTE!!!**: 

> Para todas las instrucciones se asumirán que estás en el directorio de trabajo del genoma. Deberás indicar los paths relativos.

1. **Total de features**. [ 10% ].  
Usando el archivo de features del genoma, queremos saber CUÁNTOS TIPOS de features tiene anotados el genoma de estudio.

**Algoritmo**

1. Limpiar el archivo, quitando las líneas de comentarios.
2. Cortar la columna 3, que indica el tipo de feature.
3. Ordenar los datos para poder quitar repeticiones de features.
4. Quitar repeticiones de features.
5. Contar las líneas que nos indica el tipo de features diferentes.


**Solución**

```bash
cd ~/Buchnera_aphidicola

grep -v "#"  data/Buchnera_aphidicola_genomic.gff | cut -f3 | sort -u | wc -l

# o bien
grep -v "#"  data/Buchnera_aphidicola_genomic.gff | cut -f3 | sort | uniq | wc -l
```

**Resultado**

10 Tipos de Feature (CDS, exon, gene, pseudogene, region, RNase_P_RNA, rRNA, SRP_RNA, tmRNA, tRNA)



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

**Algoritmo**

1. Limpiar el archivo, quitando las líneas de comentarios.
2. Cortar la columna 3, que indica el tipo de feature.
3. Ordenar los datos para agrupar por tipo de feature
4. Contar el número de veces que aparece un feature
5. Ordenar por la frecuencia del feature de mayor a menor


**Solución**

```bash
grep -v "#"  data/Buchnera_aphidicola_genomic.gff | cut -f3 | sort | uniq -c | sort -nr > results/feature_counts.txt
```

**Resultado**
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



3. **Features ordenados**. [ 30% ]

Genera un nuevo archivo GFF llamado genoma_ordenado.txt , ordenado por tipo de feature y después por posición genómica de manera mumérica (toma la posición izquierda/la menor). No olvides quitar los comentarios.

**Algoritmo**

1. Quitar los comentarios del archivo de features
2. Ordenar por la columna 3 (tipo de feature) y por la columna 4 (posición genómica izquierda del feature) 
3. Mandar la salida del ordenamiento a un archivo 

**Solución**

```bash
grep -v "#" data/Buchnera_aphidicola_genomic.gff | sort -t $'\t' -k3,3 -k4,4n > results/Buchnera_aphidicola_genomic_sorted.gff  # o bien  genoma_ordenado.txt  
```

<!-- si la respuesta viene sin $'\t' se da como valida sino se vió en clase -->

Explicación: 

El $'...' es una expansión de comillas ANSI-C en Bash.

Sirve para escribir caracteres especiales (que normalmente no puedes poner literal en la terminal) usando secuencias como \t, \n, \r, etc.  Ejemplo: sort -t $'\t'  sort -t $'\x1f'   es decir cuando el caracter es invisible.


4. **tRNAs** [ 15% ] 

Descarga el archivo `*rna_from_genomic.fna.gz` de tu genoma. Queremos saber si todos los tRNAs del archivo (gbkey=tRNA) `*rna_from_genomic.fna.gz`, se encuentran en el archivo GFF.  Mánda los resultados de los tRNAs a un archivo. Y responde si todos los tRNAs fueron encontrados.


**Algoritmo**

1. **Descargar el archivo** `rna_from_genomic.fna.gz` desde el FTP de NCBI y guardarlo en `data/` con un nombre adecuado.
    
2. **Verificar la integridad** del archivo descargado comparando su hash MD5 con el publicado en `md5checksums.txt`.
    
3. **Descomprimir** el archivo FASTA de RNAs en `data/`.
    
4. **Obtener los IDs de tRNA** desde el FASTA (líneas con `gbkey=tRNA`) y guardarlos en `results/tRNA_IDS_fasta.txt`.
    
5. **Buscar esos IDs en el archivo GFF**, filtrando por el feature `gene` (curado RefSeq), y guardar los IDs encontrados en `results/tRNAs_ID_gff.txt`.
    
6. **Comparar ambas listas (FASTA vs GFF)**: unir, ordenar y contar duplicados. Si todos aparecen 2 veces y el número de líneas coincide, significa que todos los tRNAs del FASTA fueron encontrados en el GFF.

**Solución**

```bash

# bajamos el archivo
wget  https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/007/365/GCF_000007365.1_ASM736v1/GCF_000007365.1_ASM736v1_rna_from_genomic.fna.gz  -O data/Buchnera_aphidicola_rna_from_genomic.fna.gz

# descomprimimos el archivo
gunzip data/Buchnera_aphidicola_rna_from_genomic.fna.gz

# Validamos que se haya descargado con md5

# 2. Obtenemos el ID de los tRNAs que serviran como patrones de busqueda
grep ">" data/Buchnera_aphidicola_rna_from_genomic.fna | grep "gbkey=tRNA" | cut -d" " -f1 | cut -c23-34 | sort -u  > results/tRNA_IDS_fasta.txt

# Buscamos los IDs (regresa mas de una feautre (gene, tRNAs), nos quedamos con la fuente RefSeq que es la curada, por lo tanto filtramos por el feature "gene" o puede ser "RefSeq"
grep -f results/tRNA_IDS_fasta.txt data/Buchnera_aphidicola_genomic.gff  | grep  "\tgene\t" | cut -f9 | cut -d";" -f1 | cut -c9- | sort -u > results/tRNAs_ID_gff.txt

# Si unimos los dos archivos, ordenamos y contamos repetidos. Si todos tienen 2, es que TODOS fueron encontrados. 
# Y contamos el número de lineas y deben ser el mismo total.
cat results/tRNA_IDS_fasta.txt results/tRNAs_ID_gff.txt | sort | uniq -c 

wc results/tRNAs_ID_gff.txt
wc results/tRNA_IDS_fasta.txt
```


**Resultado**

Sí, los 32 tRNAs del archivo `*rna_from_genomic.fna.gz` se encuentran en el archivo GFF


