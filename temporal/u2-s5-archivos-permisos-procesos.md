# Unidad 2 · Módulo S5 — Archivos, compresión, permisos y procesos

> **NOTA — Lectura previa (aula invertida).** Este documento se lee **antes de la sesión S5**. En el
> taller haremos codificación en vivo con repetición del estudiante. Trae tu **primer intento** y tus
> dudas. Al final hay una **práctica** con tres momentos.

Tercer módulo de la [Unidad 2](u2-entorno-unix-hpc.md). Ya organizas tu proyecto en el servidor (S4);
ahora trabajarás **con los archivos**: identificarlos, verlos, editarlos, comprimirlos, y aprenderás a
leer y cambiar **permisos** y a **controlar procesos**. Estas dos últimas habilidades son la antesala
directa del trabajo en cluster (S6).

## Ficha del módulo

| Elemento | Descripción |
| --- | --- |
| **Sesión** | S5 (2 h) |
| **Tema** | Tipos de archivos, visualización, edición, compresión, permisos y procesos |
| **Competencia** | B — Dominio del entorno Unix y del cómputo científico |
| **Resultado (plan)** | Gestiona tipos de archivo, compresión, permisos y procesos |
| **Lectura base** | Buffalo (2015), Cap. 3; Shotts (2019), caps. de permisos y procesos |
| **Evidencia** | Archivo restaurado, script ejecutable y registro del control de un proceso |

## Relación con la Unidad 1 y con el proyecto integrador

La reproducibilidad de la Unidad 1 exige **documentar** qué hiciste con cada archivo. Aquí adquieres el
control fino sobre archivos y procesos que necesitarás para ejecutar y vigilar análisis. Entender un
**proceso** en el servidor prepara el concepto de **trabajo** que enviarás al cluster en S6.

## Resultados de aprendizaje de la sesión

Al terminar S5, el estudiante es capaz de:

1. **Identificar** el tipo de un archivo con `file` y **visualizar** su contenido con `less`, `head` y
   `tail` (y `cat` con prudencia).
2. **Editar** un archivo de texto en el servidor con `nano`.
3. **Comprimir y restaurar** archivos con `gzip`/`gunzip`/`zcat` y `tar`.
4. **Leer permisos** en `ls -l`, distinguir permisos de archivos y de directorios, y **modificarlos**
   con `chmod` (simbólico y numérico).
5. **Observar y controlar** procesos: primer/segundo plano, `ps`, `top`, `jobs`, `bg`, `fg`, `kill`.

## Antes de la sesión

| Elemento | Detalle |
| --- | --- |
| **Lectura obligatoria** | Este módulo completo. |
| **Preparación técnica** | Ten un archivo de texto de prueba en tu proyecto del servidor. |
| **Primer intento** | Ejecuta `file` y `head` sobre un archivo, e intenta lanzar un proceso `sleep 30` y observarlo. |
| **Producto para el taller** | Tu primer intento (comandos y lo que observaste) y tus dudas. |
| **Tiempo estimado** | Lectura ~45 min · primer intento ~25 min. |

---

## 1. Tipos de archivos: `file`

No todos los archivos son iguales: hay texto plano, binarios, comprimidos, etc. El comando `file`
identifica el tipo real de un archivo (sin fiarse solo de su extensión):

```bash
file genoma.fasta     # p. ej. "ASCII text"
file datos.gz         # p. ej. "gzip compressed data"
```

## 2. Visualizar el contenido

El siguiente bloque muestra las formas más comunes de ver un archivo **sin abrir un editor**:

```bash
less archivo.txt    # visor paginado (avanzar con espacio, salir con q)
head archivo.txt    # primeras 10 líneas
tail archivo.txt    # últimas 10 líneas
head -n 3 archivo   # primeras 3 líneas
cat archivo.txt     # muestra TODO el contenido de una vez
```

> **COMENTARIO:** Para archivos biológicos grandes (un genoma completo) **no uses `cat`**: llenaría la
> pantalla. Usa `less`, `head` o `tail` para asomarte a su contenido. `cat` es útil para archivos
> pequeños o para unir archivos, no para inspeccionar uno enorme.

## 3. Editar en el servidor: `nano`

Para crear o modificar texto directamente en el servidor usamos un editor de terminal. En este curso
empezamos con **nano**, que muestra los atajos en pantalla:

```bash
nano notas.md       # abrir/crear con nano
# guardar: Ctrl+O (y Enter) · salir: Ctrl+X
```

> **NOTA (consulta):** Existe también **vi/vim**, muy potente pero con más curva de aprendizaje.
> Conviene saber que existe porque está en todos los sistemas Unix, pero en esta unidad usamos `nano`.
> `vi/vim` queda como material de **consulta**, no se evalúa aquí.

## 4. Compresión de archivos

Los datos biológicos son grandes; comprimirlos ahorra espacio y acelera las transferencias. El
siguiente bloque muestra las herramientas básicas:

```bash
gzip archivo.fasta       # comprime -> archivo.fasta.gz (sustituye al original)
gunzip archivo.fasta.gz  # descomprime -> archivo.fasta
zcat archivo.fasta.gz    # muestra el contenido SIN descomprimir
tar -czf datos.tar.gz carpeta/   # empaqueta y comprime una carpeta
tar -xzf datos.tar.gz            # extrae el contenido
```

- `gzip`/`gunzip` comprimen y descomprimen un archivo.
- `zcat` te deja **leer** un `.gz` sin descomprimirlo (útil para asomarte).
- `tar` **empaqueta** una carpeta entera en un solo archivo (`.tar.gz`) y la restaura.

## 5. Permisos

En Unix cada archivo tiene **permisos** que definen **quién puede hacer qué**. Hay tres tipos de
permiso —**r** (leer), **w** (escribir), **x** (ejecutar)— para tres categorías de usuario: el
**dueño** (*user*), el **grupo** (*group*) y **los demás** (*others*).

Al ejecutar `ls -l` ves los permisos al inicio de cada línea:

```text
-rwxr-xr--  1 usuario grupo  1024 ago 20 10:00 script.sh
 │└┬┘└┬┘└┬┘
 │ │  │  └── others: r--  (solo leer)
 │ │  └───── group:  r-x  (leer y ejecutar)
 │ └──────── user:   rwx  (leer, escribir, ejecutar)
 └────────── tipo:   -=archivo, d=directorio
```

![Desglose de una cadena de permisos de ls -l en sus bloques (tipo, dueño, grupo y otros) con su equivalencia numérica.](images/figura-u2-permisos-unix.png)

*Figura 1. Lectura de permisos en `ls -l`: el primer carácter indica el tipo y los tres bloques siguientes los permisos de dueño, grupo y otros.*

> **NOTA — permisos de archivos vs. directorios.** El significado de `x` cambia según el objeto: en un
> **archivo**, `x` permite **ejecutarlo**; en un **directorio**, `x` permite **entrar** en él (hacer
> `cd`) y acceder a su contenido. Un directorio sin `x` no se puede recorrer aunque tenga `r`.

El comando `chmod` cambia los permisos. Primero conviene la forma **simbólica**, que es más legible:

```bash
chmod u+x script.sh    # AÑADE ejecución (x) al dueño (u)  — forma simbólica
chmod g-w script.sh    # QUITA escritura (w) al grupo (g)
```

Solo **después** de entender `r`, `w`, `x` conviene la forma **numérica**, que suma valores
(`r=4`, `w=2`, `x=1`):

```bash
chmod 754 script.sh    # user=7(rwx) group=5(r-x) others=4(r--)
```

> **NOTA:** `7 = 4+2+1 = rwx`, `5 = 4+1 = r-x`, `4 = r--`. Usa la forma numérica cuando ya tengas claro
> qué significa cada letra; si no, quédate con la simbólica.

## 6. Procesos

Cada programa en ejecución es un **proceso**, identificado por un número (**PID**, *Process ID*).
Saber verlos y controlarlos es esencial cuando corres análisis que tardan.

**Observar procesos:**

```bash
ps -f -u $USER   # tus procesos, con detalle (usuario, PID, comando…)
top              # procesos en tiempo real (salir con q)
jobs             # trabajos que lanzaste en esta terminal (con su número)
```

**Primer plano y segundo plano.** Un proceso puede correr en **primer plano** (ocupa tu terminal hasta
que termina) o en **segundo plano** (sigue corriendo y te devuelve la terminal):

```bash
comando &        # ejecuta "comando" en segundo plano
# si lo lanzaste en primer plano: Ctrl-Z lo pausa; luego 'bg' lo manda al fondo
fg               # trae al primer plano el trabajo en segundo plano
kill PID         # termina el proceso con identificador PID
nohup comando &  # segundo plano que NO se interrumpe si cierras la sesión
```

![Diagrama de un proceso en primer plano que ocupa la terminal frente a uno en segundo plano que la libera.](images/figura-u2-procesos-primer-segundo-plano.png)

*Figura 2. Primer plano frente a segundo plano: en primer plano el proceso ocupa la terminal; en segundo plano (`&`) la libera y sigue corriendo.*

> **NOTA:** `nohup ... &` sirve para procesos largos: continúan aunque cierres la conexión, y su
> salida de pantalla queda en el archivo `nohup.out`.

> **IMPORTANTE — `nohup` no sustituye al planificador.** En un servidor compartido, y sobre todo en un
> cluster, los análisis **pesados o prolongados** no se lanzan con `nohup` en el nodo de acceso: se
> **envían al sistema de colas** (SGE), como verás en S6. `nohup` sirve para tareas modestas; no para
> saturar una máquina compartida.

> **NOTA (ampliación):** Para mantener una sesión abierta aunque te desconectes existen `screen` y
> `tmux`. Se mencionan como **ampliación**: no se evalúan en esta unidad y se profundizan en cursos
> posteriores.

> **COMENTARIO:** Entender procesos es la antesala del cómputo en cluster: cuando envías un trabajo,
> en realidad lanzas un proceso que corre por su cuenta en otra máquina.

---

## Práctica S5 — Archivos, permisos y control de un proceso

> **Regla — primero a mano.** Ejecuta y observa **tú** cada paso; documenta qué ocurre. No apliques
> permisos "porque sí": cada cambio debe tener un propósito claro.

### Antes de clase (primer intento)

1. Copia al servidor (o crea con `nano`) un archivo de texto de prueba y averigua su tipo con `file`.
2. Visualízalo con `head`, `tail` y `less`.
3. Lanza `sleep 30` y, en otra terminal o con `&`, intenta **observarlo** con `ps` o `jobs`.
4. Anota qué viste y tus dudas.

### Durante el taller

Con codificación en vivo y repetición:

1. **Identifica y visualiza** un archivo (`file`, `head`, `tail`, `less`).
2. **Edítalo** con `nano` (añade una línea, guarda y sal).
3. **Comprímelo y restáuralo** (`gzip`/`gunzip`, o `tar` para una carpeta) y verifica que el contenido
   restaurado coincide con el original.
4. **Crea un script mínimo** llamado `prueba.sh` con este contenido:

   ```bash
   #!/bin/bash
   echo "Prueba de ejecución"
   ```

5. **Pruébalo antes y después** de darle permiso de ejecución, para ver la diferencia:

   ```bash
   ./prueba.sh          # antes: "Permission denied"
   chmod u+x prueba.sh  # añade ejecución al dueño
   ./prueba.sh          # después: imprime "Prueba de ejecución"
   ```

6. **Ejecuta un proceso controlado**, por ejemplo `sleep 120`, y practica **observarlo y controlarlo**
   con `jobs`, `bg`, `fg` y `kill`.
7. Documenta **qué ocurrió** en cada paso.

> **COMENTARIO:** El script `prueba.sh` sí tiene propósito para `chmod u+x`: es un **programa** que
> queremos ejecutar. No tiene sentido dar permiso de ejecución a un archivo de texto que solo se lee.

### Después del taller (entrega final)

Entrega, en tu bitácora/protocolo:

- el archivo **comprimido y restaurado** correctamente (evidencia de que el contenido coincide);
- el **script `prueba.sh`** hecho ejecutable, con la muestra de "antes y después" de `chmod`;
- el **registro del control de un proceso**: cómo lo lanzaste, cómo lo observaste (`jobs`/`ps`) y cómo
  lo llevaste a segundo plano o lo terminaste (`bg`/`fg`/`kill`).

## Errores frecuentes y cómo diagnosticarlos

| Síntoma | Causa probable | Cómo diagnosticar / corregir |
| --- | --- | --- |
| `Permission denied` al ejecutar un script | Falta el permiso `x` | `ls -l` para ver permisos; `chmod u+x` |
| No puedo entrar a un directorio | Falta `x` en el directorio | `ls -ld carpeta`; ajusta con `chmod` |
| `cat` "inundó" la pantalla | Archivo muy grande | Usa `less`, `head` o `tail` |
| El proceso sigue tras cerrar la terminal | Se lanzó con `nohup ... &` | Búscalo con `ps -f -u $USER` y `kill PID` |
| `kill` no termina el proceso | PID equivocado | Confirma el PID con `ps`/`jobs` antes de `kill` |

## Evidencia de aprendizaje

**Archivo restaurado** correctamente, **script ejecutable** y **registro del control de un proceso**.

## Criterios de logro

| Criterio | Logrado | Parcialmente logrado | Aún no logrado |
| --- | --- | --- | --- |
| Identificar/visualizar archivos | Usa `file`, `head`, `tail`, `less` según el caso | Usa alguno con dudas | No distingue cuándo usar cada uno |
| Compresión y restauración | Comprime y restaura verificando el contenido | Comprime sin verificar | No logra restaurar |
| Permisos con propósito | Explica `r`,`w`,`x` y usa `chmod` con sentido | Cambia permisos sin explicar | No lee ni cambia permisos |
| Control de un proceso | Lanza, observa y controla (`jobs`/`bg`/`fg`/`kill`) | Solo observa | No controla el proceso |
| Registro | Documenta qué ocurrió en cada paso | Registro incompleto | Sin registro |

## Autoevaluación — semáforo de salida

- 🟢 **Verde:** comprimí y restauré un archivo, hice ejecutable mi script y controlé un proceso.
- 🟡 **Amarillo:** logré la mayoría, pero dudo del manejo de `bg`/`fg`/`kill`.
- 🔴 **Rojo:** me atoré con permisos o procesos; llevo mis comandos y el error al taller.

## Preparación para la siguiente sesión (S6)

Ya controlas archivos y procesos en el servidor. En **S6** darás el salto al **cluster**: verás por
qué un proceso pesado no debe correr en el nodo de acceso y cómo se **envía** al sistema de colas
(SGE). Lee el módulo [S6 — Cluster HPC y SGE](u2-s6-cluster-hpc.md) y escribe, antes de clase, un
primer *job script* mínimo.

## Alineación resultado–actividad–evidencia–criterio

| Resultado de aprendizaje | Actividad | Evidencia | Criterio de logro |
| --- | --- | --- | --- |
| Identificar y visualizar archivos | Práctica S5, pasos 1–2 | Comandos en la bitácora | Usa `file`/`head`/`tail`/`less` con criterio |
| Editar en el servidor | Práctica S5, paso 2 (taller) | Archivo editado | Edita y guarda con `nano` |
| Comprimir y restaurar | Práctica S5, paso 3 | Archivo restaurado | Restaura con contenido íntegro |
| Gestionar permisos | Práctica S5, pasos 4–5 | Script ejecutable | Usa `chmod` con propósito y lo explica |
| Controlar procesos | Práctica S5, paso 6 | Registro del proceso | Observa y controla un proceso |

## Glosario (español–inglés)

| Español | Inglés | Definición breve |
| --- | --- | --- |
| Permisos | Permissions | Reglas de quién puede leer, escribir o ejecutar. |
| Dueño / grupo / otros | User / group / others | Las tres categorías de usuario de un archivo. |
| Ejecutable | Executable | Archivo con permiso `x` que puede correrse como programa. |
| Comprimir | Compress | Reducir el tamaño de un archivo. |
| Proceso | Process | Un programa en ejecución. |
| Identificador de proceso | Process ID (PID) | Número que identifica un proceso. |
| Primer / segundo plano | Foreground / background | Ocupar la terminal frente a liberarla. |

## Referencias

- Buffalo, V. (2015). *Bioinformatics Data Skills*. O'Reilly Media. — Cap. 3. Disponible en
  `referencias/bioinformatics-data-skills.pdf`.
- Shotts, W. E. (2019). *The Linux Command Line* (2ª ed.). No Starch Press. — Permisos y procesos.
- htop (<https://htop.dev/>), GNU Screen (<https://www.gnu.org/software/screen/>) y tmux
  (<https://github.com/tmux/tmux/wiki>) — herramientas de monitoreo y sesión (ampliación).
