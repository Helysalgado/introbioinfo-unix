# Prompt para Gemini Canvas
## S2 · Práctica 1 — Data Steward Lab

Actúa como **diseñador instruccional y desarrollador front-end especializado en bioinformática, reproducibilidad, gestión de datos científicos, principios FAIR y aprendizaje activo**.

Construye una **app web educativa interactiva en un único archivo HTML** para:

**Introducción a la Bioinformática — LCG UNAM — 2026**

Corresponde a:

**Sesión 2 — Práctica 1**

Nombre de la experiencia:

# Data Steward Lab

Subtítulo:

> **Organiza, describe y conserva los datos antes de analizarlos**

---

# 1. Contexto pedagógico

Esta práctica ocurre DESPUÉS de S1.

En S1 el estudiante ya trabajó:

- pregunta científica;
- subpreguntas;
- evidencia;
- estrategia;
- estructura básica de `protocolo.md`;
- Markdown básico;
- Mermaid básico.

NO vuelvas a enseñar Markdown.

NO vuelvas a enseñar Mermaid.

Puedes UTILIZAR ambos como herramientas ya conocidas.

En S2 cambia la pregunta.

Ya no preguntamos principalmente:

> “¿Cómo analizaría estos datos?”

Ahora preguntamos:

> **“¿Qué necesito saber y documentar para que estos datos puedan encontrarse, interpretarse y reutilizarse correctamente?”**

La práctica debe conectar:

```text
DATO
↓
PROCEDENCIA
↓
METADATOS
↓
ORGANIZACIÓN
↓
FAIR
↓
REPRODUCIBILIDAD
```

---

# 2. Caso conductor

Usaremos nuevamente:

`pacientes.md`

Es un conjunto de datos **sintético**, creado exclusivamente con fines educativos.

No contiene datos de pacientes reales.

El archivo tiene tres registros y las variables:

- `id`
- `peso`
- `altura`
- `sexo`
- `edad`
- `dx`

El estudiante ya conoce este archivo de S1. Eso es intencional.

Queremos que descubra que un mismo dato puede examinarse desde perspectivas diferentes:

```text
S1 → ¿qué podría investigar con él?

S2 → ¿sé realmente qué significa, de dónde viene
     y cómo debo conservarlo?
```

---

# 3. Objetivo

Al terminar la práctica, el estudiante debe poder:

1. organizar conceptualmente un proyecto bioinformático reproducible;
2. distinguir datos fuente de datos derivados;
3. decidir dónde debe vivir cada objeto del proyecto;
4. construir una ficha básica de metadatos;
5. elaborar un diccionario de variables;
6. distinguir información comprobable, pendiente de confirmar y no documentada;
7. evitar inventar metadatos;
8. relacionar decisiones concretas con FAIR;
9. producir `pacientes-metadatos.md`.

---

# 4. Restricción importante: todavía NO Unix

En este punto NO se enseñan comandos Unix.

NO incluir:

- `mkdir`
- `cd`
- `ls`
- `cp`
- `mv`
- `cat`
- `touch`
- `grep`
- terminal
- shell
- bash

La estructura del proyecto se trabaja CONCEPTUALMENTE.

---

# 5. Arquitectura de la app

Construye cinco misiones:

```text
MISIÓN 1
¿Dónde vive cada cosa?
        ↓
MISIÓN 2
Protege el punto de partida
        ↓
MISIÓN 3
¿Qué sabemos realmente?
        ↓
MISIÓN 4
Construye los metadatos
        ↓
MISIÓN 5
Auditoría FAIR
        ↓
RESUMEN
```

Navegación:

```text
① Organizar
② Conservar
③ Evidencia
④ Metadatos
⑤ FAIR
✓ Resumen
```

IMPORTANTE: el número debe aparecer UNA SOLA VEZ dentro del círculo.

NO producir `① 1 Organizar`.

La pestaña final debe llamarse exactamente **Resumen**.

---

# 6. Encabezado

Usar el mismo lenguaje visual de Protocol Builder.

Primera línea:

```text
[ LCG UNAM 2026 ]   Introducción a la Bioinformática • Sesión 2 • Práctica 1
```

Debajo:

# Data Steward Lab

Subtítulo:

> Organiza, describe y conserva los datos antes de analizarlos

NO colocar una caja grande lateral con “Meta de la sesión”.

Mantener encabezado compacto.

---

# 7. Introducción narrativa

Mostrar:

> En S1 utilizaste `pacientes.md` para pensar una pregunta y una estrategia. Pero todavía queda un problema: ¿qué sabemos realmente sobre ese archivo?

Después:

> Un análisis puede estar técnicamente bien ejecutado y aun así no ser reproducible si desconocemos la procedencia, las unidades, el significado de las variables o las transformaciones realizadas sobre los datos.

Pregunta inicial:

> **Si otra persona recibiera solamente `pacientes.md`, ¿podría interpretarlo correctamente sin preguntarte nada?**

Opciones:

- Sí, el archivo contiene todo lo necesario.
- Probablemente no; necesita información adicional.
- Depende únicamente del programa utilizado.

Esperada:

> Probablemente no; necesita información adicional.

Feedback:

> **Ese contexto adicional forma parte de los metadatos.**

---

# MISIÓN 1 — ¿Dónde vive cada cosa?

## 8. Introducir la estructura

Presentar:

```text
proyecto/
├── README.md
├── data/
│   ├── source/
│   └── processed/
├── src/
├── results/
└── doc/
```

Explicar brevemente:

```text
README.md
→ qué es el proyecto y cómo reproducirlo

data/source/
→ datos originales + sus metadatos

data/processed/
→ datos derivados o transformados

src/
→ scripts y procedimientos computacionales

results/
→ resultados y evidencia regenerable

doc/
→ documentación y reportes
```

---

# 9. Actividad “Ubica cada objeto”

Haz una actividad interactiva de clasificación.

Preferentemente drag-and-drop accesible, pero si complica la accesibilidad utiliza tarjetas + botones/selectores.

Objetos:

```text
pacientes.md original
pacientes-metadatos.md
pacientes_limpios.csv
calcular_imc.py
tabla_resultados.csv
protocolo.md
README.md
```

Destinos:

```text
raíz del proyecto
data/source/
data/processed/
src/
results/
doc/
```

Respuestas esperadas:

```text
README.md → raíz
pacientes.md original → data/source/
pacientes-metadatos.md → data/source/
pacientes_limpios.csv → data/processed/
calcular_imc.py → src/
tabla_resultados.csv → results/
protocolo.md → doc/
```

El feedback debe explicar el porqué, no limitarse a correcto/incorrecto.

Después construir visualmente el árbol final del proyecto a partir de las decisiones.

No volver a enseñar Mermaid. Si se ofrece como extensión, dejar claro que aquí se evalúa la organización, no la sintaxis.

---

# MISIÓN 2 — Protege el punto de partida

## 10. Regla de los datos fuente

Presentar:

# `data/source/` conserva el punto de partida

Reglas:

- el original puede leerse;
- puede copiarse;
- NO debe editarse;
- NO debe sobrescribirse;
- NO debe reemplazarse;
- conserva su nombre original;
- conserva su checksum cuando esté disponible;
- una transformación produce un archivo NUEVO.

## 11. Actividad de decisiones

Caso A:

> Detectas un error tipográfico en `pacientes.md`.

Opciones:
A. Editas directamente el original.  
B. Generas una copia corregida como dato derivado y documentas la transformación.  
C. Borras el original.

Correcta: B.

Caso B:

> Necesitas convertir el archivo a CSV.

A. Cambias únicamente la extensión.  
B. Sobrescribes el original.  
C. Produces un nuevo archivo en `data/processed/`.

Correcta: C.

Caso C:

> Obtienes nuevamente el mismo dataset desde su fuente. ¿Qué información permitiría comprobar que es exactamente el mismo archivo?

Respuesta: **checksum**.

Explicar conceptualmente la función del checksum, pero NO enseñar todavía cómo calcularlo.

Cerrar con:

> **La reproducibilidad comienza por conservar el punto de partida.**

---

# MISIÓN 3 — ¿Qué sabemos realmente?

## 12. Tres categorías epistemológicas

Introducir:

### ✓ COMPROBABLE
Puede determinarse directamente a partir del archivo o de documentación proporcionada.

### ? PENDIENTE DE CONFIRMAR
Parece plausible o puede inferirse parcialmente, pero necesita una fuente adicional.

### ! NO DOCUMENTADO
La información necesaria no está disponible.

Aclarar:

> “No documentado” no significa falso o inexistente. Significa que no tenemos evidencia suficiente para afirmarlo.

## 13. Actividad “¿Qué puedes afirmar?”

Clasificar afirmaciones sobre `pacientes.md`.

Ejemplos:

- El archivo contiene tres registros sintéticos → comprobable si fue proporcionado por el curso.
- Las columnas son `id`, `peso`, `altura`, `sexo`, `edad`, `dx` → comprobable.
- `peso` está en kilogramos → pendiente/no documentado.
- `altura` está en metros → pendiente/no documentado.
- El archivo procede de un hospital → no documentado.
- Los datos corresponden a personas reales → incorrecto, porque el curso indica que son sintéticos.
- La extensión `.md` demuestra que el contenido interno es Markdown → incorrecto.

Mostrar después una tabla con tres estados.

Mensaje central:

> **Una buena ficha de metadatos no rellena todos los campos a cualquier precio. Documentar honestamente lo que NO sabemos también es buena práctica científica.**

## 14. Reto “El metadato tentador”

Mostrar:

> Peso — número decimal — kilogramos

Preguntar qué parte puede conservarse y cuál debe cuestionarse.

Reforzar:

> **plausible ≠ documentado**

---

# MISIÓN 4 — Construye los metadatos

## 15. Diferenciar protocolo y metadatos

Mostrar:

```text
protocolo.md
→ qué pregunta hago y cómo pienso responderla

pacientes-metadatos.md
→ qué es pacientes.md, de dónde viene,
  qué contiene y qué sabemos de sus variables
```

## 16. Constructor de ficha

Crear un formulario que construya `pacientes-metadatos.md`.

Campos mínimos:

- Nombre original del archivo
- Descripción del contenido
- Organismo
- Base de datos de origen
- URL
- Identificador o accesión
- Fecha de acceso
- Formato
- Responsable

Permitir explícitamente:

- `no documentado`
- `pendiente de confirmar`

NO obligar a inventar información.

Mostrar como campos futuros:

- Versión o release
- Tamaño
- Checksum
- Licencia o condiciones de uso
- Procedimiento de obtención
- Notas de procedencia
- Transformaciones realizadas

## 17. Diccionario de variables

Para:

- `id`
- `peso`
- `altura`
- `sexo`
- `edad`
- `dx`

Campos:

- Nombre
- Descripción
- Tipo
- Unidades
- Valores permitidos / códigos
- Estado de documentación
- Notas

Estado:

```text
✓ documentado
? pendiente de confirmar
! no documentado
```

CRÍTICO: NO autocompletar unidades, significado de `dx`, procedencia, licencia, URL, responsable o cualquier conocimiento inexistente.

## 18. Generar Markdown literal

Mostrar un panel:

# MI FICHA DE METADATOS

Debe mostrar Markdown literal, no HTML renderizado.

El contenido debe provenir de las respuestas REALES del estudiante.

Agregar:

- **📋 Copiar metadatos**
- **Abrir en StackEdit ↗**

StackEdit: `https://stackedit.io/app`

Abrir en nueva pestaña con `target="_blank"` y `rel="noopener noreferrer"`.

Mensaje:

> StackEdit representa el Markdown; no puede decidir si tus metadatos son científicamente correctos.

---

# MISIÓN 5 — Auditoría FAIR

## 19. Introducción

Presentar:

### F — Findable
Localizable.

### A — Accessible
Existe un procedimiento claro para recuperarlo bajo las condiciones correspondientes.

### I — Interoperable
Usa formatos y vocabularios interpretables.

### R — Reusable
Tiene procedencia, documentación y condiciones de uso suficientes para reutilizarlo.

## 20. FAIR no significa abierto

Plantear:

> Un dataset requiere autorización para acceder, pero tiene identificador persistente, metadatos completos y un procedimiento claro de acceso. ¿Puede ser FAIR?

Correcta:

> Sí, FAIR no exige necesariamente acceso abierto.

## 21. ¿Qué principio fortaleces?

Ejemplos:

- Registrar metadatos e identificador → principalmente Findable.
- Documentar URL/procedimiento → Accessible.
- Formato estándar → Interoperable.
- Procedencia y licencia → Reusable.
- Conservar el original → contribuye a Reusable y reproducibilidad.

Aclarar que FAIR es multidimensional y una acción puede contribuir a varios principios.

## 22. Auditoría del proyecto

Preguntar:

```text
¿Puedo localizar el dato?
¿Sé cómo se obtuvo?
¿Sé qué significa cada variable?
¿Conozco el formato?
¿Conozco las unidades?
¿Conozco las condiciones de uso?
¿Conservo el original?
¿Distingo original de derivado?
```

Opciones:

```text
✓ Sí
? Parcial
! Falta documentar
```

Cerrar con:

> **Detectar una ausencia de información es un resultado válido.**

> **Nunca conviertas una ausencia de documentación en una suposición.**

---

# RESUMEN

La pestaña final debe llamarse exactamente:

# Resumen

Debe reunir el trabajo REAL del estudiante.

## 23. Mi proyecto

Mostrar el árbol final basado en sus decisiones.

## 24. Lo que sé de `pacientes.md`

Tres grupos:

```text
✓ COMPROBABLE
[...]

? PENDIENTE DE CONFIRMAR
[...]

! NO DOCUMENTADO
[...]
```

## 25. Mis metadatos

Mostrar el contenido real completo de `pacientes-metadatos.md`.

Agregar:

- 📋 Copiar metadatos
- Abrir en StackEdit ↗

## 26. FAIR

Mostrar:

```text
F — Findable
¿Qué hice que contribuye?

A — Accessible
¿Qué falta?

I — Interoperable
¿Qué sabemos?

R — Reusable
¿Qué falta documentar?
```

No asignar porcentaje.

## 27. Reflexión final

Preguntar:

1. ¿Qué dato que parecía obvio descubriste que en realidad no estaba documentado?
2. ¿Por qué conservar el archivo original ayuda a la reproducibilidad?
3. ¿Qué diferencia encuentras entre “no sé” y “no está documentado”?
4. ¿Cuál principio FAIR consideras más difícil de garantizar con la información disponible y por qué?

Guardar las respuestas.

---

# 28. BOTONES DE DESCARGA OBLIGATORIOS

La práctica debe incluir de manera visible, dentro de la pestaña **Resumen**, los siguientes botones:

## ⬇ Descargar mis metadatos

Debe generar localmente:

```text
pacientes-metadatos.md
```

con el contenido REAL construido por el estudiante.

## ⬇ Descargar resultados del ejercicio

Debe generar localmente:

```text
data-steward-lab-resultados.md
```

Este segundo botón es OBLIGATORIO y debe guardar la evidencia completa del ejercicio.

Implementar ambas descargas únicamente con JavaScript nativo, por ejemplo:

- `Blob`
- `URL.createObjectURL`
- elemento `<a download>`

No usar servidor, API ni almacenamiento externo.

Además, puede existir un botón:

## 📋 Copiar resultados

para copiar el reporte completo al portapapeles.

---

# 29. Contenido obligatorio de `data-steward-lab-resultados.md`

Debe incluir:

```markdown
# Data Steward Lab — Resultados

Introducción a la Bioinformática
S2 — Práctica 1

Fecha: [automática]

## Organización del proyecto

[árbol construido por el estudiante]

## Clasificación de objetos

[decisiones reales]

## Conservación del original

[respuestas reales]

## Información comprobable

[...]

## Información pendiente de confirmar

[...]

## Información no documentada

[...]

## Metadatos

[contenido real de pacientes-metadatos.md]

## Diccionario de variables

[...]

## Auditoría FAIR

[...]

## Reflexión

### ¿Qué dato parecía obvio pero no estaba documentado?
[...]

### ¿Por qué conservar el original ayuda a la reproducibilidad?
[...]

### Diferencia entre “no sé” y “no está documentado”
[...]

### Principio FAIR más difícil de garantizar
[...]

## Registro formativo

Intentos revisados: [...]
Pistas utilizadas: [...]
Decisiones corregidas: [...]
```

Si un campo no fue respondido, escribir:

```text
Sin respuesta
```

NO incluir:

- calificación;
- porcentaje;
- aprobado/reprobado;
- ranking.

---

# 30. Filosofía del feedback

La app NO debe premiar “llenar todo”.

Debe reforzar:

```text
OBSERVAR
↓
DISTINGUIR
↓
DOCUMENTAR
↓
NO INVENTAR
```

Cuando el estudiante marque correctamente algo como `no documentado`, mostrar feedback positivo:

> ✓ Buena decisión científica. No existe evidencia suficiente para completar este campo.

---

# 31. Diseño visual

Mantener identidad visual de Protocol Builder:

- azul oscuro;
- dorado/amarillo para `LCG UNAM 2026`;
- fondo claro;
- tarjetas limpias;
- estética universitaria;
- tipografía legible;
- código y nombres de archivos en monoespaciada.

Dar identidad propia mediante metáforas visuales de:

- carpetas;
- fichas;
- etiquetas;
- procedencia;
- huellas;
- organización.

NO usar estética infantil.

---

# 32. Evitar repetición con S1

Antes de entregar verifica:

- NO estoy enseñando Markdown otra vez.
- NO estoy enseñando Mermaid otra vez.
- NO estoy reconstruyendo la estrategia IMC-dx.
- NO estoy preguntando nuevamente cómo diseñar el análisis.
- NO estoy enseñando Unix.
- Estoy utilizando conocimientos de S1 para resolver un problema NUEVO.

El foco debe ser:

> **gestión y documentación del dato**

y no:

> diseño del análisis.

---

# 33. Accesibilidad

Implementar:

- HTML semántico;
- navegación por teclado;
- foco visible;
- botones reales;
- labels;
- `fieldset` y `legend`;
- `aria-live`;
- contraste suficiente;
- no depender únicamente del color;
- targets táctiles cómodos;
- responsive.

Si usas drag-and-drop, proporcionar alternativa completa mediante teclado.

---

# 34. Restricciones técnicas

Generar:

- un único HTML;
- CSS embebido;
- JavaScript embebido;
- sin frameworks;
- sin React;
- sin backend;
- sin login;
- sin tracking;
- sin APIs;
- sin dependencias externas obligatorias.

La app debe funcionar offline excepto los enlaces explícitos a servicios externos.

---

# 35. Persistencia

Conservar las respuestas mientras el estudiante navega entre pestañas.

Puedes usar estado JavaScript y preferentemente `localStorage`.

Agregar:

> Reiniciar práctica

pero solicitar confirmación antes de borrar las respuestas.

---

# 36. Validación final obligatoria

Antes de entregar verifica:

1. ¿La numeración de pestañas aparece una sola vez?
2. ¿El encabezado sigue el estilo compacto de Protocol Builder?
3. ¿No hay comandos Unix?
4. ¿No se vuelve a enseñar Markdown?
5. ¿No se vuelve a enseñar Mermaid?
6. ¿Se distingue dato original de derivado?
7. ¿`pacientes.md` queda en `data/source/`?
8. ¿Los metadatos quedan junto al dato fuente?
9. ¿Las transformaciones generan archivos nuevos?
10. ¿Se explica conceptualmente checksum sin calcularlo?
11. ¿Se distingue comprobable / pendiente / no documentado?
12. ¿No se inventan unidades?
13. ¿No se inventa el significado de `dx`?
14. ¿No se inventa procedencia?
15. ¿No se inventa licencia?
16. ¿Se construye un diccionario de variables?
17. ¿Se genera `pacientes-metadatos.md`?
18. ¿Existe Copiar metadatos?
19. ¿Existe Abrir en StackEdit?
20. ¿FAIR no se presenta como equivalente a abierto?
21. ¿Las acciones FAIR no se presentan como absolutamente exclusivas?
22. ¿Existe una auditoría FAIR?
23. ¿Detectar información faltante se considera un resultado válido?
24. ¿Existe siempre la pestaña Resumen?
25. ¿Resumen utiliza respuestas reales?
26. ¿Existe el botón `⬇ Descargar mis metadatos`?
27. ¿Existe el botón `⬇ Descargar resultados del ejercicio`?
28. ¿`Descargar mis metadatos` genera `pacientes-metadatos.md`?
29. ¿`Descargar resultados del ejercicio` genera `data-steward-lab-resultados.md`?
30. ¿El reporte contiene las respuestas REALES del alumno?
31. ¿No hay calificación automática?
32. ¿La aplicación es accesible?
33. ¿La práctica se siente diferente a S1?

---

# 37. Entregable

Devuélveme el **HTML COMPLETO y funcional**.

No entregues fragmentos.

No pidas confirmación.

Al final explica brevemente:

- arquitectura de las cinco misiones;
- decisiones pedagógicas;
- qué elementos reutilizan conocimientos de S1;
- qué elementos son nuevos en S2;
- cómo insertar la actividad en el Markdown de S2.

La experiencia debe terminar dejando clara esta idea:

> **Un dato no es reutilizable solo porque tenemos el archivo. Necesitamos conservar su punto de partida, conocer su procedencia y documentar honestamente qué sabemos y qué todavía no sabemos.**
