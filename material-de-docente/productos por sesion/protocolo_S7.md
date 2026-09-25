# Protocolo del proyecto --- E. coli K-12

> **Estado al cierre de S7:** se conserva la pregunta biológica y la
> evidencia construida hasta S6. En S7 se determina qué objetos,
> evidencias y datos son necesarios para responder las subpreguntas, se
> distingue secuencia de anotación y se realiza una **selección
> provisional del conjunto de datos**. Todavía no se descarga el nuevo
> conjunto de datos ni se inicia el análisis biológico.

## Introducción

Este proyecto utilizará información genómica de *Escherichia coli* K-12
para practicar un flujo de trabajo bioinformático reproducible. El
objetivo no es comenzar por una herramienta, sino definir primero la
pregunta biológica, dividirla en subpreguntas y establecer qué evidencia
permitiría responderlas.

El protocolo es un documento vivo: se completará durante el curso
conforme se incorporen los datos, los comandos, las verificaciones, los
resultados y su interpretación.

## Pregunta central

**¿Cuántos genes tiene el genoma de *E. coli* K-12 y cómo se distribuyen
en el cromosoma?**

## Subpreguntas

1.  ¿Cuál es el tamaño del genoma de *E. coli* K-12?
2.  ¿Cuántos genes están anotados en el genoma?
3.  ¿Cuántos genes se encuentran en la hebra `+` y cuántos en la hebra
    `-`?

## Datos

### Archivo principal

-   **Archivo:** `genes_ecoli.gff`
-   **Organismo:** *Escherichia coli* K-12 MG1655
-   **Referencia:** `NC_000913.3`
-   **Formato:** GFF
-   **Función en el proyecto:** archivo de anotación genómica utilizado
    como dato fuente.
-   **Metadatos asociados:** `genes_ecoli-metadatos.md`
-   **Integridad:** el campo de checksum queda reservado hasta
    calcularlo en una sesión posterior.

La ficha `genes_ecoli-metadatos.md` registra la procedencia y el
contexto del dato. La información que no esté comprobada debe quedar
marcada como pendiente, no inferirse ni inventarse.

### Política de organización de datos

-   Los datos originales se conservarán sin modificaciones en
    `data/source/`.
-   Los archivos transformados o derivados se guardarán en
    `data/processed/`.
-   Los resultados regenerables se almacenarán en `results/`.
-   Los scripts se almacenarán en `src/`.
-   La documentación del proyecto se almacenará en `doc/`.

Estas decisiones contribuyen a la localización, trazabilidad y
reutilización del trabajo; FAIR se aplica de forma progresiva y no se
considera resuelto únicamente por crear carpetas o una ficha de
metadatos.

### Ubicación de los datos fuente

``` text
~/proyecto-ecoli/data/source/
├── genes_ecoli.gff
└── genes_ecoli-metadatos.md
```

Los archivos de `data/source/` se consideran datos originales del
proyecto y no deben editarse directamente. Los derivados futuros se
almacenarán en `data/processed/`.

## Estrategia

| Subpregunta | Evidencia necesaria | Datos | Operación conceptual | Validación prevista |
|---|---|---|---|---|
| ¿Cuál es el tamaño del genoma? | Longitud total del genoma | `genes_ecoli.gff` / registro asociado | Localizar la longitud declarada | Contrastar con el registro de referencia |
| ¿Cuántos genes hay? | Número de registros `gene` | `genes_ecoli.gff` | Filtrar conceptualmente por tipo `gene` y contar | Comparar con referencia externa |
| ¿Cuántos genes hay por hebra? | Conteos `+` y `-` para genes | `genes_ecoli.gff` | Agrupar conceptualmente por hebra y contar | `+` + `-` = total de genes |

         
  ----------------------------------------------------------------------------------

## Comandos y procedimiento

### Sesión 3 --- Transferencia y verificación

### 1. Acceso al servidor

**Contexto: LOCAL**

``` bash
ssh [USUARIO]@[SERVIDOR]
```

**Contexto: REMOTO**

``` bash
hostname
whoami
pwd
exit
```

No se registran contraseñas, llaves privadas ni credenciales en el
protocolo.

### 2. Transferencia de datos y metadatos

**Contexto: LOCAL → SFTP**

``` bash
sftp [USUARIO]@[SERVIDOR]
lpwd
pwd
put genes_ecoli.gff
put genes_ecoli-metadatos.md
exit
```

También se transfiere via Filezilla, pero no es automatizable.

### 3. Comprobación de presencia

**Contexto: REMOTO**

``` bash
ssh [USUARIO]@[SERVIDOR]
ls -lh genes_ecoli.gff genes_ecoli-metadatos.md
```

### 4. Comprobación de integridad

**Contexto: LOCAL**

``` bash
sha256sum genes_ecoli.gff
sha256sum genes_ecoli-metadatos.md
```

> En macOS puede utilizarse `shasum -a 256`.

**Contexto: REMOTO**

``` bash
sha256sum genes_ecoli.gff
sha256sum genes_ecoli-metadatos.md
```

### Registro de checksums

  ----------------------------------------------------------------------------------
  Archivo                      SHA-256 local     SHA-256 remoto    Estado
  ---------------------------- ----------------- ----------------- -----------------
  `genes_ecoli.gff`            `[REGISTRAR]`     `[REGISTRAR]`     Deben coincidir

  `genes_ecoli-metadatos.md`   `[REGISTRAR]`     `[REGISTRAR]`     Deben coincidir
  ----------------------------------------------------------------------------------

### Sesión 4 --- Organización del proyecto

### 1. Confirmar contexto

``` bash
hostname
whoami
cd ~
pwd
ls -lah
```

### 2. Crear y verificar la estructura

``` bash
mkdir proyecto-ecoli
cd proyecto-ecoli
pwd
mkdir -p data/source data/processed
mkdir src results doc
touch README.md
tree
```

Si `tree` no está disponible:

``` bash
ls -R
```

### 3. Copiar datos fuente

Desde `~/proyecto-ecoli`:

``` bash
cp -i ~/genes_ecoli.gff data/source/
cp -i ~/genes_ecoli-metadatos.md data/source/
ls -lh data/source/
```

Se usa copia antes de mover para conservar un punto de regreso hasta
verificar.

### 4. Colocar documentación

``` bash
mv -i ~/protocolo.md doc/
```

La bitácora de IA, si permanece en el equipo local, se transfiere al
servidor y se verifica en `doc/`.

### 5. Verificar integridad del GFF

``` bash
sha256sum data/source/genes_ecoli.gff
```

La suma debe coincidir con la registrada para el archivo fuente en S3.

### Sesión 6 --- Consolidación del entorno Unix

### 1. Verificar acceso y contexto

``` bash
hostname
whoami
pwd
cd ~/proyecto-ecoli
pwd
```

**Ruta absoluta observada:** `[REGISTRAR SALIDA DE pwd]`

### 2. Verificar estructura real

``` bash
ls -R ~/proyecto-ecoli
```

Para cada elemento adicional creado en S5 se toma una decisión
explícita: conservar, mover o eliminar, con justificación. No se elimina
nada de `data/source/`.

### 3. Verificar continuidad de la integridad de los originales

Primero se calculan nuevamente las sumas SHA-256 de los archivos que
actualmente se encuentran en `data/source/`:

``` bash
cd ~/proyecto-ecoli/data/source
sha256sum genes_ecoli.gff
sha256sum genes_ecoli-metadatos.md
```

Los valores obtenidos en S6 deben compararse con los **checksums de
referencia registrados en S3**.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Archivo                      SHA-256 de referencia (S3)                                         SHA-256 actual (S6)                                                Estado
  ---------------------------- ------------------------------------------------------------------ ------------------------------------------------------------------ -----------------
  `genes_ecoli.gff`            af8609c2ff73e4e23f2007b4938470d350fe8ee75dba832f908992855767fac8   af8609c2ff73e4e23f2007b4938470d350fe8ee75dba832f908992855767fac8   `COINCIDE`

  `genes_ecoli-metadatos.md`   609aa3ec9db616ee243328d15833eeb59f83d9cb8a94b7e0f01e1c252cd0ca95   609aa3ec9db616ee243328d15833eeb59f83d9cb8a94b7e0f01e1c252cd0ca95   `COINCIDE`
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

La coincidencia entre S3 y S6 aporta evidencia de que el contenido de
los archivos fuente se ha conservado desde la transferencia inicial.

#### Archivo de checksums para verificaciones posteriores

Una vez comprobada la coincidencia con los valores de referencia de S3,
puede generarse un archivo de sumas para facilitar verificaciones
posteriores:

``` bash
cd ~/proyecto-ecoli/data/source
sha256sum genes_ecoli.gff genes_ecoli-metadatos.md > ../../doc/checksums-u2.txt
sha256sum -c ../../doc/checksums-u2.txt
```

**Salida esperada:**

``` text
genes_ecoli.gff: OK
genes_ecoli-metadatos.md: OK
```

> **Importante:** obtener `OK` inmediatamente después de crear
> `checksums-u2.txt` demuestra que los archivos actuales coinciden con
> las sumas recién registradas. La evidencia de continuidad desde S3
> proviene de comparar previamente los checksums actuales con los
> valores de referencia de S3.

### 4. Verificar permisos

``` bash
ls -l ~/proyecto-ecoli/data/source/
ls -l ~/proyecto-ecoli/src/
```

Criterios:

-   Datos fuente: lectura; sin permiso de ejecución.
-   Documentación: lectura y escritura para el dueño según necesidad.
-   Scripts: ejecución únicamente cuando el script deba ejecutarse.

Cualquier corrección con `chmod` debe documentar archivo, permiso
modificado y justificación.

### 5. Verificar reproducibilidad del protocolo

El protocolo se revisa por pares. La persona revisora debe poder
identificar:

-   dónde se ejecuta cada comando;
-   de dónde proviene cada archivo o valor;
-   qué evidencia produce cada procedimiento;
-   por qué se tomó cada decisión;
-   qué información permanece pendiente o limitada.

No deben existir credenciales ni información sensible en el documento.

### Sesión 7 --- Representar: de los objetos biológicos a FASTA, GFF3 y GenBank

S7 no comienza preguntando qué comando utilizar. El razonamiento de la
sesión es:

``` text
¿Qué quiero saber?
        ↓
¿Qué evidencia necesito?
        ↓
¿Qué dato representa esa evidencia?
        ↓
¿En qué formato está representado?
        ↓
¿Qué operación necesito?
        ↓
¿Qué herramienta puedo utilizar?
```

#### Distinciones conceptuales

Antes de seleccionar los datos se distingue entre:

-   **Objeto biológico:** entidad que se estudia, por ejemplo genoma o
    gen.
-   **Registro:** representación estructurada de información sobre un
    objeto o característica biológica.
-   **Archivo:** contenedor concreto de secuencias o registros.
-   **Formato:** reglas que determinan cómo se representa y organiza la
    información.

También se distingue entre:

-   **Secuencia:** qué nucleótidos o aminoácidos hay.
-   **Anotación:** qué objetos o características biológicas se reconocen
    sobre una secuencia y dónde se localizan.

Por tanto, disponer de la secuencia del genoma no implica disponer
explícitamente de la anotación de sus genes.

#### Formatos considerados

  -----------------------------------------------------------------------
  Formato                 Qué representa          Información relevante
                          principalmente          para este proyecto
  ----------------------- ----------------------- -----------------------
  FASTA                   Secuencia               Secuencia genómica;
                                                  permite obtener su
                                                  longitud a partir de la
                                                  secuencia

  GFF3                    Anotaciones asociadas a Tipo de feature,
                          una secuencia           coordenadas, hebra y
                                                  atributos

  GenBank                 Registro integrado con  Permite consultar
                          secuencia, anotaciones  conjuntamente secuencia
                          y metadatos             y features anotadas
  -----------------------------------------------------------------------

> Un formato no se selecciona porque sea "mejor" en general. Se
> selecciona porque representa los datos necesarios para obtener una
> evidencia concreta.

#### Matriz objeto--evidencia--formato corregida

  --------------------------------------------------------------------------------------
  Subpregunta   Evidencia      Objeto      Datos que deben     Formato     Falta
                necesaria                  estar representados candidato   confirmar
  ------------- -------------- ----------- ------------------- ----------- -------------
  ¿Cuál es el   Longitud total Genoma /    Secuencia de        FASTA o     Referencia y
  tamaño del    de la          cromosoma   nucleótidos         GenBank     versión
  genoma?       secuencia                                                  exactas
                genómica                                                   

  ¿Cuántos      Número de      Gen anotado Tipo de feature,    GFF3 o      Qué registros
  genes están   features que               coordenadas y       GenBank     se contarán
  anotados?     correspondan a             atributos                       exactamente
                genes según el                                             como `gene`
                criterio                                                   
                definido                                                   

  ¿Cuántos      Genes anotados Gen anotado Tipo de feature y   GFF3 o      Criterio de
  genes hay en  clasificados               hebra/orientación   GenBank     conteo y
  la hebra `+`  por hebra                                                  valores de
  y cuántos en                                                             hebra
  `-`?                                                                     
  --------------------------------------------------------------------------------------

La matriz **no debe interpretarse como una correspondencia rígida "una
pregunta = un formato"**. Por ejemplo, un registro GenBank puede
contener tanto secuencia como anotaciones.

#### Selección provisional del conjunto de datos

Para continuar el proyecto se requieren datos que correspondan al mismo
organismo, cepa y referencia genómica, y que permitan disponer de:

-   la **secuencia genómica**;
-   la **anotación genómica**;
-   metadatos suficientes para identificar la procedencia y versión de
    los datos.

**Organismo:** *Escherichia coli* K-12 MG1655\
**Referencia a verificar al seleccionar la descarga:** `NC_000913.3`

La fuente, los archivos concretos, la versión y la correspondencia entre
secuencia y anotación se verificarán antes de la descarga en S8.

> **FAIR / buena práctica en contexto:** registrar organismo, cepa,
> identificador de referencia, versión y procedencia favorece la
> identificación, trazabilidad y reutilización. Utilizar formatos
> estandarizados favorece la interoperabilidad, pero por sí solo no hace
> que un conjunto de datos sea FAIR.

> **Buena práctica:** antes de combinar secuencia y anotación debe
> comprobarse que ambas correspondan a la misma referencia y versión.

#### Pendientes antes de S8

  -----------------------------------------------------------------------
  Verificación                        Estado al cierre de S7
  ----------------------------------- -----------------------------------
  Organismo y cepa identificados      *E. coli* K-12 MG1655

  Referencia de trabajo identificada  `NC_000913.3` --- verificar en la
                                      fuente

  Evidencia necesaria para cada       Sí
  subpregunta definida                

  Información que debe aportar la     Sí
  secuencia definida                  

  Información que debe aportar la     Sí
  anotación definida                  

  Archivos concretos seleccionados y  **PENDIENTE --- S8**
  versión verificada                  

  Correspondencia                     **PENDIENTE --- S8**
  secuencia--anotación verificada     

  Procedencia de los nuevos archivos  **PENDIENTE --- S8**
  registrada                          

  Integridad de la nueva descarga     **PENDIENTE --- S8**
  verificada                          
  -----------------------------------------------------------------------

**En S7 no se descarga todavía el nuevo genoma y no se ejecutan comandos
para responder las subpreguntas biológicas.**

## Evidencia de consolidación del entorno

  -----------------------------------------------------------------------------
  Afirmación              Evidencia                  Estado
  ----------------------- -------------------------- --------------------------
  Puedo reconectar y      `hostname`, `whoami`,      `[COMPROBADO/PENDIENTE]`
  ubicarme en el servidor `pwd`                      

  El proyecto tiene una   `ls -R ~/proyecto-ecoli`   `[COMPROBADO/PENDIENTE]`
  estructura conocida                                

  Los originales          comparación de SHA-256 de  `[COMPROBADO/PENDIENTE]`
  mantienen el mismo      S3 y S6                    
  contenido desde S3                                 

  Existe un mecanismo     `doc/checksums-u2.txt` +   `[COMPROBADO/PENDIENTE]`
  para verificaciones     `sha256sum -c`             
  posteriores                                        

  Los permisos son        `ls -l` + correcciones     `[COMPROBADO/PENDIENTE]`
  justificables           documentadas               

  Otra persona puede      revisión por pares         `[COMPROBADO/PENDIENTE]`
  seguir el protocolo                                
  -----------------------------------------------------------------------------

## Resultados

**El análisis biológico continúa pendiente.**

El producto de S7 no es todavía un conteo de genes ni una medida del
tamaño del genoma. Los resultados de esta sesión son:

1.  una **matriz objeto--evidencia--formato corregida**;
2.  la distinción explícita entre **secuencia y anotación**;
3.  una **selección provisional del conjunto de datos**;
4.  una lista de verificaciones pendientes antes de descargar y analizar
    los datos.

Todavía no se reportan valores para tamaño del genoma, número de genes o
número de genes por hebra.

## Validación

Sobre los datos

> Puedo afirmar que los datos fuente conservan su integridad desde la
> transferencia inicial porque los checksums calculados en S6 coinciden
> con los valores de referencia registrados en S3. Además,
> `doc/checksums-u2.txt` permite realizar verificaciones posteriores del
> estado de estos archivos.

```{=html}
<!-- Si un checksum no coincide o `sha256sum -c` produce `FAILED`, no se interpreta automáticamente como corrupción: primero se revisan la ruta, el archivo comparado, posibles cambios accidentales y errores de transcripción o registro del checksum. -->
```
## Discusión

El cierre de U2 muestra la diferencia entre "me funcionó" y "puedo
demostrar que funciona". La organización, los metadatos, las rutas, los
checksums, los permisos y la documentación son parte del análisis
reproducible porque permiten reconstruir el estado del proyecto antes de
comenzar el análisis biológico.

## Conclusiones

El entorno Unix del proyecto está preparado para continuar con el
análisis de datos biológicos una vez que las verificaciones de acceso,
estructura, integridad, permisos y documentación estén marcadas como
comprobadas.

La pregunta biológica todavía no se ha respondido. Hasta S6 se construyó
y validó el entorno; en S7 se definió qué evidencia y qué
representaciones de datos serán necesarias.

El siguiente paso es obtener y verificar el conjunto de datos correcto.
La descarga verificable, el registro de procedencia y versión y la
comprobación de integridad corresponden a S8.

## Actualizaciones

-   **S1:** pregunta, subpreguntas y estrategia.

-   **S2:** datos, metadatos y principios de organización/FAIR.

-   **S3:** transferencia al servidor y registro de checksums de
    referencia.

-   **S4:** estructura `~/proyecto-ecoli/`, ubicación definitiva de
    archivos y verificación.

-   **S5:** práctica operativa sin alterar el protocolo científico ni
    los datos fuente.

-   **S6:** consolidación de evidencias de U2, comparación con checksums
    de referencia, creación de `doc/checksums-u2.txt`, revisión de
    permisos y revisión por pares del protocolo.

-   **S7:** distinción objeto--registro--archivo--formato y
    secuencia--anotación; matriz objeto--evidencia--formato corregida;
    selección provisional de datos y pendientes para S8.
