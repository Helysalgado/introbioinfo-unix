# Construcción de la Unidad 5 — Automatización de análisis bioinformáticos con Shell

Vamos a continuar el desarrollo del curso universitario de **Bioinformática** para estudiantes de **primer semestre de la Licenciatura en Ciencias Genómicas**.

Antes de escribir cualquier contenido debes estudiar cuidadosamente:

1. `README.md`
2. `guia-generacion-unidad.md`

Estos documentos contienen la filosofía del curso, el estilo editorial, la metodología de Aula Invertida, la estructura de las sesiones, el protocolo reproducible y las reglas para construir el material.

Después revisa completamente:

- toda la Unidad 4;
- especialmente S23;
- el plan de clases actualizado.

La Unidad 5 debe ser una continuación natural de la Unidad 4.

No debe sentirse como un curso independiente de Bash.

---

# Filosofía del curso

Este NO es un curso de Shell.

Tampoco es un curso de Bash.

Shell únicamente proporciona herramientas para automatizar análisis bioinformáticos.

Cada concepto debe aparecer porque resuelve una necesidad científica real.

Nunca enseñar sintaxis únicamente porque existe.

Siempre:

limitación

↓

pregunta científica

↓

herramienta

↓

nuevo nivel de automatización.

---

# Contexto narrativo

Al terminar S23 el estudiante logró construir:

- un protocolo reproducible;
- un flujo completamente documentado;
- productos derivados;
- resultados verificables;
- controles manuales;
- interpretación biológica.

Sin embargo aparece una nueva limitación.

Aunque el protocolo es reproducible,

todavía depende completamente de la persona.

Cada vez que desea analizar otro genoma necesita:

- copiar comandos;
- cambiar rutas;
- modificar nombres;
- ejecutar paso por paso;
- revisar manualmente los resultados.

Ese problema debe convertirse en el hilo conductor de toda la unidad.

---

# Cambio conceptual de la unidad

Hasta ahora el estudiante aprendió:

```text
Responder preguntas biológicas
↓

Documentar el análisis

↓

Construir un protocolo reproducible
```

Ahora aprenderá:

```text
Convertir ese protocolo

↓

en una herramienta reutilizable
```

El protagonista deja de ser el comando.

El protagonista es el **script científico**.

---

# Propósito general

Que el estudiante aprenda a transformar un protocolo manual en una herramienta reutilizable capaz de automatizar análisis bioinformáticos sencillos, validar entradas, organizar resultados y registrar su ejecución de forma reproducible.

Al finalizar la unidad deberá ser capaz de reutilizar el mismo análisis sobre distintos conjuntos de datos biológicos sin modificar manualmente el flujo.

---

# Competencia que desarrolla

Hasta ahora el estudiante aprendió a:

✔ construir protocolos reproducibles

✔ documentar decisiones

✔ generar resultados verificables

Ahora aprenderá a:

✔ reutilizar análisis

✔ automatizar flujos

✔ validar entradas

✔ procesar múltiples archivos

✔ construir herramientas científicas reutilizables

---

# Filosofía de las sesiones

Cada sesión debe introducir exactamente una limitación nueva.

Nunca organizar las sesiones por características del lenguaje.

No hacer sesiones de:

- variables;
- if;
- for;
- parámetros.

Cada uno debe aparecer únicamente cuando sea necesario para resolver un problema bioinformático.

---

# Arquitectura aprobada

## S24 — Del protocolo al script

### Cambio conceptual

```text
Protocolo

↓

Script
```

### Problema

El análisis completo requiere copiar decenas de comandos.

### Preguntas biológicas

- ¿Cómo ejecuto nuevamente el mismo análisis sin copiar todo el protocolo?
- ¿Cómo conservo exactamente el mismo orden?

### Conceptos nuevos

- estructura de un script
- shebang
- permisos
- comentarios

### Producto

Primer script que reproduce parte del protocolo.

---

## S25 — Variables, parámetros y validaciones

### Cambio conceptual

```text
Script para un genoma

↓

Script para cualquier genoma
```

### Problema

El script funciona únicamente para los archivos originales.

### Preguntas

- ¿Cómo recibo otro FASTA?
- ¿Cómo recibo otro GFF3?
- ¿Cómo verifico que existen?

### Conceptos

- variables
- expansión
- parámetros
- `$1`
- `$2`
- `if`
- validación
- mensajes de error

Todo integrado en una misma historia.

### Producto

Script reutilizable para cualquier genoma.

---

## S26 — Automatización por lotes

### Cambio conceptual

```text
Un genoma

↓

Muchos genomas
```

### Problema

Analizar varios genomas manualmente es repetitivo.

### Preguntas

- ¿Cómo proceso diez FASTA?
- ¿Cómo organizo automáticamente los resultados?

### Concepto nuevo

`for`

Debe aparecer únicamente como solución al procesamiento repetitivo.

### Producto

Pipeline para múltiples genomas.

---

## S27 — Construcción de herramientas bioinformáticas

### Cambio conceptual

```text
Script funcional

↓

Herramienta científica
```

### Problema

Un script puede funcionar correctamente y aun así ser difícil de reutilizar.

### Temas

- organización del proyecto
- README
- documentación
- mensajes
- bitácora
- reproducibilidad
- pruebas

No introducir sintaxis nueva.

La novedad es la calidad del software científico.

### Producto

Versión casi final del pipeline.

---

## S28 — Proyecto integrador

### Cambio conceptual

```text
Comandos

↓

Protocolo

↓

Script

↓

Herramienta reutilizable
```

### Proyecto

El estudiante construye una herramienta que:

- recibe FASTA;
- recibe GFF3;
- valida entradas;
- automatiza el flujo de la Unidad 4;
- genera archivos derivados;
- organiza resultados;
- produce un reporte;
- registra la ejecución.

Esta sesión sustituye al examen práctico.

---

# Documento reproducible

El protocolo continúa siendo el eje del curso.

Ahora incorpora una nueva dimensión:

la automatización.

Cada sesión debe extender el protocolo para registrar:

- propósito del script;
- entradas;
- parámetros;
- validaciones;
- comandos automatizados;
- productos generados;
- registro de ejecución;
- pruebas realizadas;
- errores encontrados;
- limitaciones;
- interpretación biológica.

Nunca registrar únicamente código.

Siempre documentar el razonamiento científico que motivó cada automatización.

---

# Figuras

Diseñar la unidad suponiendo que contendrá numerosas figuras.

Por ejemplo:

- evolución Protocolo → Script → Herramienta;
- anatomía de un script científico;
- variables dentro del flujo;
- parámetros como entradas del análisis;
- validaciones antes de ejecutar;
- procesamiento por lotes;
- organización del proyecto;
- evolución de la reproducibilidad;
- flujo completo automatizado.

Las figuras deben explicar el razonamiento científico.

No ilustrar únicamente sintaxis.

---

# Integración con IA

La IA debe seguir utilizándose como herramienta de apoyo crítico.

Cada sesión debe incorporar actividades donde el estudiante:

- compare código generado por IA con su propia solución;
- valide sugerencias utilizando la documentación oficial;
- pruebe el script con casos pequeños;
- registre aciertos y errores en `doc/bitacora-ia.md`;
- identifique posibles alucinaciones.

Nunca aceptar código sin validarlo.

---

# Revisión crítica

Mientras construyes la unidad revisa continuamente:

- continuidad con la Unidad 4;
- carga cognitiva;
- coherencia con la filosofía del curso;
- protagonismo de las preguntas biológicas;
- claridad conceptual;
- integración del protocolo reproducible;
- transición natural hacia HPC (S29);
- preparación para BLAST.

Si detectas oportunidades para mejorar la arquitectura, propón ajustes justificados.

---

# Objetivo final

La Unidad 5 debe representar el paso de:

```text
Comandos

↓

Protocolo reproducible

↓

Script

↓

Herramienta bioinformática reutilizable
```

Al finalizar la unidad el estudiante no solo deberá saber escribir scripts.

Deberá comprender que una herramienta bioinformática es la evolución natural de un protocolo científico reproducible.

Ese debe ser el mensaje central de toda la unidad.


