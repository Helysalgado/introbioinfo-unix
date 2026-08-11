# Unidad 5 — Arquitectura de la unidad (documento de diseño)

**Automatización y scripting bioinformático** · Sesiones **S24–S26** · Competencia **E**

> **NOTA:** Este documento **no es material para el estudiante**. Es el diseño previo de la Unidad 5:
> hilo conductor, propuesta de sesiones, matriz de evolución de las preguntas biológicas y evidencia
> integradora. Una vez aprobado, cada sesión se redactará como módulo autocontenido
> (`u5-sNN-<nombre>.md`) siguiendo `contenidos-2026/plantilla-unidad.md` y las convenciones de
> `contenidos-2026/README.md`.

> **IMPORTANTE — orden de las unidades.** Esta unidad va **antes** de la Unidad 6 (*Comparación de
> secuencias y homología*), como fija el Programa 2026. La decisión es deliberada: los estudiantes
> piden scripts pronto, la unidad es la más práctica del curso, y colocarla aquí hace que la
> comparación masiva de secuencias en U6 deje de ser una promesa y se vuelva algo que se ejecuta en
> clase. Ver `u6-arquitectura.md` §1.3.

---

## 1. Visión general de la unidad

### 1.1 Hilo conductor

**La Unidad 5 convierte un procedimiento en una herramienta.**

Al cerrar S23 el estudiante tiene algo valioso: un protocolo ejecutable que lleva de los archivos
originales de su genoma a una síntesis, con sus dependencias y sus puntos de control. Y tiene una
limitación que ya vivió en carne propia durante la evaluación individual demostrativa, cuando le tocó
un genoma que no era el suyo:

> *El protocolo funciona, pero solo si alguien lo lee, lo copia y lo pega. Y sirve para un genoma:
> para otro, hay que reescribirlo.*

La Unidad 5 se construye alrededor de una pregunta nueva:

> **¿Cómo hago que un procedimiento se ejecute solo, muchas veces, sobre datos distintos?**

De ella se desprende un conjunto pequeño y estable de preguntas:

- ¿Cómo guardo un procedimiento para que otra persona —o yo dentro de un mes— lo ejecute sin leerlo?
- ¿Cómo hago que el mismo procedimiento sirva para datos distintos?
- ¿Cómo lo aplico a doscientos casos sin escribirlo doscientas veces?
- ¿Cómo sé que hizo lo que yo creía, si ya no estoy mirando la pantalla?
- ¿Cómo dejo registro de lo que hizo, para poder repetirlo?

### 1.2 La distinción que gobierna toda la unidad

Cada unidad del curso tiene una distinción rectora. En U4 fue *un registro no es un objeto
biológico*. En U5 es esta:

```text
UN COMANDO                        UN SCRIPT
resuelve un caso                  resuelve una CLASE de casos
lleva los datos dentro            recibe los datos desde fuera
se ejecuta y se olvida            queda como archivo del proyecto
si falla, lo ves                  si falla, puede no verse
```

De ahí se sigue la frase que ordena la unidad entera:

> **Automatizar no es guardar comandos. Es separar el procedimiento de sus datos.**

Un archivo con los mismos comandos de siempre y las rutas escritas dentro no es automatización: es un
apunte ejecutable. Lo que convierte un apunte en herramienta es la **parametrización** —la frontera
entre lo que cambia y lo que permanece—, y eso es una decisión de diseño, no una construcción de
shell.

### 1.3 Cambio de paradigma respecto a la Unidad 4

| Dimensión | Unidad 4 | Unidad 5 |
| --- | --- | --- |
| Objeto de trabajo | Un archivo y sus registros | **Un procedimiento** |
| Pregunta rectora | ¿Qué contiene y cuánto mide? | ¿Cómo lo repito sin repetirme? |
| Unidad de trabajo | Una línea de comando, un resultado | Un archivo en `src/`, muchos resultados |
| Quién ejecuta | Tú, mirando cada salida | El intérprete, sin nadie mirando |
| Naturaleza del error | Puntual y visible: la salida se ve rara | **Sistemático y silencioso**: doscientos archivos mal, sin aviso |
| Qué protege del error | Que tú lo notes | Que el script lo compruebe y lo diga |
| Producto | Protocolo que una persona ejecuta | **Herramienta que se ejecuta sola** |

El punto crítico es el de la penúltima fila, y debe declararse desde S24. En U4, si una estrategia de
conteo estaba mal, el número salía raro y el estudiante lo veía. En U5 el mismo error se multiplica
por el número de iteraciones y **nadie lo mira**. Por eso la validación de entradas, los mensajes de
error y los puntos de control **no son un refinamiento final de la unidad: son su contenido**. El
Programa lo pide explícitamente, y la razón didáctica es exactamente esta.

> **IDEA CLAVE que debe aparecer en las tres sesiones.** Un script no se juzga por lo que hace cuando
> todo va bien, sino por lo que hace cuando algo falta.

### 1.4 El hilo biológico: la red de regulación de *Escherichia coli*

Automatizar por comodidad es una mala motivación didáctica: si el estudiante puede hacerlo a mano en
dos minutos, el ciclo le parecerá una ceremonia. La unidad necesita un problema donde **repetir a
mano sea sinceramente inviable**, y donde cada repetición responda una pregunta biológica real.

La **red de regulación transcripcional de *Escherichia coli* K-12** (RegulonDB, Centro de Ciencias
Genómicas, UNAM) cumple todas las condiciones:

| Condición | Cómo la cumple |
| --- | --- |
| Formato ya conocido | Es un TSV con encabezado comentado: mismo tratamiento que el GFF3 de U4, cero fricción técnica |
| Escala genuina | Del orden de **200 reguladores** y varios miles de interacciones. Nadie extrae 200 regulones a mano |
| Cada iteración es una pregunta | «¿Qué genes regula este factor?» se responde una vez por regulador |
| Produce muchos archivos | Un archivo por regulón → el procesamiento por lotes del Programa aparece solo |
| Procedencia declarable | Versión, fecha y criterio de evidencia documentados: encaja con las fichas de U3 |
| Cercanía institucional | Es un recurso del propio centro donde se imparte la licenciatura |
| Puente hacia U6 | Un regulón es un **conjunto de genes con sentido biológico**: el conjunto natural sobre el que preguntar, en U6, si están conservados en otros organismos |

Las preguntas que sostienen la unidad son biológicas, no informáticas:

- ¿Cuántos genes regula cada factor de transcripción?
- ¿Cómo se reparten los tamaños de regulón? ¿Hay unos pocos reguladores globales y muchos locales?
- ¿Qué genes están regulados por más de un factor?
- ¿Cuántas interacciones son de activación y cuántas de represión, y cambia esa proporción con el
  tamaño del regulón?

> **ADVERTENCIA — procedencia.** Antes de redactar S25 hay que **fijar el archivo exacto y su
> versión**, descargarlo a `data/source/` con su ficha (nombre, versión, fecha, URL, criterio de
> evidencia) y verificar el número de columnas y el formato del encabezado comentado. Los archivos de
> interacciones TF–gen de RegulonDB han cambiado de estructura entre versiones; el material debe
> escribirse contra el archivo que realmente se va a usar, no contra el recuerdo de uno anterior.

> **NOTA — dos objetos, un solo proyecto.** El genoma propio de U4 **no se abandona**: S24 automatiza
> el protocolo de S23 sobre él, y es lo que da continuidad. La red de regulación entra en S25, cuando
> hace falta un problema con escala. Ambos conviven en el mismo `data/source/`, cada uno con su ficha.

### 1.5 Los cuatro principios transversales, en esta unidad

- **Reproducibilidad:** aquí deja de ser una aspiración y se vuelve un archivo. Un script con sus
  parámetros y su bloque de uso **es** el registro del análisis.
- **Verificación:** cada script comprueba sus entradas antes de trabajar y avisa si algo falta. Un
  script que continúa con una entrada inexistente produce basura convincente.
- **Validación:** el resultado automatizado se contrasta contra el resultado manual conocido. La
  primera vez que se corre un script, la pregunta no es «¿funcionó?» sino «**¿da lo mismo que a
  mano?**».
- **Robustez:** se prueba con lo que no está previsto —un archivo vacío, un nombre con espacios, un
  regulador que no existe— y se decide qué debe pasar en cada caso.

### 1.6 Principios de diseño de la unidad

1. **Ninguna construcción se enseña antes de que exista la necesidad.** Las variables aparecen cuando
   editar el script cada vez se vuelve insoportable; el ciclo, cuando ejecutarlo 200 veces se vuelve
   insoportable. Es el mismo motor que U4.
2. **Ninguna sesión se llama como una construcción del lenguaje.** Se nombran por lo que resuelven:
   guardar un procedimiento, separarlo de sus datos, repetirlo sin repetirse.
3. **Nada de shell que no se use.** Se excluyen explícitamente funciones, `while`, `case`, arreglos,
   `getopts` y sustitución aritmética. Un primer semestre no necesita un lenguaje: necesita cuatro
   construcciones que domine.
4. **Todo script produce evidencia biológica interpretable.** Ningún ejercicio termina en «el script
   corrió». Terminan en un número o una lista que responde una pregunta sobre la red o el genoma.
5. **Todo script se valida contra el resultado manual.** La comparación con lo hecho a mano en U4 es
   obligatoria y es lo que se evalúa.
6. **Datos originales intactos.** Ningún script escribe en `data/source/`. Es la regla más importante
   de la unidad, porque es la primera vez que el estudiante ejecuta algo que puede destruir sin
   preguntar.

---

## 2. Propuesta de sesiones

La unidad ocupa **tres sesiones de 2 h**: **S24–S26**. Después, S27–S28 son la Unidad 6, S29 el
Examen práctico 2 (competencias D, E y F) y S30 la presentación del proyecto integrador.

```text
U5 — De un procedimiento que se lee a una herramienta que se ejecuta

S24 Guardar el procedimiento   →  ¿cómo lo ejecuto sin copiarlo?     script · intérprete · permisos
S25 Separarlo de sus datos     →  ¿cómo sirve para otro caso?        variables · parámetros · validación
S26 Repetirlo sin repetirse    →  ¿cómo lo aplico a doscientos?      ciclos · lotes · reporte
                              ↓
        Script reutilizable, con parámetros, que procesa varios archivos y produce un reporte
```

---

### S24 — Guardar el procedimiento: del comando al script

**[Plan: estructura de un script, intérprete, comentarios, permisos y ejecución · Comp. E]**

- **Propósito.** Convertir el protocolo de S23 en un archivo que se ejecuta, y entender qué hace el
  sistema cuando se le pide ejecutarlo.
- **Preguntas biológicas que responde.** Ninguna nueva: **responde otra vez las de S23, sin
  intervención humana**. Ese es exactamente el punto, y conviene decirlo. La sesión no amplía lo que
  se sabe del genoma; amplía quién puede obtenerlo y cuántas veces.
- **Conceptos nuevos.**
  - Qué es un script y en qué se diferencia de un apunte con comandos.
  - La línea `#!` y por qué el sistema necesita saber quién interpreta el archivo.
  - Comentarios: encabezado del script —qué hace, quién, cuándo, qué entradas espera—.
  - Permisos de ejecución y `chmod +x`; por qué `chmod 777` **nunca**.
  - `./script.sh` frente a `bash script.sh`, y por qué hace falta el `./`.
  - El script como archivo del proyecto: vive en `src/`, se versiona, se cita en el protocolo.
- **Herramientas nuevas.** `#!/bin/bash`, `#` como comentario, `chmod +x`, `./`, `echo`.
- **Herramientas reutilizadas.** Todo el protocolo de S23: `grep`, `cut`, `sort`, `uniq`, `sed`,
  `awk`, `comm`, redirecciones y tuberías. **No se introduce ninguna herramienta de análisis nueva en
  toda la unidad.**
- **Limitación que resuelve.** El protocolo exigía una persona que lo leyera y lo copiara. Ahora se
  ejecuta con una orden.
- **Evolución de la capacidad.** De «tengo un procedimiento documentado» a «**tengo un procedimiento
  que se ejecuta**».
- **Limitación con la que cierra (motor de S25).** Las rutas están escritas dentro del script. Para el
  genoma del equipo de al lado —el mismo caso de la evaluación individual demostrativa— hay que abrir
  el archivo y editarlo. Y editar un procedimiento cada vez que cambian los datos es justo lo que se
  quería evitar.
- **Actualización del protocolo.** El protocolo deja de contener los comandos y pasa a **citar el
  script**: qué hace, cómo se ejecuta y qué produce. Es un cambio de estatus del documento que debe
  hacerse explícito.
- **Riesgo didáctico principal.** Que la sesión se agote en mecánica de permisos. La mecánica son
  quince minutos; el resto es la idea de que un procedimiento puede ser un objeto del proyecto.

---

### S25 — Separar el procedimiento de sus datos: variables y parámetros

**[Plan: variables, expansión, sustitución de comandos y parámetros de entrada · Comp. E]**

- **Propósito.** Trazar la frontera entre lo que permanece —el procedimiento— y lo que cambia —los
  datos—, y hacer que lo segundo entre desde fuera.
- **Preguntas biológicas que responde.**
  - ¿Qué genes regula un factor de transcripción dado?
  - ¿Cuántos son, y cuántos activa frente a cuántos reprime?
  - ¿Da el mismo resultado que la extracción manual con `grep` y `cut` de U4?
- **Conceptos nuevos.**
  - Variable: asignación sin espacios alrededor de `=`; expansión `$var` y `${var}`.
  - **Comillas dobles, siempre.** Con ejemplo real: la ruta del repositorio del curso contiene un
    espacio, y sin comillas la ruta se parte en dos.
  - Sustitución de comandos `$(...)`: guardar en una variable el resultado de un comando.
  - Parámetros de entrada `$1`, `$2`, y `$#` para saber cuántos llegaron.
  - Validación mínima: `if` con `-f` —el archivo existe— y `-z` —el argumento está vacío—.
  - Mensaje de error a `>&2`, `exit 1`, y un bloque de **uso** que explique cómo se llama al script.
- **Herramientas nuevas.** Asignación, `$var`, `${var}`, `"$var"`, `$(...)`, `$1`/`$#`,
  `if`/`then`/`fi`, `-f`, `-z`, `>&2`, `exit`.
- **Objeto de trabajo.** Entra la red de regulación: un script `src/regulon.sh` que recibe el nombre
  de un regulador y produce su regulón, con el efecto de cada interacción.
- **Limitación que resuelve.** Un solo archivo sirve ahora para cualquier regulador y para cualquier
  genoma, sin tocarlo.
- **Evolución de la capacidad.** De «un procedimiento que se ejecuta» a «**una herramienta que recibe
  una pregunta**».
- **Limitación con la que cierra (motor de S26).** El script funciona para un regulador. La red tiene
  del orden de doscientos, y la pregunta interesante —*¿cómo se reparten los tamaños de regulón?*— no
  se puede responder para uno solo. Llamar al script doscientas veces a mano es el problema de S24 con
  otro disfraz.
- **Actualización del protocolo.** Ficha de procedencia de la red de regulación —versión, fecha,
  criterio de evidencia— y sección del script: qué recibe, qué produce, cómo se valida.
- **Riesgo didáctico principal.** El choque entre `$1` del shell y `$1` de `awk`, que el estudiante
  acaba de aprender en S22. Es una confusión garantizada: hay que provocarla y resolverla en clase, no
  esperar a que aparezca sola. **Dentro de comillas simples, `awk` recibe su propio `$1`; dentro de
  comillas dobles, el shell lo sustituye antes.**

---

### S26 — Repetirlo sin repetirse: ciclos, lotes y reporte

**[Plan: ciclos `for`, procesamiento por lotes, encadenamiento, nombres de salida y organización de
resultados · Comp. E]**

- **Propósito.** Aplicar el procedimiento a un conjunto completo y producir, a partir de todas las
  ejecuciones, **un resultado que ninguna de ellas contenía por separado**.
- **Preguntas biológicas que responde.**
  - ¿Cómo se reparten los tamaños de regulón en la red completa?
  - ¿Existen unos pocos reguladores globales y una mayoría de reguladores locales?
  - ¿Qué genes aparecen regulados por más de un factor?
  - ¿Cambia la proporción de activación frente a represión con el tamaño del regulón?
- **Conceptos nuevos.**
  - `for` sobre una lista literal, sobre un patrón de archivos y sobre `$(...)`.
  - Nombres de salida **derivados de la variable**, y qué pasa cuando no lo son.
  - `mkdir -p` y la organización de resultados en `results/s26/`.
  - **`>` frente a `>>` dentro de un ciclo**: el error clásico que deja un solo archivo con la última
    iteración.
  - Qué hace un patrón de archivos que no encuentra nada, y por qué el ciclo se ejecuta igual.
  - Encadenar: recorrer un conjunto, escribir un archivo por elemento y después **resumir todos** en
    una tabla —el reporte que pide el Programa—.
  - Procesamiento por lotes de varios archivos FASTA, con el mismo patrón.
- **Herramientas nuevas.** `for`/`do`/`done`, patrones de archivo (`*`), `mkdir -p`, `>>`.
- **Limitación que resuelve.** El análisis deja de depender de cuántas veces esté dispuesto a repetir
  una orden quien lo ejecuta.
- **Evolución de la capacidad.** De «una herramienta que recibe una pregunta» a «**un análisis que
  responde una pregunta sobre un conjunto completo**», y que otra persona puede reejecutar entero.
- **Limitación con la que cierra (motor de la Unidad 6).** El estudiante tiene ahora conjuntos de
  genes con sentido biológico —los regulones— y la maquinaria para procesarlos a escala. Y sigue sin
  saber **qué son** esos genes: si tienen equivalentes en otros organismos, si el regulón está
  conservado, si la función anotada es de fiar. Ninguna de esas preguntas se responde mirando los
  propios archivos: exigen comparar contra el resto de la vida.
- **Actualización del protocolo.** Sección *Análisis en lote*: qué conjunto se recorrió, qué produjo
  cada iteración, dónde quedaron los resultados y qué dice el reporte.
- **Riesgo didáctico principal.** Que el ciclo se enseñe como sintaxis. El contenido de la sesión es
  la pregunta que solo se puede responder **después** de las doscientas ejecuciones: la distribución
  de tamaños de regulón no está en ningún regulón.

---

## 2.b Relación con el ciclo de la evidencia de la Unidad 4

La Unidad 5 **no añade un verbo al ciclo**: le añade una dimensión. Los seis verbos siguen siendo los
mismos —seleccionar, identificar, normalizar, confrontar, cuantificar, integrar—, pero ahora cada uno
puede aplicarse a un conjunto en vez de a un caso.

| | Unidad 4 | Unidad 5 |
| --- | --- | --- |
| El ciclo se recorre | una vez, sobre un genoma | **muchas veces**, sobre un conjunto |
| Cada paso lo ejecuta | una persona que mira la salida | un script que comprueba y avisa |
| La integración produce | una síntesis | una síntesis **más** una distribución |

Esa última fila es el contenido conceptual de S26 y conviene que aparezca como figura: **un conjunto
de resultados individuales admite preguntas que ningún resultado individual admite**.

---

## 3. Matriz de evolución de las preguntas *(eje de diseño de la unidad)*

| # | Pregunta | Primera aparición | Estrategia inicial y su límite | Cómo se refina | Queda resuelta en |
| --- | --- | --- | --- | --- | --- |
| Q1 | ¿Cómo repito el análisis de S23? | S24 | Releer el protocolo y copiar comando por comando | **S24 · script**: un archivo que el sistema ejecuta | S24 |
| Q2 | ¿Cómo lo aplico a otro genoma? | S24 (cierre) | Abrir el script y editar las rutas | **S25 · parámetros**: el dato entra desde fuera | S25 |
| Q3 | ¿Qué genes regula este factor? | S25 | `grep` y `cut` a mano, una vez por factor | **S25 · script parametrizado**: `regulon.sh <factor>` | S25 |
| Q4 | ¿Cómo sé que el script hizo lo correcto? | S25 | Confiar en que corrió sin error | **S25 · validación de entradas** y contraste contra el resultado manual de U4 | S25, reforzado en S26 |
| Q5 | ¿Qué hago si falta el archivo o el argumento? | S25 | El script sigue y produce basura convincente | **S25 · comprobación, mensaje a `>&2` y `exit 1`** | S25 |
| Q6 | ¿Cómo lo aplico a los doscientos reguladores? | S26 | Llamarlo doscientas veces | **S26 · ciclo `for`** sobre el conjunto | S26 |
| Q7 | ¿Cómo se reparten los tamaños de regulón? | S26 | No se podía preguntar: hacía falta el conjunto entero | **S26 · reporte** que resume todas las iteraciones | S26 |
| Q8 | ¿Dónde quedan doscientos archivos de salida? | S26 | En el directorio de trabajo, mezclados | **S26 · nombres derivados de la variable y `results/s26/`** | S26 |
| Q9 | ¿Qué son estos genes y existen en otros organismos? | S26 (cierre) | No se puede responder desde los archivos propios | **Unidad 6 · comparación de secuencias** | U6 |

> **Criterio de diseño.** Q7 es la pregunta más importante de la unidad: es la única que **no existía
> antes** del ciclo. Si el material no la hace visible, el `for` quedará como una comodidad y no como
> un cambio en lo que se puede preguntar.

---

## 4. Evidencia integradora

El producto es el que fija el Programa: **un script reutilizable que reciba parámetros, procese varios
archivos biológicos, produzca un reporte y deje registro suficiente para repetir el análisis**.

| Sesión | Qué aporta al producto | Archivo |
| --- | --- | --- |
| S24 | El procedimiento, ejecutable y comentado | `src/analizar-genoma.sh` |
| S25 | La parametrización y la validación de entradas | `src/regulon.sh` |
| S26 | El recorrido del conjunto y el reporte | `src/reporte-regulones.sh` + `results/s26/` |

**Criterios de la rúbrica**, derivados de los principios de §1.5 y del propio Programa:

| Criterio | Qué se comprueba |
| --- | --- |
| Recibe parámetros | El script no contiene ninguna ruta ni ningún identificador fijo que debiera venir de fuera |
| Valida las entradas | Comprueba lo que necesita, avisa por `>&2` y termina con un código distinto de cero |
| Documenta su uso | Encabezado con propósito, entradas, salidas y una línea de ejemplo de invocación |
| Procesa un conjunto | Recorre varios archivos u objetos y deja una salida por cada uno, con nombre derivado |
| Produce un reporte | Una tabla que resume todas las iteraciones y responde una pregunta biológica |
| Es verificable | Se compara contra el resultado manual conocido y el material declara la coincidencia |
| Respeta los originales | No escribe en `data/source/` |
| Deja registro | El protocolo cita el script, sus parámetros y la fecha de ejecución |

---

## 5. Alcance, delimitaciones y discrepancias

### 5.1 Cobertura del alcance oficial

| Contenido del Programa | Sesión |
| --- | --- |
| Estructura de un script, intérprete, comentarios, permisos y ejecución | S24 |
| Variables, expansión, sustitución de comandos | S25 |
| Parámetros de entrada | S25 |
| Ciclos `for` y procesamiento por lotes | S26 |
| Encadenamiento de tareas, nombres de salida y organización de resultados | S26 |
| Automatización de múltiples archivos FASTA y reportes simples | S26 |
| Validación de entradas y salidas, mensajes de error | S25 (entradas), S26 (salidas) |
| Documentación mínima de uso | S24 (encabezado), S25 (bloque de uso) |
| **Evidencia integradora: script reutilizable con reporte** | S26 (iniciada en S24) |

### 5.2 Delimitación: lo que esta unidad NO enseña

La lista es tan importante como la anterior, porque el riesgo de esta unidad es convertirse en un
curso de programación.

**Excluido explícitamente:** funciones definidas por el usuario; `while` y `until`; `case`; arreglos y
arreglos asociativos; `getopts`; sustitución aritmética `$((...))`; expresiones regulares dentro de
`[[ ]]`; `set -euo pipefail`; `trap`; procesos en segundo plano y paralelismo; `xargs`; scripts de
Python o R.

**Criterio:** cuatro construcciones bien dominadas —variable, parámetro, condición simple y ciclo—
bastan para todo lo que pide el Programa. Una quinta construcción que no se use en ningún ejercicio es
contenido muerto.

> **NOTA — `set -e`.** Es tentador incluirlo como buena práctica. Se deja fuera a propósito: su
> comportamiento con tuberías y con condiciones tiene excepciones que un primer semestre no puede
> distinguir, y da una falsa sensación de seguridad. La comprobación explícita con `if` enseña más y
> engaña menos.

### 5.3 Discrepancias con el Plan operativo

| # | Plan de clases | Esta arquitectura | Estado |
| --- | --- | --- | --- |
| **D1** | S24 «Alineamientos», S25 «BLAST, variables y scripts», S26 «Homología y ciclos»: sesiones **compartidas** entre las dos unidades | Se separan en **bloques limpios**: U5 ocupa S24–S26 completas y U6 ocupa S27–S28. Ninguna sesión sirve a dos hilos | **Decisión docente (ago-2026).** Motivo: los estudiantes piden scripting pronto, y la unidad gana con tres sesiones seguidas de práctica |
| **D2** | S27–S28: «Semana de práctica: automatización de un pipeline» | La práctica de automatización se absorbe en S26 y en el trabajo en lote de S28. S27–S28 pasan a ser la Unidad 6 | Consecuencia de D1 |
| **D3** | S23 introduce «parámetros de entrada en scripts» | La arquitectura de U4 ya pospuso esa siembra. Con este orden, **S25 es su lugar natural**, justo después de que S24 haya creado la necesidad | **Resuelto.** Coherente con lo decidido en U4 |
| **D4** | El cierre de S23 anuncia la automatización como la siguiente unidad | **Correcto tal como está.** La renumeración que se consideró y se descartó lo habría roto; con este orden no hay nada que ajustar | **Sin acción** |
| **D5** | La Tarea 8 del Plan es «BLAST automatizado con un script», asociada a S25 | Con bloques limpios, esa tarea pasa a **S28**, donde el script y BLAST ya coexisten. La tarea de S26 es el reporte de regulones | Propuesta; requiere visto bueno |
| **D6** | El Plan no contempla la red de regulación como fuente de datos | Se incorpora en S25–S26 como segunda entrada del proyecto, con su ficha de procedencia (§1.4) | Propuesta; requiere fijar archivo y versión |

### 5.4 Riesgos técnicos que el material debe prevenir

Todos verificados en un shell real. Cada uno debe tener su lugar y, preferiblemente, **provocarse
antes de explicarse**.

| Riesgo | Qué ocurre | Dónde se previene |
| --- | --- | --- |
| Variable sin comillas y ruta con espacios | La ruta se parte: `ls: cannot access 'Mi'` | **S25**, con la ruta real del repositorio del curso, que contiene un espacio |
| `var = valor` con espacios alrededor del `=` | `command not found`: el shell lee `var` como una orden | S25 |
| `>` dentro de un ciclo | Solo sobrevive la **última** iteración; las 199 anteriores se pierden en silencio | **S26**, provocado antes de explicarlo |
| Nombre de salida que no depende de la variable | Doscientas iteraciones, un solo archivo | S26 |
| Patrón de archivos sin coincidencias | El ciclo se ejecuta **una vez**, con el patrón literal como valor | S26 |
| `$1` del shell frente a `$1` de `awk` | Comillas simples: `awk` recibe el suyo. Comillas dobles: el shell lo sustituye antes | **S25**, como trampa central |
| `chmod 777` | Permiso de escritura para todo el mundo sobre un archivo ejecutable | S24 |
| Línea `#!` con retorno de carro (archivo editado en Windows) | `bad interpreter: No such file or directory`, sin más pista | S24, como error frecuente |
| Ejecutar sin `./` | `command not found` aunque el archivo esté ahí | S24 |
| Un script que escribe en `data/source/` | Destruye el original sin preguntar. Es irreversible | **S24 y S26**, como regla no negociable |
| Confiar en que «corrió sin error» | Un script puede terminar con éxito y no haber hecho nada | S25 (validación) y S26 (contraste con el resultado manual) |

---

## 6. Verificación de esta arquitectura

- [ ] Cada sesión cierra con una limitación concreta que la siguiente resuelve, y S26 abre la Unidad 6.
- [ ] Ninguna sesión se titula con el nombre de una construcción del lenguaje.
- [ ] Ninguna construcción de la lista de exclusiones (§5.2) aparece en ningún ejercicio.
- [ ] **Ninguna herramienta de análisis nueva**: todo viene de U1–U4.
- [ ] Cada ejercicio termina en un número o una lista que responde una pregunta biológica.
- [ ] Todo script se contrasta contra el resultado manual conocido.
- [ ] Ningún script escribe en `data/source/`.
- [ ] La distinción **un comando resuelve un caso / un script resuelve una clase de casos** aparece en
      las tres sesiones.
- [ ] El error silencioso y multiplicado (§1.3) se declara en S24 y se combate en S25 y S26.
- [ ] Q7 —la pregunta que solo existe después del ciclo— es visible como tal en S26.
- [ ] La ficha de procedencia de la red de regulación está hecha y verificada contra el archivo real.
- [ ] Español claro para primer semestre; glosario español–inglés en cada módulo.
- [ ] Toda buena práctica y toda definición citan su fuente.

---

## 7. Archivos de la unidad

| Sesión | Archivo previsto | Tema del nombre |
| --- | --- | --- |
| — (portada) | `u5-automatizacion-scripting.md` | Portada de la unidad |
| S24 | `u5-s24-del-comando-al-script.md` | Guardar un procedimiento ejecutable |
| S25 | `u5-s25-separar-procedimiento-datos.md` | Variables, parámetros y validación |
| S26 | `u5-s26-repetir-sin-repetirse.md` | Ciclos, lotes y reporte |
| — (docente) | `u5-arquitectura.md` | Este documento |

Scripts que el estudiante produce, en `src/`:

| Archivo | Sesión | Qué hace |
| --- | --- | --- |
| `analizar-genoma.sh` | S24 | Ejecuta el protocolo de S23 completo |
| `regulon.sh` | S25 | Recibe un regulador y produce su regulón |
| `reporte-regulones.sh` | S26 | Recorre la red y produce la tabla resumen |

Figuras previstas, en el estilo SVG del curso (paleta y tipografía de U4):

| Figura | Contenido | Sesión |
| --- | --- | --- |
| 24.1 | Un apunte con comandos frente a un script: qué añade el archivo ejecutable | S24 |
| 24.2 | Qué hace el sistema al ejecutar un script: la línea `#!`, los permisos y el `./` | S24 |
| 25.1 | La frontera del script: qué permanece dentro y qué entra desde fuera | S25 |
| 25.2 | Un script que valida frente a uno que confía: dos caminos ante una entrada que falta | S25 |
| 26.1 | Una iteración, doscientas iteraciones y la pregunta que solo admite el conjunto | S26 |
| 26.2 | `>` frente a `>>` dentro de un ciclo: doscientos resultados o uno | S26 |

---

## 8. Siguiente paso

1. **Visto bueno de las discrepancias** D1 a D6, en especial la separación en bloques limpios (D1) y
   la incorporación de la red de regulación (D6).
2. **Fijar el archivo de RegulonDB**: versión, fecha, URL, criterio de evidencia y estructura real de
   columnas. Descargarlo a `data/source/` con su ficha y verificar el formato **antes** de redactar
   S25 (§1.4).
3. **Decidir la Tarea 8** (D5): confirmar que «BLAST automatizado con un script» se mueve a S28 y que
   la tarea de S26 es el reporte de regulones.
4. **Redactar S24**, verificar contra la checklist de §6 y solo entonces continuar con S25 y S26.

---

## Fuentes

- RegulonDB, Centro de Ciencias Genómicas, UNAM — conjuntos de datos de interacciones TF–gen:
  [regulondb.ccg.unam.mx · descargas](http://regulondb.ccg.unam.mx/menu/download/datasets/)
- Santos-Zavaleta, A. *et al.* «Using RegulonDB, the *Escherichia coli* K-12 Gene Regulatory
  Transcriptional Network Database»: [PubMed 30040192](https://pubmed.ncbi.nlm.nih.gov/30040192/)
- Gama-Castro, S. *et al.* «RegulonDB version 9.0: high-level integration of gene regulation,
  coexpression, motif clustering and beyond», *Nucleic Acids Research*:
  [academic.oup.com/nar/article/44/D1/D133](https://academic.oup.com/nar/article/44/D1/D133/2502650)
