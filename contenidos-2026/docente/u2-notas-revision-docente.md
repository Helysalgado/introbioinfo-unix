# Unidad 2 — Notas de revisión para el docente

## Decisión curricular posterior — cierre en S5 y reubicación de HPC

Se acordó que la **Unidad 2 termina con S5 — Archivos, permisos y procesos**. El contenido operativo
de cluster y SGE se conserva, pero se reubica después de que el alumnado haya practicado
procesamiento de datos, tuberías y scripting, cerca de una aplicación bioinformática como BLAST.

Cambios aplicados a los materiales Markdown:

- la portada de U2 presenta únicamente la ruta S3–S5 e incorpora un cierre verificable;
- S5 termina con un puente explícito hacia U3 — Datos y bases de datos biológicas;
- `u2-s6-cluster-hpc.md` queda marcado como borrador reubicado y no publicable como parte de U2;
- el README separa el borrador de HPC del índice vigente de la Unidad 2.

**Pendiente de actualización en los documentos rectores:** el Plan de clases 2026 todavía asigna
S6 a HPC y el Programa 2026 todavía incluye la introducción operativa al cluster dentro de la Unidad
2. La competencia de HPC no se elimina del curso; debe reubicarse en ambos documentos cuando se
defina la sesión posterior concreta. La transición inmediata después de S5 mantiene el contenido
previsto para la Unidad 3: formatos biológicos, bases públicas, descarga y verificación de
integridad.

> **Qué es esto.** Documento **interno** (no es material del estudiante). Reúne los entregables de
> control de la reorganización de la Unidad 2: la tabla de cambios respecto al documento original, las
> inconsistencias que requieren decisión docente, la lista de elementos marcados `PENDIENTE DE
> VALIDACIÓN EN CHAAC` y la comprobación final. Documentos generados:
>
> - `u2-entorno-unix-hpc.md` — portada e índice de la unidad.
> - `u2-s3-shell-acceso-remoto.md` — shell, SSH y transferencia.
> - `u2-s4-sistema-archivos.md` — sistema de archivos.
> - `u2-s5-archivos-permisos-procesos.md` — archivos, permisos y procesos.
> - `u2-s6-cluster-hpc.md` — cluster HPC y SGE.

## 1. Tabla de cambios respecto al documento original

El original era un único archivo `u2-entorno-unix-hpc.md` (642 líneas) con las secciones 1–8. La
reorganización lo divide en una portada + cuatro módulos S3–S6 y aplica las correcciones del encargo.

| # | Cambio | Dónde estaba (original) | Dónde queda ahora | Motivo |
| --- | --- | --- | --- | --- |
| 1 | División en portada + 4 módulos de 2 h | Documento único | Portada + S3/S4/S5/S6 | Cada sesión es trabajable como aula invertida independiente |
| 2 | Reordenamiento S3 (por qué Unix → GUI/CLI → filosofía → terminal/shell → anatomía → ayuda → cliente/servidor → SSH → transferencia → integridad) | Secciones 1, 3, 2 (mezcladas) | `u2-s3` §1–§10 | El original presentaba SSH/transferencia (sec. 2) antes de explicar qué es un comando (sec. 3) |
| 3 | Se retira "shell y terminal" del bloque tardío y se coloca antes de la anatomía del comando | Sec. 3 (después de SSH) | `u2-s3` §4–§5 | No presentar `ssh`/`scp`/`rsync` antes de saber qué es un comando |
| 4 | Corrección de `rsync`: ya no se afirma que `rsync -av` reanuda solo; se añade `rsync -avP` | Sec. 2.5 y TIP | `u2-s3` §9 | El original decía que `-av` "retoma donde quedó"; para transferencias parciales se requiere `-P` |
| 5 | Verificación de integridad ampliada con `sha256sum` (Linux) vs. `shasum -a 256` (macOS) | Sec. 2.5 (solo mención) | `u2-s3` §10 | El encargo pide checksums reales y distinguir SO |
| 6 | Preflight de conexión añadido | No existía | `u2-s3` (antes de §1) | Requisito del encargo |
| 7 | Recomendaciones de seguridad (huella SSH, no compartir credenciales con IA, probar en archivos de prueba, `rm -i`, documentar) | Dispersas/ausentes | S3, S4, S5 (callouts) | Correcciones globales de seguridad |
| 8 | Estructura de directorios unificada a `data/source` + `data/processed` | Sec. 4 y Práctica 3 usaban `data_source/` | S4 §7 y portada | Consistencia con la Unidad 1; se elimina `data_source/` |
| 9 | Práctica de S4 pide construir la estructura canónica paso a paso + verificación con `tree` | Práctica 3 (parcial) | `u2-s4` Práctica S4 | Requisito del encargo |
| 10 | "Tarea A" (IA) renombrada **Actividad formativa de IA** | Sec. 8, "Tarea A" | S4 y S6 | Evitar confusión con las tareas oficiales del plan |
| 11 | S5: script mínimo con propósito para `chmod u+x`; prueba antes/después | Práctica 4 (permiso sin propósito) | `u2-s5` Práctica S5 | No aplicar permiso de ejecución a un texto sin sentido |
| 12 | S5: se aclara permisos de archivo vs. directorio y `nohup` no sustituye al scheduler | Sec. 5.5–5.6 (implícito) | `u2-s5` §5–§6 | Requisitos del encargo |
| 13 | `screen`/`tmux` marcados como **ampliación** (no evaluados) | Sec. 5.6 | `u2-s5` §6 (nota) | Separar esencial/consulta/ampliación |
| 14 | S6: job de ejemplo cambiado de **BLAST** a un job **autocontenido** (`hostname/date/echo/sleep`) | Sec. 6.3 (`blastn.jdl`) | `u2-s6` §4 (`prueba_u2.jdl`) | BLAST se enseña en U6; no depender de bases/programas desconocidos |
| 15 | `.jdl` aclarado como **convención del curso**, no requisito de SGE | Sec. 6.3 (implícito requisito) | `u2-s6` §4 (nota) | Requisito del encargo |
| 16 | `watch -n 1 qstat` reemplazado por intervalo moderado (`watch -n 5`) o consulta manual | Sec. 6.4 (`watch -n 1`) | `u2-s6` §5 (nota) | No sobrecargar el planificador |
| 17 | Estados de SGE explicados: `qw`/`r`; terminado desaparece de `qstat`; desaparecer ≠ éxito; revisar `.out`/`.err`/`qacct` | Sec. 6.4 (parcial) | `u2-s6` §5 | Requisito del encargo |
| 18 | Dos ejercicios de S6 (uno que se cancela, uno que termina) | Práctica 5 (uno solo) | `u2-s6` Práctica S6 | Requisito del encargo |
| 19 | Actividad de IA en S6 revisa el mismo job manual y contrasta SGE vs. Slurm | Tarea B (BLAST con IA) | `u2-s6` Actividad formativa de IA | BLAST con IA se reserva a U6; detectar alucinación SGE/Slurm |
| 20 | `source /etc/bashrc` y directivas de recursos marcados `PENDIENTE DE VALIDACIÓN EN CHAAC` | Sec. 6.3 (incluido sin marca) | `u2-s6` §4 y §6 | No dar por confirmada configuración institucional |
| 21 | Se aclara que un cluster no paraleliza automáticamente | Ausente | `u2-s6` §1 | Requisito del encargo |
| 22 | Eliminadas todas las indicaciones "FIGURA SUGERIDA — … Crear figura" | 7 bloques editoriales | Sustituidos por imágenes reales con alt + pie | Las figuras ya existen en `images/` |
| 23 | Tablas de alineación RA–actividad–evidencia–criterio por módulo + tabla acumulativa de competencia B en portada | Ausente | Cada módulo + portada | Requisito de alineación y evaluación |
| 24 | `/home/usuario` (genérico) distinguido de `/export/space3/users/$USER` (institucional) | Mezclado | S3 §5, S4 §1 (notas) | Requisito del encargo |
| 25 | Rúbricas/criterios de logro y semáforo de salida por módulo | Solo checklist final | Cada módulo | Estándar de la plantilla de unidad |

## 2. Inconsistencias que requieren decisión docente

1. **Numeración de tareas.** El plan operativo asigna a la Unidad 2 la **Tarea 3** (estructura de
   directorios, S4). El original hablaba de "Tarea A/Tarea B" para las actividades de IA; se
   renombraron **Actividad formativa de IA** para no chocar con la numeración oficial. **Decisión
   pendiente:** confirmar si las evidencias de S3 (transferencia), S5 (archivos/permisos/procesos) y
   S6 (HPC) deben recibir número de tarea propio o quedar como "evidencias" sin numerar. El Programa
   lista para la competencia B una "Tarea de transferencia de archivos" y un "Ejercicio guiado de
   envío de un trabajo al cluster" como evidencias, pero el plan por sesiones solo numera la Tarea 3.

2. **`data_source/` vs. `data/source/`.** El documento **original de U2** usaba `data_source/` en la
   Práctica 3, mientras la Unidad 1 y la plantilla usan `data/source/`. Se unificó todo a
   `data/source/`. **Recomendación:** revisar que ninguna versión previa del plan/programa siga
   citando `data_source/`; si aparece, corregirla en una actualización posterior (no se modificó aquí
   el plan ni el programa).

3. **Servidor del examen práctico.** El Examen práctico 1 (S16) evalúa "entorno Unix, datos y
   filtros". La Unidad 2 asume `chaac.lcg.unam.mx` como servidor/cluster único. **Decisión pendiente:**
   confirmar si el examen se hará sobre `chaac` o sobre otra máquina, para alinear las rutas
   `/export/space3/users/$USER` que aparecen en los módulos.

4. **Lectura base.** La ficha de la unidad cita Buffalo Cap. 3 y Shotts (2019). El plan menciona
   "L3-shell (diapositivas 1–final)" y un "artículo de procesos" / "codigofacilito: unix-process".
   **Decisión pendiente:** indicar si esos recursos (diapositivas L3, artículo de procesos) deben
   enlazarse explícitamente en los módulos S3–S5; ahora se citan como lectura base genérica.

5. **Huella oficial del servidor.** El preflight (S3) pide la "huella oficial del servidor". **Acción
   docente:** proveer la huella SHA-256 real de `chaac` a los estudiantes por un canal seguro antes de
   la S3.

## 3. Elementos marcados `PENDIENTE DE VALIDACIÓN EN CHAAC`

Todos están en `u2-s6-cluster-hpc.md`. Deben verificarse con una **cuenta de estudiante** antes de
publicar:

1. **§4 — `source /etc/bashrc`.** Si el cluster requiere cargar el entorno al inicio del *job script*.
2. **§4 — Directivas de recursos** (`-q` cola, `-pe` núcleos, memoria, tiempo): no incluidas como
   confirmadas.
3. **§6 — Plantilla de recursos** (cola(s), directiva de núcleos, de memoria, de walltime, y si se
   requiere `source /etc/bashrc`): tabla en blanco para completar.
4. **Verificación general de comandos SGE** (`qsub`, `qstat`, `qdel`, `qhost`, `qacct -j`,
   `qstat -g c`) contra la configuración real de `chaac`.
5. **Ruta de trabajo** `/export/space3/users/$USER`: confirmar que es la vigente para las cuentas de
   estudiante.

> **Recomendación general:** ejecutar los dos ejercicios de la Práctica S6 con una cuenta de estudiante
> real y ajustar el ejemplo `prueba_u2.jdl` si el cluster exige alguna directiva adicional.

## 4. Notas de revisión sobre las figuras (no se editaron las imágenes)

Las figuras se insertaron desde `contenidos-2026/images/` con texto alternativo y pie. Se detectaron
elementos a corregir en las imágenes (pendiente de edición gráfica por el docente):

1. **`figura-u2-filosofia-unix`.** El último bloque está rotulado `wc -l`, pero la tubería de ejemplo
   termina en `uniq -c`. Alinear el rótulo del último bloque con el comando ilustrado (contar por
   categoría con `uniq -c`). El texto de S3 §3 ya evita afirmar que el flujo termina en `wc -l`.
2. **`figura-u2-ciclo-sge`.** Verificar que (a) `qdel` conduzca a un estado **"Cancelado"** y no de
   regreso a "Preparar", y (b) el final no se represente como un estado permanente "fin" en la cola
   (un trabajo terminado **desaparece** de `qstat`). El texto de S6 §5 describe el comportamiento
   correcto.
3. **`figura-u2-filezilla-esquema`.** Es un **esquema didáctico**, no una captura real. El pie ya lo
   aclara; si se desea una captura auténtica, tomarla desde una conexión al servidor del curso.
4. **Estructura de directorios en las figuras.** Donde una figura muestre carpetas del proyecto, debe
   usar `data/source/` (no `data_source/`). Revisar `figura-u2-arbol-sistema-archivos` si aplica.
5. **Rutas genéricas vs. institucionales.** Al reutilizar figuras con `/home/usuario`, tener presente
   que el espacio institucional real es `/export/space3/users/$USER` (aclarado en el texto).

## 5. Comprobación final

| Punto verificado | Estado | Nota |
| --- | --- | --- |
| **Enlaces internos** entre portada y módulos | OK | Portada enlaza a S3–S6; cada módulo enlaza al siguiente y a la portada |
| **Rutas de imágenes** (12 figuras) existen en `images/` | OK | Todas las `.png` referenciadas existen (verificado) |
| **Coherencia de términos** (shell, terminal, checksum, nodo, cola) | OK | Definidos la primera vez y en glosarios |
| **Estructura de directorios** `data/source` / `data/processed` | OK | Uniforme en portada, S4 y ejemplos; sin `data_source/` |
| **Correspondencia RA–práctica–evidencia–criterio** | OK | Tabla de alineación en cada módulo + acumulativa en portada |
| **Sin instrucciones editoriales** ("FIGURA SUGERIDA", "Crear figura") | OK | Eliminadas; sustituidas por figuras reales |
| **RA no sobredeclarados** | OK | S6 pide "enviar/monitorear/cancelar y revisar", no "gestionar" sin evidencia |
| **Sin BLAST como primera práctica de HPC** | OK | Job autocontenido; BLAST remitido a U6 |
| **Marcas `PENDIENTE DE VALIDACIÓN EN CHAAC`** presentes | OK | 3 marcas en S6 §4 y §6 |
| **Sin mención a Quarto en material del alumno** | OK | No aparece |
| **No se modificaron** Plan, Programa ni Unidad 1 | OK | Solo se generaron los 5 documentos + estas notas |

## 6. Revisión de S4 (versión v2) — `u2-s4-sistema-archivos-v2.md`

Se produjo una versión corregida `u2-s4-sistema-archivos-v2.md` (no se borró la v1). Cambios y
redistribuciones respecto de la v1 y del plan:

| # | Cambio | Motivo |
| --- | --- | --- |
| S4-1 | **Hilo acumulativo S1–S4 explícito.** La práctica reutiliza los productos previos: crea la estructura diseñada en S2 y coloca en ella `pacientes.md`, `pacientes-metadatos.md`, `protocolo.md` (transferidos en S3) y `bitacora-ia.md`. Ya no hay directorios vacíos ni archivos artificiales. | Encargo: práctica auténtica y acumulativa |
| S4-2 | **Problema conductor** añadido: organizar en el servidor los archivos que en S3 quedaron en ubicación provisional y comprobar que los datos no cambiaron. | Encargo |
| S4-3 | **`bitacora-ia.md` señalado como no transferido en S3**; se transfiere en S4 con `scp`/`rsync`. | S3 solo transfirió 3 archivos; no presuponer disponibilidad |
| S4-4 | **`scp`/`rsync` aplicados** (transferir `bitacora-ia.md` desde `[LOCAL]`), como anuncia S3. Clasificados como "aplicación". | Plan S4: "Transferencia scp/rsync (aplicada)" |
| S4-5 | **`nano` introducido** en el mínimo para completar `README.md` y actualizar `protocolo.md`; **`vi` solo como consulta** (cómo salir). | Plan S4: "Editores nano y vi"; título del plan incluye "y edición" |
| S4-6 | **Microprácticas intercaladas** (navegación; copiar/mover/renombrar; borrado seguro) tras cada concepto crítico, en vez de acumular la práctica al final. | Encargo: progresión didáctica |
| S4-7 | **Seguridad reforzada:** se presentan `cp -i`/`mv -i`/`rm -i` antes de las variantes sin confirmación; se advierte que `cp`/`mv` pueden sobrescribir; borrado solo en `prueba-s4/`; se retira la sugerencia de `rm -ri` como rutina; `rm -r` fuera de la práctica obligatoria. | Encargo: seguridad |
| S4-8 | **Verificación de integridad con checksum** de `pacientes.md` (comparación con el valor de S3) integrada a la Tarea 3. | Encargo: verificación observable |
| S4-9 | **Cuatro principios distinguidos** (reproducibilidad/verificación/validación/robustez), sin usarlos como sinónimos; robustez = llegar al mismo directorio por ruta absoluta y relativa. | Encargo |
| S4-10 | **Actividad formativa de IA** revisa la **misma** estructura creada a mano (no un proyecto nuevo), con anonimización `[SERVIDOR]`/`[USUARIO]`/`[RUTA]`, comparación comando por comando, validación con `man` y en `prueba-s4/`, y bitácora completa. | Encargo |
| S4-11 | **Distribución de 120 min** y tiempos separados (lectura, lectura obligatoria adicional, consulta, primer intento, taller, corrección, actividad IA). | Encargo |
| S4-12 | **Rúbricas separadas** (primer intento, participación/corrección, Tarea 3, actividad IA) en tres niveles + **Anexo A** (RA–actividad–evidencia–criterio–momento–nivel) y **Anexo B** (alineación transversal). | Encargo/plantilla |
| S4-13 | **Lecturas alineadas al plan:** se identifica L3 (diapos 39–60), se indica que el módulo **sustituye** esas diapositivas como lectura autocontenida; Buffalo = base, Shotts = consulta, con tiempos. **Ruta de Buffalo corregida** a `../introBioInfo/referencias/bioinformatics-data-skills.pdf` (enlace Markdown). Referencias con DOI/URL para Noble y Shotts. | Encargo |
| S4-14 | **Figuras corregidas** (SVG + PNG): `figura-u2-arbol-sistema-archivos` ahora muestra `/`, `/export/space3/users/$USER`, `proyecto/`, `README.md`, `data/source/`, `data/processed/`, `src/`, `results/`, `doc/`, **sin `data_source/`**; `figura-u2-rutas-absolutas-relativas` muestra el mismo archivo por ruta absoluta (`/export/space3/users/$USER/proyecto/data/source/pacientes.md`) y relativa desde el directorio actual (`proyecto/`), **sin afirmar que la relativa empieza en `~`**. | Encargo: figuras |
| S4-15 | **Patrón "plantilla reutilizable" en la Tarea 3** (a petición docente): la práctica ahora crea `template/` (estructura + `doc/protocolo.md` de arranque), la **clona** con `cp -r template proyecto` y **mueve** (`mv -i`) `pacientes.md` y `pacientes-metadatos.md` a `proyecto/data/source/`. Se añade `cp -r` como comando esencial (concepto de plantilla, §8; ensayo en Micropráctica 2; criterio de rúbrica; RA5). El `protocolo.md` real de S3 se trae con `cp -i` sobre el de arranque (demuestra confirmación de sobrescritura); `bitacora-ia.md` se transfiere con `scp`/`rsync`. La integridad de `pacientes.md` se comprueba **tras mover** (mover no altera el contenido; el checksum lo confirma). | Petición docente + refuerza reproducibilidad (plantilla estandarizada, Noble 2009) |

### Redistribución respecto del plan (S4)

El plan lista para S4: navegación, operaciones con archivos y directorios, **editores nano y vi**, y
**transferencia scp/rsync (aplicada)**. La v2 mantiene como **núcleo** la navegación, las rutas y la
construcción/organización del proyecto (Tarea 3); incorpora una **aplicación breve y auténtica** de
`scp`/`rsync` (transferir `bitacora-ia.md`); introduce `nano` solo lo necesario para `README.md` y
`protocolo.md`; y deja `vi` como consulta. No se alteró el plan operativo para ocultar esta
priorización.

### Correcciones editoriales en documentos rectores (fuera de S4)

- `prompts-ia/guia-generacion-unidad.md`: referencia `u1-trabajo-reproducible-v2.md` → `v3`;
  "verdad de referencia" → "línea base de comparación, no una verdad absoluta"; añadida nota de alcance
  (unidad completa vs. módulo; U2 = portada + S3–S6).
- `contenidos-2026/plantilla-unidad.md`: referencia `v2` → `v3`; añadida la misma nota de alcance.
- No se modificaron el Programa `.docx`, el Plan `.xlsx` ni los productos de S1–S3.

### Decisiones docentes pendientes (S4)

1. **Ubicación provisional de los archivos de S3.** La v2 asume que en S3 los archivos quedaron en el
   *home* del estudiante (`~`). Confirmar cuál es la carpeta de destino provisional real indicada en
   clase, para ajustar las rutas de `cp -i` de la Tarea 3.
2. **Disponibilidad de `tree` en `chaac`.** El módulo ofrece `ls -R` como alternativa siempre
   disponible. Confirmar si `tree` está instalado para las cuentas de estudiante.
3. **`scp`/`rsync` desde el equipo del estudiante.** Confirmar que la política del servidor permite
   `scp`/`rsync` entrantes desde las máquinas locales del grupo (puerto/registro), o si debe usarse
   SFTP como en S3. Depende de `PENDIENTE DE VALIDACIÓN EN CHAAC` (ruta `/export/space3/users/$USER`).
4. **Checksum registrado en S3.** La verificación de integridad de S4 requiere que el estudiante haya
   guardado el checksum de `pacientes.md` en `protocolo.md` durante S3. Confirmar que esa evidencia se
   exige en la entrega de S3.
5. **Numeración de tareas.** Se conserva **Tarea 3** para S4 (sin cambios); sigue vigente la decisión
   pendiente §2.1 sobre numerar o no las evidencias de S3/S5/S6.
