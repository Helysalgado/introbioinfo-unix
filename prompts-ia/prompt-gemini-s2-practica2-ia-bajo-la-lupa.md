# Prompt maestro para Gemini Canvas
## S2 · Práctica 2 — IA bajo la lupa
### Introducción a la Bioinformática · LCG UNAM 2026

Actúa como **diseñador instruccional y desarrollador front-end especializado en bioinformática, pensamiento científico, alfabetización en IA, reproducibilidad y aprendizaje activo**.

Construye DESDE CERO una **app web educativa interactiva, completa y funcional en un único archivo HTML**.

No reutilices código de otras apps ni parches versiones anteriores.

---

# 1. Identidad

Curso:

**Introducción a la Bioinformática — LCG UNAM — 2026**

Sesión:

**Sesión 2**

Actividad:

**Práctica 2**

Nombre de la app:

# IA bajo la lupa

Subtítulo:

> **Pregunta, compara, valida y decide qué puedes confiar**

Encabezado compacto:

```text
[ LCG UNAM 2026 ]   Introducción a la Bioinformática • Sesión 2 • Práctica 2
```

Usar el mismo lenguaje visual de las demás apps del curso:

- azul oscuro;
- badge dorado `LCG UNAM 2026`;
- fondos claros;
- tarjetas limpias;
- tipografía académica y legible;
- código y nombres de archivo en monoespaciada;
- sin estética infantil.

---

# 2. Propósito pedagógico

Esta práctica introduce el **eje de uso responsable de IA** del curso.

El estudiante ya realizó trabajo manual previo:

- en S1 formuló una pregunta y una estrategia;
- en S2 Práctica 1 organizó `pacientes.md`, construyó metadatos y distinguió información comprobable, pendiente y no documentada.

Ahora utilizará IA para generar propuestas alternativas y compararlas con su trabajo previo.

La idea central es:

```text
PRIMERO PIENSO
      ↓
DESPUÉS CONSULTO IA
      ↓
COMPARO
      ↓
DETECTO SUPUESTOS Y ERRORES
      ↓
VALIDO INDEPENDIENTEMENTE
      ↓
CORRIJO
      ↓
DECIDO QUÉ PUEDO CONFIAR
      ↓
DOCUMENTO EL USO DE IA
```

La app NO debe presentar la IA como autoridad ni como enemiga.

Debe enseñar que:

> **Una respuesta plausible no es necesariamente una respuesta correcta.**

y:

> **El trabajo manual previo es una línea base para comparar, no una verdad absoluta. La referencia final se construye con los datos, los metadatos disponibles, fuentes autorizadas, pruebas controladas y razonamiento científico.**

---

# 3. Caso conductor

Mantener el caso:

`pacientes.md`

Dataset sintético de tres registros con las variables:

```text
id
peso
altura
sexo
edad
dx
```

No contiene datos de pacientes reales.

Pregunta científica utilizada:

> **¿Los datos de `pacientes.md` son suficientes para evaluar si el índice de masa corporal está relacionado con el diagnóstico registrado en `dx`?**

Restricciones conocidas:

- solo hay tres registros;
- no deben suponerse las unidades de `peso` y `altura`;
- no debe inventarse el significado de `dx`;
- cada código de diagnóstico aparece una sola vez;
- la extensión `.md` no demuestra por sí sola el formato interno.

---

# 4. Objetivos

Al terminar, el estudiante debe poder:

1. explicar de manera sencilla qué es un LLM;
2. reconocer que una respuesta puede sonar convincente y ser incorrecta;
3. distinguir un prompt vago de un prompt científico verificable;
4. construir un prompt con contexto, objetivo, datos, restricciones, salida y verificación;
5. comparar una respuesta de IA con su trabajo previo;
6. detectar omisiones, inferencias, suposiciones e invenciones;
7. distinguir una operación conceptual de un comando;
8. diseñar una validación independiente;
9. clasificar una respuesta como **confiable, parcialmente confiable o no confiable**;
10. justificar esa clasificación;
11. reconocer qué partes del razonamiento no conviene delegar;
12. producir entradas de `bitacora-ia.md`;
13. descargar el trabajo realizado.

---

# 5. Restricción importante: todavía NO Unix

NO enseñar comandos de terminal.

NO pedir ejecutar comandos.

NO convertir esta práctica en una clase de Unix.

Cuando se analice una estrategia, trabajar con:

```text
pregunta
→ subpregunta
→ evidencia
→ variables
→ operación conceptual
→ validación
```

NO:

```text
pregunta
→ comando
```

---

# 6. Arquitectura de la app

Crear pestañas:

```text
① Entender
② Construir prompt
③ Metadatos + IA
④ Estrategia + IA
⑤ Validar
⑥ Bitácora
✓ Resumen
```

El número aparece UNA sola vez.

La navegación debe ser **libre en todo momento**.

NO bloquear pestañas por progreso.

El estudiante puede explorar, volver, corregir y continuar aunque existan ejercicios pendientes.

---

# 7. Navegación robusta

Implementar con:

```html
<div role="tablist">
```

botones `role="tab"` y paneles `role="tabpanel"`.

Crear UNA función:

```javascript
activateTab(tabName)
```

La navegación NO debe depender de respuestas correctas ni de actividades completas.

Guardar:

```javascript
state.activeTab
```

en `localStorage`.

---

# 8. Estado inicial neutral

CRÍTICO:

Ninguna pregunta debe aparecer contestada.

Ninguna opción:

- verde;
- roja;
- marcada;
- seleccionada;
- con ✓;
- con ✗.

No revelar respuestas antes de que el estudiante actúe.

Cuando una actividad tenga una respuesta esperada:

```text
DECIDIR
→ COMPROBAR
→ FEEDBACK
→ PISTA SI HACE FALTA
→ CORREGIR
```

No mostrar simplemente la solución.

---

# PESTAÑA 1 — ENTENDER

# 9. ¿Qué hace realmente un LLM?

Presentar brevemente:

> Un modelo de lenguaje genera continuaciones plausibles a partir del contexto recibido. Puede producir explicaciones útiles, pero la fluidez y la seguridad del texto no garantizan que lo dicho sea verdadero.

Evitar afirmaciones antropomórficas.

---

# 10. Actividad — Plausible no significa correcto

Mostrar una respuesta deliberadamente defectuosa:

> “Usa el comando `countgenes archivo.gff`, que devuelve el número exacto de genes. Está descrito en Smith et al. (2019), *Journal of Genome Counting*.”

Preguntar al estudiante qué señales deberían despertar sospecha.

Presentar tarjetas seleccionables inicialmente neutrales, por ejemplo:

```text
□ propone un comando que habría que verificar
□ cita una referencia que habría que comprobar
□ está redactado con seguridad
□ incluye un nombre de archivo
□ afirma un resultado exacto sin mostrar evidencia
```

Permitir seleccionar varias.

Después de `Revisar`, explicar que:

- un comando puede ser inventado;
- una referencia puede ser inexistente;
- el tono seguro no es evidencia;
- una respuesta debe contrastarse independientemente.

NO enseñar todavía el comando correcto para contar genes.

---

# 11. Semáforo epistemológico

Presentar afirmaciones y pedir clasificarlas:

```text
✓ Puedo aceptarlo con la evidencia disponible
? Necesito verificarlo
! No debería aceptarlo sin evidencia
```

Ejemplos:

- “La respuesta está bien escrita.”
- “Por estar bien escrita, debe ser correcta.”
- “La referencia citada existe.”
- “El comando mencionado existe.”
- “La IA puede sugerirme una estrategia.”
- “La responsabilidad de validar sigue siendo mía.”

El objetivo es diferenciar:

```text
plausibilidad
≠
evidencia
```

---

# PESTAÑA 2 — CONSTRUIR PROMPT

# 12. Anatomía de un prompt científico

Introducir los componentes:

```text
Contexto
Objetivo
Datos / formato
Ambiente
Restricciones
Resultado esperado
Supuestos
Solicitud de explicación
Fuentes
Plan de verificación
```

No pedir memorizar la lista.

Convertirla en una actividad de construcción.

---

# 13. Prompt Builder

Caso:

> Quieres pedir ayuda para evaluar si `pacientes.md` permite estudiar una posible relación entre IMC y `dx`.

Mostrar bloques/tarjetas desordenados que el estudiante pueda seleccionar o acomodar conceptualmente:

```text
CONTEXTO
Tengo un dataset sintético de tres registros.

OBJETIVO
Quiero evaluar si los datos son suficientes para investigar una posible relación entre IMC y dx.

DATOS
Las columnas son id, peso, altura, sexo, edad y dx.

RESTRICCIÓN
No supongas las unidades de peso y altura.

RESTRICCIÓN
No inventes el significado de dx.

SALIDA
Descompón la pregunta en subpreguntas, evidencia, variables, operaciones y validación.

VERIFICACIÓN
Señala qué afirmaciones requieren confirmación independiente.
```

Agregar distractores, por ejemplo:

```text
Dame la respuesta correcta sin explicar.
Supón que peso está en kg.
Decide qué significa dx.
No menciones limitaciones.
```

El estudiante debe construir un prompt razonable.

---

# 14. Calidad del prompt

Al pulsar:

`Revisar mi prompt`

NO asignar porcentaje.

Mostrar una lista formativa:

```text
✓ Incluiste el objetivo
✓ Describiste los datos
? Falta indicar cómo quieres validar
! Estás autorizando una suposición no sustentada sobre las unidades
```

Después permitir editar.

---

# 15. Prompt final editable

Generar un `<textarea>` con el prompt construido.

Permitir que el alumno lo modifique.

Botones:

```text
📋 Copiar prompt
```

Agregar:

> **Ahora copia este prompt en el asistente de IA autorizado que utilizarás para la práctica.**

No integrar ninguna API de IA en la app.

La app es un **laboratorio para diseñar, registrar y auditar el uso de IA**, no un chatbot.

---

# PESTAÑA 3 — METADATOS + IA

# 16. Regla

Mostrar:

> **Primero a mano, después con IA.**

Recordar:

> Ya construiste una ficha manual de `pacientes.md`. Ahora compararás esa línea base con una propuesta generada por IA.

---

# 17. Prompt base para metadatos

Ofrecer como punto de partida editable:

```text
Tengo un archivo llamado pacientes.md cuyo contenido está separado por comas.
Sus columnas son id, peso, altura, sexo, edad y dx.

Necesito una ficha de metadatos en Markdown con origen, formato, fecha de
acceso, responsable, licencia y un diccionario de variables que incluya
descripción, tipo de dato, unidades y valores permitidos.

No inventes información. Marca como “no documentado” o “pendiente de
confirmar” todo lo que no pueda determinarse a partir de la información
proporcionada.

Explica qué información adicional sería necesario conseguir.
```

Permitir editarlo.

Botón:

`📋 Copiar prompt`

---

# 18. Registrar respuesta real

Campo grande:

> **Pega aquí la respuesta que obtuviste del asistente.**

NO proporcionar una respuesta ficticia como si fuera la del estudiante.

Guardar el texto completo.

Campo:

```text
Herramienta/modelo utilizado:
[                         ]
```

Permitir:

`No conozco la versión`

---

# 19. Auditoría de la respuesta de IA

Crear checklist interactivo basado en estos criterios:

```text
¿Identificó el formato interno y lo distinguió de la extensión .md?
¿Supuso las unidades de peso o altura?
¿Inventó el significado de dx?
¿Supuso fuente, fecha, responsable o licencia?
¿Identificó tipos de datos plausibles?
¿Distinguió información conocida, inferida y faltante?
¿Indicó qué información adicional se necesita?
```

Para cada criterio permitir:

```text
✓ Correcto / sustentado
? Dudoso / requiere verificación
! Error, omisión o invención
○ No aplica
```

y un campo:

`Evidencia o explicación`

---

# 20. Comparación con trabajo manual

Crear dos columnas o paneles:

```text
MI TRABAJO PREVIO
vs.
PROPUESTA DE IA
```

El alumno registra:

```text
Coincidencias:
[textarea]

Aportes útiles de la IA:
[textarea]

Omisiones:
[textarea]

Suposiciones:
[textarea]

Invenciones o errores:
[textarea]

Correcciones realizadas:
[textarea]
```

Mensaje importante:

> **Tu trabajo manual tampoco es una autoridad absoluta. Si existe una discrepancia, valida con el archivo original, los metadatos disponibles, una fuente autorizada o una prueba controlada.**

---

# PESTAÑA 4 — ESTRATEGIA + IA

# 21. Pregunta científica

Mostrar:

> **¿Los datos de `pacientes.md` son suficientes para evaluar si el índice de masa corporal está relacionado con el diagnóstico registrado en `dx`?**

Recordar:

```text
n = 3
```

y:

> Cada código de diagnóstico aparece una sola vez.

---

# 22. Prompt base editable

Mostrar:

```text
Quiero evaluar si los datos de pacientes.md son suficientes para investigar
una posible relación entre el índice de masa corporal y el diagnóstico
registrado en dx.

Ayúdame a descomponer la pregunta en subpreguntas y, para cada una, indica
qué evidencia necesitaría, en qué variables estaría, qué operación conceptual
realizaría y cómo validaría el resultado.

No me des comandos.

No supongas las unidades de peso y altura ni el significado de dx.

Considera que el archivo contiene únicamente tres pacientes y que cada código
de diagnóstico aparece una sola vez.

Señala las limitaciones y los datos adicionales necesarios.
```

Botón:

`📋 Copiar prompt`

Campo para pegar respuesta real de IA.

---

# 23. Auditoría de estrategia

Evaluar interactivamente:

1. ¿Comenzó por la pregunta y no por una herramienta?
2. ¿Propuso subpreguntas relevantes?
3. ¿Relacionó subpregunta con evidencia, variables, operación y validación?
4. ¿Diferenció operación conceptual de comando?
5. ¿Reconoció que las unidades deben confirmarse antes de calcular IMC?
6. ¿Evitó inventar el significado de `dx`?
7. ¿Reconoció que solo existe un paciente por diagnóstico?
8. ¿Evitó afirmar una asociación que los datos no permiten demostrar?
9. ¿Distinguió resultados descriptivos de interpretaciones médicas?
10. ¿Indicó datos, controles o metadatos adicionales necesarios?

Usar nuevamente:

```text
✓ Sustentado
? Requiere verificar
! Problema detectado
○ No aplica
```

con justificación.

---

# 24. Hallazgos nuevos

Preguntar:

```text
¿Qué subpregunta útil propuso la IA que tú no habías considerado?
[textarea]

¿Es realmente pertinente?
[ Sí ] [ Parcialmente ] [ No ]

¿Por qué?
[textarea]
```

Esto debe reforzar que una propuesta novedosa tampoco se acepta automáticamente.

---

# PESTAÑA 5 — VALIDAR

# 25. Ciclo de validación

Mostrar visualmente:

```text
ENTENDER
   ↓
PROBAR
   ↓
CONTRASTAR
   ↓
DECIDIR
   ↓
CORREGIR
   ↺
```

Explicar:

### Entender
¿Puedes explicar con tus palabras la propuesta?

### Probar
¿Puedes utilizar un caso pequeño o de resultado conocido?

### Contrastar
¿Existe documentación oficial, material del curso, archivo original u otra fuente independiente?

---

# 26. Diseña tu validación

Para METADATOS:

```text
¿Qué afirmación de la IA necesitas validar?
[textarea]

¿Qué evidencia independiente utilizarás?
[textarea]

¿Qué encontraste?
[textarea]

¿Tuviste que corregir la respuesta?
[ Sí ] [ Parcialmente ] [ No ]

Corrección:
[textarea]
```

Repetir para ESTRATEGIA.

---

# 27. Escalera de confiabilidad

Solo DESPUÉS de la validación pedir:

```text
¿Cómo clasificas la respuesta de IA?

[ Confiable ]
[ Parcialmente confiable ]
[ No confiable ]
```

No preseleccionar.

Exigir:

```text
Justificación basada en evidencia:
[textarea]
```

No aceptar como justificación suficiente:

```text
“porque sonaba bien”
“porque lo dijo la IA”
“porque coincidió conmigo”
```

Mostrar una pista si aparece una justificación de ese tipo.

---

# 28. Matiz importante

Explicar:

> **Una respuesta puede ser parcialmente confiable:** puede contener elementos útiles y al mismo tiempo incluir supuestos, omisiones o errores.

Y:

> **Coincidir con tu respuesta manual no demuestra por sí mismo que ambas sean correctas.**

---

# PESTAÑA 6 — BITÁCORA

# 29. Construir `bitacora-ia.md`

Generar automáticamente dos entradas a partir del trabajo REAL del alumno:

```text
Entrada 1 — Metadatos con IA
Entrada 2 — Estrategia con IA
```

Cada entrada debe contener:

```markdown
## [fecha] — S2 Práctica 2 — [actividad]

- Objetivo:
- Herramienta/modelo:
- Prompt completo:
- Respuesta relevante:
- Comparación con el trabajo manual:
- Coincidencias:
- Errores/limitaciones:
- Suposiciones o invenciones:
- Fuente/evidencia utilizada para validar:
- Prueba realizada:
- Correcciones:
- Conclusión de confiabilidad:
- Justificación:
```

No inventar campos que el alumno no contestó.

Usar:

`Sin respuesta`

cuando corresponda.

---

# 30. Reflexión

Preguntar:

1. ¿En qué mejoró la IA tu ficha de metadatos o tu estrategia?
2. ¿Qué información omitió, supuso o inventó?
3. ¿Qué error habrías aceptado si no hubieras realizado primero el trabajo manual?
4. ¿Qué partes del análisis no conviene delegar?
5. ¿Qué concepto comprendiste mejor al comparar ambos enfoques?
6. ¿La IA fue más útil para generar, revisar, explicar o detectar alternativas? Justifica.

Guardar todas las respuestas.

---

# PESTAÑA RESUMEN

# 31. Resumen obligatorio

Debe abrir SIEMPRE aunque existan actividades incompletas.

Mostrar:

## Mi proceso

```text
Trabajo previo
→ Prompt
→ Respuesta de IA
→ Comparación
→ Validación independiente
→ Corrección
→ Juicio de confiabilidad
```

## Mis prompts

Mostrar los dos prompts finales.

## Lo que detecté

Separar:

```text
✓ Coincidencias sustentadas
? Aspectos pendientes
! Errores / invenciones / suposiciones
```

## Mi validación

Mostrar evidencia utilizada.

## Mi juicio

```text
Metadatos → [confiable / parcialmente confiable / no confiable / pendiente]

Estrategia → [confiable / parcialmente confiable / no confiable / pendiente]
```

## Mi reflexión

Mostrar respuestas reales.

---

# 32. Descargas obligatorias

Agregar en Resumen:

## ⬇ Descargar `bitacora-ia.md`

Generar el archivo real con las dos entradas.

Y:

## ⬇ Descargar resultados del ejercicio

Generar:

```text
s2-practica2-ia-resultados.md
```

Implementar con JavaScript nativo:

- `Blob`;
- `URL.createObjectURL`;
- `<a download>`.

Sin backend.

---

# 33. Reporte de resultados

Debe contener:

```markdown
# S2 — Práctica 2 — IA bajo la lupa

## Prompt científico construido

[...]

## Actividad A — Metadatos con IA

### Herramienta/modelo
[...]

### Prompt
[...]

### Respuesta
[...]

### Auditoría
[...]

### Comparación con trabajo previo
[...]

### Validación independiente
[...]

### Correcciones
[...]

### Conclusión de confiabilidad
[...]

## Actividad B — Estrategia con IA

[...]

## Reflexión final

[...]

## Registro formativo

Aspectos revisados: [...]
Errores/suposiciones detectados: [...]
Decisiones corregidas: [...]
```

NO incluir:

- calificación;
- porcentaje;
- aprobado/reprobado;
- ranking.

---

# 34. Persistencia

Usar `localStorage`.

Conservar:

- pestaña activa;
- Prompt Builder;
- prompts editados;
- herramienta/modelo;
- respuestas pegadas;
- auditorías;
- comparaciones;
- evidencias;
- validaciones;
- correcciones;
- clasificaciones de confiabilidad;
- reflexiones.

Agregar:

`Reiniciar práctica`

con confirmación.

---

# 35. Política de IA visible

Incluir una tarjeta breve:

```text
IA en este curso

✓ Puede apoyar para entender, explicar, sugerir y revisar.
✓ Su uso debe declararse.
✓ Sus respuestas deben validarse.

✗ No entregues contenido generado que no comprendes.
✗ No aceptes una afirmación solo porque suena convincente.
✗ No compartas datos privados o no públicos.

La responsabilidad del resultado sigue siendo tuya.
```

---

# 36. No automatizar lo que queremos que el estudiante piense

NO usar IA dentro de la propia app para evaluar al estudiante.

NO llamar APIs externas.

NO generar automáticamente la conclusión científica.

NO decidir automáticamente si una respuesta real de ChatGPT/Claude es correcta mediante palabras clave.

La app debe ayudar al estudiante a:

```text
registrar
comparar
cuestionar
validar
justificar
```

El juicio científico sigue siendo del estudiante.

---

# 37. Feedback

Usar feedback formativo.

Ejemplos:

> ✓ Identificaste una afirmación que requiere evidencia independiente.

> ? Que una respuesta coincida con tu primera propuesta no basta para validarla. ¿Qué otra evidencia puedes consultar?

> ! Estás aceptando una unidad que no aparece documentada en el caso.

> ✓ Reconocer una limitación mejora la confiabilidad de tu análisis.

Evitar:

> “¡Perfecto!”
> “La IA está equivocada siempre.”
> “Tu respuesta es correcta porque coincide con la clave.”

---

# 38. Accesibilidad

Implementar:

- HTML semántico;
- `role="tablist"`;
- `role="tab"`;
- `role="tabpanel"`;
- `aria-selected`;
- labels;
- fieldsets;
- legends;
- foco visible;
- teclado;
- `aria-live`;
- contraste suficiente;
- no depender solo del color.

---

# 39. Restricciones técnicas

Entregar un único HTML autónomo con:

- HTML;
- CSS;
- JavaScript.

NO usar:

- React;
- frameworks;
- backend;
- login;
- APIs;
- tracking;
- dependencias externas obligatorias.

Debe funcionar offline, salvo que el alumno abra voluntariamente un asistente externo.

---

# 40. Inicialización robusta

Usar conceptualmente:

```javascript
document.addEventListener("DOMContentLoaded", () => {
    loadState();
    initializeNavigation();
    initializeUnderstanding();
    initializePromptBuilder();
    initializeMetadataAI();
    initializeStrategyAI();
    initializeValidation();
    initializeLog();
    initializeDownloads();

    activateTab(state.activeTab || "entender");
});
```

Un error en una actividad NO debe destruir la navegación.

No reemplazar mediante `innerHTML` el contenedor que contiene las pestañas.

---

# 41. Prueba funcional obligatoria

Antes de entregar:

1. abrir app;
2. sin contestar nada, abrir `Validar`;
3. abrir `Resumen`;
4. abrir `Metadatos + IA`;
5. volver a `Entender`;
6. escribir parcialmente un prompt;
7. cambiar de pestaña;
8. regresar;
9. comprobar que permanece;
10. recargar;
11. comprobar `localStorage`;
12. descargar `bitacora-ia.md`;
13. descargar reporte completo.

Todo debe funcionar.

---

# 42. Validación pedagógica obligatoria

Antes de entregar comprobar:

- no hay respuestas preseleccionadas;
- no hay ejercicios ya “correctos” al abrir;
- la app no inventa respuestas del asistente;
- el alumno pega la respuesta que realmente obtuvo;
- se conserva la regla primero a mano, después IA;
- el trabajo manual se trata como línea base, no como verdad absoluta;
- se distinguen extensión y formato interno;
- no se inventan unidades;
- no se inventa `dx`;
- se reconoce `n = 3`;
- se reconoce un solo registro por diagnóstico;
- no se afirma asociación estadística sustentada con esos datos;
- se distingue descripción de interpretación médica;
- se diferencia operación conceptual de comando;
- la validación es independiente;
- la clasificación de confiabilidad ocurre DESPUÉS de validar;
- `parcialmente confiable` es una opción legítima;
- la bitácora registra el uso de IA;
- Resumen funciona siempre;
- descargas funcionan;
- no hay calificación;
- no hay Unix.

---

# 43. Entregable

Devuélveme el **HTML COMPLETO, autónomo y funcional**.

NO un parche.

NO fragmentos.

NO pidas confirmación.

Construye la app desde cero.

Al final explica brevemente:

1. arquitectura de la actividad;
2. cómo se mantiene libre la navegación;
3. cómo se construyen los prompts;
4. cómo se registran respuestas reales de IA;
5. cómo se realiza la comparación;
6. cómo se documenta la validación independiente;
7. cómo se genera `bitacora-ia.md`;
8. cómo funciona el reporte descargable.

La experiencia debe cerrar con esta idea:

> **La habilidad importante no es obtener una respuesta de IA. Es saber formular una buena pregunta, detectar lo que la respuesta supone, comprobarla con evidencia independiente y decidir responsablemente qué puedes utilizar.**
