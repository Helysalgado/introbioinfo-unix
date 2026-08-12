# Inventario de flashcards — Curso 2026

Propuestas de **frente/reverso** (no mazos definitivos).  
Prioriza calidad y recuperación espaciada. Total orientativo: **100–130** tarjetas.

Tipos: `CONCEPTO` · `DISTINCIÓN` · `ES-EN` · `FORMATO` · `COMANDO-OPERACIÓN` · `MÉTRICA` · `ERROR-FRECUENTE` · `BIOLOGÍA` · `REPRODUCIBILIDAD` · `IA-CRÍTICA`

---

## Unidad 1 — Principios y organización

**Propósito del mazo:** recuperar con fluidez las distinciones que sostienen todo el curso.

| ID | Sesión origen | Tipo | Frente propuesto | Reverso esperado | ¿Acumulativa? | Prioridad |
| --- | --- | --- | --- | --- | --- | --- |
| U1-01 | S1 | DISTINCIÓN | Reproducibilidad | Regenerar resultados con los **mismos** datos, procedimientos y herramientas documentados | Sí | P1 |
| U1-02 | S1 | DISTINCIÓN | Replicabilidad | Evidencia compatible con datos o estudios **independientes** | Sí | P1 |
| U1-03 | S1 | DISTINCIÓN | Verificación vs validación | Verificación: ¿archivos/comandos hacen lo esperado? · Validación: ¿la evidencia responde la pregunta biológica? | Sí | P1 |
| U1-04 | S1 | CONCEPTO | Robustez | La conclusión no depende de una sola vía frágil | Sí | P1 |
| U1-05 | S1 | DISTINCIÓN | ¿Reproducible = correcto? | No: puede regenerarse y aun así usar la operación equivocada | Sí | P1 |
| U1-06 | S1 | CONCEPTO | Orden del razonamiento | Pregunta → evidencia → datos → operación → herramienta | Sí | P1 |
| U1-07 | S2 | CONCEPTO | FAIR | Findable, Accessible, Interoperable, Reusable | Sí | P1 |
| U1-08 | S2 | DISTINCIÓN | FAIR ≠ datos abiertos | FAIR no exige gratuidad; sí metadatos, acceso claro, formatos y reutilización | Sí | P1 |
| U1-09 | S2 | REPRODUCIBILIDAD | `data/source/` vs `data/processed/` | Originales inmutables vs derivados regenerables | Sí | P1 |
| U1-10 | S2 | CONCEPTO | Metadatos | Datos que describen un dato | Sí | P1 |
| U1-11 | S2 | ES-EN | Procedencia | Provenance — origen e historia del dato | Sí | P1 |
| U1-12 | S2 | IA-CRÍTICA | Alucinación (en LLM) | Respuesta falsa pero verosímil (comando, opción o cita inventados) | Sí | P1 |
| U1-13 | S2 | CONCEPTO | Prompt | Texto (instrucción/encargo) que orienta la respuesta de un asistente de IA | No | P2 |
| U1-14 | S1 | ES-EN | Verificación | Verification | Sí | P2 |

---

## Unidad 2 — Unix conceptual (no pipelines)

**Propósito:** fluidez léxica y distinciones *antes* del laboratorio SSH.

| ID | Sesión | Tipo | Frente | Reverso | ¿Acumulativa? | Prioridad |
| --- | --- | --- | --- | --- | --- | --- |
| U2-01 | S3 | DISTINCIÓN | Terminal vs shell | Terminal = interfaz; shell = interpreta y ejecuta | Sí | P1 |
| U2-02 | S3 | COMANDO-OPERACIÓN | Anatomía `ls -l archivo` | comando · opción · argumento | Sí | P1 |
| U2-03 | S3 | DISTINCIÓN | SSH vs SFTP | Sesión remota cifrada vs transferencia de archivos | Sí | P1 |
| U2-04 | S3 | CONCEPTO | Checksum | Huella del contenido para comprobar **integridad** | Sí | P1 |
| U2-05 | S4 | DISTINCIÓN | Ruta absoluta vs relativa | Empieza en `/` vs parte del directorio actual | Sí | P1 |
| U2-06 | S4 | CONCEPTO | `.` y `..` | Actual · padre | Sí | P1 |
| U2-07 | S5 | DISTINCIÓN | Comprimir vs empaquetar | `gzip` reduce un archivo · `tar` reúne varios | Sí | P1 |
| U2-08 | S5 | DISTINCIÓN | `x` en archivo vs directorio | Ejecutar · recorrer/entrar | Sí | P1 |
| U2-09 | S5 | ERROR-FRECUENTE | ¿`chmod 777`? | No: privilegio mínimo (`u+x` cuando baste) | Sí | P1 |
| U2-10 | S5 | CONCEPTO | PID | Identificador de un proceso en ejecución | No | P2 |
| U2-11 | S3 | ES-EN | Shell | Shell (intérprete de comandos) | Sí | P2 |
| U2-12 | S6 | DISTINCIÓN | Afirmación vs evidencia | Creer que tienes X ≠ poder demostrarlo con un comando | Sí | P2 |

---

## Unidad 3 — Biología, formatos e identificadores

**Propósito:** conectar pregunta biológica ↔ tipo de dato ↔ formato ↔ ID.

| ID | Sesión | Tipo | Frente | Reverso | ¿Acumulativa? | Prioridad |
| --- | --- | --- | --- | --- | --- | --- |
| U3-01 | S7 | BIOLOGÍA | Gen ≠ necesariamente proteína | Algunos genes producen ARN funcional | Sí | P1 |
| U3-02 | S7 | DISTINCIÓN | Secuencia vs anotación | Orden de símbolos vs afirmaciones sobre ubicación/función | Sí | P1 |
| U3-03 | S7 | FORMATO | FASTA → función | Representar una o más secuencias | Sí | P1 |
| U3-04 | S7 | FORMATO | GFF3 → función | Anotaciones con coordenadas/atributos | Sí | P1 |
| U3-05 | S7 | FORMATO | GenBank → función | Secuencia + anotación + metadatos | Sí | P1 |
| U3-06 | S7 | DISTINCIÓN | `GCF_…` vs `NC_…` | Accession de ensamblado vs de secuencia | Sí | P1 |
| U3-07 | S7 | DISTINCIÓN | `araC` vs accession | Nombre biológico (ambiguo) vs ID de repositorio | Sí | P1 |
| U3-08 | S8 | DISTINCIÓN | Checksum correcto demuestra… | Integridad de la copia · **no** que el organismo/versión sean los correctos | Sí | P1 |
| U3-09 | S8 | CONCEPTO | Cadena de decisiones NCBI | Organismo → cepa → ensamblado → versión → registro | Sí | P1 |
| U3-10 | S9 | ERROR-FRECUENTE | Comparar MD5 con SHA-256 | Algoritmos distintos → la comparación no demuestra nada | Sí | P1 |
| U3-11 | S7 | ES-EN | Feature (elemento) | Feature — elemento anotado del genoma | Sí | P1 |
| U3-12 | S7 | ES-EN | Strand / cadena | Strand — hebra `+` o `-` | Sí | P1 |
| U3-13 | S7 | BIOLOGÍA | CDS | Región del transcrito que se traduce | Sí | P2 |
| U3-14 | S7 | BIOLOGÍA | Exón vs intrón | Permanece en ARN maduro vs se elimina | No | P2 |

---

## Unidad 4 — Flujos, GFF, conteos, normalización, awk

**Propósito:** liberar cognición en el taller de filtrado y contraste.

| ID | Sesión | Tipo | Frente | Reverso | ¿Acumulativa? | Prioridad |
| --- | --- | --- | --- | --- | --- | --- |
| U4-01 | S10 | COMANDO-OPERACIÓN | ¿Qué mide `wc -c` sobre un FASTA? | Bytes del **archivo**, no pb del genoma | Sí | P1 |
| U4-02 | S10 | COMANDO-OPERACIÓN | `>` vs `>>` vs `\|` | Sobrescribe · añade · conecta stdout→stdin | Sí | P1 |
| U4-03 | S10 | ERROR-FRECUENTE | Regla del archivo único | Solo el **primer** eslabón de la tubería nombra el archivo | Sí | P1 |
| U4-04 | S11 | FORMATO | Columna 3 GFF3 | `type` — clase del *feature* | Sí | P1 |
| U4-05 | S11 | FORMATO | Columnas 4–5 | `start`–`end` — coordenadas **1-based inclusivas** | Sí | P1 |
| U4-06 | S11 | FORMATO | Columna 9 | `attributes` — pares `clave=valor` separados por `;` | Sí | P1 |
| U4-07 | S11 | DISTINCIÓN | `.` vs `0` en score | `.` = sin valor · `0` = valor medido | Sí | P1 |
| U4-08 | S12 | DISTINCIÓN | Falso positivo (filtrado) | Línea seleccionada que **no** pertenece al conjunto buscado | Sí | P1 |
| U4-09 | S12 | ERROR-FRECUENTE | ¿Por qué `grep gene` infla? | Coincide en atributos y en `pseudogene` | Sí | P1 |
| U4-10 | S13 | DISTINCIÓN | Registro vs objeto biológico | Una línea ≠ un gen; un gen puede tener varios registros | Sí | P1 |
| U4-11 | S13 | COMANDO-OPERACIÓN | `uniq` sin `sort` | Solo colapsa **adyacentes** | Sí | P1 |
| U4-12 | S18 | FORMATO | `^` y `$` | Anclan **línea**, no columnas | Sí | P1 |
| U4-13 | S19 | DISTINCIÓN | Seleccionar vs recuperar | Línea completa vs fragmento (`grep -o`) | Sí | P2 |
| U4-14 | S20 | DISTINCIÓN | Normalizar vs filtrar | Forma comparable vs decidir qué entra | Sí | P1 |
| U4-15 | S20 | CONCEPTO | Colisión | Dos originales distintos → misma clave normalizada | Sí | P1 |
| U4-16 | S21 | DISTINCIÓN | Coherencia interna vs validación | Acuerdo dentro del mismo paquete vs contraste con otra procedencia | Sí | P1 |
| U4-17 | S22 | COMANDO-OPERACIÓN | `$1` | Primer campo (con el FS declarado) | Sí | P1 |
| U4-18 | S22 | COMANDO-OPERACIÓN | `$NF` | Último campo (`NF` = nº de campos) | Sí | P1 |
| U4-19 | S22 | MÉTRICA | Longitud inclusiva 1-based | `end − start + 1` | Sí | P1 |
| U4-20 | S22 | ERROR-FRECUENTE | ¿Por qué `-F'\t'` importa en GFF? | Sin él, espacios en `source` desplazan `$3` | Sí | P1 |
| U4-21 | S22 | DISTINCIÓN | Conteo vs densidad | Cuántos hay vs cuántos por unidad de longitud | Sí | P1 |
| U4-22 | S23 | REPRODUCIBILIDAD | Control bloqueante | Si falla, **no continuar** | Sí | P1 |
| U4-23 | S10 | ES-EN | Pipe / tubería | Pipe — conecta stdout de un proceso al stdin del siguiente | Sí | P2 |

---

## Unidad 5 — Scripting conceptual y HPC (sin pipelines)

**Propósito:** diagnosticar fallos y diseñar fronteras sin memorizar scripts.

| ID | Sesión | Tipo | Frente | Reverso | ¿Acumulativa? | Prioridad |
| --- | --- | --- | --- | --- | --- | --- |
| U5-01 | S24 | CONCEPTO | ¿Para qué sirve `#!`? | Declara el intérprete (shebang) | Sí | P1 |
| U5-02 | S24 | ERROR-FRECUENTE | `Permission denied` con `./script.sh` | Falta permiso de ejecución | Sí | P1 |
| U5-03 | S24 | ERROR-FRECUENTE | `command not found` con el archivo a la vista | Falta `./` o cwd no está en `PATH` | Sí | P1 |
| U5-04 | S24 | DISTINCIÓN | Código de salida `0` | “Sin error” del sistema · **no** prueba que el análisis sea correcto | Sí | P1 |
| U5-05 | S24 | CONCEPTO | Fallo silencioso | Termina sin error aparente y no produce el resultado esperado | Sí | P1 |
| U5-06 | S25 | DISTINCIÓN | ¿Qué entra desde fuera? | Lo que cambia con otro organismo (rutas/datos) | Sí | P1 |
| U5-07 | S25 | DISTINCIÓN | ¿Qué se queda dentro? | Decisiones de método (p. ej. definición de gen) | Sí | P1 |
| U5-08 | S25 | DISTINCIÓN | `-f` vs `-s` | Existe · existe **y** tamaño > 0 | Sí | P1 |
| U5-09 | S26 | ERROR-FRECUENTE | `>` dentro de un `for` al mismo archivo | Trunca cada vuelta → solo queda el último | Sí | P1 |
| U5-10 | S29 | DISTINCIÓN | Login node vs compute node | Puerta de entrada · donde corre el trabajo | Sí | P1 |
| U5-11 | S29 | ERROR-FRECUENTE | `#SBATCH` en chaac (SGE) | Directivas Slurm; no intercambiables con `#$` de SGE | Sí | P1 |
| U5-12 | S24 | ES-EN | Shebang | Shebang — línea `#!` del intérprete | No | P2 |

---

## Unidad 6 — Métricas y distinciones evolutivas

**Propósito:** interpretar resultados sin saltar a conclusiones.

| ID | Sesión | Tipo | Frente | Reverso | ¿Acumulativa? | Prioridad |
| --- | --- | --- | --- | --- | --- | --- |
| U6-01 | S30 | DISTINCIÓN | Similitud vs homología | Se observa/mide · hipótesis de ancestro común | Sí | P1 |
| U6-02 | S30 | ERROR-FRECUENTE | «80 % de homología» | Incorrecto; di «80 % de identidad» | Sí | P1 |
| U6-03 | S32 | MÉTRICA | Identidad (`pident`) | % de columnas idénticas **en el tramo alineado** | Sí | P1 |
| U6-04 | S32 | MÉTRICA | Cobertura de consulta | Fracción de la query cubierta por el HSP | Sí | P1 |
| U6-05 | S32 | MÉTRICA | E-value | Nº esperado de aciertos ≥ tan buenos **por azar** | Sí | P1 |
| U6-06 | S32 | DISTINCIÓN | ¿E-value = P(homólogos)? | No | Sí | P1 |
| U6-07 | S32 | MÉTRICA | Bit score | Calidad normalizada del alineamiento | Sí | P1 |
| U6-08 | S31 | CONCEPTO | HSP | Par de segmentos de alta puntuación | Sí | P1 |
| U6-09 | S32 | ERROR-FRECUENTE | Identidad alta + cobertura baja | Dominio/fragmento — no “toda la proteína” | Sí | P1 |
| U6-10 | S33 | DISTINCIÓN | Ortólogos | Separados por **especiación** | Sí | P1 |
| U6-11 | S33 | DISTINCIÓN | Parálogos | Separados por **duplicación** | Sí | P1 |
| U6-12 | S33 | DISTINCIÓN | Homología ⇒ misma función? | No necesariamente | Sí | P1 |
| U6-13 | S33 | BIOLOGÍA | HBA1 vs HBA2 (100 % id.) | Misma proteína, genes distintos (paralogía reciente) | Sí | P1 |
| U6-14 | S30 | DISTINCIÓN | Resultado ≠ conclusión | La tabla/métrica no es la afirmación biológica | Sí | P1 |
| U6-15 | S31 | ES-EN | Query / Subject | Consulta / sujeto | Sí | P2 |
| U6-16 | S30 | ES-EN | Gap | Hueco en el alineamiento | No | P2 |
| U6-17 | S32 | IA-CRÍTICA | El «por lo tanto» peligroso | Pasar de % identidad a ortología/función sin peldaños | Sí | P1 |

---

## Mazos acumulativos (cadenas espaciadas)

| Cadena | Trayectoria | Tarjetas ancla |
| --- | --- | --- |
| A | U1 verificación≠validación → U3 checksum≠selección → U4 coherencia≠validación → U6 resultado≠conclusión | U1-03, U3-08, U4-16, U6-14 |
| B | U3 coordenada/feature → U4 longitud `$5-$4+1` → U5 conservar el cálculo en el script | U3-11, U4-19, U5-07 |
| C | U4 identidad de objeto/registro → U6 identidad de secuencia / ortología | U4-10, U6-01, U6-10 |
| D | U6 identidad (S30) → pident+cobertura (S32) → no basta para homología (S33) → ranking caso ciego (S34) | U6-03…U6-09 |

---

## Qué **no** convertir en flashcards

- Pipelines completos o scripts  
- Opciones raras de comandos  
- Respuestas de prácticas / resultados de un genoma concreto  
- Listas extensas de bases NCBI sin decisión  
- Conclusiones biológicas complejas que deben argumentarse  

**Pregunta filtro:** ¿recuperar esto rápidamente libera capacidad para un problema más complejo? Si no, descartar.
