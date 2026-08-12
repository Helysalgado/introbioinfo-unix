# Auditoría de recursos interactivos y flashcards — Curso 2026

**Curso:** Introducción a la Bioinformática · LCG · UNAM · 2026  
**Fuente canónica:** `contenidos-2026/` (S1–S34)  
**Canon leído:** `contenidos-2026/README.md`, `plantilla-unidad.md`, Programa 2026, descripción detallada, portadas de unidad.  
**Fecha:** 2026-08-12  
**Fase:** solo análisis (sin HTML, sin mazos exportables, sin modificar sesiones).

---

## Criterio rector

``` text
pregunta biológica → evidencia → datos → operación → herramienta
→ resultado → verificación → interpretación → conclusión y límites
```

- **HTML:** obliga a decidir, predecir, clasificar, detectar errores o interpretar.  
- **Flashcards:** recuperación fluida de unidades pequeñas que liberan cognición para problemas mayores.  
- **MANTENER:** competencia auténtica (Markdown, SSH/SFTP, terminal, NCBI, `grep`/`sed`/`awk`, scripts, BLAST, SGE, defensa oral, protocolo).

> ¿La interactividad hace pensar mejor o solo se ve más bonita?  
> ¿Recordar esto ayuda a razonar después o solo memoriza lo consultable?

---

## 1. Inventario completo (Entregable 1)

Leyenda de formato: `HTML` · `FLASHCARDS` · `AMBOS` · `MANTENER`.  
Prioridad: `P1` debería desarrollarse · `P2` útil · `P3` opcional · `NO` conservar formato actual.

### Unidad 1 — S1–S2 + portada

| Sesión | Actividad/contenido | Formato | Tipo | Valor | Complejidad | Prioridad | Razón |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U1 portada | Preguntas 1–5 (cuatro principios) | HTML | classify | ALTO | MEDIA | P1 | Casos cortos; ancla del curso |
| U1 portada | Preguntas 6–9 (FAIR, carpetas, IA) | AMBOS | classify / IA | ALTO | BAJA | P1 | HTML + cards de distinción |
| U1 portada | Reto `pacientes.md` (overclaim) | HTML | progressive-case | ALTO | MEDIA | P1 | Caso → evidencia → límites |
| U1 portada | Checklist habilidades | MANTENER | metacog | MEDIO | — | P3 | Reflexión de cierre |
| U1 portada / S1–S2 | Glosarios ES–EN | FLASHCARDS | ES-EN / CONCEPTO | ALTO | BAJA | P1 | Acumulativas a todo el curso |
| S1 | Distinciones reproducibilidad… | AMBOS | DISTINCIÓN | ALTO | BAJA | P1 | Base cognitiva |
| S1 | Procesos A vs B (emparejar) | HTML | match | ALTO | MEDIA | P1 | Antes del protocolo |
| S1 | P1 pregunta→estrategia | MANTENER | design | ALTO | — | P2 | Producto auténtico; HTML solo andamiaje |
| S1 | P2 protocolo + Markdown | MANTENER | produce | ALTO | — | NO | Escritura real |
| S2 | FAIR principio↔acción | AMBOS | match | ALTO | BAJA | P1 | Emparejar + cards |
| S2 | Campos metadatos (concepto) | FLASHCARDS | FORMATO | MEDIO | BAJA | P2 | Campo→función; ficha real se mantiene |
| S2 | P1 árbol + metadatos | MANTENER | produce | ALTO | — | NO | Tarea 2 |
| S2 | Detectar IA defectuosa (`countgenes`) | HTML | find-the-error / IA | ALTO | BAJA | P1 | Caso corto transversal |
| S2 | Anatomía del prompt | AMBOS | classify | MEDIO | BAJA | P2 | Estructura recuperable |
| S2 | P2a/2b IA + bitácora | MANTENER | IA-crítica | ALTO | — | NO | Asistente real + bitácora |

### Unidad 2 — S3–S6

| Sesión | Actividad/contenido | Formato | Tipo | Valor | Complejidad | Prioridad | Razón |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S3 | Preguntas pre-SSH | AMBOS | classify | ALTO | BAJA | P1 | Antes de conectar |
| S3 | P1–P5 SSH/SFTP/checksum | MANTENER | authentic | ALTO | — | NO | No simulador |
| S3–S5 | Glosarios Unix | FLASHCARDS | ES-EN / COMANDO-OP | ALTO | BAJA | P1 | Léxico denso |
| S4 | Predicción rutas abs/rel | HTML | predict | ALTO | BAJA | P1 | Predicción → terminal |
| S4 | Microprácticas filesystem | MANTENER | authentic | ALTO | — | NO | Competencia real |
| S5 | Pausas predicción 1–6 | HTML | predict | ALTO | MEDIA | P1 | Paquete de microciclos |
| S5 | gzip vs tar (situaciones) | AMBOS | classify | ALTO | BAJA | P1 | Decisión conceptual |
| S5 | Actividades permisos/procesos | MANTENER | authentic | ALTO | — | NO | Servidor real |
| S6 | P1 afirmación≠evidencia | AMBOS | predict | ALTO | BAJA | P2 | HTML + comprobar en servidor |
| S6 | P2–P7 consolidación U2 | MANTENER | authentic | ALTO | — | NO | Cierre auténtico |

### Unidad 3 — S7–S9

| Sesión | Actividad/contenido | Formato | Tipo | Valor | Complejidad | Prioridad | Razón |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S7 | Test alfabetos / procesos / elementos | AMBOS | classify / match | ALTO | MEDIA | P1 | Mejor HTML biológico temprano |
| S7 | Secuencia vs anotación | HTML | classify | ALTO | BAJA | P1 | Decisión corta |
| S7 | Interpretar FASTA / GFF3 | HTML | interpret | ALTO | MEDIA | P1 | Sin descarga |
| S7 | ¿Suficiente para reproducir? | HTML | find-the-error | ALTO | MEDIA | P1 | Gaps de evidencia |
| S7–S8 | Glosarios biología/formatos | FLASHCARDS | BIOLOGÍA / FORMATO | ALTO | BAJA | P1 | Mazo rico acumulativo |
| S8 | ¿Qué BD NCBI? | HTML | classify | ALTO | BAJA | P1 | Antes de navegar |
| S8 | Cadena de búsqueda | AMBOS | predict | ALTO | MEDIA | P1 | HTML → NCBI real |
| S8 | ¿Qué archivos pido? | HTML | classify | ALTO | BAJA | P1 | Decisión de familia |
| S8 | Checksum ¿qué demuestra? | HTML | distinguish | ALTO | BAJA | P1 | Integridad≠selección |
| S8 | Ficha procedencia real | MANTENER | produce | ALTO | — | NO | Tarea 4 |
| S9 | MD5 vs SHA-256 (error) | HTML | find-the-error | ALTO | BAJA | P1 | Error clásico |
| S9 | Plan antes de ejecutar | HTML | predict | ALTO | BAJA | P1 | Luego terminal |
| S9 | P2–P5 inspección/transfer | MANTENER | authentic | ALTO | — | NO | No sustituir |

### Unidad 4 — S10–S13, S18–S23 + transversal S14–S17

| Sesión | Actividad/contenido | Formato | Tipo | Valor | Complejidad | Prioridad | Razón |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S10 | P1 predicción tamaño/sesgo | HTML | predict | ALTO | MEDIA | P1 | Compromiso antes de medir |
| S10 | P2–P3 inspección/`wc` | AMBOS / MANTENER | — | ALTO | — | P1/NO | HTML qué mide; terminal ejecuta |
| S10 | Tubería rota / archivo único | AMBOS | find-the-error | ALTO | MEDIA | P1 | Error silencioso |
| S10 | Glosario + errores frecuentes | FLASHCARDS | ERROR / ES-EN | ALTO | BAJA | P1 | Acumulativo U4 |
| S11 | P1 pregunta→dato | HTML | classify | ALTO | BAJA | P1 | Antes de `cut` |
| S11 | P2 diccionario 9 columnas | AMBOS | FORMATO | ALTO | MEDIA | P1 | Cards col→función + HTML |
| S11 | P4 tres evidencias replicones | HTML | compare-evidence | ALTO | MEDIA | P1 | Independencia de evidencia |
| S11 | P3 `cut` real | MANTENER | authentic | ALTO | — | NO | — |
| S12 | P1 predicción genes | HTML | predict | ALTO | BAJA | P1 | Antes de `grep` |
| S12 | P4 clasificar FP de `gene` | HTML | classify / find-error | ALTO | MEDIA | P1 | Ideal pre-`grep` |
| S12 | P2–P3–P5 ejecución | MANTENER | authentic | ALTO | — | NO | — |
| S13 | P1 predicción catálogo | HTML | predict | ALTO | BAJA | P1 | — |
| S13 | P6 tres caminos replicones | HTML | compare-evidence | ALTO | MEDIA | P1 | Cierre acumulativo |
| S13 | Inventario `sort\|uniq` | MANTENER | authentic | ALTO | — | NO | — |
| S14–S15 | Mini-proyecto I | MANTENER | authentic | ALTO | — | NO | Investigación real |
| S15 | ¿Evidencia suficiente? (micro) | AMBOS | compare-evidence | MEDIO | BAJA | P2 | Entrena dictamen |
| S16 | Dictamen / pares | MANTENER | peer | ALTO | — | NO | — |
| S17 | Evaluación demostrativa | MANTENER | eval | ALTO | — | NO | HTML invalidaría |
| S18 | P1 definir gen + P2 matches | HTML | predict | ALTO | MEDIA | P1 | Antes de regex |
| S18 | P3–P6 ejecución | MANTENER | authentic | ALTO | — | NO | — |
| S18 | Cierre IA patrones | AMBOS | IA-crítica | ALTO | BAJA | P1 | `\d`/`\b` inválidos |
| S18 | Glosario anclas | FLASHCARDS | FORMATO | ALTO | BAJA | P1 | — |
| S19 | P1 predicción + P3 zonas `comm` | HTML | compare-evidence | ALTO | MEDIA | P1 | Interpretar zonas |
| S19 | Extracción IDs real | MANTENER | authentic | ALTO | — | NO | — |
| S19 | Cierre IA patrón ambicioso | AMBOS | IA-crítica | ALTO | BAJA | P1 | `.*` vs `[^;]+` |
| S20 | P1 comparables + P3 riesgo reglas | HTML | classify / decision | ALTO | MEDIA | P1 | Antes de `sed` |
| S20 | P4–P7 transformación real | MANTENER | authentic | ALTO | — | NO | — |
| S20 | P6 formato vs discrepancia | HTML | compare-evidence | ALTO | MEDIA | P1 | — |
| S21 | P5–P6 zonas + árbol causas | HTML | decision-tree | ALTO | ALTA | P1 | Mejor HTML U4 |
| S21 | Descarga UniProt / normalizar | MANTENER | authentic | ALTO | — | NO | — |
| S21 | Glosario verificación≠validación | FLASHCARDS | DISTINCIÓN | ALTO | BAJA | P1 | Acumulativa curso |
| S22 | P1 cuatro partes pregunta | HTML | classify | ALTO | BAJA | P1 | Antes de `awk` |
| S22 | P6–P7 comparación tamaños/zonas | HTML | compare-evidence | ALTO | MEDIA | P1 | Narrativa acumulativa |
| S22 | Cálculos `awk` reales | MANTENER | authentic | ALTO | — | NO | — |
| S22 | `$1` `$NF` longitud +1 | FLASHCARDS | COMANDO-OP | ALTO | BAJA | P1 | Exacto al brief |
| S23 | P1 inventariar + P2 orden dependencias | HTML | order-pipeline | ALTO | MEDIA | P1 | Decidir sin ejecutar |
| S23 | P3–P7 protocolo ejecutable | MANTENER | authentic | ALTO | — | NO | — |
| S23 | Cierre IA orden/controles | AMBOS | IA-crítica | ALTO | MEDIA | P1 | Find-the-error en propuesta IA |

### Unidad 5 — S24–S29

| Sesión | Actividad/contenido | Formato | Tipo | Valor | Complejidad | Prioridad | Razón |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S24 | P1 qué automatizar | HTML | decision | ALTO | BAJA | P1 | Alcance sin sustituir script |
| S24 | P2 predecir fracasos | AMBOS | predict / ERROR | ALTO | BAJA | P1 | Mensaje↔causa |
| S24 | P3–P5 script real | MANTENER | authentic | ALTO | — | NO | — |
| S24 | Cierre IA script | HTML | IA-crítica | ALTO | MEDIA | P1 | Fuera de alcance / alucinación |
| S24 | Glosario shebang/PATH | FLASHCARDS | CONCEPTO | ALTO | BAJA | P1 | No pipelines |
| S25 | Frontera dato/método | HTML | classify | ALTO | MEDIA | P1 | Diseño, no sintaxis |
| S25 | Predecir 6 fallos | HTML | progressive-case | ALTO | MEDIA | P1 | Orden invertido peligroso |
| S25 | Parametrizar / validar | MANTENER | authentic | ALTO | — | NO | — |
| S25 | Cierre IA frontera | HTML | IA-crítica | ALTO | BAJA | P1 | — |
| S26 | Recorrido en español | HTML | order | MEDIO | BAJA | P2 | Antes del `for` |
| S26 | Ciclo / bitácora lote | MANTENER | authentic | ALTO | — | NO | No simular `for` |
| S27 | Compañero mudo / README real | MANTENER | authentic | ALTO | — | NO | — |
| S27 | Contrato + README inventado IA | HTML | IA-crítica | ALTO | BAJA | P1 | Alucinación documental |
| S28 | Capstone defensa / datos nuevos | MANTENER | authentic | ALTO | — | NO | — |
| S28 | Mapa afirmación→evidencia | HTML | match | MEDIO | BAJA | P2 | Prepara defensa |
| S29 | ¿Cuándo HPC? | HTML | decision | MEDIO | BAJA | P2 | Criterio; medición real aparte |
| S29 | `qsub`/`qstat` reales | MANTENER | authentic | ALTO | — | NO | No simular SGE |
| S29 | IA Slurm vs SGE | HTML | IA-crítica | ALTO | BAJA | P1 | Error institucional |
| S29 | Glosario HPC | FLASHCARDS | ES-EN | ALTO | BAJA | P1 | — |

### Unidad 6 — S30–S34

| Sesión | Actividad/contenido | Formato | Tipo | Valor | Complejidad | Prioridad | Razón |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U6 portada | 6 principios + resultado≠conclusión | FLASHCARDS | DISTINCIÓN | ALTO | BAJA | P1 | Nuclea U6 |
| S30 | Clustal / MSA reales | MANTENER | authentic | ALTO | — | NO | — |
| S30 | IA «49 % homología» | HTML | IA-crítica | ALTO | MEDIA | P1 | Caso canónico |
| S30 | Global vs local | AMBOS | DISTINCIÓN | ALTO | BAJA | P1 | Prepara BLAST |
| S30–S32 | Glosarios métricas | FLASHCARDS | MÉTRICA | ALTO | BAJA | P1 | Mazo estrella |
| S31 | Diseñar búsqueda | HTML | decision | ALTO | BAJA | P2 | Antes de BLAST |
| S31 | `makeblastdb` / `blastp` | MANTENER | authentic | ALTO | — | NO | — |
| S31 | IA blastn+nr+ortólogo | HTML | IA-crítica | ALTO | MEDIA | P1 | — |
| S32 | Hit A vs B vs C | HTML | compare-evidence | ALTO | MEDIA | P1 | Comparar métricas |
| S32 | Identidad + cobertura (cálculo) | AMBOS | MÉTRICA | ALTO | MEDIA | P1 | HTML + Unix |
| S32 | Cobertura parcial / HBA | HTML | progressive-case | ALTO | MEDIA | P1 | 100% ≠ mismo gen |
| S32 | IA «94% ⇒ ortólogo» | HTML | IA-crítica | ALTO | BAJA | P1 | El «por lo tanto» |
| S33 | Capas obs→hipótesis | HTML | classify | ALTO | BAJA | P1 | — |
| S33 | Globinas / ortólogo-parálogo | HTML | decision / match | ALTO | MEDIA | P1 | Distinciones clave |
| S33 | Semáforo transferencia función | HTML | decision-tree | ALTO | MEDIA | P1 | — |
| S33 | IA salta peldaños | HTML | IA-crítica | ALTO | BAJA | P1 | — |
| S34 | Caso ciego BLAST + informe | MANTENER | authentic | ALTO | — | NO | Capstone real |
| S34 | Auditar informe IA | HTML | IA-crítica | ALTO | ALTA | P1 | Capstone HTML |
| S34 | Hipótesis rivales / árbol | HTML | decision-tree | ALTO | MEDIA | P2 | Prepara informe |
| S34 | Defensa oral | MANTENER | oral | ALTO | — | NO | — |

---

## 2. Top 5 HTML (Entregable 4)

| Rank | Sesión | Actividad | Beneficio pedagógico | Esfuerzo técnico | Por qué empezar aquí |
| --- | --- | --- | --- | --- | --- |
| 1 | S21 | Árbol de causas de discrepancia (P6) | Integra verificación/validación, `comm`, independencia | MEDIA | Patrón `progressive-case` + `decision-tree`; alto ROI U4 |
| 2 | S32 | Comparar Hit A vs B vs C | Obliga a usar métricas juntas, no de memoria | MEDIA | Complemento perfecto del mazo BLAST; no sustituye BLAST |
| 3 | S12 | Clasificar falsos positivos de `gene` | Predicción→auditoría antes de `grep` | BAJA | Datos sintéticos fáciles; reutilizable en S18 |
| 4 | S30/S33 | IA «% homología» / «% ⇒ ortólogo» | Eje IA-crítica del curso en U6 | BAJA | Casos fijos, feedback rico, sin servidor |
| 5 | S2 | Detectar respuesta IA defectuosa | Introduce validación IA desde U1 | BAJA | Ya existe en el módulo; portar a HTML autocontenido |

---

## 3. Mejores mazos de flashcards (Entregable 5)

| Rank | Unidad / sesiones | Mazo | Conceptos clave | Nº aprox. | Beneficio | Prioridad |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | U1→todo | Principios científicos | reproducibilidad, verificación≠validación, robustez, FAIR≠abierto | 12–15 | Base de todo razonamiento | P1 |
| 2 | U4 S11–S22 | Columnas GFF + `$1`/`$NF` | cols 1–9, 1-based, longitud+1, FS tab | 15–20 | Libera cognición en taller U4/U5 | P1 |
| 3 | U6 S30–S34 | Métricas BLAST | pident, cobertura, E-value, bitscore, HSP | 12–15 | Imprescindible para interpretar | P1 |
| 4 | U6 S30–S33 | Distinciones evolutivas | similitud≠homología, ortólogo/parálogo, transferencia | 10–12 | Evita saltos injustificados | P1 |
| 5 | U3 S7–S9 | Biología + formatos + IDs | FASTA/GFF/GenBank, accession vs ensamblado, checksum | 15 | Puente biología↔dato | P1 |
| — | U2 S3–S5 | Unix conceptual | terminal≠shell, rutas, gzip≠tar, permisos | 12–14 | Antes del lab | P1 |
| — | U5 S24–S25 | Scripting conceptual | shebang, PATH, fallo silencioso, `-f`≠`-s` | 10–12 | Sin memorizar pipelines | P1 |
| — | Transversal | IA-crítica | alucinación, primero a mano, qué no afirmar | 8–10 | Espaciado U1–U6 | P2 |

**Total aproximado recomendado:** 100–130 tarjetas de calidad (no cientos), con ~25–35 marcadas **ACUMULATIVAS**.

---

## 4. Patrones HTML reutilizables (Entregable 7)

| Componente | Función pedagógica | Sesiones donde reutilizar |
| --- | --- | --- |
| `multiple-choice-feedback` | Elegir con justificación y pista | U1 portada, S3, S8, S31 diseño |
| `predict-then-reveal` | Comprometerse antes de ver resultado | S4, S5, S10, S12, S18, S24/S25 |
| `classify-cards` | Clasificar ítems en categorías | S7 alfabetos, S12 FP, S20 riesgo, S25 frontera |
| `match-concepts` | Emparejar término↔definición / fase↔proceso | S1 A↔B, S2 FAIR, S11 cols, S28 evidencia |
| `order-pipeline` | Ordenar pasos por dependencia | S23, S26 recorrido, S8 cadena NCBI |
| `find-the-error` | Detectar fallo técnico o conceptual | S2 IA, S9 MD5≠SHA, S10 tubería, S23 IA |
| `compare-evidence` | Jerarquizar o contrastar evidencias | S11/S13 replicones, S19/S21 `comm`, S32 hits |
| `progressive-case` | Caso → decisión → pista → nueva evidencia | U1 reto, S21, S32 cobertura parcial, S34 |
| `decision-tree` | Árbol de causas o semáforo | S21 P6, S33 transferencia, S34 árbol |
| `ai-error-detection` | Auditar texto/código generado | S2, S18–S23, S24–S29, S30–S34 |

---

## 5. Arquitectura futura (Entregable 8)

Propuesta **sin crear directorios todavía**:

``` text
interactive/
├── components/          # plantillas JS/CSS de los 10 patrones
├── u1/ … u6/            # una carpeta por unidad; HTML autocontenidos
└── shared/              # datasets sintéticos mínimos para HTML

flashcards/
├── u1/ … u6/
├── acumulativas/        # mazos que cruzan unidades
└── source/              # CSV/TSV o Markdown YAML front+back
```

**Formato fuente de flashcards:** CSV/TSV o Markdown estructurado (`frente`, `reverso`, `tipo`, `unidad`, `sesiones`, `acumulativa`, `prioridad`) → exportar después a Anki/Quizlet/plataforma elegida.

**Restricciones HTML (fase futura):** navegador, autocontenidos, HTML+CSS+JS, sin frameworks salvo necesidad, offline cuando sea posible, responsive, teclado, semántico, feedback local, sin telemetría, versionados en Git junto al curso.

---

## 6. Informe final (sección 23 del brief)

| Indicador | Estimación |
| --- | --- |
| 1. Actividades/contenidos revisados | ~160–180 ítems (prácticas, microprácticas, glosarios, cierres IA, predicciones, transversales) |
| 2. Candidatas HTML (P1–P3, no solo P1) | ~55–65 |
| 3. Candidatas flashcards (mazos/ítems) | ~12 mazos · ~100–130 tarjetas |
| 4. Candidatas `AMBOS` | ~35–45 |
| 5. Distribución prioridad (aprox.) | P1 ~45 · P2 ~35 · P3 ~20 · NO ~60+ (auténticas) |
| 6. Top 5 HTML | S21 árbol causas · S32 hits · S12 FP `gene` · S30/S33 IA % · S2 IA defectuosa |
| 7. Mejores mazos | Principios U1 · GFF/`awk` · Métricas BLAST · Distinciones evolutivas · Biología/formatos |
| 8. Nº total tarjetas recomendado | **100–130** |
| 9. Flashcards acumulativas | Principios U1; verificación≠validación; cols GFF; identidad→cobertura→homología; checksum≠selección |
| 10. Patrones HTML | 10 componentes listados arriba |
| 11. Mejores secuencias `FC→HTML→auténtica→protocolo` | Ver `matriz-html-flashcards-2026.md` |
| 12. Riesgos pedagógicos | (a) Simular Unix/BLAST/SGE y vaciar la competencia; (b) flashcards de pipelines/opciones raras; (c) HTML solo “correcto/incorrecto” sin forzar revisión del razonamiento; (d) saturar S14–S17 con interactivos que compiten con evaluación auténtica; (e) mazos aislados por sesión sin recuperación espaciada |

### Riesgos — detalle breve

1. **Sustitución accidental:** cualquier HTML que “ejecute” tuberías, BLAST o `qsub` debilita el curso.  
2. **Memorización vacía:** memorizar flags raros o resultados de un genoma concreto no libera cognición.  
3. **Feedback pobre:** sin pista que reabra el razonamiento, el HTML es adorno.  
4. **Sobrecarga U4:** demasiados HTML en S10–S23 compiten con el tiempo de terminal; priorizar predicción *antes* del lab.  
5. **IA simulada vs real:** los casos fijos de alucinación son HTML; la bitácora con asistente real se mantiene.

---

## Archivos hermanos

- [`shortlist-practicas-html-2026.md`](shortlist-practicas-html-2026.md)  
- [`inventario-flashcards-2026.md`](inventario-flashcards-2026.md)  
- [`matriz-html-flashcards-2026.md`](matriz-html-flashcards-2026.md)  
- Prompt origen: [`../prompts-ia/prompt-cursor-auditoria-html-flashcards.md`](../prompts-ia/prompt-cursor-auditoria-html-flashcards.md)
