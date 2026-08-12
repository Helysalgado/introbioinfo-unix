# Unidad 1 — Trabajo reproducible y comunicación técnica

::: {.callout-note title="Aula invertida"}
Esta unidad se estudia en dos sesiones. S1 es la primera del curso y se
lee **junto con la sesión**; a partir de S2 el orden es el habitual: leer antes, practicar en el
taller, corregir después. Los primeros intentos son formativos; las entregas calificadas son las
**Tareas 1 y 2**.
:::

Antes de tocar un dato biológico, esta unidad establece **qué distingue un análisis del que uno puede
fiarse**. Es la única del curso que no usa Unix: se trabaja con Markdown, con datos sintéticos y con
el razonamiento que ordenará todo lo demás. Lo que aquí se decide —una pregunta, una estrategia, un
protocolo, una estructura de proyecto— es lo que la Unidad 2 llevará al servidor y las unidades
siguientes irán refinando.

## Ficha de la unidad

| Elemento | Descripción |
| --- | --- |
| **Sesiones** | S1–S2 |
| **Competencias** | A (Trabajo reproducible y comunicación científica) · G (Uso responsable de IA) |
| **Propósito** | Establecer desde el arranque una cultura de trabajo reproducible y la capacidad de resolver y comunicar un problema bioinformático de forma documentada, verificable y científicamente válida. |
| **Contribución al objetivo del curso** | Sienta las bases para *resolver problemas bioinformáticos reales mediante un trabajo computacional documentado, reproducible, verificado y suficientemente robusto*. |
| **Ajustes integrados** | Introducción al prompting científico y uso responsable de IA |
| **Lecturas** | Buffalo (2015): **Cap. 1 — obligatorio** (genera el reporte de lectura de la Tarea 1; ~45–60 min). **Cap. 2 — consulta dirigida** (organización de proyectos y Markdown; se consulta al hacer las secciones 4–6; ~20–30 min). |

### Resultados de aprendizaje (demostrables)

Al terminar la unidad, el estudiante es capaz de:

1. **Explicar** la importancia de la reproducibilidad en la investigación.
2. **Distinguir** reproducibilidad, replicabilidad, verificación, validación y robustez. La
   replicabilidad se introduce de forma **conceptual**; verificación, validación y robustez se
   **practican como acciones** al nivel de esta unidad (sobre datos pequeños y de forma anticipada).
3. **Reconocer** las fases del manejo y análisis de datos.
4. **Diseñar** una estrategia sistemática para resolver un problema bioinformático sencillo (se
   **diseña**, todavía **no se ejecuta**).
5. **Descomponer** una pregunta biológica en subpreguntas abordables.
6. **Relacionar** cada subpregunta con datos, operaciones, evidencia y un método de validación
   (validación **diseñada**, no ejecutada).
7. **Documentar** un protocolo bioinformático en Markdown.
8. **Organizar** datos, procedimientos, resultados y documentación de forma reproducible.
9. **Crear** metadatos de datos aplicando los **principios guía FAIR**, e **introducir de forma
   conceptual** el registro de metadatos de software.
10. **Utilizar** asistentes de IA de forma crítica, ética y verificable.
11. **Formular** una **conclusión provisional** que no exceda la evidencia disponible, señalando sus
    **limitaciones**.

---

## Ruta de aprendizaje de la unidad

La unidad se cursa en **dos sesiones presenciales de 2 horas**, con trabajo autónomo antes, entre y
después. La siguiente tabla indica **qué leer, qué intentar, qué llevar y qué entregar** en cada
momento. Los tiempos son **estimaciones** y varían según tu experiencia previa.

| Momento | Qué leer | Qué intentar (a mano) | Qué llevar / entregar | Tiempo estimado |
| --- | --- | --- | --- | --- |
| **Antes de la sesión 1** | Secciones 1–5 (reproducibilidad, fases, resolución de problemas, protocolo y Markdown) + **Cap. 1 de Buffalo** | **Práctica 1** (protocolo inicial + reporte de lectura) | Tu primer intento de la Práctica 1 y tus dudas | Lectura unidad ~60–75 min · Buffalo Cap. 1 ~45–60 min · Práctica 1 ~30–45 min → **~2–2.5 h** |
| **Sesión 1 (2 h)** | — | — | Bienvenida y encuadre · repaso de reproducibilidad y fases · **taller de Markdown** · revisión de pregunta, subpreguntas y estructura del protocolo · retroalimentación de la Práctica 1 | 2 h presencial |
| **Entre S1 y S2** | Sección 6 (organización del proyecto), el apartado FAIR/metadatos (secciones 2 y 4.2) y sección 7 (IA); consulta el **Cap. 2 de Buffalo** | **Prácticas 2 y 3** a mano; después, **Práctica 4** (con IA) | Tus intentos de las Prácticas 2–4 y tus dudas | Lectura ~30–45 min · Práctica 2 ~30–45 min · Práctica 3 ~30–45 min · Práctica 4 ~30–45 min → **~2.5–3 h** |
| **Sesión 2 (2 h)** | — | — | Taller de FAIR, metadatos y organización · comparación de estrategias · discusión de limitaciones de los datos · comparación trabajo manual vs. IA · validación y corrección argumentada | 2 h presencial |
| **Después de la S2** | — | — | **Entrega** de las Tareas 1 y 2 corregidas · cierre de la `bitacora-ia.md` · autoevaluación (sección 11) | **~1.5–2 h** |

**Secciones indispensables (comprender):** 1, 2, 3, 4, **5** y 6, más la 7. La **Tarea 1 exige
producir documentos en Markdown**, por eso la sección 5 es indispensable. Solo la subsección **5.3
(Mermaid)** es de ampliación opcional.

::: {.callout-tip}
Cuatro verbos guían esta ruta. **Comprender** las secciones indispensables; **consultar**
lo opcional cuando lo necesites; **intentar** las prácticas aunque no las termines; y **entregar**
solo después del taller. Si algo no te sale, anótalo: esa nota vale para el taller.
:::

---

## Módulos de la unidad

### [S1 — Documentar: Markdown y las fases del análisis de datos](u1-s1-documentar-markdown-fases.md)

Qué es la bioinformática y por qué exige habilidades con datos; los cuatro conceptos que el curso usa
con precisión —reproducibilidad, replicabilidad, verificación, validación—; las fases del análisis y
las de resolución de un problema; y cómo se pasa de una pregunta biológica a una estrategia escrita.
Cierra con Markdown como herramienta de comunicación. Desarrolla la **Tarea 1**.

### [S2 — Organizar: buenas prácticas FAIR e introducción al prompting científico](u1-s2-organizar-fair-ia.md)

Los principios FAIR y qué acciones concretas contribuyen a cada uno; la ficha de metadatos con su
diccionario de variables; la organización reproducible del proyecto; y la cápsula de IA que abre el
eje transversal del curso: qué es un modelo de lenguaje, qué son las alucinaciones, cómo se formula
un prompt científico y cómo se valida su respuesta. Desarrolla la **Tarea 2**.

::: {.callout-note title="dos cortes deliberados"}
Los principios FAIR y la ficha de metadatos podrían leerse junto
a las fases del análisis y al protocolo, en S1. Van en S2 porque es donde el plan sitúa su
aplicación: FAIR se ve en dos momentos —el estándar junto al manejo de datos, la aplicación junto
al protocolo—, y los metadatos son parte de la Tarea 2, no de la 1.
:::


## Cierre de la unidad

Este cierre te permitirá comprobar no solo si reconoces los conceptos, sino si puedes **aplicarlos y
mostrar evidencia** de tu trabajo. Realiza primero las actividades sin consultar las respuestas;
después abre la retroalimentación y corrige lo necesario.

Cada actividad tiene un **momento** y un **tipo** para que no se evalúe lo mismo dos veces:

| Actividad | Momento sugerido | Tipo |
| --- | --- | --- |
| **11.2** Comprueba tu comprensión (preguntas 1–5) | **Antes** de la sesión 1 (diagnóstico) | Formativa |
| **11.2** Preguntas 6–9 | Cuando avances en la unidad | Opcional |
| **11.3** Reto final (¿qué permiten concluir los datos?) | **Durante/después** de la sesión 2 | Formativa (aplicada) |
| **11.1** Evidencias de mis habilidades | **Después** de la sesión 2 | **Obligatoria** (checklist de cierre) |
| **11.5** Semáforo de salida | **Después** de la sesión 2 | **Obligatoria** (autoevaluación de salida) |
| **11.4** Resultado de la autoevaluación | Al terminar 11.2 | Formativa (orientación) |

::: {.callout-note}
Lo **obligatorio** del cierre es la sección 11.1 (evidencias) y el semáforo 11.5; lo demás
es **formativo u opcional**. La **calificación** proviene de las Tareas 1 y 2 (rúbricas 9.3 y 9.4),
no de este cierre.
:::

---

### Evidencias de mis habilidades

Marca una habilidad solamente si puedes señalar una evidencia concreta. En la última columna escribe
el nombre del archivo, sección o producto donde puede revisarse.

| Habilidad que puedo demostrar | Evidencia esperada | Mi evidencia | Estado |
| --- | --- | --- | --- |
| Explico por qué la reproducibilidad es necesaria en la investigación | Explicación o ejemplo donde un resultado pueda regenerarse | | ☐ |
| Distingo reproducibilidad, replicabilidad, verificación, validación y robustez | Clasificación correcta de casos y justificación | | ☐ |
| Diferencio el manejo de datos de la resolución de un problema | Identificación de acciones correspondientes a cada proceso | | ☐ |
| Parto de una pregunta biológica antes de elegir herramientas | Pregunta central y subpreguntas en `protocolo.md` | | ☐ |
| Relaciono subpreguntas con evidencia, datos, operaciones y validación | Tabla de estrategia corregida | | ☐ |
| Documento un protocolo científico en Markdown | `protocolo.md` organizado y correctamente renderizado | | ☐ |
| Organizo un proyecto reproducible | Árbol con `data/source/`, `data/processed/`, `src/`, `results/` y `doc/` | | ☐ |
| Conservo los datos originales intactos | Archivo original ubicado en `data/source/` y derivados separados | | ☐ |
| Redacto metadatos y un diccionario de variables | `pacientes-metadatos.md` | | ☐ |
| Aplico los principios FAIR sin confundirlos con “datos abiertos” | Justificación de qué principios se aplican y cómo | | ☐ |
| Utilizo IA de forma crítica, verificable y declarada | Entrada completa de `bitacora-ia.md` | | ☐ |
| Formulo conclusiones que no exceden la evidencia | Conclusión y limitaciones claramente separadas | | ☐ |

---

### Comprueba tu comprensión

#### Pregunta 1 — Reproducible no significa necesariamente correcto

Un análisis produce exactamente el mismo resultado cada vez que se ejecuta, pero utiliza por error
una columna equivocada del archivo.

¿Cuál afirmación es correcta?

- A. Es válido porque siempre produce el mismo resultado.
- B. Es reproducible, pero no necesariamente válido.
- C. Es replicable porque se ejecutó varias veces.
- D. Es robusto porque el resultado no cambia.

<details>
<summary>Ver retroalimentación</summary>

**Respuesta: B.**

El resultado puede regenerarse con los mismos datos y procedimientos, por lo que el análisis es
reproducible. Sin embargo, utilizar una columna equivocada impide que la evidencia responda
correctamente la pregunta biológica, por lo que el análisis no está validado.

</details>

---

#### Pregunta 2 — Replicabilidad

Otro grupo estudia una población independiente, utiliza nuevos datos y obtiene evidencia compatible
con la conclusión del estudio original.

¿Qué propiedad está evaluando principalmente?

- A. Reproducibilidad.
- B. Replicabilidad.
- C. Verificación.
- D. Documentación.

<details>
<summary>Ver retroalimentación</summary>

**Respuesta: B.**

La replicabilidad utiliza un estudio, población o conjunto de datos independiente. La
reproducibilidad, en cambio, busca regenerar resultados usando los mismos datos y procedimientos
documentados.

</details>

---

#### Pregunta 3 — Verificación

Después de descargar un archivo, comparas su checksum con el valor publicado por el repositorio.

¿Qué estás haciendo?

- A. Interpretando biológicamente el resultado.
- B. Validando la pregunta biológica.
- C. Verificando la integridad del archivo.
- D. Replicando el estudio.

<details>
<summary>Ver retroalimentación</summary>

**Respuesta: C.**

El checksum permite comprobar que el archivo descargado está completo y no cambió durante la
transferencia. Es una acción de verificación.

</details>

---

#### Pregunta 4 — Validación

Quieres conocer cuántos genes contiene un archivo GFF, pero cuentas todas sus líneas, incluyendo
comentarios, regiones y otros tipos de elementos.

Aunque el comando funcione, ¿cuál es el principal problema?

- A. El archivo no es FAIR.
- B. La operación no está validada para responder la pregunta.
- C. El resultado no puede documentarse.
- D. El archivo original fue replicado.

<details>
<summary>Ver retroalimentación</summary>

**Respuesta: B.**

Contar todas las líneas no equivale necesariamente a contar genes. Es necesario comprobar qué
registros representan genes y diseñar una operación que produzca la evidencia adecuada para
responder la pregunta.

</details>

---

#### Pregunta 5 — Orden del razonamiento

¿Cuál es el orden más adecuado para diseñar un análisis bioinformático?

- A. Herramienta → comando → datos → pregunta → evidencia.
- B. Datos → herramienta → pregunta → resultado → interpretación.
- C. Pregunta → evidencia → datos → operación → herramienta.
- D. Comando → resultado → pregunta → validación.

<details>
<summary>Ver retroalimentación</summary>

**Respuesta: C.**

Primero se define qué se quiere responder; después, qué evidencia permitiría responderlo, dónde se
encuentra esa evidencia, qué operación conceptual se necesita y, finalmente, qué herramienta puede
realizarla.

</details>

---

#### Pregunta 6 — Organización de los datos

Tienes un archivo original y una versión limpia en la que corregiste formatos y eliminaste registros
inválidos.

¿Dónde debería guardarse cada archivo?

- A. Ambos en `results/`.
- B. El original en `data/source/` y el derivado en `data/processed/`.
- C. El original en `src/` y el derivado en `doc/`.
- D. Ambos en `data/source/`, reemplazando el archivo anterior.

<details>
<summary>Ver retroalimentación</summary>

**Respuesta: B.**

Los datos originales deben conservarse intactos en `data/source/`. Los datos limpios o transformados
son archivos derivados y deben guardarse por separado en `data/processed/`.

</details>

---

#### Pregunta 7 — FAIR

¿Cuál afirmación describe correctamente los principios FAIR?

- A. Todo dato FAIR debe ser gratuito y público.
- B. FAIR significa que los datos no necesitan metadatos.
- C. FAIR busca que los datos sean localizables, accesibles, interoperables y reutilizables.
- D. FAIR solo se aplica a grandes repositorios internacionales.

<details>
<summary>Ver retroalimentación</summary>

**Respuesta: C.**

FAIR significa *Findable, Accessible, Interoperable and Reusable*. Un recurso FAIR no tiene que ser
necesariamente abierto o gratuito, pero debe contar con metadatos, condiciones de acceso claras,
formatos adecuados y suficiente documentación para su reutilización.

</details>

---

#### Pregunta 8 — Uso crítico de IA

Un asistente afirma que el código `C12` de `pacientes.md` corresponde a una enfermedad específica,
aunque no recibió un diccionario de códigos ni una fuente clínica.

¿Qué deberías hacer?

- A. Aceptar la respuesta porque el código parece médico.
- B. Copiar la interpretación y citar al asistente.
- C. Marcar el significado como no documentado y buscar una fuente o diccionario confiable.
- D. Eliminar la columna porque la IA no pudo interpretarla.

<details>
<summary>Ver retroalimentación</summary>

**Respuesta: C.**

El significado de `dx` no puede inferirse únicamente por la apariencia del código. La IA podría
estar asociándolo con un sistema real sin evidencia de que ese sistema se utilice en el archivo. La
respuesta debe contrastarse con los metadatos, el responsable de los datos o un diccionario
documentado.

</details>

---

#### Pregunta 9 — Robustez

Obtienes el mismo conteo mediante dos estrategias independientes y ambas coinciden con un caso
pequeño cuyo resultado conoces.

¿Qué propiedad estás fortaleciendo principalmente?

- A. Robustez.
- B. Accesibilidad.
- C. Replicabilidad.
- D. Formato Markdown.

<details>
<summary>Ver retroalimentación</summary>

**Respuesta: A.**

Obtener el resultado por caminos diferentes y probar con un caso conocido reduce la posibilidad de
que la conclusión dependa de un error silencioso o de una única estrategia frágil.

</details>

---

### Reto final — ¿Qué permiten concluir los datos?

Considera nuevamente el archivo ficticio `pacientes.md`:

| id | peso | altura | sexo | edad | dx |
| --- | ---: | ---: | --- | ---: | --- |
| 001 | 65 | 170 | F | 23 | A23 |
| 002 | 78 | 180 | M | 45 | B15 |
| 003 | 70 | 165 | F | 38 | C12 |

Un compañero afirma:

> “El diagnóstico `C12` está relacionado con un índice de masa corporal mayor porque el paciente
> `003` tiene el valor más alto.”

Antes de aceptar o rechazar la afirmación, responde:

1. ¿Qué evidencia sí puede obtenerse con los datos disponibles?
2. ¿Qué unidades necesitas confirmar antes de calcular el IMC?
3. ¿Qué significa la variable `dx` y dónde debería estar documentada?
4. ¿Cuántos pacientes hay para cada diagnóstico?
5. ¿Es posible distinguir una asociación de una diferencia individual?
6. ¿Qué datos adicionales necesitarías?
7. ¿Qué métodos usarías para verificar los cálculos?
8. ¿Cuál sería una conclusión que no exceda la evidencia?

#### Mi respuesta

**Evidencia que sí puedo obtener:**

...

**Información o metadatos faltantes:**

...

**Operaciones necesarias:**

...

**Método de validación:**

...

**Conclusión:**

...

<details>
<summary>Ver retroalimentación</summary>

Una respuesta adecuada debería reconocer que:

- Es posible describir el peso, la altura, la edad y el sexo de cada paciente.
- El IMC solo puede calcularse válidamente después de confirmar las unidades.
- El significado de `dx` debe obtenerse de los metadatos o de un diccionario documentado.
- Cada diagnóstico aparece una sola vez.
- No existe replicación dentro de los grupos de diagnóstico.
- No hay un grupo de comparación.
- Las diferencias también podrían deberse a edad, sexo u otras variables no registradas.
- Es posible identificar qué paciente tiene el valor calculado más alto, pero no atribuirlo al
  diagnóstico.
- Se necesitan más pacientes por diagnóstico, controles y variables clínicas relevantes.
- Concluir que la evidencia es insuficiente también es un resultado científicamente válido.

Una posible conclusión sería:

> Los datos permiten describir las características biométricas de los tres pacientes, pero no
> permiten determinar si el IMC está asociado con el diagnóstico. Solo existe un paciente por
> categoría y el significado de `dx` no está documentado. Se requieren más observaciones, controles
> y metadatos clínicos antes de evaluar la relación propuesta.

</details>

---

### Resultado de la autoevaluación

Asigna un punto por cada respuesta correcta de la sección 11.2.

| Resultado | Interpretación | Acción recomendada |
| --- | --- | --- |
| 8–9 respuestas correctas | Comprensión sólida | Continúa con el reto final y documenta tus evidencias |
| 6–7 respuestas correctas | Comprensión en desarrollo | Revisa las preguntas incorrectas y explica por qué cambiaste tu respuesta |
| 4–5 respuestas correctas | Hay conceptos que necesitan refuerzo | Retoma las secciones relacionadas y consulta tus ejemplos |
| 0–3 respuestas correctas | Necesitas acompañamiento | Lleva tus dudas al taller y resuelve nuevamente el cuestionario |

El número de respuestas correctas es solo una orientación. Lo más importante es que puedas explicar
por qué una respuesta es correcta y mostrar evidencia de que aplicaste esa habilidad.

---

### Semáforo de salida

Marca el nivel que describe mejor tu situación actual.

| Color | Significado | Marca |
| --- | --- | --- |
| 🟢 Verde | Puedo explicarlo, aplicarlo y mostrar una evidencia | ☐ |
| 🟡 Amarillo | Comprendo la idea, pero todavía necesito ayuda para aplicarla | ☐ |
| 🔴 Rojo | Aún no puedo explicarla o no sé cómo comenzar | ☐ |

#### Habilidad en verde

La habilidad que puedo demostrar mejor es:

...

La evidencia que puedo mostrar es:

...

#### Habilidad en amarillo o rojo

La habilidad que necesito reforzar es:

...

Mi duda concreta es:

...

La acción que realizaré antes de comenzar la Unidad 2 es:

...


### Tareas a entregar (después del taller)

- **Tarea 1** — `protocolo.md` iniciado (pregunta, subpreguntas y estrategia, de las Prácticas 1 y 3)
  y `reporte-lectura.md` del Cap. 1 de Buffalo (2015).
- **Tarea 2** — estructura del proyecto con metadatos (campos mínimos, Práctica 2) y `bitacora-ia.md`
  con las entradas de la Práctica 4 (más cualquier otro uso de IA que hayas registrado).

### Lecturas / consulta previa para la Unidad 2

- Buffalo (2015), Cap. 3 ("Remedial Unix Shell"): filosofía de Unix y por qué se usa en bioinformática.
- Instalar un cliente de transferencia de archivos (FileZilla) si aún no lo tienes.

::: {.callout-note}
Los cuatro principios —reproducibilidad, verificación, validación y robustez— se retoman
progresivamente en las siguientes unidades y culminan en el **proyecto integrador**.
:::

---

## Anexo A. Correspondencia resultado–actividad–evidencia–criterio

**Nivel en U1:** *comprensión* (se entiende), *diseño anticipado* (se planea, aún no se ejecuta) o
*ejecución* (se realiza en esta unidad).

| Resultado de aprendizaje | Actividad | Evidencia | Criterio (rúbrica) | Momento | Nivel en U1 |
| --- | --- | --- | --- | --- | --- |
| RA1 Importancia de la reproducibilidad | Lectura + discusión; cuestionario 11.2 | Participación; respuestas | 9.2; autoevaluación | Taller | comprensión |
| RA2 Distinguir los cinco conceptos (replicabilidad conceptual) | Cuestionario 11.2; protocolo | Respuestas; `protocolo.md` | 9.3; 11.2 | Taller/entrega | comprensión |
| RA3 Fases del manejo de datos | Práctica 2 | Estructura + metadatos | 9.4 (estructura) | Entrega | comprensión / ejecución |
| RA4 Diseñar una estrategia | Práctica 3 | Tabla de estrategia en `protocolo.md` | 9.3 (estrategia) | Entrega | diseño anticipado |
| RA5 Descomponer en subpreguntas | Práctica 3 | Subpreguntas en `protocolo.md` | 9.3 (pregunta y subpreguntas) | Entrega | diseño anticipado |
| RA6 Relacionar subpregunta–evidencia–datos–validación | Práctica 3 | Tabla de estrategia | 9.3 (estrategia) | Entrega | diseño anticipado |
| RA7 Documentar en Markdown | Prácticas 1–2 | `protocolo.md`, `reporte-lectura.md` | 9.3 (Markdown) | Entrega | ejecución |
| RA8 Organización reproducible | Práctica 2 | Árbol del proyecto | 9.4 (estructura) | Entrega | ejecución (a mano) |
| RA9 Metadatos de datos (FAIR) + software conceptual | Práctica 2 | `pacientes-metadatos.md`; sección de entorno en `README.md` | 9.4 (metadatos) | Entrega | ejecución (datos) / comprensión (software) |
| RA10 IA crítica y verificable | Práctica 4 | `bitacora-ia.md` | 9.4 (bitácora, validación) | Entrega | ejecución |
| RA11 Conclusión provisional y limitaciones | Práctica 3; reto 11.3 | Conclusión + limitaciones en `protocolo.md` | 9.3 (conclusión) | Entrega | diseño anticipado |

## Anexo B. Alineación transversal

| Objetivo del curso | Resultado de la unidad | Práctica | Evidencia | Reproducibilidad | Verificación | Validación | Robustez |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Resolver problemas bioinformáticos documentados y reproducibles | RA4–RA6, RA11 | Práctica 3 | Estrategia y conclusión en `protocolo.md` | Protocolo permite regenerar el análisis | Probar con caso pequeño conocido | La estrategia responde la pregunta | Obtener el conteo por dos caminos |
| Trabajo verificado y válido | RA2, RA10 | Práctica 4 | Bitácora de validación de IA | Registro reproducible del proceso | Contrastar con fuente confiable | Confirmar que la respuesta resuelve la duda | Concluir grado de confiabilidad |
| Datos gestionados con buenas prácticas | RA3, RA8, RA9 | Práctica 2 | Metadatos + estructura | Datos fuente recuperables | Checksum (reservado) | Metadatos suficientes para reusar | Original intacto + derivados aparte |

::: {.callout-note}
Cuando aún no sea posible una comprobación completa de robustez, basta una actividad
inicial: comparar dos formas de obtener un mismo conteo, probar con un archivo pequeño de resultado
conocido, examinar a mano una muestra de registros, cambiar un parámetro y ver si cambia la
conclusión, o contrastar con una fuente independiente.
:::

---

## Glosario

| Español | Inglés | Definición breve |
| --- | --- | --- |
| Reproducibilidad | Reproducibility | Regenerar resultados con los mismos datos y procedimientos |
| Replicabilidad | Replicability | Evidencia compatible con datos o estudios independientes |
| Verificación | Verification | Comprobar que archivos, comandos y resultados funcionan como se espera |
| Validación | Validation | Demostrar que el procedimiento responde la pregunta |
| Robustez | Robustness | Que la conclusión no dependa de decisiones frágiles |
| Metadatos | Metadata | Datos que describen un dato |
| Checksum / suma de verificación | Checksum | Huella digital para comprobar integridad de un archivo |
| Procedencia | Provenance | Origen e historia de un dato |
| Feature (elemento) | Feature | Elemento anotado del genoma (gen, región, etc.) |
| Cadena / hebra | Strand | Hebra del ADN donde se ubica un feature (`+` o `-`) |

---

## Referencias

- Buffalo, V. (2015). *Bioinformatics Data Skills: Reproducible and Robust Research with Open Source
  Tools*. O'Reilly Media. — Cap. 1 (reproducibilidad, robustez, Regla de Oro) y Cap. 2 (organización
  de proyectos, documentación, Markdown). Disponible en `referencias/bioinformatics-data-skills.pdf`.
- Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for scientific data management and
  stewardship. *Scientific Data*, 3, 160018. doi:10.1038/sdata.2016.18.
- Miller, G. (2006). A Scientist's Nightmare: Software Problem Leads to Five Retractions. *Science*,
  314(5807), 1856–1857. doi:10.1126/science.314.5807.1856.
- Cyranoski, D. (2015, 18 de febrero). *Haruko Obokata: the STAP cells controversy*. The Guardian.
  <https://www.theguardian.com/science/2015/feb/18/haruko-obokata-stap-cells-controversy-scientists-lie>
- The Japan Times (2024, 9 de abril). *10 years since STAP*.
  <https://www.japantimes.co.jp/news/2024/04/09/japan/science-health/10-years-since-stap/>
- Popper, K. (1959). *The Logic of Scientific Discovery*. Hutchinson & Co.
- Collado-Torres, L., Nellore, A., Kammers, K., Ellis, S. E., Taub, M. A., Hansen, K. D., Jaffe,
  A. E., Langmead, B., & Leek, J. T. (2017). Reproducible RNA-seq analysis using recount2. *Nature
  Biotechnology*, 35(4), 319–321. doi:10.1038/nbt.3838.
- Barker, M., Chue Hong, N. P., Katz, D. S., et al. (2022). Introducing the FAIR Principles for
  research software (FAIR4RS). *Scientific Data*, 9, 622. doi:10.1038/s41597-022-01710-x.
- Noble, W. S. (2009). A Quick Guide to Organizing Computational Biology Projects. *PLoS
  Computational Biology*, 5(7), e1000424. doi:10.1371/journal.pcbi.1000424. (organización de
  directorios: `data/`, `results/`, `src/`, `doc/`).
- GO-FAIR. FAIR Principles. <https://www.go-fair.org/fair-principles/>
- Markdown — página oficial (John Gruber). <https://daringfireball.net/projects/markdown/>
- Markdown Guide. <https://www.markdownguide.org/>
- StackEdit — editor de Markdown en línea. <https://stackedit.io>
- Mermaid — documentación oficial. <https://mermaid.js.org/>
