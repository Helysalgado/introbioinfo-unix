# Unidad 2. El entorno Unix/Linux y el cómputo científico

> **NOTA — Cómo se estudia esta unidad (aula invertida).** La Unidad 2 se divide en **tres
> módulos**, uno por cada sesión presencial de dos horas (S3 a S5). Cada módulo tiene su propio
> documento de **lectura previa**: lo lees y haces un **primer intento** *antes* de clase, practicas y
> corriges *durante* el taller, y *después* entregas la evidencia corregida. Esta portada solo te da
> la **visión de conjunto** y los enlaces; el contenido y las prácticas viven en cada módulo.

Esta unidad es tu primer contacto con el **entorno de trabajo real del bioinformático**: la línea de
comandos de Unix/Linux y un servidor remoto al que te conectas por red. Todo lo que aprendas aquí es
la base sobre la que se construyen las unidades siguientes: obtención de datos, procesamiento,
automatización, comparación de secuencias y, más adelante, uso del cluster institucional.

## Ficha de la unidad

| Elemento | Descripción |
| --- | --- |
| **Sesiones** | S3–S5 (tres sesiones de 2 h) |
| **Competencia** | B — Dominio del entorno Unix y del cómputo científico |
| **Propósito** | Que el estudiante opere con soltura el entorno Unix/Linux, desde su propia máquina hasta un servidor remoto compartido. |
| **Contribución al objetivo del curso** | Aporta el entorno computacional donde ocurrirá el trabajo posterior: conectarse, transferir datos, organizar archivos, gestionar permisos y controlar procesos propios. |
| **Progresión acordada** | El uso operativo del cluster se retoma después de practicar procesamiento de datos y scripting, cuando exista un análisis bioinformático que justifique el planificador. |
| **Lectura base** | Buffalo (2015), Cap. 3 ("Remedial Unix Shell"); Shotts (2019), *The Linux Command Line* (consulta por temas). |
| **Infraestructura del curso** | Servidor institucional (la dirección, tu usuario y tu contraseña se dan **en clase**) y el proyecto de trabajo bajo `~/proyecto/`. |

## Resultados de aprendizaje generales de la unidad

Al terminar la Unidad 2, el estudiante es capaz de:

1. **Explicar** por qué se usa Unix en bioinformática y **conectarse** a un servidor remoto por SSH,
   **transfiriendo** archivos entre su computadora y el servidor con verificación de integridad (S3).
2. **Navegar** el sistema de archivos con rutas absolutas y relativas y **operar** con archivos y
   directorios para construir la estructura canónica del proyecto (S4).
3. **Visualizar, editar y comprimir** archivos, y **gestionar** permisos y procesos en el servidor
   (S5).
Cada módulo desglosa estos resultados en objetivos demostrables por sesión, con su práctica, su
evidencia y su criterio de logro.

> **ALCANCE DEL CURSO:** La competencia de usar un cluster a nivel usuario se conserva en el curso,
> pero ya no se introduce ni se evalúa en esta unidad. Se retomará después de que el alumnado haya
> procesado datos biológicos, construido tuberías y trabajado con scripts; así podrá relacionar el
> planificador con una necesidad computacional observable.

## Ruta de aprendizaje S3–S5

La unidad avanza desde reconocer la terminal y conectarse a un servidor hasta organizar archivos,
administrar permisos y controlar procesos propios. Cada módulo supone que ya dominas el anterior.

| Momento | Módulo | Qué haces antes de clase | Qué se hace en el taller | Qué entregas después |
| --- | --- | --- | --- | --- |
| **S3** | [Shell, SSH y transferencia](u2-s3-shell-acceso-remoto.md) | Lees el módulo; preparas el *preflight*; primer intento de conexión | Conexión guiada, transferencia y verificación de integridad | Registro reproducible de una transferencia verificada |
| **S4** | [Sistema de archivos](u2-s4-sistema-archivos-v3.md) | Lees el módulo; primer intento de la estructura del proyecto | Navegación y operaciones en vivo; comparación con IA | **Tarea 3**: estructura del proyecto en el servidor |
| **S5** | [Archivos, permisos y procesos](u2-s5-archivos-permisos-procesos-v2.md) | Lees el módulo; primer intento con un archivo y un proceso | Visualización, compresión, permisos y control de procesos | Archivo restaurado + script ejecutable + registro de un proceso |

> **NOTA:** Los tiempos son estimaciones. Cada módulo indica su carga por momento (lectura, primer
> intento y práctica). Reserva alrededor de **2–2.5 h** de trabajo autónomo por sesión, además de las
> 2 h presenciales.

## Evidencias acumuladas de la unidad

La Unidad 2 no se evalúa con un solo entregable, sino con **evidencias que se acumulan** módulo a
módulo. Al cerrar la unidad debes tener:

- **S3 —** un registro reproducible de una transferencia de archivos cuya integridad comprobaste con
  *checksums* (host, rutas, comandos y resultados, sin credenciales).
- **S4 — Tarea 3:** la estructura canónica del proyecto creada en tu espacio del servidor, verificada
  con `tree` o `ls -R` y documentada.
- **S5 —** un archivo comprimido y restaurado correctamente, un *script* mínimo hecho ejecutable y el
  registro del control de un proceso.
> **IMPORTANTE — dónde viven tus datos.** En todos los módulos usamos la **misma estructura de
> proyecto** de la Unidad 1. Los datos originales se conservan en `data/source/` **sin modificarse**;
> cualquier transformación genera archivos nuevos fuera de esa carpeta (Noble, 2009).

```text
proyecto/
├── data/
│   ├── source/      # datos originales, inmutables
│   └── processed/   # datos derivados
├── src/             # scripts
├── results/         # resultados del análisis
└── doc/             # documentación (protocolo, bitácora, README)
```

## Cómo S3–S5 cubren la competencia B

La siguiente tabla acumulativa muestra cómo los tres módulos demuestran los resultados de la
**Competencia B** correspondientes al cierre actual de la Unidad 2.

| Resultado de la competencia B (Programa) | Módulo(s) | Práctica / evidencia en la unidad | Evidencia del Programa |
| --- | --- | --- | --- |
| Operar la línea de comandos: navegar el sistema de archivos, gestionar archivos y directorios, permisos y procesos | S4, S5 | Estructura del proyecto (Tarea 3); control de archivos, permisos y procesos | Examen práctico 1; tareas de shell |
| Conectarse a servidores remotos por SSH y transferir datos (sftp, scp, rsync) verificando integridad | S3 | Registro reproducible de transferencia verificada con *checksums* | Tarea de transferencia de archivos |
> **NOTA:** El **Examen práctico 1** (S16 del plan) evalúa de forma integrada el entorno Unix, los
> datos y los filtros. La Unidad 2 prepara la parte de entorno; no se examina dentro de la unidad.

## Índice de módulos

1. **[S3 — Shell, SSH y transferencia](u2-s3-shell-acceso-remoto.md).** Por qué Unix, GUI frente a
   CLI, filosofía Unix, terminal y shell, anatomía de un comando y ayuda; cliente/servidor y
   protocolos; conexión por SSH; transferencia con SFTP, FileZilla, `scp` y `rsync`; verificación de
   integridad.
2. **[S4 — Sistema de archivos](u2-s4-sistema-archivos-v3.md).** Raíz, home y directorio actual; rutas
   absolutas y relativas; `.`, `..`, `~`; navegación y operaciones (`pwd`, `ls`, `cd`, `mkdir`,
   `touch`, `cp`, `mv`), eliminación segura y visualización del árbol.
3. **[S5 — Archivos, permisos y procesos](u2-s5-archivos-permisos-procesos-v2.md).** Tipos de archivo,
   visualización, edición con `nano`, compresión; lectura de permisos y `chmod`; procesos, primer y
   segundo plano, y su control.
## Cierre de la Unidad 2

Al concluir S5, verifica que puedes demostrar lo siguiente con evidencia propia:

- reconocer si trabajas en tu computadora o en el servidor y conectarte de forma segura;
- transferir archivos y comprobar su integridad;
- navegar mediante rutas absolutas y relativas y explicar dónde está cada archivo del proyecto;
- preservar los originales en `data/source/` y trabajar sobre copias o productos derivados;
- inspeccionar y comprimir archivos, interpretar permisos y aplicar el cambio mínimo necesario;
- distinguir archivo, programa, proceso, PID y trabajo del shell;
- controlar únicamente un proceso propio y comprobar que terminó;
- documentar comandos, resultados, errores y verificaciones en `doc/protocolo.md`.

Este cierre no exige utilizar un cluster. El producto acumulado de S3–S5 es un proyecto organizado
y verificable en el servidor, preparado para recibir datos biológicos reales.

## Puente hacia la Unidad 3 — Datos y bases de datos biológicas

Hasta ahora aprendiste **dónde y cómo trabajar**. La Unidad 3 cambia el foco hacia **qué datos
biológicos obtendrás y cómo comprobarás que son confiables**. De acuerdo con el Plan y el Programa,
el siguiente recorrido aborda:

1. dogma central y representación de información biológica;
2. formatos FASTA, GenBank y GFF3;
3. registros, identificadores y anotaciones en bases de datos;
4. exploración de NCBI, Genomes y PubMed;
5. descarga de secuencias o genomas y verificación de integridad;
6. incorporación documentada de los datos al proyecto, conservando su procedencia y sus metadatos.

Las habilidades de la Unidad 2 siguen activas: usarás SSH, rutas, `data/source/`, herramientas de
inspección y checksums para obtener y resguardar los datos de la Unidad 3.

## Lecturas / consulta previa para la Unidad 3

- Buffalo (2015), Cap. 6 ("Bioinformatics Data"): obtención de datos y su descarga reproducible.
- Explorar el sitio de NCBI (<https://www.ncbi.nlm.nih.gov>).

## Referencias de la unidad

Las referencias completas se listan al final de cada módulo. Fuentes transversales de la Unidad 2:

- Buffalo, V. (2015). *Bioinformatics Data Skills*. O'Reilly Media. — Cap. 3 ("Remedial Unix Shell")
  y Cap. 6 (datos bioinformáticos). Disponible en `referencias/bioinformatics-data-skills.pdf`.
- Shotts, W. E. (2019). *The Linux Command Line: A Complete Introduction* (2ª ed.). No Starch Press.
- Noble, W. S. (2009). A Quick Guide to Organizing Computational Biology Projects. *PLoS
  Computational Biology*, 5(7), e1000424. doi:10.1371/journal.pcbi.1000424.
- Ritchie, D. M., & Thompson, K. (1974). The UNIX Time-Sharing System. *Communications of the ACM*,
  17(7), 365–375. doi:10.1145/361011.361061.
