# Shortlist — prácticas HTML candidatas (2026)

Selecciona ~12–15 mejores candidatas HTML del curso, **sin cuota por unidad**.  
Criterio: interactividad que obliga a pensar mejor; no sustituye Unix, BLAST, SGE ni protocolo.

---

## 1. S21 — Árbol de causas de discrepancia

| Campo | Detalle |
| --- | --- |
| **Sesión** | S21 — Confrontar fuente independiente |
| **Actividad original** | P6: formular hipótesis por zona de `comm` (alcance, versión, filtros, error…) |
| **Oportunidad** | Integra validación externa, asimetría de listas y límites de la evidencia |
| **Interacción propuesta** | Caso con diferencia observada → elegir causa → pista → nueva evidencia → reformular |
| **Tipo** | `decision-tree` + `progressive-case` |
| **Antes** | Flashcards verificación≠validación; zonas de `comm` |
| **Después** | Ejecutar contraste real UniProt↔propio; documentar en protocolo |
| **NO sustituye** | Descarga, normalización ni `comm` reales |
| **Valor** | ALTO · **Complejidad** MEDIA · **Prioridad** P1 |

## 2. S32 — Comparar Hit A vs Hit B vs Hit C

| Campo | Detalle |
| --- | --- |
| **Sesión** | S32 — Interpretar / inferir |
| **Actividad original** | Ranking argumentado con ≥3 métricas |
| **Oportunidad** | Usar identidad, cobertura, E-value y bitscore *juntos* |
| **Interacción** | Tres hits sintéticos → elegir candidato → justificar → revelar trampa (p. ej. alta identidad / baja cobertura) |
| **Tipo** | `compare-evidence` |
| **Antes** | Mazo métricas BLAST |
| **Después** | Calcular/filtrar `.tsv` propio; BLAST real si aplica |
| **NO sustituye** | BLAST ni parsing Unix del output |
| **Valor** | ALTO · MEDIA · P1 |

## 3. S12 — Clasificar falsos positivos de `gene`

| Campo | Detalle |
| --- | --- |
| **Sesión** | S12 — Filtrado y conteos |
| **Actividad original** | P4 auditoría de coincidencias (col3 / pseudogene / atributos) |
| **Oportunidad** | Ver *por qué* `grep gene` infla antes de ejecutar |
| **Interacción** | Líneas GFF sintéticas → clasificar en categorías FP/OK → feedback |
| **Tipo** | `classify-cards` + `predict-then-reveal` |
| **Antes** | Flashcards FP/FN, “palabra completa” |
| **Después** | `grep`/`cut` reales sobre el genoma del estudiante |
| **NO sustituye** | Conteos reales |
| **Valor** | ALTO · BAJA · P1 |

## 4. S30 / S33 — Detectar errores en texto de IA (% homología / % ⇒ ortólogo)

| Campo | Detalle |
| --- | --- |
| **Sesión** | S30 y S33 |
| **Actividad original** | Párrafos IA con ≥5 errores; frase «94% ⇒ ortólogo» |
| **Oportunidad** | Eje IA-crítica de U6 con casos fijos reproducibles |
| **Interacción** | Marcar afirmaciones (hecho / inferencia / injustificado) + feedback por error |
| **Tipo** | `ai-error-detection` |
| **Antes** | Flashcards similitud≠homología |
| **Después** | Verificar con alineamiento/BLAST propios; bitácora |
| **NO sustituye** | Clustal/BLAST ni bitácora con asistente real |
| **Valor** | ALTO · BAJA · P1 |

## 5. S2 — Respuesta IA defectuosa (`countgenes`)

| Campo | Detalle |
| --- | --- |
| **Sesión** | S2 — FAIR e IA |
| **Actividad original** | Detectar comando inventado y cita falsa |
| **Oportunidad** | Primera experiencia de validación independiente de IA |
| **Interacción** | Texto defectuoso → señalar sospechas → contrastar con criterio → conclusión de confiabilidad |
| **Tipo** | `ai-error-detection` + `find-the-error` |
| **Antes** | Definición de alucinación / prompt |
| **Después** | Práctica 2 con asistente real + bitácora |
| **NO sustituye** | Uso real de IA ni bitácora |
| **Valor** | ALTO · BAJA · P1 |

## 6. U1 portada — Principios + reto `pacientes.md`

| Campo | Detalle |
| --- | --- |
| **Sesión** | Portada U1 |
| **Actividad original** | Preguntas 1–5 y reto de overclaim IMC–dx |
| **Oportunidad** | Anclar reproducibilidad/verificación/validación desde el día 1 |
| **Interacción** | Casos cortos + caso progresivo de afirmación vs evidencia |
| **Tipo** | `multiple-choice-feedback` + `progressive-case` |
| **Antes** | Lectura de secciones conceptuales |
| **Después** | Protocolo y prácticas S1–S2 |
| **NO sustituye** | Escritura del protocolo |
| **Valor** | ALTO · MEDIA · P1 |

## 7. S11 — Mapa de columnas GFF + tres evidencias de replicones

| Campo | Detalle |
| --- | --- |
| **Sesión** | S11 |
| **Actividad original** | P2 diccionario columnas; P4 jerarquizar evidencias |
| **Oportunidad** | Traducir pregunta biológica → campo, sin abrir aún el archivo |
| **Interacción** | Pregunta→elegir columna; luego ordenar tres fuentes por independencia |
| **Tipo** | `match-concepts` + `compare-evidence` |
| **Antes** | Flashcards col 1–9 |
| **Después** | `cut`/`head` reales |
| **NO sustituye** | Inspección tabular real |
| **Valor** | ALTO · MEDIA · P1 |

## 8. S18 — ¿Qué líneas matchean `^gene$`?

| Campo | Detalle |
| --- | --- |
| **Sesión** | S18 |
| **Actividad original** | P2 ver antes de ejecutar |
| **Oportunidad** | Predicción de anclas antes de `grep -E` |
| **Interacción** | Cadenas de prueba → marcar coincidencias de dos patrones → revelar |
| **Tipo** | `predict-then-reveal` |
| **Antes** | Flashcards `^` `$` |
| **Después** | Ejecutar sobre GFF propio; tabla S13→S18 |
| **NO sustituye** | Regex en terminal ni visualizadores solo-online como evidencia |
| **Valor** | ALTO · BAJA · P1 |

## 9. S20 — Clasificar riesgo de reglas de normalización

| Campo | Detalle |
| --- | --- |
| **Sesión** | S20 |
| **Actividad original** | P3 política de normalización (aceptar/descartar reglas) |
| **Oportunidad** | Ver que “limpiar” puede colisionar identidades |
| **Interacción** | Reglas candidatas → clasificar riesgo → justificar → feedback de colisión |
| **Tipo** | `classify-cards` + `decision-tree` |
| **Antes** | Flashcards normalizar≠filtrar |
| **Después** | `sed`/`tr` + cardinalidad reales |
| **NO sustituye** | Transformación real |
| **Valor** | ALTO · MEDIA · P1 |

## 10. S23 — Ordenar dependencias del protocolo ejecutable

| Campo | Detalle |
| --- | --- |
| **Sesión** | S23 |
| **Actividad original** | P2 orden por dependencia |
| **Oportunidad** | Decidir el pipeline *antes* de pegar comandos |
| **Interacción** | Tarjetas de bloques → ordenar → validar dependencias → puntos de control |
| **Tipo** | `order-pipeline` |
| **Antes** | Flashcards entrada/derivado/resultado |
| **Después** | Ensamblar y regenerar protocolo real |
| **NO sustituye** | Ejecución limpia ni síntesis del genoma |
| **Valor** | ALTO · MEDIA · P1 |

## 11. S24 / S25 — Qué automatizar + frontera dato/método + fallos

| Campo | Detalle |
| --- | --- |
| **Sesión** | S24–S25 |
| **Actividad original** | P1 elegir bloque; P1 frontera; predicción de fracasos |
| **Oportunidad** | Automatizar con criterio, no “porque ya sé bash” |
| **Interacción** | Elegir alcance → clasificar literales → predecir mensajes de error |
| **Tipo** | `decision` + `classify-cards` + `predict-then-reveal` |
| **Antes** | Flashcards shebang/PATH/`-f`≠`-s` |
| **Después** | Escribir/parametrizar/validar script real |
| **NO sustituye** | Scripting en terminal |
| **Valor** | ALTO · MEDIA · P1 |

## 12. S7 / S8 — Formatos, IDs y qué demuestra un checksum

| Campo | Detalle |
| --- | --- |
| **Sesión** | S7–S8 |
| **Actividad original** | Test alfabetos; secuencia vs anotación; familia de archivos; checksum |
| **Oportunidad** | Razonar biología↔formato *antes* de NCBI/terminal |
| **Interacción** | Clasificar necesidades → elegir formato/BD → V/F sobre checksum |
| **Tipo** | `classify-cards` + `match-concepts` |
| **Antes** | Flashcards biología/formatos |
| **Después** | Descarga NCBI + ficha de procedencia |
| **NO sustituye** | NCBI ni transferencia |
| **Valor** | ALTO · MEDIA · P1 |

## 13. S34 — Auditar informe IA completo (capstone HTML)

| Campo | Detalle |
| --- | --- |
| **Sesión** | S34 |
| **Actividad original** | P5 auditar informe generado |
| **Oportunidad** | Integrar todas las distinciones U6 en un solo artefacto |
| **Interacción** | Informe ficticio → marcar hecho/inferencia/sin evidencia → semáforo de transferencia |
| **Tipo** | `ai-error-detection` + `progressive-case` |
| **Antes** | Mazos métricas + evolutivas; HTML S32–S33 |
| **Después** | Caso ciego real + defensa oral + protocolo |
| **NO sustituye** | BLAST del caso ciego ni defensa |
| **Valor** | ALTO · ALTA · P1 |

## 14. S5 — Pausas de predicción (paquete Unix)

| Campo | Detalle |
| --- | --- |
| **Sesión** | S5 |
| **Actividad original** | Pausas 1–6 (inspección, gzip, chmod, jobs…) |
| **Oportunidad** | Microciclos predicción→feedback→lab |
| **Interacción** | Seis viñetas con `predict-then-reveal` |
| **Tipo** | `predict-then-reveal` |
| **Antes** | Flashcards Unix conceptual |
| **Después** | Actividades reales en servidor |
| **NO sustituye** | Permisos/procesos reales |
| **Valor** | ALTO · MEDIA · P1 |

## 15. S19 — Interpretar las tres zonas de `comm`

| Campo | Detalle |
| --- | --- |
| **Sesión** | S19 |
| **Actividad original** | P3 zonas solo-A / ambas / solo-B |
| **Oportunidad** | Interpretar asimetría antes de automatizar el relato |
| **Interacción** | Listas pequeñas → asignar IDs a zonas → hipótesis de discrepancia |
| **Tipo** | `compare-evidence` |
| **Antes** | Flashcards objeto≠registro |
| **Después** | Extracción real de IDs + `comm` |
| **NO sustituye** | `grep -o` / `comm` |
| **Valor** | ALTO · BAJA · P1 |

---

## Fuera de shortlist (explícito)

Mantener como están: SSH/SFTP, descarga NCBI, mini-proyecto S14–S17, evaluación S17, scripts S24–S28, `qsub` S29, Clustal/BLAST reales, caso ciego S34, escritura de protocolo y bitácora con IA real.
