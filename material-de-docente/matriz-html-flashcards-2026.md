# Matriz HTML + flashcards — secuencias recomendadas (2026)

Busca el patrón:

``` text
flashcards → HTML → práctica auténtica → protocolo
```

Solo se listan secuencias con **valor claro**. Las sesiones de evaluación auténtica (S14–S17, S28 defensa, S34 oral) aparecen como destino, no como HTML sustituto.

---

## Matriz por sesión / bloque

| Sesión / bloque | Flashcards preparan | HTML aplica | Práctica auténtica posterior | Valor |
| --- | --- | --- | --- | --- |
| **U1 portada + S1** | Principios; verificación≠validación | Casos principios + reto overclaim; emparejar fases A/B | Protocolo Markdown; pregunta→estrategia | ALTO |
| **S2** | FAIR; alucinación; prompt | Detectar IA defectuosa; anatomía de prompt | Metadatos reales; bitácora con IA real | ALTO |
| **S3** | Terminal≠shell; SSH≠SFTP; checksum | Preguntas pre-conexión | SSH/SFTP + checksum reales | ALTO |
| **S4** | Rutas abs/rel; `.` `..` | Predicción de rutas | Navegar/copiar/estructura en servidor | ALTO |
| **S5** | gzip≠tar; permisos; PID | Pausas de predicción 1–6 | Inspección, `chmod`, procesos reales | ALTO |
| **S6** | Afirmación≠evidencia | Micro “¿cómo lo compruebo?” | Consolidación U2 en servidor | MEDIO |
| **S7** | Secuencia≠anotación; formatos; IDs | Test alfabetos; interpretar FASTA/GFF | Matriz pregunta→formato en protocolo | ALTO |
| **S8** | Cadena NCBI; checksum≠selección | Elegir BD/archivos; V/F checksum | Descarga NCBI + ficha procedencia | ALTO |
| **S9** | MD5≠SHA; inspección≠integridad | Plan + error de algoritmos | `md5sum`/`wget`/transfer reales | ALTO |
| **S10** | `wc`; `>`/`>>`/`\|`; archivo único | Predicción tamaño/sesgo; tubería rota | Inspección y pipes reales | ALTO |
| **S11** | Columnas GFF 1–9; `.`≠`0` | Pregunta→columna; 3 evidencias replicones | `cut`/`head` reales | ALTO |
| **S12** | FP/FN; por qué infla `gene` | Clasificar líneas FP | `grep`/`wc` reales | ALTO |
| **S13** | Registro≠objeto; `sort\|uniq` | Predicción catálogo; 3 caminos | Inventario Estado 1 real | ALTO |
| **S14–S17** | Criterios de evidencia (breve) | Micro “¿evidencia suficiente?” (P2) | Mini-proyecto, dictamen, evaluación | MEDIO (HTML mínimo) |
| **S18** | `^` `$`; anclar≠columnas | Matches de patrones; definición de gen | `grep -E` + tabla refinamiento | ALTO |
| **S19** | Seleccionar≠recuperar; objeto≠registro | Zonas de `comm`; predicción discrepancia | Extracción IDs + `comm` | ALTO |
| **S20** | Normalizar≠filtrar; colisión | Riesgo de reglas; formato vs discrepancia | `sed`/`tr` + cardinalidad | ALTO |
| **S21** | Coherencia≠validación | **Árbol de causas**; zonas confrontación | UniProt real + `comm` | ALTO (estrella U4) |
| **S22** | `$1` `$NF`; longitud+1; conteo≠densidad | Descomponer pregunta; comparar tamaños/zonas | `awk` real | ALTO |
| **S23** | Entrada/derivado/control | Ordenar dependencias; error en propuesta IA | Protocolo ejecutable regenerable | ALTO |
| **S24** | Shebang; PATH; fallo silencioso | Qué automatizar; predecir fracasos; IA script | Primer script + validar vs manual | ALTO |
| **S25** | Frontera dato/método; `-f`≠`-s` | Clasificar literales; 6 fallos; IA frontera | Parametrizar + validar entradas | ALTO |
| **S26** | `>` vs `>>` en lotes | Recorrido en español (P2) | `for` real + bitácora de lote | MEDIO |
| **S27** | Contrato (términos) | README inventado por IA | README real + prueba cruzada | MEDIO |
| **S28** | Trazabilidad (breve) | Mapa afirmación→evidencia (warm-up) | Datos nuevos + defensa oral | MEDIO |
| **S29** | Login≠compute; SGE≠Slurm | ¿Cuándo HPC?; detectar `#SBATCH` | `qsub`/`qstat` reales + checksum | ALTO |
| **S30** | Similitud≠homología; identidad | IA «% homología»; global vs local | Clustal/MSA reales | ALTO |
| **S31** | HSP; seed; obs≠inferencia | Diseñar búsqueda; IA blastn+ortólogo | `makeblastdb` / BLAST reales | ALTO |
| **S32** | pident; cobertura; E-value; bitscore | **Hit A vs B vs C**; cobertura parcial; IA «⇒ ortólogo» | Cálculos/filtros sobre `.tsv` | ALTO (estrella U6) |
| **S33** | Ortología/paralogía; transferencia | Globinas; historias; semáforo función; IA peldaños | Argumentación + datos de apoyo | ALTO |
| **S34** | Mazos U6 acumulados | Auditar informe IA; hipótesis rivales | Caso ciego BLAST + informe + defensa | ALTO |

---

## Secuencias ejemplares (para diseño)

### 1. Principios → protocolo (arranque del curso)

``` text
FLASHCARDS  reproducibilidad · verificación≠validación · FAIR≠abierto
     ↓
HTML        casos U1 + reto pacientes.md + IA defectuosa S2
     ↓
PRÁCTICA    protocolo.md · metadatos · bitácora-IA real
     ↓
PROTOCOLO   pregunta, límites, declaración de incertidumbre
```

### 2. Formatos → NCBI (U3)

``` text
FLASHCARDS  FASTA/GFF/GenBank · IDs · checksum≠selección
     ↓
HTML        alfabetos · ¿qué archivo? · ¿qué demuestra el checksum?
     ↓
PRÁCTICA    descarga NCBI · md5sum · transferencia
     ↓
PROTOCOLO   ficha de procedencia
```

### 3. Predicción → filtrado genómico (U4 núcleo)

``` text
FLASHCARDS  columnas GFF · FP · ^$ · $1/$NF
     ↓
HTML        clasificar FP · matches regex · descomponer pregunta · árbol S21
     ↓
PRÁCTICA    cut/grep/sed/comm/awk reales
     ↓
PROTOCOLO   Estado 1 refinado · contraste de fuentes · límites
```

### 4. Automatizar con criterio (U5)

``` text
FLASHCARDS  shebang · PATH · fallo silencioso · frontera dato/método
     ↓
HTML        qué automatizar · predecir fallos · criticar script/README IA
     ↓
PRÁCTICA    script · parámetros · lote · qsub
     ↓
PROTOCOLO   citar script · bitácora · declaración S28
```

### 5. Interpretar similitud (U6)

``` text
FLASHCARDS  identidad · cobertura · E-value · similitud≠homología · ortólogo/parálogo
     ↓
HTML        Hit A/B/C · cobertura parcial · IA % · transferencia · informe S34
     ↓
PRÁCTICA    Clustal + BLAST + caso ciego
     ↓
PROTOCOLO   observación / inferencia / alternativas / límites / bitácora
```

### 6. IA crítica (transversal)

``` text
FLASHCARDS  alucinación · qué se puede afirmar · primero a mano
     ↓
HTML        casos fijos S2, S18–S23, S24–S29, S30–S34
     ↓
PRÁCTICA    contrastar con man, ejecución o .tsv propio
     ↓
PROTOCOLO  doc/bitacora-ia.md
```

---

## Prioridad de implementación sugerida (oleadas)

| Oleada | Flashcards (fuente CSV) | HTML | No tocar |
| --- | --- | --- | --- |
| **1** | Principios U1 · GFF/`awk` · Métricas BLAST | S2 IA · S12 FP · S21 árbol · S32 hits · S30/S33 IA % | Terminal, BLAST, SGE |
| **2** | Biología/formatos · Unix conceptual · Scripting conceptual | S7/S8 · S5 predicciones · S18 matches · S24/S25 decisiones | Productos calificados |
| **3** | Distinciones evolutivas · HPC · IA-crítica acumulativa | S19/S20 · S23 pipeline · S34 informe IA · S29 Slurm≠SGE | S14–S17 evaluación |

---

## Nota de diseño

El HTML debe vivir **antes** del taller (aula invertida) o como **calentamiento de 5–10 min**, nunca como reemplazo del bloque de ejecución. Las flashcards deben reaparecer días/semanas después (acumulativas), no solo al cerrar la sesión.
