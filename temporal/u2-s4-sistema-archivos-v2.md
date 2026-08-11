# Unidad 2 · Módulo S4 — El sistema de archivos: navegación, organización y edición

> **NOTA — Lectura previa (aula invertida).** Este documento se lee **antes de la sesión S4**. En el
> taller construiremos en vivo la **estructura real del proyecto** sobre el servidor, con repetición
> del estudiante. Trae tu **primer intento** y tus dudas. Al final hay una **práctica (Tarea 3)** con
> tres momentos: antes de clase, durante el taller y entrega final.

Segundo módulo de la [Unidad 2](u2-entorno-unix-hpc.md). En S3 aprendiste a conectarte por SSH y a
**transferir** tus archivos al servidor comprobando su integridad. Hoy aprenderás a **moverte por el
sistema de archivos** y a **crear y organizar** directorios y archivos para levantar, por primera vez,
la **estructura real del proyecto** en tu espacio del servidor y colocar dentro de ella los archivos
que ya transferiste.

## El problema que resolveremos hoy

> **IMPORTANTE — problema conductor de S4.** Los archivos que transferiste en S3 (`pacientes.md`,
> `pacientes-metadatos.md` y `protocolo.md`) quedaron **juntos, en una ubicación provisional** de tu
> espacio en el servidor. Tu tarea de hoy es **crear la estructura que diseñaste en la Unidad 1
> (Tarea 2, S2)**, **colocar cada archivo donde corresponde** y **comprobar que los datos originales
> no cambiaron** en el proceso.

En la Unidad 1 (S1–S2) hiciste un trabajo que hoy vas a materializar:

- En **S1** iniciaste `protocolo.md` y tu **reporte de lectura** (Tarea 1).
- En **S2** trabajaste `pacientes.md`, sus **metadatos** (`pacientes-metadatos.md`), tu
  `bitacora-ia.md` y el **diseño conceptual** de la organización del proyecto (Tarea 2). Ese diseño
  quedó **en papel**: todavía **no** construiste la estructura con Unix.
- En **S3** transferiste al servidor `pacientes.md`, `pacientes-metadatos.md` y `protocolo.md`, y
  comprobaste su integridad con *checksums*.
- En **S4** (hoy) creas por **primera vez** la estructura real en el servidor y colocas dentro de ella
  los archivos ya transferidos.

La estructura final a la que queremos llegar es:

```text
proyecto/
├── README.md
├── data/
│   ├── source/
│   │   ├── pacientes.md
│   │   └── pacientes-metadatos.md
│   └── processed/
├── src/
├── results/
└── doc/
    ├── protocolo.md
    └── bitacora-ia.md
```

> **ADVERTENCIA — un archivo aún no está en el servidor.** En S3 solo transferiste tres archivos
> (`pacientes.md`, `pacientes-metadatos.md` y `protocolo.md`). Tu `bitacora-ia.md` **todavía vive en tu
> computadora**. Para completar la organización tendrás que **transferirlo** al servidor; lo haremos en
> el taller como aplicación de `scp`/`rsync` (§9). No supongas que ya está disponible: primero
> compruébalo con `ls`.

## Ficha del módulo

| Elemento | Descripción |
| --- | --- |
| **Sesión** | S4 (2 h) |
| **Tema** | Sistema de archivos, navegación, organización del proyecto y edición en el servidor |
| **Competencia** | B — Dominio del entorno Unix y del cómputo científico |
| **Resultado (plan)** | Navega el sistema de archivos y opera archivos y directorios; edita en el servidor |
| **Consulta previa (plan)** | L3-shell, diapositivas 39–60 (este módulo las sustituye como lectura autocontenida) |
| **Lectura base** | Buffalo (2015), Cap. 3 (navegación y manipulación de archivos) |
| **Lectura de consulta** | Shotts (2019), caps. 2–4 (navegación y manipulación de archivos y directorios) |
| **Tarea del plan** | **Tarea 3** — estructura de directorios del proyecto en el servidor |
| **Evidencia** | Estructura reproducible del proyecto, con los archivos de S2–S3 en su lugar, verificada con `tree`/`ls -R` y con checksum, y `protocolo.md` actualizado |

## Relación con la Unidad 1 y con el proyecto integrador

En la Unidad 1 diseñaste la **organización de un proyecto reproducible** (Noble, 2009). Aquí la
**materializas** en el servidor: creas las carpetas reales donde vivirán tus datos, scripts y
resultados durante todo el curso, y colocas en ellas los archivos que ya produjiste y transferiste.
La estructura que construyas hoy es la que usarás en las Unidades 3 a 6.

## Resultados de aprendizaje de la sesión

Al terminar S4, el estudiante es capaz de:

1. **Describir** la estructura en árbol del sistema de archivos y el papel de `/`, `~` y el directorio
   actual, y **distinguir** el *home* genérico del **espacio institucional** `/export/space3/users/$USER`.
2. **Distinguir** rutas absolutas y relativas y **usar** `.`, `..` y `~`, entendiendo que una ruta
   relativa **parte del directorio actual**.
3. **Navegar** entre directorios con `pwd`, `ls` y `cd` usando ambos tipos de ruta, tras **comprobar el
   contexto** con `hostname`, `whoami` y `pwd`.
4. **Crear y organizar** archivos y directorios (`mkdir`, `mkdir -p`, `touch`, `cp -i`, `cp -r`,
   `mv -i`) y **eliminar de forma segura** (`rm -i`, `rmdir`) dentro de una carpeta de prueba.
5. **Construir** una **plantilla reutilizable** (`template/`) con la estructura canónica, **clonarla**
   con `cp -r` a `proyecto/` y **colocar** en ella los archivos transferidos en S3.
6. **Verificar** la estructura con `tree` o `ls -R` y **comprobar la integridad** de `pacientes.md`
   comparando su *checksum* con el registrado en S3.
7. **Transferir** con `scp` o `rsync` un archivo faltante (`bitacora-ia.md`) desde el equipo local
   (aplicación).
8. **Editar** en el servidor con `nano` para completar `README.md` y **actualizar** `doc/protocolo.md`.

## Antes de la sesión

| Elemento | Detalle |
| --- | --- |
| **Lectura obligatoria** | Este módulo completo (sustituye a las diapositivas L3 39–60). |
| **Lectura obligatoria adicional** | Buffalo (2015), Cap. 3 — navegación y manipulación de archivos. |
| **Lectura de consulta** | Shotts (2019), caps. 2–4 (opcional, para profundizar). |
| **Preparación técnica** | Conéctate al servidor (habilidad de S3). Ten a la vista el diseño de la estructura del proyecto de la Unidad 1 y tu `protocolo.md` (con el checksum de `pacientes.md` que registraste en S3). Localiza en tu computadora `bitacora-ia.md`. |
| **Primer intento** | Ver la Práctica S4 → *Antes de clase*. |
| **Producto para el taller** | Tu primer intento (comandos, errores y dudas) y la ubicación de `bitacora-ia.md` en tu equipo. |

> **NOTA — tiempos estimados (son estimaciones).** Lectura del módulo ~40 min · lectura obligatoria
> adicional (Buffalo Cap. 3, parte) ~30 min · lecturas de consulta (Shotts) ~20 min opcional · primer
> intento ~30 min · taller presencial 120 min · corrección y entrega posterior ~40 min · actividad
> formativa de IA ~30 min.

> **NOTA — cómo leer los bloques de comandos.** Igual que en S3, cada bloque indica **desde dónde** se
> ejecuta: `[LOCAL]` en tu computadora y `[REMOTO]` dentro del servidor. Antes de cualquier operación,
> comprueba el contexto con `hostname`, `whoami` y `pwd`. `scp` y `rsync` (§9) **se lanzan desde tu
> computadora** (`[LOCAL]`), aunque copien hacia el servidor.

---

## 1. La estructura en árbol, la raíz y tu espacio de trabajo

En Unix, archivos y directorios (carpetas) se organizan en una **jerarquía en forma de árbol** que
empieza en la **raíz**, representada por `/`. De la raíz cuelgan directorios que, a su vez, contienen
otros directorios y archivos.

![Árbol del sistema de archivos que parte de la raíz `/`, muestra el espacio institucional `/export/space3/users/$USER`, la carpeta `proyecto/` y sus subcarpetas `README.md`, `data/source/`, `data/processed/`, `src/`, `results/` y `doc/`.](images/figura-u2-arbol-sistema-archivos.png)

*Figura 1. El sistema de archivos como árbol: todo cuelga de la raíz `/`; tu espacio de trabajo
institucional y la carpeta del proyecto son ramas de ese árbol. Elaboración propia.*

Conceptos clave:

- **Directorio raíz `/`:** el origen de todo el árbol.
- **Directorio *home* (`~`):** tu carpeta personal, aquella donde el sistema te sitúa al iniciar sesión
  y donde tienes permisos para trabajar. La variable `~` es un atajo que representa esa carpeta.
- **Directorio actual:** el lugar donde "estás parado" en este momento (lo consultas con `pwd`).
- **Ruta (*path*):** la dirección de un archivo o directorio dentro del árbol.

> **NOTA — *home* genérico vs. espacio institucional.** En ejemplos genéricos verás `/home/usuario`
> como directorio personal. En el servidor del curso, tu espacio de trabajo **no** está en `/home`
> sino en `/export/space3/users/$USER`. La variable `$USER` se reemplaza automáticamente por tu nombre
> de usuario. Cuando trabajes en el servidor, usa **tu espacio institucional**: es ahí donde tienes
> capacidad y permisos para crear el proyecto.

> **TIP:** Para saber cuál es tu *home* en el servidor, ejecuta `echo $HOME` o simplemente `cd` seguido
> de `pwd`. Compara el resultado con `/export/space3/users/$USER`.

## 2. Rutas absolutas y relativas

Una **ruta** es la dirección que le das a un comando para que encuentre un archivo o directorio. Hay
dos formas de escribirla:

- **Ruta absoluta:** parte desde la raíz `/` y **siempre apunta al mismo lugar**, sin importar dónde
  estés. Ejemplo:
  `/export/space3/users/$USER/proyecto/data/source/pacientes.md`.
- **Ruta relativa:** parte **desde tu directorio actual** (no desde `~`). Ejemplo: si estás en
  `.../proyecto`, la ruta relativa `data/source/pacientes.md` apunta al mismo archivo.

Símbolos útiles en las rutas:

- `.` : el directorio actual.
- `..` : el directorio padre (uno hacia arriba).
- `~` : tu directorio *home*.

![Comparación entre una ruta absoluta que parte de la raíz `/` hasta `pacientes.md` y una ruta relativa que parte del directorio actual `proyecto/` hasta el mismo archivo.](images/figura-u2-rutas-absolutas-relativas.png)

*Figura 2. El mismo archivo, dos rutas: la absoluta parte de `/`; la relativa parte del directorio
actual (aquí, `proyecto/`). Elaboración propia.*

> **IMPORTANTE:** Una ruta **relativa** empieza en tu **directorio actual**, no necesariamente en tu
> *home* (`~`). Si te confundes de punto de partida, terminarás creando o buscando carpetas donde no
> querías. Ante la duda, ejecuta `pwd` para saber desde dónde parte tu ruta relativa.

> **¿SABÍAS QUE?:** Una misma ubicación se puede alcanzar por **muchos caminos**. Desde
> `.../proyecto/doc` puedes llegar a `pacientes.md` con la ruta relativa `../data/source/pacientes.md`
> (subes con `..` y bajas por `data/source`). Comprobar que dos caminos distintos llevan al mismo sitio
> es una forma sencilla de **robustez** (§11).

## 3. Navegar: `pwd`, `ls`, `cd`

Antes de crear nada, hay que saber orientarse. Estos son los comandos **esenciales** de navegación:

```bash
pwd                 # muestra dónde estás (ruta absoluta actual)
ls                  # lista el contenido del directorio actual
ls -lah             # lista con detalle (l), incluye ocultos (a) y tamaños legibles (h)
cd carpeta          # entra a "carpeta" (ruta relativa)
cd /ruta/absoluta   # entra usando una ruta absoluta
cd ..               # sube al directorio padre
cd ~                # va a tu home
cd -                # regresa al directorio anterior
```

> **TIP:** Combina la tecla **Tab** para autocompletar nombres de rutas y evitar errores de tipeo;
> `ls -lh` muestra los tamaños en formato legible (KB, MB, GB) y `cd -` te devuelve al directorio donde
> estabas antes.

### Micropráctica 1 — Reconocer el contexto y navegar

> **Problema.** Antes de crear la estructura necesitas confirmar en qué máquina estás, con qué cuenta y
> en qué ubicación, y saber moverte con seguridad.

**[LOCAL] En tu computadora, conéctate:**

```bash
ssh usuario@servidor        # usa las credenciales dadas en clase
```

**[REMOTO] Ya dentro del servidor, comprueba el contexto y explora:**

```bash
hostname     # ¿en qué computadora estoy? (debe ser el servidor)
whoami       # ¿con qué cuenta trabajo?
pwd          # ¿en qué ubicación estoy?
ls -lah      # ¿qué archivos hay aquí?
cd ..        # sube un nivel
pwd          # confirma que cambiaste de ubicación
cd -         # regresa al directorio anterior
```

Deberías ver entre los archivos `pacientes.md`, `pacientes-metadatos.md` y `protocolo.md`, que
transferiste en S3. Si no los ves, revisa que estés en la ubicación donde los dejaste.

> **Después de la micropráctica, responde:** (1) ¿Qué te devolvió `hostname` y cómo confirma que estás
> en el servidor? (2) ¿Aparecen tus tres archivos de S3? ¿Ves también `bitacora-ia.md`?

## 4. Crear directorios y archivos

Estas son las operaciones **esenciales** para construir la estructura:

```bash
mkdir nueva            # crea el directorio "nueva"
mkdir -p a/b/c         # crea toda la ruta anidada de una vez
touch archivo.txt      # crea un archivo vacío (o actualiza su fecha)
```

- `mkdir` crea **un** directorio; falla si el directorio padre no existe.
- `mkdir -p` crea **directorios anidados** en un solo paso (útil para `data/source`).
- `touch` crea un archivo vacío; lo usaremos, por ejemplo, para dejar preparado `README.md` antes de
  editarlo.

## 5. Copiar, mover y renombrar de forma segura

Para **colocar** los archivos en su lugar usarás copia y movimiento. Presentamos **primero las
variantes seguras**, con confirmación:

```bash
cp -i origen destino     # copia; pregunta antes de sobrescribir el destino
cp -r carpeta destino    # copia una carpeta y su contenido
mv -i origen destino     # mueve o renombra; pregunta antes de sobrescribir
```

- `cp -i` **copia** y **pide confirmación** si el destino ya existe.
- `mv -i` **mueve** o **renombra**: si el destino es otra carpeta, mueve; si es un nombre nuevo en el
  mismo lugar, renombra. Con `-i` te avisa antes de sobrescribir.
- Las versiones **sin `-i`** (`cp`, `mv`) hacen lo mismo pero **sin preguntar**.

> **ADVERTENCIA — `cp` y `mv` pueden sobrescribir.** Si el destino ya existe, `cp` y `mv` **sin `-i`**
> lo **reemplazan sin avisar** y el contenido anterior se pierde. Mientras te acostumbras, usa siempre
> `cp -i` y `mv -i`. En este módulo **copiamos antes de mover**: conservamos una copia provisional
> hasta terminar de verificar (§8).

### Micropráctica 2 — Copiar, mover y renombrar en una carpeta de prueba

> **Problema.** Antes de tocar tus archivos reales, practica copia, movimiento y renombrado en un lugar
> donde un error no tenga consecuencias.

**[REMOTO] En el servidor, dentro de tu espacio de trabajo:**

```bash
mkdir -p prueba-s4          # carpeta aislada solo para practicar
cd prueba-s4
touch a.txt                 # crea un archivo de prueba
cp -i a.txt b.txt           # copia a.txt como b.txt
mv -i b.txt c.txt           # renombra b.txt a c.txt
mkdir sub
mv -i c.txt sub/            # mueve c.txt dentro de sub/
cp -r sub sub-copia         # copia la carpeta COMPLETA (ensayo de cp -r)
ls -R                       # observa el resultado
cd ..
```

Fíjate en `cp -r sub sub-copia`: copia **toda** la carpeta `sub/` con su contenido. Es el mismo comando
que usarás para **clonar la plantilla** (`cp -r template proyecto`) en la Tarea 3.

> **Después de la micropráctica, responde:** (1) ¿En qué se diferenció **renombrar** (`mv a b` en el
> mismo directorio) de **mover** (`mv a carpeta/`)? (2) ¿Qué copió `cp -r sub sub-copia` que `cp` sin
> `-r` no habría copiado? (3) ¿Por qué conviene usar `-i`?

## 6. Eliminar de forma segura

En Unix **no hay papelera**: `rm` borra de forma **permanente e inmediata**. Por eso, la eliminación se
practica con cuidado y **solo dentro de la carpeta de prueba**.

```bash
rm -i archivo          # borra un archivo, pidiendo confirmación
rmdir carpeta          # borra un directorio VACÍO (falla si tiene contenido)
```

> **ADVERTENCIA — comprueba antes de borrar.** Antes de ejecutar cualquier `rm`, comprueba **dónde
> estás** y **qué hay** con `pwd` y `ls`. Borra solo dentro de `prueba-s4/`. En la **Tarea 3
> obligatoria no se borra ningún archivo del proyecto**: eliminar es una habilidad que se practica
> aparte, en la carpeta de prueba.

> **NOTA — sobre `rm -r`.** Existe la opción `rm -r`, que borra un directorio **y todo su contenido**.
> Es potente y peligrosa: un error de ruta puede eliminar mucho más de lo que querías. En este módulo
> **no** la usamos en la práctica obligatoria, y **no** conviene adoptar `rm -ri` como hábito rutinario:
> la costumbre de confirmar "sí" a todo anula la protección. Para vaciar una carpeta de prueba, borra
> primero sus archivos con `rm -i` y luego el directorio vacío con `rmdir`.

### Micropráctica 3 — Eliminación segura (solo en `prueba-s4/`)

**[REMOTO] En el servidor:**

```bash
cd prueba-s4
pwd                    # confirma que estás en la carpeta de prueba
ls -R                  # confirma qué vas a borrar
rm -i sub/c.txt        # borra el archivo, confirmando
rmdir sub              # ahora sub/ está vacío: se puede borrar
rm -i a.txt            # borra el resto de archivos de prueba
cd ..
```

> **Después de la micropráctica, responde:** (1) ¿Por qué `rmdir sub` falló si `sub/` aún contenía
> `c.txt`? (2) ¿Cómo te protegió comprobar `pwd` y `ls` antes de borrar?

## 7. Ver el árbol: `tree` o `ls -R`

Para comprobar que tu estructura quedó como esperabas:

```bash
tree              # muestra el árbol de directorios (si está instalado)
ls -R             # lista recursivamente el contenido (alternativa siempre disponible)
```

Si `tree` no está disponible en el servidor, `ls -R` cumple la misma función de verificación.

> **NOTA — `tree` puede no estar instalado.** `tree` es cómodo pero no siempre está disponible. `ls -R`
> **siempre** funciona y sirve exactamente para comprobar la estructura. Usa el que tengas.

## 8. La estructura canónica del proyecto

Usaremos **la misma** estructura de la Unidad 1 (Noble, 2009), sin variaciones:

```text
proyecto/
├── README.md          # descripción del proyecto
├── data/
│   ├── source/        # datos originales, inmutables
│   └── processed/     # datos derivados
├── src/               # scripts
├── results/           # resultados del análisis
└── doc/               # documentación (protocolo, bitácora)
```

> **IMPORTANTE — datos originales intactos.** Los datos originales se conservan en `data/source/`
> **sin modificarse**: se leen y se copian, pero no se editan. Cualquier transformación produce
> archivos nuevos que van a `data/processed/`, nunca encima del original. Conservar el original con su
> nombre y su *checksum* preserva la **procedencia** y la trazabilidad de tu análisis (Noble, 2009;
> Buffalo, 2015, Cap. 3).

### Una plantilla reutilizable del proyecto

En lugar de crear la estructura "a mano" cada vez, conviene construir **una sola vez** una carpeta
**plantilla** (`template/`) con el esqueleto vacío del proyecto y un `doc/protocolo.md` de arranque, y
después **clonarla** con `cp -r` cada vez que empieces un proyecto nuevo. Así garantizas que **todos**
tus proyectos comparten la misma organización, con menos errores y menos tecleo (Noble, 2009).

En la Tarea 3 usaremos exactamente este patrón:

1. Creas la plantilla `template/` con la estructura canónica y `doc/protocolo.md`.
2. La **clonas** con `cp -r template proyecto`: `proyecto/` es una copia independiente; `template/`
   queda intacta para reutilizarla.
3. Dentro de `proyecto/` **mueves** a su lugar los archivos que ya tenías (los datos de S3), traes tu
   `protocolo.md` real y transfieres `bitacora-ia.md`.

> **TIP:** `cp -r template proyecto` copia la carpeta **completa** (todas sus subcarpetas y archivos).
> Como `template/` no contiene datos, puedes clonarla tantas veces como proyectos tengas. Esta es la
> versión sencilla, "a mano", de la idea de las **plantillas de proyecto** que se usan en
> bioinformática para estandarizar la organización.

## 9. Transferir el archivo que falta con `scp` o `rsync`

Como viste en el problema conductor, `bitacora-ia.md` **no** se transfirió en S3: sigue en tu
computadora. En S3 usaste SFTP/FileZilla de forma interactiva; ahora aplicamos las dos herramientas de
**línea de comandos** que S3 anunció para S4: `scp` y `rsync`. Ambas **se lanzan desde tu computadora**
(`[LOCAL]`), no desde el servidor.

```bash
# [LOCAL] Copiar un archivo al servidor con scp:
scp bitacora-ia.md usuario@servidor:/export/space3/users/$USER/

# [LOCAL] Alternativa con rsync (informa el progreso y no recopia lo idéntico):
rsync -avP bitacora-ia.md usuario@servidor:/export/space3/users/$USER/
```

- `scp origen usuario@servidor:destino` copia un archivo en **una sola orden**.
- `rsync -avP` **sincroniza**: `-a` conserva atributos, `-v` informa qué hace y `-P` muestra el
  progreso y permite **reanudar** una transferencia parcial. Es preferible cuando copias muchos
  archivos o archivos grandes.
- El `:` separa la máquina remota de la **ruta de destino**; fíjate bien en los dos puntos.

> **IMPORTANTE — ¿local o remoto?** `scp` y `rsync` se ejecutan **desde tu computadora**, con el
> servidor como destino tras el `:`. Comprueba con `hostname` que estás en `[LOCAL]` antes de lanzarlos.
> No compartas tu contraseña, llaves ni la dirección real del servidor en registros o capturas.

> **NOTA — clasificación de estas herramientas.** En S4, `scp`/`rsync` son una **aplicación** puntual
> para completar la organización; su estudio a fondo (junto con datos reales) continúa en la Unidad 3.

## 10. Editar en el servidor con `nano`

Para completar `README.md` y actualizar `protocolo.md` **dentro del servidor** usaremos `nano`, un
editor de texto sencillo de la terminal. Lo introducimos en el **mínimo necesario** para esta tarea.

```bash
nano README.md         # abre (o crea) el archivo en el editor
```

Dentro de `nano`:

- escribes normalmente;
- **guardar:** `Ctrl-O`, luego Enter para confirmar el nombre;
- **salir:** `Ctrl-X`.

Las combinaciones aparecen en la barra inferior; `^` significa la tecla `Ctrl`.

> **NOTA — `vi` como herramienta de consulta.** En el servidor también existe `vi` (o `vim`), un editor
> muy potente pero de manejo distinto. En este curso lo tratamos **solo como consulta**: lo importante
> es que, si entras a `vi` por accidente, sepas **salir** pulsando `Esc` y escribiendo `:q!` seguido de
> Enter (salir sin guardar). Para editar en S4 usa `nano`.

> **TIP:** No es necesario editar archivos enormes en la terminal. `nano` es ideal para retoques
> rápidos —completar un `README.md`, añadir una sección a `protocolo.md`— directamente en el servidor,
> sin transferir de ida y vuelta.

## Clasificación de los comandos de S4

| Categoría | Comandos | Para qué |
| --- | --- | --- |
| **Esenciales** | `pwd`, `ls`, `cd`, `mkdir`, `mkdir -p`, `touch`, `cp -i`, `cp -r`, `mv -i`, `tree`/`ls -R`, `nano` | Navegar, crear la plantilla y clonarla, organizar la estructura, editar en el servidor |
| **Seguridad** | `cp -i`, `mv -i`, `rm -i`, `rmdir`, `hostname`, `whoami`, `pwd` (antes de operar) | Evitar sobrescrituras y borrados accidentales; confirmar el contexto |
| **Aplicación** | `scp`, `rsync -avP` | Transferir `bitacora-ia.md` desde el equipo local |
| **Consulta** | `man`, `vi` (solo salir) | Resolver dudas sin depender del docente; reconocer `vi` |

---

## Práctica S4 — Estructura de directorios del proyecto (Tarea 3)

> **Regla — primero a mano, luego con IA.** Primero construyes y organizas la estructura **tú**, paso a
> paso. Después la comparas con una propuesta de IA en la **Actividad formativa de IA** (§ siguiente).
> Tu trabajo manual es la **línea base de comparación, no una verdad absoluta**: tanto tu solución como
> la de la IA se contrastan con la lección, con `man` y con una prueba controlada.

Conserva la numeración oficial: esta es la **Tarea 3** del plan.

### Antes de clase (primer intento) — *formativo*

Trabaja en tu espacio del servidor. Registra **todo** (comandos, errores y dudas) para llevarlo al
taller.

1. **Revisa** la estructura que diseñaste en S2 (Tarea 2) y tenla a la vista.
2. **Identifica** los archivos que produjiste o transferiste antes: `pacientes.md`,
   `pacientes-metadatos.md`, `protocolo.md` (ya en el servidor) y `bitacora-ia.md` (aún en tu
   computadora).
3. **Decide** en qué directorio debe vivir cada archivo (según la estructura canónica de §8).
4. **Intenta** crear una carpeta **plantilla** `template/` con la estructura del proyecto y un
   `doc/protocolo.md`, y **clonarla** con `cp -r template proyecto`. Hazlo **paso a paso**, no de
   memoria; si no llegas a todo, deja anotado dónde te atoraste.
5. **Registra** los comandos que usaste, los errores que aparecieron y tus dudas.

> **NOTA — cómo se evalúa este momento.** El primer intento es **formativo**: da puntos por
> **preparación**, no por acierto. Los errores razonables **no se penalizan**; su valor es llegar al
> taller con preguntas concretas.

### Durante el taller — *formativo (participación y corrección)*

Con repetición guiada y comprobando el contexto en cada paso. La idea rectora: **construir la
plantilla una vez, clonarla y luego colocar los archivos**.

1. **Confirma** que estás en el servidor y en `/export/space3/users/$USER` (`hostname`, `whoami`,
   `pwd`).
2. **Localiza** los archivos transferidos en S3 (`ls -lah`) en su ubicación provisional; comprueba que
   `bitacora-ia.md` **aún no** está en el servidor.
3. **Crea** explícitamente la carpeta plantilla `template/` y entra en ella:

   ```bash
   mkdir template
   cd template
   pwd
   ```

4. **Construye** la estructura dentro de `template/` (crea la carpeta antes que sus ramas) y deja un
   `doc/protocolo.md` de arranque:

   ```bash
   mkdir -p data/source data/processed
   mkdir src results doc
   touch README.md
   touch doc/protocolo.md
   ls -R
   cd ..
   ```

   Si quieres, abre `doc/protocolo.md` con `nano` y escribe los encabezados de arranque (Objetivo,
   Procedimiento, Verificación…), para que la plantilla ya traiga el esqueleto del protocolo.
5. **Clona** la plantilla para este proyecto copiando **toda la carpeta** con `cp -r`:

   ```bash
   cp -r template proyecto
   ls -R proyecto
   ```

   Ahora `proyecto/` es una copia **independiente** de `template/`; la plantilla queda intacta para
   reutilizarla en futuros proyectos.
6. **Navega** por `proyecto/` usando rutas **absolutas** y **relativas** (y `.`, `..`, `~`),
   comprobando con `pwd` que llegas a donde esperas.
7. **Mueve** los datos transferidos en S3 a su lugar dentro de `proyecto/` con `mv -i` (desde la
   ubicación provisional, aquí tu *home*):

   ```bash
   mv -i ~/pacientes.md            proyecto/data/source/
   mv -i ~/pacientes-metadatos.md  proyecto/data/source/
   ```

8. **Trae tu `protocolo.md` real** de S3 sobre el de arranque de la plantilla (te pedirá **confirmar la
   sobrescritura**) y **transfiere** `bitacora-ia.md`, que no viajó en S3:

   ```bash
   # [REMOTO] tu protocolo real reemplaza el de arranque de la plantilla:
   cp -i ~/protocolo.md proyecto/doc/protocolo.md
   # [LOCAL] transfiere la bitácora desde tu computadora:
   scp bitacora-ia.md usuario@servidor:/export/space3/users/$USER/
   # [REMOTO] colócala en doc/:
   mv -i ~/bitacora-ia.md proyecto/doc/
   ```

   Al terminar este paso deben estar colocados:

   - `pacientes.md` y `pacientes-metadatos.md` en `proyecto/data/source/`;
   - `protocolo.md` y `bitacora-ia.md` en `proyecto/doc/`;
   - `README.md` en la raíz de `proyecto/`.

9. **Comprueba la integridad** de `pacientes.md` tras moverlo: calcula su *checksum* en su nueva
   ubicación y compáralo con el que registraste en S3.

   ```bash
   sha256sum proyecto/data/source/pacientes.md
   ```

   La cadena debe ser **idéntica** a la de S3 (la tienes en `protocolo.md`). **Mover** un archivo no
   cambia su contenido; el checksum lo confirma.
10. **Verifica el árbol** con `tree` o `ls -R` desde `proyecto/`.
11. **Practica `mv -i` (renombrar) y `cp -r` (copiar una carpeta)** solo en `prueba-s4/`, no con los
    archivos del proyecto.
12. **Practica `rm -i` y `rmdir`** solo dentro de `prueba-s4/`, comprobando antes `pwd` y `ls`.
13. **Actualiza** `proyecto/doc/protocolo.md` con `nano` (ver *Después del taller*).

> **NOTA — mover con red de seguridad.** Movemos los **datos** con `mv -i` porque el objetivo del
> problema conductor es **sacarlos de la ubicación provisional** y colocarlos en su lugar. La red de
> seguridad no es una copia manual, sino **dos comprobaciones**: la plantilla `template/` queda intacta
> para **regenerar la estructura** cuando quieras, y el **checksum** confirma que mover no alteró
> `pacientes.md`. El `protocolo.md` sí se trae con `cp -i` (conserva la copia provisional y demuestra la
> **confirmación de sobrescritura** sobre el archivo de arranque de la plantilla).

### Después del taller (entrega final) — *Tarea 3 · calificación principal*

Entrega, en tu espacio del servidor y documentado en `doc/protocolo.md`:

- **(Obligatorio)** la **plantilla `template/`** reutilizable y el proyecto **`proyecto/`** clonado a
  partir de ella con `cp -r`;
- **(Obligatorio)** la **estructura completa** de `proyecto/` con los archivos en su lugar;
- **(Obligatorio)** la **salida de `tree`** (o `ls -R`) que muestra el árbol;
- **(Obligatorio)** la **ubicación correcta** de los archivos reutilizados (`pacientes.md` y
  `pacientes-metadatos.md` en `data/source/`; `protocolo.md` y `bitacora-ia.md` en `doc/`;
  `README.md` en la raíz);
- **(Obligatorio)** el **checksum** de `pacientes.md` que demuestra que no cambió (comparado con S3);
- **(Obligatorio)** una **sección nueva** en `doc/protocolo.md` (ver plantilla abajo);
- **(Obligatorio)** el **registro de los comandos** utilizados;
- **(Obligatorio)** los **problemas encontrados** y cómo los resolviste (o indicar que no hubo);
- **(Obligatorio)** una **conclusión breve** sobre por qué esta organización favorece la
  reproducibilidad;
- **(Formativo)** el `README.md` **completado** con `nano` (descripción mínima del proyecto);
- **(Opcional)** el retiro, con `rm -i`, de la copia provisional de `protocolo.md` que quedó en la
  ubicación provisional, **solo después** de verificar.

Plantilla para la sección nueva de `doc/protocolo.md` (complétala con lo que **realmente** hiciste):

```markdown
## Organización del proyecto en el servidor (S4)

### Objetivo
Crear una plantilla reutilizable (template/), clonarla a proyecto/ con cp -r y colocar en ella los
archivos de S2–S3, comprobando que los datos originales no cambiaron.

### Estructura creada (salida de tree / ls -R de proyecto/)

### Ubicación de cada archivo
| Archivo | Directorio destino |
| --- | --- |
| pacientes.md | data/source/ |
| pacientes-metadatos.md | data/source/ |
| protocolo.md | doc/ |
| bitacora-ia.md | doc/ |
| README.md | (raíz de proyecto/) |

### Verificación de integridad de pacientes.md
| Momento | Checksum (SHA-256) |
| --- | --- |
| En S3 (transferencia) | |
| En S4 (tras mover a data/source/) | |
| ¿Coinciden? | |

### Registro de comandos

### Problemas encontrados y solución

### Conclusión
Por qué esta organización favorece la reproducibilidad.
```

## Actividad formativa de IA — revisar la estructura ya creada

> **NOTA:** Se llama **Actividad formativa de IA** (no "Tarea A") para no confundirla con las tareas
> oficiales del plan. Es **formativa**: su valor está en la comparación, no en una calificación aparte.
> La IA **revisa la misma estructura que ya creaste a mano**; **no** propone un proyecto nuevo ni opera
> el servidor.

Realízala **después** de construir la estructura tú. Trabaja sobre una **copia** de tu registro.

1. **Formula o adapta un prompt** con contexto, objetivo, formato esperado y criterios de verificación.
2. **Sustituye** cualquier dato institucional por marcadores: `[SERVIDOR]`, `[USUARIO]` y `[RUTA]`. No
   incluyas contraseñas, IP, huellas, llaves ni tokens.
3. **Pide** a la IA una propuesta para **crear y verificar la misma estructura**.
4. **Compara** su propuesta con la tuya **comando por comando**.
5. **Detecta** comandos eficientes (p. ej. `mkdir -p` para varias carpetas), riesgosos (p. ej. un
   `rm -r` innecesario), redundantes o incorrectos.
6. **Valida** con `man` y probando en `prueba-s4/`, nunca directamente sobre `proyecto/`.
7. **Registra** en `bitacora-ia.md`: fecha; actividad; herramienta y modelo (si se conoce); prompt;
   respuesta relevante; verificación independiente; errores o alucinaciones; correcciones;
   observaciones aceptadas o rechazadas; y decisión final.

<details>
<summary>Ver prompt sugerido</summary>

> Estoy aprendiendo el sistema de archivos de Unix en un curso de bioinformática. Ya creé a mano, en
> `[SERVIDOR]` bajo `[RUTA]`, esta estructura de proyecto: `proyecto/` con `README.md`, `data/source`,
> `data/processed`, `src`, `results` y `doc`. Propón los comandos para **crear y verificar** esa misma
> estructura y explica cómo comprobar que quedó bien. No incluyas datos sensibles ni ejecutes nada; solo
> propón comandos. Señala si algún comando podría sobrescribir o borrar archivos. Presenta el resultado
> como una tabla con columnas "comando", "qué hace" y "riesgo".

</details>

> **IMPORTANTE:** No ejecutes un comando sugerido por la IA sobre tu `proyecto/` solo porque parezca
> correcto. En esta actividad la IA funciona como **revisora**, no como operadora del servidor. Todo lo
> que valides, pruébalo antes en `prueba-s4/`.

## Los cuatro principios, hechos observables en S4

Estos cuatro principios (Unidad 1) se distinguen entre sí; **no** son sinónimos:

- **Reproducibilidad:** registra en `protocolo.md` las **rutas, comandos, decisiones y resultados**, de
  modo que otra persona pueda recrear la estructura.
- **Verificación:** comprueba que el árbol quedó como esperabas (`tree`/`ls -R`) y que el archivo no
  cambió (**checksum antes/después** de copiar `pacientes.md`).
- **Validación:** contrasta la **sintaxis y el comportamiento** de un comando con `man`, con la lección
  y con una **prueba controlada** en `prueba-s4/`.
- **Robustez:** llega **al mismo directorio por dos rutas** —una absoluta y otra relativa—, comprueba
  ambas con `pwd` y confirma que el resultado es el mismo.

## Errores frecuentes y cómo diagnosticarlos

| Síntoma | Causa probable | Cómo diagnosticar / corregir |
| --- | --- | --- |
| `No such file or directory` | Ruta mal escrita o punto de partida equivocado | Ejecuta `pwd` y `ls`; revisa si la ruta es relativa o absoluta |
| Las carpetas no quedan anidadas | `mkdir` sin `-p`, o `cd` en el lugar equivocado | Usa `mkdir -p a/b/c`; verifica con `tree`/`ls -R` |
| `mkdir: cannot create ... No such file or directory` | Falta el directorio padre | Crea el padre primero o usa `mkdir -p` |
| `cp: omitting directory 'template'` o la copia queda vacía | Copiaste una carpeta con `cp` sin `-r` | Usa `cp -r` para copiar carpetas completas (p. ej. `cp -r template proyecto`) |
| `mv` "desapareció" un archivo | `mv` renombró o movió a otro sitio | Revisa el destino; recuerda que `mv` mueve **y** renombra |
| Sobrescribí un archivo sin querer | `cp`/`mv` sin `-i` | Usa siempre `cp -i` y `mv -i`; conserva la copia provisional hasta verificar |
| `rmdir: Directory not empty` | La carpeta tiene contenido | Borra su contenido con `rm -i` y luego `rmdir` (no adoptes `rm -ri` como rutina) |
| Los checksums no coinciden | El archivo cambió o se copió mal | No uses el archivo; vuelve a copiar desde el original y verifica |
| Quedé atrapado dentro de `vi` | Abriste `vi` por accidente | Pulsa `Esc`, escribe `:q!` y Enter para salir sin guardar |

## Evidencia de aprendizaje

**Estructura reproducible del proyecto** en el servidor (Tarea 3): una **plantilla `template/`**
reutilizable clonada con `cp -r` a **`proyecto/`**, con los archivos de S2–S3 en su lugar, la salida de
`tree`/`ls -R`, el **checksum** que confirma que `pacientes.md` no cambió, el registro de comandos y la
sección nueva de `doc/protocolo.md`. Como evidencia complementaria,
`bitacora-ia.md` registra la Actividad formativa de IA. Una captura de pantalla, por sí sola, **no**
sustituye ninguna de estas evidencias.

## Rúbricas

> **Cómo se evalúa cada momento.** El **primer intento** y la **participación** son **formativos** (dan
> puntos por preparación y por corrección argumentada). La **Tarea 3** (entrega posterior) lleva la
> **calificación principal**. La **Actividad formativa de IA** es formativa. Tres niveles:
> **Logrado**, **Parcialmente logrado**, **Aún no logrado**.

### Primer intento (formativa · puntos por preparación)

| Criterio | Logrado | Parcialmente logrado | Aún no logrado |
| --- | --- | --- | --- |
| Revisión del diseño de S2 | Retoma la estructura diseñada y decide dónde va cada archivo | Retoma el diseño parcialmente | No lo retoma |
| Intento de creación | Intenta `proyecto/` y al menos `data/source/` paso a paso | Intento incompleto | Sin intento |
| Registro de comandos y errores | Anota comandos, errores y ≥1 duda concreta | Registro parcial | Sin registro |

### Participación y corrección durante el taller (formativa)

| Criterio | Logrado | Parcialmente logrado | Aún no logrado |
| --- | --- | --- | --- |
| Comprobación de contexto | Usa `hostname`/`whoami`/`pwd` antes de operar | Lo hace a veces | No comprueba el contexto |
| Corrección argumentada | Detecta y corrige sus errores explicando por qué | Corrige sin justificar | No corrige |
| Práctica segura | Usa `-i` y practica borrado solo en `prueba-s4/` | Cumple en parte | Opera sin cuidado |

### Tarea 3 — estructura del proyecto en el servidor (entrega final)

| Criterio | Logrado | Parcialmente logrado | Aún no logrado |
| --- | --- | --- | --- |
| Plantilla y clonado | Crea `template/` reutilizable (estructura + `doc/protocolo.md`) y la clona con `cp -r template proyecto` | Crea la estructura pero sin plantilla o sin clonar con `cp -r` | No usa plantilla ni `cp -r` |
| Estructura canónica | `proyecto/` con `README.md`, `data/source`, `data/processed`, `src`, `results`, `doc` correctamente anidados | Falta alguna carpeta o anidación incorrecta | Sin estructura o desordenada |
| Ubicación de los archivos de S2–S3 | Mueve los datos a `data/source/` y coloca protocolo y bitácora en `doc/` | Algún archivo mal ubicado | Archivos sueltos o ausentes |
| Verificación de integridad | Incluye checksum de `pacientes.md` y lo compara con S3; coinciden | Calcula sin comparar | No verifica |
| Verificación del árbol | Incluye salida de `tree`/`ls -R` que confirma la estructura | Verifica parcialmente | No verifica |
| Registro y protocolo | `doc/protocolo.md` con comandos, problemas y conclusión de reproducibilidad | Registro incompleto | Sin registro |
| Navegación con rutas | Documenta acceso por ruta absoluta y relativa al mismo archivo | Usa solo un tipo | No documenta navegación |

### Actividad formativa de IA

| Criterio | Logrado | Parcialmente logrado | Aún no logrado |
| --- | --- | --- | --- |
| Prompt y anonimización | Prompt con contexto, objetivo, formato y criterios; datos sustituidos por `[SERVIDOR]`/`[USUARIO]`/`[RUTA]` | Prompt incompleto o anonimización parcial | Sin criterios o comparte datos sensibles |
| Comparación comando por comando | Compara y detecta eficientes/riesgosos/incorrectos | Compara sin analizar riesgos | Acepta la IA sin comparar |
| Validación independiente | Valida con `man` y en `prueba-s4/` | Valida parcialmente | No valida |
| Registro en `bitacora-ia.md` | Entrada completa (prompt, verificación, correcciones, decisión) | Entrada incompleta | Sin registro |

## Autoevaluación — semáforo de salida

- 🟢 **Verde:** creé la plantilla `template/`, la cloné con `cp -r` a `proyecto/`, moví cada archivo de
  S2–S3 a su lugar, transferí `bitacora-ia.md`, verifiqué el árbol y el checksum coincidió con el de S3.
- 🟡 **Amarillo:** creé y cloné la estructura, pero dudo de la ubicación de algún archivo, de la
  verificación de integridad o de distinguir rutas relativas y absolutas.
- 🔴 **Rojo:** no logré crear la plantilla o clonarla; llevo mis comandos y el error al taller.

## Distribución orientativa de las dos horas (120 min)

| Tiempo | Actividad |
| ---: | --- |
| 0–10 min | Recuperación de S2–S3: diseño del proyecto, archivos transferidos y problema conductor |
| 10–25 min | Árbol, raíz, *home* y espacio institucional; rutas absolutas y relativas |
| 25–35 min | Micropráctica 1: reconocer contexto y navegar (rutas absolutas y relativas) |
| 35–50 min | Crear la plantilla `template/` y construir la estructura completa (+ `doc/protocolo.md`) |
| 50–65 min | Micropráctica 2: copiar, mover, renombrar y `cp -r` en `prueba-s4/` (con `-i`) |
| 65–85 min | Clonar `template`→`proyecto` (`cp -r`), mover los datos (`mv -i`) y transferir `bitacora-ia.md` (`scp`/`rsync`) |
| 85–100 min | Verificación: árbol (`tree`/`ls -R`) e integridad (checksum de `pacientes.md`) |
| 100–110 min | Práctica segura de `rm -i`/`rmdir` en `prueba-s4/`; edición de `protocolo.md` con `nano` |
| 110–117 min | Diagnóstico de errores frecuentes |
| 117–120 min | Semáforo de salida y registro de dudas |

> **NOTA — reparto del tiempo.** Son estimaciones; ajústalas al ritmo del grupo. La **Actividad
> formativa de IA** y su registro en `bitacora-ia.md` se realizan **después** de la sesión.

## Preparación para la siguiente sesión (S5)

Ya tienes tu proyecto organizado en el servidor. En **S5** trabajarás **dentro** de esos archivos: los
identificarás y visualizarás, ampliarás la edición con `nano`, los comprimirás, y aprenderás a leer y
cambiar **permisos** y a controlar **procesos**. Lee el módulo
[S5 — Archivos, permisos y procesos](u2-s5-archivos-permisos-procesos.md) e intenta un primer
acercamiento a un archivo con `file` y `head`.

## Anexo A. Correspondencia resultado–actividad–evidencia–criterio–momento–nivel

**Nivel en S4:** *comprensión* (se entiende), *ejecución* (se realiza en esta sesión).

| Resultado de aprendizaje | Actividad | Evidencia | Criterio (rúbrica) | Momento | Nivel en S4 |
| --- | --- | --- | --- | --- | --- |
| RA1 Árbol, `/`, `~`, actual; home genérico vs. institucional | §1; recuperación en taller | Explicación en `protocolo.md`; uso correcto de `/export/space3/users/$USER` | Tarea 3 (estructura) | Taller | comprensión |
| RA2 Rutas absolutas y relativas; `.`, `..`, `~` | §2–§3; Micropráctica 1 | Registro de navegación por ambos tipos de ruta | Tarea 3 (navegación) | Taller/entrega | ejecución |
| RA3 Navegar con `pwd`/`ls`/`cd` tras comprobar contexto | Micropráctica 1; taller | Comandos con `hostname`/`whoami`/`pwd` | Participación | Taller | ejecución |
| RA4 Crear y organizar (`cp -r` incluido); eliminar seguro | §4–§6; Microprácticas 2–3 | Operaciones en `prueba-s4/` documentadas | Participación (práctica segura) | Taller | ejecución |
| RA5 Crear la plantilla `template/`, clonarla con `cp -r` y colocar los archivos de S3 | Práctica S4 (Tarea 3) | `template/` + `proyecto/` clonado + archivos en su lugar | Tarea 3 (plantilla, estructura y ubicación) | Entrega | ejecución |
| RA6 Verificar árbol e integridad | Práctica S4, pasos 9–10 | Salida de `tree`/`ls -R` + checksum comparado con S3 | Tarea 3 (verificación) | Entrega | ejecución |
| RA7 Transferir con `scp`/`rsync` | §9; Práctica S4, paso 8 | `bitacora-ia.md` presente en el servidor | Tarea 3 (ubicación) | Taller/entrega | ejecución |
| RA8 Editar con `nano`; usar IA de forma crítica | §10; Actividad formativa de IA | `README.md`/`protocolo.md` editados; entrada en `bitacora-ia.md` | Actividad IA | Después | ejecución |

## Anexo B. Alineación transversal

| Resultado de la sesión | Práctica | Evidencia | Reproducibilidad | Verificación | Validación | Robustez |
| --- | --- | --- | --- | --- | --- | --- |
| Construir y organizar la estructura (RA5) | Práctica S4 (Tarea 3) | `template/` + `proyecto/` + archivos ubicados | La plantilla `template/` y los comandos en `protocolo.md` permiten **recrear** la estructura tantas veces como haga falta | Confirmar el árbol con `tree`/`ls -R` | La estructura corresponde al diseño de S2 | Llegar al mismo directorio por ruta absoluta y relativa |
| Preservar el dato original (RA6) | Pasos 7–9 | Checksum de `pacientes.md` | Original intacto en `data/source/`, copias aparte | Comparar checksum antes/después | El dato conservado sigue siendo el de S3 | Copiar (no mover) hasta verificar |
| Operar con seguridad (RA4, RA7) | Microprácticas 2–3; §9 | Registro de operaciones seguras | Registro reproducible de cada operación | Probar en `prueba-s4/` | Contrastar sintaxis con `man` | Comprobar contexto con `hostname`/`whoami`/`pwd` |
| Usar IA de forma crítica (RA8) | Actividad formativa de IA | Entrada en `bitacora-ia.md` | Prompt y decisión registrados | Validar con `man` y prueba controlada | Confirmar que la propuesta resuelve la tarea | Comparar la solución manual con la de IA |

> **NOTA:** Cuando aún no sea posible una comprobación completa de robustez, basta una actividad
> inicial: llegar a un mismo directorio por dos rutas distintas y comparar `pwd`, o copiar en lugar de
> mover para conservar el original mientras verificas.

## Glosario (español–inglés)

| Español | Inglés | Definición breve |
| --- | --- | --- |
| Sistema de archivos | File system | Organización jerárquica de archivos y directorios. |
| Raíz | Root (`/`) | Directorio del que cuelga todo el árbol. |
| Directorio personal | Home directory (`~`) | Carpeta propia del usuario. |
| Directorio actual | Current/working directory | Lugar donde estás parado (lo da `pwd`). |
| Ruta absoluta | Absolute path | Ruta que parte de `/`. |
| Ruta relativa | Relative path | Ruta que parte del directorio actual. |
| Directorio padre | Parent directory (`..`) | El directorio inmediatamente superior. |
| Checksum / suma de verificación | Checksum | Huella del contenido de un archivo para comprobar integridad. |
| Editor de texto de terminal | Terminal text editor | Programa para editar archivos desde la línea de comandos (p. ej. `nano`, `vi`). |

## Referencias

- Buffalo, V. (2015). *Bioinformatics Data Skills*. O'Reilly Media. — Cap. 3 (navegación y manipulación
  de archivos y directorios). Lectura **base** de S4. Disponible en
  [`bioinformatics-data-skills.pdf`](../introBioInfo/referencias/bioinformatics-data-skills.pdf).
- Shotts, W. E. (2019). *The Linux Command Line: A Complete Introduction* (2ª ed.). No Starch Press.
  Caps. 2–4 (moverse por el sistema de archivos; explorar; manipular archivos y directorios). Lectura
  de **consulta**. Edición libre en línea: <https://linuxcommand.org/tlcl.php>
- Noble, W. S. (2009). A Quick Guide to Organizing Computational Biology Projects. *PLoS Computational
  Biology*, 5(7), e1000424. <https://doi.org/10.1371/journal.pcbi.1000424> — organización de proyectos
  y conservación de datos originales.

> **NOTA — sobre la lectura del plan.** El plan operativo asigna a S4 la consulta previa "L3-shell,
> diapositivas 39–60". Este módulo **sustituye** esas diapositivas como lectura previa autocontenida:
> cúbrelo completo como lectura obligatoria. Buffalo Cap. 3 es la lectura **base** (obligatoria
> adicional) y Shotts es de **consulta**.
