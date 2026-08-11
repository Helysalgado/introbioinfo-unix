# Diseño de la Unidad 4 — Procesamiento de archivos biológicos con herramientas Unix

Vamos a diseñar completamente la **Unidad 4** del curso de Introducción a la Bioinformática.

Antes de escribir cualquier contenido debes leer cuidadosamente:

- README del proyecto
- Guía metodológica
- Todas las sesiones desarrolladas de las Unidades 1, 2 y 3
- Plan de clases
- Materiales históricos del curso

No copies los materiales anteriores.

Utilízalos únicamente para:

- comprender la continuidad del curso;
- rescatar buenas ideas;
- mantener coherencia metodológica;
- identificar oportunidades de mejora.

La Unidad 4 debe mantener exactamente la filosofía desarrollada en las unidades anteriores.

---

# Alcance oficial de la unidad

## Propósito

Construir flujos de trabajo transparentes para inspeccionar, filtrar, resumir y transformar archivos de texto biológico.

## Contenidos obligatorios

- Visualización y edición de archivos de texto.
- Delimitadores.
- Encabezados.
- Valores faltantes.
- Entrada estándar.
- Salida estándar.
- Redirecciones.
- Pipes.
- Conteos.
- head
- tail
- cut
- wc
- sort
- uniq
- grep
- expresiones regulares básicas
- tr
- sed
- awk
- Aplicaciones sobre FASTA.
- Aplicaciones sobre GFF3.
- Aplicaciones sobre tablas biológicas.

## Evidencia integradora

Un protocolo ejecutable capaz de responder preguntas sobre un genoma utilizando archivos FASTA y GFF3.

NO modificar el alcance oficial de la unidad.

---

# Punto de partida

La Unidad 3 termina con un protocolo reproducible donde el estudiante ya documentó:

- la pregunta biológica;
- el organismo;
- el ensamblado seleccionado;
- la procedencia de los datos;
- los archivos descargados;
- la verificación mediante checksum;
- la evidencia de reproducibilidad.

Ese protocolo NO termina.

Durante la Unidad 4 se convertirá en un verdadero cuaderno de laboratorio computacional.

El estudiante seguirá ampliando ese mismo documento.

No queremos prácticas independientes.

Queremos un único protocolo que evolucione durante todo el curso.

---

# Cambio de paradigma

La Unidad 4 NO es una unidad para aprender comandos Unix.

La Unidad 4 es una unidad para aprender a analizar un genoma.

Los comandos únicamente aparecen porque ayudan a responder preguntas biológicas.

Nunca deben convertirse en el objetivo de la sesión.

---

# Modelo pedagógico

La unidad se construirá alrededor de un conjunto de preguntas biológicas sobre el mismo genoma.

Por ejemplo:

- ¿De qué tamaño es el genoma?
- ¿Cuántos cromosomas o replicones tiene?
- ¿Qué tipos de features contiene?
- ¿Cuántos tipos distintos existen?
- ¿Cuáles son las fuentes de anotación?
- ¿Cuántos genes existen?
- ¿Cuántas CDS existen?
- ¿Cuántos orígenes de replicación existen?
- ¿Cuántos genes existen en cada cadena?
- Construye un archivo ordenado por cadena y posición genómica.

Estas preguntas representan una única investigación.

No son ejercicios aislados.

---

# Principio pedagógico fundamental

Las preguntas biológicas permanecen prácticamente constantes durante toda la unidad.

Lo que evoluciona es la capacidad analítica del estudiante.

Cada nueva herramienta permite responder mejor la misma pregunta.

Nunca debe sentirse que el estudiante "repite un ejercicio".

Debe sentirse que ahora puede responder la misma pregunta con una estrategia más limpia, más robusta, más reproducible o más expresiva.

---

# Evolución de la capacidad analítica

Las herramientas deben aparecer gradualmente.

No porque exista una jerarquía absoluta entre ellas.

Sino porque cada una resuelve una limitación observada en la estrategia anterior.

Por ejemplo:

Nivel inicial

cut

↓

El estudiante descubre la estructura del archivo y las columnas.

Observa limitaciones.

Por ejemplo:

- aparecen comentarios;
- aparecen registros irrelevantes;
- obtiene demasiada información.

↓

Ahora aparece grep.

Puede eliminar comentarios y seleccionar únicamente los registros relevantes.

↓

Después aparecen sort y uniq.

Ahora puede resumir información.

↓

Posteriormente uniq -c.

Ahora puede cuantificar.

↓

Finalmente awk.

Ahora puede expresar condiciones complejas sobre distintas columnas y resolver preguntas más específicas.

El estudiante debe percibir claramente esa evolución.

---

# Filosofía de las sesiones

Cada sesión debe seguir aproximadamente este flujo.

Pregunta biológica

↓

Hipótesis

↓

Datos necesarios

↓

Estrategia disponible hasta este momento

↓

Limitaciones observadas

↓

Nueva herramienta

↓

Refinamiento del análisis

↓

Resultados

↓

Interpretación biológica

↓

Actualización del protocolo

Cada sesión debe terminar planteando naturalmente la siguiente.

---

# Organización de la unidad

NO organizar las sesiones por comandos.

NO quiero sesiones llamadas:

- grep
- awk
- sed
- sort

Quiero sesiones organizadas por etapas del análisis del genoma.

Cada sesión debe representar un avance en la investigación.

Las preguntas pueden volver a aparecer porque la estrategia evoluciona.

---

# Protocolo

Cada sesión agregará nuevas secciones al protocolo.

Por ejemplo:

- Pregunta biológica.
- Hipótesis.
- Estrategia de análisis.
- Comandos ejecutados.
- Resultados.
- Interpretación.
- Limitaciones.
- Mejoras respecto a la estrategia anterior.
- Nuevas preguntas.

Al finalizar la unidad el estudiante deberá tener un verdadero cuaderno de laboratorio computacional.

---

# Interpretación

Todas las actividades deben terminar con una interpretación biológica sencilla.

No basta con obtener una salida.

El estudiante debe responder:

- ¿Qué significa este resultado?
- ¿Qué aprendimos acerca del genoma?
- ¿La evidencia apoya nuestra hipótesis?
- ¿Qué nuevas preguntas aparecen?

No buscamos interpretaciones avanzadas.

Solo aquellas sustentadas por la evidencia obtenida.

---

# Introducción de comandos

Cada vez que aparezca una herramienta nueva deberá incluir:

## Sintaxis mínima

```bash
...
```

**¿Qué hace?**

Máximo dos líneas.

**¿Por qué aparece en esta sesión?**

Explica qué limitación de la estrategia anterior resuelve.

🤖 **Consulta a ProfeUnix Bioinfo**

Sugiere uno o dos prompts para explorar opciones adicionales.

No convertir la guía en un manual de Unix.

---

# Delimitación con las unidades posteriores

La Unidad 4 termina cuando el estudiante es capaz de construir flujos interactivos para responder preguntas biológicas sobre un genoma.

NO desarrollar todavía:

- BLAST.
- alineamientos.
- homología.
- ortólogos.
- parálogos.
- scripting.
- variables.
- parámetros.
- ciclos.
- automatización.

Esos temas pertenecen a las siguientes unidades.

---

# Primera tarea

NO escribas todavía ninguna sesión.

Primero diseña completamente la arquitectura de la unidad.

Entrega:

## 1. Visión general de la unidad

Explica cuál es el hilo conductor.

¿Cuál es el cambio de paradigma respecto a la Unidad 3?

---

## 2. Propuesta de sesiones

Propón las sesiones necesarias.

Cada sesión debe incluir:

- propósito;
- preguntas biológicas que responderá;
- herramientas nuevas;
- herramientas reutilizadas;
- qué limitación del análisis resuelve;
- cómo evoluciona la capacidad analítica del estudiante;
- qué parte del protocolo se actualizará;
- cómo prepara la siguiente sesión.

---

## 3. Matriz de evolución de las preguntas

Construye una tabla donde aparezcan todas las preguntas biológicas de la unidad.

Para cada una indica:

- en qué sesión aparece por primera vez;
- con qué estrategia inicial se responde;
- cómo se refina en sesiones posteriores;
- qué herramienta permite cada refinamiento;
- en qué sesión queda completamente resuelta.

Esta matriz es obligatoria.

Será el eje de diseño de toda la unidad.

---

## 4. Evidencia integradora

Explica cómo el protocolo evoluciona sesión tras sesión.

Describe exactamente qué nuevos apartados incorpora el estudiante después de cada sesión.

---

## Importante

Detente después de presentar la arquitectura completa de la Unidad 4.

No desarrolles todavía ninguna sesión.

Esperaré mi aprobación antes de comenzar el desarrollo detallado de S10.


