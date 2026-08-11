Actúa como especialista en diseño instruccional para bioinformática, enseñanza inicial de Unix/Linux y aprendizaje basado en problemas.

Tu tarea es revisar y reescribir la lección:

- `u2-s3-shell-acceso-remoto.md`

Utiliza como fuentes de alineación obligatorias:

- `Plan-Clases-BioInfo-2026.xlsx`
- `Programa-IntroBioinfo-2026.docx`
- `u1-trabajo-reproducible-v3.md`
- `ejemplos/pacientes.md`
- `ejemplos/metadatos_pacientes.md`, si corresponde
- los archivos de imágenes de la Unidad 2 ubicados en `images/`

Entrega una versión completa y corregida de `u2-s3-shell-acceso-remoto.md`.

No modifiques el Plan, el Programa ni la Unidad 1. Si detectas una inconsistencia entre ellos, regístrala al final como nota para el docente.

# Objetivo de la revisión

Transforma la lección S3 en una experiencia progresiva y práctica de dos horas, basada en un problema frecuente del trabajo bioinformático.

Los comandos no deben aparecer como una lista de instrucciones aisladas. Cada comando debe introducirse porque resuelve una necesidad concreta dentro de un caso conductor.

La lección debe alternar:

```text
problema → explicación breve → comando o herramienta → práctica inmediata → observación del resultado
```

Conserva un reto integrador al final, pero no esperes hasta el final para que el estudiante ejecute por primera vez los comandos.

# Caso conductor obligatorio

Retoma el conjunto de datos sintético `pacientes.md` utilizado en la Unidad 1 y los metadatos que el estudiante elaboró.

Introduce la sesión mediante una situación como esta:

> En la Unidad 1 trabajaste con `pacientes.md`, un conjunto de datos sintético con tres registros, y elaboraste sus metadatos. También aprendiste que los datos originales deben conservarse sin modificaciones y acompañados de la información necesaria para interpretarlos. A partir de esta unidad, el trabajo computacional se realizará en el servidor del curso. Necesitas trasladar al servidor el archivo de datos y sus metadatos, comprobar que llegaron intactos y documentar el procedimiento para que pueda repetirse.

El estudiante deberá transferir:

```text
pacientes.md
pacientes-metadatos.md
```

Si `pacientes-metadatos.md` no existe como archivo preparado, explica que corresponde al archivo elaborado por cada estudiante en la Unidad 1.

Aclara que:

- `pacientes.md` contiene datos sintéticos y no información de personas reales;
- el estudiante ya conoce sus columnas y limitaciones;
- en S3 no analizará estadísticamente los datos;
- el problema de esta sesión es trasladar los archivos de forma segura, íntegra y reproducible;
- en S4 organizará los archivos dentro de la estructura del proyecto en el servidor.

# Alineación con el Plan de clases

Respeta estrictamente la progresión prevista:

## S3

Debe concentrarse en:

- por qué Unix y la CLI son relevantes para la bioinformática;
- terminal y shell;
- anatomía general de un comando;
- consulta de ayuda;
- cliente, servidor y protocolos;
- conexión mediante SSH;
- transferencia mediante SFTP o FileZilla;
- primera comprobación de integridad;
- documentación reproducible.

## S4

Reserva para S4:

- enseñanza detallada de rutas absolutas y relativas;
- navegación sistemática del sistema de archivos;
- creación de la estructura del proyecto;
- aplicación práctica de `scp` y `rsync`;
- operaciones con archivos y directorios.

En S3 se pueden mencionar `scp` y `rsync` en una tabla comparativa o como adelanto, pero no deben competir con SFTP/FileZilla como herramientas prácticas principales.

No sobrecargues S3 intentando enseñar simultáneamente SFTP, FileZilla, `scp` y `rsync`.

# Organización general de la lección

Conserva estas secciones iniciales:

1. Ficha del módulo.
2. Relación con la Unidad 1 y el proyecto integrador.
3. Resultados de aprendizaje.
4. Antes de la sesión.
5. Preflight.
6. Caso conductor.

Después organiza el contenido y las prácticas en bloques progresivos.

# Antes de la sesión

Resuelve la contradicción actual sobre las credenciales.

Si la dirección, el usuario y la contraseña se entregarán durante la clase, no pidas al estudiante conectarse antes de S3.

En ese caso, el primer intento previo debe consistir en:

1. Localizar `pacientes.md`.
2. Localizar o terminar `pacientes-metadatos.md`.
3. Instalar FileZilla, si se utilizará.
4. Confirmar que puede abrir la terminal o el cliente SSH.
5. Registrar una duda sobre la lectura.
6. Llevar los archivos preparados para la transferencia.

Solo solicita un intento de conexión previo si las credenciales y la huella oficial se entregaron con anticipación.

# Bloque conceptual inicial

Las secciones sobre Unix, GUI/CLI, filosofía Unix, terminal, shell, anatomía de comandos, ayuda y protocolos pueden presentarse antes de SSH.

Sin embargo, reconoce que antes de conectarse no todo el grupo dispone del mismo entorno Unix local. Por ello:

- no conviertas los comandos locales en una práctica evaluable;
- presenta inicialmente la anatomía y la ayuda de manera conceptual;
- realiza la práctica uniforme de comandos después de la primera conexión SSH;
- utiliza el servidor Linux del curso como entorno común.

Puede haber comprobaciones conceptuales breves antes de SSH, por ejemplo:

- identificar comando, opción y argumento;
- distinguir terminal de shell;
- elegir el protocolo adecuado para una situación;
- explicar por qué un comando de texto favorece la reproducibilidad.

# Primera práctica técnica: conexión SSH

Inmediatamente después de explicar SSH, inserta:

## Práctica 1 — Entrar al servidor, reconocer el entorno y salir

La práctica debe incluir:

```bash
ssh usuario@servidor
hostname
whoami
pwd
exit
```

Cada comando debe responder una pregunta:

| Pregunta | Comando |
|---|---|
| ¿En qué computadora estoy? | `hostname` |
| ¿Con qué cuenta estoy trabajando? | `whoami` |
| ¿En qué ubicación comenzó mi sesión? | `pwd` |
| ¿Cómo cierro correctamente la sesión remota? | `exit` |

Pide comparar el prompt antes y después de la conexión.

Explica claramente:

- cuándo el estudiante está en su computadora;
- cuándo está dentro del servidor;
- que la contraseña normalmente no muestra caracteres mientras se escribe;
- que `exit` cierra la sesión remota, no la aplicación de terminal;
- que `Ctrl-D` también puede cerrar una sesión, pero `exit` será la forma principal en esta lección.

# Repetición deliberada de SSH

Inserta una práctica específica de familiarización.

## Práctica 2 — Entrar, salir y volver a entrar

El estudiante debe realizar al menos tres ciclos:

```text
conectarse → hostname → whoami → pwd → exit
```

Organízalos así:

1. Primera ronda acompañada.
2. Segunda ronda consultando sus notas.
3. Tercera ronda sin seguir instrucciones paso a paso.

Al terminar debe explicar:

- cómo sabe que está en el servidor;
- cómo sabe con qué usuario trabaja;
- cómo sale;
- cómo vuelve a conectarse;
- qué cambia en el prompt.

La conexión repetida debe tratarse como una habilidad que necesita práctica, no como una acción que se realiza una sola vez.

# Práctica de comandos y ayuda dentro del servidor

Después de lograr la primera conexión, retoma y aplica la anatomía de comandos y la consulta de ayuda.

## Práctica 3 — Reconocer archivos y consultar ayuda en el servidor

Enmarca la práctica con este problema:

> Antes de transferir o procesar datos científicos necesitas reconocer dónde estás, qué archivos existen y cómo obtener ayuda cuando no recuerdas una opción.

Utiliza:

```bash
pwd
ls
ls -l
man ls
ls -lh
history
```

La práctica debe pedir:

1. Ejecutar `pwd`.
2. Ejecutar `ls`.
3. Comparar `ls` con `ls -l`.
4. Abrir `man ls`.
5. Localizar la opción `-h`.
6. Salir del manual con `q`.
7. Probar `ls -lh`.
8. Recuperar un comando mediante flecha ↑.
9. Revisar `history`.
10. Identificar comando, opciones y argumentos en un ejemplo ejecutado.

Relaciona los comandos con necesidades reales:

- `pwd`: evitar trabajar en la ubicación equivocada;
- `ls`: comprobar que un archivo existe;
- `ls -l` y `ls -lh`: revisar información básica y tamaño;
- `man`: resolver dudas sin depender del docente;
- Tab: evitar errores en nombres largos;
- flecha ↑ e `history`: recuperar y documentar procedimientos.

Aclara que `history` ayuda a reconstruir lo ejecutado, pero no sustituye una bitácora organizada.

# Uso de Tab y nombres de archivos

Relaciona el autocompletado con el trabajo bioinformático:

> Los archivos científicos suelen tener nombres largos, identificadores, versiones y sufijos. Un error de una letra puede hacer que un comando falle o utilice el archivo equivocado.

Incluye una práctica breve de Tab con un nombre conocido o preparado por el curso.

No dependas de que `pacientes.md` ya esté en el servidor antes de la transferencia. Si es necesario, utiliza otro nombre de archivo o directorio existente para demostrar Tab.

# Uso contextualizado de Ctrl-C

No presentes `Ctrl-C` como un atajo aislado.

Introduce el problema:

> Un análisis o una descarga puede tardar más de lo esperado, haberse iniciado con parámetros incorrectos o estar usando el archivo equivocado. Debes saber detener el proceso antes de causar más trabajo innecesario.

Puede usarse una simulación segura:

```bash
sleep 30
```

Aclara que `sleep` solo representa de manera controlada un proceso que todavía no termina; no es el objetivo bioinformático de la actividad.

El estudiante debe iniciarlo y detenerlo con `Ctrl-C`.

# Distinción local–remoto

Añade una explicación visual y recurrente de los contextos:

| Contexto | Cómo reconocerlo | Qué controla |
|---|---|---|
| `[LOCAL]` | `hostname` muestra la computadora del estudiante | Archivos locales |
| `[REMOTO]` | `hostname` muestra el servidor | Archivos y procesos remotos |
| `[SFTP]` | El prompt cambia a `sftp>` | Transferencia entre ambos lados |

Etiqueta todos los bloques de comandos relevantes como:

```text
[LOCAL] Ejecuta en tu computadora:
```

```text
[REMOTO] Ejecuta después de conectarte mediante SSH:
```

o:

```text
[SFTP] Ejecuta dentro de la sesión de transferencia:
```

No presentes comandos de transferencia sin aclarar desde qué contexto deben ejecutarse.

# Transferencia contextualizada

Después de explicar SFTP/FileZilla, inserta inmediatamente:

## Práctica 4 — Transferir los datos y sus metadatos

Problema:

> `pacientes.md` y `pacientes-metadatos.md` están en la computadora local, pero el trabajo posterior se realizará en el servidor. El dato debe viajar acompañado por la información que permite interpretarlo.

La práctica debe solicitar:

1. Identificar los dos archivos en la computadora local.
2. Conectarse por SFTP o FileZilla.
3. Distinguir el lado local del remoto.
4. Subir `pacientes.md`.
5. Subir `pacientes-metadatos.md`.
6. Cerrar la sesión de transferencia.
7. Volver a conectarse mediante SSH.
8. Confirmar con `ls -lh` que ambos archivos llegaron.
9. Salir correctamente.
10. Volver a conectarse y comprobar nuevamente que permanecen ahí.

Si se utiliza SFTP por terminal, enseña solamente el conjunto mínimo:

```text
lpwd
lls
pwd
ls
put
get
exit
```

Explica:

- `lpwd`, `lls` y `lcd`: lado local;
- `pwd`, `ls` y `cd`: lado remoto;
- `put`: subir;
- `get`: descargar;
- `exit`: cerrar SFTP.

No profundices en navegación ni rutas; esos temas se desarrollarán en S4.

Si se utiliza FileZilla, indica explícitamente:

- utilizar SFTP, no FTP plano;
- identificar panel local y panel remoto;
- no guardar ni mostrar credenciales en capturas;
- usar el puerto institucional confirmado, normalmente 22 si corresponde.

# Verificación de integridad

Después de explicar checksums, inserta inmediatamente:

## Práctica 5 — Comprobar que los archivos llegaron intactos

El problema debe formularse así:

> Ver el nombre del archivo en el servidor no demuestra que su contenido sea idéntico al original. Antes de analizar datos científicos debemos comprobar que la transferencia no los modificó.

En macOS local:

```bash
shasum -a 256 pacientes.md
shasum -a 256 pacientes-metadatos.md
```

En Linux local o en el servidor:

```bash
sha256sum pacientes.md
sha256sum pacientes-metadatos.md
```

Pide completar:

| Archivo | Checksum local | Checksum remoto | ¿Coinciden? |
|---|---|---|---|
| `pacientes.md` | | | |
| `pacientes-metadatos.md` | | | |

Aclara:

- ambos comandos utilizan SHA-256;
- debe compararse la cadena de la huella, no el nombre mostrado después;
- el tamaño o la presencia del archivo no bastan;
- si las huellas no coinciden, el archivo no debe utilizarse hasta repetir y verificar la transferencia.

Presenta esta actividad como primera aplicación de la integridad. Indica que la competencia se retomará con datos biológicos reales en la Unidad 3.

# Reto integrador final

Conserva una práctica final, pero cambia su función y nombre:

## Reto integrador S3 — Trasladar un dato científico de forma segura y reproducible

El estudiante debe realizar sin instrucciones paso a paso:

1. Conectarse mediante SSH.
2. Verificar que está en el servidor correcto.
3. Reconocer usuario y ubicación.
4. Salir.
5. Transferir `pacientes.md` y sus metadatos.
6. Volver a conectarse.
7. Confirmar que los archivos llegaron.
8. Calcular y comparar checksums.
9. Consultar ayuda si la necesita.
10. Cerrar correctamente las sesiones.
11. Documentar el procedimiento.

El reto final no debe ser la primera vez que el estudiante realiza estas acciones, sino la integración de habilidades previamente practicadas.

# Evidencia

La evidencia de S3 debe ser un registro reproducible que incluya:

- objetivo de la transferencia;
- sistema local utilizado: macOS, Linux o Windows con cliente correspondiente;
- host del servidor, sin contraseña;
- distinción entre acciones locales, remotas y SFTP;
- comandos exactos ejecutados;
- registro de al menos una conexión y salida correctas;
- una opción de `ls` encontrada mediante `man`;
- tabla de checksums;
- afirmación sustentada de que los archivos llegaron intactos;
- error encontrado y forma en que se diagnosticó, si aplica;
- ausencia de credenciales o información sensible.

La evidencia no debe limitarse a una captura de pantalla.

# Errores frecuentes

Amplía la tabla de diagnóstico con:

| Síntoma | Interpretación o acción |
|---|---|
| La contraseña parece no escribirse | SSH no muestra caracteres; es normal |
| `Could not resolve hostname` | Revisar nombre del servidor, red o VPN |
| `Connection refused` | Revisar servidor, puerto, red o disponibilidad |
| `Permission denied` | Revisar usuario, contraseña o método de autenticación |
| La huella no coincide | No aceptar; consultar al responsable |
| No sé si estoy local o remoto | Ejecutar `hostname`, `whoami` y `pwd` |
| El prompt muestra `sftp>` | Estás en una sesión SFTP, no en un shell |
| `No such file or directory` | Revisar contexto y nombre del archivo |
| El archivo se transfirió al lugar equivocado | Identificar nuevamente lado local y remoto |
| Los checksums no coinciden | No usar el archivo; repetir y verificar la transferencia |
| `ls --help` no funciona localmente en macOS | Utilizar `man ls`; `--help` depende de la implementación |

# Portabilidad

Aclara:

- el servidor del curso es el entorno Linux común;
- `man ls` es la forma preferida y más portable de consultar ayuda;
- `ls --help` funciona en GNU/Linux, pero no necesariamente en el `ls` estándar de macOS;
- los comandos ejecutados localmente pueden variar según el sistema;
- los comandos remotos deben probarse previamente en el servidor institucional.

# Seguridad

Conserva y refuerza:

- verificar la huella SSH;
- no aceptar cambios inesperados de identidad;
- no compartir contraseñas, llaves privadas ni tokens;
- no registrar credenciales en la bitácora;
- no incluir credenciales en capturas;
- no proporcionar información sensible a asistentes de IA;
- no ejecutar comandos sugeridos por IA sin entenderlos y verificarlos.

# Alcance de directorios y rutas

No enseñes todavía formalmente:

- rutas absolutas y relativas;
- `mkdir`, `cp`, `mv`, `rm`;
- estructura completa del sistema de archivos;
- construcción de `data/source/`, `data/processed/`, `src/`, `results/` y `doc/`.

Estos temas pertenecen a S4.

Para S3:

- utiliza el directorio inicial asignado al estudiante; o
- utiliza una carpeta preparada previamente por el docente.

Si resulta indispensable utilizar una ruta de destino, proporciónala como dato operativo sin desarrollar todavía su teoría.

Al final conecta con S4:

> En S3 trasladamos al servidor `pacientes.md` y sus metadatos. En S4 construiremos la estructura reproducible del proyecto y colocaremos el original intacto en `data/source/`.

# Distribución de las dos horas

Diseña la sesión aproximadamente así:

| Tiempo | Actividad |
|---:|---|
| 0–10 min | Recuperación: reproducibilidad, Unix y caso `pacientes.md` |
| 10–25 min | Primera conexión SSH acompañada |
| 25–40 min | Práctica de comandos y ayuda dentro del servidor |
| 40–55 min | Tres ciclos de conexión, reconocimiento y salida |
| 55–80 min | Transferencia guiada con SFTP o FileZilla |
| 80–95 min | Verificación mediante checksums |
| 95–115 min | Reto integrador individual o en parejas |
| 115–120 min | Semáforo de salida y registro de dudas |

Ajusta los tiempos si la conexión institucional requiere más acompañamiento, pero conserva la progresión práctica.

# Imágenes

Conserva e integra las imágenes existentes correspondientes a:

- GUI frente a CLI;
- filosofía Unix;
- anatomía de un comando;
- conexión SSH;
- FileZilla.

Cada imagen debe tener:

- texto alternativo informativo;
- pie de figura;
- referencia en el texto;
- una función didáctica clara.

No dejes notas editoriales como “figura sugerida”, “crear figura” o “nota de revisión docente” dentro de la versión destinada al estudiante, salvo que realmente requieran una decisión pendiente.

Verifica que la figura de filosofía Unix ya muestre `uniq -c` y no `wc -l`.

# Resultados, actividades y criterios

Actualiza la tabla final para que cada resultado tenga práctica y evidencia:

| Resultado | Actividad principal | Evidencia |
|---|---|---|
| Explica por qué Unix/CLI favorecen reproducibilidad | Caso conductor y discusión | Explicación breve vinculada con `pacientes.md` |
| Identifica partes de un comando y consulta ayuda | Práctica 3 | Comando analizado y opción localizada mediante `man` |
| Se conecta y reconoce el entorno remoto | Prácticas 1–2 | Registro de conexión, `hostname`, `whoami`, `pwd` y salida |
| Transfiere datos y metadatos | Práctica 4 | Ambos archivos presentes en el servidor |
| Verifica integridad | Práctica 5 | Checksums locales y remotos coincidentes |
| Documenta de manera reproducible | Reto integrador | Registro completo sin credenciales |

# Estilo pedagógico

- Escribe para estudiantes de primer semestre sin experiencia previa.
- Introduce primero el problema y después el comando.
- No utilices comandos sin explicar qué necesidad resuelven.
- Evita catálogos de opciones.
- Utiliza instrucciones cortas y resultados observables.
- Después de cada práctica incluye dos preguntas:
  - ¿Qué observaste?
  - ¿Cómo se relaciona con el problema de trasladar los datos?
- Diferencia claramente contenido esencial, consulta y ampliación.
- Conserva el tono claro, reflexivo y reproducible de la Unidad 1.
- Mantén continuidad con el proyecto integrador.
- No introduzcas FASTA, BLAST ni análisis biológicos que todavía no corresponden.
- No agregues más teoría si no ayuda a ejecutar o interpretar la práctica.
- Prioriza profundidad, repetición y confianza sobre cantidad de comandos.

# Entrega solicitada

Entrega:

1. La versión completa revisada de `u2-s3-shell-acceso-remoto.md`.
2. Una tabla breve de cambios respecto a la versión anterior.
3. Una lista de decisiones o datos que debe confirmar el docente:
   - host;
   - huella oficial;
   - puerto;
   - VPN;
   - directorio inicial;
   - disponibilidad de credenciales antes de la sesión.
4. Una comprobación final de que:
   - cada comando está relacionado con un problema;
   - las prácticas aparecen después del aprendizaje crítico correspondiente;
   - SSH se practica repetidamente;
   - local y remoto están claramente diferenciados;
   - SFTP/FileZilla son las herramientas prácticas principales en S3;
   - `scp` y `rsync` se reservan para S4;
   - `pacientes.md` y sus metadatos articulan toda la sesión;
   - los checksums forman parte de la práctica;
   - no se solicitan habilidades de sistema de archivos que pertenecen a S4;
   - la sesión cabe razonablemente en dos horas;
   - no hay credenciales ni datos sensibles;
   - no quedan instrucciones editoriales pendientes.


