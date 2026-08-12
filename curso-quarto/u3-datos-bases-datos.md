# Unidad 3 — Datos y bases de datos biológicas

::: {.callout-note title="Aula invertida"}
Esta unidad se estudia en tres sesiones. Antes de cada sesión leerás
las secciones indispensables y realizarás un primer intento breve. Durante el taller compararás
decisiones, explorarás registros y archivos reales y corregirás tu trabajo con evidencia. Después
integrarás las correcciones en `doc/protocolo.md` y en la ficha de procedencia de tus datos. Los
primeros intentos son formativos: se evalúa que llegues preparado y puedas explicar tus decisiones;
las entregas calificadas son las **Tareas 4 y 5**.
:::

## Ficha de la unidad

| Elemento | Descripción |
| --- | --- |
| **Sesiones** | S7–S9, tres sesiones de 2 horas |
| **Competencia principal** | C. Manejo de datos y bases de datos biológicas |
| **Competencias integradas** | A. Trabajo reproducible y comunicación científica; B. Entorno Unix; G. Uso responsable de IA |
| **Propósito** | Interpretar, recuperar y gestionar datos biológicos considerando qué representan, de dónde provienen y cómo se identifican, versionan y verifican |
| **Contribución al curso** | Convierte la estructura de proyecto construida en U1–U2 en un espacio de trabajo con datos biológicos reales, documentados y listos para procesarse en U4 |
| **Ajustes integrados** | **[Reforzado]** procedencia, metadatos, versiones, integridad y conservación de originales; **[Integración]** pregunta biológica → evidencia → datos → operación → herramienta |
| **Lectura base** | Material de esta unidad y Buffalo (2015), secciones sobre datos, formatos y proyectos bioinformáticos |
| **Lecturas de consulta** | Documentación oficial de NCBI sobre FASTA, GenBank, GFF3 y ensamblados; especificación GFF3 de Sequence Ontology |
| **Producto acumulativo** | Ficha de procedencia de un conjunto de datos + actualización de `doc/protocolo.md` |
| **Tareas del Plan** | Tarea 4: revisión de dos bases de datos de NCBI; Tarea 5: transferencia de archivos del proyecto |

## Punto de partida y continuidad

En la Unidad 1 definiste una pregunta, organizaste un proyecto reproducible y preparaste metadatos.
En la Unidad 2 construiste esa estructura en Unix, aprendiste a inspeccionar y transferir archivos y
comprobaste integridad mediante *checksums*. Ahora aplicarás esas habilidades a datos biológicos
reales.

La unidad mantiene esta estructura:

```text
proyecto/
├── data/
│   ├── source/
│   └── processed/
├── src/
├── results/
└── doc/
```

Los archivos obtenidos de una base pública se conservan, con su nombre original, en
`data/source/`. No se corrigen ni se reformatean allí. Cualquier transformación posterior generará
un archivo nuevo en `data/processed/` (Noble, 2009; Wilson et al., 2017).

## Resultados de aprendizaje de la unidad

Al finalizar, podrás:

1. **Relacionar** una pregunta biológica con la evidencia, el tipo de dato y el formato necesarios.
2. **Distinguir** secuencia, anotación, registro, archivo, identificador, *accession* y versión.
3. **Interpretar** la estructura esencial de archivos FASTA, GFF3 y GenBank.
4. **Consultar** Nucleotide/GenBank, Genome/NCBI Datasets y PubMed con un propósito explícito.
5. **Seleccionar y recuperar** datos registrando procedencia, fecha, versión, formato y condiciones
   de uso.
6. **Verificar** la integridad de una descarga y de una transferencia mediante una suma publicada o
   una comparación origen–destino.
7. **Conservar** los datos fuente sin cambios y **documentar** las decisiones en una ficha de datos
   y en `doc/protocolo.md`.
8. **Revisar críticamente** con IA una ficha ya elaborada a mano y validar las afirmaciones con el
   registro y la documentación oficial.

## Ruta de aprendizaje

Los tiempos son estimaciones; pueden variar según la experiencia previa y la conectividad.

| Momento | Trabajo | Producto | Tiempo estimado |
| --- | --- | --- | ---: |
| Antes de S7 | Leer las secciones indispensables de S7, construir el mapa biológico y comparar tres fragmentos de archivo | Primer intento: mapa + matriz objeto–formato | 100–125 min |
| S7 | Interpretar FASTA, GFF3 y GenBank; explorar un registro | Matriz corregida + selección provisional de datos | 120 min |
| Entre S7 y S8 | Leer S8 y localizar dos bases de NCBI | Borrador de comparación | 45–60 min |
| S8 | Evaluar bases, recuperar archivos y verificar una descarga | Tarea 4 + ficha de procedencia iniciada | 120 min |
| Entre S8 y S9 | Leer S9 y preparar los archivos descargados | Plan de transferencia | 30–40 min |
| S9 | Inspeccionar y transferir sin alterar originales; comparar checksums | Tarea 5 + ficha de procedencia final | 120 min |
| Después de S9 | Corregir protocolo, realizar cierre con IA y entregar | `protocolo.md`, ficha y `bitacora-ia.md` | 45–60 min |

## Módulos de la unidad

### [S7 — Representar: de los objetos biológicos a FASTA, GFF3 y GenBank](u3-s7-secuencias-formatos-genbank.md)

Reconocerás qué representa cada formato, interpretarás identificadores y versiones y relacionarás
una pregunta biológica con la evidencia y los datos que permitirían responderla.

### [S8 — Recuperar: bases de datos, descarga y verificación de integridad](u3-s8-bases-datos-descarga-integridad.md)

Compararás recursos de NCBI, recuperarás archivos de un ensamblado seleccionado y documentarás su
procedencia e integridad. Esta sesión desarrolla la **Tarea 4**.

### [S9 — Verificar: inspección y transferencia de datos biológicos](u3-s9-inspeccion-transferencia-verificable.md)

Inspeccionarás los archivos sin modificar los originales, cerrarás la verificación de integridad
iniciada en S8, recuperarás un archivo de forma reproducible con `wget`/`curl` y demostrarás que
origen y destino contienen los mismos bytes. Esta sesión desarrolla la **Tarea 5**.

## Producto acumulativo: ficha de procedencia de datos

La ficha se inicia en S7, se completa en S8 y se verifica en S9. Como mínimo incluirá:

```markdown
# Ficha de procedencia del conjunto de datos

- Pregunta biológica:
- Evidencia necesaria:
- Organismo o sistema:
- Base de datos y colección:
- Título o descripción del registro:
- Accession completo, incluida la versión:
- URL persistente o página del registro:
- Fecha de consulta y descarga:
- Archivos descargados y nombres originales:
- Formato de cada archivo:
- Estado de compresión:
- Tamaño de cada archivo:
- Checksum publicado y algoritmo:
- Checksum calculado:
- Resultado de la comparación:
- Licencia o condiciones de uso:
- Ruta dentro del proyecto:
- Información no documentada o pendiente de confirmar:
```

::: {.callout-important}
Si la fuente no proporciona un dato, escribe “no documentado” o “pendiente de
confirmar”. No lo completes por inferencia y nunca pidas a una IA que lo invente.
:::

## Evidencias y evaluación

| Evidencia | Momento | Tipo | Qué demuestra |
| --- | --- | --- | --- |
| Matriz objeto–evidencia–formato | S7 | Formativa | Selección razonada de datos y formatos |
| Tarea 4 | Después de S8 | Calificada | Comparación documentada de dos bases de NCBI |
| Tarea 5 | Después de S9 | Calificada | Transferencia reproducible con integridad comprobada |
| Ficha de procedencia | S7–S9 | Acumulativa | Origen, versión, formato, checksum y ubicación de los datos |
| `doc/protocolo.md` | S7–S9 | Acumulativa | Decisiones, comandos, resultados y limitaciones |
| `doc/bitacora-ia.md` | Después de S9 | Formativa | Uso declarado, comparación y validación independiente |

## Cierre de la unidad

Al terminar verifica que puedes responder:

- ¿Qué objeto biológico representa cada archivo?
- ¿Qué diferencia hay entre una base de datos, un registro y un archivo descargado?
- ¿Qué identificador y versión permiten volver a localizar los mismos datos?
- ¿Por qué FASTA y GFF3 no son intercambiables?
- ¿Qué evidencia demuestra que una descarga o transferencia llegó íntegra?
- ¿Dónde se conserva el original y dónde se colocarán sus derivados?
- ¿Qué información sigue pendiente de confirmar?

Los archivos verificados de esta unidad serán las entradas de la Unidad 4, donde aprenderás a
inspeccionarlos, filtrarlos, resumirlos y transformarlos mediante herramientas Unix.

## Referencias generales

- Buffalo, V. (2015). *Bioinformatics Data Skills*. O’Reilly Media.
- Noble, W. S. (2009). A quick guide to organizing computational biology projects. *PLoS
  Computational Biology*, 5(7), e1000424. <https://doi.org/10.1371/journal.pcbi.1000424>
- Wilson, G., et al. (2017). Good enough practices in scientific computing. *PLoS Computational
  Biology*, 13(6), e1005510. <https://doi.org/10.1371/journal.pcbi.1005510>
