# Introducción a la Bioinformática 

URL: https://lcg-cursos.github.io/material/introbioinfo/

## Descripción del curso:
El objetivo de este curso es familiarizar a los estudiantes con las herramientas bioinformáticas básicas más importantes y de uso frecuente en el área. Se abordarán temas como el sistema operativo Linux, bases de datos biológicas, manejo de secuencias y genomas, alineamientos y automatización de tareas con scripts.

## Información del curso

- **Semestre:** agosto-diciembre 
- **Modalidad:** Curso regular  
- **Lugar:** Centro de Ciencias Genómicas, UNAM  
- **Duración:** 2 horas por sesión, 28 sesiones  
- **Disponibilidad en línea:** Sí, el curso contará con modalidad virtual  

## Temario

### Biología Computacional
- Introducción a la bioinformática
- Secuencias y genomas
  - Tipos de secuencias
  - Código genético
  - Formatos de secuencias (FASTA)
- Bases de datos biológicas
  - NCBI: Genomes, Nucleotide, PubMed, etc.
  - EMBL, DDBJ
- Alineamientos de secuencias
  - Alineamientos de pares y múltiples secuencias
  - Herramienta BLAST
  - Homología entre secuencias (Homólogo, Ortólogo, Parálogo, Xenólogo)

### Computación
- Uso de buenas prácticas
- Introducción al Shell de Linux
- Navegación y manipulación de archivos
- Uso de tuberías y filtros
- Patrones y expresiones regulares
- Automatización con scripts de Shell


### Temas

El Plan de clases detallado con actividades, recursos, plantillas, material de lectura esta disponible en pdf. Aquí listamos la organización de los temas y las habilidades que el alumno debe lograr.

|Tema  | Objetivo |
| --- | ---- |
| [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) | a) Los alumnos deberán conocer y usar un estándar (markdown) para la creación de documentos textos con formato, muy usado unix y bioinformática. <br>  b) El alumno debe entender las fases del análisis de datos necesarias al abordar un problema en bioinformática. |
| [Buenas Practicas](https://lcg-cursos.github.io/material/introbioinfo/L2-buenas-practicas.html#1)	| a) El alumno deben comprender la importancia de las buenas prácticas en el análisis de datos (FAIR datos, FAIR software). <br> b) El alumno debe Identificar/crear los medatados de los datos a usar en proyectos de análisis bioinformáticos. <br>  c) El alumno debe Identificar/crear  los metadatos del software a usar en proyectos de análisis bioinformáticos. |
| [El shell y protocolos de internet.](https://lcg-cursos.github.io/material/introbioinfo/L3-shell.html) | a) El alumnos debe comprender que es unix y para que se usa. <br>  b) El alumno debe comprender los protocolos que existen de intercambio de datos en internet. <br>  c) El alumno debe comprender y usar el protocolo de  transferencia de archivos y acceso a servidores remotos.
| [El shell: Sistema de archivos y comandos básicos de navegación.](https://lcg-cursos.github.io/material/introbioinfo/L3-shell.html#47) | a) El alumnos debe entender y saber desplazarse en el sistema de archivos en unix ( diapo 39 - 60) <br> b) El alumnos debe conocer los comandos usados para las operaciones básicas de archivos y directorios.
|[El shell: Tipos de archivos y operaciones básicas.](https://lcg-cursos.github.io/material/introbioinfo/L3-shell.html#70)| a) El alumno debe entender los tipos de archivos, visualizar su contenido y como se manejan en unix. <br> b) El alumnos debe saber comprimir/descomprimir archivos.<br>  c) El alumno debe comprender el uso de permisos en la estructura de archivos de unix. 
|[Dogma Central y Formatos de secuencias biológicas. DB: Genbank.](https://lcg-cursos.github.io/material/introbioinfo/L4-archivos.html)| a) Lxs alumnxs deberán ser capaces de comprender el dogma central de la biología, los formatos de secuencias biológicas. <br> b) Los alumnos deben comprender los conceptos relacionados a bases de datos, como ID, registro, propiedades, etc. <br>   c) El alumno explorará la base de datos GenBank.|
| [DB: Genomes y PubMed. Archivos: Descarga, Integridad y Visualización.](https://lcg-cursos.github.io/material/introbioinfo/L4-archivos.html#34) |a) El alumno conocerán los comandos para descargar secuencias, ver los archivos de secuencias y generar nuevos archivos. <br>  b) El alumno conocerá la base de datos PubMed y Genomes. <br>  c) El alumno debe comprender la importancia de la integridad en la descarga de archivos.|
|[Archivos: Visualizar, Editar y Crear](https://lcg-cursos.github.io/material/introbioinfo/L4-archivos.html#63) | a) El alumno debe aprender a usar los comandos para visualizar el contenido de un archivo. <br>  b) El alumno debe aprender a usar editores de texto en el servidor |
| [Procesos](https://codigofacilito.com/articulos/unix-process) | a) El alumno debe comprender el manejo de procesos en unix.
| [redireccionamientos y tuberias](https://lcg-cursos.github.io/material/introbioinfo/L5-tuberias.html#1) | a) El alumno debe aprender a usar los rediccionamientos y tuberias en unix para tareas en bioinformática. |
| [Análisis de un Genoma: comandos para el análisis de archivos fasta y GFF.](https://lcg-cursos.github.io/material/introbioinfo/L6-conteos.html) | a) El alumno deberá aplicar los conocimientos adquiridos previamente para el análisis de un genoma. |
| [Análisis de un Genoma: patrones y filtros](https://lcg-cursos.github.io/material/introbioinfo/L7-filtros.html#1) | a) El alumno deberá aplicar el uso de patrones para filtrar información de un archivo GFF o fastA |
| [Análisis de Genomas: Expresiones regulares](https://lcg-cursos.github.io/material/introbioinfo/L8-expresiones-regulares.html) | a) El alumno deberá aprender las expresiones regulares y aplicarlas para filtrar información genética. |
| [Sustituciones	](https://lcg-cursos.github.io/material/introbioinfo/tr_sed.html#1)| El alumno aprenderá como realizar sustituciones y transformaciones de datos. |
| [Base de datos ensembl y Formateo de datos con awk](https://lcg-cursos.github.io/material/introbioinfo/ensembl-awk.html#41) | a) El alumno debe ser capaz de aplicar filtros y reformatear archivos de datos con awk. <br>  b) El alumno conocerá la base de datos ensembl y aprenderá a usar biomart.|
| [Alineamientos](https://lcg-cursos.github.io/material/introbioinfo/alineamientos.html)	| a) El alumno debe ser capaz de entender el concepto de similitud entre secuencias. |
| [Blast, variables y scripts](https://lcg-cursos.github.io/material/introbioinfo/blast_var_for_scripts.html) | a) El alumno debe ser capaz de entender el uso de blast y el uso de variable  y scripts en unix. |
| [Homología y ciclos](https://lcg-cursos.github.io/material/introbioinfo/blast_var_for_scripts.html#34)| a) El alumno debe ser capaz de entender el uso de ciclos |



## Evaluación

- **Participación en clase:** 10%  
- **Proyecto de investigación:** 30%  
- **Trabajos:** 50%  
- **Exámenes:** 10%  

## Bibliografía recomendada

1. Buffalo, V. (2015). *Bioinformatics Data Skills: Reproducible and Robust Research with Open Source Tools.* O'Reilly Media, Inc.
2. Shotts Jr, W. E. (2012). *The Linux Command Line: A Complete Introduction.* No Starch Press.

## Contacto

**LI Heladia Salgado**   
- **Entidad académica:** Programa de Genómica Computacional, Centro de Ciencias Genómicas, UNAM  
- **Correo electrónico:** heladia@ccg.unam.mx  


## Créditos  

* Este material fue desarrollado con base en una primera versión elaborada por **Laura Gómez**, disponible el latex. 

