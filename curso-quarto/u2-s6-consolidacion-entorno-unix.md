# S6 — Consolidar: el entorno Unix listo para datos biológicos

::: {.callout-note title="Aula invertida"}
Este documento se lee **antes de la sesión S6**. No introduce
herramientas nuevas: usa las de S3, S4 y S5 para responder una pregunta distinta. Antes del taller
harás un **primer intento** de inventario de tus evidencias; durante la sesión comprobarás cada una
sobre el servidor y corregirás lo que falte; después entregarás la **evidencia de cierre de la
Unidad 2** en `doc/protocolo.md`.
:::

Cuarto y último módulo de la [Unidad 2](u2-entorno-unix.md). En S3 te conectaste y transferiste; en
S4 construiste la estructura del proyecto; en S5 aprendiste a inspeccionar, comprimir, ajustar
permisos y controlar procesos. Hoy no vas a construir nada nuevo: vas a **demostrar que lo construido
está bien**, y a dejar el proyecto en condiciones de recibir datos que no inventaste tú.

## Ficha del módulo

| Elemento | Descripción |
| --- | --- |
| **Sesión** | S6 (2 h) |
| **Tema** | Consolidación del entorno Unix y preparación para datos biológicos |
| **Competencias** | B — Dominio del entorno Unix y del cómputo científico; A — Trabajo reproducible y comunicación científica |
| **Resultado (plan)** | Consolida las evidencias de S3–S5 y deja listo el proyecto para comenzar a trabajar con datos biológicos reales |
| **Consulta previa (plan)** | Repaso de S3–S5 y cierre de la Unidad 2 |
| **Lectura base** | Este módulo + los módulos S3, S4 y S5 (secciones indispensables) |
| **Caso conductor** | Demostrar, con evidencia comprobable, que tu proyecto en el servidor está íntegro, organizado, protegido y documentado |
| **Evidencia** | Evidencia de cierre de U2: proyecto verificado + registros de S3–S5 completos en `doc/protocolo.md` |
| **Ajuste integrado** | **[Reubicado]** el trabajo con cluster y SGE ya no se imparte aquí; se desarrolla en **S29** |

::: {.callout-important title="qué NO es esta sesión"}
No es un repaso ni un examen sorpresa. Es la diferencia
entre *«me funcionó»* y *«puedo demostrar que funciona»*. Esa diferencia es el corazón de la
reproducibilidad, y se practica aquí por primera vez sobre algo que construiste tú.
:::

## Relación con lo anterior

Cada sesión de esta unidad te dejó un producto y una deuda:

| Sesión | Qué construiste | Qué quedó sin comprobar |
| --- | --- | --- |
| S3 | Conexión por SSH y transferencia de tres archivos | Si puedes reconectar **sin ayuda** y si los archivos **siguen** íntegros semanas después |
| S4 | La estructura `~/proyecto/` con los archivos colocados | Si el árbol real coincide con el que **crees** tener |
| S5 | Inspección, compresión, permisos y procesos | Si los permisos actuales son los **mínimos** y si los originales siguen intactos tras haber practicado sobre ellos |

Las tres deudas tienen la misma forma: **hiciste algo y no volviste a mirarlo**. En un proyecto de dos
semanas eso no se nota. En un análisis que dura meses, es la causa más común de resultados que no se
pueden reproducir.

::: {.callout-note}
En S5 practicaste con copias precisamente para no tocar los originales. Hoy lo
**compruebas**: la política de datos deja de ser una regla que te dijeron y pasa a ser una
afirmación que puedes sostener con evidencia.
:::

## Resultados de aprendizaje

Al terminar S6, el estudiante es capaz de:

1. **Distinguir** una afirmación sobre su entorno de la evidencia que la sostiene.
2. **Restablecer** el acceso al servidor de forma autónoma y **describir** el entorno en el que
   trabaja.
3. **Comparar** la estructura real de su proyecto con la estructura declarada, y **explicar** cualquier
   diferencia.
4. **Demostrar** que los datos originales no han cambiado, mediante una comprobación de integridad
   registrada y repetible.
5. **Justificar** los permisos vigentes de cada archivo en términos del **permiso mínimo necesario**.
6. **Comprobar** que su `protocolo.md` permite a otra persona repetir el procedimiento, y **corregir**
   lo que impida hacerlo.
7. **Preparar** el proyecto para recibir datos externos, reconociendo qué información le faltará
   cuando los datos no sean suyos.

## Antes de empezar: lista de verificación

Marca cada punto antes del taller. Si alguno falla, **no lo resuelvas todavía**: anótalo, es
exactamente el material de la sesión.

- [ ] Tienes a mano las credenciales del servidor y sabes cómo conectarte.
- [ ] Conservas `doc/protocolo.md` con los registros de S3, S4 y S5.
- [ ] Recuerdas dónde anotaste los *checksums* que calculaste en S3.
- [ ] Tienes en tu equipo las copias locales de `pacientes.md` y `pacientes-metadatos.md`.
- [ ] Has hecho el **primer intento** de la Práctica 1.

## Ruta de S6

| Momento | Trabajo | Producto |
| --- | --- | --- |
| Antes de clase | Leer §1 y hacer la Práctica 1 (inventario declarado, **sin conectarte**) | Tabla de afirmaciones |
| Durante el taller | §2–§7 con sus prácticas: comprobar cada afirmación sobre el servidor | Tabla contrastada y correcciones aplicadas |
| Después del taller | §8–§9: cerrar el protocolo y entregar | Evidencia de cierre de U2 |

---

## 1. Una afirmación no es una evidencia [Indispensable]

Cuando alguien pregunta si tu proyecto está bien, hay tres respuestas posibles, y solo una sirve:

| Respuesta | Qué es | Vale como evidencia |
| --- | --- | --- |
| «Sí, lo hice en S4.» | Un **recuerdo** | No |
| «Sí, la carpeta `data/source/` está ahí.» | Una **afirmación** | No |
| «Sí: aquí está la salida de `ls -R ~/proyecto` y aquí el `sha256sum` que coincide con el que anoté en S3.» | Una **evidencia** | Sí |

La diferencia no es de rigor personal, sino de **verificabilidad**: la tercera respuesta puede
comprobarla otra persona sin creerte, y puedes comprobarla tú misma dentro de seis meses, cuando ya no
recuerdes nada.

Esta sesión convierte, una por una, tus afirmaciones sobre el entorno en evidencias registradas.

::: {.callout-note}
La verificación tiene un coste, y por eso conviene hacerla bien: se verifica **lo que
sostiene una conclusión**, no todo. En este proyecto sostienen conclusiones cuatro cosas: el acceso,
la estructura, la integridad de los originales y el registro. Son las cuatro que comprobarás hoy.
:::

### Práctica 1 — Lo que crees que tienes *(antes de clase, primer intento)*

**Sin conectarte al servidor**, y **sin consultar tus apuntes**, completa esta tabla de memoria:

| Afirmación | Tu respuesta de memoria | ¿Con qué lo comprobarías? | Comprobado (taller) |
| --- | --- | --- | --- |
| Ruta absoluta de mi proyecto en el servidor | | | |
| Número de directorios dentro de `proyecto/` | | | |
| Archivos que hay en `data/source/` | | | |
| Archivos que hay en `doc/` | | | |
| Permisos actuales de `data/source/pacientes.md` | | | |
| ¿Hay algún archivo con permiso de ejecución? ¿Cuál y por qué? | | | |
| ¿Sigue `pacientes.md` idéntico al de tu equipo? | | | |

**Entrega.** La tabla con las dos primeras columnas llenas. **No la corrijas antes del taller**: su
valor está en la diferencia entre lo que creías y lo que hay.

::: {.callout-tip}
Si en la columna «¿con qué lo comprobarías?» te quedas en blanco en alguna fila, márcala.
Esa fila es la que más vas a aprender hoy.
:::

---

## 2. Verificar el acceso: reconectar sin ayuda [Indispensable]

En S3 te conectaste acompañada. Hoy la pregunta es otra: **¿puedes hacerlo sola?** Y una vez dentro,
**¿sabes dónde estás?**

Tres comandos responden a lo segundo, y conviene ejecutarlos siempre al entrar:

```bash
hostname     # en qué máquina estoy
whoami       # con qué usuario
pwd          # en qué directorio me dejó la conexión
```

Parecen triviales y evitan el error más caro del curso: **ejecutar en la máquina equivocada**. Un `rm`
lanzado en tu equipo creyendo estar en el servidor, o al revés, no tiene deshacer.

::: {.callout-warning}
Si `hostname` no devuelve el nombre del servidor del curso, **estás en tu propia
máquina**. Detente y vuelve a conectarte antes de ejecutar cualquier otra cosa.
:::

### Práctica 2 — Entrar y situarse *(durante el taller)*

1. **Cierra** cualquier sesión abierta con `exit`.
2. **Conéctate** desde cero, sin mirar los apuntes de S3. Si no puedes, míralos: el objetivo es
   detectar qué no recordabas, no aprobar un examen.
3. **Sitúate.** Ejecuta los tres comandos y copia la salida al protocolo.
4. **Compara.** ¿La ruta que devuelve `pwd` coincide con la que escribiste de memoria en la Práctica 1?
5. **Documenta.** Anota cuántos intentos necesitaste y qué te faltó recordar.

<details>
<summary>Ver retroalimentación</summary>

Lo esperable es que `pwd` al entrar te deje en tu ***home***, es decir `/home/tu-usuario` o similar,
**no** dentro de `~/proyecto/`. Una conexión siempre te deja en el *home*; llegar al proyecto es un
paso que haces tú.

Si en la Práctica 1 escribiste `~/proyecto` como respuesta a «ruta absoluta», la respuesta es
**incompleta**: `~` es una abreviatura que el shell expande, no una ruta absoluta. La ruta absoluta
empieza por `/` y es la que devuelve `pwd` una vez dentro del directorio.

Que hayas necesitado consultar los apuntes no es un problema: lo que se evalúa es que sepas **qué**
consultar. No recordar la sintaxis exacta es normal; no saber que existe `hostname` sí es una laguna
que conviene cerrar hoy.

</details>

---

## 3. Verificar la estructura: que el árbol sea el que dices [Indispensable]

En S4 construiste la estructura. Pero entre S4 y hoy hubo una sesión entera de prácticas (S5) en la
que creaste copias, comprimiste archivos y ejecutaste un script. Es muy probable que el árbol real
**ya no sea** el que dibujaste.

Eso no está mal: un proyecto vivo acumula archivos. Lo que está mal es **no saberlo**.

Para ver el árbol completo de una vez:

```bash
ls -R ~/proyecto
```

`ls -R` recorre el directorio y todos sus subdirectorios (*recursive*). Es la forma más directa de
comparar lo que hay con lo que declaraste, usando solo lo que ya conoces.

La estructura declarada en la Unidad 1 y construida en S4 es:

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

::: {.callout-note title="archivos que aparecen solos"}
Verás cosas que no pusiste ahí a propósito: restos de las
prácticas de S5, copias de trabajo, algún `.tar.gz`. Cada uno merece una decisión explícita:
**conservarlo** (y decir para qué), **moverlo** a donde corresponda, o **eliminarlo**. Lo que no vale
es dejarlo sin decidir: dentro de tres meses no sabrás si es importante.
:::

### Práctica 3 — El árbol real frente al declarado *(durante el taller)*

1. **Predice.** Antes de ejecutar nada, escribe cuántos archivos crees que hay dentro de `~/proyecto/`.
2. **Localiza.** Ejecuta `ls -R ~/proyecto` y copia la salida completa al protocolo.
3. **Contrasta.** Marca en la salida: (a) lo que coincide con la estructura declarada, (b) lo que
   sobra, (c) lo que falta.
4. **Decide.** Para cada elemento que sobre, escribe una línea: `conservar porque…`, `mover a…` o
   `eliminar porque…`. Aplica solo las decisiones de las que estés segura.
5. **Documenta.** Registra la diferencia entre tu predicción y el número real.

::: {.callout-warning}
No elimines nada de `data/source/`. Si algo te sobra ahí, anótalo y consúltalo: es
el único directorio del proyecto donde borrar tiene consecuencias irreversibles para tu evidencia.
:::

<details>
<summary>Ver retroalimentación</summary>

Casi todo el mundo predice **menos** archivos de los que hay. Lo habitual tras S5 es encontrar entre
tres y seis elementos no declarados: la copia de `README.md` que hiciste para practicar compresión, el
`.tar.gz` resultante, el script de prueba en `src/`, y a veces un archivo restaurado con otro nombre.

Los tres directorios que aparecen **vacíos** —`data/processed/`, `results/` y `src/`, si no dejaste el
script— no son un error: están reservados. `ls -R` los muestra sin contenido y así debe ser hasta la
Unidad 3, cuando `data/processed/` empiece a recibir archivos derivados.

Si te falta `bitacora-ia.md` en `doc/`, es la deuda que S4 dejó abierta: ese archivo vivía en tu
equipo y había que transferirlo. Transferirlo ahora es la corrección correcta, y conviene registrarla
como tal en el protocolo, no hacerla en silencio.

</details>

---

## 4. Verificar los originales: el checksum como prueba, no como ritual [Indispensable]

En S3 calculaste un *checksum* de `pacientes.md` en tu equipo y otro en el servidor, y comprobaste que
coincidían. Eso demostró que la **transferencia** fue correcta. No demuestra nada sobre lo que pasó
después.

La pregunta de hoy es distinta y más importante: **¿siguen los originales como estaban?** Entre medias
hubo una sesión completa manipulando archivos.

Recuerda cómo se calcula:

```bash
sha256sum ~/proyecto/data/source/pacientes.md
sha256sum ~/proyecto/data/source/pacientes-metadatos.md
```

Comparar esas cadenas a ojo contra las que anotaste en S3 funciona con dos archivos, pero no escala y
es propenso a error. Conviene dar un paso más.

### Herramienta mínima: un archivo de sumas

**Sintaxis mínima**

```bash
cd ~/proyecto/data/source
sha256sum pacientes.md pacientes-metadatos.md > ../../doc/checksums-u2.txt
sha256sum -c ../../doc/checksums-u2.txt
```

**¿Qué hace?** La primera orden guarda las sumas en un archivo de texto. La segunda las vuelve a
calcular y compara cada una con la guardada, respondiendo `OK` o `FAILED` por archivo.

**¿Por qué aparece en esta sesión?** Porque comparar cadenas a ojo no es reproducible: depende de tu
atención. Un archivo de sumas convierte la comprobación en algo que **cualquiera** puede repetir con
una sola orden, hoy o dentro de un año.

::: {.callout-tip title="prompt al asistente del curso"}
*«Explícame qué significa cada columna de la salida de
`sha256sum -c` y qué causas puede tener un `FAILED` que no sea corrupción del archivo.»* Contrasta la
respuesta con `man sha256sum` antes de darla por buena.
:::

::: {.callout-important}
El archivo de sumas se guarda en `doc/`, **no** en `data/source/`. Es documentación
que tú generas, no un dato original.
:::

### Práctica 4 — Demostrar que los originales no cambiaron *(durante el taller)*

1. **Recupera** del protocolo de S3 los *checksums* que anotaste entonces.
2. **Calcula** de nuevo las sumas de los dos archivos de `data/source/`.
3. **Compara** con las de S3. ¿Coinciden?
4. **Construye** el archivo `doc/checksums-u2.txt` con la sintaxis mínima de arriba.
5. **Comprueba** con `sha256sum -c` y copia la salida al protocolo.
6. **Interpreta.** Escribe una frase que empiece por: *«Puedo afirmar que los datos originales no han
   cambiado desde S3 porque…»*.

<details>
<summary>Ver retroalimentación</summary>

Lo esperado es que las sumas **coincidan** y que `sha256sum -c` devuelva:

```text
pacientes.md: La suma coincide
pacientes-metadatos.md: La suma coincide
```

(o `OK` en lugar de `La suma coincide`, según el idioma configurado en el sistema).

Si alguna **no** coincide, no supongas corrupción. Por orden de probabilidad, las causas son:

1. **Abriste el archivo con `nano` y guardaste sin querer.** `nano` puede añadir un salto de línea
   final. Basta con eso para cambiar la suma por completo: un *checksum* no mide «cuánto» cambió un
   archivo, solo si cambió.
2. **Copiaste el checksum de S3 con un espacio o carácter de más** al pegarlo en el protocolo.
3. **Estás comparando archivos distintos**: por ejemplo, el del *home* contra el de `data/source/`.

La corrupción real en una transferencia local es rarísima. Si descartas las tres causas anteriores,
restaura el archivo desde tu copia local y **registra el incidente** en el protocolo: una limitación
declarada es evidencia de buen trabajo, no de mal trabajo.

Sobre la frase final: *«…porque el `sha256sum` calculado hoy coincide con el que registré en S3, y la
comprobación queda automatizada en `doc/checksums-u2.txt`»* es una respuesta completa.
*«…porque no los toqué»* no lo es: eso es un recuerdo, no una evidencia.

</details>

---

## 5. Verificar permisos: el mínimo necesario [Indispensable]

En S5 aprendiste que un permiso se concede porque hace falta, no por si acaso. Hoy revisas si el
estado actual de tu proyecto lo refleja.

```bash
ls -l ~/proyecto/data/source/
ls -l ~/proyecto/src/
```

La regla es corta:

| Tipo de archivo | Permiso esperado | Por qué |
| --- | --- | --- |
| Datos originales (`data/source/`) | lectura; **sin ejecución** | No son programas y no deben modificarse |
| Documentación (`doc/`) | lectura y escritura del dueño | Son documentos vivos que corriges |
| Scripts (`src/`) | ejecución **solo si se ejecutan** | El permiso mínimo que la tarea requiere |

::: {.callout-warning}
Un archivo `.md` con permiso de ejecución no es peligroso por sí mismo, pero es una
**señal**: indica que en algún momento aplicaste `chmod` a más archivos de los que pretendías. Vale
la pena averiguar cuándo pasó.
:::

### Práctica 5 — Justificar cada permiso *(durante el taller)*

1. **Localiza.** Ejecuta los dos `ls -l` y copia las salidas.
2. **Clasifica.** Para cada archivo, escribe qué permisos tiene y **por qué los necesita**.
3. **Detecta.** Marca cualquier archivo cuyos permisos no puedas justificar.
4. **Corrige** con `chmod` simbólico, cambiando **solo** lo que sobra, y vuelve a ejecutar `ls -l`
   para comprobar el efecto.
5. **Documenta** cada cambio: qué archivo, qué permiso retiraste o añadiste y con qué argumento.

<details>
<summary>Ver retroalimentación</summary>

El caso más frecuente es un archivo de datos o de documentación con `x` en los permisos del dueño
(`-rwxr--r--` en lugar de `-rw-r--r--`). Se corrige con:

```bash
chmod u-x ~/proyecto/data/source/pacientes.md
```

El segundo caso frecuente es el contrario: el script de S5 en `src/` **sin** permiso de ejecución,
porque lo restauraste desde el archivo comprimido y la restauración no siempre conserva el bit de
ejecución. Se corrige con `chmod u+x`.

Fíjate en que ambas correcciones usan notación **simbólica** (`u-x`, `u+x`) y afectan a **un** archivo.
Si te ves escribiendo `chmod` sobre un directorio completo, detente: casi siempre significa que no has
identificado qué archivo concreto tiene el problema.

Un permiso que **no** debes «corregir» es el de lectura para grupo y otros (`r--r--`) en tus archivos
de trabajo: en el servidor del curso es el estado normal y retirarlo no aporta seguridad real a datos
sintéticos. El criterio es el permiso mínimo **necesario para la tarea**, no el mínimo posible.

</details>

---

## 6. Verificar el registro: ¿puede otra persona repetirlo? [Indispensable]

Los cinco puntos anteriores comprueban el **entorno**. Este comprueba el **documento**, y es el que
distingue un proyecto reproducible de uno que simplemente funcionó una vez.

Un `protocolo.md` sirve si otra persona, con tus mismas credenciales y sin hablar contigo, puede
llegar al mismo estado. Los fallos típicos no son de contenido, sino de **contexto ausente**:

| Fallo | Cómo se ve | Por qué rompe la repetición |
| --- | --- | --- |
| Comandos sin decir dónde se ejecutan | `sha256sum pacientes.md` | ¿En el equipo o en el servidor? ¿Desde qué directorio? |
| Resultados sin el comando que los produjo | Una cadena de 64 caracteres suelta | No se sabe cómo obtenerla otra vez |
| Decisiones sin argumento | «Cambié los permisos» | No se sabe a qué ni por qué |
| Rutas que solo existen en tu equipo | `/Users/ana/Escritorio/…` | Nadie más las tiene |
| Credenciales escritas | Usuario y contraseña en el texto | **Nunca**: se retiran de inmediato |

::: {.callout-warning title="credenciales"}
Si encuentras una contraseña en tu protocolo, elimínala ahora y
avisa a quien imparte el curso. Un protocolo se comparte; una contraseña no.
:::

### Práctica 6 — Leer el protocolo de otra persona *(durante el taller)*

Trabaja en parejas. Cada quien lee el protocolo del otro **sin preguntar nada**.

1. **Intenta seguirlo.** Marca la primera instrucción que no puedas ejecutar por falta de información.
2. **Clasifica** cada problema según la tabla anterior.
3. **Devuelve** a tu pareja tres observaciones concretas, en forma de pregunta: *«¿dónde se ejecuta
   esto?»*, *«¿de dónde sale este número?»*, *«¿por qué esta decisión y no otra?»*.
4. **Corrige** tu propio protocolo a partir de lo que te devolvieron. No discutas las observaciones:
   si tu pareja no lo entendió, algo falta.
5. **Documenta** qué cambiaste y por qué.

::: {.callout-note}
Esta es la primera revisión por pares del curso, y es deliberadamente corta. En S16 harás
una revisión completa, con criterios explícitos y dictamen escrito. Aquí solo practicas la
experiencia básica: **descubrir que lo obvio para ti no lo es para nadie más**.
:::

---

## 7. Preparar el espacio para datos que no son tuyos [Indispensable]

Hasta ahora todos tus datos fueron **sintéticos**: `pacientes.md` tiene tres registros que se
inventaron para el curso. Los conoces enteros, caben en pantalla y no tienen historia.

En la Unidad 3 llegan datos **reales**: un genoma descargado de una base pública. Y con ellos, tres
diferencias que cambian cómo hay que trabajar:

| | Datos sintéticos (U1–U2) | Datos reales (U3 en adelante) |
| --- | --- | --- |
| **Tamaño** | Caben en pantalla | Millones de líneas; no se abren enteros |
| **Origen** | Los hiciste tú | Vienen de una base pública, con versión y fecha |
| **Confianza** | Sabes qué contienen | Hay que comprobar qué contienen y si llegaron completos |

De ahí sale lo único que hay que preparar hoy: un lugar donde ponerlos y la costumbre de anotar de
dónde vienen.

::: {.callout-note title="dónde irán los datos grandes"}
Los archivos de esta unidad son pequeños y viven en tu
*home*. Cuando los genomas lo justifiquen, el curso usará el espacio institucional
`/export/space3/users/$USER`. **Hoy no lo necesitas** y no debes usarlo todavía.
:::

### Práctica 7 — Dejar el proyecto listo *(durante el taller)*

1. **Comprueba** que `data/processed/` y `results/` existen y están vacíos. Si no existen, créalos.
2. **Actualiza** `README.md` con `nano`: qué contiene el proyecto, cómo está organizado y qué
   representa cada directorio. Dos o tres frases por directorio bastan.
3. **Anticipa.** Escribe en el protocolo, bajo el título *Preguntas abiertas para U3*, tres cosas que
   no sabrías comprobar de un archivo que no hiciste tú.
4. **Verifica** por última vez con `ls -R ~/proyecto` que el árbol es el que declaras en `README.md`.

<details>
<summary>Ver retroalimentación</summary>

Las tres preguntas de la actividad 3 no tienen una respuesta única, pero las más productivas suelen
girar en torno a:

- **Procedencia:** ¿de qué base salió, qué versión es y en qué fecha se descargó? Sin eso, el análisis
  no se puede repetir aunque los comandos sean perfectos.
- **Integridad:** el `sha256sum` que calculas tú solo demuestra que el archivo no cambió **después** de
  llegar. Para saber si llegó completo hace falta una suma **publicada por la fuente**.
- **Contenido:** si el archivo tiene millones de líneas, `cat` deja de servir. ¿Cómo miras un archivo
  que no cabe en pantalla, y cómo sabes cuántos registros tiene realmente?

Las tres son exactamente las preguntas que abren la Unidad 3. Si llegaste a alguna por tu cuenta, has
entendido para qué servía esta sesión.

</details>

---

## 8. Lo que ya puedes afirmar, y lo que todavía no [Indispensable]

**Puedes afirmar, con evidencia:**

- que accedes al servidor de forma autónoma y sabes reconocer dónde estás;
- que tu proyecto tiene la estructura declarada, y que cada elemento no declarado tiene una decisión
  escrita;
- que los datos originales no han cambiado desde S3, y que cualquiera puede comprobarlo con una orden;
- que cada permiso vigente responde a una necesidad que puedes justificar;
- que tu procedimiento es repetible por otra persona, porque alguien lo intentó.

**Todavía no puedes:**

- comprobar la integridad de un archivo contra una suma **publicada por su fuente** —hasta ahora
  siempre comparaste contra ti misma—;
- describir el contenido de un archivo que no cabe en pantalla;
- documentar la procedencia de un dato que no produjiste tú.

Esas tres carencias no son un fallo de esta sesión: son su resultado. El entorno ya está listo; **lo
que falta ahora son los datos**, y con ellos empieza la Unidad 3.

---

## 9. Documentar: la sección del protocolo [Indispensable]

Añade a `doc/protocolo.md` un apartado nuevo. **No reescribas** los de S3, S4 y S5: se conservan tal
como quedaron, y las correcciones de hoy se registran aquí, indicando qué corrigen.

```markdown
## Unidad 2 · S6 — Cierre y verificación del entorno

### Estado verificado
- Acceso: (salida de hostname, whoami, pwd)
- Estructura: (salida de ls -R y diferencias con la estructura declarada)
- Integridad de originales: (salida de sha256sum -c)
- Permisos: (salida de ls -l y justificación por archivo)

### Diferencias encontradas entre lo declarado y lo real

### Correcciones aplicadas
(qué se corrigió, en qué sesión se había originado y con qué argumento)

### Revisión por pares
(observaciones recibidas y cambios que produjeron)

### Limitaciones
(qué no se pudo comprobar y por qué)

### Preguntas abiertas para U3
```

::: {.callout-important}
El apartado *Diferencias encontradas* no debe quedar vacío. Si de verdad no hubo
ninguna, escríbelo explícitamente junto con la evidencia que lo respalda. Un apartado en blanco no se
distingue de un apartado sin hacer.
:::

## Evidencia de la sesión

| Elemento | Dónde | Qué demuestra |
| --- | --- | --- |
| Tabla de la Práctica 1, con la columna «comprobado» llena | `doc/protocolo.md` | Distinción entre afirmación y evidencia |
| Salidas de `ls -R`, `sha256sum -c` y `ls -l` | `doc/protocolo.md` | Verificación del entorno |
| `doc/checksums-u2.txt` | `doc/` | Comprobación de integridad repetible |
| Registro de correcciones | `doc/protocolo.md` | Trazabilidad de los cambios |
| `README.md` actualizado | Raíz del proyecto | El proyecto se explica solo |
| Preguntas abiertas para U3 | `doc/protocolo.md` | Reconocimiento de los límites actuales |

Esta es la **evidencia de cierre de la Unidad 2** que pide el plan de clases.

## Errores frecuentes y estrategias de diagnóstico

| Error | Síntoma | Diagnóstico |
| --- | --- | --- |
| Ejecutar en la máquina equivocada | El comando funciona pero no encuentra los archivos | `hostname` y `pwd` antes de nada |
| Corregir sin registrar | El árbol queda bien pero el protocolo no lo explica | Toda corrección lleva una línea en *Correcciones aplicadas* |
| Confundir `~` con ruta absoluta | La ruta anotada no funciona para otra persona | `pwd` dentro del directorio da la ruta real |
| `sha256sum -c` con rutas relativas | `FAILED open or read` | El archivo de sumas guarda las rutas tal como se escribieron: ejecuta `-c` desde el mismo directorio |
| `chmod` sobre un directorio entero | Cambian permisos que no querías tocar | Identifica el archivo concreto; usa notación simbólica |
| Borrar lo que «sobra» sin mirar | Se pierde evidencia de S5 | Decide primero por escrito, aplica después |
| Dejar el protocolo sin limitaciones | Todo parece perfecto | Un trabajo sin limitaciones declaradas está incompleto, no perfecto |

## Rúbricas

### Primer intento (Práctica 1) — formativo

| Nivel | Descriptor |
| --- | --- |
| Logrado | Completa la tabla de memoria y propone una comprobación plausible para cada fila |
| Parcialmente logrado | Completa la tabla pero deja sin proponer comprobación en varias filas |
| Aún no logrado | Consulta los apuntes o el servidor para rellenarla, perdiendo el contraste |

### Participación en el taller — formativo

| Nivel | Descriptor |
| --- | --- |
| Logrado | Comprueba cada afirmación, detecta diferencias y las argumenta; da y recibe revisión por pares con observaciones concretas |
| Parcialmente logrado | Comprueba pero no interpreta las diferencias, o participa en la revisión de forma genérica |
| Aún no logrado | Ejecuta los comandos sin contrastarlos con su tabla inicial |

### Evidencia de cierre de U2 — calificada

| Criterio | Logrado | Parcialmente logrado | Aún no logrado |
| --- | --- | --- | --- |
| Verificación del entorno | Las cuatro comprobaciones están, con su salida | Faltan una o dos | Hay afirmaciones sin salida que las respalde |
| Integridad | Demuestra que los originales no cambiaron y deja la comprobación automatizada | Compara a ojo, sin archivo de sumas | No comprueba integridad |
| Justificación de permisos | Cada permiso tiene un argumento en términos de necesidad | Justifica algunos | Enumera permisos sin justificarlos |
| Trazabilidad de correcciones | Cada corrección dice qué arregla y de dónde venía | Registra el cambio sin su origen | Corrige en silencio |
| Repetibilidad | Otra persona siguió el protocolo e identificó los puntos ciegos, que fueron corregidos | Hubo revisión pero sin corrección posterior | No hubo revisión |
| Límites declarados | Declara qué no pudo comprobar y qué le faltará en U3 | Menciona límites de forma vaga | No declara límites |

## Autoevaluación

Responde con sí, parcialmente o todavía no:

- ¿Sé distinguir una afirmación sobre mi entorno de la evidencia que la sostiene?
- ¿Puedo conectarme al servidor y situarme sin ayuda?
- ¿Coincide el árbol real de mi proyecto con el que declaro, y sé explicar cada diferencia?
- ¿Puedo demostrar —no afirmar— que mis datos originales no han cambiado?
- ¿Sé justificar por qué cada archivo tiene los permisos que tiene?
- ¿Alguien más siguió mi protocolo y llegó al mismo sitio?
- ¿Sé decir qué no podré comprobar cuando los datos no sean míos?

Si respondes «todavía no» a la cuarta o a la sexta, revísalas antes de empezar la Unidad 3: son las
dos que U3 da por adquiridas.

## Distribución estimada de las dos horas

| Bloque | Actividad | Tiempo |
| --- | --- | ---: |
| Apertura | Contraste de las tablas de la Práctica 1 en grupo | 10 min |
| Bloque 1 | §2–§3 con Prácticas 2 y 3: acceso y estructura | 30 min |
| Bloque 2 | §4 con Práctica 4: integridad y archivo de sumas | 25 min |
| Bloque 3 | §5 con Práctica 5: permisos | 20 min |
| Bloque 4 | §6 con Práctica 6: revisión por pares | 20 min |
| Cierre | §7 con Práctica 7 y preguntas abiertas para U3 | 15 min |

## Anexo A. Correspondencia resultado–actividad–evidencia–criterio

| Resultado | Actividad | Evidencia | Criterio | Momento |
| --- | --- | --- | --- | --- |
| 1. Distinguir afirmación de evidencia | Práctica 1 | Tabla contrastada | Propone comprobación para cada afirmación | Antes / taller |
| 2. Restablecer el acceso | Práctica 2 | Salidas de `hostname`, `whoami`, `pwd` | Se conecta y se sitúa sin ayuda | Taller |
| 3. Comparar estructura real y declarada | Práctica 3 | Salida de `ls -R` y decisiones escritas | Explica cada diferencia | Taller |
| 4. Demostrar integridad | Práctica 4 | `checksums-u2.txt` y salida de `-c` | La comprobación es repetible por terceros | Taller |
| 5. Justificar permisos | Práctica 5 | Salidas de `ls -l` y argumentos | Aplica el criterio de permiso mínimo | Taller |
| 6. Comprobar repetibilidad | Práctica 6 | Observaciones recibidas y correcciones | Corrige a partir de la lectura ajena | Taller |
| 7. Preparar para datos externos | Práctica 7 | `README.md` y preguntas abiertas | Identifica qué información le faltará | Taller / después |

## Anexo B. Alineación transversal

| Práctica | Reproducibilidad | Verificación | Validación | Robustez |
| --- | --- | --- | --- | --- |
| P2 Acceso | Procedimiento repetible sin ayuda | `hostname` confirma la máquina | — | Detecta el error de máquina equivocada |
| P3 Estructura | Árbol declarado y real coinciden | `ls -R` como prueba | Contraste con la estructura de U1 | Decisión explícita sobre lo no declarado |
| P4 Integridad | Archivo de sumas reutilizable | `sha256sum -c` | Contraste con el registro de S3 | Diagnóstico de causas de un `FAILED` |
| P5 Permisos | Cambios registrados | `ls -l` antes y después | Criterio de permiso mínimo | Cambio acotado a un archivo |
| P6 Revisión | Protocolo ejecutable por terceros | Otra persona lo intenta | Evidencia externa e independiente | Corrección a partir del fallo ajeno |
| P7 Preparación | Estructura lista para U3 | `ls -R` final | — | Anticipa límites del entorno |

## Glosario

| Español | Inglés | Nota |
| --- | --- | --- |
| suma de verificación | *checksum* | Cadena que resume el contenido de un archivo |
| integridad | *integrity* | Que el contenido no ha cambiado |
| ruta absoluta | *absolute path* | Empieza en la raíz `/` |
| permiso mínimo | *least privilege* | Conceder solo lo que la tarea requiere |
| recursivo | *recursive* | Que recorre también los subdirectorios |
| revisión por pares | *peer review* | Lectura crítica por otra persona |
| dato sintético | *synthetic data* | Generado para practicar, no observado |
| procedencia | *provenance* | Origen, versión y fecha de un dato |

## Referencias

- Buffalo, V. (2015). *Bioinformatics Data Skills*, cap. 2 y 3. O’Reilly Media.
- Noble, W. S. (2009). A quick guide to organizing computational biology projects. *PLoS
  Computational Biology*, 5(7), e1000424. <https://doi.org/10.1371/journal.pcbi.1000424>
- Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible
  computational research. *PLoS Computational Biology*, 9(10), e1003285.
  <https://doi.org/10.1371/journal.pcbi.1003285>
- Shotts, W. E. (2019). *The Linux Command Line* (2.ª ed.), caps. 9 y 10. No Starch Press.
- Wilson, G., et al. (2017). Good enough practices in scientific computing. *PLoS Computational
  Biology*, 13(6), e1005510. <https://doi.org/10.1371/journal.pcbi.1005510>
