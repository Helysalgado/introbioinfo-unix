# Prompt para Gemini Canvas — Interactivo HTML S7: “¿Qué archivo necesito?”

## Tarea

Actúa como **diseñador instruccional y desarrollador front-end especializado en educación científica y bioinformática**.

Vas a construir un recurso interactivo para integrarlo al sitio web del curso:

**Introducción a la Bioinformática — LCG, UNAM — 2026**

## Contexto pedagógico

Este recurso pertenece a:

**S7 — De los objetos biológicos a FASTA, GFF3 y GenBank**

La sesión enseña que los formatos no deben memorizarse como definiciones aisladas. El estudiante debe aprender a razonar:

```text
pregunta biológica
→ evidencia necesaria
→ dato
→ formato
→ operación posterior
```

El interactivo será **parte de S7**, no una actividad adicional.

NO debe sustituir:

- la inspección de archivos reales;
- la navegación de registros;
- la práctica posterior con FASTA, GFF3 y GenBank;
- la actualización de `protocolo.md`.

Su función es preparar al estudiante para tomar una decisión antes de trabajar con los archivos reales.

---

# Objetivo del interactivo

Que el estudiante pueda responder:

> **¿Qué tipo de información necesito para responder una pregunta biológica y qué formato contiene esa información?**

Al terminar, el estudiante debe distinguir funcionalmente:

- **FASTA** → secuencia;
- **GFF3** → anotación, features y coordenadas;
- **GenBank** → secuencia + anotación + metadatos en un registro estructurado.

Pero NO presentes estas asociaciones inicialmente como una tabla para memorizar.

El estudiante debe descubrirlas mediante casos.

---

# Experiencia deseada

El recurso debe funcionar como un pequeño laboratorio de decisiones.

Flujo general:

```text
caso biológico
→ ¿qué necesitas saber?
→ elección de formato
→ retroalimentación
→ segundo intento si es necesario
→ explicación
→ siguiente caso
→ síntesis final
```

No uses el patrón:

```text
pregunta
→ correcto / incorrecto
```

Prefiere:

```text
respuesta
→ pista
→ revisión del razonamiento
→ segundo intento
→ explicación final
```

---

# Caso 1 — Coordenadas de un gen

Presenta:

> Quieres responder:
>
> **¿En qué coordenadas del genoma se encuentra un gen específico?**

Opciones:

- FASTA
- GFF3
- GenBank

Si el estudiante elige FASTA, no mostrar “incorrecto” de inmediato.

Mostrar algo como:

> FASTA contiene secuencias. Pero la pregunta no pide todavía la secuencia del gen. **¿Qué tipo de evidencia necesitas para conocer su posición en el genoma?**

Permitir segundo intento.

Respuesta esperada: **GFF3**.

Después explicar brevemente:

> GFF3 describe features genómicos y sus coordenadas.

---

# Caso 2 — Secuencia de una proteína

Pregunta:

> Quieres recuperar la secuencia de aminoácidos de una proteína ya identificada.

Opciones:

- FASTA
- GFF3
- GenBank

Respuesta esperada: **FASTA**.

Retroalimentación:

> Aquí la evidencia principal es la secuencia misma.

---

# Caso 3 — Registro completo

Pregunta:

> Quieres consultar en un solo registro la secuencia, anotaciones y metadatos asociados a una región o secuencia biológica.

Opciones:

- FASTA
- GFF3
- GenBank

Respuesta esperada: **GenBank**.

Explicar:

> GenBank integra secuencia, anotaciones y metadatos en un registro estructurado.

---

# Caso 4 — Necesitas más de un formato

Sube la dificultad.

Pregunta:

> Quieres extraer del genoma la secuencia de todos los CDS anotados.

Primero pregunta:

> ¿Un solo archivo contiene necesariamente toda la evidencia que necesitas?

Opciones:

- Sí
- No

Respuesta esperada: **No**.

Después mostrar:

```text
GFF3
→ coordenadas de los CDS

+

FASTA
→ secuencia genómica

↓

extracción de secuencias
```

Pregunta final:

> ¿Qué aporta cada archivo al análisis?

Permite emparejar:

- GFF3 → coordenadas
- FASTA → secuencia

---

# Caso 5 — Detectar una mala elección

Presenta:

> Un estudiante dice: “Voy a usar FASTA para saber cuántos genes están anotados en el genoma.”

Pregunta:

> ¿Cuál es el problema de esta estrategia?

Opciones:

- FASTA no puede contener DNA
- FASTA no representa directamente la anotación de genes
- GFF3 siempre contiene las secuencias
- GenBank no sirve para anotaciones

Respuesta esperada: **FASTA no representa directamente la anotación de genes**.

La retroalimentación debe enfatizar:

> La pregunta biológica determina qué evidencia necesitas. No se elige un formato por costumbre.

---

# Cierre conceptual

Al terminar los casos, mostrar una síntesis visual simple:

```text
PREGUNTA
   ↓
¿Necesito secuencia?
   → FASTA

¿Necesito coordenadas/anotación?
   → GFF3

¿Necesito un registro integrado?
   → GenBank

¿Necesito combinar tipos de evidencia?
   → puede requerirse más de un archivo
```

Después mostrar el mensaje:

> **El formato no se elige primero.**
>
> Primero se identifica la pregunta y la evidencia necesaria.

---

# Integración con la sesión S7

Al final agrega una transición explícita:

> Ahora lleva este razonamiento a los archivos reales de la práctica de S7.
>
> Antes de abrir cada archivo, pregúntate:
>
> **¿Qué información espero encontrar aquí y cómo ayudará a responder mi pregunta biológica?**

No agregues tareas adicionales.

---

# Diseño visual

Quiero un diseño:

- limpio;
- científico;
- juvenil sin verse infantil;
- apropiado para estudiantes universitarios;
- con estética de bioinformática;
- fondo claro;
- buena jerarquía visual;
- tarjetas;
- iconografía discreta;
- tipografía legible;
- estados hover/focus;
- responsive.

No usar decoración excesiva.

Puedes usar pequeños elementos visuales inspirados en secuencias, cromosomas, registros, tablas y archivos, pero el foco debe ser la decisión pedagógica.

---

# Accesibilidad

Implementa:

- HTML semántico;
- navegación por teclado;
- `button` reales;
- `fieldset` y `legend` cuando corresponda;
- labels asociados;
- contraste suficiente;
- `aria-live` para retroalimentación;
- no depender únicamente del color para indicar correcto/incorrecto;
- foco visible;
- texto responsive.

---

# Restricciones técnicas

Genera una solución:

- en **un solo archivo HTML**;
- con CSS y JavaScript embebidos;
- sin frameworks;
- sin React;
- sin Node;
- sin dependencias externas obligatorias;
- sin servidor;
- sin login;
- sin tracking;
- sin enviar datos;
- sin APIs;
- funcional offline;
- lista para versionarse en Git;
- fácil de integrar en un sitio web estático.

No uses IA en tiempo real dentro del interactivo.

---

# Persistencia

No necesitas almacenar respuestas en servidor.

Durante la sesión actual puedes mantener:

- caso actual;
- intentos;
- progreso.

Si recarga la página, no es necesario conservar progreso.

---

# Progreso

Incluye una barra discreta:

```text
Caso 2 de 5
```

No utilices puntaje competitivo.

El objetivo no es ganar puntos sino mejorar el razonamiento.

---

# Retroalimentación

Usa tres tipos de mensajes:

### Pista

Cuando el estudiante falla por primera vez:

> Revisa qué tipo de evidencia pide la pregunta.

### Segunda pista

Si vuelve a fallar:

> ¿Necesitas una secuencia o necesitas saber dónde está anotado algo?

### Explicación

Después de resolver:

> GFF3 contiene features anotados con coordenadas; por eso responde mejor esta pregunta.

No revelar la solución demasiado pronto.

---

# Componentes reutilizables

Aunque construyas un solo HTML, organiza el código para que en el futuro puedan reutilizarse componentes conceptuales como:

- `case-card`
- `multiple-choice-feedback`
- `hint-box`
- `progress-indicator`
- `concept-summary`

Comenta el código claramente.

---

# Nombre sugerido del archivo

```text
interactive/u3/s7-que-archivo-necesito.html
```

---

# Entregables

Quiero:

1. el archivo HTML completo;
2. una breve explicación de la estructura;
3. dónde integrarlo dentro de S7;
4. qué parte del Markdown actual podría reemplazar o complementar;
5. qué práctica real debe permanecer después del interactivo.

No modifiques todavía la sesión S7.

Primero genera el recurso y explícame cómo integrarlo.
