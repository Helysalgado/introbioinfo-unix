# Unidad 2. El entorno Unix/Linux y el cómputo científico

> **NOTA:** Este documento es **lectura previa**. Léelo antes de las sesiones S3–S6. En clase
> practicaremos los comandos en vivo sobre el servidor; esta lectura te da los conceptos para
> aprovechar ese tiempo. Al final de cada tema hay una **práctica**.

## Ficha de la unidad

| Elemento | Descripción |
| --- | --- |
| **Sesiones** | S3–S6 |
| **Competencia** | B (Dominio del entorno Unix y del cómputo científico) |
| **Propósito** | Que el estudiante opere con soltura el entorno de trabajo del bioinformático, desde su propia máquina hasta un cluster institucional. |
| **Ajustes integrados** | Introducción al uso de clusters de cómputo (HPC) **[Nuevo]** |
| **Lectura base** | Buffalo (2015), Cap. 3 ("Remedial Unix Shell"); Shotts (2019), *The Linux Command Line* |

### Resultados de aprendizaje (demostrables)

Al terminar la unidad, el estudiante es capaz de:

1. **Explicar** por qué se usa Unix en bioinformática (filosofía Unix, modularidad).
2. **Distinguir** los protocolos de intercambio de datos (HTTP, FTP, SSH) y **conectarse** a un servidor remoto por SSH.
3. **Transferir** archivos entre su computadora y el servidor (sftp, scp, rsync), verificando su integridad.
4. **Navegar** el sistema de archivos y **operar** con archivos y directorios usando rutas absolutas y relativas.
5. **Visualizar y editar** archivos en el servidor, **comprimir/descomprimir** y **gestionar permisos y procesos**.
6. **Describir** la arquitectura de un cluster de cómputo y **enviar, monitorear y cancelar** un trabajo sencillo en su sistema de colas. **[Nuevo]**

---

## 1. ¿Por qué usamos Unix en bioinformática?

**Unix** es una familia de sistemas operativos creada en los años 70. Hoy, casi toda la
bioinformática se ejecuta sobre sistemas **tipo Unix** (Linux y macOS lo son). No es una moda: hay
razones de fondo (Buffalo, 2015, Cap. 3, "Why Do We Use Unix in Bioinformatics? Modularity and the
Unix Philosophy").

### 1.1 GUI vs. CLI

- **GUI** (*Graphical User Interface*): interfaz gráfica, se opera con el ratón haciendo clic en
  ventanas y botones. Es intuitiva pero difícil de **automatizar** y de **documentar** (¿cómo
  escribes "hice clic aquí" de forma reproducible?).
- **CLI** (*Command Line Interface*): interfaz de línea de comandos, se opera **escribiendo
  instrucciones de texto**. Tiene una curva de aprendizaje mayor, pero cada acción es un comando que
  se puede **guardar, repetir, automatizar y compartir**.

> **IMPORTANTE:** En bioinformática preferimos la CLI porque un comando es **texto reproducible**:
> puedes pegarlo en tu protocolo, volver a ejecutarlo y obtener el mismo resultado. Esto enlaza
> directamente con la reproducibilidad de la Unidad 1.

> **FIGURA SUGERIDA — GUI vs. CLI.** Comparación lado a lado: a la izquierda, una ventana con
> botones (GUI); a la derecha, una terminal con un comando escrito (CLI). **Crear** figura propia
> del curso.

### 1.2 La filosofía Unix

La **filosofía Unix** consiste en tener **muchos programas pequeños**, cada uno de los cuales
**hace una sola cosa y la hace bien**, y que se pueden **combinar** para resolver tareas complejas.
En lugar de un único programa gigante, encadenas herramientas simples (lo veremos con las *tuberías*
en la Unidad 4).

Esta modularidad explica por qué Unix es tan potente para datos biológicos: puedes construir flujos
de análisis combinando herramientas estándar, sin reescribir todo desde cero (Buffalo, 2015, Cap. 3).

> **¿SABÍAS QUE?:** Unix nació alrededor de 1969–1970 en los Laboratorios Bell (AT&T), de la mano de
> Ken Thompson y Dennis Ritchie. Más de medio siglo después, sus ideas siguen vigentes: macOS está
> construido sobre una base tipo Unix y Linux —un sistema tipo Unix libre— domina los servidores
> científicos del mundo (Ritchie & Thompson, 1974).

---

## 2. Cómo viajan los datos: protocolos de internet y acceso remoto

### 2.1 Cliente y servidor

Cuando tu computadora se conecta a internet para pedir información (una página, un archivo), actúa
como **cliente** que hace una petición a un **servidor** que responde. Un **servidor** es
simplemente una computadora, normalmente potente y siempre encendida, que ofrece servicios o datos a
otras. Para que cliente y servidor se entiendan usan **protocolos**: reglas comunes de comunicación.

### 2.2 Los protocolos que usaremos

- **HTTP** (*HyperText Transfer Protocol*): el protocolo de la web; transfiere páginas y, a menudo,
  archivos de descarga.
- **FTP** (*File Transfer Protocol*): protocolo dedicado a **transferir archivos** entre
  computadoras. Muchas bases de datos biológicas ofrecen descargas por FTP.
- **SSH** (*Secure SHell*): protocolo para **conectarse de forma segura** (cifrada) a una
  computadora remota y trabajar en ella como si estuvieras sentado frente a ella.

> **NOTA:** "Seguro" en SSH significa que la comunicación viaja **cifrada**: aunque alguien
> intercepte los datos, no puede leerlos.

### 2.3 ¿Por qué conectarnos a un servidor?

En bioinformática trabajamos en servidores (y clusters) en lugar de en nuestra laptop porque los
análisis requieren **mucha memoria, muchos procesadores y mucho almacenamiento**, y porque los
**datos ya viven ahí**. Tu computadora personal sirve para conectarte; el trabajo pesado ocurre en
el servidor.

### 2.4 Conexión por SSH

Para conectarte a un servidor por SSH se usa el comando `ssh` con tu usuario y la dirección del
servidor. El siguiente bloque muestra la sintaxis:

```bash
ssh usuario@servidor.institucion.mx
# ejemplo (el nombre del servidor lo indica quien imparte el curso):
ssh usuario@chaac.lcg.unam.mx
```

La primera vez te pedirá confirmar la identidad del servidor y luego tu contraseña. Una vez dentro,
todo lo que escribas se ejecuta **en el servidor**.

> **¿SABÍAS QUE?:** Los servidores del laboratorio suelen llevar nombres temáticos. `chaac`, el
> cluster que usaremos, toma su nombre de **Cháak**, la deidad maya de la lluvia. Ponerles nombre
> facilita recordar a cuál te conectas.

> **FIGURA SUGERIDA — Conexión cliente–servidor por SSH.** Diagrama: laptop (cliente) → conexión
> SSH cifrada → servidor remoto. Etiquetar "tu computadora", "internet (SSH cifrado)", "servidor".
> **Crear** figura propia.

### 2.5 Transferencia de archivos

Para mover archivos entre tu computadora y el servidor hay varias herramientas. El siguiente bloque
muestra las más comunes:

```bash
# sftp: transferencia interactiva y segura (sobre SSH)
sftp usuario@servidor        # abre una sesión; luego: put archivo / get archivo

# scp: copia puntual de un archivo (sobre SSH)
scp archivo.fasta usuario@servidor:/ruta/destino/      # de tu PC al servidor
scp usuario@servidor:/ruta/archivo.fasta ./            # del servidor a tu PC

# rsync: sincroniza, eficiente para muchos archivos o reanudar transferencias
rsync -av carpeta_local/ usuario@servidor:/ruta/destino/
```

- **sftp**: sesión interactiva para subir (`put`) y bajar (`get`) archivos.
- **scp**: copia directa de un archivo o carpeta, en una sola orden.
- **rsync**: sincroniza carpetas copiando **solo lo que cambió**; ideal para conjuntos grandes o
  para reanudar una transferencia interrumpida.

También existe **FileZilla**, un programa con **interfaz gráfica** que hace transferencia por
SFTP/FTP arrastrando archivos entre dos paneles: el de tu computadora (izquierda) y el del servidor
(derecha).

> **FIGURA SUGERIDA — Interfaz de FileZilla.** Captura de la ventana de FileZilla con sus dos
> paneles etiquetados ("sitio local" y "sitio remoto") y la barra de conexión arriba. **Crear**
> captura propia desde una conexión al servidor del curso. Atribuir la herramienta (FileZilla).

> **TIP:** Para conjuntos de muchos archivos o transferencias que se pueden interrumpir, prefiere
> `rsync -av`: si la copia se corta, al volver a ejecutarla **retoma donde quedó** en lugar de
> empezar de cero.

> **IMPORTANTE:** Tras transferir datos, **verifica su integridad** (que el archivo llegó completo y
> sin corromperse). Es una buena práctica que retomaremos en la Unidad 3 con las sumas de
> verificación (*checksums*).

### Práctica 1 — Primera conexión y transferencia (S3)

1. Instala **FileZilla** si aún no lo tienes.
2. Conéctate al servidor del curso por **SSH** con `ssh usuario@servidor`.
3. Dentro del servidor, crea tu carpeta de trabajo del curso.
4. Desde tu computadora, **sube** un archivo de prueba al servidor con `scp` o con FileZilla.
5. Registra en tu protocolo/README el servidor usado y los comandos exactos que ejecutaste.

---

## 3. El shell y la terminal

### 3.1 ¿Qué es el shell?

El **shell** es un programa **intérprete de comandos**: lee lo que escribes, se lo pide al sistema
operativo y te devuelve el resultado. Es la capa con la que "conversas" con Unix. Existen varios
shells (**bash**, **tcsh**, **csh**, **zsh**); el más común es **bash**.

La **terminal** es la ventana donde se ejecuta el shell y escribes los comandos.

> **NOTA:** En macOS y Linux la terminal viene incluida. En Windows puedes usar el subsistema WSL,
> Git Bash o conectarte directamente por SSH a un servidor Unix.

### 3.2 Sintaxis de un comando

Un comando de Unix tiene tres partes. El siguiente bloque muestra su estructura:

```bash
comando  -opciones  argumentos
# ejemplo:
ls  -l  /home/usuario
```

- **comando**: la herramienta que quieres usar (`ls`, `cd`, `cp`…).
- **opciones** (o *flags*): modifican el comportamiento; suelen empezar con `-` (p. ej. `-l`).
- **argumentos**: sobre qué actúa el comando (un archivo, una carpeta…).

> **FIGURA SUGERIDA — Anatomía de un comando.** Diagrama de `ls -l /home/usuario` con tres llaves o
> colores que señalen "comando", "opciones" y "argumentos". **Crear** figura propia del curso.

> **TIP:** Dos atajos que te harán mucho más rápido en la terminal: la tecla **Tab** autocompleta
> nombres de comandos y archivos (evita errores de tipeo), y la **flecha ↑** recupera comandos que
> ya ejecutaste (el comando `history` los lista todos). `Ctrl-C` cancela lo que se esté ejecutando.

### 3.3 Buscar ayuda

Nunca hay que memorizar todo. El siguiente bloque muestra cómo consultar la ayuda de un comando:

```bash
man ls        # manual completo del comando (se sale con q)
ls --help     # ayuda breve de opciones
```

> **COMENTARIO:** Aprender a leer `man` y `--help` es una habilidad en sí misma: te hace autónomo.
> El GPT "Profesor de Unix" también puede explicarte un comando, pero **valida siempre** su
> respuesta con `man` (recuerda la Unidad 1).

### Práctica 2 — Explorar comandos (S3)

1. Conéctate al servidor.
2. Ejecuta `man ls` y localiza qué hacen las opciones `-l`, `-a` y `-h`.
3. Ejecuta `ls -lah` y describe en tu bitácora qué información muestra cada columna.

---

## 4. El sistema de archivos de Unix

### 4.1 Estructura en árbol

En Unix, los archivos y directorios (carpetas) se organizan en una **jerarquía en forma de árbol**
que empieza en la **raíz**, representada por `/`. De la raíz cuelgan directorios, que a su vez
contienen otros directorios y archivos.

> **FIGURA SUGERIDA — Árbol del sistema de archivos.** Diagrama de árbol desde `/` con ramas típicas
> (`/home`, `/home/usuario`, subcarpetas del proyecto). **Crear** figura propia, o generarla con un
> `tree` real y capturarla.

Conceptos clave:

- **Directorio raíz `/`**: el origen de todo el árbol.
- **Directorio home (`~`)**: tu carpeta personal, donde tienes permisos para trabajar.
- **Ruta (path)**: la dirección de un archivo dentro del árbol.

### 4.2 Rutas absolutas y relativas

- **Ruta absoluta**: parte desde la raíz `/`. Siempre apunta al mismo lugar. Ej.: `/home/usuario/proyecto/data`.
- **Ruta relativa**: parte desde donde estás parado ahora (tu directorio actual). Ej.: `proyecto/data`.

Símbolos útiles en las rutas:

- `.` : el directorio actual.
- `..` : el directorio padre (uno hacia arriba).
- `~` : tu directorio home.

### 4.3 Comandos de navegación y operación

El siguiente bloque reúne los comandos básicos para moverte y operar con archivos y directorios:

```bash
pwd                 # muestra dónde estás (ruta actual)
ls                  # lista el contenido del directorio
cd carpeta          # entra a "carpeta"
cd ..               # sube al directorio padre
cd ~                # va a tu home

mkdir nueva         # crea el directorio "nueva"
touch archivo.txt   # crea un archivo vacío
cp origen destino   # copia
mv origen destino   # mueve o renombra
rm archivo          # borra un archivo   (¡sin papelera!)
rmdir carpeta       # borra un directorio vacío
```

> **ADVERTENCIA:** En Unix **no hay papelera**: `rm` borra de forma permanente e inmediata. Verifica
> siempre qué vas a borrar antes de ejecutar `rm`, y ten mucho cuidado con `rm -r` (borra
> directorios y todo su contenido).

> **TIP:** Usa `rm -i` para que te **pida confirmación** antes de borrar cada archivo; es una red de
> seguridad mientras te acostumbras. Otros atajos útiles: `ls -lh` muestra los tamaños en formato
> legible (KB, MB, GB) y `cd -` te regresa al directorio anterior.

### 4.4 Errores comunes

- Escribir mal una ruta ("No such file or directory"): revisa con `pwd` y `ls` dónde estás.
- Confundir mover con renombrar: `mv` hace ambas según el destino.
- Crear varios directorios y que no queden anidados como esperabas (revisa las rutas de cada uno).

### Práctica 3 — Estructura de directorios (Tarea 3, S4)

1. En tu home del servidor, crea la estructura de directorios de tu proyecto (usa la de la Unidad 1:
   `data_source/`, `results/`, `src/`, `doc/`).
2. Practica moverte con rutas **absolutas** y **relativas** entre esas carpetas.
3. Genera e incluye en la entrega la estructura con `tree` (o `ls -R` si `tree` no está disponible).
4. Documenta en tu protocolo los comandos usados.

---

## 5. Archivos: tipos, visualización, edición, compresión y permisos

### 5.1 Tipos de archivos y cómo identificarlos

No todos los archivos son iguales: hay texto plano, binarios, comprimidos, etc. El comando `file`
identifica el tipo de un archivo:

```bash
file genoma.fasta     # p. ej. "ASCII text"
file datos.gz         # p. ej. "gzip compressed data"
```

### 5.2 Visualizar el contenido

El siguiente bloque muestra las formas más comunes de ver un archivo **sin abrir un editor**:

```bash
cat archivo.txt     # muestra todo el contenido
less archivo.txt    # visor paginado (avanzar con espacio, salir con q)
head archivo.txt    # primeras 10 líneas
tail archivo.txt    # últimas 10 líneas
head -n 3 archivo   # primeras 3 líneas
```

> **COMENTARIO:** Para archivos biológicos grandes (un genoma completo) **no uses `cat`**: llenaría
> la pantalla. Usa `less`, `head` o `tail` para asomarte a su contenido.

### 5.3 Editar archivos en el servidor

Para crear o modificar archivos de texto directamente en el servidor se usan editores de terminal:

- **nano**: sencillo, muestra los atajos en pantalla; ideal para empezar.
- **vi / vim**: muy potente pero con curva de aprendizaje; conviene conocerlo porque está en todos
  los sistemas Unix.

```bash
nano notas.md       # abrir/crear con nano  (guardar: Ctrl+O, salir: Ctrl+X)
vi notas.md         # abrir/crear con vi
```

### 5.4 Compresión de archivos

Los datos biológicos son grandes; comprimirlos ahorra espacio y acelera las transferencias. El
siguiente bloque muestra las herramientas básicas:

```bash
gzip archivo.fasta      # comprime -> archivo.fasta.gz
gunzip archivo.fasta.gz # descomprime
zcat archivo.fasta.gz   # muestra el contenido SIN descomprimir
tar -czf datos.tar.gz carpeta/   # empaqueta y comprime una carpeta
tar -xzf datos.tar.gz            # extrae
```

### 5.5 Permisos

En Unix cada archivo tiene **permisos** que definen quién puede hacer qué. Hay tres tipos de permiso
—**r** (leer), **w** (escribir), **x** (ejecutar)— para tres categorías de usuario: el **dueño**
(*user*), el **grupo** (*group*) y **los demás** (*others*).

Al ejecutar `ls -l` ves los permisos al inicio de cada línea:

```text
-rwxr-xr--  1 usuario grupo  1024 ago 20 10:00 script.sh
 │└┬┘└┬┘└┬┘
 │ │  │  └── others: r--  (solo leer)
 │ │  └───── group:  r-x  (leer y ejecutar)
 │ └──────── user:   rwx  (leer, escribir, ejecutar)
 └────────── tipo:   -=archivo, d=directorio
```

El comando `chmod` cambia los permisos:

```bash
chmod u+x script.sh    # da permiso de ejecución al dueño (forma simbólica)
chmod 754 script.sh    # forma numérica: user=7(rwx) group=5(r-x) others=4(r--)
```

> **NOTA:** La forma numérica suma valores: r=4, w=2, x=1. Así, `7 = 4+2+1 = rwx`, `5 = 4+1 = r-x`.

> **FIGURA SUGERIDA — Desglose de permisos en `ls -l`.** Diagrama que descomponga una cadena como
> `-rwxr-xr--` en sus bloques (tipo · dueño · grupo · otros) y muestre la equivalencia numérica
> (754). **Crear** figura propia del curso (puede basarse en el esquema en texto de arriba).

### 5.6 Procesos

Cada programa en ejecución es un **proceso**, identificado por un número (**PID**). Saber verlos y
controlarlos es esencial cuando corres análisis que tardan. El siguiente bloque muestra cómo
**observarlos**:

```bash
ps -f -u $USER  # tus procesos, con detalle (usuario, PID, comando…)
top             # procesos en tiempo real (salir con q)
htop            # como top, más visual e interactivo (salir con q)
watch -n 3 "ps -f -u $USER"   # repite un comando cada 3 s (salir con Ctrl-c)
```

Un proceso puede correr en **primer plano** (ocupa tu terminal hasta que termina) o en **segundo
plano** (sigue corriendo y te devuelve la terminal). El siguiente bloque muestra cómo manejarlo:

```bash
comando &            # ejecuta "comando" en segundo plano
# (si ya lo lanzaste en primer plano: Ctrl-z para pausarlo y luego 'bg' para mandarlo al fondo)
nohup comando &      # segundo plano que NO se interrumpe si cierras la sesión
kill PID             # termina el proceso con identificador PID
```

> **NOTA:** `nohup ... &` es útil para análisis largos: el proceso continúa aunque cierres la
> conexión. Su salida de pantalla queda en el archivo `nohup.out`.

Para **mantener una sesión de trabajo abierta** aunque te desconectes (y reconectarte después),
existen `screen` y `tmux`. Son muy útiles al trabajar en servidores; se introducen aquí solo para
que sepas que existen y se profundizan en cursos posteriores.

> **COMENTARIO:** Entender procesos es la antesala del cómputo en cluster: cuando envías un trabajo
> pesado, en realidad lanzas un proceso que corre por su cuenta en otra máquina.

### Práctica 4 — Archivos, permisos y procesos (S5)

1. Copia al servidor un archivo de texto y averigua su tipo con `file`.
2. Visualízalo con `head`, `tail` y `less`.
3. Crea un archivo con `nano`, guárdalo y dale permiso de ejecución con `chmod`.
4. Ejecuta `ps` y `top` y describe en tu bitácora qué observas.

---

## 6. Introducción a los clusters de cómputo (HPC)  [Nuevo]

> **NOTA:** Esta sección es una **introducción a nivel usuario**. El objetivo **no** es que
> administres un cluster, sino que comprendas su lógica y sepas **conectarte, enviar un trabajo y
> monitorearlo**. Muchos cursos posteriores y proyectos de investigación lo requieren.

### 6.1 Computadora personal vs. servidor vs. cluster

- **Computadora personal:** una máquina para tu trabajo diario. Recursos limitados.
- **Servidor:** una computadora potente, compartida y siempre encendida, a la que te conectas por
  SSH (secciones anteriores).
- **Cluster de cómputo de alto desempeño (HPC):** un **conjunto de muchos servidores** (llamados
  *nodos*) conectados entre sí y coordinados para trabajar como un solo sistema muy potente.

> **FIGURA SUGERIDA — PC vs. servidor vs. cluster.** Tres iconos en escala creciente (una laptop; un
> servidor; un conjunto de servidores = cluster) con una frase de capacidad bajo cada uno. **Crear**
> figura propia.

### 6.2 Arquitectura de un cluster

Un cluster tiene tres piezas que debes conocer como usuario:

- **Nodo de acceso (*login node*):** la máquina a la que te conectas por SSH. Sirve para **preparar**
  tu trabajo (editar archivos, organizar datos), **no** para correr análisis pesados.
- **Nodos de cómputo:** las máquinas donde realmente se ejecutan los análisis. No te conectas a
  ellos directamente: les envías el trabajo a través del sistema de colas.
- **Almacenamiento compartido:** un sistema de archivos que **todos los nodos ven por igual**, así
  tus datos están disponibles sin importar en qué nodo corra el trabajo. En el cluster del curso, tu
  espacio de trabajo está bajo `/export/space3/users/$USER`.

> **IMPORTANTE:** No ejecutes análisis pesados en el **nodo de acceso**: es un espacio compartido por
> todos y lo saturarías. Los trabajos pesados **siempre** se envían a los nodos de cómputo mediante
> el sistema de colas.

> **FIGURA SUGERIDA — Arquitectura de un cluster HPC.** Diagrama: usuario → (SSH) → nodo de acceso →
> (sistema de colas) → varios nodos de cómputo; todos conectados a un almacenamiento compartido.
> **Crear** figura propia del curso (puedo generarla con el estilo del esquema integrador).

### 6.3 El sistema de colas (*scheduler*)

Como muchos usuarios comparten el cluster, no todos pueden correr al mismo tiempo. Un **sistema de
colas** (o *planificador* / *scheduler*) recibe los trabajos de todos, los **ordena en una cola** y
los asigna a los nodos de cómputo conforme se liberan recursos. Tú no eliges el nodo: describes qué
necesita tu trabajo y el sistema decide cuándo y dónde ejecutarlo.

El cluster del curso usa el planificador **SGE** (*Sun/Son of Grid Engine*). Para pedirle trabajo
escribes un pequeño **script de trabajo** (*job script*), un archivo de texto —con extensión
`.jdl`— que contiene los recursos que necesitas y los comandos a ejecutar. El siguiente bloque es un
ejemplo mínimo (`blastn.jdl`):

```bash
#!/bin/bash
#$ -N mi_blast                        # nombre del trabajo
#$ -cwd                               # ejecutar en el directorio actual
#$ -S /bin/bash                       # shell a utilizar
#$ -o salida-$JOB_NAME-$JOB_ID.out    # archivo de salida estándar
#$ -e salida-$JOB_NAME-$JOB_ID.err    # archivo de errores
source /etc/bashrc

# comando bioinformático que se ejecutará en el nodo de cómputo:
blastn -db ntRed -query sequences.fa
```

> **NOTA:** Las líneas que empiezan con `#$` son **directivas** para SGE (nombre del trabajo,
> directorio, archivos de salida y error, etc.). Opciones más avanzadas —elegir cola (`-q`), pedir
> varios núcleos (`-pe smp N` con `$NSLOTS`) o lanzar *arrayjobs* (`-t 1-99`)— se usan en cursos
> posteriores como Bioinformática y Estadística II. Consulta siempre la documentación del cluster.

### 6.4 Enviar, monitorear y cancelar trabajos

El siguiente bloque muestra los comandos esenciales para un usuario de SGE:

```bash
qhost               # ver los nodos del cluster y su estado
qstat -g c          # ver las colas disponibles y su ocupación
qsub blastn.jdl     # ENVIAR el trabajo a la cola (devuelve un número de job)
qstat               # MONITOREAR: ver el estado de tus trabajos
watch -n 1 qstat    # monitorear continuamente (salir con Ctrl-c)
qdel 12345          # CANCELAR el trabajo con identificador 12345
```

- **`qhost`** y **`qstat -g c`**: exploran el cluster (nodos y colas) antes de enviar.
- **`qsub`**: envía tu *job script* (`.jdl`) a la cola.
- **`qstat`**: muestra tus trabajos y su estado (`qw` = esperando en cola, `r` = corriendo). Con
  `watch -n 1 qstat` lo monitoreas en vivo.
- **`qdel`**: cancela un trabajo enviado, usando su número (JOBID).

> **NOTA:** Para una sesión **interactiva** en un nodo de cómputo (probar un comando sin encolar un
> script) existe `qrsh`. Úsala con moderación: ocupa un nodo mientras la mantienes abierta.

### 6.5 Recursos: CPU, memoria y tiempo

Al enviar un trabajo declaras cuántos recursos necesita:

- **CPU (procesadores / *cores*):** cuántos núcleos usará. Más núcleos pueden acelerar programas que
  trabajan en paralelo.
- **Memoria RAM:** cuánta memoria necesita el análisis. Si pides poca y el programa necesita más,
  fallará.
- **Tiempo de ejecución (*walltime*):** tiempo máximo estimado. Si lo superas, el sistema puede
  detener el trabajo.

> **COMENTARIO:** Estimar bien los recursos es parte del oficio: pedir de más desperdicia recursos
> compartidos y puede retrasar tu turno en la cola; pedir de menos hace que el trabajo falle.

### 6.6 ¿Cuándo se necesita un cluster? Ejemplos en bioinformática

- **Ensamblado de genomas:** requiere mucha memoria RAM.
- **Análisis de RNA-seq:** procesa muchas muestras y archivos grandes.
- **Búsquedas masivas con BLAST:** comparar miles de secuencias contra bases enormes.

Estos ejemplos reaparecen en la Unidad 6 (BLAST) y en cursos posteriores. **[Integración]**

### Práctica 5 — Enviar un trabajo al cluster (S6)

1. Conéctate por SSH al **nodo de acceso** del cluster del curso (`ssh usuario@chaac.lcg.unam.mx`) y
   ubícate en tu espacio de trabajo `/export/space3/users/$USER`.
2. Explora el cluster con `qhost` y `qstat -g c`.
3. Escribe un *job script* sencillo `mi_trabajo.jdl` (usa el ejemplo de 6.3 como base; el comando
   puede ser algo simple como `echo` o un conteo sobre un archivo).
4. Envíalo con `qsub mi_trabajo.jdl` y anota el número de trabajo.
5. Monitorea su estado con `qstat` (o `watch -n 1 qstat`) hasta que termine.
6. Revisa los archivos de salida (`.out` y `.err`) y documenta en tu bitácora todos los comandos
   usados. Si necesitas cancelarlo, practica `qdel JOBID`.

> **ADVERTENCIA:** El nombre del servidor, las rutas y las colas pueden cambiar. Confirma con quien
> imparte el curso y consulta las notas de uso del cluster antes de enviar trabajos.

---

## 7. Cierre de la unidad

### Checklist de habilidades (¿lo puedo demostrar?)

- [ ] Explico por qué se usa Unix en bioinformática y qué es la filosofía Unix.
- [ ] Me conecto a un servidor por SSH y transfiero archivos con scp/sftp/rsync o FileZilla.
- [ ] Navego el sistema de archivos con rutas absolutas y relativas y opero con archivos y directorios.
- [ ] Visualizo y edito archivos, los comprimo/descomprimo y gestiono permisos y procesos.
- [ ] Describo la arquitectura de un cluster y envío, monitoreo y cancelo un trabajo con qsub/qstat/qdel.

### Tareas a entregar

- **Tarea 3 — Estructura de directorios** (Práctica 3): estructura del proyecto en el servidor, con
  la salida de `tree` y los comandos documentados.
- **Evidencia de HPC** (Práctica 5): captura o registro del envío y monitoreo de un trabajo en el
  cluster.

### Lecturas / consulta previa para la Unidad 3

- Buffalo (2015), Cap. 6 ("Bioinformatics Data"): obtención de datos y su descarga reproducible.
- Explorar el sitio de NCBI (<https://www.ncbi.nlm.nih.gov>).

---

## 8. Cierre con IA: clásico vs. asistido

> **Regla — primero a mano, luego con IA.** Ya ejecutaste estos comandos paso a paso; ahora repites
> algunas tareas con un asistente para **comparar** el enfoque clásico con el asistido. Lo que hiciste
> en la terminal (verificado con `man` y probado en pequeño) es tu **verdad de referencia**: la IA no
> lo sustituye, lo **contrastas**.

**Herramientas.** Puedes usar **ChatGPT** o **Claude** en el chat, o los GPTs del curso (Profesor de
Unix / guía de razonamiento). Declara y registra todo en tu `bitacora-ia.md`, y formula tus prompts
con la estructura vista en la Unidad 1.

> **IMPORTANTE:** Nunca ejecutes en el servidor un comando que la IA te dé **sin entenderlo**. Léelo,
> compáralo con lo que hiciste a mano, revísalo con `man` y pruébalo primero en una carpeta o archivo
> de prueba.

### Tarea A — Crear la estructura de directorios, ahora con IA

Recordatorio (lo que hiciste a mano): en la Práctica 3 creaste la estructura del proyecto navegando y
usando comandos de archivos.

1. Prompt sugerido:
   > "En Linux, dame los comandos para crear, dentro de mi carpeta actual, esta estructura:
   > `data/source`, `data/processed`, `src`, `results`, `doc`. Explícame cada comando y cómo verifico
   > que se creó correctamente."
2. **Compara** con lo que hiciste a mano: ¿usó los mismos comandos?, ¿propuso algo más eficiente
   (por ejemplo, crear varios directorios a la vez)?, ¿algún comando es riesgoso? Verifícalo con `man`.
3. Registra el prompt, la respuesta y tu validación en la bitácora.

### Tarea B — Un *job script* de SGE, ahora con IA

Recordatorio (lo que hiciste a mano): en la Práctica 5 escribiste un *job script* `.jdl` y lo enviaste
con `qsub`.

1. Prompt sugerido:
   > "Escríbeme un *job script* para el planificador **SGE (Grid Engine)** que ejecute
   > `blastn -db ntRed -query sequences.fa`, con nombre de trabajo, ejecución en el directorio actual
   > y archivos de salida y error. Explícame cada directiva `#$`."
2. **Compara** con el script que escribiste. **Atención a las alucinaciones:** la IA a veces mezcla
   planificadores y te da sintaxis de **Slurm** (`#SBATCH`, `sbatch`) en lugar de **SGE** (`#$`,
   `qsub`). ¿Detectaste directivas que **no** corresponden a nuestro cluster? Contrasta con las notas
   de uso del cluster (`chaac`).
3. Registra qué corregiste y por qué en la bitácora.

### Reflexión (para el taller)

- ¿La IA mezcló planificadores u opciones que no existen en nuestro cluster? Ese es un caso real de
  **alucinación técnica** que solo pudiste detectar porque lo hiciste antes a mano.
- ¿Qué validaste con `man` y con la documentación del cluster?
- ¿Qué tareas de esta unidad **sí** conviene apoyar con IA y cuáles es mejor dominar por tu cuenta?

---

## Referencias

- Buffalo, V. (2015). *Bioinformatics Data Skills*. O'Reilly Media. — Cap. 3 ("Remedial Unix Shell":
  filosofía Unix, shell, pipes) y Cap. 6 (datos bioinformáticos). Disponible en
  `referencias/bioinformatics-data-skills.pdf`.
- Shotts, W. E. (2019). *The Linux Command Line: A Complete Introduction* (2ª ed.). No Starch Press.
- Ritchie, D. M., & Thompson, K. (1974). The UNIX Time-Sharing System. *Communications of the ACM*,
  17(7), 365–375. doi:10.1145/361011.361061 (origen y filosofía de Unix).
- Documentación oficial de SSH/OpenSSH. <https://www.openssh.com/manual.html>
- FileZilla — cliente de transferencia. <https://filezilla-project.org/>
- Notas de uso de servidores y cluster del CCG (SGE, cluster `chaac`), material del curso
  Bioinformática y Estadística II (`lcg-be2-2026-2-servidores`). Consultar con quien imparte el curso.
- Documentación de Grid Engine (SGE): comandos `qsub`, `qstat`, `qdel`, `qhost`.
- Herramientas de monitoreo y sesión: `htop` (<https://htop.dev/>), GNU Screen
  (<https://www.gnu.org/software/screen/>) y tmux (<https://github.com/tmux/tmux/wiki>).
- Tange, O. (2011). GNU Parallel — The Command-Line Power Tool. *;login:*, 36(1), 42–47. (ejecución
  concurrente; se profundiza en cursos posteriores).
