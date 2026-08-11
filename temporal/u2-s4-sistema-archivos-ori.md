# Unidad 2 · Módulo S4 — El sistema de archivos

> **NOTA — Lectura previa (aula invertida).** Este documento se lee **antes de la sesión S4**. En el
> taller construiremos en vivo la estructura del proyecto sobre el servidor, con repetición del
> estudiante. Trae tu **primer intento** y tus dudas. Al final hay una **práctica** con tres momentos.

Segundo módulo de la [Unidad 2](u2-entorno-unix-hpc.md). Ya sabes conectarte y transferir (S3); ahora
aprenderás a **moverte por el sistema de archivos** y a **crear y organizar** archivos y directorios
para levantar la **estructura canónica del proyecto** en tu espacio del servidor.

## Ficha del módulo

| Elemento | Descripción |
| --- | --- |
| **Sesión** | S4 (2 h) |
| **Tema** | Sistema de archivos, navegación y operaciones |
| **Competencia** | B — Dominio del entorno Unix y del cómputo científico |
| **Resultado (plan)** | Navega el sistema de archivos y opera archivos y directorios |
| **Lectura base** | Buffalo (2015), Cap. 3; Shotts (2019), caps. de navegación y manipulación de archivos |
| **Tarea del plan** | **Tarea 3** — estructura de directorios del proyecto en el servidor |
| **Evidencia** | Estructura reproducible del proyecto y registro de comandos |

## Relación con la Unidad 1 y con el proyecto integrador

En la Unidad 1 diseñaste la **organización de un proyecto reproducible** (Noble, 2009). Aquí la
**materializas** en el servidor: creas las carpetas reales donde vivirán tus datos, scripts y
resultados durante todo el curso. La estructura que construyas hoy es la que usarás en las Unidades 3
a 6.

## Resultados de aprendizaje de la sesión

Al terminar S4, el estudiante es capaz de:

1. **Describir** la estructura en árbol del sistema de archivos y el papel de `/`, `~` y el directorio
   actual.
2. **Distinguir** rutas absolutas y relativas y **usar** `.`, `..` y `~`.
3. **Navegar** entre directorios con `pwd`, `ls` y `cd` usando ambos tipos de ruta.
4. **Crear y operar** con archivos y directorios (`mkdir`, `touch`, `cp`, `mv`) y **eliminar** de forma
   segura (`rm -i`, `rmdir`).
5. **Construir y verificar** la estructura canónica del proyecto con `tree` o `ls -R`.

## Antes de la sesión

| Elemento | Detalle |
| --- | --- |
| **Lectura obligatoria** | Este módulo completo. |
| **Preparación técnica** | Conéctate al servidor (habilidad de S3). Ten a la vista la estructura del proyecto de la Unidad 1. |
| **Primer intento** | Esboza —en papel o en un bloque de código— la estructura de directorios del proyecto e intenta crear al menos `data/source/`. |
| **Producto para el taller** | Tu primer intento de la estructura y las dudas encontradas. |
| **Tiempo estimado** | Lectura ~40 min · primer intento ~25 min. |

---

## 1. La estructura en árbol

En Unix, archivos y directorios (carpetas) se organizan en una **jerarquía en forma de árbol** que
empieza en la **raíz**, representada por `/`. De la raíz cuelgan directorios, que a su vez contienen
otros directorios y archivos.

![Árbol del sistema de archivos que parte de la raíz e incluye el directorio home del usuario y las subcarpetas del proyecto.](images/figura-u2-arbol-sistema-archivos.png)

*Figura 1. El sistema de archivos como árbol: todo cuelga de la raíz `/`; tu directorio personal y las carpetas del proyecto son ramas de ese árbol.*

Conceptos clave:

- **Directorio raíz `/`:** el origen de todo el árbol.
- **Directorio *home* (`~`):** tu carpeta personal, donde tienes permisos para trabajar.
- **Directorio actual:** el lugar donde "estás parado" en este momento (lo consultas con `pwd`).
- **Ruta (*path*):** la dirección de un archivo dentro del árbol.

> **NOTA — home genérico vs. espacio institucional.** En ejemplos genéricos verás `/home/usuario` como
> directorio personal. En el servidor del curso, tu espacio de trabajo **no** está en `/home` sino en
> `/export/space3/users/$USER`. La variable `$USER` se reemplaza automáticamente por tu nombre de
> usuario. Cuando trabajes en el servidor, usa **tu espacio institucional**.

## 2. Rutas absolutas y relativas

- **Ruta absoluta:** parte desde la raíz `/` y **siempre apunta al mismo lugar**, sin importar dónde
  estés. Ej.: `/export/space3/users/$USER/proyecto/data`.
- **Ruta relativa:** parte **desde tu directorio actual** (no desde `~`). Ej.: si estás en
  `.../proyecto`, la ruta relativa `data/source` apunta a `.../proyecto/data/source`.

Símbolos útiles en las rutas:

- `.` : el directorio actual.
- `..` : el directorio padre (uno hacia arriba).
- `~` : tu directorio *home*.

![Comparación entre una ruta absoluta que parte de la raíz y una ruta relativa que parte del directorio actual.](images/figura-u2-rutas-absolutas-relativas.png)

*Figura 2. Rutas absolutas y relativas: la absoluta parte de `/`; la relativa parte de donde estás ahora.*

> **IMPORTANTE:** Una ruta **relativa** empieza en tu **directorio actual**, no necesariamente en tu
> *home* (`~`). Si te confundes de punto de partida, terminarás creando carpetas donde no querías.
> Ante la duda, ejecuta `pwd` para saber dónde estás.

## 3. Navegar: `pwd`, `ls`, `cd`

El siguiente bloque muestra los comandos para orientarte y moverte:

```bash
pwd                 # muestra dónde estás (ruta absoluta actual)
ls                  # lista el contenido del directorio actual
ls -lah             # lista con detalle (l), ocultos (a) y tamaños legibles (h)
cd carpeta          # entra a "carpeta" (ruta relativa)
cd /ruta/absoluta   # entra usando una ruta absoluta
cd ..               # sube al directorio padre
cd ~                # va a tu home
cd -                # regresa al directorio anterior
```

> **TIP:** `ls -lh` muestra los tamaños en formato legible (KB, MB, GB) y `cd -` te devuelve al
> directorio donde estabas antes. Combina Tab para autocompletar rutas y evitar errores de tipeo.

## 4. Crear y operar con archivos y directorios

El siguiente bloque reúne las operaciones básicas:

```bash
mkdir nueva          # crea el directorio "nueva"
mkdir -p a/b/c       # crea toda la ruta anidada de una vez
touch archivo.txt    # crea un archivo vacío (o actualiza su fecha)
cp origen destino    # copia
cp -r carpeta destino  # copia una carpeta y su contenido
mv origen destino    # mueve o renombra (según el destino)
```

- `mkdir -p` crea **directorios anidados** en un solo paso (útil para `data/source`).
- `cp` copia; `cp -r` copia carpetas completas.
- `mv` **mueve** o **renombra**: si el destino es otra carpeta, mueve; si es un nombre nuevo en el
  mismo lugar, renombra.

## 5. Eliminar de forma segura

```bash
rm archivo           # borra un archivo   (¡sin papelera!)
rm -i archivo        # pide confirmación antes de borrar
rmdir carpeta        # borra un directorio VACÍO
```

> **ADVERTENCIA:** En Unix **no hay papelera**: `rm` borra de forma permanente e inmediata. Ten
> especial cuidado con `rm -r` (borra un directorio y **todo** su contenido). Verifica siempre qué vas
> a borrar antes de ejecutar.

> **TIP:** Mientras te acostumbras, usa `rm -i`: te **pedirá confirmación** por cada archivo. Es una
> red de seguridad. `rmdir` solo borra carpetas vacías, así que evita borrar contenido por accidente.

## 6. Ver el árbol: `tree` o `ls -R`

Para comprobar que tu estructura quedó como esperabas:

```bash
tree              # muestra el árbol de directorios (si está instalado)
ls -R             # lista recursivamente el contenido (alternativa siempre disponible)
```

Si `tree` no está disponible en el servidor, `ls -R` cumple la misma función de verificación.

## 7. La estructura canónica del proyecto

Usaremos **la misma** estructura de la Unidad 1 (Noble, 2009), sin variaciones:

```text
proyecto/
├── data/
│   ├── source/      # datos originales, inmutables
│   └── processed/   # datos derivados
├── src/             # scripts
├── results/         # resultados del análisis
└── doc/             # documentación (protocolo, bitácora, README)
```

> **IMPORTANTE — datos originales intactos.** Los datos originales se conservan en `data/source/`
> **sin modificarse**: se leen y se copian, pero no se editan. Cualquier transformación produce
> archivos nuevos que van a `data/processed/` u otra carpeta, nunca encima del original. Así preservas
> la trazabilidad de tu análisis.

---

## Práctica S4 — Estructura de directorios del proyecto (Tarea 3)

> **Regla — primero a mano, luego con IA.** Primero construyes la estructura **tú**, paso a paso.
> Después la comparas con una propuesta de IA en la **Actividad formativa de IA**. Tu trabajo manual
> es la **línea base** de la comparación.

### Antes de clase (primer intento)

1. Conéctate al servidor y ubícate en tu espacio de trabajo (`/export/space3/users/$USER`).
2. Con `mkdir` (y `touch` para un `README.md`), intenta crear la **estructura canónica** de arriba,
   creando **primero** `data/` y dentro `source/` y `processed/`. Hazlo **paso a paso**, no de memoria.
3. Anota los comandos que usaste y cualquier duda.

### Durante el taller

Con repetición guiada:

1. Construimos la estructura **paso a paso**, verificando con `pwd` y `ls` en cada nivel.
2. **Navegamos** entre las carpetas usando rutas **absolutas** y **relativas** (y `.`, `..`, `~`).
3. **Verificamos** el árbol con `tree` (o `ls -R`).
4. Comparamos estrategias y corregimos errores frecuentes (rutas mal escritas, carpetas mal anidadas).

### Después del taller (entrega final) — Tarea 3

Entrega:

- la **estructura del proyecto** creada en tu espacio del servidor, con `data/source/` y
  `data/processed/` correctamente anidados;
- la **salida de `tree`** (o `ls -R`) que muestra el árbol;
- el **registro de los comandos** usados, en tu bitácora/protocolo.

### Actividad formativa de IA — crear la estructura, ahora con IA

> **NOTA:** Se llama **Actividad formativa de IA** (no "Tarea A") para no confundirla con las tareas
> oficiales del plan. Es formativa: su valor está en la comparación, no en una calificación aparte.

1. Prompt sugerido:
   > "En Linux, dame los comandos para crear, dentro de mi carpeta actual, esta estructura:
   > `data/source`, `data/processed`, `src`, `results`, `doc`. Explícame cada comando y cómo verifico
   > que se creó correctamente."
2. **Compara** con lo que hiciste a mano: ¿usó los mismos comandos?, ¿propuso algo más eficiente (por
   ejemplo, `mkdir -p` para varias carpetas de una vez)?, ¿algún comando es **riesgoso** (por ejemplo,
   un `rm -r` innecesario)? Verifícalo con `man`.
3. **Identifica** qué comandos son eficientes y cuáles riesgosos, y registra en tu `bitacora-ia.md` el
   prompt, la respuesta y tu validación.

## Errores frecuentes y cómo diagnosticarlos

| Síntoma | Causa probable | Cómo diagnosticar / corregir |
| --- | --- | --- |
| `No such file or directory` | Ruta mal escrita o punto de partida equivocado | Ejecuta `pwd` y `ls`; revisa si la ruta es relativa o absoluta |
| Las carpetas no quedan anidadas | `mkdir` sin `-p`, o `cd` en el lugar equivocado | Usa `mkdir -p a/b/c`; verifica con `tree`/`ls -R` |
| `mv` "desapareció" un archivo | `mv` renombró o movió a otro sitio | Revisa el destino; recuerda que `mv` mueve **y** renombra |
| `rmdir: Directory not empty` | La carpeta tiene contenido | Vacíala primero o usa `rm -ri` con cuidado |

## Evidencia de aprendizaje

**Estructura reproducible del proyecto** en el servidor (Tarea 3), con la salida de `tree`/`ls -R` y
el registro de comandos.

## Criterios de logro

| Criterio | Logrado | Parcialmente logrado | Aún no logrado |
| --- | --- | --- | --- |
| Estructura canónica | `data/source`, `data/processed`, `src`, `results`, `doc` correctamente anidados | Falta alguna carpeta o anidación incorrecta | Sin estructura o desordenada |
| Navegación con rutas | Usa rutas absolutas y relativas con soltura | Usa solo un tipo con dudas | No navega con seguridad |
| Verificación del árbol | Incluye salida de `tree`/`ls -R` que confirma la estructura | Verifica parcialmente | No verifica |
| Registro de comandos | Comandos exactos documentados | Registro incompleto | Sin registro |
| Actividad formativa de IA | Compara, detecta comandos eficientes/riesgosos y valida con `man` | Compara sin validar | Acepta la IA sin comparar |

## Autoevaluación — semáforo de salida

- 🟢 **Verde:** creé la estructura, navego con rutas absolutas y relativas y verifiqué con `tree`.
- 🟡 **Amarillo:** creé la estructura pero me confundo entre rutas relativas y absolutas.
- 🔴 **Rojo:** no logré anidar bien las carpetas; llevo mis comandos y el error al taller.

## Preparación para la siguiente sesión (S5)

Ya tienes tu proyecto organizado en el servidor. En **S5** trabajarás **dentro** de esos archivos:
los identificarás, visualizarás, editarás, comprimirás y aprenderás a leer y cambiar **permisos** y a
controlar **procesos**. Lee el módulo [S5 — Archivos, permisos y procesos](u2-s5-archivos-permisos-procesos.md)
e intenta un primer acercamiento a un archivo con `file` y `head`.

## Alineación resultado–actividad–evidencia–criterio

| Resultado de aprendizaje | Actividad | Evidencia | Criterio de logro |
| --- | --- | --- | --- |
| Distinguir rutas absolutas/relativas | §2; navegación en taller | Registro de navegación | Usa ambos tipos correctamente |
| Navegar el sistema de archivos | Práctica S4, taller | Comandos en la bitácora | Se mueve con `pwd`/`ls`/`cd` con seguridad |
| Operar archivos y directorios | Práctica S4, primer intento y taller | Estructura creada | Crea/mueve/copia sin borrar por error |
| Construir y verificar la estructura | Práctica S4 (Tarea 3) | Árbol + salida de `tree` | Estructura canónica verificada |

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

## Referencias

- Buffalo, V. (2015). *Bioinformatics Data Skills*. O'Reilly Media. — Cap. 3. Disponible en
  `referencias/bioinformatics-data-skills.pdf`.
- Shotts, W. E. (2019). *The Linux Command Line* (2ª ed.). No Starch Press.
- Noble, W. S. (2009). A Quick Guide to Organizing Computational Biology Projects. *PLoS Computational
  Biology*, 5(7), e1000424. doi:10.1371/journal.pcbi.1000424.
