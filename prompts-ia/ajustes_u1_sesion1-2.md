Actúa como especialista en diseño curricular universitario, enseñanza de bioinformática, aula invertida, reproducibilidad científica, evaluación por competencias y uso responsable de inteligencia artificial.

Tu tarea es revisar y mejorar la Unidad 1 del curso Introducción a la Bioinformática:

- Unidad que se debe editar: `contenidos-2026/u1-trabajo-reproducible-v2.md`
- Programa de referencia: `Programa-IntroBioinfo-2026.docx`
- Plan operativo de referencia: `Plan-Clases-BioInfo-2026.xlsx`
- Materiales auxiliares: `introBioInfo/ejemplos/`, `introBioInfo/referencias/` y `contenidos-2026/images/`

## Objetivo

Genera una versión mejorada de la Unidad 1 que:

1. Mantenga su profundidad conceptual.
2. Sea viable para dos sesiones presenciales de dos horas.
3. Distribuya explícitamente el trabajo de aula invertida antes, entre y después de las sesiones.
4. Alinee resultados de aprendizaje, actividades, evidencias y rúbricas.
5. Corrija inconsistencias conceptuales, terminológicas y de materiales.
6. Conserve el tono claro, cercano y apropiado para estudiantes de primer semestre sin experiencia previa en Unix.

No reduzcas sustancialmente el contenido solo por su longitud. Prioriza una mejor secuencia, señalización y distribución de la carga.

## Restricciones

- No modifiques el programa ni el plan de clases; úsalos como referencias normativas.
- Edita únicamente la Unidad 1 y, si es necesario, los materiales auxiliares explícitamente mencionados en este prompt.
- No inventes datos, referencias, fechas, unidades, licencias ni metadatos.
- Conserva las figuras existentes cuando sean pertinentes.
- Conserva la integración temprana de reproducibilidad, Markdown, FAIR, organización de proyectos e IA.
- No introduzcas comandos de Unix que todavía no se hayan enseñado.
- Mantén la regla pedagógica “primero a mano, después con IA”, pero con la precisión indicada más adelante.
- Registra cualquier contradicción que no pueda resolverse sin modificar el programa o el plan.

## Ajustes requeridos

### 1. Reorganizar la unidad alrededor de dos sesiones

Sustituye la organización genérica “antes de clase / durante el taller / después del taller” por una secuencia explícita:

#### Antes de la sesión 1

- Lectura de las secciones conceptuales necesarias para comprender reproducibilidad, fases del análisis, resolución de problemas, protocolo y Markdown.
- Lectura del capítulo 1 de Buffalo.
- Primer intento de la Práctica 1.
- Tiempo orientativo total: 2–2.5 horas.

#### Sesión 1 presencial — 2 horas

- Bienvenida y encuadre de la unidad.
- Revisión de reproducibilidad y fases del análisis.
- Taller de Markdown.
- Revisión de pregunta central, subpreguntas y estructura inicial del protocolo.
- Retroalimentación sobre el primer intento de la Práctica 1.

#### Entre las sesiones 1 y 2

- Lectura de las secciones sobre organización del proyecto, FAIR, metadatos e IA.
- Primer intento manual de las Prácticas 2 y 3.
- Inicio de la Práctica 4 después de completar el trabajo manual.
- Tiempo orientativo total: 2.5–3 horas.

#### Sesión 2 presencial — 2 horas

- Taller sobre FAIR, metadatos y organización reproducible.
- Comparación de estrategias para resolver el problema.
- Discusión de limitaciones de los datos.
- Comparación entre trabajo manual y respuestas de IA.
- Validación y corrección argumentada de las respuestas de IA.

#### Después de la sesión 2

- Corrección y entrega de las Tareas 1 y 2.
- Finalización de la bitácora de IA.
- Autoevaluación y cierre de la unidad.
- Tiempo orientativo total: 1.5–2 horas.

Presenta esta secuencia en una tabla clara al inicio de la unidad. Indica qué se debe leer, intentar, llevar, corregir y entregar en cada momento.

### 2. Corregir la estimación de carga

Elimina o modifica la afirmación de que todo el primer intento requiere solamente 60–90 minutos.

Distingue claramente:

- Tiempo de lectura del material de la unidad.
- Tiempo de lectura de Buffalo.
- Tiempo de elaboración de cada práctica.
- Tiempo antes de S1.
- Tiempo entre S1 y S2.
- Tiempo de corrección posterior.

Aclara que los tiempos son estimaciones y pueden variar según la experiencia del estudiante.

### 3. Corregir la ruta de aprendizaje

La sección “Comunicar con Markdown” debe aparecer entre las secciones indispensables, porque la Tarea 1 exige producir documentos Markdown.

Marca solamente la subsección de Mermaid como consulta o ampliación opcional.

La ruta debe responder sin ambigüedad:

- ¿Qué leo antes de S1?
- ¿Qué intento antes de S1?
- ¿Qué llevo a S1?
- ¿Qué hago entre sesiones?
- ¿Qué llevo a S2?
- ¿Qué entrego después de S2?

### 4. Ajustar los resultados de aprendizaje al alcance real de U1

Revisa los resultados para que describan lo que realmente se demuestra durante esta unidad.

En particular:

- Cambia “resolver de forma sistemática un problema bioinformático sencillo” por una formulación como “diseñar una estrategia sistemática para resolver un problema bioinformático sencillo”.
- Distingue entre diseñar una validación y ejecutarla.
- Si la conclusión todavía es provisional, indícalo expresamente.
- Decide si la replicabilidad se demostrará de forma aplicada en U1 o si solo se introducirá conceptualmente y se demostrará después.
- Evita declarar como alcanzado un resultado que solo se evaluará en unidades posteriores.

### 5. Alinear resultados, prácticas y evidencias

Revisa los anexos y las tablas de correspondencia.

Para cada resultado de aprendizaje, especifica:

- Actividad donde se practica.
- Evidencia concreta.
- Criterio de evaluación.
- Momento de evaluación.
- Nivel alcanzado en U1: comprensión, diseño anticipado o ejecución.

No atribuyas a U1 conteos, comandos, validaciones ejecutadas o análisis completos que todavía no se realizan.

Si RA11 exige una conclusión, incorpora explícitamente en la Práctica 3 una conclusión provisional que no exceda la evidencia disponible.

### 6. Mejorar las rúbricas

Sustituye las rúbricas genéricas de “Sí / Parcial / No” por criterios con descriptores breves y observables.

Crea, como mínimo:

- Rúbrica del primer intento.
- Rúbrica de participación en el taller.
- Rúbrica de Tarea 1.
- Rúbrica de Tarea 2.

Las rúbricas deben distinguir claramente:

- Logrado.
- Parcialmente logrado.
- Aún no logrado.

Incluye criterios específicos para:

- Pregunta y subpreguntas.
- Estrategia.
- Protocolo.
- Reporte de lectura.
- Estructura del proyecto.
- Metadatos y diccionario de variables.
- Reconocimiento de información no documentada.
- Uso funcional de Markdown.
- Bitácora de IA.
- Validación de respuestas de IA.
- Conclusión provisional y limitaciones.

Aclara si el primer intento tiene valor formativo, puntos por preparación o una calificación.

### 7. Corregir el ejemplo de metadatos

Revisa conjuntamente:

- `introBioInfo/ejemplos/pacientes.md`
- `introBioInfo/ejemplos/metadatos_pacientes.md`

El ejemplo actual de metadatos no debe afirmar información que no aparece en los datos. Corrige o reemplaza cualquier afirmación inventada, incluyendo:

- Nombre incorrecto del archivo.
- Número incorrecto de filas.
- Unidades no documentadas.
- Fechas no documentadas.
- Fuente no documentada.
- Responsable no documentado.
- Licencia no documentada.
- Significado no documentado de `dx`.
- Valores permitidos no confirmados.

Utiliza expresiones como:

- “No documentado”.
- “Pendiente de confirmar”.
- “Inferido del contenido, pero no confirmado”.
- “No puede determinarse a partir del archivo”.

El ejemplo corregido debe modelar exactamente la conducta que se espera del estudiante.

Si se conserva el ejemplo incorrecto, etiquétalo explícitamente como “ejemplo defectuoso para auditar” y proporciona después una versión corregida.

### 8. Precisar la regla “primero a mano, después con IA”

Conserva esta secuencia pedagógica, pero no llames al primer intento manual “verdad de referencia”, porque también puede contener errores.

Utiliza una formulación como:

> El trabajo manual constituye la línea base para la comparación. La referencia final se construye mediante el archivo original, los metadatos disponibles, la documentación autorizada, pruebas controladas y la retroalimentación docente.

La validación debe ser independiente tanto de la IA como del primer intento del estudiante.

### 9. Corregir la explicación de FAIR

No describas FAIR como un “estándar de calidad”. Preséntalo como:

> Un conjunto de principios guía para mejorar la localización, accesibilidad, interoperabilidad y reutilización de datos y otros objetos digitales de investigación.

Aclara que los principios FAIR:

- No constituyen por sí mismos un estándar ni una especificación técnica.
- No equivalen a datos abiertos o gratuitos.
- Buscan favorecer el uso por personas y máquinas.
- No se cumplen automáticamente por guardar un archivo de metadatos en una carpeta local.
- Requieren varias acciones complementarias.

En la tabla que relaciona FAIR con las fases del manejo de datos, sustituye expresiones como “aquí se aplica cada principio” por “acciones que contribuyen a este principio”.

Conserva y cita correctamente a Wilkinson et al. (2016).

### 10. Incorporar o reubicar los metadatos de software

El programa menciona metadatos de datos y de software, pero las prácticas actuales solo generan metadatos de datos.

Elige una de estas soluciones y justifícala:

- Incorporar en `README.md` una sección mínima de entorno computacional: herramienta, versión, sistema, fuente, fecha y condiciones de uso.
- Crear una plantilla mínima de metadatos de software que se complete progresivamente en unidades posteriores.
- Ajustar el resultado de U1 para indicar que en esta unidad se crean metadatos de datos y se introduce conceptualmente el registro de software.

No exijas versiones de herramientas que todavía no se hayan utilizado.

Conserva la referencia a FAIR4RS, explicando que el software requiere considerar versión, evolución, ejecutabilidad y dependencias.

### 11. Unificar la estructura de directorios

Usa consistentemente:

```text
data/source/
data/processed/
src/
results/
doc/
```

Evita alternar entre `data_source` y `data/source/`.

Como el programa usa `data_source`, incluye una nota docente o de alineación que explique la discrepancia y que la convención operativa adoptada por la unidad es `data/source/`.

No modifiques el programa sin autorización.

### 12. Reparar referencias y enlaces a materiales

Comprueba todos los archivos mencionados en la unidad, incluyendo:

- Plantilla de protocolo.
- Ejemplo de reporte de *E. coli*.
- Archivo `pacientes.md`.
- Ejemplo de metadatos.
- PDF de Buffalo.
- Imágenes.
- Sitios externos.

No presentes una ruta como código si el estudiante necesita abrirla. Utiliza enlaces Markdown funcionales.

Asegúrate de que las rutas sean válidas en el sitio final. Si durante la migración a Quarto será necesario copiar recursos, deja una nota técnica clara para la publicación.

Genera una lista de enlaces o recursos que no puedan resolverse.

### 13. Reducir la redundancia del cierre sin eliminar la evaluación formativa

La unidad puede conservar un cierre amplio, pero distribúyelo adecuadamente:

- Antes del taller: 4–5 preguntas diagnósticas esenciales.
- Durante el taller: reto aplicado o discusión de caso.
- Después de S2: checklist de evidencias y semáforo de salida.
- Actividades opcionales: preguntas adicionales de práctica.

Evita que rúbrica, checklist, cuestionario, reto, escala y semáforo evalúen repetidamente lo mismo.

Indica claramente qué actividades son obligatorias, cuáles son formativas y cuáles son opcionales.

### 14. Aclarar la lectura de Buffalo

Distingue entre:

- Lectura obligatoria con reporte: capítulo 1.
- Lectura o consulta dirigida: capítulo 2.
- Secciones o páginas específicas, si es posible.
- Tiempo estimado de cada lectura.

No llames indistintamente “lectura base” a los capítulos 1 y 2 si solo uno genera una evidencia evaluada.

### 15. Corregir la terminología de los datos de pacientes

Si los datos fueron creados para el ejercicio y no provienen de personas reales, utiliza:

> Conjunto de datos sintéticos, creado exclusivamente con fines educativos.

Evita llamarlos “anonimizados” o “anónimos” si no se originaron en pacientes reales.

No asignes significado médico a `dx` sin un diccionario documentado.

### 16. Conservar las fortalezas de la unidad

No elimines los siguientes elementos:

- Diferencia entre reproducibilidad, replicabilidad, verificación, validación y robustez.
- Orden pregunta → evidencia → datos → operación → herramienta.
- Separación entre datos originales y derivados.
- Protocolo como documento vivo.
- Uso funcional de Markdown.
- Introducción temprana a FAIR.
- Validación independiente de la IA.
- Bitácora de IA.
- Reconocimiento de que datos insuficientes también pueden conducir a una conclusión científicamente válida.
- Aula invertida basada en primeros intentos, errores y corrección argumentada.

## Proceso de trabajo

1. Lee completamente los tres documentos principales.
2. Revisa los materiales auxiliares mencionados por la unidad.
3. Presenta primero una tabla breve con:
   - Problema.
   - Ubicación.
   - Cambio propuesto.
   - Archivo afectado.
4. Modifica la Unidad 1 sección por sección.
5. Conserva una copia o diff que permita revisar los cambios.
6. Corrige los materiales auxiliares únicamente cuando estén explícitamente dentro del alcance.
7. No modifiques los documentos de referencia.
8. Al terminar, realiza una verificación integral.

## Verificación final obligatoria

Antes de entregar, confirma que:

- La unidad está distribuida en dos sesiones de dos horas.
- La carga autónoma está declarada por momento.
- Las prácticas se realizan en un orden posible.
- Ninguna práctica depende de un producto que aún no se ha elaborado.
- Los resultados de aprendizaje coinciden con lo que realmente se demuestra.
- Cada resultado tiene actividad, evidencia y criterio.
- Las rúbricas contienen descriptores observables.
- No se presenta información inventada en los metadatos.
- El trabajo manual se trata como línea base, no como verdad absoluta.
- FAIR se describe como principios guía.
- Se distingue entre metadatos de datos y de software.
- Se usa consistentemente `data/source/`.
- Todos los enlaces y archivos referenciados existen o quedan señalados para corrección.
- Las actividades obligatorias, formativas y opcionales están identificadas.
- La lectura del capítulo 1 se distingue de la consulta del capítulo 2.
- Los datos ficticios se denominan “sintéticos”.
- Se mantienen las fortalezas conceptuales y pedagógicas de la unidad.
- El contenido continúa siendo apropiado para estudiantes de primer semestre que parten de cero en Unix.

## Entregables

Entrega:

1. La versión corregida de `u1-trabajo-reproducible-v2.md`.
2. Los materiales auxiliares corregidos, si fueron necesarios y estaban autorizados.
3. Un resumen numerado de los cambios realizados.
4. Una lista de discrepancias que requieren modificar el programa o el plan de clases.
5. Una lista de enlaces o recursos pendientes.
6. Una estimación final de la carga:
   - Antes de S1.
   - Durante S1.
   - Entre S1 y S2.
   - Durante S2.
   - Después de S2.


