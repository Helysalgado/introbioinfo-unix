Actúa como especialista en diseño instruccional para bioinformática, enseñanza de Unix/Linux y uso de clusters HPC.

Tu tarea es reorganizar y mejorar la Unidad 2 del curso “Introducción a la Bioinformática 2026”.

## Archivos de entrada

Analiza conjuntamente:

- `u2-entorno-unix-hpc.md`: material que debe reorganizarse.
- `Plan-Clases-BioInfo-2026.xlsx`: fuente principal para la distribución por sesiones.
- `Programa-IntroBioinfo-2026.docx`: fuente para competencias, resultados y evidencias.
- `u1-trabajo-reproducible-v3.md`: referencia de estilo pedagógico, aula invertida, prácticas, evidencias y autoevaluación.
- Directorio `images/`: contiene las figuras de la Unidad 2.

No modifiques los archivos de referencia. Genera nuevos documentos Markdown.

## Objetivo principal

Divide la Unidad 2 en una portada general y cuatro módulos correspondientes a las sesiones S3–S6 de dos horas:

1. `u2-entorno-unix-hpc.md`: portada e índice de la unidad.
2. `u2-s3-shell-acceso-remoto.md`: shell, ayuda, protocolos, SSH y transferencia.
3. `u2-s4-sistema-archivos.md`: sistema de archivos, rutas, navegación y operaciones.
4. `u2-s5-archivos-permisos-procesos.md`: archivos, edición, compresión, permisos y procesos.
5. `contenidos-2026/docente/u2-s6-cluster-hpc.md`: arquitectura HPC, SGE, recursos y ciclo de un trabajo.

Evita duplicar contenido entre la portada y los módulos. La portada debe contener únicamente la visión global, la ruta S3–S6, los resultados generales, las evidencias acumuladas y enlaces a los módulos.

## Diseño pedagógico común a los cuatro módulos

Cada módulo debe poder trabajarse como una sesión presencial de dos horas con aula invertida. Usa esta estructura:

1. Ficha del módulo.
2. Relación con la Unidad 1 y con el proyecto integrador.
3. Resultados de aprendizaje demostrables de la sesión.
4. Antes de la sesión:
   - lectura obligatoria;
   - preparación técnica;
   - primer intento;
   - producto que debe llevarse al taller;
   - tiempo estimado.
5. Contenido conceptual esencial.
6. Comandos mínimos, explicados mediante ejemplos.
7. Práctica guiada.
8. Errores frecuentes y cómo diagnosticarlos.
9. Evidencia de aprendizaje.
10. Criterios de logro o rúbrica breve.
11. Autoevaluación o semáforo de salida.
12. Preparación para la siguiente sesión.
13. Referencias específicas.

Distingue claramente tres momentos:

- Antes de clase: lectura y primer intento.
- Durante la sesión: práctica, comparación de estrategias y corrección.
- Después de clase: entrega o evidencia corregida.

No sobrecargues los módulos con comandos opcionales. Separa explícitamente:

- Esencial: se debe comprender y ejecutar.
- Consulta: se utiliza cuando sea necesario.
- Ampliación: no se evalúa en esta unidad.

## Correcciones globales obligatorias

### 1. Estructura de directorios

Utiliza de manera consistente la estructura adoptada en la Unidad 1:

```text
proyecto/
├── data/
│   ├── source/
│   └── processed/
├── src/
├── results/
└── doc/
```

No alternes entre `data_source/` y `data/source/`. Explica que los datos originales se conservan en `data/source/` sin modificarse.

Si el Programa o el Plan utilizan otra convención, señala la discrepancia en una nota de revisión para el docente, pero mantén una sola convención en los materiales estudiantiles.

### 2. Imágenes

Elimina todas las indicaciones editoriales del tipo “FIGURA SUGERIDA” o “Crear figura”.

Inserta las imágenes existentes mediante Markdown, con texto alternativo informativo y pie de figura. Usa las figuras donde realmente apoyen el aprendizaje:

- `figura-u2-gui-vs-cli.png`
- `figura-u2-filosofia-unix.png`
- `figura-u2-anatomia-comando.png`
- `figura-u2-conexion-ssh.png`
- `figura-u2-filezilla-esquema.png`
- `figura-u2-arbol-sistema-archivos.png`
- `figura-u2-rutas-absolutas-relativas.png`
- `figura-u2-permisos-unix.png`
- `figura-u2-procesos-primer-segundo-plano.png`
- `figura-u2-pc-servidor-cluster.png`
- `figura-u2-arquitectura-hpc.png`
- `figura-u2-ciclo-sge.png`

Antes de insertar una figura, verifica que coincida con el texto. Reporta como correcciones necesarias:

- La figura de filosofía Unix termina visualmente en `wc -l`, pero el comando ilustrado usa `uniq -c`.
- La figura del ciclo SGE no debe representar `qdel` como regreso a “Preparar”; debe llevar a un estado “Cancelado”.
- Un trabajo terminado normalmente desaparece de `qstat`; “fin” no debe mostrarse como un estado permanente de la cola.
- Las figuras deben utilizar la estructura `data/source/`.
- Aclara que la figura de FileZilla es un esquema didáctico y no una captura real.
- Distingue las rutas genéricas `/home/usuario` del espacio institucional `/export/space3/users/$USER`.

Si no puedes editar las figuras, inserta una nota de revisión para el docente y no reproduzcas información incorrecta en el texto.

### 3. Seguridad y reproducibilidad

Incluye recomendaciones explícitas:

- Verificar la huella del servidor SSH con la proporcionada por el docente; no aceptar una identidad desconocida a ciegas.
- No compartir contraseñas, llaves privadas, tokens, nombres de usuario reales ni información sensible con asistentes de IA.
- Probar comandos potencialmente riesgosos en archivos o directorios de prueba.
- Explicar que `rm` no tiene papelera y favorecer inicialmente `rm -i`.
- Documentar los comandos ejecutados y sus resultados.
- Verificar transferencias con checksums, no solo mediante el tamaño o la presencia del archivo.

### 4. Infraestructura institucional

Utiliza estos datos solamente como configuración del curso:

- Servidor: `chaac.lcg.unam.mx`
- Espacio de trabajo: `/export/space3/users/$USER`
- Planificador: SGE
- Comandos principales: `qsub`, `qstat`, `qdel` y `qhost`

No inventes nombres de colas, límites de memoria, walltime, ambientes de software o directivas no confirmadas.

Marca con `PENDIENTE DE VALIDACIÓN EN CHAAC` cualquier opción dependiente de la configuración institucional. Incluye una nota para verificar todos los comandos con una cuenta de estudiante antes de publicar.

## Requisitos específicos por módulo

### Módulo S3 — Shell, SSH y transferencia

Organiza el contenido en este orden:

1. Por qué Unix se usa en bioinformática.
2. GUI frente a CLI.
3. Filosofía Unix.
4. Diferencia entre terminal y shell.
5. Anatomía de un comando.
6. `man`, `--help`, Tab, historial y `Ctrl-C`.
7. Cliente, servidor y protocolos.
8. Conexión mediante SSH.
9. Transferencia mediante SFTP, FileZilla, `scp` y `rsync`.
10. Verificación de integridad.

No presentes `ssh`, `scp` o `rsync` antes de explicar qué es un comando.

Incluye un preflight:

- cuenta habilitada;
- dirección del servidor;
- cliente SSH disponible;
- FileZilla instalado si se utilizará;
- conexión a la red o VPN, si aplica;
- huella oficial del servidor;
- espacio de trabajo asignado.

Corrige la explicación de `rsync`. No afirmes que `rsync -av` siempre reanuda un archivo exactamente donde se interrumpió. Para conservar transferencias parciales utiliza, cuando corresponda:

```bash
rsync -avP origen/ usuario@servidor:/ruta/destino/
```

La práctica debe pedir:

1. Conectarse por SSH.
2. Crear una carpeta de prueba.
3. Transferir un archivo hacia el servidor.
4. Transferirlo de regreso.
5. Calcular y comparar checksums.
6. Documentar host, rutas, comandos y resultados sin registrar credenciales.

En Linux puede utilizarse `sha256sum`; en macOS, `shasum -a 256`. Explica la diferencia.

Evidencia esperada: registro reproducible de una transferencia cuya integridad haya sido comprobada.

### Módulo S4 — Sistema de archivos

Incluye:

- raíz `/`;
- directorio personal;
- directorio actual;
- rutas absolutas y relativas;
- `.`, `..` y `~`;
- `pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp` y `mv`;
- eliminación segura con `rm -i` y `rmdir`;
- `tree` o `ls -R`.

Explica claramente que una ruta relativa comienza en el directorio actual, no necesariamente en `~`.

La práctica debe construir la estructura canónica del proyecto:

```text
proyecto/
├── data/
│   ├── source/
│   └── processed/
├── src/
├── results/
└── doc/
```

Pide al estudiante:

1. Crear primero la estructura paso a paso.
2. Navegar usando rutas absolutas y relativas.
3. Verificarla con `tree` o `ls -R`.
4. Documentar los comandos.
5. Comparar después su solución con una propuesta de IA.
6. Identificar comandos eficientes y comandos riesgosos.

La actividad con IA debe llamarse “Actividad formativa de IA”, no “Tarea A”, para no confundirse con las tareas oficiales.

Evidencia esperada: estructura reproducible del proyecto y registro de comandos.

### Módulo S5 — Archivos, compresión, permisos y procesos

Incluye:

- `file`;
- `less`, `head`, `tail` y uso prudente de `cat`;
- edición básica con `nano`;
- `gzip`, `gunzip`, `zcat` y `tar`;
- lectura de permisos;
- diferencia entre permisos de archivos y directorios;
- `chmod` simbólico;
- forma numérica solamente después de comprender `r`, `w` y `x`;
- procesos, PID, primer y segundo plano;
- `ps`, `top`, `jobs`, `bg`, `fg`, `kill` y `nohup`;
- `screen` y `tmux` solo como ampliación.

No pidas aplicar permiso de ejecución a un archivo de texto sin propósito. La práctica debe crear un script mínimo:

```bash
#!/bin/bash
echo "Prueba de ejecución"
```

La práctica debe incluir:

1. Identificar y visualizar un archivo.
2. Editarlo.
3. Comprimirlo y restaurarlo.
4. Crear el script.
5. Probarlo antes y después de `chmod u+x`.
6. Ejecutar un proceso controlado, por ejemplo `sleep 120`.
7. Observarlo y practicar `jobs`, `bg`, `fg` o `kill`.
8. Documentar qué ocurrió.

Aclara que `nohup` no sustituye al scheduler. En un cluster, los análisis pesados o prolongados deben enviarse mediante SGE.

Evidencia esperada: archivo restaurado correctamente, script ejecutable y registro del control de un proceso.

### Módulo S6 — Cluster HPC y SGE

Incluye:

- diferencia entre computadora personal, servidor y cluster;
- nodo de acceso;
- nodos de cómputo;
- almacenamiento compartido;
- scheduler;
- trabajos en espera y ejecución;
- CPU, núcleos, memoria y tiempo;
- `qhost`, `qstat`, `qsub` y `qdel`;
- archivos de salida estándar y error;
- criterio para decidir cuándo utilizar el cluster.

Aclara que un cluster no convierte automáticamente un programa en paralelo. Un trabajo puede utilizar un nodo o varios recursos únicamente si el programa y la solicitud lo permiten.

Aclara que `.jdl` es una convención de nombres del curso, no un requisito general de SGE.

No utilices BLAST como primera práctica de HPC. BLAST se enseñará posteriormente en la Unidad 6. Usa un trabajo autocontenido que no dependa de bases de datos ni programas todavía desconocidos, por ejemplo:

```bash
#!/bin/bash
#$ -N prueba_u2
#$ -cwd
#$ -S /bin/bash
#$ -o salida-$JOB_NAME-$JOB_ID.out
#$ -e salida-$JOB_NAME-$JOB_ID.err

hostname
date
echo "Trabajo ejecutado mediante SGE"
sleep 30
date
```

Marca `source /etc/bashrc` y las directivas de recursos como dependientes de la configuración institucional si no están confirmadas.

Diseña dos ejercicios:

1. Un trabajo suficientemente largo para observarlo con `qstat` y cancelarlo con `qdel`.
2. Un trabajo corto que llegue a término y produzca `.out` y `.err`.

No utilices `watch -n 1 qstat` como recomendación principal para toda la clase. Prefiere un intervalo moderado, por ejemplo cinco segundos, o ejecuciones manuales de `qstat`.

Explica que:

- `qw` significa espera en cola;
- `r` significa ejecución;
- cuando termina, normalmente desaparece de `qstat`;
- desaparecer no garantiza éxito;
- deben revisarse `.out`, `.err` y, si está habilitado, `qacct -j JOBID`.

Incluye una sección breve sobre recursos con ejemplos institucionales únicamente si están confirmados. Si no lo están, deja una plantilla claramente marcada para que la complete el docente.

La actividad con IA debe revisar el mismo job sencillo que el estudiante creó manualmente. Debe comprobar que la IA no mezcle SGE con Slurm (`#$`/`qsub` frente a `#SBATCH`/`sbatch`). Reserva cualquier actividad de IA con BLAST para la Unidad 6.

Evidencia esperada: job enviado, monitoreado y finalizado o cancelado, con revisión documentada de `.out` y `.err`.

## Alineación y evaluación

Al final de cada módulo incluye una tabla:

| Resultado de aprendizaje | Actividad | Evidencia | Criterio de logro |
|---|---|---|---|

La portada general debe incluir una tabla acumulativa que muestre cómo S3–S6 cubren la competencia B del programa.

Asegura que cada resultado declarado tenga:

- una acción observable;
- una práctica correspondiente;
- una evidencia concreta;
- un criterio para determinar si se logró.

No declares que el estudiante “gestiona procesos”, “verifica integridad” o “cancela trabajos” si la práctica solamente le pide observarlos.

## Estilo

- Escribe en español claro para estudiantes de primer semestre sin experiencia previa.
- Define los términos técnicos la primera vez.
- Favorece ejemplos bioinformáticos sencillos, pero no introduzcas herramientas que se enseñarán después.
- Conserva el tono pedagógico y visual de la Unidad 1.
- Evita párrafos excesivamente largos.
- No conviertas el material en un catálogo de comandos.
- Explica para qué sirve cada comando y qué resultado debe observarse.
- Incluye salidas esperadas solo cuando ayuden a diagnosticar.
- Distingue claramente instrucciones para macOS, Linux local y el servidor remoto.
- Mantén los comandos destructivos al mínimo.
- No inventes resultados de una ejecución real.

## Entrega solicitada

Entrega:

1. Los cinco documentos Markdown completos.
2. Una tabla de cambios respecto al documento original.
3. Una lista de inconsistencias que requieren decisión docente.
4. Una lista de elementos marcados como `PENDIENTE DE VALIDACIÓN EN CHAAC`.
5. Una comprobación final de:
   - enlaces internos;
   - rutas de imágenes;
   - coherencia de términos;
   - estructura de directorios;
   - correspondencia entre resultados, prácticas y evidencias;
   - ausencia de instrucciones editoriales pendientes.

No modifiques el Plan, el Programa ni la Unidad 1. Si detectas que requieren una actualización posterior, regístrala como recomendación separada.

