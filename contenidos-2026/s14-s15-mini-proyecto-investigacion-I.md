# S14–S15 — Investigar: del assembly al Estado 1 del genoma

> **NOTA — Aula invertida:** Antes de la primera sesión localizarás tu ensamblado y prepararás un
> primer intento de identificación del organismo con la evidencia que encuentres. Durante S14
> recuperarás, verificarás y analizarás los archivos oficiales. Entre sesiones consolidarás el
> **Estado 1 del genoma** en `doc/protocolo.md`. En S15 revisarás el protocolo de otro equipo y
> mejorarás el propio con la retroalimentación recibida.

## Ficha del proyecto

| Elemento | Descripción |
| --- | --- |
| **Sesiones** | S14–S15, 2 horas cada una, más trabajo autónomo |
| **Unidad** | U4. Procesamiento y exploración de datos genómicos |
| **Modalidad** | Aula invertida · trabajo colaborativo (2–3 estudiantes por equipo) |
| **Competencias** | A. Documentación reproducible; B. Entorno Unix; C. Manejo de datos biológicos; D. Análisis y exploración de datos genómicos |
| **Propósito** | Integrar todo lo aprendido de la Unidad 3 a S13 sobre un genoma **desconocido**, asignado únicamente por su *Assembly Accession* |
| **Insumo entregado** | Un identificador RefSeq por equipo. **No se entregan archivos** |
| **Evidencia** | **Estado 1 del genoma** documentado en `doc/protocolo.md`, con la evidencia que sostiene cada afirmación |
| **Producto principal** | Actualización de `doc/protocolo.md` (no se elabora un documento independiente) |
| **Preparación para** | Revisión por pares (S16) y evaluación individual (S17) |

## Contexto

Durante las primeras trece sesiones aprendiste a trabajar como bioinformático: recuperaste datos
biológicos desde bases de datos públicas, verificaste su integridad y documentaste su procedencia.
Después exploraste archivos FASTA y GFF3, comprendiste su estructura, formulaste preguntas
biológicas, seleccionaste la información relevante y construiste el primer inventario completo de un
genoma.

Hasta este momento siempre trabajaste con el **mismo organismo de referencia**. Ahora comienza una
situación diferente.

## Escenario

El Laboratorio de Genómica Computacional ha recibido **doce nuevos ensamblados completos**
provenientes de RefSeq. Antes de que estos datos puedan utilizarse en proyectos posteriores es
necesario verificar su procedencia, recuperar los archivos oficiales y construir un primer informe
técnico del genoma.

Cada equipo recibirá **únicamente un identificador de ensamblado (*Assembly Accession*)**. No
conocerán previamente:

- el organismo;
- la cepa;
- el tamaño del genoma;
- el número de replicones;
- el contenido de la anotación.

Toda esa información deberá **descubrirse mediante evidencia reproducible**. A partir de este
momento actuarán como investigadores computacionales.

## Objetivo general

Construir el **Estado 1 del genoma** de un ensamblado asignado: recuperar los datos desde NCBI,
verificar su integridad y documentar de manera reproducible las principales características
estructurales del genoma, empleando las herramientas estudiadas desde la Unidad 3 hasta la Sesión 13.

## Competencias integradas

| Competencia | Qué integra en este proyecto |
| --- | --- |
| **A. Documentación científica reproducible** | Registrar procedencia, comandos y evidencia en `doc/protocolo.md` |
| **B. Manejo del entorno Unix** | Navegación, organización de directorios, tuberías y verificación |
| **C. Recuperación y organización de datos biológicos** | Descarga desde NCBI, verificación de integridad, estructura del proyecto |
| **D. Exploración y análisis inicial de un genoma** | Inventario de replicones, *features*, categorías y fuentes de anotación |

## Productos esperados

Al finalizar, cada equipo deberá haber construido un primer informe reproducible del genoma asignado
que permita responder, **con evidencia**:

- ¿Qué organismo fue asignado?
- ¿Cuál es su ensamblado oficial?
- ¿Cómo se verificó la procedencia de los archivos?
- ¿Cuántos replicones posee?
- ¿Qué tipos de anotaciones contiene?
- ¿Qué categorías predominan?
- ¿Qué limitaciones tiene todavía el análisis?

## Organización del proyecto

Cada equipo recibirá un único identificador RefSeq. **No se entregarán archivos.** Los equipos
deberán:

1. localizar el ensamblado;
2. recuperar los archivos oficiales;
3. verificar su procedencia;
4. organizar el proyecto;
5. construir el Estado 1 del genoma.

La estructura de proyecto es la misma que se ha usado durante todo el curso:

```text
proyecto/
├── data/
│   ├── source/
│   └── processed/
├── src/
├── results/
└── doc/
```

## Ensamblados asignados

| Equipo | *Assembly Accession* |
| ---: | --- |
| 1 | `GCF_000091005.1` |
| 2 | `GCF_000009045.1` |
| 3 | `GCF_000006945.2` |
| 4 | `GCF_000195955.2` |
| 5 | `GCF_000016285.1` |
| 6 | `GCF_000006965.1` |
| 7 | `GCF_000008525.1` |
| 8 | `GCF_000006765.1` |
| 9 | `GCF_000027325.1` |
| 10 | `GCF_000009605.1` |
| 11 | `GCF_000010065.1` |
| 12 | `GCF_000012825.1` |

> **IMPORTANTE:** No intercambies ensamblados con otros equipos. Cada proyecto representa un caso de
> estudio diferente y la evidencia de un equipo no es válida para otro.

## Ruta del proyecto

| Momento | Qué hacer | Qué llevar o entregar |
| --- | --- | --- |
| **Antes de S14** | Fase I: localizar el ensamblado e identificar el organismo | Primer intento de identificación con su evidencia |
| **S14 (taller)** | Fases II y III: recuperar, verificar y describir la anatomía de los archivos | Proyecto organizado y verificación de integridad |
| **Entre S14 y S15** | Fases IV y V: construir el Estado 1 e interpretarlo | Borrador del protocolo actualizado |
| **S15 (taller)** | Revisión por pares del protocolo de otro equipo | Observaciones fundamentadas |
| **Después de S15** | Fase VI: incorporar la retroalimentación | `doc/protocolo.md` final |

## Desarrollo del proyecto

### Fase I — Descubrir el organismo

Utilizando únicamente el identificador asignado:

- localiza el ensamblado en NCBI;
- identifica el organismo;
- identifica la cepa;
- identifica la versión del ensamblado;
- registra quién realizó la anotación;
- documenta toda la evidencia.

> **Preguntas guía:** ¿Cómo sabes que localizaste el ensamblado correcto? ¿Qué evidencia respalda
> esa afirmación?

### Fase II — Recuperación y verificación

Descarga los archivos oficiales y recupera:

- FASTA genómico;
- GFF3;
- archivos de verificación necesarios.

Organiza el proyecto siguiendo la estructura utilizada durante el curso y verifica la integridad
mediante los procedimientos aprendidos en la Unidad 3.

> **Preguntas guía:** ¿Cómo demuestras que los archivos son exactamente los publicados por RefSeq?
> ¿Qué evidencia respalda esa afirmación?

### Fase III — Anatomía del genoma

Describe la estructura de los archivos recuperados:

- organización del FASTA;
- organización del GFF3;
- delimitadores;
- encabezados;
- comentarios;
- representación de valores faltantes.

### Fase IV — Construcción del Estado 1 del genoma

Aplica todas las herramientas estudiadas de S10 a S13 para responder:

- ¿Cuánto mide el genoma?
- ¿Cuántos replicones existen?
- ¿Qué tipos de *features* contiene?
- ¿Cuántas categorías distintas aparecen?
- ¿Qué categorías predominan?
- ¿Qué fuentes participaron en la anotación?

> **IMPORTANTE:** Toda afirmación debe estar respaldada por evidencia reproducible: el comando que
> la produjo y la salida que la sostiene.

### Fase V — Interpretación científica

El objetivo ya no es únicamente obtener números, sino analizar críticamente los resultados. Discute:

- categorías dominantes;
- categorías poco frecuentes;
- diferencias respecto al organismo utilizado durante las clases;
- posibles explicaciones biológicas;
- limitaciones del análisis.

Y responde:

- ¿Qué aprendiste sobre este genoma?
- ¿Qué resultados eran esperables?
- ¿Qué resultados te sorprendieron?
- ¿Qué todavía no puedes afirmar?
- ¿Qué preguntas nuevas surgieron durante el análisis?

### Fase VI — Construcción del protocolo

Toda la información obtenida deberá integrarse en el documento:

```text
doc/protocolo.md
```

> **NOTA:** No se elabora un documento independiente. El protocolo construido desde la Unidad 1
> continúa creciendo como un verdadero cuaderno de laboratorio computacional.

## Revisión por pares (S15)

Durante la segunda sesión cada equipo intercambiará su protocolo con otro equipo. La revisión **no**
tiene como objetivo encontrar errores de comandos, sino **evaluar la calidad de la evidencia
científica**.

Cada equipo responderá:

- ¿Las conclusiones están respaldadas por la evidencia?
- ¿Existe alguna afirmación demasiado fuerte?
- ¿Falta alguna validación?
- ¿Qué información adicional sería conveniente obtener?
- ¿Qué fue lo más interesante del genoma analizado?

Finalmente, cada equipo mejorará su protocolo incorporando la retroalimentación recibida.

## Entregables

- proyecto organizado correctamente;
- archivos recuperados y documentados;
- resultados generados durante el análisis;
- protocolo actualizado (`doc/protocolo.md`).

## Criterios de evaluación

| Aspecto | Peso |
| --- | ---: |
| Recuperación correcta del ensamblado | 10 % |
| Organización reproducible del proyecto | 10 % |
| Documentación de procedencia e integridad | 15 % |
| Calidad del análisis del genoma | 25 % |
| Interpretación biológica | 20 % |
| Calidad del protocolo | 15 % |
| Revisión por pares | 5 % |
| **Total** | **100 %** |

## Preparación para S16 y S17

Este mini proyecto integra todos los conocimientos desarrollados desde la Unidad 3 hasta la Sesión
13. Su resultado alimenta las dos sesiones siguientes: en **S16** someterás tu protocolo a la
**revisión por pares** y lo corregirás con lo que recibas; en **S17** demostrarás individualmente,
sobre datos nuevos, que puedes recuperar, verificar, organizar y analizar un ensamblado de manera
autónoma.

## Reflexión final

En este proyecto no aprendiste un nuevo comando. Aprendiste a utilizar herramientas computacionales
para **responder preguntas biológicas mediante evidencia reproducible**: precisamente el trabajo
cotidiano de un investigador en Genómica Computacional.

El **Estado 1 del genoma** representa el primer nivel de conocimiento que puede obtenerse con
herramientas básicas de Unix. En el siguiente bloque del curso aprenderás a formular consultas mucho
más precisas mediante expresiones regulares y nuevas estrategias de transformación de datos, lo que
permitirá revisar, corregir y ampliar muchas de las conclusiones obtenidas hasta ahora.
