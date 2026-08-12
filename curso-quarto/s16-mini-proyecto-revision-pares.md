# S16 — Revisar: evaluación por pares y cierre del mini-proyecto

::: {.callout-note title="Aula invertida"}
Esta sesión simula el proceso de revisión científica: leerás el trabajo
de otro equipo, emitirás un dictamen y mejorarás el tuyo a partir del que recibas.
:::


> **Duración:** 1 sesión (S15)  
> **Modalidad:** Trabajo colaborativo  
> **Producto generado:** `doc/dictamen-cientifico.md`

---

## Introducción

En investigación científica, obtener resultados es únicamente una parte del proceso.

Antes de que un trabajo pueda considerarse sólido, otros investigadores analizan críticamente:

- la calidad de la evidencia;
- la reproducibilidad del análisis;
- la validez de las conclusiones;
- las limitaciones del estudio;
- la claridad con la que fue documentado.

Este proceso se conoce como **revisión por pares** (*peer review*) y constituye uno de los mecanismos fundamentales para garantizar la calidad de la investigación científica.

En esta actividad simularemos ese proceso.

Cada equipo actuará como revisor científico del trabajo desarrollado por otro equipo.

---

## Objetivos de la actividad

Al finalizar esta actividad serás capaz de:

- evaluar críticamente un protocolo científico;
- distinguir entre evidencia y opinión;
- identificar fortalezas y oportunidades de mejora;
- formular observaciones objetivas y fundamentadas;
- fortalecer tu propio trabajo a partir de la retroalimentación recibida.

---

## Materiales

Cada equipo recibirá únicamente el archivo:

```text
doc/protocolo.md
```

No se proporcionarán archivos de datos, resultados intermedios ni explicaciones adicionales.

La revisión deberá realizarse exclusivamente a partir de la información documentada en el protocolo.

---

## Desarrollo de la actividad

### Paso 1. Asignación de revisores

El profesor asignará a cada equipo el protocolo desarrollado por otro equipo.

Cada protocolo será revisado por un único equipo.

---

### Paso 2. Lectura crítica

Lean cuidadosamente el protocolo recibido.

Durante esta etapa:

- no ejecuten nuevamente los comandos;
- no consulten a los autores;
- no hagan suposiciones sobre información que no esté documentada.

Evalúen únicamente aquello que pueda demostrarse mediante la evidencia presentada.

Pregúntense constantemente:

> **¿La evidencia presentada es suficiente para sostener esta conclusión?**

---

### Paso 3. Elaboración del dictamen científico

Con base en la revisión realizada, elaboren el archivo:

```text
doc/dictamen-cientifico.md
```

El dictamen deberá contener observaciones objetivas, respetuosas y fundamentadas.

Eviten comentarios como:

- "Está bien."
- "Todo correcto."
- "Me gustó."

Cada observación debe explicar claramente:

- qué aspecto se evaluó;
- por qué representa una fortaleza o una oportunidad de mejora;
- cómo podría fortalecerse el trabajo.

Recuerden que el propósito de una revisión científica no es encontrar errores, sino contribuir a mejorar la calidad de una investigación.

---

### Paso 4. Entrega del dictamen

Una vez concluido el dictamen, entréguenlo al equipo autor.

No modifiquen directamente su protocolo.

Toda la retroalimentación deberá registrarse únicamente en el archivo:

```text
doc/dictamen-cientifico.md
```

---

### Paso 5. Análisis de la retroalimentación

El equipo autor leerá cuidadosamente el dictamen recibido.

Posteriormente deberá analizar cada observación y decidir qué modificaciones incorporará al protocolo.

No todas las observaciones deben aceptarse obligatoriamente.

Sin embargo, cualquier decisión deberá estar razonada.

---

### Paso 6. Mejora del protocolo

Después de analizar la retroalimentación, el equipo actualizará:

```text
doc/protocolo.md
```

incorporando las mejoras que considere pertinentes.

El objetivo es obtener una versión científicamente más sólida del trabajo.

---

### Paso 7. Respuesta de los autores

Finalmente, el equipo autor completará la última sección del archivo:

```text
doc/dictamen-cientifico.md
```

En ella deberá documentar:

- qué observaciones incorporó;
- cuáles decidió no incorporar;
- qué mejoras realizó al protocolo;
- qué aprendió durante el proceso de revisión.

De esta manera quedará registrado cómo evolucionó la investigación gracias a la revisión por pares.

---

## Entregables

Al finalizar la actividad, el proyecto deberá contener los siguientes documentos:

```text
proyecto/
│
├── data/
├── results/
├── doc/
│   ├── protocolo.md
│   └── dictamen-cientifico.md
└── README.md
```

### `doc/protocolo.md`

Versión final del protocolo científico, mejorada después de la revisión.

### `doc/dictamen-cientifico.md`

Documento que registra:

- la evaluación realizada por el equipo revisor;
- las recomendaciones emitidas;
- la respuesta del equipo autor;
- las mejoras incorporadas al trabajo.

---

## Criterios de evaluación

Durante esta actividad se evaluará:

- calidad del análisis crítico realizado;
- fundamentación de las observaciones;
- claridad y profesionalismo del dictamen;
- capacidad para incorporar retroalimentación;
- mejora observable del protocolo final.

No se evaluará la cantidad de observaciones realizadas, sino su calidad y utilidad para fortalecer la investigación.

---

## Reflexión

La revisión por pares es uno de los pilares de la ciencia moderna.

Gracias a ella, las investigaciones son evaluadas por otros especialistas antes de ser aceptadas por la comunidad científica.

En este curso utilizamos este mismo principio para fortalecer nuestros proyectos.

Aprender a revisar críticamente el trabajo de otros y aprender a mejorar el propio a partir de la retroalimentación son habilidades esenciales para cualquier investigador en Genómica Computacional.

---

## Cierre del bloque S14–S17

Has completado el primer nivel del análisis de un genoma.

Ahora eres capaz de:
- Recuperar un ensamblado desde NCBI.
- Verificar su procedencia e integridad.
- Organizar un proyecto reproducible.
- Explorar archivos FASTA y GFF3.
- Construir el primer inventario del genoma.
- Documentar tus resultados en un protocolo científico.
- Evaluar críticamente el trabajo de otro equipo mediante revisión por pares.

Sin embargo, todavía existe una limitación importante: tus consultas siguen siendo principalmente literales. En el siguiente bloque aprenderás a construir búsquedas mucho más precisas mediante expresiones regulares y nuevas estrategias de transformación de datos.
