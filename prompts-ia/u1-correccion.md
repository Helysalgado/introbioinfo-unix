Actúa como especialista en enseñanza universitaria de bioinformática, diseño de aula invertida, reproducibilidad científica y comunicación técnica.

Revisa y corrige integralmente la siguiente lección:

`u1-trabajo-reproducible.md`

Utiliza como documentos de referencia, sin modificarlos:

- `Programa-IntroBioinfo-2026.docx`
- `Plan-Clases-BioInfo-2026.xlsx`

El resultado debe ser una versión revisada, completa y lista para publicarse de la lección. Conserva el formato Markdown.

## Contexto del curso

La asignatura es Introducción a la Bioinformática, para estudiantes de primer semestre de la Licenciatura en Ciencias Genómicas. No se requieren conocimientos previos de Unix.

La Unidad 1 se imparte mediante aula invertida:

1. El estudiante lee el material antes de clase.
2. Realiza un primer intento de la práctica.
3. El intento puede estar incompleto y contener errores.
4. En clase se trabaja en formato taller.
5. Durante el taller se revisan intentos, errores y dudas.
6. Después del taller se entrega una versión corregida.

No reduzcas el contenido simplemente por su extensión. La parte conceptual está diseñada para estudiarse antes de clase y el tiempo presencial se dedica a la práctica guiada.

La secuencia pedagógica debe quedar completamente explícita:

**lectura orientada → primer intento → taller guiado → corrección → entrega final**

## Definición del protocolo utilizado en el curso

En este curso, el protocolo no es solamente una propuesta previa ni una lista de comandos.

Es un **protocolo de resolución de un problema bioinformático**: un documento vivo en el que el estudiante:

1. Plantea una pregunta biológica central.
2. La divide en varias subpreguntas.
3. Define qué evidencia necesita para contestar cada subpregunta.
4. Identifica los datos necesarios.
5. Diseña una estrategia de solución.
6. Traduce la estrategia en operaciones y comandos Unix.
7. Ejecuta y documenta los comandos.
8. Verifica los resultados.
9. Interpreta biológicamente cada resultado.
10. Integra las respuestas en una conclusión que contesta la pregunta central.

El protocolo se completa progresivamente durante el curso. Por eso puede contener metodología, comandos, resultados, discusión y conclusiones. Conserva esta concepción y explícala claramente en la lección.

## Objetivos que deben conservarse

La lección debe enseñar al estudiante a:

- Comprender la importancia de la reproducibilidad.
- Distinguir reproducibilidad, replicabilidad, robustez y verificación.
- Reconocer las fases del manejo y análisis de datos.
- Resolver sistemáticamente un problema bioinformático.
- Descomponer una pregunta biológica en subpreguntas abordables.
- Relacionar cada subpregunta con datos, operaciones, evidencia y validación.
- Documentar un protocolo bioinformático en Markdown.
- Organizar datos, procedimientos, resultados y documentación.
- Aplicar principios FAIR y crear metadatos.
- Utilizar asistentes de IA de forma crítica, ética y verificable.
- Formular conclusiones que respondan la pregunta biológica central.

## Correcciones que debes realizar

### 1. Explicar claramente el aula invertida

Reescribe la nota inicial para indicar:

- Qué debe leerse antes de clase.
- Qué debe intentarse antes de clase.
- Que no se espera una solución completa ni perfecta.
- Que los errores y dudas son insumos para el taller.
- Qué debe llevar el estudiante al taller.
- Qué se revisará durante la clase.
- Qué se entregará después del taller.
- Cómo se evaluará cada etapa.

El estudiante debe llevar:

- Su primer intento.
- Al menos una duda concreta.
- Una nota sobre la parte que le resultó más difícil.
- Los errores o resultados inesperados que encontró.

Indica expresamente que el primer intento se valora por la preparación, el esfuerzo y la identificación de dificultades, no por estar completamente correcto.

### 2. Crear una ruta de aprendizaje al inicio

Después de la ficha de la unidad agrega una sección breve que incluya:

- Tiempo estimado de lectura.
- Tiempo estimado para el primer intento.
- Secciones indispensables.
- Secciones de consulta o ampliación.
- Productos mínimos que deben llevarse al taller.
- Productos que se entregarán después del taller.

Distingue claramente entre “comprender”, “consultar”, “intentar” y “entregar”.

### 3. Diferenciar dos procesos complementarios

La versión actual presenta fases generales del análisis de datos, pero no desarrolla suficientemente cómo se resuelve un problema.

Separa y relaciona:

#### A. Fases del manejo y análisis de datos

- Obtención.
- Registro de procedencia.
- Exploración.
- Limpieza o transformación.
- Análisis.
- Conservación.
- Documentación y comunicación.

#### B. Fases de resolución de un problema bioinformático

- Delimitar la pregunta biológica.
- Descomponerla en subpreguntas.
- Definir la evidencia necesaria.
- Identificar los datos requeridos.
- Examinar el formato y los campos disponibles.
- Diseñar la estrategia antes de elegir comandos.
- Traducir la estrategia en operaciones computacionales.
- Seleccionar y ejecutar comandos.
- Probar primero con un caso pequeño.
- Verificar los resultados.
- Interpretar cada respuesta.
- Integrar una conclusión.

Aclara que ambos procesos se relacionan, pero no son equivalentes.

### 4. Enseñar explícitamente cómo resolver un problema

Agrega una sección titulada, por ejemplo:

`## De la pregunta biológica a una solución computacional`

Utiliza un ejemplo biológico sencillo y continuo, preferentemente relacionado con un genoma bacteriano y un archivo GFF o FASTA.

El ejemplo debe mostrar:

- Pregunta biológica central.
- Subpreguntas.
- Evidencia necesaria para cada subpregunta.
- Datos requeridos.
- Operaciones conceptuales.
- Posibles herramientas Unix.
- Resultado esperado.
- Método de verificación.
- Interpretación biológica.
- Conclusión integrada.

Incluye una tabla con esta estructura:

| Subpregunta | Evidencia necesaria | Datos | Operación | Herramienta posible | Validación | Interpretación |
| --- | --- | --- | --- | --- | --- | --- |

No presentes el comando como punto de partida. Primero debe aparecer la pregunta, después la evidencia y finalmente la herramienta.

### 5. Definir formalmente el protocolo del curso

Agrega una definición explícita de “protocolo de resolución de un problema bioinformático”.

Explica que el protocolo:

- Es un documento vivo.
- Se completa durante varias unidades.
- Organiza el razonamiento, no solo los comandos.
- Relaciona cada comando con una subpregunta.
- Registra entradas, operaciones, salidas y validaciones.
- Incluye resultados e interpretación.
- Termina con una conclusión que responde la pregunta central.
- Permite reproducir y evaluar el análisis.

Incluye una tabla que relacione las secciones del protocolo con su función:

| Sección | Función |
| --- | --- |
| Introducción | Presentar contexto y problema |
| Pregunta central | Delimitar qué se quiere responder |
| Subpreguntas | Dividir el problema |
| Datos | Registrar origen, versión, formato e integridad |
| Estrategia | Explicar cómo se resolverá cada subpregunta |
| Comandos | Documentar la ejecución |
| Resultados | Presentar la evidencia obtenida |
| Validación | Comprobar los resultados |
| Discusión | Interpretar su significado biológico |
| Conclusiones | Integrar las respuestas |

Conserva Resultados, Discusión y Conclusiones en la plantilla, pero indica cuáles se completarán en unidades posteriores.

### 6. Corregir la relación entre fases y escritura científica

Utiliza esta correspondencia:

- Pregunta y contexto → Introducción.
- Datos y exploración → Metodología.
- Estrategia y procedimientos analíticos → Metodología.
- Evidencias obtenidas → Resultados.
- Significado biológico y limitaciones → Discusión.
- Respuesta integrada → Conclusiones.
- Documentación y metadatos → atraviesan todo el proceso.

No presentes los procedimientos analíticos como si pertenecieran a Resultados.

### 7. Precisar los conceptos de reproducibilidad

Incluye definiciones breves y ejemplos de:

- Reproducibilidad computacional.
- Replicabilidad.
- Robustez.
- Verificación.

Aclara que la terminología puede variar entre disciplinas y establece las definiciones que utilizará el curso.

Evita usar “repetir” de forma ambigua. Prefiere expresiones como:

- Regenerar resultados con los mismos datos y procedimiento.
- Obtener evidencia compatible mediante un estudio o conjunto de datos independiente.
- Verificar resultados mediante controles o métodos alternativos.

### 8. Mejorar la explicación de los datos fuente

Sustituye expresiones como “los datos no se tocan nunca” por una explicación más precisa:

- Los archivos originales pueden leerse y copiarse.
- No deben editarse, sobrescribirse ni reemplazarse.
- Deben conservar su nombre original y checksum.
- Las transformaciones deben producir archivos nuevos.
- Los datos derivados deben guardarse fuera de `data_source/`.
- Los resultados deben poder regenerarse a partir de los datos fuente.

Puedes proponer una estructura como:

```text
proyecto/
├── README.md
├── data_source/
├── data_processed/
├── src/
├── results/
└── doc/
```

Aclara que la creación mediante comandos Unix y la estructura en el servidor se trabajarán formalmente en la Unidad 2.

### 9. Evitar exigir Unix antes de enseñarlo

En esta unidad no supongas que el estudiante conoce `ls`, `tree`, `mkdir` u otros comandos.

Para el primer intento permite:

- Dibujar el árbol de directorios.
- Escribirlo como bloque de texto.
- Utilizar una carpeta modelo proporcionada por el curso.
- Trabajar con datos pequeños suministrados por la docente.

Durante el taller se puede crear una estructura local de manera guiada. La creación y verificación en el servidor debe quedar para la Unidad 2.

### 10. Mejorar FAIR y los metadatos

Distingue:

- Principios FAIR para datos.
- Buenas prácticas y principios FAIR para software, mencionando FAIR4RS cuando corresponda.

Actualiza la plantilla de metadatos para incluir:

- Nombre original.
- Descripción del contenido.
- Organismo.
- Base de datos de origen.
- URL.
- Identificador o accesión.
- Versión o release.
- Fecha de acceso.
- Formato.
- Tamaño.
- Checksum.
- Licencia o condiciones de uso.
- Responsable.
- Procedimiento de obtención.
- Notas de procedencia.
- Transformaciones realizadas, si existen.

Distingue los campos mínimos que se llenan en U1 de los que se completarán posteriormente.

### 11. Mantener Markdown enfocado en la comunicación

Conserva la enseñanza de:

- Encabezados.
- Párrafos.
- Énfasis.
- Listas.
- Enlaces.
- Tablas.
- Código en línea.
- Bloques de código.

No obligues a incluir tablas o bloques de código en documentos donde no sean útiles. Evalúa que los elementos de Markdown cumplan una función comunicativa.

Mantén Mermaid como contenido opcional o de ampliación, salvo que sea necesario para representar las fases de solución del problema.

### 12. Fortalecer el uso responsable de IA

Conserva:

- Prompting.
- Alucinaciones.
- Validación.
- Transparencia.
- Privacidad.
- Responsabilidad del estudiante.
- Bitácora de IA.

Amplía la estructura de un prompt científico para incluir:

- Contexto.
- Pregunta u objetivo.
- Tipo y formato de los datos.
- Ambiente de ejecución.
- Restricciones.
- Resultado esperado.
- Supuestos.
- Solicitud de explicación.
- Fuentes o documentación que deben consultarse.
- Plan de verificación.

Aclara que un mejor prompt no sustituye la validación independiente.

### 13. Diseñar una actividad auténtica de validación de IA

Además de formular un prompt, presenta una respuesta de IA deliberadamente defectuosa, por ejemplo:

- Un comando inexistente.
- Una opción incorrecta.
- Una referencia inventada.
- Un conteo mal interpretado.
- Una conclusión biológica no sustentada.

Solicita al estudiante:

1. Identificar el posible error.
2. Explicar por qué resulta sospechoso.
3. Consultar una fuente confiable.
4. Probar la propuesta con datos pequeños.
5. Corregirla.
6. Registrar el procedimiento en la bitácora.
7. Concluir si la respuesta era total, parcial o nada confiable.

### 14. Añadir una política de IA

Incluye una política breve con:

- Usos permitidos.
- Usos no permitidos.
- Reglas para tareas.
- Reglas para el proyecto.
- Reglas para exámenes prácticos.
- Protección de datos sensibles.
- Responsabilidad sobre los resultados.
- Declaración obligatoria del uso de IA.

La bitácora debe registrar:

- Fecha.
- Actividad.
- Herramienta y modelo, cuando sea posible.
- Consulta o prompt.
- Respuesta relevante.
- Error o limitación detectada.
- Fuente utilizada para validar.
- Prueba realizada.
- Corrección efectuada.
- Conclusión sobre la confiabilidad.

### 15. Reestructurar todas las prácticas

En cada práctica utiliza exactamente estos apartados:

#### Antes de clase: primer intento

Indica el producto mínimo que debe intentarse y las dudas que deben registrarse.

#### Durante el taller

Explica qué se revisará, comparará, corregirá o completará en clase.

#### Después del taller: entrega final

Indica archivos, nombres, contenido y criterios de entrega.

Evita llamar “entrega” al primer intento si la entrega evaluada ocurre después del taller.

### 16. Añadir una práctica de resolución de problemas

Diseña una actividad breve donde el estudiante reciba un problema bioinformático y tenga que completar, antes de elegir comandos:

- Pregunta central.
- Subpreguntas.
- Evidencia esperada.
- Datos necesarios.
- Operaciones requeridas.
- Posible herramienta.
- Método de validación.
- Posible interpretación.

Durante el taller se compararán estrategias y se discutirá por qué puede haber varias soluciones correctas.

### 17. Crear rúbricas breves

Añade criterios para evaluar:

#### Primer intento

- Evidencia de lectura.
- Esfuerzo auténtico.
- Identificación de dudas.
- Registro de dificultades.
- No se penalizan errores razonables.

#### Participación en el taller

- Revisión del intento.
- Formulación de preguntas.
- Corrección argumentada.
- Comparación de estrategias.
- Registro de aprendizajes.

#### Entrega final

- Claridad de la pregunta.
- Coherencia de las subpreguntas.
- Relación entre preguntas, datos y operaciones.
- Reproducibilidad.
- Metadatos.
- Validación.
- Interpretación biológica.
- Conclusión.
- Claridad del Markdown.
- Declaración de uso de IA.

### 18. Alinear resultados y evidencias

Comprueba que cada resultado de aprendizaje de la ficha tenga al menos una evidencia observable en las prácticas.

Incluye una tabla final:

| Resultado de aprendizaje | Actividad | Evidencia | Momento de evaluación |
| --- | --- | --- | --- |

Si encuentras contradicciones con el programa o el plan de clases, alinea la lección con esos documentos y registra la discrepancia en el informe de cambios.

No modifiques silenciosamente la numeración de tareas si eso rompe la correspondencia con el plan operativo.

### 19. Mejorar accesibilidad y orientación

Agrega cuando resulte pertinente:

- Glosario breve español–inglés.
- Tiempo estimado.
- Alternativa sin conexión para herramientas web.
- Indicaciones para problemas de conectividad.
- Texto alternativo en figuras.
- Ejemplos correctos.
- Ejemplos con errores frecuentes.
- Lenguaje adecuado para estudiantes sin experiencia previa en Unix.

### 20. Limpiar el material para publicación

Elimina o resuelve:

- “FIGURA SUGERIDA”.
- Instrucciones internas para crear ilustraciones.
- Comentarios editoriales dirigidos a la autora.
- Marcadores de contenido pendiente.
- Indicaciones que no correspondan al estudiante.

Sustituye esos elementos por contenido definitivo o elimínalos si no son necesarios.

## Aspectos que debes preservar

No elimines ni debilites:

- El modelo de aula invertida.
- El formato de taller.
- La práctica de primer intento.
- El protocolo como documento vivo.
- La pregunta biológica central.
- La descomposición en subpreguntas.
- La resolución mediante comandos Unix.
- La validación de resultados.
- La interpretación biológica.
- La conclusión.
- La Regla de Oro de la bioinformática.
- Los principios FAIR.
- La bitácora de IA.
- La organización reproducible del proyecto.
- La conexión con el proyecto integrador.

## Restricciones

- No conviertas U1 en una clase anticipada de comandos Unix.
- No presupongas experiencia computacional.
- No reduzcas el contenido solo por su longitud.
- No confundas manejo de datos con resolución de problemas.
- No conviertas el protocolo en una simple plantilla de artículo.
- No elimines Resultados, Discusión o Conclusiones.
- No presentes los comandos como punto de partida del razonamiento.
- No inventes referencias.
- Verifica la exactitud de cualquier referencia nueva.
- Conserva un tono académico, claro, cercano y orientado a primer semestre.
- Usa español consistente, corrigiendo ortografía, puntuación y terminología.
- Conserva el archivo original y produce una versión revisada separada.

## Productos que debes entregar

1. Una versión completa y revisada de `u1-trabajo-reproducible.md`.
2. Un resumen de los principales cambios realizados.
3. Una tabla de correspondencia entre resultados, prácticas y evidencias.
4. Las rúbricas de primer intento, taller y entrega final.
5. Una lista de discrepancias encontradas con el programa o plan de clases.
6. Una lista breve de decisiones que todavía requieran confirmación docente.

## Verificación final

Antes de terminar, comprueba que un estudiante pueda responder claramente:

- ¿Qué debo leer antes de clase?
- ¿Qué debo intentar?
- ¿Qué pasa si no logro terminar?
- ¿Qué dudas debo registrar?
- ¿Qué debo llevar al taller?
- ¿Qué haremos durante el taller?
- ¿Qué debo corregir después?
- ¿Qué archivos debo entregar?
- ¿Cómo se evaluará cada momento?
- ¿Cómo se pasa de una pregunta biológica a subpreguntas?
- ¿Cómo se decide qué datos y operaciones se necesitan?
- ¿Por qué no se empieza eligiendo comandos?
- ¿Cómo se verifica un resultado?
- ¿Cómo se interpreta biológicamente?
- ¿Cómo se construye la conclusión?
- ¿Cuál es la función del protocolo durante todo el análisis?


## Alineación transversal obligatoria

Antes de finalizar la revisión, comprueba la alineación completa entre:

**Objetivo general del curso → propósito de la Unidad 1 → resultados de aprendizaje → contenidos → prácticas → evidencias → criterios de evaluación**

La Unidad 1 debe contribuir explícitamente al objetivo general del curso: resolver problemas bioinformáticos reales mediante un trabajo computacional documentado, reproducible, verificado, científicamente válido y suficientemente robusto.

Utiliza consistentemente estas definiciones:

- **Reproducibilidad:** otra persona puede regenerar los resultados utilizando los mismos datos, procedimientos, comandos y herramientas documentadas.
- **Verificación:** se comprueba que los archivos, comandos, operaciones y resultados intermedios funcionan como se esperaba.
- **Validación:** se demuestra que el procedimiento y la evidencia obtenida realmente permiten responder la pregunta biológica.
- **Robustez:** se comprueba que la conclusión no depende de decisiones frágiles, errores silenciosos o una única comprobación insuficiente.

No presentes estos conceptos solamente como definiciones teóricas. Deben aparecer como acciones observables dentro de las prácticas.

Para cada práctica, comprueba que el estudiante pueda identificar:

1. La pregunta biológica.
2. Las subpreguntas necesarias.
3. La evidencia requerida.
4. Los datos y su procedencia.
5. La estrategia de solución.
6. Los comandos u operaciones utilizados.
7. El procedimiento de verificación.
8. El criterio de validación científica.
9. Alguna comprobación de robustez apropiada al nivel del curso.
10. La interpretación biológica.
11. La conclusión sustentada por la evidencia.
12. La documentación necesaria para reproducir el análisis.

Cuando una comprobación completa de robustez todavía no sea posible por el nivel del estudiante, incluye al menos una actividad inicial, como:

- Comparar dos formas de obtener un mismo conteo.
- Probar el procedimiento con un archivo pequeño de resultado conocido.
- Examinar manualmente una muestra de registros.
- Modificar razonablemente un parámetro y observar si cambia la conclusión.
- Contrastar el resultado con una fuente independiente.
- Identificar supuestos y posibles puntos de fragilidad.

Añade a la tabla de correspondencia estas columnas:

| Objetivo del curso | Resultado de la unidad | Práctica | Evidencia | Reproducibilidad | Verificación | Validación | Robustez |
| --- | --- | --- | --- | --- | --- | --- | --- |

Ningún resultado de aprendizaje debe quedar sin práctica, evidencia y criterio de evaluación. Ninguna práctica debe ser una actividad aislada: debe contribuir claramente a uno o más resultados de la unidad y, mediante ellos, al objetivo general del curso.

Al final de la lección, recuerda al estudiante que estos cuatro principios se retomarán progresivamente en las siguientes unidades y en el proyecto integrador.


