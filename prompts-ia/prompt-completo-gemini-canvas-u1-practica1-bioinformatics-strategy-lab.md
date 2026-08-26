# Prompt completo para Gemini Canvas — U1 · Práctica 1: “Bioinformatics Strategy Lab”

Actúa como **diseñador instruccional y desarrollador front-end especializado en bioinformática, pensamiento científico, análisis de datos, reproducibilidad y aprendizaje activo**.

Construye un recurso HTML interactivo para integrarlo al sitio web del curso:

**Introducción a la Bioinformática — LCG, UNAM — 2026**

Este recurso corresponde a la **Unidad 1 / Sesión 1** y transforma la actividad existente:

# Práctica 1 — Diseñar una estrategia antes de elegir herramientas

en una experiencia interactiva de razonamiento científico.

Genera directamente la **versión final completa**. No asumas que existe un HTML previo.

---

# 1. Propósito pedagógico

NO conviertas esta práctica en un ejercicio para calcular IMC ni en un tutorial de Python.

La habilidad central es aprender a diseñar una estrategia de análisis **antes de elegir comandos, lenguajes o herramientas**.

La progresión conceptual que debe quedar visible es:

```text
pregunta biológica
→ subpreguntas
→ evidencia necesaria
→ datos disponibles
→ datos/metadatos faltantes
→ operaciones
→ validación
→ interpretación
→ herramienta
```

Debe reforzar especialmente:

> **La herramienta se elige después de comprender la pregunta, la evidencia y los datos.**

Y:

> **Tener columnas aparentemente relevantes no significa necesariamente tener evidencia suficiente para responder una pregunta científica.**

---

# 2. Caso de estudio

La práctica utiliza el archivo:

```text
pacientes.md
```

El recurso debe mostrar esta tabla de trabajo:

| id | peso | altura | sexo | edad | dx |
|---|---:|---:|---|---:|---|
| 001 | 65 | 170 | F | 23 | A23 |
| 002 | 78 | 180 | M | 45 | B15 |
| 003 | 70 | 165 | F | 38 | C12 |

No inventes metadatos que no se proporcionaron.

En particular, el estudiante debe detectar como parte de su razonamiento que necesita confirmar, entre otras cosas:

- qué representa exactamente `peso`;
- sus unidades;
- qué representa exactamente `altura`;
- sus unidades;
- qué significa `dx`;
- qué significan los códigos `A23`, `B15` y `C12`;
- si el tamaño y estructura del conjunto de datos permiten evaluar una asociación.

---

# 3. Pregunta central

Usa exactamente:

> **¿Los datos de `pacientes.md` son suficientes para evaluar si el índice de masa corporal está relacionado con el diagnóstico registrado en `dx`?**

No contestes esta pregunta al inicio.

La práctica debe hacer que el estudiante construya evidencia antes de emitir un dictamen.

---

# 4. Nombre del interactivo

Usa:

# Bioinformatics Strategy Lab

Subtítulo:

> **Antes del comando, construye la estrategia**

Texto introductorio:

> Has recibido un pequeño conjunto de datos y una pregunta científica. Tu tarea no es empezar a calcular: primero debes decidir qué necesitas saber, qué evidencia sería suficiente y qué limitaciones tienen los datos.

La estética debe ser:

- científica;
- universitaria;
- moderna;
- clara;
- visual;
- juvenil sin parecer infantil.

---

# 5. Arquitectura general

Organiza la experiencia en **seis etapas** y una **pestaña final obligatoria de Resumen**:

```text
ETAPA 1
Primer dictamen
        ↓
ETAPA 2
Auditoría de los datos
        ↓
ETAPA 3
Construir la cadena de evidencia
        ↓
ETAPA 4
Diseñar operaciones y validación
        ↓
ETAPA 5
Evaluar qué permiten concluir los datos
        ↓
ETAPA 6
Dictamen científico final
        ↓
RESUMEN
```

Navegación:

```text
1 Reto
2 Datos
3 Evidencia
4 Estrategia
5 Interpretación
6 Dictamen
Resumen
```

La pestaña **Resumen debe existir SIEMPRE al final**.

No usar:

- puntos;
- vidas;
- medallas;
- ranking;
- competencia;
- calificación numérica.

---

# 6. Regla general de retroalimentación

Para decisiones estructuradas utiliza:

```text
respuesta
→ feedback visual
→ pista
→ segundo intento
→ explicación
```

## Correcto

- verde;
- icono `✓`;
- texto como `Decisión sustentada`.

## Incorrecto

- rojo;
- icono `✗`;
- texto como `Revisa esta decisión`.

El color nunca será la única señal.

Ante el primer error:

1. registrar la respuesta;
2. NO revelar inmediatamente la correcta;
3. mostrar una pista;
4. permitir segundo intento;
5. después explicar.

Registrar durante toda la sesión:

- primer intento;
- segundo intento, si existe;
- uso de pistas;
- respuesta final;
- respuestas abiertas;
- cambios de opinión.

---

# 7. Etapa 1 — Primer dictamen

Mostrar la tabla completa y la pregunta central.

Preguntar:

> **Solo con una primera inspección, ¿crees que estos datos son suficientes para evaluar la relación entre IMC y `dx`?**

Opciones:

- Sí
- No
- Todavía no puedo decidir

No tratar `Todavía no puedo decidir` como evasión.

La práctica busca enseñar que, antes de conocer unidades, significado de variables y estructura de los grupos, **suspender el juicio puede ser científicamente apropiado**.

Después preguntar:

> **¿Por qué elegiste esa respuesta?**

Campo de texto.

Guardar esta respuesta para compararla con el dictamen final.

No mostrar todavía una “solución”.

---

# 8. Etapa 2 — Auditoría de los datos

Título:

# ¿Qué sabes realmente de estas columnas?

Mostrar nuevamente la tabla.

Cada encabezado debe ser interactivo:

```text
id | peso | altura | sexo | edad | dx
```

Al seleccionar una columna, abrir una ficha:

```text
Nombre:
Valores observados:
Qué creo que representa:
¿Conozco las unidades/códigos?
¿Qué necesito confirmar?
```

---

# 9. Auditoría de `peso`

Mostrar:

```text
65
78
70
```

Preguntar:

> **¿Puedes asumir solamente por los valores que `peso` está expresado en kilogramos?**

Opciones:

- Sí
- No

Respuesta esperada:

**No**

Pista:

> Un valor plausible no documenta una unidad.

Explicación:

> Podemos formular la hipótesis de que sean kilogramos, pero para un análisis reproducible debemos confirmarlo en los metadatos.

---

# 10. Auditoría de `altura`

Mostrar:

```text
170
180
165
```

Preguntar:

> **¿Puedes calcular correctamente el IMC sin confirmar la unidad de `altura`?**

Respuesta esperada:

**No**

Después mostrar:

```text
IMC = peso / altura²
```

y preguntar:

> **Si estos valores fueran centímetros, ¿qué transformación sería necesaria antes de aplicar la fórmula estándar del IMC?**

Respuesta conceptual:

> Convertir centímetros a metros.

No conviertas todavía la práctica en una sesión de cálculo.

---

# 11. Auditoría de `dx`

Mostrar:

```text
A23
B15
C12
```

Preguntar:

> **¿Sabes qué diagnóstico representa cada código solo con este archivo?**

Respuesta:

**No**

Pista:

> El código existe, pero ¿dónde está su significado?

Explicación:

> Una categoría sin documentación puede utilizarse computacionalmente como etiqueta, pero no puede interpretarse biológicamente con seguridad.

---

# 12. Auditoría del tamaño y estructura de la muestra

Hacer que el estudiante observe:

```text
3 pacientes
3 códigos dx diferentes
```

Preguntar:

> **¿Cuántas observaciones hay por cada valor de `dx` en este archivo?**

Respuesta:

```text
1
```

Después:

> **¿Comparar tres valores individuales equivale a demostrar una asociación entre IMC y diagnóstico?**

Respuesta:

**No**

Explicación:

> Observar diferencias entre individuos no es lo mismo que establecer una asociación entre variables. El tamaño y la estructura de la muestra limitan las conclusiones posibles.

No entrar todavía en pruebas estadísticas específicas.

---

# 13. Semáforo de evidencia

Al terminar la auditoría construir automáticamente un panel:

# Estado actual de la evidencia

Ejemplo conceptual:

```text
¿Existe peso?                    ✓ Sí
¿Existe altura?                  ✓ Sí
¿Conocemos sus unidades?         ? Falta confirmar
¿Existe dx?                      ✓ Sí
¿Sabemos qué significa dx?       ? Falta confirmar
¿Hay múltiples observaciones
por diagnóstico?                 ✗ No en estos datos
```

No depender únicamente de colores.

Usar también:

- ✓ confirmado;
- ? falta confirmar;
- ✗ limitación detectada.

---

# 14. Etapa 3 — Construir la cadena de evidencia

Esta es la actividad central.

No mostrar una tabla vacía desde el inicio.

El estudiante debe construir visualmente una estrategia:

```text
PREGUNTA CENTRAL
        ↓
SUBPREGUNTAS
        ↓
EVIDENCIA
        ↓
DATOS
        ↓
OPERACIONES
```

Permitir varias ramas.

---

# 15. Rama A — ¿Puedo obtener IMC?

Presentar:

> **Para estudiar una posible relación entre IMC y diagnóstico, ¿qué necesitas establecer primero?**

Opciones:

- que puedo calcular un IMC interpretable para cada paciente;
- qué comando de Unix usar;
- qué librería de Python instalar;
- qué gráfica se ve mejor.

Esperada:

**que puedo calcular un IMC interpretable para cada paciente**

Después construir:

```text
¿Puedo calcular IMC?
        ↓
Necesito peso y altura
        ↓
Necesito confirmar unidades
        ↓
Conversión si corresponde
        ↓
IMC = peso / altura²
        ↓
Validar valores obtenidos
```

---

# 16. Rama B — ¿Puedo interpretar `dx`?

Construir:

```text
¿Qué significa dx?
        ↓
Necesito documentación de los códigos
        ↓
A23 / B15 / C12
        ↓
significado biológico/diagnóstico
```

Preguntar:

> **¿Puedes saltar esta rama y tratar los códigos como diagnósticos interpretables?**

Respuesta:

**No**

Explicación:

> Puedes manipular etiquetas sin conocer su significado, pero no interpretar científicamente el resultado.

---

# 17. Rama C — ¿Puedo evaluar una relación?

Construir:

```text
¿Existe relación IMC ↔ dx?
        ↓
Necesito IMC interpretable
+
dx interpretable
+
estructura de datos adecuada
        ↓
comparación/análisis
        ↓
evaluación de evidencia
        ↓
conclusión limitada por los datos
```

Hacer visible que:

```text
calcular IMC
≠
demostrar asociación
```

y:

```text
observar diferencias individuales
≠
demostrar relación entre variables
```

---

# 18. Actividad “Detecta el salto”

Presentar pequeñas estrategias.

## Caso 1

```text
Pregunta:
¿IMC está relacionado con dx?

↓
Abrir Python
```

Respuesta:

**Salto de razonamiento**

Explicación:

> Python es una herramienta. Todavía no has establecido qué evidencia necesitas ni si los datos permiten obtenerla.

## Caso 2

```text
Pregunta:
¿Puedo calcular IMC?

↓
Necesito peso y altura con unidades conocidas

↓
Aplicar la operación apropiada

↓
Validar resultados
```

Respuesta:

**Ruta razonada**

## Caso 3

```text
Pregunta:
¿Qué significa dx?

↓
Hacer una gráfica
```

Respuesta:

**Salto de razonamiento**

## Caso 4

```text
Pregunta:
¿Qué significa dx?

↓
Consultar/documentar los metadatos de los códigos
```

Respuesta:

**Ruta razonada**

---

# 19. Etapa 4 — Diseñar operaciones y validación

Título:

# ¿Qué harías y cómo comprobarías que salió bien?

Ahora sí permitir hablar de operaciones.

Para cada rama, pedir:

```text
Subpregunta
Evidencia
Datos
Operación
Validación
Interpretación esperada
Herramienta candidata
```

IMPORTANTE:

La **herramienta debe aparecer al final**, no al principio.

---

# 20. Constructor de estrategia

Permitir construir al menos estas filas conceptuales:

## IMC

```text
Subpregunta:
¿Puedo obtener un IMC interpretable por paciente?

Evidencia:
IMC por individuo

Datos:
peso + altura + unidades

Operación:
confirmar unidades → convertir si hace falta → calcular IMC

Validación:
revisar unidades, fórmula, valores imposibles o inesperados

Interpretación:
obtener una variable derivada; todavía no demuestra asociación

Herramienta:
puede decidirse después
```

## Diagnóstico

```text
Subpregunta:
¿Qué representa dx?

Evidencia:
definición de los códigos

Datos:
dx + metadatos/documentación

Operación:
relacionar códigos con su significado

Validación:
comprobar que todos los códigos estén documentados

Interpretación:
permite interpretar las categorías
```

## Relación

```text
Subpregunta:
¿Los datos permiten evaluar una relación IMC-dx?

Evidencia:
comparación sustentada entre IMC y categorías dx

Datos:
IMC + dx + estructura/tamaño de muestra

Operación:
explorar/comparar según lo que los datos permitan

Validación:
comprobar número de observaciones y limitaciones

Interpretación:
no exceder la evidencia disponible
```

No obligues a usar exactamente estas frases si el estudiante escribe equivalentes.

---

# 21. Elección tardía de herramienta

Después de construir la estrategia preguntar:

> **¿En qué momento tiene sentido elegir una herramienta?**

Opciones:

- al leer la pregunta;
- antes de inspeccionar los datos;
- después de definir evidencia, datos y operaciones;
- siempre debe elegirse Python.

Respuesta:

**después de definir evidencia, datos y operaciones**

Mensaje:

> **La herramienta implementa una operación; no sustituye el razonamiento que decide qué operación necesitas.**

---

# 22. Etapa 5 — Evaluar qué permiten concluir los datos

Título:

# Evidencia, inferencia o exceso de conclusión

Presentar afirmaciones y pedir clasificarlas como:

- Sustentada por los datos
- Posible hipótesis / requiere más evidencia
- No sustentada

No convertirlo en un examen estadístico.

---

# 23. Afirmaciones de interpretación

## Afirmación A

> `pacientes.md` contiene columnas de peso y altura.

Respuesta:

**Sustentada por los datos**

---

## Afirmación B

> Los valores de `peso` están documentados como kilogramos.

Respuesta:

**No sustentada con la información disponible**

---

## Afirmación C

> Podemos saber qué enfermedad representa `A23` solamente leyendo esta tabla.

Respuesta:

**No sustentada**

---

## Afirmación D

> Si confirmamos las unidades, podemos calcular un IMC para cada paciente.

Respuesta:

**Posible, condicionado a confirmar las unidades**

---

## Afirmación E

> Si los tres IMC son diferentes, entonces existe asociación entre IMC y diagnóstico.

Respuesta:

**No sustentada**

---

## Afirmación F

> Con una sola observación por código `dx`, la capacidad para evaluar una asociación está fuertemente limitada.

Respuesta:

**Sustentada por la estructura observable del conjunto de datos**

---

# 24. Miniactividad “Calcular no es interpretar”

Mostrar tres niveles:

```text
NIVEL 1
Calcular
“Obtengo un IMC”

NIVEL 2
Comparar
“Los valores son diferentes”

NIVEL 3
Interpretar
“¿La evidencia permite hablar de relación?”
```

Pedir al estudiante ordenar los tres niveles.

Mensaje final:

> **Un resultado computacional no es automáticamente una conclusión científica.**

---

# 25. Etapa 6 — Dictamen científico final

Volver a mostrar exactamente la pregunta inicial:

> **¿Los datos de `pacientes.md` son suficientes para evaluar si el índice de masa corporal está relacionado con el diagnóstico registrado en `dx`?**

Mostrar también su **primer dictamen**.

Preguntar nuevamente:

- Sí
- No
- Solo parcialmente / se requiere información adicional

Permitir una justificación abierta.

No forzar una frase exacta.

La respuesta debe poder reconocer que existen variables relevantes, pero faltan metadatos importantes y la estructura/tamaño del conjunto limita una evaluación de asociación.

---

# 26. Comparación del cambio de razonamiento

Mostrar:

```text
AL INICIO
Yo pensaba:
[...]

DESPUÉS DE ANALIZAR
Ahora considero:
[...]

¿Qué cambió en mi razonamiento?
[respuesta del estudiante]
```

Esta reflexión es obligatoria y debe guardarse.

---

# 27. Producto final — Estrategia de análisis

A partir de todo lo construido, generar automáticamente una tabla final:

| Subpregunta | Evidencia | Datos | Operación | Herramienta candidata | Validación | Interpretación |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... |

La tabla debe construirse con las respuestas REALES del alumno.

No sustituirlas silenciosamente por respuestas modelo.

Si el alumno corrigió una decisión, utilizar su respuesta final y conservar el primer intento en el historial.

---

# 28. Pestaña final obligatoria — RESUMEN

La experiencia SIEMPRE debe terminar con una pestaña:

# Resumen

Debe estar disponible como último elemento de navegación.

No debe ser una simple pantalla de “terminaste”.

Debe reunir el proceso de razonamiento del estudiante.

---

# 29. Resumen — Pregunta central

Mostrar:

> ¿Los datos de `pacientes.md` son suficientes para evaluar si el IMC está relacionado con `dx`?

Después:

```text
Primer dictamen:
[...]

Dictamen final:
[...]

Justificación final:
[...]
```

---

# 30. Resumen — Lo que sé y lo que falta

Mostrar dos columnas:

```text
PUEDO OBSERVAR EN EL ARCHIVO
- peso
- altura
- sexo
- edad
- dx
- 3 observaciones
...

NECESITO CONFIRMAR / LIMITACIONES
- unidades
- significado de dx
- códigos
- estructura de grupos
...
```

Usar las decisiones reales del estudiante cuando sea posible.

---

# 31. Resumen — Mi cadena de evidencia

Mostrar gráficamente:

```text
PREGUNTA
   ↓
SUBPREGUNTAS
   ↓
EVIDENCIA
   ↓
DATOS
   ↓
OPERACIONES
   ↓
VALIDACIÓN
   ↓
INTERPRETACIÓN
   ↓
HERRAMIENTAS
```

Y debajo las ramas construidas por el alumno.

---

# 32. Resumen — Mi estrategia

Mostrar la tabla final:

| Subpregunta | Evidencia | Datos | Operación | Herramienta | Validación | Interpretación |
|---|---|---|---|---|---|---|

Debe poder copiarse fácilmente.

---

# 33. Resumen — Metadatos y limitaciones

Mostrar:

```text
Metadatos que necesito confirmar:
- ...

Limitaciones detectadas:
- ...

Aspectos que no puedo afirmar todavía:
- ...
```

---

# 34. Resumen — Cómo cambió mi razonamiento

Mostrar:

```text
Al inicio:
[...]

Al final:
[...]

Lo que cambió:
[...]
```

---

# 35. Resumen — Idea esencial

Cerrar con:

> **En bioinformática, el primer paso no es elegir una herramienta. Es decidir qué evidencia necesitas, qué datos pueden proporcionarla y cómo comprobarás que tu interpretación está sustentada.**

Y:

```text
pregunta
→ evidencia
→ datos
→ operación
→ validación
→ interpretación
→ herramienta
```

---

# 36. Botón obligatorio — Descargar mis resultados

Dentro de la pestaña **Resumen**, incluir un botón claramente visible:

# ⬇ Descargar mis resultados

Debe generar localmente:

```text
bioinformatics-strategy-lab-resultados.md
```

El archivo debe contener el trabajo REAL del estudiante.

Implementar únicamente con JavaScript nativo:

- `Blob`;
- `URL.createObjectURL`;
- `<a download>`;
- o equivalente.

No usar:

- servidor;
- API;
- almacenamiento externo;
- librerías externas.

---

# 37. Contenido del archivo descargable

Generar una estructura semejante a:

```markdown
# Bioinformatics Strategy Lab — Resultados

Unidad 1 — Introducción a la Bioinformática
Práctica 1 — Diseñar una estrategia antes de elegir herramientas

Fecha: [automática]

## Pregunta central

¿Los datos de pacientes.md son suficientes para evaluar si el índice de masa corporal está relacionado con el diagnóstico registrado en dx?

## Primer dictamen

Respuesta:
[...]

Justificación:
[...]

## Auditoría de datos

### peso
Qué puedo observar:
[...]

Qué necesito confirmar:
[...]

### altura
...

### dx
...

### Estructura de la muestra
Número de observaciones:
3

Observaciones por dx:
[...]

Limitaciones detectadas:
[...]

## Mi cadena de evidencia

### Rama 1
Subpregunta:
[...]

Evidencia:
[...]

Datos:
[...]

Operación:
[...]

Validación:
[...]

Interpretación:
[...]

Herramienta candidata:
[...]

### Rama 2
...

## Detecta el salto

Decisiones iniciales:
[...]

Decisiones corregidas:
[...]

Pistas utilizadas:
[...]

## Evidencia e interpretación

Afirmaciones revisadas:
[...]

Casos donde reconocí que necesitaba más evidencia:
[...]

## Dictamen final

Respuesta:
[...]

Justificación:
[...]

## Cómo cambió mi razonamiento

Al inicio:
[...]

Al final:
[...]

Lo que cambió:
[...]

## Mi estrategia final

| Subpregunta | Evidencia | Datos | Operación | Herramienta | Validación | Interpretación |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... |

## Metadatos pendientes

- ...

## Limitaciones

- ...

## Resumen descriptivo

Subpreguntas construidas: [n]
Pistas utilizadas: [n]
Decisiones revisadas: [n]
Metadatos pendientes detectados: [n]
Limitaciones identificadas: [n]
Dictamen revisado después del análisis: Sí / No
```

Si un campo no fue respondido:

```text
Sin respuesta
```

---

# 38. El reporte NO es una calificación

No incluir:

- nota;
- porcentaje;
- aprobado/reprobado;
- ranking;
- puntuación.

Sí puede incluir indicadores descriptivos del proceso.

La finalidad es conservar evidencia del razonamiento.

---

# 39. Preparación para `protocolo.md`

En la pestaña Resumen incluir:

# Para llevar a tu protocolo

Texto:

> Tu estrategia no termina en este interactivo. Usa el reporte descargado como borrador para documentar la sección de estrategia de `protocolo.md`.

Mostrar:

```text
Pregunta central
+
subpreguntas
+
evidencia
+
datos
+
operaciones
+
validación
+
interpretación
+
limitaciones
```

No modificar archivos automáticamente.

---

# 40. Accesibilidad

Implementar:

- HTML semántico;
- navegación completa por teclado;
- foco visible;
- botones reales;
- `fieldset` y `legend`;
- labels asociados;
- `aria-live` para feedback;
- contraste suficiente;
- no depender solo del color;
- targets táctiles cómodos;
- responsive para computadora y tableta.

Las pestañas deben seguir el patrón accesible:

- `role="tablist"`
- `role="tab"`
- `role="tabpanel"`
- `aria-selected`
- navegación mediante teclado.

La pestaña **Resumen** debe ser completamente accesible.

---

# 41. Restricciones técnicas

Generar:

- un único archivo HTML;
- CSS embebido;
- JavaScript embebido;
- sin frameworks;
- sin React;
- sin Node;
- sin backend;
- sin login;
- sin tracking;
- sin APIs;
- sin dependencias externas obligatorias;
- completamente funcional offline;
- listo para Git;
- fácil de integrar en sitio estático.

No usar IA en tiempo real.

---

# 42. Componentes reutilizables

Organiza el código para que puedan reutilizarse patrones como:

- `dataset-inspector`
- `metadata-audit`
- `evidence-chain`
- `strategy-branch`
- `jump-detector`
- `evidence-status`
- `interpretation-classifier`
- `strategy-builder`
- `final-verdict`
- `summary-tab`
- `download-report`
- `hint-box`
- `progress-indicator`

Comenta CSS y JavaScript suficientemente para reutilización.

---

# 43. Nombre sugerido

```text
interactive/u1/s1-practica1-bioinformatics-strategy-lab.html
```

---

# 44. Integración con el Markdown de S1

El HTML puede reemplazar pedagógicamente el **primer intento individual de la Práctica 1**, pero debe conservarse en el documento:

- título de la práctica;
- propósito;
- archivo `pacientes.md`;
- pregunta central;
- enlace o iframe al interactivo;
- instrucciones posteriores para documentar la estrategia;
- integración con `protocolo.md`;
- criterio de logro.

Si el texto actual menciona una “práctica anterior” aunque esta sea la primera práctica/sesión del curso, señala esa inconsistencia para que el docente pueda corregirla.

NO modifiques S1 automáticamente.

Al final de tu respuesta indica:

1. qué contenido actual puede sustituirse por el interactivo;
2. qué contenido debe permanecer;
3. dónde insertar enlace/iframe;
4. cómo quedaría una versión mínima de la sección en Markdown.

---

# 45. Validación final obligatoria

Antes de entregar verifica:

1. ¿Se utiliza la pregunta central correcta?
2. ¿Se muestran los tres pacientes?
3. ¿No se inventan unidades?
4. ¿No se inventa el significado de A23/B15/C12?
5. ¿El estudiante detecta la necesidad de metadatos?
6. ¿Se trabaja explícitamente el tamaño/estructura de la muestra?
7. ¿Se distingue calcular IMC de demostrar asociación?
8. ¿Se distingue observar diferencias de interpretar una relación?
9. ¿La herramienta aparece después de evidencia/datos/operaciones?
10. ¿Existe “Detecta el salto”?
11. ¿Se conserva el primer dictamen?
12. ¿Existe un dictamen final?
13. ¿Se registra el cambio de razonamiento?
14. ¿La estrategia final incluye subpregunta, evidencia, datos, operación, herramienta, validación e interpretación?
15. ¿Las respuestas incorrectas reciben pista antes de revelar la solución?
16. ¿Se registra el primer intento?
17. ¿No existe calificación automática?
18. ¿Existe SIEMPRE una pestaña final llamada `Resumen`?
19. ¿El Resumen utiliza respuestas reales del alumno?
20. ¿Existe dentro de Resumen el botón `Descargar mis resultados`?
21. ¿Genera `bioinformatics-strategy-lab-resultados.md`?
22. ¿El archivo descargado contiene respuestas reales y no ficticias?
23. ¿Se incluyen metadatos pendientes y limitaciones?
24. ¿El reporte puede reutilizarse para `protocolo.md`?
25. ¿El recurso funciona completamente offline?
26. ¿Es accesible por teclado?
27. ¿Las pestañas son accesibles?
28. ¿El diseño es científico y universitario?
29. ¿No se convierte prematuramente en una práctica de Python o estadística?
30. ¿La actividad hace visible la cadena pregunta → evidencia → datos → operación → validación → interpretación → herramienta?

---

# 46. Entregables

Entrega directamente:

1. **HTML completo final**, no fragmentos ni parches;
2. explicación breve de la arquitectura;
3. descripción de las seis etapas;
4. explicación de la pestaña final **Resumen**;
5. instrucciones para probarlo localmente;
6. fragmento Markdown recomendado para integrarlo en S1;
7. nota de accesibilidad;
8. decisiones técnicas importantes.

No pidas confirmación antes de generar el recurso.

La versión final debe hacer que el estudiante experimente que **el trabajo bioinformático comienza con una pregunta y una estrategia de evidencia, no con un comando**.
