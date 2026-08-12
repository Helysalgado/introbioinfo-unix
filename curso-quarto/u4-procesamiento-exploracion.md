# Unidad 4 — Procesamiento y exploración de datos genómicos

::: {.callout-note title="Aula invertida:"}
Esta unidad se estudia en diez sesiones. Antes de cada una leerás las
secciones marcadas como **indispensables** y harás un primer intento breve: casi siempre, escribir
qué estrategia usarías para responder una pregunta biológica, **sin ejecutar todavía nada**. Durante
el taller ejecutarás, compararás resultados y descubrirás las limitaciones de tu estrategia.
Después integrarás la corrección en `doc/protocolo.md`. Los primeros intentos son formativos: se
evalúa que llegues preparado y puedas explicar tus decisiones. Las entregas calificadas son la
**Tarea 6**, la **Tarea 7** y los avances del proyecto integrador.
:::

## De qué trata esta unidad

En la Unidad 3 conseguiste algo que ahora vale mucho: un conjunto de archivos biológicos **reales,
propios, verificados y documentados**. Sabes de dónde vienen, qué versión son y puedes demostrar con
un checksum que nadie los ha alterado.

Hasta aquí has **descrito** esos archivos. En esta unidad vas a **interrogarlos**.

La Unidad 4 no es una unidad para aprender comandos de Unix. Es una unidad para **analizar un
genoma**. Los comandos aparecen únicamente porque te permiten responder preguntas biológicas, y
aparecen en el momento en que los necesitas, no antes.

Toda la unidad gira alrededor de una sola investigación:

> **¿Qué puedo afirmar sobre este genoma a partir de la evidencia contenida en sus archivos?**

Y de esa pregunta se desprenden otras, más concretas, que te acompañarán durante las diez sesiones:

- ¿De qué tamaño es el genoma?
- ¿Cuántos cromosomas o replicones tiene?
- ¿Qué tipos de *features* contiene su anotación y cuántos tipos distintos existen?
- ¿Cuáles son las fuentes de anotación?
- ¿Cuántos genes hay? ¿Cuántas CDS? ¿Cuántos orígenes de replicación?
- ¿Cuántos genes hay en cada cadena?
- ¿Puedo construir un archivo ordenado por cadena y posición genómica?

::: {.callout-important}
Estas preguntas **no cambian** a lo largo de la unidad. Lo que cambia eres tú. La
primera vez responderás algunas de forma imperfecta —y sabrás por qué es imperfecta—. Cada sesión
te dará una herramienta que corrige una limitación concreta de tu respuesta anterior. No estarás
repitiendo ejercicios: estarás **mejorando tu evidencia**.
:::

Un ejemplo real de ese recorrido, con la primera pregunta de la unidad:

```text
¿De qué tamaño es el genoma?

S10   cuentas los bytes del archivo      →  incluye encabezados y saltos de línea: sobreestima
S11   descubres por qué está mal         →  las líneas están cortadas y el encabezado también contó
S12   excluyes encabezados y saltos      →  ahora sí: bases reales
S13   lo contrastas con lo que declara el propio GFF3
S22   lo calculas por replicón y lo sumas
```

Cinco respuestas a la misma pregunta, cada una mejor que la anterior y cada una documentada. Al final
de la unidad, tu protocolo mostrará ese recorrido completo: eso es un **cuaderno de laboratorio
computacional**.

## Ficha de la unidad

| Elemento | Descripción |
| --- | --- |
| **Sesiones** | S10–S13 y S18–S23, diez sesiones de 2 horas |
| **Competencia principal** | D. Análisis y exploración de datos genómicos |
| **Competencias integradas** | A. Trabajo reproducible y comunicación científica; B. Entorno Unix; C. Manejo de datos biológicos; G. Uso responsable de IA |
| **Propósito** | Construir flujos de trabajo transparentes para inspeccionar, filtrar, resumir y transformar archivos de texto biológico, y responder con ellos preguntas sobre un genoma |
| **Contribución al curso** | Convierte los datos verificados de U3 en evidencia interpretada, y el protocolo del curso en un cuaderno de laboratorio computacional con un procedimiento ejecutable |
| **Ajustes integrados** | **[Reforzado]** interpretación biológica de cada resultado y documentación de limitaciones; **[Integración]** pregunta biológica → evidencia → datos → operación → herramienta |
| **Lectura obligatoria (con evidencia)** | Buffalo (2015), Cap. 7 *Unix Data Tools* — evidencia: reporte de lectura de la **Tarea 6** |
| **Lectura de consulta** | Fitzgerald (2012), para expresiones regulares; especificación GFF3 de Sequence Ontology; Buffalo (2015), Cap. 3, ya leído en U2, como repaso puntual |
| **Producto acumulativo** | `doc/protocolo.md` convertido en cuaderno de laboratorio, con un **protocolo ejecutable** al cierre |
| **Tareas del Plan** | Tarea 6 (S10): reporte de lectura + 1.er avance del proyecto · Tarea 7 (S22): reformateo y análisis condicionado de un archivo tabular |

| **Evaluación intermedia** | Revisión por pares (S16) y evaluación individual demostrativa (S17), sobre lo trabajado en S10–S13 |

## Punto de partida y continuidad

No hay nada que volver a descargar ni que volver a verificar. Trabajas exactamente con los archivos
que dejaste en `data/source/` al terminar S9:

```text
proyecto/
├── data/
│   ├── source/        ← originales verificados en U3. NO se modifican en esta unidad
│   └── processed/     ← aquí nacen los archivos derivados que construirás (S20 en adelante)
├── src/
├── results/           ← aquí se guardan las salidas de tus análisis
└── doc/
    ├── protocolo.md   ← el mismo documento desde U1; aquí se convierte en cuaderno de laboratorio
    └── bitacora-ia.md
```

::: {.callout-warning}
En esta unidad vas a leer, filtrar, contar y transformar tus archivos muchas veces.
**Ninguna de esas operaciones modifica `data/source/`.** Todo lo que produzcas se escribe en
`results/` (salidas de análisis) o en `data/processed/` (archivos derivados reutilizables). Si al
final de la unidad el checksum de un archivo de `data/source/` cambió, algo salió mal (Noble, 2009;
Wilson et al., 2017).
:::

Lo que ya sabes hacer y seguirás usando: navegar el sistema de archivos y operar con rutas (S4),
inspeccionar sin modificar con `head`, `tail`, `less` y `file` (S5, S9), interpretar la estructura de
FASTA, GFF3 y GenBank (S7) y documentar decisiones con honestidad (U1–U3).

## Resultados de aprendizaje de la unidad

Al finalizar, podrás:

1. **Reconocer** la estructura de un archivo de texto biológico: líneas, columnas, delimitadores,
   encabezados, comentarios y valores faltantes.
2. **Construir** flujos de trabajo con entrada estándar, salida estándar, redirecciones y *pipes*, y
   capturar sus resultados de forma reproducible.
3. **Extraer** columnas y campos pertinentes a una pregunta biológica.
4. **Filtrar** registros mediante patrones y **detectar** los falsos positivos que un patrón
   demasiado laxo produce.
5. **Resumir y cuantificar** la información de un archivo: inventarios completos, frecuencias por
   categoría y ordenamientos.
6. **Especificar** patrones con expresiones regulares básicas para eliminar coincidencias
   indeseadas.
7. **Transformar** texto biológico (delimitadores, encabezados, valores faltantes) generando archivos
   derivados trazables, sin alterar los originales.
8. **Expresar** condiciones sobre varias columnas y **calcular** medidas sencillas a partir de
   coordenadas genómicas.
9. **Contrastar** un resultado propio con el de una fuente independiente y **explicar** las
   diferencias.
10. **Interpretar biológicamente** cada resultado y **documentar** las limitaciones de la estrategia
    empleada.
11. **Integrar** todo el análisis en un **protocolo ejecutable** que otra persona pueda reproducir.
12. **Contrastar críticamente** con IA un análisis ya resuelto a mano, validando con documentación y
    pruebas controladas.

## Ruta de aprendizaje

Los tiempos son estimaciones y pueden variar según tu experiencia previa.

| Momento | Trabajo | Producto | Tiempo estimado |
| --- | --- | --- | ---: |
| Antes de S10 | Leer S10 y el Cap. 7 de Buffalo; primer intento sobre la anatomía de tus archivos | Notas + primer intento | 90–110 min |
| **S10** | Anatomía de FASTA y GFF3; flujos, redirecciones y *pipes* | Primeras mediciones, con su advertencia | 120 min |
| Entre S10 y S11 | Redactar el reporte de lectura y el 1.er avance del proyecto | **Tarea 6** | 60–90 min |
| **S11** | Estructura tabular de la anotación; extracción de columnas | Diccionario de columnas | 120 min |
| **S12** | Filtrado de registros y primeros conteos defendibles | Conteos + limitaciones documentadas | 120 min |
| **S13** | Inventario completo del genoma; frecuencias y ordenamientos | **Estado 1 del genoma** | 120 min |
| S14–S15 | Semana de práctica integradora (fuera de U4) | 2.º avance del proyecto | 240 min |
| S16–S17 | Revisión por pares y evaluación individual demostrativa (fuera de U4) | Dictamen + evaluación individual | 240 min |
| **S18** | Precisión de los patrones con expresiones regulares | Conteos refinados | 120 min |
| **S19** | Extracción de identificadores y correspondencia FASTA↔GFF3 | Listas comparadas | 120 min |
| **S20** | Normalización y generación de datos derivados | Tabla limpia en `data/processed/` | 120 min |
| **S21** | Tabla biológica de otra fuente y contraste de resultados | Comparación entre fuentes | 120 min |
| **S22** | Análisis condicionado sobre columnas y cálculo de longitudes | **Tarea 7** iniciada | 120 min |
| **S23** | Integración: protocolo ejecutable y cierre con IA | Evidencia integradora | 120 min |
| Después de S23 | Cerrar el protocolo, entregar Tarea 7 y actualizar la bitácora de IA | `protocolo.md`, `bitacora-ia.md` | 60–90 min |

**Secciones indispensables:** en cada módulo, las marcadas [Indispensable] y la práctica del
primer intento. **De consulta:** las cajas de *Sintaxis mínima* con opciones adicionales y los
prompts a ProfeUnix Bioinfo, que puedes explorar a tu ritmo.

## Módulos de la unidad

### Bloque A — Establecer los hechos del genoma (S10–S13)

#### [S10 — Reconocer: anatomía de un archivo biológico y flujos de datos](u4-s10-anatomia-flujos-datos.md)

Reconocerás cómo está organizado por dentro un FASTA y un GFF3 —líneas, delimitadores, encabezados,
comentarios, valores faltantes— y aprenderás a encadenar operaciones y capturar resultados con
*pipes* y redirecciones. Obtendrás tus primeras mediciones y descubrirás por qué son imprecisas.
Esta sesión desarrolla la **Tarea 6**.

#### [S11 — Localizar: la estructura tabular de la anotación](u4-s11-estructura-tabular-anotacion.md)

Descubrirás que el GFF3 es una tabla y que cada columna responde a una pregunta biológica distinta.
Aprenderás a extraer la columna pertinente y a leer coordenadas genómicas.

#### [S12 — Filtrar y contar: primeras preguntas sobre el genoma](u4-s12-filtrado-conteos-genoma.md)

Decidirás qué registros entran a tu análisis y obtendrás tus primeros números defendibles sobre
genes, CDS y orígenes de replicación. También aprenderás a desconfiar de ellos: un conteo puede ser
correcto y aun así responder otra pregunta.

#### [S13 — Resumir y cuantificar: inventario del genoma](u4-s13-inventario-resumen-genoma.md)

Dejarás de contar solo lo que se te ocurre preguntar: el archivo te dirá qué contiene. Construirás el
inventario completo de tipos de *feature* y de fuentes de anotación, con sus frecuencias, y
establecerás el número de replicones por tres caminos independientes.

::: {.callout-note}
Al terminar S13 cierras el **Estado 1 del genoma**: sabes su tamaño, cuántos replicones
tiene, qué contiene su anotación y en qué proporciones. Ese es el material de la semana de práctica
integradora (S14–S15), de la revisión por pares (S16) y de la evaluación individual (S17).
:::

### Bloque B — Precisar, transformar y concluir (S18–S23)

#### [S18 — Precisar: decir exactamente lo que se quiere buscar](u4-s18-precision-patrones-expresiones-regulares.md)

Corregirás los falsos positivos que detectaste en S12–S13. Aprenderás a describir formalmente un
patrón —anclarlo, delimitarlo, definir clases— y volverás sobre tus conteos anteriores para
mejorarlos y documentar la corrección.

#### [S19 — Extraer: identificadores, encabezados y campos dentro del texto](u4-s19-extraccion-identificadores-correspondencia.md)

Extraerás la información que está anidada dentro del texto: identificadores en los encabezados FASTA
y en la columna de atributos del GFF3. Con ellos comprobarás si ambos archivos hablan realmente del
mismo genoma.

#### [S20 — Normalizar: preparar los datos para compararlos](u4-s20-normalizar-datos-comparables.md)

Producirás tu primer archivo derivado: una tabla limpia de anotaciones en `data/processed/`, con el
delimitador, el encabezado y el tratamiento de valores faltantes que tú decidas y documentes.

#### [S21 — Confrontar: validar un resultado con una fuente independiente](u4-s21-confrontar-fuente-independiente.md)

Aplicarás el mismo flujo a una tabla biológica obtenida de otro recurso y confrontarás sus resultados
con los tuyos. Un análisis validado solo contra sí mismo no está validado.

#### [S22 — Condicionar y calcular: preguntas complejas sobre columnas](u4-s22-condicionar-calcular-columnas.md)

Formularás en un solo paso preguntas que combinan varias columnas y calcularás medidas a partir de
las coordenadas: genes por cadena, longitudes, densidad génica. Esta sesión desarrolla la
**Tarea 7**.

#### [S23 — Integrar: el protocolo como cuaderno de laboratorio ejecutable](u4-s23-protocolo-ejecutable-genoma.md)

Integrarás todo el recorrido en una secuencia ordenada y verificada de comandos que reproduce el
análisis completo desde `data/source/`, construirás el archivo ordenado por cadena y posición
genómica y cerrarás la unidad comparando tu trabajo manual con el de una IA.

## Producto acumulativo: el protocolo como cuaderno de laboratorio

No abres un documento nuevo. Sigues ampliando el mismo `doc/protocolo.md` que iniciaste en U1. A
partir de S12, cada bloque de análisis que agregues tendrá esta forma:

```markdown
## <Etapa del análisis>

- Pregunta biológica:
- Hipótesis o expectativa previa:
- Datos necesarios y archivo utilizado:
- Estrategia de análisis (con lo que sé hacer en este momento):
- Comandos ejecutados (exactos, ejecutables tal cual):
- Resultados obtenidos:
- Interpretación biológica:
- Limitaciones de esta estrategia:
- Mejoras respecto a la estrategia anterior:
- Nuevas preguntas que abre:
```

::: {.callout-important}
Los tres últimos apartados son la marca distintiva de esta unidad. Un protocolo que
solo enumera comandos y resultados no es un cuaderno de laboratorio: falta lo que **aprendiste del
genoma**, lo que tu estrategia **no puede** garantizar y **por qué** la versión de hoy es mejor que
la de la sesión pasada.
:::

Y no borres lo anterior. Si en S18 corriges el conteo de genes que escribiste en S12, **conserva
ambos** y explica la diferencia: esa corrección documentada vale más que el número final.

## Evidencia integradora

Al cerrar S23, tu protocolo debe contener un **protocolo ejecutable**: una secuencia ordenada de
comandos que, partiendo de los archivos FASTA y GFF3 de `data/source/`, responda las preguntas de la
unidad y genere las tablas de `results/`.

Se considera logrado si otra persona, con tus archivos originales y **solo este documento**, puede:

1. ejecutar los comandos en orden y obtener **los mismos resultados**;
2. entender **por qué** cada pregunta se responde así y no de otro modo;
3. identificar **qué limitación** tenía cada estrategia previa y **cómo** se corrigió;
4. leer una **interpretación biológica** de cada resultado, no solo la salida del comando;
5. saber **qué queda pendiente** y por qué esta unidad no puede responderlo.

## Evidencias y evaluación

| Evidencia | Momento | Tipo | Qué demuestra |
| --- | --- | --- | --- |
| Primeros intentos de cada sesión | Antes de cada taller | Formativa | Preparación y razonamiento previo a ejecutar |
| **Tarea 6** | Después de S10 | Calificada | Reporte de lectura (Buffalo, Cap. 7) + 1.er avance del proyecto |
| Estado 1 del genoma | S13 | Acumulativa | Tamaño, replicones e inventario de la anotación, con validación cruzada |
| Práctica integradora | S14–S15 | Formativa | Aplicación autónoma con datos nuevos (fuera de U4) |
| Revisión por pares | S16 | Calificada | Lectura crítica de un análisis ajeno y mejora del propio |
| Evaluación individual demostrativa | S17 | Calificada | Dominio individual de flujos, filtrado y conteos |
| **Tarea 7** | Después de S22 | Calificada | Reformateo y análisis condicionado de un archivo tabular |
| `doc/protocolo.md` | S10–S23 | Acumulativa | Preguntas, comandos, resultados, interpretación, limitaciones y mejoras |
| Protocolo ejecutable | S23 | Integradora | Reproducibilidad completa del análisis del genoma |
| `doc/bitacora-ia.md` | S23 | Formativa | Uso declarado de IA, comparación y validación independiente |

## Uso de IA en esta unidad

Se mantiene la regla del curso: **primero a mano, después con IA**. Durante las sesiones,
[ProfeUnix Bioinfo](https://chatgpt.com/g/g-6893cf2451d88191b11cd0c87de045ab-profeunix-bioinfo)
aparece como recurso de **consulta puntual** —para ampliar las opciones de una herramienta que ya
usaste—, nunca como fuente del resultado. El cierre crítico se hace en S23: reproducirás con IA una o
dos preguntas ya resueltas a mano y compararás.

::: {.callout-warning}
Esta unidad es especialmente propicia para las alucinaciones técnicas: opciones de
comandos que no existen, diferencias entre variantes de expresiones regulares, o conteos que ignoran
las líneas de comentario del GFF3. Solo detectarás esos errores si antes hiciste el análisis a mano.
Registra todo uso relevante en `doc/bitacora-ia.md`.
:::

## Cierre de la unidad

Al terminar verifica que puedes responder:

- ¿Qué estructura tiene por dentro un archivo FASTA y uno GFF3?
- ¿Cómo se encadenan varias operaciones y cómo se guarda su resultado?
- ¿Cómo paso de una pregunta biológica a una columna concreta de un archivo?
- ¿Por qué un conteo puede ser correcto y aun así no responder la pregunta?
- ¿Cómo obtengo la misma cantidad por dos caminos independientes y qué hago si no coinciden?
- ¿Dónde escribo un archivo derivado y cómo demuestro que el original sigue intacto?
- ¿Qué significan mis resultados sobre este genoma en particular?
- ¿Qué no puede responder mi análisis y por qué?

Lo que aprendiste aquí se ejecuta comando por comando, a mano, cada vez. En la **Unidad 5** eso
cambia: aprenderás a guardar resultados en variables, a parametrizar y a repetir un flujo sobre
muchos archivos sin escribirlo de nuevo. La necesidad la habrás sentido tú mismo al final de S23.

## Referencias generales

- Buffalo, V. (2015). *Bioinformatics Data Skills*. O'Reilly Media. — Cap. 7 (*Unix Data Tools*:
  flujos, redirecciones, `grep`, `cut`, `sort`, `uniq`, `awk`, `sed`); Cap. 3 (*Remedial Unix Shell*),
  ya leído en la Unidad 2.
- Fitzgerald, M. (2012). *Introducing Regular Expressions*. O'Reilly Media.
- Noble, W. S. (2009). A quick guide to organizing computational biology projects. *PLoS
  Computational Biology*, 5(7), e1000424. <https://doi.org/10.1371/journal.pcbi.1000424>
- Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough
  practices in scientific computing. *PLoS Computational Biology*, 13(6), e1005510.
  <https://doi.org/10.1371/journal.pcbi.1005510>
- Sequence Ontology. (2020). *Generic Feature Format Version 3 (GFF3) specification*.
  <https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md>
