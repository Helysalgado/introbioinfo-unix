# Propuesta de actualización del README y de la guía de generación

> **Origen.** Lecciones aprendidas durante el desarrollo de la Unidad 4 (arquitectura, S10 y S11).
> El objetivo es que las unidades futuras nazcan con este estándar, sin reescribir nada de lo
> existente ni introducir reglas atadas a una herramienta o formato concreto.
>
> **Reparto propuesto:** `contenidos-2026/README.md` = **fuente de los principios pedagógicos y del
> estilo**. `prompts-ia/guia-generacion-unidad.md` = **instrucciones operativas** para generar una
> unidad nueva. `contenidos-2026/plantilla-unidad.md` = **esqueleto y checklist de calidad**.

---

# Documento 1 · Cambios propuestos para `contenidos-2026/README.md`

## R1. Identidad del curso *(sección nueva, al inicio, antes de "Principios de diseño didáctico")*

**Motivo pedagógico.** Es la confusión más costosa del curso: si el material se percibe como un curso
de Unix, el estudiante estudia comandos y no razonamiento biológico. Conviene declararlo antes que
cualquier otra cosa, porque condiciona todas las decisiones editoriales posteriores.

**Texto sugerido:**

```markdown
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
```

## R2. Capacidad analítica creciente *(añadir a "Principios de diseño didáctico")*

**Motivo pedagógico.** Distingue *repetir un ejercicio* de *refinar una respuesta*. Sin este
principio, revisitar una pregunta se percibe como relleno; con él, se percibe como progreso.

**Texto sugerido** (como viñeta nueva del listado existente):

```markdown
- **La capacidad analítica crece; las preguntas no cambian.** Una misma pregunta biológica puede
  revisitarse varias veces a lo largo de una unidad. No se trata de repetir un ejercicio, sino de
  producir una respuesta **más precisa, mejor fundamentada, más reproducible o con evidencia de mayor
  calidad** que la anterior. Cada regreso a una pregunta debe declarar explícitamente qué limitación
  de la estrategia previa corrige.
```

## R3. Las herramientas aparecen por necesidad *(añadir a "Principios de diseño didáctico")*

**Motivo pedagógico.** Sustituye el orden del temario por el orden del problema: la herramienta se
vuelve memorable porque el estudiante ya sintió su falta.

**Texto sugerido:**

```markdown
- **Ninguna herramienta se introduce porque "toca verla".** Cada una aparece porque resuelve una
  **limitación observada** en la estrategia anterior, y esa limitación debe haberse hecho evidente
  antes —idealmente, el estudiante la habrá encontrado por sí mismo—. El orden de las herramientas lo
  dicta la secuencia en que aparecen los obstáculos, no la estructura del temario.
```

## R4. Dato ≠ operación *(añadir a "Principios de diseño didáctico")*

**Motivo pedagógico.** Es el error de razonamiento más frecuente: buscar en el archivo algo que el
archivo no contiene porque exige calcularlo. Nombrarlo lo vuelve enseñable.

**Texto sugerido:**

```markdown
- **Distinguir el dato de la operación.** Toda práctica debe ayudar a separar cuatro cosas, siempre
  en este orden: la **pregunta biológica** → el **dato** que la responde → la **operación** que hay
  que hacer sobre ese dato → la **herramienta** que ejecuta esa operación. Nunca se empieza por el
  comando. Muchas preguntas fracasan no porque falte el dato, sino porque falta la operación —y a
  veces esa operación aún no está al alcance del estudiante: reconocerlo también es un resultado.
```

## R5. El protocolo como registro del razonamiento *(reforzar el punto existente sobre el producto acumulativo)*

**Motivo pedagógico.** Mientras el protocolo se perciba como entregable, se redacta al final y para
la calificación. Como registro del razonamiento, se escribe durante el análisis y sirve al estudiante.

**Texto sugerido** (sustituye a la viñeta "Cada cierre actualiza un producto acumulativo…"):

```markdown
- **El protocolo no es un entregable: es el registro del razonamiento científico.** `protocolo.md`
  crece sesión tras sesión y **nunca se reinicia**. Cada sesión añade o corrige **solo** el apartado
  que le corresponde, y conserva las versiones anteriores de una respuesta cuando la mejora: la
  comparación entre ambas es la evidencia de aprendizaje más valiosa del curso. Un apartado de
  *limitaciones* honesto vale más que un resultado presentado como definitivo.
```

## R6. Prácticas progresivas *(ampliar la viñeta existente sobre prácticas intercaladas)*

**Motivo pedagógico.** La viñeta actual ya pide progresión; conviene decir **cómo** se logra, con
operaciones concretas y verificables.

**Texto sugerido** (a continuación de la viñeta existente):

```markdown
  En la práctica, esa progresión se construye como una escalera: cada actividad **recupera** un
  resultado anterior, lo **compara**, lo **refina** y **documenta qué mejoró**. Una práctica que
  podría ejecutarse sin haber hecho las anteriores está mal diseñada.
```

## R7. Lenguaje del curso *(sección nueva dentro de "Guía de estilo…")*

**Motivo pedagógico.** El vocabulario construye la identidad del curso con más eficacia que cualquier
declaración de intenciones. Si el texto dice "usar `cut`", el estudiante entiende que el objetivo es
`cut`.

**Texto sugerido:**

```markdown
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
medición, estimación, protocolo*. Evitar sinónimos que introduzcan matices no deseados.
```

## R8. Uso moderado de callouts *(añadir a "Callouts", tras la tabla de mapeo)*

**Motivo pedagógico.** El callout funciona por contraste. Cuando todo está destacado, nada lo está —y
la lectura previa se vuelve agotadora.

**Texto sugerido:**

```markdown
Los callouts se usan **con moderación**: no toda observación merece uno. Como referencia práctica,
conviene no superar unos pocos por sección y reservarlos para lo que el estudiante no debe pasar por
alto —un riesgo real, una regla que evita un error silencioso, una distinción conceptual crítica—. Si
al revisar una sesión los callouts ocupan más espacio que el texto corrido, sobran callouts.
```

## R9. Organización visual de las prácticas *(añadir a "Código, prácticas y referencias")*

**Motivo pedagógico.** El material se lee antes de clase, pero las prácticas se **navegan** durante el
taller, con prisa y la terminal abierta. Son dos usos distintos del mismo texto.

**Texto sugerido:**

```markdown
Las prácticas se leen antes de clase pero se **navegan** durante el taller. Cuando una práctica tenga
muchos pasos, conviene marcarlos con una etiqueta breve en negrita al inicio del paso —*Predice,
Localiza, Comprueba, Contrasta, Interpreta, Documenta*— para que puedan localizarse de un vistazo.
Se evitan los bloques de texto largos: si una idea ocupa más de cuatro o cinco líneas seguidas,
normalmente admite dividirse o convertirse en lista. Esto mejora la lectura sin añadir contenido.
```

---

# Documento 2 · Cambios propuestos para `prompts-ia/guia-generacion-unidad.md`

> Criterio general: la guía **no repite** los principios; los **aplica**. Cada cambio se formula como
> instrucción verificable para quien genera una unidad nueva.

## G1. Encabezado del rol *(sustituir el párrafo inicial "Actúa como especialista…")*

**Motivo pedagógico.** El encargo inicial condiciona todo lo que se genera después. Si no declara la
identidad del curso, el material tiende por defecto hacia el manual de Unix.

**Texto sugerido** (añadir tras la primera frase existente):

```markdown
Ten presente en todo momento que **no estás escribiendo un curso de Unix ni un manual de comandos**:
escribes material de bioinformática en el que las herramientas aparecen únicamente como medio para
responder preguntas biológicas. El principio rector del curso —*las preguntas biológicas permanecen;
las estrategias de análisis evolucionan*— está desarrollado en `contenidos-2026/README.md`, sección
**Identidad del curso**; léelo antes de escribir.
```

## G2. Antes de escribir *(añadir a §1, lista de documentos de referencia)*

**Motivo pedagógico.** Una unidad se diseña completa antes de redactarse; en U4 la arquitectura previa
—matriz de preguntas incluida— evitó que las sesiones se convirtieran en capítulos independientes.

**Texto sugerido:**

```markdown
- **La arquitectura de la unidad**, si existe (`uN-arquitectura.md`): hilo conductor, propuesta de
  sesiones, matriz de evolución de las preguntas y evolución del producto acumulativo. Si la unidad
  aún no la tiene, **diséñala y sométela a visto bueno antes de redactar ninguna sesión**.
- **La sesión inmediatamente anterior, completa**: no basta con conocer su temario. Necesitas saber
  con qué limitación terminó, qué números quedaron pendientes de corregir y qué pregunta dejó abierta.
```

## G3. Matriz de evolución de las preguntas *(apartado nuevo en §2, "Estándares de contenido")*

**Motivo pedagógico.** Es el instrumento que hace operativo el principio de capacidad analítica
creciente: sin él, "revisitar preguntas" es una intención; con él, es una decisión de diseño
verificable.

**Texto sugerido:**

```markdown
- **Matriz de evolución de las preguntas.** Antes de redactar, construye una tabla con todas las
  preguntas biológicas de la unidad y, para cada una: en qué sesión aparece por primera vez, con qué
  estrategia se responde inicialmente, cómo se refina después, qué herramienta permite cada
  refinamiento y en qué sesión queda resuelta. Al escribir cada sesión, consúltala: las preguntas que
  **aparecen** definen el contenido nuevo; las que se **refinan** definen las actividades de retorno.
  **Una sesión que no refina ninguna pregunta anterior está mal situada en la unidad.**
```

## G4. Introducción de herramientas *(apartado nuevo en §2)*

**Motivo pedagógico.** Convierte el principio R3 en un formato reproducible, ya probado en S10 y S11.

**Texto sugerido:**

```markdown
- **Cada herramienta nueva entra por una necesidad, y se presenta en formato mínimo.** Antes de
  introducirla, el material debe haber mostrado la limitación que resuelve. La presentación no excede
  cuatro elementos: **Sintaxis mínima** (un bloque de código), **¿Qué hace?** (dos líneas como
  máximo), **¿Por qué aparece en esta sesión?** (qué limitación de la estrategia anterior corrige) y
  uno o dos **prompts al asistente del curso** para explorar opciones adicionales por cuenta propia.
  El material no es un manual: las opciones exhaustivas se delegan a `man` y al asistente.
```

## G5. Continuidad narrativa *(apartado nuevo en §2)*

**Motivo pedagógico.** Da un criterio de revisión concreto —tres preguntas— en lugar de una aspiración
difusa de "que fluya".

**Texto sugerido:**

```markdown
- **Continuidad entre sesiones.** Cada sesión debe poder responder tres preguntas, aunque no las
  formule literalmente: **¿qué problema resolvió la sesión anterior?**, **¿qué mejora aporta esta?** y
  **¿qué limitación queda abierta para la siguiente?** La sesión termina dejando una limitación viva
  —no un suspense artificial, sino la consecuencia natural del análisis— y la siguiente abre
  resolviéndola. Incluye además una orientación breve que permita al estudiante situarse: qué
  preguntas de la unidad se trabajan hoy y cuáles quedan para más adelante.
```

## G6. Prácticas *(ampliar el punto 6 de §3, "Estructura obligatoria")*

**Motivo pedagógico.** Añade a los tres momentos ya exigidos el criterio de encadenamiento y el de
navegabilidad en el taller.

**Texto sugerido** (a continuación del punto 6 existente):

```markdown
   Además, las prácticas de una misma unidad forman una **escalera**: cada una recupera un resultado
   anterior, lo compara, lo refina y documenta qué mejoró. Toda práctica arranca de una **pregunta
   biológica**, nunca de un comando, y cierra con una **interpretación** al nivel que la evidencia
   permita. Cuando una práctica tenga muchos pasos, marca cada uno con una etiqueta breve en negrita
   (*Predice, Localiza, Comprueba, Contrasta, Interpreta, Documenta*) para facilitar su navegación
   durante el taller.
```

## G7. Verificación final *(ampliar §7)*

**Motivo pedagógico.** Los defectos de coherencia y de ritmo solo se ven mirando la unidad completa,
no sesión por sesión.

**Texto sugerido:**

```markdown
Cuando la unidad esté terminada, realiza además una **revisión horizontal** —leyendo todas sus
sesiones seguidas— para comprobar:

- **consistencia terminológica**: los mismos conceptos se nombran siempre igual;
- **continuidad narrativa**: cada sesión enlaza con la anterior y prepara la siguiente;
- **longitud y ritmo de las prácticas**: pasos comparables, sin bloques de texto excesivos;
- **estilo de las figuras**: paleta, tipografía y formato de pie coherentes en toda la unidad;
- **referencias cruzadas**: los reenvíos entre sesiones apuntan a secciones que existen;
- **equilibrio de callouts**: destacan lo importante sin saturar;
- **evolución del protocolo**: cada sesión añade su apartado, ninguno se reinicia ni se duplica;
- **redundancias entre sesiones**: ninguna explicación se repite en dos sesiones distintas; la
  segunda vez se sustituye por una remisión breve.
```

## G8. Recorte por remisión *(sustituir apartados de §4 y §5 que ya viven en el README)*

**Motivo pedagógico.** Reduce la guía y evita que dos documentos se contradigan al evolucionar. Ver
Documento 3.

**Texto sugerido** (para el inicio de §4, "Convenciones de estilo"):

```markdown
## 4. Convenciones de estilo

Las convenciones —callouts, figuras, bloques de código, etiquetas de ajuste, referencias inline y
lenguaje del curso— están definidas en `contenidos-2026/README.md` y son de aplicación obligatoria.
No se reproducen aquí para evitar divergencias. Al generar la unidad, **verifica** que se cumplen; si
detectas una convención que el README no cubre, propón añadirla allí en vez de resolverla solo en esta
unidad.
```

---

# Documento 3 · Reglas duplicadas y reparto propuesto

Hoy hay tres documentos que se solapan: el **README** (estilo y principios), la **guía de generación**
(prompt operativo) y la **plantilla de unidad** (esqueleto y checklist). La regla de reparto que
propongo:

| Documento | Responde a la pregunta | Contenido que le corresponde |
| --- | --- | --- |
| `README.md` | **Por qué y con qué criterio** se escribe el material | Identidad del curso, principios didácticos, política de IA, estructura de proyecto, convenciones de estilo, lenguaje |
| `guia-generacion-unidad.md` | **Cómo generar** una unidad nueva | Rol, orden de lectura, flujo de trabajo, requisitos previos (arquitectura, matriz), instrucciones de verificación |
| `plantilla-unidad.md` | **Qué debe contener** una unidad terminada | Esqueleto en orden fijo, checklist de calidad, tabla de parámetros por unidad |

## Duplicaciones detectadas

| # | Regla | Hoy aparece en | Debería quedar en | Acción |
| ---: | --- | --- | --- | --- |
| D1 | Tabla de callouts y su mapeo | README §Callouts · guía §4 | **README** | La guía remite (G8) |
| D2 | Convenciones de figuras: revisar `images/`, alt text, pie numerado | README §Figuras · guía §4 | **README** | La guía remite (G8) |
| D3 | Bloques de código con lenguaje declarado | README · guía §4 | **README** | La guía remite (G8) |
| D4 | Etiquetas **[Nuevo] / [Reforzado] / [Integración]** | README · guía §4 | **README** | La guía remite (G8) |
| D5 | Referencias inline + prohibición de inventarlas | README · guía §2 y §4 | **README** el principio | La guía conserva solo la instrucción de **verificar** las referencias nuevas |
| D6 | Estructura de proyecto `data/source/`, `data/processed/`, `src/`, `results/`, `doc/` | README · guía §5 | **README** | La guía remite |
| D7 | Política de IA: "primero a mano", línea base, bitácora, asistente del curso | README §Uso crítico de IA (extenso) · guía §5 (resumen) | **README** | La guía conserva únicamente **cómo redactar** la sección de cierre con IA |
| D8 | Esqueleto de la unidad / estructura editorial | README §Estructura editorial (16 pasos) · guía §3 (12 puntos) · plantilla §1 (12 puntos) | **plantilla-unidad.md** | README y guía remiten a la plantilla; se elimina la tercera versión, hoy divergente en numeración |
| D9 | Alcance "unidad completa vs. módulo" | guía §1 (nota extensa) · plantilla (nota casi idéntica) | **plantilla-unidad.md** | La guía la sustituye por una línea de remisión |
| D10 | Prácticas en tres momentos ligadas a las Tareas del plan | guía §2 y §3 · plantilla §1.6 | **plantilla-unidad.md** | La guía conserva solo la advertencia sobre no romper la numeración de Tareas y registrar discrepancias |

## Efecto esperado

- El **README** gana cuatro principios nuevos (identidad, capacidad analítica creciente, herramientas
  por necesidad, dato ≠ operación) y dos apartados de estilo (lenguaje, moderación de callouts), y se
  convierte en la fuente única de la filosofía del curso.
- La **guía** se acorta de forma apreciable —pierde §4 casi entero y buena parte de §5— y gana lo que
  antes no tenía: exigencia de arquitectura previa, matriz de evolución de preguntas, formato de
  introducción de herramientas, criterio de continuidad y revisión horizontal final.
- La **plantilla** queda como referencia única del esqueleto y la checklist, eliminando la divergencia
  actual entre tres listas parecidas pero distintas.

## Orden sugerido de aplicación

1. README: añadir R1–R9 (los principios primero; el estilo después).
2. Plantilla: absorber D8 y D9 si hace falta ajustar redacción.
3. Guía: aplicar G1–G7 y, al final, el recorte G8 con las remisiones.

Aplicar la guía en último lugar evita remitir a secciones del README que todavía no existen.
