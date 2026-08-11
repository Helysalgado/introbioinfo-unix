# Contenidos 2026 — Introducción a la Bioinformática

Esta carpeta contiene el **contenido didáctico nuevo** del curso, redactado en Markdown limpio. El
material está pensado como **lectura previa** para un modelo de aula invertida y debe ser
**autocontenido**: define los conceptos necesarios, explica para qué se usan y prepara al
estudiante para el taller. El formateo final en Quarto (`.qmd`, callouts, temas y navegación) se
realizará en una fase posterior.

Los materiales de `../introBioInfo/` y `../introBioInfo/referencias/` se usan como **referencia**.

> **Nota técnica — recursos para la migración a Quarto.** Los ejemplos propios de esta carpeta
> viven en [`ejemplos/`](ejemplos/) y se enlazan con rutas relativas. Quedan pendientes de copiar,
> al publicar en Quarto, los recursos que todavía viven en `../introBioInfo/`:
> `ejemplos/formato_protocolo_v1.0.md`, `ejemplos/ReporteGenomeEcoli_Formato_v2.md` y
> `referencias/bioinformatics-data-skills.pdf`. Al migrar, deben copiarse a la carpeta de recursos
> del sitio y actualizarse sus rutas.

## Identidad del curso

Este **no** es un curso de Unix ni un curso de comandos. Es un curso de **Introducción a la
Bioinformática**: las herramientas computacionales aparecen únicamente como medios para responder
preguntas biológicas.

De ahí se sigue el principio que ordena todo el material:

> **Las preguntas biológicas permanecen; las estrategias de análisis evolucionan.**

Consecuencias editoriales directas:

- Ninguna sesión se titula con el nombre de un comando; se titula con la **etapa del análisis** que
  representa.
- Ningún resultado de aprendizaje se formula como "usar la herramienta X", sino como lo que la
  herramienta permite **averiguar, contrastar o justificar**.
- Ninguna actividad termina en una salida de terminal: termina en una **interpretación biológica**
  sostenida por la evidencia obtenida.

## Principios de diseño didáctico

- Cada **módulo o sesión de dos horas** combina preparación previa, práctica presencial y una
  evidencia posterior corregida.
- Los conceptos se presentan antes que los comandos o herramientas que los implementan.
- **La capacidad analítica crece; las preguntas no cambian.** Una misma pregunta biológica puede
  revisitarse varias veces a lo largo de una unidad. No se trata de repetir un ejercicio, sino de
  producir una respuesta **más precisa, mejor fundamentada, más reproducible o con evidencia de mayor
  calidad** que la anterior. Cada regreso a una pregunta debe declarar explícitamente qué limitación
  de la estrategia previa corrige.
- **Ninguna herramienta se introduce porque "toca verla".** Cada una aparece porque resuelve una
  **limitación observada** en la estrategia anterior, y esa limitación debe haberse hecho evidente
  antes —idealmente, el estudiante la habrá encontrado por sí mismo—. El orden de las herramientas lo
  dicta la secuencia en que aparecen los obstáculos, no la estructura del temario.
- **Distinguir el dato de la operación.** Toda práctica debe ayudar a separar cuatro cosas, siempre
  en este orden: la **pregunta biológica** → el **dato** que la responde → la **operación** que hay
  que hacer sobre ese dato → la **herramienta** que ejecuta esa operación. Nunca se empieza por el
  comando. Muchas preguntas fracasan no porque falte el dato, sino porque falta la operación —y a
  veces esa operación aún no está al alcance del estudiante: reconocerlo también es un resultado.
- Las prácticas son **progresivas e intercaladas**: cada una recupera y amplía habilidades,
  decisiones o productos de las prácticas anteriores. La complejidad y la autonomía aumentan
  gradualmente, evitando ejercicios aislados o repeticiones sin propósito. Cada práctica se
  coloca **después del concepto crítico correspondiente**, no se acumula al final y contribuye al
  producto acumulativo del curso. Esa progresión se construye como una escalera: cada actividad
  **recupera** un resultado anterior, lo **compara**, lo **refina** y **documenta qué mejoró**. Una
  práctica que podría ejecutarse sin haber hecho las anteriores está mal diseñada.
- **El protocolo no es un entregable: es el registro del razonamiento científico.** `protocolo.md`
  crece sesión tras sesión y **nunca se reinicia**. Cada sesión añade o corrige **solo** el apartado
  que le corresponde, y conserva las versiones anteriores de una respuesta cuando la mejora: la
  comparación entre ambas es la evidencia de aprendizaje más valiosa del curso. Un apartado de
  *limitaciones* honesto vale más que un resultado presentado como definitivo.
- `protocolo.md`, los metadatos del proyecto y `bitacora-ia.md` son **documentos vivos**: se
  amplían y corrigen entre sesiones y unidades.
- La estructura de proyecto usada de manera consistente es:

```text
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

La IA se incorpora cuando permite **comparar, revisar o mejorar** una actividad realizada
previamente por el estudiante. Se aplica la regla **primero a mano, después con IA**. El primer
intento manual constituye una **línea base de comparación**, no una verdad absoluta: tanto el
trabajo manual como la respuesta de IA deben contrastarse con el material del curso,
documentación autorizada, pruebas controladas y evidencia independiente.

La actividad de IA puede colocarse al final de una sesión, al cierre de una unidad o como trabajo
posterior, según el tiempo disponible y el resultado de aprendizaje. No es obligatorio forzar un
“cierre con IA” idéntico en cada unidad.

### Asistente de Unix y bioinformática del curso

El curso dispone de [**ProfeUnix Bioinfo**](https://chatgpt.com/g/g-6893cf2451d88191b11cd0c87de045ab-profeunix-bioinfo),
un GPT que puede utilizarse como recurso de consulta y revisión en las actividades que lo indiquen.
El enlace canónico se presenta al alumnado en la Unidad 1; las lecciones posteriores pueden remitir
a él sin repetir toda la política de IA.

Su uso debe ser **intencional, ocasional y verificable**: conviene solicitarlo cuando aporte una
comparación pedagógica concreta —por ejemplo, revisar permisos, diagnosticar un comando o detectar
la mezcla entre dos planificadores—, no añadirlo automáticamente a todas las sesiones. Cuando una
actividad pida utilizarlo, debe conservar la regla **primero a mano, después con IA**, exigir
validación independiente y registrar el uso en `bitacora-ia.md`.

El acceso a los GPT personalizados puede depender de la cuenta o de las condiciones vigentes de la
plataforma. Por ello, ninguna evidencia debe depender exclusivamente de abrir este recurso: si un
estudiante no tiene acceso, podrá realizar la misma revisión con otro asistente autorizado e indicar
en la bitácora cuál utilizó.

Reglas de uso responsable:

- La IA no sustituye la ejecución de habilidades básicas que el módulo busca desarrollar.
- No se comparten credenciales, datos sensibles, direcciones institucionales privadas, llaves,
  tokens ni información que identifique a una persona.
- No se ejecutan comandos sugeridos sin comprenderlos, revisar sus efectos y probarlos, cuando
  corresponda, en archivos o directorios de prueba.
- Todo uso relevante se registra en `bitacora-ia.md`: objetivo, herramienta, prompt, respuesta o
  resumen, verificación independiente, correcciones y decisión final.

## Estructura editorial común de cada módulo

Cada módulo sigue esta secuencia general, adaptada al contenido y sin duplicar secciones que no
aporten valor:

1. Título y número de sesión.
2. Nota de aula invertida: antes, durante y después de clase.
3. Ficha del módulo.
4. Relación con unidades anteriores y con el caso bioinformático.
5. Resultados de aprendizaje observables.
6. Preparación previa o *preflight*.
7. Bloques conceptuales esenciales.
8. Prácticas progresivas e intercaladas después de cada concepto crítico; cada una retoma y
   amplía lo desarrollado anteriormente.
9. Cierre que actualice un producto acumulativo, preferentemente `protocolo.md`.
10. Evidencia de aprendizaje.
11. Errores frecuentes y estrategias de diagnóstico.
12. Criterios de logro o rúbrica breve.
13. Autoevaluación o semáforo de salida.
14. Distribución estimada de las dos horas.
15. Alineación resultado–actividad–evidencia–criterio.
16. Glosario y referencias específicas.

Los comandos se clasifican, cuando sea útil, como **esenciales**, **de consulta** o **de
ampliación**. Las soluciones, la retroalimentación y los prompts extensos pueden colocarse en
bloques HTML colapsables para no interrumpir la lectura:

```html
<details>
<summary>Ver solución o retroalimentación</summary>

Contenido que se muestra al desplegar el bloque.

</details>
```

## Guía de estilo para facilitar el paso a Quarto

### Lenguaje

El vocabulario debe situar el análisis en primer plano y la herramienta en segundo. Siempre que sea
natural, se prefieren expresiones como **construir evidencia**, **localizar el dato**, **refinar una
respuesta**, **contrastar resultados**, **justificar una interpretación**, **fortalecer una
conclusión** y **documentar la estrategia**, frente a formulaciones centradas en "usar un comando".

Esto no implica ocultar las herramientas: los comandos se nombran con precisión y aparecen en todos
los bloques de código. Implica que el texto que los rodea explique **qué se averigua**, no solo qué se
ejecuta.

Términos que conviene usar de forma consistente en todo el material: *pregunta biológica, dato,
operación, evidencia, estrategia, interpretación, refinamiento, limitación, respuesta provisional,
medición, estimación, protocolo*. Se evitan los sinónimos que introduzcan matices no deseados.

### Callouts

Se escriben como cita (`>`) con una etiqueta en mayúsculas y negrita. Mapean directamente a
callouts de Quarto durante la fase de formateo:

| Marcador en el contenido | Callout de Quarto |
| --- | --- |
| `> **NOTA:** …` | `::: {.callout-note}` |
| `> **IMPORTANTE:** …` | `::: {.callout-important}` |
| `> **TIP:** …` | `::: {.callout-tip}` |
| `> **¿SABÍAS QUE?:** …` | `::: {.callout-tip title="¿Sabías que?"}` |
| `> **COMENTARIO:** …` | `::: {.callout-tip}` |
| `> **ADVERTENCIA:** …` | `::: {.callout-warning}` |

Los callouts se usan **con moderación**: no toda observación merece uno. Como referencia práctica,
conviene no superar unos pocos por sección y reservarlos para lo que el estudiante no debe pasar por
alto —un riesgo real, una regla que evita un error silencioso, una distinción conceptual crítica—. Si
al revisar una sesión los callouts ocupan más espacio que el texto corrido, sobran callouts.

### Figuras terminadas

Las figuras listas para publicación se guardan en [`images/`](images/), se insertan en el punto
donde apoyan el aprendizaje y llevan **texto alternativo informativo** y **pie numerado**. Se usa
PNG para publicación y se conserva el SVG editable cuando exista. No deben quedar marcadores
editoriales como “FIGURA SUGERIDA” o “Crear figura”.

```markdown
![Comparación visual entre una interfaz gráfica y una interfaz de línea de comandos.](images/figura-u2-gui-vs-cli.png)

*Figura 1. Comparación entre GUI y CLI. Elaboración propia.*
```

Antes de publicar, se comprueba que la figura coincida con el texto, use la convención
`data/source/` cuando represente el proyecto y no contenga estados, comandos o rutas incorrectos.

### Código, prácticas y referencias

- Los bloques de código siempre declaran el lenguaje (`bash`, `markdown`, `text`, etc.) y se
  anuncian en el texto.
- Cada práctica incluye pasos explícitos, producto esperado, momento de trabajo y criterio de
  logro.
- Las prácticas se leen antes de clase pero se **navegan** durante el taller. Cuando una práctica
  tenga muchos pasos, conviene marcarlos con una etiqueta breve en negrita al inicio del paso
  —*Predice, Localiza, Comprueba, Contrasta, Interpreta, Documenta*— para que puedan localizarse de
  un vistazo. Se evitan los bloques de texto largos: si una idea ocupa más de cuatro o cinco líneas
  seguidas, normalmente admite dividirse o convertirse en lista.
- Las referencias se citan en línea como `(Autor, año, cap./p.)` y se desarrollan al final del
  módulo. Toda definición, afirmación relevante y buena práctica debe estar respaldada por una
  fuente verificable; no se inventan referencias.
- Se conservan las etiquetas **[Nuevo]**, **[Reforzado]** e **[Integración]** del Programa 2026.

## Índice de contenidos

### Unidad 1 — Trabajo reproducible y comunicación técnica

- [`u1-s1-s2-trabajo-reproducible-v3.md`](u1-s1-s2-trabajo-reproducible-v3.md): versión vigente de la
  unidad (S1–S2). **Unidad de referencia (estándar de oro)** para generar las demás.

### Unidad 2 — Entorno Unix/Linux y cómputo científico

- [`u2-s3-shell-acceso-remoto.md`](u2-s3-shell-acceso-remoto.md): shell, ayuda, protocolos, SSH y
  transferencia con verificación de integridad.
- [`u2-s4-sistema-archivos-v3.md`](u2-s4-sistema-archivos-v3.md): sistema de archivos, rutas, navegación
  y operaciones seguras.
- [`u2-s5-archivos-permisos-procesos-v2.md`](u2-s5-archivos-permisos-procesos-v2.md): archivos,
  compresión, permisos y procesos.

La Unidad 2 concluye con S5. El siguiente bloque curricular es **Unidad 3 — Datos y bases de datos
biológicas**, conforme al Plan y al Programa.

> **NOTA:** La portada de la Unidad 2 (`u2-entorno-unix-hpc.md`) está redactada pero todavía no se ha
> incorporado a esta carpeta. Hasta entonces, los tres módulos S3–S5 se leen de forma independiente.

### Unidad 3 — Datos y bases de datos biológicas

- [`u3-datos-bases-datos.md`](u3-datos-bases-datos.md): portada de la unidad, ruta S7–S9 y evidencias
  acumuladas.
- [`u3-s7-secuencias-formatos-genbank.md`](u3-s7-secuencias-formatos-genbank.md): dogma central,
  formatos FASTA/GenBank/GFF3 y anatomía de un registro.
- [`u3-s8-bases-datos-descarga-integridad.md`](u3-s8-bases-datos-descarga-integridad.md): recuperación
  de datos, procedencia y verificación de integridad.
- [`u3-s9-inspeccion-transferencia-verificable.md`](u3-s9-inspeccion-transferencia-verificable.md):
  inspección de archivos y transferencia verificable.

### Unidad 4 — Procesamiento y exploración de datos genómicos

Una investigación sobre un genoma, en diez sesiones: **S10–S13** (establecer los hechos) y
**S18–S23** (el ciclo de la evidencia).

- [`u4-procesamiento-exploracion.md`](u4-procesamiento-exploracion.md): portada de la unidad.
- [`u4-s10-anatomia-flujos-datos.md`](u4-s10-anatomia-flujos-datos.md): anatomía del archivo
  biológico, redirecciones y tuberías.
- [`u4-s11-estructura-tabular-anotacion.md`](u4-s11-estructura-tabular-anotacion.md): estructura
  tabular de la anotación y coordenadas.
- [`u4-s12-filtrado-conteos-genoma.md`](u4-s12-filtrado-conteos-genoma.md): filtrado y primeros
  conteos.
- [`u4-s13-inventario-resumen-genoma.md`](u4-s13-inventario-resumen-genoma.md): inventario y resumen
  del genoma.
- [`u4-s18-precision-patrones-expresiones-regulares.md`](u4-s18-precision-patrones-expresiones-regulares.md):
  precisión de los patrones.
- [`u4-s19-extraccion-identificadores-correspondencia.md`](u4-s19-extraccion-identificadores-correspondencia.md):
  extracción de identificadores y correspondencia entre archivos.
- [`u4-s20-normalizar-datos-comparables.md`](u4-s20-normalizar-datos-comparables.md): normalización y
  datos derivados.
- [`u4-s21-confrontar-fuente-independiente.md`](u4-s21-confrontar-fuente-independiente.md): contraste
  con una fuente independiente.
- [`u4-s22-condicionar-calcular-columnas.md`](u4-s22-condicionar-calcular-columnas.md): análisis
  condicionado y medidas derivadas.
- [`u4-s23-protocolo-ejecutable-genoma.md`](u4-s23-protocolo-ejecutable-genoma.md): el protocolo como
  cuaderno de laboratorio ejecutable.

### Unidad 5 — Automatización de análisis bioinformáticos con Shell

De un procedimiento que se lee a una herramienta que se ejecuta: **S24–S29**.

- [`u5-automatizacion-scripting.md`](u5-automatizacion-scripting.md): portada de la unidad, ruta
  S24–S29, matriz de evolución de las preguntas y evidencia integradora.
- [`u5-s24-del-protocolo-al-script.md`](u5-s24-del-protocolo-al-script.md): guardar el procedimiento;
  del protocolo ejecutable al script.
- [`u5-s25-separar-procedimiento-datos.md`](u5-s25-separar-procedimiento-datos.md): variables,
  parámetros y validación de entradas; el mismo análisis para cualquier genoma.
- [`u5-s26-procesamiento-por-lotes.md`](u5-s26-procesamiento-por-lotes.md): ciclos, colecciones de
  genomas, bitácora de ejecuciones y resumen del conjunto.
- [`u5-s27-herramienta-cientifica.md`](u5-s27-herramienta-cientifica.md): el contrato escrito,
  documentación de uso, ayuda integrada y prueba cruzada entre equipos.
- [`u5-s28-proyecto-integrador.md`](u5-s28-proyecto-integrador.md): **evidencia integradora de la
  unidad** — ejecución con datos nuevos, revisión cruzada y defensa del proyecto.
- [`u5-s29-cluster-hpc-sge.md`](u5-s29-cluster-hpc-sge.md): el mismo análisis en el clúster `chaac`
  con SGE; envío, monitoreo y demostración de que el resultado es idéntico.

La evidencia integradora de la unidad —en **S28**— **sustituye al examen práctico 2**.

### Unidad 6 — Comparar secuencias para construir hipótesis biológicas

De ejecutar una herramienta a interpretar la evidencia que produce: **S30–S34**. Cierra el curso.

- [`u6-comparacion-homologia.md`](u6-comparacion-homologia.md): portada de la unidad, ruta S30–S34,
  los seis principios científicos y la evidencia integradora.
- [`u6-s30-comparar-alinear.md`](u6-s30-comparar-alinear.md): por qué una secuencia aislada dice poco;
  el alineamiento como hipótesis de correspondencia; identidad, similitud y gaps; nucleótidos frente a
  aminoácidos.
- [`u6-s31-buscar-blast.md`](u6-s31-buscar-blast.md): de alinear contra una secuencia a buscar en una
  colección; base local, heurística y candidatos.
- [`u6-s32-interpretar-inferir.md`](u6-s32-interpretar-inferir.md): *una lista de hits no es una
  conclusión*; integrar métricas y rankear evidencia.
- [`u6-s33-defender-hipotesis.md`](u6-s33-defender-hipotesis.md): *inferir: cuando la similitud no
  basta*; homología, ortología/paralogía y límites de la transferencia de función.
- [`u6-s34-integrar-hipotesis.md`](u6-s34-integrar-hipotesis.md): *integrar: de la evidencia a la
  hipótesis biológica*; **evidencia integradora** (informe de secuencia desconocida; cierre).

Documento docente de la unidad: [`u6-auditoria-datos.md`](u6-auditoria-datos.md), auditoría de los 31
archivos de [`datos-alineamientos/`](datos-alineamientos/).

### Material docente de referencia

- [`u2-s6-cluster-hpc.md`](u2-s6-cluster-hpc.md): borrador previo sobre clúster, recursos y SGE. Su
  contenido quedó incorporado y corregido en [`u5-s29-cluster-hpc-sge.md`](u5-s29-cluster-hpc-sge.md);
  **se conserva como referencia** y ya no forma parte de ninguna unidad. Al revisar **S6** (Unidad 2)
  conviene comprobar el reparto: S6 mantiene el panorama a nivel usuario y S29 no lo repite.

### Material transversal

- [`s14-s15-mini-proyecto-investigacion-I.md`](s14-s15-mini-proyecto-investigacion-I.md),
  [`s16-mini-proyecto-revision-pares.md`](s16-mini-proyecto-revision-pares.md),
  [`s16.b-cierre.md`](s16.b-cierre.md),
  [`s17-evaluacion-individual-demostrativa.md`](s17-evaluacion-individual-demostrativa.md) y
  [`mini-proyecto-dictamen-cientifico.md`](mini-proyecto-dictamen-cientifico.md): semana de práctica
  integradora, revisión por pares y evaluación individual demostrativa. **No pertenecen a ninguna
  unidad**, pero condicionan el diseño de U4.

### Documentos docentes (no se publican)

- [`plantilla-unidad.md`](plantilla-unidad.md): plantilla, esqueleto y checklist de calidad de 16
  puntos. **Fuente de verdad** al generar o revisar una unidad.
- [`u4-arquitectura.md`](u4-arquitectura.md): diseño previo de la Unidad 4.
- [`u4-s21-arquitectura-confrontar.md`](u4-s21-arquitectura-confrontar.md): arquitectura específica de
  S21 (fuente, prácticas y figuras).
- [`u4-s11-ajustes-editoriales.md`](u4-s11-ajustes-editoriales.md) y
  [`u2-notas-revision-docente.md`](u2-notas-revision-docente.md): notas de revisión.
- [`propuesta-actualizacion-readme-guia.md`](propuesta-actualizacion-readme-guia.md): propuesta de
  actualización de esta guía.

El prompt disparador para generar una unidad está en `../prompts-ia/guia-generacion-unidad.md`, junto
con las arquitecturas de unidad (`uN-arquitectura.md`).

### Estado de redacción

Referencia operativa vigente: **`../Plan-Clases-BioInfo-2026-ajustado-HPC.xlsx`**, pestaña
`PlanClases-2026-HPC` (32 sesiones). Sustituye a `Plan-Clases-BioInfo-2026.xlsx` de S24 en adelante.

| Unidad | Sesiones | Estado |
| --- | --- | --- |
| U1. Trabajo reproducible y comunicación técnica | S1–S2 | Completa |
| U2. Entorno Unix/Linux y cómputo científico | S3–S6 | Módulos S3–S5 completos; **portada pendiente de incorporar**; S6 por revisar junto con S29 |
| U3. Datos y bases de datos biológicas | S7–S9 | Completa |
| U4. Procesamiento y exploración de datos genómicos | S10–S13, S18–S23 | Completa |
| U5. Automatización de análisis bioinformáticos con Shell | S24–S29 | **Completa** |
| U6. Comparar secuencias para construir hipótesis biológicas | S30–S34 | **Completa** (auditoría, portada, S30–S34) |

> **Discrepancia registrada (U6).** El Plan ajustado asigna **tres** sesiones (S30–S32) y la
> arquitectura pedagógica propone **seis**. El material se redacta con **cinco** (S30–S34): S30
> fusiona *comparar*+*alinear*; S32–S34 separan *interpretar*, *inferir* e *integrar*. El cierre no
> introduce conceptos nuevos. Requiere confirmar semanas adicionales.

Sesiones sin unidad: S14–S15 (práctica integradora), S16 (examen práctico 1) y S17 (revisión). **No
hay examen práctico 2**: lo sustituye el proyecto integrador de S28.

## Acervo de referencias

Disponible en `../introBioInfo/referencias/`:

- Buffalo, V. (2015). *Bioinformatics Data Skills*. O'Reilly Media.
- Ritchie, M. D., et al. (2015). Methods of integrating data to uncover genotype–phenotype
  interactions. *Nature Reviews Genetics*, 16, 85–97. <https://doi.org/10.1038/nrg3868>
- Fitzgerald, M. (2012). *Introducing Regular Expressions*. O'Reilly Media.
