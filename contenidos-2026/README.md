# Contenidos 2026 --- Introducción a la Bioinformática

Esta carpeta contiene el **contenido didáctico nuevo** del curso,
redactado en Markdown limpio. El material está pensado como **lectura
previa** para un modelo de aula invertida y debe ser **autocontenido**:
define los conceptos necesarios, explica para qué se usan y prepara al
estudiante para el taller. El formateo final en Quarto (`.qmd`,
callouts, temas y navegación) se realizará en una fase posterior.

Los materiales de `../introBioInfo/` y `../introBioInfo/referencias/` se
usan como **referencia**.

> **Nota técnica --- datos y ejemplos de las lecciones.** Todos los datos
> y ejemplos que utilizan las lecciones viven en [`ejemplos/`](ejemplos/)
> y se enlazan con rutas relativas. Ninguna lección debe referirse a un
> dato que resida fuera de esta carpeta: si una sesión nueva necesita
> datos, se depositan aquí antes de redactarla.
>
> Contenido actual: [`datos-alineamientos/`](ejemplos/datos-alineamientos/)
> (31 archivos de secuencia de U6), `pacientes.md` y
> `metadatos_pacientes.md` (datos sintéticos de U1),
> `formato_protocolo_v1.0.md` y `ReporteGenomeEcoli_Formato_v2.md`
> (plantillas del protocolo y del reporte) y
> `s34-casos-secuencia-desconocida.zip` (casos ciegos de S34).
>
> Queda pendiente de copiar, al publicar en Quarto,
> `referencias/bioinformatics-data-skills.pdf`, que todavía vive en
> `../introBioInfo/`; al migrar debe copiarse a la carpeta de recursos
> del sitio y actualizarse su ruta.

## Identidad del curso

Este **no** es un curso de Unix ni un curso de comandos. Es un curso de
**Introducción a la Bioinformática**: las herramientas computacionales
aparecen únicamente como medios para responder preguntas biológicas.

De ahí se sigue el principio que ordena todo el material:

> **Las preguntas biológicas permanecen; las estrategias de análisis
> evolucionan.**

Consecuencias editoriales directas:

-   Ninguna sesión se titula con el nombre de un comando; se titula con
    la **etapa del análisis** que representa.
-   Ningún resultado de aprendizaje se formula como "usar la herramienta
    X", sino como lo que la herramienta permite **averiguar, contrastar
    o justificar**.
-   Ninguna actividad termina en una salida de terminal: termina en una
    **interpretación biológica** sostenida por la evidencia obtenida.

### Convención de títulos y encabezados

El título canónico de una sesión es:

``` markdown
# S22 — Condicionar y calcular: expresar preguntas complejas sobre columnas
```

Reglas:

-   usar `S<NN> — Verbo de acción: descripción`;
-   el verbo expresa la **operación intelectual** de la sesión, no el
    nombre de una herramienta;
-   cada archivo de sesión tiene **un solo H1 real**;
-   cualquier `#` que pertenezca a un script, *shebang*, plantilla o
    ejemplo debe quedar dentro de un bloque de código cercado para que
    no se interprete como encabezado Markdown.

## Principios de diseño didáctico

-   Cada **módulo o sesión de dos horas** combina preparación previa,
    práctica presencial y una evidencia posterior corregida.
-   Los conceptos se presentan antes que los comandos o herramientas que
    los implementan.
-   **La capacidad analítica crece; las preguntas no cambian.** Una
    misma pregunta biológica puede revisitarse varias veces a lo largo
    de una unidad. No se trata de repetir un ejercicio, sino de producir
    una respuesta **más precisa, mejor fundamentada, más reproducible o
    con evidencia de mayor calidad** que la anterior. Cada regreso a una
    pregunta debe declarar explícitamente qué limitación de la
    estrategia previa corrige.
-   **Ninguna herramienta se introduce porque "toca verla".** Cada una
    aparece porque resuelve una **limitación observada** en la
    estrategia anterior, y esa limitación debe haberse hecho evidente
    antes ---idealmente, el estudiante la habrá encontrado por sí
    mismo---. El orden de las herramientas lo dicta la secuencia en que
    aparecen los obstáculos, no la estructura del temario.
-   **Distinguir el dato de la operación.** Toda práctica debe ayudar a
    separar cuatro cosas, siempre en este orden: la **pregunta
    biológica** → el **dato** que la responde → la **operación** que hay
    que hacer sobre ese dato → la **herramienta** que ejecuta esa
    operación. Nunca se empieza por el comando. Muchas preguntas
    fracasan no porque falte el dato, sino porque falta la operación
    ---y a veces esa operación aún no está al alcance del estudiante:
    reconocerlo también es un resultado.
-   Las prácticas son **progresivas e intercaladas**: cada una recupera
    y amplía habilidades, decisiones o productos de las prácticas
    anteriores. La complejidad y la autonomía aumentan gradualmente,
    evitando ejercicios aislados o repeticiones sin propósito. Cada
    práctica se coloca **después del concepto crítico correspondiente**,
    no se acumula al final y contribuye al producto acumulativo del
    curso. Esa progresión se construye como una escalera: cada actividad
    **recupera** un resultado anterior, lo **compara**, lo **refina** y
    **documenta qué mejoró**. Una práctica que podría ejecutarse sin
    haber hecho las anteriores está mal diseñada.
-   **El protocolo no es un entregable: es el registro del razonamiento
    científico.** `protocolo.md` crece sesión tras sesión y **nunca se
    reinicia**. Cada sesión añade o corrige **solo** el apartado que le
    corresponde, y conserva las versiones anteriores de una respuesta
    cuando la mejora: la comparación entre ambas es la evidencia de
    aprendizaje más valiosa del curso. Un apartado de *limitaciones*
    honesto vale más que un resultado presentado como definitivo.
-   `protocolo.md`, los metadatos del proyecto y `bitacora-ia.md` son
    **documentos vivos**: se amplían y corrigen entre sesiones y
    unidades.
-   La estructura de proyecto usada de manera consistente es:

``` text
proyecto/
├── data/
│   ├── source/
│   └── processed/
├── src/
├── results/
└── doc/
```

Los datos originales se conservan sin modificaciones en `data/source/`.

## Uso crítico de IA como eje transversal

La IA se incorpora cuando permite **comparar, revisar o mejorar** una
actividad realizada previamente por el estudiante. Se aplica la regla
**primero a mano, después con IA**. El primer intento manual constituye
una **línea base de comparación**, no una verdad absoluta: tanto el
trabajo manual como la respuesta de IA deben contrastarse con el
material del curso, documentación autorizada, pruebas controladas y
evidencia independiente.

La actividad de IA puede colocarse al final de una sesión, al cierre de
una unidad o como trabajo posterior, según el tiempo disponible y el
resultado de aprendizaje. **No es obligatorio** forzar un "cierre con
IA" idéntico en cada unidad, ni darle siempre la misma estructura: se
incluye donde aporte una comparación real con trabajo ya hecho a mano.
Esta regla prevalece sobre cualquier formulación anterior que exigiera
una sección fija por unidad.

### Asistente de Unix y bioinformática del curso

El curso dispone de [**ProfeUnix
Bioinfo**](https://chatgpt.com/g/g-6893cf2451d88191b11cd0c87de045ab-profeunix-bioinfo),
un GPT que puede utilizarse como recurso de consulta y revisión en las
actividades que lo indiquen. El enlace canónico se presenta al alumnado
en la Unidad 1; las lecciones posteriores pueden remitir a él sin
repetir toda la política de IA.

Su uso debe ser **intencional, ocasional y verificable**: conviene
solicitarlo cuando aporte una comparación pedagógica concreta ---por
ejemplo, revisar permisos, diagnosticar un comando o detectar la mezcla
entre dos planificadores---, no añadirlo automáticamente a todas las
sesiones. Cuando una actividad pida utilizarlo, debe conservar la regla
**primero a mano, después con IA**, exigir validación independiente y
registrar el uso en `bitacora-ia.md`.

El acceso a los GPT personalizados puede depender de la cuenta o de las
condiciones vigentes de la plataforma. Por ello, ninguna evidencia debe
depender exclusivamente de abrir este recurso: si un estudiante no tiene
acceso, podrá realizar la misma revisión con otro asistente autorizado e
indicar en la bitácora cuál utilizó.

Reglas de uso responsable:

-   La IA no sustituye la ejecución de habilidades básicas que el módulo
    busca desarrollar.
-   No se comparten credenciales, datos sensibles, direcciones
    institucionales privadas, llaves, tokens ni información que
    identifique a una persona.
-   No se ejecutan comandos sugeridos sin comprenderlos, revisar sus
    efectos y probarlos, cuando corresponda, en archivos o directorios
    de prueba.
-   Todo uso relevante se registra en `bitacora-ia.md`: objetivo,
    herramienta, prompt, respuesta o resumen, verificación
    independiente, correcciones y decisión final.

## Estructura editorial común de cada módulo

Cada módulo sigue esta secuencia general, adaptada al contenido y sin
duplicar secciones que no aporten valor:

1.  Título y número de sesión.
2.  Nota de aula invertida: antes, durante y después de clase. Va como
    **callout inicial**, no como encabezado (ver más abajo).
3.  Ficha del módulo.
4.  Relación con unidades anteriores y con el caso bioinformático.
5.  Resultados de aprendizaje observables.
6.  Preparación previa o *preflight*.
7.  Bloques conceptuales esenciales.
8.  Prácticas progresivas e intercaladas después de cada concepto
    crítico; cada una retoma y amplía lo desarrollado anteriormente.
9.  Cierre que actualice un producto acumulativo, preferentemente
    `protocolo.md`.
10. Evidencia de aprendizaje.
11. Errores frecuentes y estrategias de diagnóstico.
12. Criterios de logro o rúbrica breve.
13. Autoevaluación o semáforo de salida.
14. Distribución estimada de las dos horas.
15. Anexos: **Anexo A**, correspondencia
    resultado--actividad--evidencia--criterio--momento--nivel; y **Anexo
    B**, alineación transversal con columnas reproducibilidad /
    verificación / validación / robustez.
16. Glosario y referencias específicas.

Para la navegación del estudiante se mantienen nombres de encabezado
consistentes: `## Ficha del módulo`, `## Resultados de aprendizaje`,
`## Evidencia de la sesión`, `## Errores frecuentes y estrategias de
diagnóstico`, `## Rúbricas`, `## Autoevaluación`, `## Distribución
estimada de las dos horas`, `## Anexo A`, `## Anexo B`, `## Glosario` y
`## Referencias`. No se crea una sección vacía únicamente para
satisfacer la plantilla.

La **nota de aula invertida** es la excepción: no lleva encabezado
propio. Se escribe como callout inmediatamente después del título, donde
se lee antes que nada y sin ocupar una entrada del índice:

``` markdown
# S6 — Consolidar: el entorno Unix listo para datos biológicos

> **NOTA — Aula invertida.** Este documento se lee antes de la sesión…
```

### Material transversal: prácticas integradoras y evaluaciones

Las sesiones que **no son módulos de contenido** ---la semana de práctica
integradora, la revisión por pares y las evaluaciones individuales--- no
siguen la estructura anterior y **no deben forzarse a ella**: no
introducen conceptos ni herramientas, así que no llevan bloques
conceptuales, prácticas intercaladas, glosario, anexos de alineación ni
distribución de las dos horas.

Su estructura propia es más corta:

1.  Título y número de sesión, con la misma convención
    `S<NN> — Verbo de acción: descripción`.
2.  Encuadre breve: qué integra y de qué sesiones proviene.
3.  Ficha de la actividad: sesión, modalidad (individual o en equipo),
    insumo, producto y peso en la evaluación.
4.  Qué se da por sabido: las sesiones cuyo resultado se pone en juego.
5.  Desarrollo, por fases o bloques.
6.  Entregables.
7.  Criterios de evaluación y **rúbricas** ---son documentos evaluables,
    y esto no es opcional.
8.  Cierre: qué se lleva el estudiante a la sesión siguiente.

Lo que sí comparten con los módulos: un solo H1, la convención de
títulos, los marcadores de lectura, el formato de figuras y la coherencia
con la pestaña vigente del Plan de clases.

Los comandos se clasifican, cuando sea útil, como **esenciales**, **de
consulta** o **de ampliación**.

### Retroalimentación de las prácticas

No toda pregunta merece el mismo tratamiento. Se aplican **tres niveles**,
y elegir el que corresponde es parte del trabajo editorial:

1.  **Respuesta directa → bloque colapsable.** Solo cuando la respuesta
    es la misma para todo el mundo: cadenas de prueba dadas en el
    enunciado, salidas deterministas, comportamientos del sistema. La
    etiqueta canónica es **Ver retroalimentación**. Conviene decir en la
    primera línea por qué la respuesta es exacta ("las cinco cadenas de
    prueba son las mismas para todo el mundo").
2.  **Respuesta que depende de los datos → `> **TIP:**` visible.** Cuando
    la cifra o el resultado varían según el genoma, el ensamblado o quien
    anotó, **no se inventa un número**. Se orienta: qué es esperable, qué
    hacer si no cuadra, y con qué **no** compararse. Va visible, no
    oculto: es una guía, no una solución.
3.  **Trabajo de rastreo o elaboración propia → nada.** Si responder
    exige que el estudiante investigue, decida o construya, no se añade
    ni colapsable ni tip. Adelantar la respuesta destruiría el ejercicio,
    y muy especialmente en los primeros intentos, cuyo valor está en
    comprometerse con una respuesta **antes** de conocer la herramienta
    que la formaliza.

Formato del colapsable:

``` html
<details>
<summary>Ver retroalimentación</summary>

Contenido que se muestra al desplegar el bloque.

</details>
```

## Guía de estilo para facilitar el paso a Quarto

### Lenguaje

El vocabulario debe situar el análisis en primer plano y la herramienta
en segundo. Siempre que sea natural, se prefieren expresiones como
**construir evidencia**, **localizar el dato**, **refinar una
respuesta**, **contrastar resultados**, **justificar una
interpretación**, **fortalecer una conclusión** y **documentar la
estrategia**, frente a formulaciones centradas en "usar un comando".

Esto no implica ocultar las herramientas: los comandos se nombran con
precisión y aparecen en todos los bloques de código. Implica que el
texto que los rodea explique **qué se averigua**, no solo qué se
ejecuta.

Términos que conviene usar de forma consistente en todo el material:
*pregunta biológica, dato, operación, evidencia, estrategia,
interpretación, refinamiento, limitación, respuesta provisional,
medición, estimación, protocolo*. Se evitan los sinónimos que
introduzcan matices no deseados.

### Marcadores de lectura

Los marcadores canónicos son:

``` text
[Indispensable]
[Consulta]
```

Se escriben **sin negritas añadidas**. `[Indispensable]` identifica lo
necesario para llegar preparado al taller; `[Consulta]` identifica
ampliaciones o material de referencia.

### Callouts

Se escriben como cita (`>`) con una etiqueta en mayúsculas y negrita.
Mapean directamente a callouts de Quarto durante la fase de formateo:

  Marcador en el contenido   Callout de Quarto
  -------------------------- -------------------------------------------
  `> **NOTA:** …`            `::: {.callout-note}`
  `> **IMPORTANTE:** …`      `::: {.callout-important}`
  `> **TIP:** …`             `::: {.callout-tip}`
  `> **¿SABÍAS QUE?:** …`    `::: {.callout-tip title="¿Sabías que?"}`
  `> **COMENTARIO:** …`      `::: {.callout-tip}`
  `> **ADVERTENCIA:** …`     `::: {.callout-warning}`

Los callouts se usan **con moderación**: no toda observación merece uno.
Como referencia práctica, conviene no superar unos pocos por sección y
reservarlos para lo que el estudiante no debe pasar por alto ---un
riesgo real, una regla que evita un error silencioso, una distinción
conceptual crítica---. Si al revisar una sesión los callouts ocupan más
espacio que el texto corrido, sobran callouts.

### Figuras terminadas

Las figuras listas para publicación se guardan en [`images/`](images/) y
se insertan exactamente en el punto donde apoyan el aprendizaje. Se usa
PNG para publicación y se conserva el SVG editable cuando exista.

#### Nombre de archivo

La convención canónica es:

``` text
figura-u<N>-s<NN>-<slug>.png
```

Por ejemplo:

``` text
figura-u6-s33-especiacion-vs-duplicacion.png
```

Se usan minúsculas, guiones y caracteres ASCII; no espacios, sufijos
accidentales ni guiones bajos.

#### Imagen, numeración y pie

La **imagen misma no contiene**:

-   `Figura NN.M`;
-   numeración editorial;
-   el pie de figura.

La numeración y el pie viven exclusivamente en Markdown:

``` markdown
![Dos ramas muestran que la especiación separa genes ortólogos entre especies, mientras una
duplicación genera copias parálogas dentro de un linaje.](images/figura-u6-s33-especiacion-vs-duplicacion.png)

**Figura 33.4.** La especiación y la duplicación generan relaciones evolutivas distintas.
```

El texto alternativo debe comunicar la **idea o relación que aporta la
figura**, no limitarse a describir su apariencia ni repetir literalmente
el pie. Debe ser suficientemente informativo para comprender el
propósito visual si la imagen no se muestra.

Una figura puede reutilizarse cuando la idea es realmente la misma; en
ese caso se indica en el texto que se recupera una figura anterior. No
se duplica el mismo recurso con otro nombre para aparentar una figura
distinta.

Las figuras que dejan de usarse **no se borran**: se mueven a
[`images/archivadas/`](images/archivadas/), cuyo README registra por qué
salieron y, si procede, qué figura las sustituyó. Los insumos de los que
se derivan otras figuras ---capturas de pantalla, másteres
autocontenidos--- viven en `images/fuentes/`. Ninguna sesión referencia
archivos de esas dos carpetas.

Antes de publicar, se comprueba que la figura coincida con el texto, use
la convención `data/source/` cuando represente el proyecto y no contenga
estados, comandos, rutas o conceptos incorrectos. No deben quedar
marcadores editoriales como "FIGURA SUGERIDA" o "Crear figura".

### Código, prácticas y referencias

-   Los bloques de código siempre declaran el lenguaje (`bash`,
    `markdown`, `text`, etc.) y se anuncian en el texto.
-   Cada práctica incluye pasos explícitos, producto esperado, momento
    de trabajo y criterio de logro.
-   Las prácticas se leen antes de clase pero se **navegan** durante el
    taller. Cuando una práctica tenga muchos pasos, conviene marcarlos
    con una etiqueta breve en negrita al inicio del paso ---*Predice,
    Localiza, Comprueba, Contrasta, Interpreta, Documenta*--- para que
    puedan localizarse de un vistazo. Se evitan los bloques de texto
    largos: si una idea ocupa más de cuatro o cinco líneas seguidas,
    normalmente admite dividirse o convertirse en lista.
-   Las referencias se citan en línea como `(Autor, año, cap./p.)` y se
    desarrollan al final del módulo. Toda definición, afirmación
    relevante y buena práctica debe estar respaldada por una fuente
    verificable; no se inventan referencias.
-   Se conservan las etiquetas **\[Nuevo\]**, **\[Reforzado\]** e
    **\[Integración\]** del Programa 2026.

## Índice de contenidos

### Unidad 1 --- Trabajo reproducible y comunicación técnica

-   [`u1-trabajo-reproducible.md`](u1-trabajo-reproducible.md): portada de
    la unidad --- ficha, ruta S1--S2, cierre de unidad con quiz y reto
    final, anexos y glosario.
-   [`u1-s1-documentar-markdown-fases.md`](u1-s1-documentar-markdown-fases.md):
    bioinformática y reproducibilidad, fases del análisis y de
    resolución, de la pregunta biológica a la estrategia, el protocolo y
    Markdown. Desarrolla la **Tarea 1**.
-   [`u1-s2-organizar-fair-ia.md`](u1-s2-organizar-fair-ia.md): principios
    FAIR, ficha de metadatos, organización reproducible del proyecto y
    cápsula de uso crítico de IA. Desarrolla la **Tarea 2**.

**Unidad de referencia (estándar de oro)** para generar las demás.

Hasta agosto de 2026, S1 y S2 compartían un archivo
(`u1-s1-s2-trabajo-reproducible-v3.md`): U1 era la única unidad sin
portada y sin un documento por sesión. Se dividió siguiendo las **Tareas
del plan** ---la Tarea 1 define S1 y la Tarea 2 define S2---, lo que
obligó a partir dos secciones: los principios FAIR y la ficha de
metadatos pasaron a S2, mientras las fases del análisis y el protocolo se
quedaron en S1. La versión previa se conserva íntegra, sin publicar, en
[`docente/u1-s1-s2-trabajo-reproducible-v3-ORIGINAL.md`](docente/u1-s1-s2-trabajo-reproducible-v3-ORIGINAL.md).

### Unidad 2 --- Entorno Unix/Linux y cómputo científico

-   [`u2-entorno-unix.md`](u2-entorno-unix.md): portada de la unidad,
    ruta S3--S6, producto acumulativo y cierre de la unidad.
-   [`u2-s3-shell-acceso-remoto.md`](u2-s3-shell-acceso-remoto.md):
    shell, ayuda, protocolos, SSH y transferencia con verificación de
    integridad.
-   [`u2-s4-sistema-archivos.md`](u2-s4-sistema-archivos.md):
    sistema de archivos, rutas, navegación y operaciones seguras.
-   [`u2-s5-archivos-permisos-procesos.md`](u2-s5-archivos-permisos-procesos.md):
    archivos, compresión, permisos y procesos.
-   [`u2-s6-consolidacion-entorno-unix.md`](u2-s6-consolidacion-entorno-unix.md):
    verificación del entorno, integridad de los originales, permiso
    mínimo, revisión por pares y preparación para datos reales.

La Unidad 2 comprende **S3--S6**. S3--S5 desarrollan el entorno
Unix/Linux y S6 cierra la unidad sin duplicar el trabajo de HPC/SGE que,
en la arquitectura vigente, se desarrolla en **S29**.

La portada anterior, `u2-entorno-unix-hpc.md`, cumplía a la vez de
portada de U2 y de material de cluster. Su contenido de HPC/SGE se
trasladó a [`u5-s29-cluster-hpc-sge.md`](u5-s29-cluster-hpc-sge.md)
---en U2 era demasiado pronto para hablar de cómputo distribuido--- y su
función de portada se recuperó en `u2-entorno-unix.md`, ya sin `-hpc` en
el nombre. **S6 ya está redactada** en
[`u2-s6-consolidacion-entorno-unix.md`](u2-s6-consolidacion-entorno-unix.md),
como sesión de verificación y cierre, sin contenido de cluster.

### Unidad 3 --- Datos y bases de datos biológicas

-   [`u3-datos-bases-datos.md`](u3-datos-bases-datos.md): portada de la
    unidad, ruta S7--S9 y evidencias acumuladas.
-   [`u3-s7-secuencias-formatos-genbank.md`](u3-s7-secuencias-formatos-genbank.md):
    dogma central, formatos FASTA/GenBank/GFF3 y anatomía de un
    registro.
-   [`u3-s8-bases-datos-descarga-integridad.md`](u3-s8-bases-datos-descarga-integridad.md):
    recuperación de datos, procedencia y verificación de integridad.
-   [`u3-s9-inspeccion-transferencia-verificable.md`](u3-s9-inspeccion-transferencia-verificable.md):
    inspección de archivos y transferencia verificable.

### Unidad 4 --- Procesamiento y exploración de datos genómicos

Una investigación sobre un genoma, en diez sesiones: **S10--S13**
(establecer los hechos) y **S18--S23** (el ciclo de la evidencia).

-   [`u4-procesamiento-exploracion.md`](u4-procesamiento-exploracion.md):
    portada de la unidad.
-   [`u4-s10-anatomia-flujos-datos.md`](u4-s10-anatomia-flujos-datos.md):
    anatomía del archivo biológico, redirecciones y tuberías.
-   [`u4-s11-estructura-tabular-anotacion.md`](u4-s11-estructura-tabular-anotacion.md):
    estructura tabular de la anotación y coordenadas.
-   [`u4-s12-filtrado-conteos-genoma.md`](u4-s12-filtrado-conteos-genoma.md):
    filtrado y primeros conteos.
-   [`u4-s13-inventario-resumen-genoma.md`](u4-s13-inventario-resumen-genoma.md):
    inventario y resumen del genoma.
-   [`u4-s18-precision-patrones-expresiones-regulares.md`](u4-s18-precision-patrones-expresiones-regulares.md):
    precisión de los patrones.
-   [`u4-s19-extraccion-identificadores-correspondencia.md`](u4-s19-extraccion-identificadores-correspondencia.md):
    extracción de identificadores y correspondencia entre archivos.
-   [`u4-s20-normalizar-datos-comparables.md`](u4-s20-normalizar-datos-comparables.md):
    normalización y datos derivados.
-   [`u4-s21-confrontar-fuente-independiente.md`](u4-s21-confrontar-fuente-independiente.md):
    contraste con una fuente independiente.
-   [`u4-s22-condicionar-calcular-columnas.md`](u4-s22-condicionar-calcular-columnas.md):
    análisis condicionado y medidas derivadas.
-   [`u4-s23-protocolo-ejecutable-genoma.md`](u4-s23-protocolo-ejecutable-genoma.md):
    el protocolo como cuaderno de laboratorio ejecutable.

### Unidad 5 --- Automatización de análisis bioinformáticos con Shell

De un procedimiento que se lee a una herramienta que se ejecuta:
**S24--S29**.

-   [`u5-automatizacion-scripting.md`](u5-automatizacion-scripting.md):
    portada de la unidad, ruta S24--S29, matriz de evolución de las
    preguntas y evidencia integradora.
-   [`u5-s24-del-protocolo-al-script.md`](u5-s24-del-protocolo-al-script.md):
    guardar el procedimiento; del protocolo ejecutable al script.
-   [`u5-s25-separar-procedimiento-datos.md`](u5-s25-separar-procedimiento-datos.md):
    variables, parámetros y validación de entradas; el mismo análisis
    para cualquier genoma.
-   [`u5-s26-procesamiento-por-lotes.md`](u5-s26-procesamiento-por-lotes.md):
    ciclos, colecciones de genomas, bitácora de ejecuciones y resumen
    del conjunto.
-   [`u5-s27-herramienta-cientifica.md`](u5-s27-herramienta-cientifica.md):
    el contrato escrito, documentación de uso, ayuda integrada y prueba
    cruzada entre equipos.
-   [`u5-s28-proyecto-integrador.md`](u5-s28-proyecto-integrador.md):
    **evidencia integradora de la unidad** --- ejecución con datos
    nuevos, revisión cruzada y defensa del proyecto.
-   [`u5-s29-cluster-hpc-sge.md`](u5-s29-cluster-hpc-sge.md): el mismo
    análisis en el clúster `chaac` con SGE; envío, monitoreo y
    demostración de que el resultado es idéntico.

La evidencia integradora de la unidad ---en **S28**--- **sustituye al
examen práctico 2**.

### Unidad 6 --- Comparar secuencias para construir hipótesis biológicas

De ejecutar una herramienta a interpretar la evidencia que produce:
**S30--S34**. Cierra el curso.

-   [`u6-comparacion-homologia.md`](u6-comparacion-homologia.md):
    portada de la unidad, ruta S30--S34, los seis principios científicos
    y la evidencia integradora.
-   [`u6-s30-comparar-alinear.md`](u6-s30-comparar-alinear.md): por qué
    una secuencia aislada dice poco; el alineamiento como hipótesis de
    correspondencia; identidad, similitud y gaps; nucleótidos frente a
    aminoácidos.
-   [`u6-s31-buscar-blast.md`](u6-s31-buscar-blast.md): de alinear
    contra una secuencia a buscar en una colección; base local,
    heurística y candidatos.
-   [`u6-s32-interpretar-inferir.md`](u6-s32-interpretar-inferir.md):
    *una lista de hits no es una conclusión*; integrar métricas y
    rankear evidencia.
-   [`u6-s33-defender-hipotesis.md`](u6-s33-defender-hipotesis.md):
    *inferir: cuando la similitud no basta*; homología,
    ortología/paralogía y límites de la transferencia de función.
-   [`u6-s34-integrar-hipotesis-casos-ciegos.md`](u6-s34-integrar-hipotesis-casos-ciegos.md):
    *integrar: de la evidencia a la hipótesis biológica*; **evidencia
    integradora** (informe de secuencia desconocida; cierre).

Documento docente de la unidad:
[`docente/u6-auditoria-datos.md`](docente/u6-auditoria-datos.md), auditoría de los 31
archivos de [`ejemplos/datos-alineamientos/`](ejemplos/datos-alineamientos/).

### Material docente de referencia

-   [`docente/u2-s6-cluster-hpc.md`](docente/u2-s6-cluster-hpc.md): material previo
    sobre clúster, recursos y SGE. **No debe publicarse como la S6
    vigente sin revisión.** S6 pertenece a la Unidad 2, pero el trabajo
    operativo de HPC/SGE quedó consolidado en
    [`u5-s29-cluster-hpc-sge.md`](u5-s29-cluster-hpc-sge.md). Durante la
    revisión debe definirse S6 de modo que prepare el entorno de cómputo
    sin duplicar S29.

### Material transversal

-   [`s14-s15-mini-proyecto-investigacion-I.md`](s14-s15-mini-proyecto-investigacion-I.md),
    [`s16-mini-proyecto-revision-pares.md`](s16-mini-proyecto-revision-pares.md),
    [`s17-evaluacion-individual-demostrativa.md`](s17-evaluacion-individual-demostrativa.md)
    y
    [`mini-proyecto-dictamen-cientifico.md`](mini-proyecto-dictamen-cientifico.md):
    semana de práctica integradora, revisión por pares y evaluación
    individual demostrativa. **No pertenecen a ninguna unidad**, pero
    condicionan el diseño de U4.

### Documentos docentes (no se publican)

Salvo la plantilla, que es canon y vive en la raíz junto a este README,
los documentos docentes están reunidos en [`docente/`](docente/). La
regla es simple: **la raíz de `contenidos-2026/` contiene solo material
del alumno** ---portadas de unidad, sesiones y material transversal---,
más los tres documentos del canon. Todo lo demás ---arquitecturas,
auditorías, notas de revisión y borradores no publicables--- va a
`docente/`. Al migrar a Quarto, esa carpeta se excluye del sitio.

-   [`plantilla-unidad.md`](plantilla-unidad.md): plantilla, esqueleto y
    checklist de calidad de 16 puntos. **Fuente de verdad** al generar o
    revisar una unidad. Permanece en la raíz por formar parte del canon
    junto a este README y a `../prompts-ia/guia-generacion-unidad.md`.
-   [`docente/u4-arquitectura.md`](docente/u4-arquitectura.md): diseño previo de la
    Unidad 4.
-   [`docente/u4-s21-arquitectura-confrontar.md`](docente/u4-s21-arquitectura-confrontar.md):
    arquitectura específica de S21 (fuente, prácticas y figuras).
-   [`docente/u4-s11-ajustes-editoriales.md`](docente/u4-s11-ajustes-editoriales.md) y
    [`docente/u2-notas-revision-docente.md`](docente/u2-notas-revision-docente.md):
    notas de revisión.
-   [`docente/propuesta-actualizacion-readme-guia.md`](docente/propuesta-actualizacion-readme-guia.md):
    propuesta de actualización de esta guía.

El prompt disparador para generar una unidad está en
`../prompts-ia/guia-generacion-unidad.md`, junto con las arquitecturas
de unidad (`uN-arquitectura.md`).

### Estado de redacción

Referencia operativa vigente:
**`Plan-Clases-BioInfo-2026-final-S34.xlsx`**, pestaña
**`PlanClases-2026-final S34`**. Esta versión incorpora la arquitectura
efectiva del curso hasta S34 y conserva las pestañas anteriores como
historial.

  -----------------------------------------------------------------------
  Unidad                  Sesiones                Estado antes de la
                                                  revisión horizontal
  ----------------------- ----------------------- -----------------------
  U1. Trabajo             S1--S2                  Redactada; por revisar
  reproducible y                                  contra el canon vigente
  comunicación técnica                            

  U2. Entorno Unix/Linux  S3--S6                  S3--S6 redactadas; **S6
  y cómputo científico                            nueva**, de verificación,
                                                  sin duplicar S29

  U3. Datos y bases de    S7--S9                  Redactada; por revisar
  datos biológicas                                horizontalmente

  U4. Procesamiento y     S10--S23                Redactada, incluyendo
  exploración de datos                            S14--S17 como bloque
  genómicos                                       transversal; por
                                                  homogeneizar

  U5. Automatización de   S24--S29                Redactada; por
  análisis                                        homogeneizar
  bioinformáticos con                             
  Shell                                           

  U6. Comparar secuencias S30--S34                Redactada; S34 es el
  para construir                                  cierre del curso
  hipótesis biológicas                            
  -----------------------------------------------------------------------

La secuencia pedagógica final de U6 es:

``` text
S30 Comparar → S31 Buscar → S32 Interpretar → S33 Inferir → S34 Integrar
```

S34 es la **evidencia integradora y cierre del curso**; no se proyecta
una S35.

El proyecto integrador de S28 sustituye al examen práctico 2. S14--S17
forman un bloque transversal dentro del arco de U4 y deben revisarse
como puente entre S10--S13 y S18--S23.

## Revisión horizontal del curso

Antes de declarar una unidad o el curso completo como versión final, las
sesiones se leen en secuencia. La revisión comprueba:

-   consistencia terminológica;
-   continuidad narrativa entre la limitación que cierra una sesión y la
    necesidad que abre la siguiente;
-   prácticas intercaladas y acumulativas;
-   evolución de `protocolo.md` sin reinicios ni duplicaciones;
-   ausencia de explicaciones repetidas cuando basta una remisión;
-   correspondencia resultado → actividad → evidencia → criterio;
-   nombres, alt text y pies de figuras consistentes;
-   referencias cruzadas válidas;
-   uso moderado de callouts;
-   un solo H1 real por sesión;
-   `[Indispensable]` / `[Consulta]` con formato uniforme;
-   retroalimentación colapsable cuando aporta autocorrección;
-   coherencia entre sesión, Programa 2026 y la pestaña vigente del Plan
    de clases;
-   separación entre material del alumno y documentos docentes,
    arquitecturas, auditorías o archivos temporales.

La revisión debe ser **conservadora**: no se reescribe una sesión solo
para hacerla parecerse a otra. Se preservan el contenido biológico, los
datos, los comandos válidos y las decisiones pedagógicas que siguen
vigentes; se corrigen primero convenciones editoriales y después, cuando
sea necesario, la estructura didáctica.

## Acervo de referencias

Disponible en `../introBioInfo/referencias/`:

-   Buffalo, V. (2015). *Bioinformatics Data Skills*. O'Reilly Media.
-   Ritchie, M. D., et al. (2015). Methods of integrating data to
    uncover genotype--phenotype interactions. *Nature Reviews Genetics*,
    16, 85--97. <https://doi.org/10.1038/nrg3868>
-   Fitzgerald, M. (2012). *Introducing Regular Expressions*. O'Reilly
    Media.
