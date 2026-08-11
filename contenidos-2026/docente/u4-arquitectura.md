# Unidad 4 — Arquitectura de la unidad (documento de diseño)

> **NOTA DE VIGENCIA (ago-2026).** Este documento describe el orden **S16 = Examen práctico 1,
> S17 = revisión**, que el plan operativo invirtió. En la pestaña vigente
> `PlanClases-2026-final S34`, **S16 es la revisión por pares y S17 la evaluación individual
> demostrativa**, con la nota *«la revisión por pares precede a la evaluación individual»*. Se
> conserva el texto original como registro del diseño; para el orden vigente, consúltese el Plan.


> **NOTA:** Este documento **no es material para el estudiante**. Es el diseño previo de la Unidad 4:
> hilo conductor, propuesta de sesiones, matriz de evolución de las preguntas biológicas y evolución
> de la evidencia integradora. Una vez aprobado, cada sesión se redactará como módulo autocontenido
> (`u4-sNN-<nombre>.md`) siguiendo `contenidos-2026/plantilla-unidad.md` y las convenciones de
> `contenidos-2026/README.md`.

---

## 1. Visión general de la unidad

### 1.1 Hilo conductor

**La Unidad 4 es una investigación sobre un genoma, no un curso de comandos Unix.**

El estudiante llega a S10 con algo que no tenía en ninguna unidad anterior: **datos biológicos reales,
propios, verificados y documentados**. En U3 demostró que sus archivos FASTA y GFF3 son exactamente
los que dice tener (procedencia, versión, checksum, ubicación). Ese material deja de ser un objeto que
se describe y se convierte en un objeto que se **interroga**.

Toda la unidad se construye alrededor de una sola investigación:

> **¿Qué puedo afirmar sobre este genoma a partir de la evidencia contenida en sus archivos?**

De esa pregunta se desprende un conjunto reducido y estable de preguntas biológicas —tamaño,
replicones, tipos de *features*, fuentes de anotación, número de genes y CDS, distribución por
cadena— que **permanecen prácticamente constantes durante las diez sesiones**. Lo que cambia no es la
pregunta: es la **capacidad analítica** con la que el estudiante la responde.

Cada sesión responde otra vez preguntas ya visitadas, pero con una estrategia más limpia, más
robusta, más reproducible o más expresiva. El estudiante nunca debe sentir que repite un ejercicio;
debe sentir que **su respuesta anterior era provisional y ahora puede mejorarla, y sabe por qué**.

El ejemplo canónico de este movimiento es la primera pregunta de la unidad:

```text
¿De qué tamaño es el genoma?

S10   wc -c genome.fna              →  cuenta bytes: incluye encabezados y saltos de línea
S11   diagnóstico estructural       →  sabes POR QUÉ está mal (líneas cortadas a 60–80 caracteres,
                                       encabezados contados como texto), pero aún no puedes corregirlo
S12   grep -v ">" | tr -d "\n" | wc -c  →  cuenta bases reales
S13   contraste con la longitud declarada en ##sequence-region del GFF3
S22   awk suma longitudes por replicón y reporta el total
```

Cinco momentos en una misma pregunta. Ninguna es un ejercicio nuevo: cada una **corrige una
limitación observada en la anterior**, y esa corrección es exactamente la justificación pedagógica
para introducir la herramienta siguiente.

### 1.2 Cambio de paradigma respecto a la Unidad 3

| Dimensión | Unidad 3 | Unidad 4 |
| --- | --- | --- |
| Relación con el dato | Se **obtiene**, se documenta y se verifica | Se **interroga**: el dato responde preguntas |
| Pregunta rectora | ¿De dónde viene este archivo y cómo demuestro que es el mismo? | ¿Qué dice este archivo sobre el genoma? |
| Operación característica | Recuperar, inspeccionar, comparar checksums | Filtrar, resumir, cuantificar, transformar |
| El archivo es… | Un objeto que se conserva intacto | Una **fuente de evidencia** que se lee sin alterarla |
| Criterio de éxito | Integridad demostrada | **Interpretación biológica sustentada** en evidencia reproducible |
| Naturaleza del error | El archivo llegó corrupto | La **estrategia de conteo** era incorrecta |
| Producto | Ficha de procedencia + protocolo | Protocolo convertido en **cuaderno de laboratorio computacional** |
| Rol de la herramienta | Medio para mover y verificar | Medio para **expresar una pregunta** con precisión creciente |

Hay un cambio adicional, más sutil pero decisivo para el diseño: en U3 **un resultado es correcto o
incorrecto** (el checksum coincide o no). En U4 **un resultado puede ser correcto y aun así ser mala
evidencia**: un `grep -c gene` devuelve un número perfectamente válido que no responde la pregunta
"¿cuántos genes hay?". Aprender a detectar esa diferencia —y a documentarla— es el núcleo formativo
de la unidad.

Por eso la unidad conserva y refuerza los cuatro principios transversales del curso:

- **Reproducibilidad:** todo resultado va acompañado del comando exacto que lo produjo.
- **Verificación:** el resultado se comprueba en pequeño antes de aplicarlo al archivo completo.
- **Validación:** la misma cantidad se obtiene por **dos caminos independientes** (p. ej. replicones
  contados en FASTA y en GFF3) y se contrasta con la fuente.
- **Robustez:** se identifica qué supuesto rompería la estrategia (comentarios, delimitadores,
  valores faltantes, coincidencias parciales).

### 1.3 Principios de diseño de la unidad

1. **Ninguna sesión se llama como un comando.** Las sesiones se nombran por la **etapa de la
   investigación** (reconocer, inventariar, filtrar, resumir, precisar, transformar, condicionar,
   integrar).
2. **Ninguna herramienta aparece antes de que su ausencia duela.** Cada herramienta se introduce
   inmediatamente después de que el estudiante haya **chocado con la limitación** que ella resuelve.
3. **Toda actividad termina en interpretación biológica**, al nivel que la evidencia permite: qué
   significa el resultado, qué aprendimos del genoma, si apoya la hipótesis y qué nueva pregunta
   abre.
4. **El protocolo es uno solo** y no reinicia: es el mismo `doc/protocolo.md` de U1–U3, que en esta
   unidad adquiere su forma de cuaderno de laboratorio.
5. **La guía no es un manual de Unix.** Cada herramienta se presenta con una caja de *Sintaxis
   mínima* (≤ 2 líneas de "¿qué hace?", más "¿por qué aparece aquí?") y un par de prompts a
   **ProfeUnix Bioinfo** para explorar opciones adicionales por cuenta propia.
6. **Datos originales intactos.** Todo lo producido en U4 se escribe en `data/processed/` o
   `results/`; `data/source/` no se toca (Noble, 2009).

---

## 2. Propuesta de sesiones

La unidad ocupa **diez sesiones de 2 h**: **S10–S13** y **S18–S23** del Plan operativo 2026. Entre
ambos bloques se intercalan S14–S15 (semana de práctica integradora), S16 (Examen práctico 1) y S17
(revisión), que **no pertenecen a U4** pero condicionan su diseño: el bloque S10–S13 debe cerrar una
etapa completa y evaluable, y S18 debe reabrir la investigación sin depender de la memoria fresca de
S13.

```text
BLOQUE A — Establecer los hechos del genoma           BLOQUE B — El ciclo de la evidencia
S10 Reconocer      S11 Inventariar                    S18 Seleccionar   S19 Identificar
S12 Filtrar        S13 Resumir y cuantificar          S20 Normalizar    S21 Confrontar
                                                      S22 Cuantificar   S23 Integrar
        ↓                                                      ↓
  Estado 1 del genoma: hechos básicos                   Cuaderno de laboratorio completo
  (evaluable en S16)                                    + protocolo ejecutable (evidencia integradora)
```

El bloque A pregunta *qué contiene este archivo*; el bloque B enseña *cómo se construye una pieza de
evidencia*. Ese segundo hilo se desarrolla en §2.b y ordena las seis sesiones finales.

> **NOTA — orden de las herramientas.** El orden `cut → grep → sort/uniq → uniq -c → regex → tr/sed →
> awk` no expresa una jerarquía absoluta entre comandos, sino la secuencia en que **las limitaciones
> aparecen** al analizar un GFF3 real. Si al pilotear la unidad una limitación aparece antes, el orden
> debe ajustarse a la evidencia, no al revés.

---

### S10 — Reconocer el terreno: anatomía de un archivo biológico y construcción de flujos

**[Plan: S10 · Procesos, redirecciones y tuberías · Comp. D]**

- **Propósito.** Convertir los archivos verificados en U3 en objetos legibles y manipulables:
  reconocer su estructura (líneas, columnas, delimitadores, encabezados, comentarios, valores
  faltantes) y aprender a **encadenar y capturar** el trabajo mediante entrada estándar, salida
  estándar, redirecciones y *pipes*.
- **Preguntas biológicas que responde.**
  - ¿Qué tipo de información contiene cada uno de mis archivos y en qué unidad se organiza?
  - ¿De qué tamaño es el genoma? *(primera aproximación, deliberadamente imperfecta)*
  - ¿Cuántos registros de anotación hay en el GFF3? *(primera aproximación)*
- **Herramientas nuevas.** Visualización y edición de texto aplicada a datos biológicos (`less`,
  `nano`/`vi` en modo lectura), `cat`, `wc` (`-l`, `-c`, `-w`); entrada/salida estándar y error;
  redirecciones `>`, `>>`, `2>`; *pipes* `|`.
- **Herramientas reutilizadas.** `head`, `tail`, `file`, `ls -l` (U2–U3); estructura de proyecto y
  conservación de originales (U1).
- **Limitación que resuelve.** Hasta ahora el estudiante solo podía *mirar* el archivo y quedarse con
  una impresión. Ahora puede **medir** y, sobre todo, **guardar** un resultado con evidencia del
  comando que lo produjo.
- **Evolución de la capacidad analítica.** De "veo el archivo" a "produzco un resultado reproducible
  y lo dirijo a donde quiero". Aparece la idea de **flujo**: la salida de un paso es la entrada del
  siguiente.
- **Limitación con la que cierra (motor de S11).** `wc -c genome.fna` cuenta bytes, no bases:
  incluye encabezados y saltos de línea. `wc -l genomic.gff` cuenta líneas, no anotaciones: incluye
  las líneas de comentario `##`. **Los números obtenidos son incorrectos y el estudiante sabe por
  qué.**
- **Actualización del protocolo.** Sección *Datos de trabajo y anatomía de los archivos*: descripción
  estructural de FASTA y GFF3 (qué es una línea, qué separa las columnas, dónde están los
  encabezados y comentarios, cómo se representa un valor faltante), primeras mediciones **con su
  advertencia explícita de sobreestimación**, y convención de nombres para los resultados en
  `results/`.
- **Cómo prepara la siguiente.** Deja abierta una pregunta operativa concreta: *para contar bases o
  anotaciones necesito quedarme solo con ciertas líneas y ciertas columnas — ¿cómo separo las
  columnas?*

---

### S11 — Inventariar: las columnas del genoma y sus coordenadas

**[Plan: S11 · Análisis de un genoma (FASTA/GFF): conteos · Comp. D]**

- **Propósito.** Descubrir que el GFF3 es una **tabla** y que cada columna responde a una pregunta
  distinta; aprender a extraer columnas y a leer coordenadas genómicas.
- **Preguntas biológicas que responde.**
  - ¿Qué información codifica cada campo de la anotación? (secuencia, fuente, tipo, inicio, fin,
    cadena, atributos)
  - ¿Cuántos cromosomas o replicones tiene el genoma? *(vía `cut -f1`, con ruido de comentarios)*
  - ¿Por qué el tamaño medido en S10 está mal? *(diagnóstico estructural: las líneas de secuencia
    están cortadas a 60–80 caracteres y el encabezado también se contó; se identifica la causa, la
    corrección llega en S12)*
- **Herramientas nuevas.** `cut` (`-f`, `-d`, `-c`); noción operativa de **delimitador**
  (tabulador vs. coma vs. espacio) y de **encabezado**; representación de **valores faltantes** en
  GFF3 (`.` en *score*, *phase*, *strand*).
- **Herramientas reutilizadas.** *Pipes*, redirecciones, `wc`, `head`/`tail`, `less`.
- **Limitación que resuelve.** El archivo dejaba de ser interrogable porque el estudiante no podía
  aislar la información: preguntaba por el tipo de *feature* y recibía la línea completa.
- **Evolución de la capacidad analítica.** De "el archivo tiene líneas" a "el archivo tiene
  **columnas con significado biológico**". Primera vez que el estudiante formula una pregunta
  biológica **en términos de una columna concreta**.
- **Limitación con la que cierra (motor de S12).** Al hacer `cut -f3` aparecen líneas de comentario,
  celdas vacías y registros que no interesan; el inventario está contaminado. **Hace falta decidir
  qué líneas entran al análisis.**
- **Actualización del protocolo.** Sección *Estructura tabular de la anotación*: diccionario de las
  nueve columnas del GFF3 con la pregunta que cada una permite responder, tratamiento documentado de
  los valores faltantes, y **tabla de versiones de la pregunta "tamaño del genoma"** (respuesta S10,
  respuesta S11, por qué cambió).
- **Cómo prepara la siguiente.** El estudiante necesita un mecanismo para **excluir** (comentarios) y
  **seleccionar** (registros pertinentes) antes de cortar columnas.

---

### S12 — Filtrar: seleccionar los registros que responden la pregunta

**[Plan: S12 · Exploración de datos genómicos · Comp. D · ver §5 Discrepancias]**

- **Propósito.** Introducir el filtrado por patrón como la operación que convierte un archivo
  completo en **el subconjunto pertinente a una pregunta**, y establecer desde el inicio su riesgo
  característico: el falso positivo.
- **Preguntas biológicas que responde.**
  - ¿Cuántos genes hay en el genoma? *(primera respuesta cuantitativa)*
  - ¿Cuántas CDS hay?
  - ¿Cuántos orígenes de replicación están anotados?
  - ¿De qué tamaño es el genoma? *(tercera respuesta: `grep -v ">" | tr -d "\n" | wc -c`; ahora sí,
    bases reales — se introduce `tr` únicamente en este uso puntual y se retoma a fondo en S20)*
- **Herramientas nuevas.** `grep` (`-c`, `-v`, `-i`, `-w`, `-n`); uso mínimo de `tr -d` para eliminar
  saltos de línea.
- **Herramientas reutilizadas.** `cut`, `wc`, *pipes*, redirecciones.
- **Limitación que resuelve.** Elimina el ruido: quita los comentarios `##` y aísla los registros de
  un tipo. Por primera vez el estudiante obtiene un **número defendible**.
- **Evolución de la capacidad analítica.** De "extraigo columnas de todo el archivo" a "**decido qué
  registros entran al análisis**". Y con ello aparece la pregunta crítica de la unidad: *¿estoy
  contando lo que creo que estoy contando?* `grep -c gene` también cuenta `pseudogene`, `tRNA` cuya
  descripción contiene "gene", y coincidencias en la columna de atributos.
- **Limitación con la que cierra (motor de S13).** El estudiante puede contar **un** tipo a la vez,
  pero no sabe **qué tipos existen** ni cuántos hay de cada uno. Contar tipo por tipo no escala y no
  garantiza cobertura.
- **Actualización del protocolo.** Sección *Filtrado y primeros conteos*: pregunta, hipótesis,
  comando exacto, resultado, **interpretación biológica** y un apartado nuevo y permanente,
  *Limitaciones de la estrategia*, donde se documenta al menos un falso positivo detectado y cómo se
  detectó.
- **Cómo prepara la siguiente.** *No puedo enumerar a mano lo que no sé que existe: necesito que el
  archivo me diga qué tipos contiene.*

---

### S13 — Resumir y cuantificar: el inventario completo del genoma

**[Plan: S13 · Patrones y filtros · Comp. D · ver §5 Discrepancias]**

- **Propósito.** Pasar del conteo puntual al **inventario exhaustivo**: obtener el catálogo completo
  de categorías presentes en la anotación y su frecuencia, sin conocerlas de antemano.
- **Preguntas biológicas que responde.**
  - ¿Qué tipos de *features* contiene la anotación y **cuántos tipos distintos** existen?
  - ¿Cuántos registros hay de cada tipo?
  - ¿Cuáles son las fuentes de anotación y qué proporción aporta cada una?
  - ¿Cuántos replicones tiene el genoma? *(respuesta robusta: `cut -f1 | sort -u | wc -l`, contrastada
    con `grep -c ">"` del FASTA y con las líneas `##sequence-region`)*
- **Herramientas nuevas.** `sort` (`-u`, `-n`, `-r`, `-k`), `uniq`, `uniq -c`.
- **Herramientas reutilizadas.** `grep`, `cut`, `wc`, *pipes*, redirecciones.
- **Limitación que resuelve.** Ya no hace falta saber qué buscar: **el archivo declara su propio
  vocabulario**. El conteo deja de ser artesanal y se vuelve exhaustivo y ordenable.
- **Evolución de la capacidad analítica.** De "cuento lo que se me ocurre preguntar" a "**construyo
  la distribución completa de una variable categórica**". Aquí entra de forma natural la lectura
  descriptiva: categoría dominante, categorías raras, proporciones, y la advertencia de que un conteo
  de registros no equivale a un conteo de objetos biológicos.
- **Limitación con la que cierra (motor de S18).** Los patrones siguen siendo literales: `grep gene`
  no distingue `gene` de `pseudogene`, y no hay forma de decir "la palabra completa, al inicio del
  campo, exactamente esto". **Falta precisión en la especificación del patrón.**
- **Actualización del protocolo.** Sección *Inventario del genoma*: tabla de tipos de *feature* con
  frecuencias, tabla de fuentes de anotación, número de replicones **con los tres caminos
  independientes y su comparación** (validación), e interpretación biológica del perfil de anotación.
- **Cómo prepara la siguiente.** Cierra el **Estado 1 del genoma** (hechos básicos establecidos),
  evaluable en el Examen práctico 1, y deja planteada la pregunta de precisión que abrirá S18.

> **Cierre del bloque A.** Al terminar S13 el estudiante puede responder, con evidencia reproducible,
> qué tamaño tiene el genoma, cuántos replicones lo componen, qué contiene su anotación y en qué
> proporciones. Ese es el material que S14–S15 practican y que S16 evalúa.

---

## 2.b El ciclo de la evidencia *(hilo conductor del bloque B)*

El bloque A respondía preguntas sobre **un archivo**. El bloque B enseña algo distinto y más
transferible: **cómo se construye una pieza de evidencia científica**, paso a paso. Cada sesión
aporta un verbo de ese proceso, no una herramienta.

```text
S18  SELECCIONAR   la evidencia correcta        ¿estoy mirando las líneas que debo?
      ↓
S19  IDENTIFICAR   el objeto biológico correcto ¿de qué objeto habla cada línea?
      ↓
S20  NORMALIZAR    la evidencia para compararla ¿está expresada de forma comparable?
      ↓
S21  CONFRONTAR    con otra fuente              ¿lo confirma alguien ajeno a mis archivos?
      ↓
S22  CUANTIFICAR   e interpretar                ¿cuánto, en qué proporción y qué significa?
      ↓
S23  INTEGRAR      el ciclo completo            ¿puede otra persona reproducirlo entero?
```

Leído así, el bloque deja de parecer una secuencia de comandos (`regex → grep -o → sed → awk`) y pasa
a ser lo que realmente es: **el procedimiento por el que una observación se convierte en evidencia
publicable**. Las herramientas cambian; el ciclo no.

Tres consecuencias de diseño que este hilo impone a cada sesión del bloque B:

1. **El verbo va en el título.** Ninguna sesión se titula con la herramienta que introduce. La
   herramienta aparece dentro, cuando el verbo la necesita.
2. **Cada sesión sitúa al estudiante en el ciclo.** El material debe dejar claro qué paso se trabaja
   hoy, cuál quedó resuelto y cuál queda pendiente —igual que la tabla *Dónde estás en la
   investigación* hace con las preguntas biológicas—.
3. **S23 no es un paso más.** Es el recorrido completo del ciclo en una sola pasada, sobre los
   archivos originales: por eso conserva el verbo *integrar*, que aquí significa reunir los cinco
   pasos anteriores en un protocolo ejecutable, no "juntar dos fuentes" (eso es **confrontar**, y
   ocurre en S21).

> **NOTA — por qué importa este encuadre.** Un estudiante de primer semestre olvidará la sintaxis de
> `awk` en un año. Lo que puede llevarse para siempre es el orden del razonamiento: seleccionar,
> identificar, normalizar, confrontar, cuantificar, integrar. Ese ciclo es el mismo en un análisis de
> secuencias, en uno de expresión o en uno clínico, y es lo que distingue a un investigador de un
> usuario de herramientas.

---

### S18 — Precisar: expresiones regulares para decir exactamente lo que se quiere buscar

**[Plan: S18 · Expresiones regulares · Comp. D]**

- **Propósito.** Sustituir el patrón literal por una **descripción formal** del patrón, y con ello
  eliminar los falsos positivos documentados en S12–S13.
- **Preguntas biológicas que responde (todas **re**-visitadas, con precisión nueva).**
  - ¿Cuántos genes hay, **excluyendo** pseudogenes y coincidencias en atributos?
  - ¿Cuántas CDS hay, contando solo el campo *type*?
  - ¿Cuántos genes hay en cada cadena? *(primera respuesta, vía patrón sobre columnas cortadas)*
- **Herramientas nuevas.** Expresiones regulares básicas: anclas `^` `$`, clases `[ ]`, `.`,
  cuantificadores `*` `+` `?`, alternancia y agrupación con `grep -E`; `grep -w` reinterpretado.
- **Herramientas reutilizadas.** `grep`, `cut`, `sort`, `uniq -c`, *pipes*.
- **Limitación que resuelve.** El patrón literal no distingue **dónde** ni **cómo** ocurre la
  coincidencia. La regex permite anclar, delimitar y describir clases de cadenas.
- **Evolución de la capacidad analítica.** De "busco un texto" a "**especifico formalmente qué cuenta
  como coincidencia**". Es el primer momento en que el estudiante corrige un resultado ya escrito en
  su protocolo y documenta la corrección: la reproducibilidad se vuelve **auditable**.
- **Limitación con la que cierra (motor de S19).** La regex identifica líneas, pero el estudiante
  quiere **extraer** el fragmento que coincide (un identificador dentro del campo de atributos, un
  *locus_tag* dentro de un encabezado FASTA).
- **Actualización del protocolo.** Sección *Refinamiento de los conteos*: tabla comparativa
  "resultado previo / resultado refinado / diferencia / causa de la diferencia", que se convierte en
  el apartado modelo de *Mejoras respecto a la estrategia anterior*.
- **Cómo prepara la siguiente.** *Ya sé seleccionar la línea correcta; ahora necesito quedarme con la
  parte correcta de la línea.*

---

### S19 — Extraer: identificadores, encabezados y campos dentro del texto

**[Plan: S19 · Expresiones regulares (aplicación) · Comp. D]**

- **Propósito.** Aplicar las regex a las dos estructuras que no son tablas limpias: los **encabezados
  FASTA** y la **columna de atributos del GFF3**, donde la información útil está anidada dentro de
  una cadena.
- **Preguntas biológicas que responde.**
  - ¿Cuáles son los identificadores de los replicones y coinciden entre FASTA y GFF3?
  - ¿Qué identificadores tienen los genes y cómo se relacionan con las CDS?
  - ¿Hay registros de anotación cuyo replicón no exista en el FASTA (o viceversa)?
- **Herramientas nuevas.** Regex aplicadas con `grep -o`; combinación de `cut -d` con delimitadores
  distintos del tabulador para descomponer atributos.
- **Herramientas reutilizadas.** Regex de S18, `cut`, `sort -u`, `uniq -c`, `comm` o `diff` como
  comparación de listas (uso puntual, presentado como herramienta de contraste).
- **Limitación que resuelve.** La información clave del GFF3 y del FASTA **no está en una columna
  propia**; hay que extraerla del texto.
- **Evolución de la capacidad analítica.** De "cuento registros" a "**relaciono dos archivos por sus
  identificadores**". Aparece la validación cruzada FASTA↔GFF3 como práctica estándar.
- **Limitación con la que cierra (motor de S20).** Las listas extraídas están sucias: prefijos
  redundantes, mayúsculas inconsistentes, delimitadores mezclados. **Comparar exige normalizar
  primero.**
- **Actualización del protocolo.** Sección *Correspondencia entre archivos*: lista de identificadores
  por archivo, resultado de la comparación e interpretación de cualquier discrepancia (¿error del
  análisis o característica del ensamblado?).
- **Cómo prepara la siguiente.** Plantea la necesidad de transformar el texto sin tocar el original.

---

### S20 — Transformar: normalizar el texto para poder compararlo

**[Plan: S20 · Sustituciones y transformaciones (sed) · Comp. D]**

- **Propósito.** Producir versiones **derivadas y limpias** de los datos —en `data/processed/`— que
  permitan comparar, tabular y compartir resultados, sin alterar jamás `data/source/`.
- **Preguntas biológicas que responde.**
  - ¿Puedo construir una tabla limpia de anotaciones (replicón, tipo, inicio, fin, cadena,
    identificador) a partir del GFF3?
  - ¿Cómo represento y documento los valores faltantes en esa tabla?
  - ¿Coinciden los identificadores una vez normalizados?
- **Herramientas nuevas.** `tr` (traducir, eliminar, comprimir), `sed` (sustitución `s///`, `-n` con
  `p`, borrado de líneas, direccionamiento por número o patrón).
- **Herramientas reutilizadas.** Regex, `grep`, `cut`, `sort`, `uniq`, redirecciones.
- **Limitación que resuelve.** Hasta aquí el estudiante solo podía **leer** el archivo. Ahora puede
  producir un **derivado** apto para el análisis, con un cambio de delimitador, un encabezado
  añadido y los valores faltantes explicitados.
- **Evolución de la capacidad analítica.** De "consulto datos" a "**genero datos procesados**", con
  la responsabilidad que ello implica: el derivado necesita trazabilidad (comando exacto, archivo de
  origen, fecha) y debe poder regenerarse desde el original.
- **Limitación con la que cierra (motor de S21–S22).** El estudiante tiene una tabla limpia pero
  sigue sin poder expresar condiciones del tipo *"líneas donde la columna 3 sea gene **y** la columna
  7 sea +"*, ni operar aritméticamente sobre las coordenadas.
- **Actualización del protocolo.** Sección *Datos derivados*: descripción del archivo generado en
  `data/processed/`, comando exacto que lo produce, criterio de normalización, tratamiento de
  faltantes y verificación de que el original permanece intacto.
- **Cómo prepara la siguiente.** Con una tabla limpia y propia, comparar con una tabla de otra fuente
  se vuelve una pregunta natural.

---

### S21 — Confrontar: aplicar el flujo a una tabla biológica de otra procedencia

**[Plan: S21 · Ensembl y BioMart · Comp. C, D · ver §5 Discrepancias]**

- **Propósito.** Demostrar que el flujo construido no depende del archivo con el que nació:
  aplicarlo a una **tabla biológica obtenida de otro recurso** —UniProt como fuente principal, o la
  anotación GenBank del mismo ensamblado como alternativa; **no BioMart**, ver D8— y confrontar sus
  resultados con los del análisis propio.
- **Preguntas biológicas que responde.**
  - ¿Una fuente independiente coincide con mi inventario de genes y CDS?
  - ¿A qué se deben las diferencias: al criterio de anotación, a la versión del ensamblado o a mi
    estrategia de conteo?
  - ¿Qué delimitadores, encabezados y valores faltantes tiene esta tabla y en qué se diferencian de
    los del GFF3?
- **Herramientas nuevas.** Ninguna herramienta Unix nueva: la novedad es el **recurso** y la
  operación intelectual de **contraste entre fuentes**.
- **Herramientas reutilizadas.** Todo el repertorio: `head`/`tail`, `wc`, `cut` (`-f` y `-d`),
  `grep` + regex, `sort`, `sort -u`, `uniq -c`, `tr`, `sed`, **`comm`**, *pipes* y redirecciones.
  Recuperación documentada de datos (U3).
- **Limitación que resuelve.** Un análisis validado solo contra sí mismo no está validado. Esta
  sesión aporta la **evidencia independiente** que exige el principio de validación del curso.
- **Evolución de la capacidad analítica.** De "analizo mi archivo" a "**contrasto mi resultado con
  otra fuente y explico la discrepancia**" — la operación que distingue un resultado de una
  conclusión.
- **Limitación con la que cierra (motor de S22).** Las preguntas que quedan sin responder son todas
  del mismo tipo: requieren **combinar condiciones sobre varias columnas** y **calcular** (longitudes,
  sumas, promedios, densidades). Ninguna herramienta vista lo permite.
- **Actualización del protocolo.** Sección *Contraste con una fuente independiente*: procedencia de la
  segunda tabla (ficha mínima al estilo U3), comparación de resultados e interpretación argumentada
  de las diferencias.
- **Cómo prepara la siguiente.** Deja una lista explícita de preguntas pendientes que solo `awk`
  puede responder.

---

### S22 — Condicionar y calcular: expresar preguntas complejas sobre columnas

**[Plan: S22 · Formateo de datos con awk · Comp. D · Tarea 7]**

- **Propósito.** Alcanzar la máxima expresividad de la unidad: formular en un solo paso condiciones
  que combinan varias columnas y realizar cálculos sobre coordenadas.
- **Preguntas biológicas que responde.**
  - ¿Cuántos genes hay en cada cadena (`+` / `−`) y están equilibrados?
  - ¿Cuál es la longitud de cada gen y cuál su distribución (mínimo, máximo, media, mediana)?
  - ¿Qué densidad de genes tiene cada replicón (genes por kb)?
  - ¿De qué tamaño es el genoma? *(respuesta final: suma de longitudes por replicón, contrastada con
    S12 y con `##sequence-region`)*
- **Herramientas nuevas.** `awk`: campos `$1…$NF`, `NR`, `NF`, patrones con condiciones lógicas
  (`&&`, `||`), acciones `print`, aritmética sobre campos, `-F` para el delimitador, formateo de
  salida. *(Sin variables de shell, sin parámetros, sin ciclos externos — ver §5.)*
- **Herramientas reutilizadas.** Todo lo anterior; en particular `sort -n` y `uniq -c` para ordenar y
  resumir las salidas de `awk`.
- **Limitación que resuelve.** Combinar `grep`, `cut` y `sort` para una condición multi-columna
  producía tuberías largas, frágiles y difíciles de leer, y no permitía **calcular**. `awk` expresa la
  misma pregunta en una línea legible.
- **Evolución de la capacidad analítica.** De "filtro y cuento" a "**expreso una pregunta biológica
  compleja como una condición y obtengo una medida**". Es también el punto donde el estudiante
  reconoce que existen varias soluciones correctas y puede argumentar cuál es más clara o más
  robusta.
- **Limitación con la que cierra (motor de S23).** Cada respuesta vive en un comando suelto en el
  protocolo. Repetir el análisis completo exige recorrer el documento y copiar comandos a mano:
  **el análisis es reproducible pero no está integrado.**
- **Actualización del protocolo.** Sección *Análisis condicionado*: preguntas resueltas con `awk`,
  con su comparación explícita frente a la estrategia previa (qué se gana en claridad, robustez o
  precisión), tabla de longitudes y densidades, e interpretación biológica.
- **Cómo prepara la siguiente.** El protocolo está completo en contenido pero disperso en forma; S23
  lo convierte en un instrumento ejecutable.

---

### S23 — Integrar: el protocolo como cuaderno de laboratorio ejecutable

**[Plan: S23 · awk (refuerzo) · Comp. D · ver §5 Discrepancias]**

- **Propósito.** Consolidar toda la investigación en un **protocolo ejecutable**: una secuencia
  ordenada y verificada de comandos que, ejecutados en orden sobre los archivos de `data/source/`,
  reproducen todas las respuestas de la unidad y generan las tablas de `results/`.
- **Preguntas biológicas que responde.** Las **mismas de toda la unidad**, ahora respondidas de una
  sola pasada, más la pregunta integradora del alcance oficial: *construye un archivo ordenado por
  cadena y posición genómica.*
- **Herramientas nuevas.** Ninguna. La novedad es la **composición**: encadenamiento de flujos,
  orden de operaciones, nombres de archivos intermedios, verificación de cada paso.
- **Herramientas reutilizadas.** Todas las de la unidad.
- **Limitación que resuelve.** Un cuaderno con resultados correctos pero dispersos no permite que
  otra persona —ni el propio estudiante en un mes— rehaga el análisis. La integración cierra la
  brecha entre *documentado* y *reproducible*.
- **Evolución de la capacidad analítica.** De "resuelvo preguntas una por una" a "**tengo un
  procedimiento completo, ordenado y verificable para analizar un genoma**". Es también el punto
  donde la limitación siguiente se vuelve evidente y deseable: *ejecutar esto a mano cada vez es
  tedioso y propenso a error* → puerta natural a la **Unidad 5 (variables, parámetros, ciclos,
  automatización)**.
- **Actualización del protocolo.** Sección final *Protocolo ejecutable*: bloque de comandos en orden,
  archivo de salida esperado en cada paso, tabla resumen de hallazgos del genoma, síntesis
  interpretativa, limitaciones globales del análisis y **preguntas abiertas** que la unidad no puede
  responder.
- **Cierre con IA.** Cierre de unidad **clásico vs. asistido**: se reproduce con IA una o dos
  preguntas ya resueltas a mano (p. ej. el conteo de genes por cadena), se compara con la línea base
  manual, se contrasta con `man` y con pruebas controladas en un archivo pequeño, y se registra en
  `doc/bitacora-ia.md`. Alucinaciones típicas a cazar: opciones de `awk` inexistentes, confusión
  entre BRE y ERE en `grep`/`sed`, y conteos que ignoran los comentarios `##`.

---

## 3. Matriz de evolución de las preguntas *(eje de diseño de la unidad)*

Cada fila es una pregunta biológica de la investigación. **Ninguna se responde de una vez**: se
responde por primera vez con lo disponible y se refina cuando aparece la herramienta que corrige su
limitación.

| # | Pregunta biológica | 1.ª aparición | Estrategia inicial | Refinamientos sucesivos (sesión · herramienta · qué corrige) | Resuelta en |
| --- | --- | --- | --- | --- | --- |
| P1 | ¿De qué tamaño es el genoma? | S10 | `wc -c genome.fna` (bytes del archivo) | **S11 · diagnóstico estructural**: se identifica la causa del error (líneas cortadas, encabezados contados), sin corregirla aún · **S12 · `grep -v ">"` + `tr -d "\n"` + `wc -c`**: excluye encabezados y saltos de línea, cuenta bases reales · **S13 · `sort -u` sobre `##sequence-region`**: contraste con la longitud declarada · **S22 · `awk`**: suma de longitudes por replicón y total | S22 |
| P2 | ¿Cuántos cromosomas o replicones tiene? | S10 | Inspección visual de encabezados con `head`/`grep ">"` | **S11 · `cut -f1`**: usa la columna 1 del GFF3 · **S13 · `sort -u \| wc -l`**: enumeración exhaustiva y sin duplicados; contraste de tres caminos independientes (FASTA, GFF3, `##sequence-region`) · **S19 · regex**: verifica que los identificadores coincidan entre archivos | S13 (validada en S19) |
| P3 | ¿Qué tipos de *features* contiene la anotación? | S11 | `cut -f3 \| head` (muestra parcial, con comentarios) | **S12 · `grep -v "^#"`**: elimina el ruido de comentarios · **S13 · `sort -u`**: catálogo completo sin conocerlo de antemano | S13 |
| P4 | ¿Cuántos tipos distintos existen? | S12 | Conteo manual de la lista observada | **S13 · `sort -u \| wc -l`**: conteo exhaustivo y reproducible | S13 |
| P5 | ¿Cuántos registros hay de cada tipo? | S12 | `grep -c` tipo por tipo (no escala, riesgo de falso positivo) | **S13 · `sort \| uniq -c \| sort -nr`**: distribución completa ordenada · **S18 · regex ancladas**: elimina falsos positivos por coincidencia parcial · **S22 · `awk '$3=="gene"'`**: restringe la coincidencia al campo correcto | S22 |
| P6 | ¿Cuáles son las fuentes de anotación y en qué proporción? | S11 | `cut -f2 \| head` | **S13 · `sort \| uniq -c`**: frecuencia por fuente · **S21 · contraste externo**: comparación con otra fuente de anotación | S21 |
| P7 | ¿Cuántos genes existen? | S12 | `grep -c "gene"` (incluye `pseudogene` y coincidencias en atributos) | **S13 · `cut -f3 \| grep -w`**: restringe a la columna de tipo · **S18 · `grep -E "^gene$"`**: coincidencia exacta, sin pseudogenes · **S21 · fuente independiente**: validación externa · **S22 · `awk '$3=="gene"'`**: expresión única y explícita | S22 |
| P8 | ¿Cuántas CDS existen? | S12 | `grep -c "CDS"` | **S13 · `uniq -c`**: aparece en el inventario completo · **S18 · regex**: coincidencia exacta en el campo de tipo · **S22 · `awk`**: conteo condicionado y relación CDS/gen | S22 |
| P9 | ¿Cuántos orígenes de replicación están anotados? | S12 | `grep -ci "origin"` (búsqueda literal, sensible al vocabulario del archivo) | **S13 · inventario de tipos**: confirma cómo se nombra realmente el *feature* · **S18 · regex**: distingue el tipo del texto descriptivo en atributos | S18 |
| P10 | ¿Cuántos genes hay en cada cadena? | S18 | `cut -f3,7 \| grep` + `sort \| uniq -c` (tubería larga y frágil) | **S22 · `awk '$3=="gene" && $7=="+"'`**: condición multi-columna en un paso, con proporciones | S22 |
| P11 | ¿Qué identificador tiene cada objeto y coinciden entre archivos? | S19 | `grep -o` + `cut -d` sobre atributos y encabezados | **S20 · `sed`/`tr`**: normalización previa a la comparación · **S21 · contraste externo**: correspondencia con los identificadores de otra fuente | S21 |
| P12 | ¿Cuál es la longitud de los genes y cómo se distribuye? | S22 | `awk '{print $5-$4+1}'` + `sort -n`, `uniq -c` | Se resuelve en la propia sesión; la interpretación (mínimo, máximo, media, mediana, casos atípicos) se documenta en el protocolo | S22 |
| P13 | ¿Puedo construir un archivo ordenado por cadena y posición genómica? *(pregunta integradora del alcance oficial)* | S20 | Tabla limpia derivada con `sed`/`tr` en `data/processed/` | **S22 · `awk` + `sort -k`**: selección condicionada y ordenamiento numérico por múltiples claves · **S23**: integración en el protocolo ejecutable, con verificación del resultado | S23 |
| P14 | ¿Qué puedo afirmar sobre este genoma en conjunto? *(pregunta rectora)* | S10 | Descripción estructural de los archivos | Se reformula al cierre de **cada** sesión, incorporando la evidencia acumulada | S23 |

**Cómo se usa esta matriz al redactar cada sesión.** Antes de escribir un módulo se leen las columnas
de esa sesión: las preguntas que **aparecen** por primera vez definen su contenido nuevo; las que se
**refinan** definen sus prácticas de retorno —y cada una debe entrar por la limitación de la
estrategia previa, nunca como repetición. Si una sesión no refina ninguna pregunta anterior, está mal
diseñada.

---

## 4. Evidencia integradora: evolución del protocolo

La evidencia integradora de la Unidad 4 es **el mismo `doc/protocolo.md` que el estudiante abrió en
U1**, convertido en un **cuaderno de laboratorio computacional** que culmina en un **protocolo
ejecutable** capaz de responder preguntas sobre un genoma a partir de FASTA y GFF3.

### 4.1 Estructura que adquiere cada entrada

A partir de S12, cada bloque de análisis del protocolo usa este esqueleto fijo (los tres últimos
apartados son la aportación característica de U4):

```markdown
## <Etapa del análisis>

- Pregunta biológica:
- Hipótesis o expectativa previa:
- Datos necesarios y archivo utilizado:
- Estrategia de análisis (con la capacidad disponible en este momento):
- Comandos ejecutados (exactos, ejecutables tal cual):
- Resultados obtenidos:
- Interpretación biológica:
- Limitaciones de esta estrategia:
- Mejoras respecto a la estrategia anterior:
- Nuevas preguntas que abre:
```

### 4.2 Qué apartado incorpora el estudiante después de cada sesión

| Sesión | Apartado nuevo en `doc/protocolo.md` | Contenido mínimo | Archivos generados |
| --- | --- | --- | --- |
| **S10** | *Datos de trabajo y anatomía de los archivos* | Inventario de archivos heredados de U3 (con su ruta y checksum ya documentado); descripción estructural de FASTA y GFF3: línea, delimitador, encabezado, comentario, valor faltante. Primeras mediciones **marcadas como aproximaciones**, con la razón de su imprecisión. Convención de nombres de `results/`. | `results/` con los primeros conteos redirigidos |
| **S11** | *Estructura tabular de la anotación* | Diccionario de las nueve columnas del GFF3 con la pregunta que cada una habilita; criterio documentado para los valores faltantes; **primera tabla de versiones de una respuesta** (P1: valor S10 → valor S11 → causa del cambio). | Extracciones de columnas en `results/` |
| **S12** | *Filtrado y primeros conteos* | Bloque completo con el esqueleto de §4.1 para P7, P8 y P9; aparece por primera vez *Limitaciones de la estrategia*, con al menos un falso positivo detectado y cómo se detectó. | Subconjuntos filtrados en `results/` |
| **S13** | *Inventario del genoma* | Tabla de tipos de *feature* con frecuencias; tabla de fuentes de anotación; número de replicones **por tres caminos independientes** con su comparación; interpretación del perfil de anotación. **Cierra el Estado 1 del genoma.** | `results/inventario-features.tsv`, `results/fuentes.tsv` |
| **S18** | *Refinamiento de los conteos* | Tabla "resultado previo / resultado refinado / diferencia / causa"; el apartado *Mejoras respecto a la estrategia anterior* pasa a ser obligatorio en todos los bloques posteriores. | Conteos corregidos en `results/` |
| **S19** | *Correspondencia entre archivos* | Listas de identificadores extraídas de FASTA y GFF3; resultado de la comparación; interpretación de toda discrepancia (¿error del análisis o característica del ensamblado?). | `results/ids-fasta.txt`, `results/ids-gff.txt` |
| **S20** | *Datos derivados* | Descripción del derivado en `data/processed/`: comando exacto que lo genera, criterio de normalización, delimitador y encabezado elegidos, tratamiento de faltantes, y comprobación de que `data/source/` sigue intacto. | `data/processed/anotacion-limpia.tsv` |
| **S21** | *Contraste con una fuente independiente* | Ficha mínima de procedencia de la segunda tabla (al estilo U3); comparación de resultados frente al análisis propio; interpretación argumentada de las diferencias. | `data/source/<fuente-externa>/`, `results/comparacion-fuentes.tsv` |
| **S22** | *Análisis condicionado* | Bloques de P10, P12 y el cierre de P1, P5, P7, P8 con `awk`; tabla de genes por cadena, longitudes y densidad por replicón; comparación explícita con la estrategia previa. | `results/genes-por-cadena.tsv`, `results/longitudes.tsv` |
| **S23** | *Protocolo ejecutable* + *Síntesis del genoma* + *Cierre con IA* | Secuencia ordenada y verificada de comandos que reproduce todo el análisis desde `data/source/`; salida esperada de cada paso; archivo ordenado por cadena y posición (P13); tabla resumen de hallazgos; limitaciones globales; preguntas abiertas hacia U5–U6; entradas nuevas en `doc/bitacora-ia.md`. | `results/anotacion-ordenada.tsv` y el conjunto completo regenerado |

### 4.3 Criterio de logro de la evidencia integradora

El protocolo se considera logrado si **otra persona, con los archivos de `data/source/` y solo este
documento**, puede:

1. ejecutar los comandos en orden y obtener **los mismos resultados**;
2. entender **por qué** cada pregunta se responde así y no de otro modo;
3. identificar **qué limitación** tenía cada estrategia previa y **cómo** se corrigió;
4. leer una **interpretación biológica** para cada resultado, no solo la salida del comando;
5. saber **qué queda pendiente** y por qué la unidad no puede responderlo.

---

## 5. Alcance, delimitaciones y discrepancias con el Plan operativo

### 5.1 Cobertura del alcance oficial

| Contenido obligatorio | Sesión(es) |
| --- | --- |
| Visualización y edición de archivos de texto | S10 |
| Delimitadores · Encabezados · Valores faltantes | S10 (reconocimiento), S11 (operación), S20 (normalización) |
| Entrada estándar · Salida estándar · Redirecciones · Pipes | S10, reutilizados en todas |
| Conteos | S10 (`wc`), S12 (`grep -c`), S13 (`uniq -c`), S22 (`awk`) |
| `head`, `tail`, `wc` | S10 |
| `cut` | S11 |
| `grep` | S12 |
| `sort`, `uniq` | S13 |
| Expresiones regulares básicas | S18, aplicadas en S19 |
| `tr` | S12 (uso puntual), S20 (a fondo) |
| `sed` | S20 |
| `awk` | S22, integrado en S23 |
| Aplicaciones sobre FASTA | S10, S11, S12, S19, S23 |
| Aplicaciones sobre GFF3 | S11–S23 (eje de la unidad) |
| Aplicaciones sobre tablas biológicas | S20, S21 |
| **Evidencia integradora: protocolo ejecutable sobre FASTA y GFF3** | S23 (construida desde S10) |

### 5.2 Delimitación con unidades posteriores

**No se desarrollan en U4:** BLAST, alineamientos, homología, ortólogos, parálogos, *scripting*,
variables de shell, parámetros, ciclos ni automatización. Cuando la limitación correspondiente
aparezca de forma natural —sobre todo al cierre de S23— se nombra como **puerta hacia la Unidad 5**,
sin desarrollarla.

> **NOTA:** `awk` en S22 se usa exclusivamente como lenguaje de patrones y acciones en una línea
> (campos, condiciones, aritmética, formato). No se introducen `BEGIN`/`END` con acumuladores
> complejos, arreglos asociativos ni archivos de programa `.awk`: eso pertenece al momento de
> *scripting*.

### 5.3 Discrepancias con el Plan de clases 2026 (a resolver antes de redactar S10)

Se registran conforme al procedimiento de la guía: se documenta la discrepancia y se alinea al Plan
salvo indicación en contrario.

| # | Plan operativo | Alcance oficial de U4 | Propuesta de esta arquitectura |
| --- | --- | --- | --- |
| D1 | **S11** introduce **variables y un primer `for`** ("siembra temprana de *scripting*", [Reforzado]) | Excluye explícitamente variables, ciclos y automatización | Se **posponen a U5**. S11 conserva el objetivo de conteos del Plan. Si se decide mantener la siembra temprana, el lugar de menor costo conceptual es el **cierre de S23**, donde la necesidad de repetir el flujo ya es evidente. **Requiere decisión docente.** |
| D2 | **S12** es *Exploración estadística básica* [Nuevo] | El alcance lista "conteos", no estadística descriptiva | Se **distribuye** en vez de eliminarse: conteos por categoría y proporciones en **S13**; distribución de longitudes con mínimo, máximo, media y mediana en **S22**, siempre como **interpretación biológica** y sin herramientas fuera del alcance. La sesión S12 se destina al filtrado, que el Plan sitúa en S13. |
| D3 | **S13** es *Patrones y filtros (grep)* | — | El contenido de `grep` se **adelanta a S12** y S13 pasa a resumen/cuantificación (`sort`, `uniq`), porque la limitación que motiva `sort \| uniq -c` solo aparece **después** de filtrar. Es un intercambio de orden entre dos sesiones contiguas, sin pérdida de contenido. |
| D4 | **S21** es *Ensembl y BioMart* (Comp. C, D) | El alcance incluye "aplicaciones sobre tablas biológicas", no un recurso concreto | Se conserva Ensembl/BioMart como **fuente de la tabla biológica**, con foco en el **contraste entre fuentes** y no en la navegación del recurso (ya trabajada en U3). Si se prefiere otra fuente tabular, la sesión funciona igual. |
| D5 | **S23** introduce **parámetros de entrada y encadenamiento en un script** | Excluye *scripting* y parámetros | Se **posponen a U5**. S23 conserva el encadenamiento **como protocolo ejecutable** (secuencia verificada de comandos), que cumple la evidencia integradora sin introducir *scripting*. **Requiere decisión docente**, junto con D1. |
| D6 | Tarea 6 (S10): reporte de lectura + 1.er avance del proyecto; Tarea 7 (S22): reformateo con `awk` | — | Se **respetan sin cambios** la numeración y el momento de las Tareas. La Tarea 7 se enuncia como *"reformatear y condicionar la anotación para responder una pregunta biológica"*, no como ejercicio de `awk`. |
| D8 | **S21** es *Ensembl y BioMart* | Aplicaciones sobre tablas biológicas | **BioMart no es viable**: Ensembl Bacteria no lo soporta desde la expansión de 2013 a decenas de miles de genomas —el recurso lo declara no soportado y remite a su API—, y todo el curso trabaja con bacterias. Se sustituye la fuente por **UniProt** (proteoma en TSV, con *ordered locus name*) y, como alternativa, la **anotación GenBank `GCA_…` del mismo ensamblado**. El contenido del Plan —contraste con una tabla biológica de otra procedencia— se conserva íntegro; solo cambia el recurso. Detalle en `u4-s21-arquitectura-confrontar.md`. **Resuelto (ago-2026).** |
| D7 | La Tarea 6 pide reporte de lectura del **Cap. 3** de Buffalo | — | El Cap. 3 (*Remedial Unix Shell*) **ya fue lectura base de la Unidad 2** (S3, S4 y S5): volver a reportarlo duplica la evidencia. La lectura obligatoria de U4 pasa al **Cap. 7 (*Unix Data Tools*)**, que corresponde exactamente al contenido de la unidad; el Cap. 3 queda como repaso de consulta. Numeración y momento de la Tarea 6 sin cambios. **Resuelto (27-jul-2026).** |

---

## 6. Verificación de esta arquitectura

- [x] Ninguna sesión lleva el nombre de un comando.
- [x] Cada sesión declara la **limitación** que la origina y la que deja abierta.
- [x] Toda herramienta del alcance oficial tiene sesión asignada (§5.1) y ninguna aparece antes de que
      su ausencia se haya vuelto un obstáculo.
- [x] Las preguntas biológicas son estables; lo que evoluciona es la estrategia (matriz §3).
- [x] Cada sesión actualiza un apartado identificable del protocolo único (§4.2).
- [x] No se introducen BLAST, homología, *scripting*, variables, parámetros ni ciclos.
- [x] La evidencia integradora coincide con la del alcance oficial: protocolo ejecutable sobre FASTA y
      GFF3.
- [x] Se conserva la continuidad con U3: mismos archivos, misma estructura de proyecto, originales
      intactos, integridad ya demostrada y no repetida.
- [x] Las discrepancias con el Plan quedan registradas y no se resuelven unilateralmente (§5.3).

---

## 7. Archivos de la unidad

Se conserva la convención de nombres ya usada en U1–U3 (`contenidos-2026/`): minúsculas, sin
acentos ni mayúsculas, palabras separadas por guiones, prefijo `uN-` para la portada y `uN-sNN-`
para cada módulo, y nombre derivado del **tema de la sesión**, nunca de un comando.

| Sesión | Archivo | Tema del nombre |
| --- | --- | --- |
| — (portada) | `u4-procesamiento-exploracion.md` | Portada de la unidad (nombre ya previsto en el índice del README) |
| S10 | `u4-s10-anatomia-flujos-datos.md` | Anatomía del archivo biológico y flujos de datos |
| S11 | `u4-s11-estructura-tabular-anotacion.md` | Estructura tabular de la anotación |
| S12 | `u4-s12-filtrado-conteos-genoma.md` | Filtrado y primeros conteos |
| S13 | `u4-s13-inventario-resumen-genoma.md` | Inventario y resumen del genoma |
| S18 | `u4-s18-precision-patrones-expresiones-regulares.md` | Precisión de los patrones |
| S19 | `u4-s19-extraccion-identificadores-correspondencia.md` | Extracción de identificadores y correspondencia entre archivos |
| S20 | `u4-s20-normalizar-datos-comparables.md` | Normalización y datos derivados |
| S21 | `u4-s21-confrontar-fuente-independiente.md` | Contraste con una fuente independiente |
| S21 (docente) | `u4-s21-arquitectura-confrontar.md` | Arquitectura específica de S21: fuente, prácticas y figuras |
| S22 | `u4-s22-condicionar-calcular-columnas.md` | Análisis condicionado y medidas derivadas |
| S23 | `u4-s23-protocolo-ejecutable-genoma.md` | Protocolo ejecutable del genoma |

Este documento de diseño (`u4-arquitectura.md`) no forma parte del material del estudiante y no se
publica; queda como referencia docente junto a `u2-notas-revision-docente.md`.

---

## 8. Siguiente paso

Arquitectura aprobada. **D1 y D5 resueltas por decisión docente (27-jul-2026):** variables, ciclos y
parámetros se **posponen íntegramente a la Unidad 5**; S11 conserva solo los conteos y S23 cierra la
unidad como **protocolo ejecutable**, dejando la necesidad de automatizar como puerta natural hacia
U5.

Se redactará primero la **portada de unidad** (`u4-procesamiento-exploracion.md`) y a continuación el
módulo **S10** (`u4-s10-anatomia-flujos-datos.md`), completo y autocontenido, verificado contra la
checklist de 16 puntos.
