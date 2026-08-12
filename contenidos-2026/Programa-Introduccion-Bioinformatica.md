# Programa 2026 --- Introducción a la Bioinformática

**Licenciatura en Ciencias Genómicas · UNAM**\
**Curso de primer semestre**\
**Plan operativo:** 34 sesiones de 2 horas\
**Organización:** 6 unidades + ejes transversales de reproducibilidad,
buenas prácticas e inteligencia artificial

------------------------------------------------------------------------

## Índice

1.  [Descripción del curso](#1-descripción-del-curso)
2.  [Propósito general](#2-propósito-general)
3.  [Enfoque formativo](#3-enfoque-formativo)
4.  [Resultados generales de
    aprendizaje](#4-resultados-generales-de-aprendizaje)
5.  [Ejes de contenido](#5-ejes-de-contenido)
    -   [5.1 Biología y datos
        biológicos](#51-biología-y-datos-biológicos)
    -   [5.2 Cómputo y herramientas
        bioinformáticas](#52-cómputo-y-herramientas-bioinformáticas)
    -   [5.3 Reproducibilidad y buenas
        prácticas](#53-reproducibilidad-y-buenas-prácticas)
    -   [5.4 Razonamiento científico e
        interpretación](#54-razonamiento-científico-e-interpretación)
    -   [5.5 Uso crítico y responsable de inteligencia
        artificial](#55-uso-crítico-y-responsable-de-inteligencia-artificial)
6.  [Contenido por unidades](#6-contenido-por-unidades)
    -   [Unidad 1. Trabajo reproducible y comunicación
        científica](#unidad-1-trabajo-reproducible-y-comunicación-científica)
    -   [Unidad 2. Entorno UnixLinux y cómputo
        científico](#unidad-2-entorno-unixlinux-y-cómputo-científico)
    -   [Unidad 3. Datos y bases de datos
        biológicas](#unidad-3-datos-y-bases-de-datos-biológicas)
    -   [Unidad 4. Procesamiento y exploración de datos
        genómicos](#unidad-4-procesamiento-y-exploración-de-datos-genómicos)
    -   [Unidad 5. Automatización de análisis bioinformáticos con
        Shell](#unidad-5-automatización-de-análisis-bioinformáticos-con-shell)
    -   [Unidad 6. Comparación de secuencias y construcción de hipótesis
        biológicas](#unidad-6-comparación-de-secuencias-y-construcción-de-hipótesis-biológicas)
7.  [Mapa integrado de contenidos](#7-mapa-integrado-de-contenidos)
8.  [Competencias](#8-competencias)
9.  [Metodología de enseñanza](#9-metodología-de-enseñanza)
10. [Evidencias y evaluación](#10-evidencias-y-evaluación)
11. [Productos acumulativos del
    curso](#11-productos-acumulativos-del-curso)
12. [Uso de inteligencia artificial](#12-uso-de-inteligencia-artificial)
13. [Perfil de egreso del curso](#13-perfil-de-egreso-del-curso)
14. [Continuidad curricular](#14-continuidad-curricular)

------------------------------------------------------------------------

# 1. Descripción del curso

**Introducción a la Bioinformática** es el curso de entrada a la
formación bioinformática de la Licenciatura en Ciencias Genómicas.
Integra fundamentos biológicos, manejo de datos, cómputo científico,
herramientas Unix/Linux, automatización, comparación de secuencias,
reproducibilidad y razonamiento científico.

El curso no está organizado como un catálogo de programas o comandos.
Las herramientas se introducen en el contexto de **preguntas biológicas
concretas** y conforme el estudiante necesita nuevas estrategias para
obtener, transformar, verificar e interpretar evidencia.

La progresión general es:

``` text
pregunta biológica
→ evidencia necesaria
→ datos
→ operación
→ herramienta
→ resultado
→ verificación / validación
→ interpretación
→ conclusión y límites
```

De esta manera, el estudiante aprende desde el inicio que ejecutar
correctamente una herramienta no equivale a resolver un problema
bioinformático. Una respuesta científica requiere comprender qué
representan los datos, justificar la estrategia, comprobar los
resultados y distinguir entre lo que la evidencia muestra y lo que
permite inferir.

------------------------------------------------------------------------

# 2. Propósito general

Desarrollar en el estudiante las bases conceptuales, computacionales y
metodológicas necesarias para resolver problemas bioinformáticos
introductorios mediante el uso reproducible de datos biológicos y
herramientas computacionales, con énfasis en la comprensión de los
datos, la automatización de procedimientos, la interpretación crítica de
resultados y la construcción de conclusiones sustentadas en evidencia.

------------------------------------------------------------------------

# 3. Enfoque formativo

El curso articula cinco dimensiones que evolucionan simultáneamente:

``` text
BIOLOGÍA
¿Qué representa el dato?
        │
        ▼
DATOS
¿De dónde provienen y cómo están representados?
        │
        ▼
CÓMPUTO
¿Qué operación y herramienta necesito?
        │
        ▼
REPRODUCIBILIDAD
¿Cómo documento, verifico y repito el análisis?
        │
        ▼
INTERPRETACIÓN
¿Qué puedo concluir y cuáles son los límites?
```

Estas dimensiones no se imparten como bloques independientes. Se
integran progresivamente en las actividades y problemas del curso.

------------------------------------------------------------------------

# 4. Resultados generales de aprendizaje

Al finalizar el curso, el estudiante será capaz de:

1.  formular preguntas bioinformáticas básicas e identificar la
    evidencia necesaria para responderlas;
2.  documentar procedimientos y resultados mediante protocolos
    reproducibles;
3.  organizar proyectos computacionales preservando datos originales y
    metadatos;
4.  trabajar en un entorno Unix/Linux local y remoto;
5.  recuperar datos de recursos biológicos públicos y documentar su
    procedencia;
6.  reconocer e interpretar archivos FASTA, GenBank y GFF/GFF3;
7.  inspeccionar, filtrar, transformar, ordenar, resumir y contrastar
    archivos biológicos;
8.  interpretar conteos, coordenadas, longitudes, distribuciones y otras
    medidas derivadas;
9.  construir tuberías transparentes mediante herramientas Unix;
10. transformar un procedimiento validado en un script reutilizable;
11. parametrizar scripts y procesar múltiples archivos;
12. documentar, probar y validar herramientas computacionales sencillas;
13. ejecutar trabajos bioinformáticos en infraestructura de cómputo
    remoto y sistemas de colas;
14. interpretar alineamientos de secuencias;
15. diseñar y ejecutar búsquedas BLAST reproducibles;
16. integrar identidad, similitud, cobertura, E-value, bit score y HSP
    en la evaluación de resultados;
17. distinguir similitud de homología;
18. razonar sobre ortología, paralogía y xenología con base en
    evidencia;
19. construir hipótesis biológicas indicando alternativas, incertidumbre
    y evidencia faltante;
20. utilizar herramientas de inteligencia artificial de manera crítica,
    ética y verificable.

------------------------------------------------------------------------

# 5. Ejes de contenido

## 5.1 Biología y datos biológicos

### Fundamentos biológicos

-   DNA, RNA y proteínas.
-   Flujo de información genética.
-   Gen y producto génico.
-   Secuencias de nucleótidos y aminoácidos.
-   Genoma y replicón.
-   Coordenadas genómicas.
-   Cadenas positiva y negativa.
-   Regiones codificantes.
-   Anotación biológica.
-   Features genómicos.
-   Relación entre secuencia, registro y anotación.

### Representación de información biológica

-   Secuencias y metadatos.
-   FASTA.
-   GenBank.
-   GFF/GFF3.
-   Tablas derivadas de bases de datos.
-   Identificadores.
-   Versiones.
-   Registros.
-   Campos y atributos.
-   Delimitadores.
-   Encabezados.
-   Valores faltantes.

### Bases de datos biológicas

-   Recursos de NCBI.
-   Genomes.
-   Nucleotide.
-   PubMed.
-   UniProt como fuente independiente para el contraste de inventarios.
-   Registro e identificador.
-   Versionado.
-   Procedencia.
-   Descarga de secuencias y genomas.
-   Integridad de los archivos recuperados.
-   Comparación entre fuentes independientes.

### Exploración de genomas

-   Inventario de features.
-   Genes y CDS.
-   Conteos.
-   Distribución por replicón.
-   Distribución por cadena.
-   Longitud de genes.
-   Mínimo, máximo, media y mediana.
-   Densidad génica.
-   Tamaño del genoma.
-   Comparación de resultados con metadatos y fuentes independientes.

### Comparación de secuencias

-   Correspondencia entre posiciones.
-   Coincidencia.
-   Sustitución.
-   Inserción/deleción.
-   Brecha (*gap*).
-   Identidad.
-   Similitud.
-   Cobertura.
-   Alineamientos de pares.
-   Alineamientos múltiples.
-   Comparación de secuencias de nucleótidos y proteínas.

### Búsqueda de similitud

-   Pregunta de búsqueda.
-   Secuencia consulta.
-   Base de datos.
-   Búsqueda heurística.
-   Semillas.
-   Tamaño de palabra.
-   Extensión.
-   HSP.
-   Sensibilidad y velocidad.
-   BLASTN.
-   BLASTP.

### Interpretación biológica y evolución

-   Identidad y cobertura como medidas diferentes.
-   E-value.
-   Bit score.
-   Alineamientos parciales.
-   Múltiples HSP.
-   Ranking de candidatos.
-   Similitud observada.
-   Homología inferida.
-   Especiación.
-   Duplicación génica.
-   Ortólogos.
-   Parálogos.
-   Xenólogos.
-   Transferencia de función.
-   Limitaciones de las búsquedas de similitud.
-   Evidencia suficiente e insuficiente.
-   Hipótesis biológica y explicaciones alternativas.

------------------------------------------------------------------------

## 5.2 Cómputo y herramientas bioinformáticas

### Entorno Unix/Linux

-   Unix y Linux.
-   Shell.
-   Terminal.
-   Línea de comandos.
-   Sintaxis básica de comandos.
-   Manuales y sistemas de ayuda.
-   Sistema de archivos.
-   Rutas absolutas y relativas.
-   Directorio de trabajo.
-   Archivos y directorios.
-   Creación, copia, movimiento y eliminación.
-   Edición de archivos de texto.
-   Tipos de archivo.
-   Compresión y descompresión.
-   Permisos.
-   Procesos.

### Cómputo remoto

-   Servidores.
-   SSH.
-   Transferencia de archivos.
-   SFTP.
-   SCP.
-   `rsync`.
-   Verificación de transferencias.
-   Sumas de comprobación e integridad.

### Entrada, salida y composición de herramientas

-   Entrada estándar.
-   Salida estándar.
-   Salida de error.
-   Redirecciones.
-   Tuberías.
-   Encadenamiento de operaciones.
-   Flujos de datos.

### Inspección, selección y resumen

-   `cat`.
-   `less`.
-   `head`.
-   `tail`.
-   `wc`.
-   `cut`.
-   `sort`.
-   `uniq`.
-   Herramientas afines de inspección y resumen.

### Búsqueda y patrones

-   `grep`.
-   Búsqueda literal.
-   Patrones.
-   Expresiones regulares.
-   Falsos positivos.
-   Falsos negativos.
-   Validación de patrones.

### Transformación de texto

-   `tr`.
-   `sed`.
-   Normalización.
-   Sustitución.
-   Limpieza controlada.
-   Conversión de delimitadores.
-   Extracción de identificadores y campos.

### Procesamiento estructurado con `awk`

-   Delimitadores.
-   Campos `$1 … $NF`.
-   `NR`.
-   `NF`.
-   Patrones.
-   Acciones.
-   Condiciones lógicas.
-   `&&`.
-   `||`.
-   Aritmética sobre campos.
-   Formateo de salida.
-   Cálculos sobre coordenadas.
-   Condiciones multicolumna.

### Scripting en Shell

-   Script.
-   Intérprete.
-   *Shebang*.
-   Comentarios.
-   Permisos de ejecución.
-   Variables.
-   Expansión.
-   Sustitución de comandos.
-   Parámetros de entrada.
-   Validación de argumentos.
-   Validación de archivos.
-   Mensajes de uso.
-   Códigos y mensajes de error.
-   Ciclos `for`.
-   Procesamiento por lotes.
-   Organización de salidas.
-   Reportes.
-   Pruebas con datos nuevos.
-   Documentación de herramientas.
-   README de software.

### Cómputo de alto rendimiento

-   Nodo de acceso.
-   Nodo de cómputo.
-   Trabajo (*job*).
-   Sistema de colas.
-   SGE.
-   Script de trabajo.
-   `qsub`.
-   `qstat`.
-   `qdel`.
-   Salida estándar y salida de error del trabajo.
-   Criterios para decidir cuándo utilizar un cluster.
-   Reproducibilidad entre infraestructuras.

### Herramientas de comparación y búsqueda

-   Herramientas de alineamiento utilizadas en las prácticas.
-   BLAST.
-   `makeblastdb`.
-   `blastn`.
-   `blastp`.
-   Bases de datos locales.
-   Formatos de salida.
-   Salida tabular.
-   Parámetros de búsqueda.

------------------------------------------------------------------------

## 5.3 Reproducibilidad y buenas prácticas

### Documentación científica

-   Markdown.
-   Protocolo computacional.
-   Pregunta y subpreguntas.
-   Estrategia.
-   Metodología.
-   Resultados.
-   Discusión.
-   Conclusiones.
-   Registro de decisiones.

### Organización reproducible de proyectos

Estructura de referencia:

``` text
proyecto/
├── data/
│   ├── source/
│   └── processed/
├── src/
├── results/
└── doc/
```

Principios:

-   preservar datos originales;
-   no editar `data/source/`;
-   separar datos originales de derivados;
-   separar código de datos;
-   conservar resultados trazables;
-   documentar procedencia;
-   utilizar nombres comprensibles;
-   conservar parámetros y comandos;
-   permitir que otra persona reconstruya el análisis.

### FAIR

-   Encontrable (*Findable*).
-   Accesible (*Accessible*).
-   Interoperable (*Interoperable*).
-   Reutilizable (*Reusable*).
-   Metadatos.
-   Diccionario de variables.
-   Procedencia.
-   Versiones.
-   Identificadores.

### Integridad y trazabilidad

-   Verificación de descargas.
-   Verificación de transferencias.
-   Conservación de archivos originales.
-   Registro de transformaciones.
-   Correspondencia entre entradas y salidas.
-   Identificación de archivos intermedios.
-   Registro de parámetros.

### Verificación, validación y robustez

-   Verificar que una operación produjo la salida esperada.
-   Comparar conteos antes y después de una transformación.
-   Utilizar ejemplos pequeños y controlados.
-   Contrastar con documentación.
-   Contrastar con otra herramienta o estrategia cuando sea pertinente.
-   Comparar resultados con una fuente independiente.
-   Reconocer discrepancias legítimas entre fuentes.
-   No confundir reproducibilidad con validez biológica.

### Buenas prácticas de scripting

-   partir de un procedimiento previamente validado;
-   separar lógica y datos;
-   parametrizar;
-   validar entradas;
-   generar mensajes comprensibles;
-   evitar sobrescribir datos originales;
-   utilizar nombres de salida trazables;
-   probar con datos diferentes;
-   documentar requisitos, entradas, salidas y uso;
-   conservar evidencia de ejecución.

### Comunicación y revisión científica

-   Revisión por pares.
-   Dictamen sobre evidencia.
-   Corrección a partir de crítica.
-   Defensa de decisiones.
-   Separación entre observación e interpretación.
-   Declaración de limitaciones.
-   Evidencia faltante.
-   Revisión de hipótesis alternativas.

------------------------------------------------------------------------

## 5.4 Razonamiento científico e interpretación

Este eje articula todo el curso.

### Formulación de preguntas

-   ¿Qué quiero saber?
-   ¿Qué evidencia permitiría responderlo?
-   ¿Qué archivo contiene esa evidencia?
-   ¿Qué campo o región debo observar?
-   ¿Qué operación necesito realizar?

### Lectura de resultados

-   Diferenciar salida de herramienta y resultado científico.
-   Identificar qué parte de una salida responde la pregunta.
-   Comprobar consistencia.
-   Detectar resultados inesperados.
-   Reconocer artefactos del procedimiento.

### Interpretación

-   Relacionar una medida computacional con su significado biológico.
-   Comparar explicaciones.
-   Reconocer incertidumbre.
-   No afirmar más de lo que los datos permiten.
-   Distinguir evidencia directa de inferencia.

### Construcción de hipótesis

``` text
observación
→ evidencia
→ interpretación
→ inferencia
→ hipótesis
→ alternativas
→ límites
→ evidencia adicional necesaria
```

------------------------------------------------------------------------

## 5.5 Uso crítico y responsable de inteligencia artificial

### Fundamentos

-   Modelos generativos como asistentes.
-   Prompt.
-   Instrucciones.
-   Contexto.
-   Formato esperado.
-   Limitaciones.
-   Alucinaciones.

### Prompting científico

-   Formular una tarea explícita.
-   Proporcionar contexto suficiente.
-   Definir restricciones.
-   Solicitar explicación o justificación cuando corresponda.
-   Pedir formatos verificables.
-   Refinar instrucciones.

### Regla metodológica

> **Primero a mano; después con IA.**

Flujo:

``` text
resolución propia
→ línea base
→ consulta a IA
→ contraste
→ verificación independiente
→ corrección
→ decisión
→ registro
```

### Validación de respuestas de IA

-   `man`.
-   `--help`.
-   Documentación oficial.
-   Pruebas pequeñas.
-   Archivos controlados.
-   Comparación con resultados manuales.
-   Fuentes biológicas independientes.

### Errores que se busca aprender a detectar

-   opciones inexistentes;
-   sintaxis plausible pero incorrecta;
-   confusión entre variantes de expresiones regulares;
-   comandos que ignoran encabezados o comentarios;
-   conteos incorrectos;
-   modificaciones no solicitadas de los datos;
-   interpretación excesiva de resultados;
-   confusión entre similitud y homología;
-   transferencia injustificada de función.

### Bitácora de IA

`doc/bitacora-ia.md` registra:

-   objetivo de la consulta;
-   prompt;
-   respuesta relevante;
-   estrategia de verificación;
-   discrepancias;
-   correcciones;
-   decisión final.

------------------------------------------------------------------------

# 6. Contenido por unidades

## Unidad 1. Trabajo reproducible y comunicación científica

**Sesiones:** S1--S2

### Propósito

Establecer desde el inicio hábitos de documentación, organización y
razonamiento reproducible e introducir criterios para utilizar
inteligencia artificial de manera crítica.

### Biología y razonamiento científico

-   Problema científico.
-   Pregunta.
-   Subpreguntas.
-   Evidencia.
-   Datos.
-   Resultado.
-   Interpretación.
-   Conclusión.

### Cómputo

-   Markdown.
-   Archivos de texto.
-   Organización inicial del proyecto.
-   Herramientas de IA como asistentes.

### Reproducibilidad y buenas prácticas

-   Protocolo computacional.
-   Estructura del proyecto.
-   FAIR.
-   Metadatos.
-   Diccionario de variables.
-   Preservación de datos originales.
-   Introducción a `bitacora-ia.md`.

### Sesiones

-   **S1 --- Documentar:** Markdown y fases del análisis de datos.
-   **S2 --- Organizar:** buenas prácticas FAIR e introducción al
    prompting científico.

### Evidencia integradora

Inicio del proyecto reproducible: `protocolo.md`, estructura de
directorios, metadatos y primera entrada de la bitácora de IA.

------------------------------------------------------------------------

## Unidad 2. Entorno Unix/Linux y cómputo científico

**Sesiones:** S3--S6

### Propósito

Construir el entorno computacional que se utilizará durante el resto del
curso y desarrollar autonomía básica para trabajar local y remotamente.

### Biología

Los datos biológicos aparecen todavía como contexto de trabajo; el
énfasis de la unidad está en preparar el entorno que permitirá
analizarlos posteriormente.

### Cómputo

-   Unix/Linux.
-   Shell.
-   Terminal.
-   Ayuda.
-   Sistema de archivos.
-   Rutas.
-   Archivos y directorios.
-   Edición.
-   Compresión.
-   Permisos.
-   Procesos.
-   SSH.
-   SFTP.
-   SCP.
-   `rsync`.

### Reproducibilidad y buenas prácticas

-   Estructura estable del proyecto.
-   Registro de comandos.
-   Transferencias verificables.
-   Integridad.
-   Separación entre trabajo local y remoto.
-   Preparación del proyecto para datos biológicos.

### Sesiones

-   **S3 --- Conectar:** shell, acceso remoto y transferencia de
    archivos.
-   **S4 --- Navegar:** sistema de archivos, organización y edición.
-   **S5 --- Gestionar:** archivos, compresión, permisos y procesos.
-   **S6 --- Consolidar:** entorno Unix listo para trabajar con datos
    biológicos.

### Evidencia integradora

Proyecto organizado y accesible en el servidor, con procedimientos de
conexión, transferencia, permisos y manejo de archivos documentados.

------------------------------------------------------------------------

## Unidad 3. Datos y bases de datos biológicas

**Sesiones:** S7--S9

### Propósito

Comprender qué representan los datos biológicos, cómo se codifican en
archivos, cómo se recuperan de bases de datos y cómo se verifica su
procedencia e integridad.

### Biología

-   DNA.
-   RNA.
-   Proteínas.
-   Genes.
-   Productos génicos.
-   Genoma.
-   Secuencias.
-   Anotación.
-   Features.
-   Coordenadas.
-   FASTA.
-   GenBank.
-   GFF/GFF3.
-   Registro.
-   Identificador.
-   Versión.
-   Bases de datos biológicas.

### Cómputo

-   Navegación de recursos de NCBI.
-   Descarga de archivos.
-   Inspección de texto.
-   Edición.
-   SCP.
-   SFTP.
-   `rsync`.
-   Verificación de integridad.

### Reproducibilidad y buenas prácticas

-   Procedencia.
-   Metadatos.
-   Versiones.
-   Integridad.
-   Registro de descarga.
-   Preservación de datos fuente.
-   Selección razonada de archivos.

### Sesiones

-   **S7 --- Representar:** de los objetos biológicos a FASTA, GFF3 y
    GenBank.
-   **S8 --- Recuperar:** bases de datos, descarga y verificación de
    integridad.
-   **S9 --- Verificar:** inspección y transferencia de datos
    biológicos.

### Evidencia integradora

Conjunto de datos biológicos documentado, íntegro y organizado en
`data/source/`, listo para ser analizado.

------------------------------------------------------------------------

## Unidad 4. Procesamiento y exploración de datos genómicos

**Sesiones:** S10--S23\
**Bloque de integración y evaluación:** S14--S17

### Propósito

Construir flujos transparentes para inspeccionar, filtrar, transformar,
resumir, calcular y contrastar datos genómicos hasta producir un
protocolo ejecutable.

### Biología

-   Genoma.
-   Replicones.
-   Genes.
-   CDS.
-   Features.
-   Coordenadas.
-   Cadenas `+` y `−`.
-   Identificadores.
-   Anotación.
-   Longitudes.
-   Densidad génica.
-   Tamaño del genoma.
-   Distribuciones.
-   Discrepancias entre fuentes.

### Cómputo

-   stdin, stdout y stderr.
-   Redirecciones.
-   Tuberías.
-   `head`.
-   `tail`.
-   `wc`.
-   `cut`.
-   `sort`.
-   `uniq`.
-   `grep`.
-   Expresiones regulares.
-   `tr`.
-   `sed`.
-   `awk`.
-   Condiciones multicolumna.
-   Aritmética sobre coordenadas.
-   Formateo de salidas.

### Reproducibilidad y buenas prácticas

-   Protocolo acumulativo.
-   Inspección antes de transformar.
-   Conteos de control.
-   Validación de patrones.
-   Trazabilidad de identificadores.
-   Normalización documentada.
-   Comparación con fuentes independientes.
-   Revisión por pares.
-   Evaluación individual.
-   Integración del procedimiento completo.

### Secuencia de sesiones

-   **S10 --- Reconocer:** anatomía de un archivo biológico y flujos de
    datos.
-   **S11 --- Localizar:** estructura tabular de la anotación.
-   **S12 --- Filtrar y contar:** primeras preguntas sobre el genoma.
-   **S13 --- Resumir y cuantificar:** inventario del genoma.
-   **S14--S15 --- Investigar:** del assembly al Estado 1 del genoma.
-   **S16 --- Revisar:** evaluación por pares y cierre del
    mini-proyecto.
-   **S17 --- Demostrar:** evaluación individual con datos nuevos.
-   **S18 --- Precisar:** patrones y expresiones regulares.
-   **S19 --- Extraer:** identificadores, encabezados y campos.
-   **S20 --- Normalizar:** preparar los datos para compararlos.
-   **S21 --- Confrontar:** validar con una fuente independiente (UniProt).
-   **S22 --- Condicionar y calcular:** preguntas complejas sobre
    columnas.
-   **S23 --- Integrar:** protocolo como cuaderno de laboratorio
    ejecutable.

### Evidencia integradora

Protocolo ejecutable que reconstruye el análisis del genoma y genera
resultados trazables a partir de los archivos fuente.

------------------------------------------------------------------------

## Unidad 5. Automatización de análisis bioinformáticos con Shell

**Sesiones:** S24--S29

### Propósito

Transformar un procedimiento ya validado en una herramienta
reutilizable, verificable y capaz de procesar múltiples archivos y
ejecutarse en infraestructura de cómputo científico.

### Biología

Los análisis de genomas desarrollados en U4 se convierten en el caso de
uso para automatización. La pregunta biológica permanece mientras cambia
la forma de ejecutar el análisis.

### Cómputo

-   Scripts.
-   *Shebang*.
-   Permisos.
-   Variables.
-   Expansión.
-   Parámetros.
-   Validación.
-   Ciclos `for`.
-   Procesamiento por lotes.
-   Nombres de salida.
-   Reportes.
-   Mensajes de error.
-   README.
-   Pruebas.
-   Cluster.
-   SGE.
-   `qsub`.
-   `qstat`.
-   `qdel`.

### Reproducibilidad y buenas prácticas

-   Automatizar únicamente procedimientos previamente validados.
-   Separar datos y lógica.
-   Parametrizar.
-   Validar entradas.
-   No sobrescribir datos fuente.
-   Documentar el contrato de uso.
-   Probar con datos nuevos.
-   Revisión por pares.
-   Defensa de decisiones.
-   Verificar equivalencia entre ejecución local y remota.

### Sesiones

-   **S24 --- Guardar:** del protocolo ejecutable al script.
-   **S25 --- Parametrizar:** separar el procedimiento de sus datos.
-   **S26 --- Iterar:** de un genoma a una colección.
-   **S27 --- Entregar:** de script funcional a herramienta científica.
-   **S28 --- Defender:** demostrar que la herramienta es reproducible.
-   **S29 --- Escalar:** la misma herramienta en otra infraestructura.

### Evidencia integradora

Herramienta bioinformática reutilizable con parámetros, validaciones,
documentación, pruebas, reporte y evidencia de ejecución reproducible.

------------------------------------------------------------------------

## Unidad 6. Comparación de secuencias y construcción de hipótesis biológicas

**Sesiones:** S30--S34

### Propósito

Interpretar comparaciones y búsquedas de similitud para construir
hipótesis biológicas defendibles, distinguiendo con precisión
observaciones computacionales de inferencias evolutivas.

### Biología

-   Secuencias de nucleótidos.
-   Secuencias de proteínas.
-   Correspondencia entre posiciones.
-   Identidad.
-   Similitud.
-   Cobertura.
-   Sustituciones.
-   Inserciones/deleciones.
-   Homología.
-   Especiación.
-   Duplicación.
-   Ortología.
-   Paralogía.
-   Xenología.
-   Función.
-   Hipótesis biológica.

### Cómputo

-   Alineamientos.
-   Herramientas de comparación.
-   BLAST.
-   `makeblastdb`.
-   `blastn`.
-   `blastp`.
-   Bases locales.
-   Parámetros.
-   Salida tabular.
-   E-value.
-   Bit score.
-   HSP.
-   Ranking de candidatos.

### Reproducibilidad y buenas prácticas

-   Documentar consulta, base y parámetros.
-   Conservar resultados.
-   No elegir candidatos con una sola métrica.
-   Separar observación de inferencia.
-   Explicitar alternativas.
-   Declarar límites.
-   Indicar evidencia adicional necesaria.
-   Contrastar interpretaciones generadas por IA.

### Secuencia conceptual

``` text
S30 Comparar
→ S31 Buscar
→ S32 Interpretar
→ S33 Inferir
→ S34 Integrar
```

### Sesiones

-   **S30 --- Comparar:** una secuencia adquiere significado en
    contexto.
-   **S31 --- Buscar:** comparar una secuencia contra una colección.
-   **S32 --- Interpretar:** una lista de hits no es una conclusión.
-   **S33 --- Inferir:** cuando la similitud no basta.
-   **S34 --- Integrar:** de la evidencia a la hipótesis biológica.

### Evidencia integradora

Informe de investigación sobre una secuencia desconocida que documenta
estrategia, búsqueda, evidencia, interpretación, hipótesis,
alternativas, limitaciones y validación crítica.

------------------------------------------------------------------------

# 7. Mapa integrado de contenidos

  ----------------------------------------------------------------------------------
  Unidad         Biología         Cómputo         Reproducibilidad y Capacidad
                                                  buenas prácticas   central
  -------------- ---------------- --------------- ------------------ ---------------
  **U1**         Pregunta,        Markdown;       FAIR, metadatos,   **Documentar y
                 evidencia, datos organización    protocolo,         organizar**
                 e interpretación digital; IA     bitácora           

  **U2**         Datos biológicos Unix, shell,    Estructura del     **Operar el
                 como objetos de  archivos, SSH,  proyecto,          entorno**
                 trabajo          transferencia   integridad,        
                                                  registro           

  **U3**         DNA, RNA,        Bases de datos, Procedencia,       **Comprender y
                 proteínas,       descarga,       versiones,         recuperar
                 genes, genomas,  inspección y    integridad,        datos**
                 anotación,       transferencia   `data/source/`     
                 FASTA, GFF3,                                        
                 GenBank                                             

  **U4**         Features, genes, Pipes, grep,    Controles,         **Analizar y
                 CDS,             regex, cut,     normalización,     confrontar**
                 coordenadas,     sort, uniq, tr, contraste,         
                 cadenas,         sed, awk        revisión,          
                 replicones,                      protocolo          
                 longitudes,                      ejecutable         
                 densidad                                            

  **U5**         Análisis         Shell           Validación,        **Automatizar y
                 genómico como    scripting,      pruebas,           escalar**
                 caso de          variables,      documentación,     
                 automatización   parámetros,     reutilización      
                                  ciclos, HPC/SGE                    

  **U6**         Alineamiento,    BLAST,          Parámetros,        **Interpretar e
                 similitud,       métricas,       ranking de         inferir**
                 homología,       bases, salida   evidencia,         
                 ortología,       tabular         límites,           
                 paralogía,                       validación         
                 xenología                                           
  ----------------------------------------------------------------------------------

------------------------------------------------------------------------

# 8. Competencias

## A. Trabajo reproducible y comunicación científica

-   Documentar reportes y protocolos en Markdown.
-   Aplicar principios FAIR.
-   Crear y utilizar metadatos.
-   Organizar proyectos bioinformáticos reproducibles.
-   Comunicar decisiones, resultados y limitaciones.

## B. Entorno Unix y cómputo científico

-   Operar la línea de comandos.
-   Gestionar archivos, directorios, permisos y procesos.
-   Trabajar en servidores remotos.
-   Transferir datos verificando integridad.
-   Utilizar un cluster a nivel usuario.

## C. Datos y bases de datos biológicas

-   Recuperar secuencias y genomas.
-   Interpretar formatos biológicos.
-   Comprender registros, identificadores, versiones y anotaciones.
-   Documentar procedencia.

## D. Análisis y exploración de datos genómicos

-   Procesar archivos mediante tuberías y herramientas Unix.
-   Buscar y filtrar mediante patrones.
-   Transformar representaciones.
-   Realizar cálculos y resúmenes.
-   Interpretar resultados en contexto biológico.

## E. Automatización y programación en Shell

-   Escribir scripts reutilizables.
-   Parametrizar.
-   Validar entradas.
-   Procesar colecciones.
-   Generar reportes.
-   Probar y documentar herramientas.

## F. Comparación de secuencias y homología

-   Interpretar alineamientos.
-   Ejecutar e interpretar BLAST.
-   Integrar métricas de similitud.
-   Distinguir similitud de homología.
-   Razonar sobre relaciones evolutivas.

## G. Uso responsable de inteligencia artificial

-   Formular prompts científicos.
-   Verificar respuestas.
-   Detectar alucinaciones.
-   Documentar uso relevante.
-   Utilizar IA sin sustituir el razonamiento científico.

------------------------------------------------------------------------

# 9. Metodología de enseñanza

El curso utiliza un modelo de **aula invertida con aprendizaje basado en
problemas**.

Antes de la clase, el estudiante revisa el material indispensable y
realiza un primer intento de las actividades previstas.

Durante el taller:

-   predice;
-   ejecuta;
-   observa;
-   compara;
-   diagnostica;
-   corrige;
-   discute;
-   interpreta;
-   documenta.

Después del taller, consolida la evidencia y actualiza los productos
acumulativos.

Las prácticas se intercalan con los conceptos que las hacen posibles.
Las herramientas nuevas se introducen cuando la estrategia anterior
alcanza una limitación reconocible.

------------------------------------------------------------------------

# 10. Evidencias y evaluación

La evaluación se basa en **desempeños demostrables**.

Entre las evidencias se incluyen:

-   protocolo reproducible;
-   reportes en Markdown;
-   metadatos;
-   diccionario de variables;
-   bitácora de IA;
-   estructura del proyecto;
-   transferencia verificable;
-   análisis de archivos biológicos;
-   inventarios y resúmenes genómicos;
-   mini-proyecto;
-   revisión por pares;
-   evaluación individual demostrativa;
-   protocolo ejecutable;
-   scripts;
-   documentación de software;
-   procesamiento por lotes;
-   proyecto integrador de automatización;
-   trabajo en cluster;
-   interpretación de alineamientos;
-   búsqueda BLAST documentada;
-   ranking argumentado de candidatos;
-   hipótesis de homología;
-   informe final sobre una secuencia desconocida.

La evaluación debe comprobar no solo que el estudiante obtiene una
salida, sino que puede explicar:

``` text
qué hizo
+ por qué lo hizo
+ qué obtuvo
+ cómo lo verificó
+ qué significa
+ qué límites tiene
```

------------------------------------------------------------------------

# 11. Productos acumulativos del curso

## `protocolo.md`

Cuaderno de laboratorio computacional que registra la investigación.

## `doc/bitacora-ia.md`

Registro de consultas relevantes a asistentes de IA y de su validación.

## `data/source/`

Datos originales y metadatos.

## `data/processed/`

Datos transformados de manera trazable.

## `results/`

Resultados derivados.

## `src/`

Scripts y herramientas desarrolladas durante la automatización.

La cadena completa debe permitir reconstruir:

``` text
fuente
→ dato original
→ transformación
→ análisis
→ resultado
→ verificación
→ interpretación
→ conclusión
```

------------------------------------------------------------------------

# 12. Uso de inteligencia artificial

La IA se integra de manera transversal y progresiva.

### Inicio

-   qué es un asistente generativo;
-   cómo formular un prompt;
-   qué es una alucinación;
-   por qué verificar;
-   pautas de uso ético.

### Durante el curso

La IA puede utilizarse para:

-   explicar un concepto;
-   proponer una alternativa;
-   revisar un comando;
-   diagnosticar un error;
-   comentar un script;
-   comparar estrategias;
-   cuestionar una interpretación.

Siempre después de que el estudiante disponga de una línea base propia
cuando la actividad evalúe una competencia que debe desarrollar.

### Cierre

El estudiante debe ser capaz de evaluar críticamente una interpretación
asistida por IA y distinguir entre:

-   una respuesta plausible;
-   una respuesta técnicamente correcta;
-   una respuesta reproducible;
-   una conclusión biológicamente sustentada.

------------------------------------------------------------------------

# 13. Perfil de egreso del curso

Al finalizar, el estudiante podrá abordar un problema bioinformático
introductorio siguiendo un procedimiento como:

``` text
1. Formular la pregunta.
2. Identificar la evidencia necesaria.
3. Localizar y recuperar los datos.
4. Documentar su procedencia.
5. Verificar su integridad.
6. Inspeccionar su estructura.
7. Diseñar el análisis.
8. Ejecutarlo mediante herramientas Unix.
9. Verificar los resultados.
10. Contrastar cuando sea posible.
11. Automatizar procedimientos repetitivos.
12. Documentar y probar la herramienta.
13. Interpretar resultados computacionales.
14. Construir una conclusión biológica.
15. Declarar incertidumbre y limitaciones.
16. Registrar el procedimiento para que pueda repetirse.
```

El estudiante habrá desarrollado una base para utilizar herramientas
computacionales sin perder de vista que el objetivo de la bioinformática
es **convertir datos biológicos en evidencia interpretable**.

------------------------------------------------------------------------

# 14. Continuidad curricular

El curso prepara al estudiante para asignaturas posteriores de
programación, algoritmos, bioinformática, estadística y análisis de
datos.

La progresión curricular buscada es:

``` text
Introducción a la Bioinformática
        │
        ├── datos biológicos
        ├── Unix/Linux
        ├── reproducibilidad
        ├── scripting
        ├── comparación de secuencias
        └── razonamiento crítico
                ↓
Programación y algoritmos
                ↓
Análisis bioinformáticos más complejos
                ↓
Investigación reproducible
```

El propósito de este primer curso es que el estudiante no llegue a las
materias posteriores únicamente con experiencia de sintaxis, sino con
una **forma de trabajo científico-computacional**: preguntar, obtener
evidencia, analizar, verificar, interpretar, documentar y reconocer los
límites de sus conclusiones.
