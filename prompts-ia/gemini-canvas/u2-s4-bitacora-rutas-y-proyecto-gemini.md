# Prompt maestro — Gemini Canvas

Construye una única aplicación web educativa, autónoma y completamente funcional, para acompañar la Sesión 4 del curso **Introducción a la Bioinformática, LCG UNAM 2026**.

Devuélveme un único archivo HTML completo. La aplicación será una **bitácora interactiva de decisiones** para S4: ayuda a pensar, predecir, comprobar en la terminal real, corregir y registrar evidencia breve. No es un simulador de terminal ni sustituye las herramientas reales.

## Restricciones técnicas innegociables

- Debe funcionar completamente offline: incluye todo el HTML, CSS y JavaScript en el mismo archivo.
- Cero dependencias externas: no React, Tailwind, Bootstrap, CDN, Google Fonts, Font Awesome, scripts remotos, APIs, backend, login, tracking ni recursos externos.
- Usa JavaScript nativo y `localStorage`; no dependas de archivos externos.
- La interfaz debe abrirse y conservar diseño y funciones sin Internet.

## Contexto pedagógico

Las y los estudiantes están en primer semestre de la Licenciatura en Ciencias Genómicas. Acaban de aprender en S3 a conectarse por SSH, transferir archivos y comparar checksums. En S4 aprenden a orientarse dentro del sistema de archivos Unix, construir la estructura real de su proyecto en el servidor y organizar archivos ya existentes.

S4 es la fuente pedagógica principal. No adelantes contenidos posteriores ni incluyas ejemplos de RNA-seq, pipelines, programación, bases de datos, genómica avanzada ni herramientas no presentadas. Usa únicamente los elementos de esta sesión: `proyecto`, `README.md`, `data/source`, `data/processed`, `src`, `results`, `doc`, `pacientes.md`, `pacientes-metadatos.md`, `protocolo.md`, `bitacora-ia.md`, rutas Unix, SSH, `scp`, `nano`, `tree`/`ls -R` y checksums.

El lenguaje debe ser sencillo, directo y adecuado para estudiantes que están comenzando. Di “carpeta” antes que “directorio” cuando ayude; conserva los nombres técnicos cuando se usan en Unix. No uses frases grandilocuentes o tecnicismos innecesarios.

## Propósito de la app

La app acompaña las microprácticas de S4 y la Tarea 3 sin hacer el trabajo por el estudiante. Debe apoyar este ciclo:

**observar → pensar → decidir → comprobar → recibir retroalimentación → corregir → justificar → documentar**.

La terminal, SSH, `scp`, `nano`, `tree`/`ls -R`, `sha256sum` y la IA se usan en sus herramientas reales. La app no debe fingir su salida ni pedir contraseñas, servidores, cuentas, IP, rutas reales, llaves ni datos sensibles.

El resultado es una única experiencia continua, con navegación libre, formada por estas pestañas:

1. `Inicio`
2. `1. Árbol y rutas`
3. `2. Comprueba en Unix`
4. `3. Organiza con cuidado`
5. `4. Verifica y documenta`
6. `5. Revisión con IA`
7. `✓ Resumen`

No bloquees pestañas por progreso. La persona puede avanzar, volver, explorar, corregir y abrir el resumen en cualquier momento.

## Identidad visual y accesibilidad

En el encabezado muestra:

`[ LCG UNAM 2026 ]   Introducción a la Bioinformática • Sesión 4 • Navegar y organizar el proyecto`

Usa una apariencia universitaria moderna, sobria y clara: azul oscuro institucional, acento dorado, fondos claros, contraste alto, tarjetas discretas, texto legible y código monoespaciado. No infantilices la interfaz.

Implementa HTML semántico, `label` asociado a cada campo, `fieldset` y `legend` para grupos de opciones, foco visible, navegación por teclado y regiones `aria-live` para el feedback. Las pestañas deben tener `role="tablist"`, `role="tab"`, `role="tabpanel"` y `aria-selected`. Nunca comuniques corrección solo con color.

## Estado inicial y persistencia

- Ninguna respuesta, radio, checkbox o selector debe estar preseleccionado.
- Los selectores comienzan con `Selecciona...`.
- No muestres aciertos, errores ni colores de corrección antes de que la persona pulse un botón de comprobación.
- Implementa una función central `activateTab(tabName)` y persiste la pestaña activa.
- Persiste en `localStorage` las decisiones, respuestas, intentos, pistas usadas, correcciones, reflexiones, estados y la pestaña activa.
- Incluye `Reiniciar práctica`, con confirmación, que borre únicamente el estado de esta app y deje la interfaz en estado inicial.
- Debe tolerar respuestas incompletas sin errores de JavaScript.

## Economía de interacción

No pidas que la persona copie cada comando ni registre todo lo que hizo. Registra solamente una decisión, una evidencia breve, una dificultad, una corrección o una reflexión que aporte aprendizaje.

Todos los placeholders deben ser neutrales: no reveles en un placeholder, ejemplo o ayuda visual la respuesta que se debe descubrir. No rellenes campos con comandos, permisos, nombres de ruta, usuarios, fechas, tamaños o respuestas correctas.

En actividades con decisión y evidencia, el feedback debe comparar explícitamente **la decisión de la persona** con **la evidencia que ella observó**. No te limites a mostrar la respuesta correcta. El patrón es: **DECIDIR → COMPROBAR → FEEDBACK → PISTA → CORREGIR**. La pista debe orientar sin regalar la solución.

## Contenido y comportamiento de cada pestaña

### Inicio

Explica en pocas líneas el reto real: los archivos de S3 quedaron juntos en el *home* del servidor; hoy se creará `~/proyecto/`, se organizarán los archivos y se comprobará que `pacientes.md` no cambió.

Muestra el árbol final, solo como mapa de referencia:

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

Aclara con una llamada breve: **la app ayuda a razonar; las acciones se realizan en la terminal real.**

### 1. Árbol y rutas

Esta es la micropráctica conceptual central. Usa un árbol visual legible basado en esta parte real de S4:

```text
~/
└── proyecto/
    ├── README.md
    ├── data/
    │   ├── source/
    │   │   └── pacientes.md
    │   └── processed/
    ├── src/
    ├── results/
    └── doc/
        └── protocolo.md
```

El árbol puede resaltar visualmente la ubicación actual y el destino de cada reto, pero no debe revelar la ruta ni la respuesta antes de la comprobación. Mantén siempre visible una leyenda sencilla: “Estás aquí”, “Destino” y “La ruta relativa empieza donde estás”.

Incluye exactamente los retos A–F siguientes, sin añadir retos ni teoría adicional:

**A. Me ubico en el árbol**

Situación: `Estás aquí: ~/proyecto/data/source/`.

Pide responder, con controles adecuados y sin pistas-respuesta previas:

1. ¿En qué carpeta estás?
2. ¿Qué carpeta está inmediatamente arriba?
3. ¿Qué archivo aparece dentro de la carpeta donde estás?
4. Si escribieras ahora una ruta relativa, ¿desde qué carpeta comenzaría a interpretarse?

Al comprobar, muestra feedback específico de orientación. Solo después de intentar permite una pista que dirija a observar la posición de `source` en el árbol. Registra las respuestas y si se usó pista.

**B. Subo un nivel**

Situación: desde `~/proyecto/data/source/`, predecir dónde termina `..`. Solicita una decisión antes de comprobar. Si hace falta, da una pista sobre seguir una rama hacia arriba. En la explicación correcta muestra explícitamente el recorrido `source → data`.

**C. Subo varios niveles**

Situación: desde la misma ubicación, interpretar `../..`. Solicita una predicción antes de comprobar. La explicación correcta debe mostrar explícitamente `source → data → proyecto`.

**D. Cambio de rama**

Situación: `Estás aquí: ~/proyecto/doc/`. Destino: `pacientes.md` dentro de `data/source/`.

Pide construir una ruta relativa y explicar cuántos niveles hay que subir y por qué rama bajar. Este razonamiento no debe simplificarse ni resolverse antes del intento. Tras comprobar, una pista puede recordar que primero se ubique en `doc` y localice el punto donde cambia de rama. La retroalimentación final solo se muestra al lograr una respuesta coherente y debe explicar el recorrido `doc → proyecto → data → source → pacientes.md`.

**E. Comparo ruta absoluta y relativa**

Situación: `Estás aquí: ~/proyecto/`. Destino: `data/source/`.

Pide:

1. Construir una ruta relativa hacia el destino.
2. Decidir desde dónde comienza una ruta absoluta.
3. Explicar si una ruta absoluta y una relativa pueden llegar al mismo directorio y por qué.

Aclara únicamente después del intento que la ruta absoluta real se comprobará más tarde con `pwd`; no uses marcadores ficticios como `/ruta/real/de/tu/home/`. En el feedback explica: una ruta absoluta comienza en `/`, una relativa comienza en el directorio actual y ambas pueden señalar el mismo destino. No inventes la ruta real del servidor.

**F. Detecto y corrijo un error**

Situación: `Estás aquí: ~/proyecto/doc/`. Alguien escribió `data/source/pacientes.md` para llegar a `pacientes.md`.

Antes de permitir corregir, pregunta: “¿Desde dónde intentará interpretar Unix esta ruta?” Pide decidir si funciona y explicar la ubicación que se buscaría. La pista debe llevar a mirar la carpeta inicial, no entregar la ruta corregida. Después de una corrección coherente explica que se buscaría dentro de `doc/` y permite registrar la corrección.

Al final de esta pestaña, destaca solo esta frase, sin añadir teoría: **Idea clave: una ruta relativa depende de dónde estás.**

Después de los retos, incluye un bloque de transición no evaluable: “Ahora valida tu modelo mental en la terminal real.” Presenta los comandos reales, claramente como instrucciones para ejecutar fuera de la app:

```bash
cd ..
pwd
cd -
pwd
```

Explica que se comparan las dos salidas de `pwd` y que todavía no se necesita crear `~/proyecto/`.

### 2. Comprueba en Unix

No simules SSH ni una terminal. Presenta una lista breve de acciones reales, con etiquetas `[REMOTO]`, para confirmar contexto antes de crear archivos:

```bash
hostname
whoami
cd ~
pwd
ls -lah
ls -ld /export/space3/users/$USER
```

Pide únicamente tres registros breves que realmente aportan evidencia:

- una confirmación de que comprobó que está en el servidor y con su cuenta;
- si encontró los tres archivos de S3 en el *home* (`pacientes.md`, `pacientes-metadatos.md`, `protocolo.md`);
- una reflexión breve: “¿Qué puedes comprobar ahora en la terminal que antes no sabías comprobar?”

No pidas que copie la ruta del *home*, el usuario ni listados completos. Incluye una nota clara: el *home* y `/export/space3/users/$USER` son ubicaciones diferentes; en S4 se trabaja en el *home*.

### 3. Organiza con cuidado

### 3. Organiza con cuidado

Reúne las Microprácticas 3 y 4 como preparación para acciones reales, sin simular sus efectos.

#### Copiar, mover y renombrar

Primero, presenta el flujo real de prueba en `prueba-s4/` con los comandos de S4:

```bash
mkdir -p prueba-s4
cd prueba-s4
touch a.txt
cp -i a.txt b.txt
mv -i b.txt c.txt
mkdir sub
mv -i c.txt sub/
ls -R
cd ..
```

Incluye una interacción breve de clasificación para comprender `mv -i`.

Usa únicamente estas dos situaciones reales:

```bash
mv -i b.txt c.txt
mv -i c.txt sub/
```

Para cada una, pide decidir qué ocurrirá:

- cambia el nombre;
- cambia la ubicación;
- necesito revisar mejor el origen y el destino.

No preselecciones ninguna respuesta.

Después de decidir, permite **Comprobar**.

El feedback debe explicar brevemente que:

- `mv -i b.txt c.txt` cambia el nombre dentro de la misma carpeta;
- `mv -i c.txt sub/` cambia la ubicación del archivo.

Pregunta una sola vez:

**¿Por qué crees que `-i` puede ser útil cuando estás aprendiendo a mover o renombrar archivos?**

No pidas que copie nuevamente los comandos ni que describa cada paso.

---

#### Eliminar con seguridad

Esta actividad debe reforzar una rutina sencilla antes de borrar:

**¿Dónde estoy? → ¿Qué existe aquí? → ¿Qué quiero borrar? → entonces ejecuto.**

Todo el ejercicio ocurre exclusivamente dentro de `prueba-s4/`.

Antes de borrar, presenta:

```bash
cd prueba-s4
pwd
ls -R
```

Pide decidir:

**¿Qué te permite comprobar cada comando antes de borrar algo?**

El feedback debe relacionar:

- `pwd` con comprobar dónde estás;
- `ls -R` con revisar qué archivos y carpetas existen.

No revelar esta explicación antes de que la persona intente responder.

##### Predice antes de borrar

En este momento `sub/` todavía contiene `c.txt`.

Presenta:

```bash
rmdir sub
```

pero **NO lo muestres como un paso rutinario que simplemente debe ejecutarse**.

Primero pregunta:

**¿Qué crees que ocurrirá si intentas ejecutar `rmdir sub` ahora?**

No preselecciones ninguna respuesta.

La persona debe tomar una decisión antes de ir a la terminal.

Después indica:

> Comprueba tu predicción en la terminal REAL.

Cuando regrese a la app, pregunta brevemente si ocurrió lo que esperaba.

Si su predicción no coincide con lo observado, ofrece primero una pista:

**Observa nuevamente qué contiene `sub/`.**

Permite corregir su respuesta.

Solo después de la comprobación explica que `rmdir` elimina directorios vacíos y que `sub/` todavía contiene `c.txt`.

##### Ahora elimina de forma controlada

Después del experimento anterior, presenta la continuación real:

```bash
rm -i sub/c.txt
rmdir sub
rm -i a.txt
cd ..
```

Haz explícita la secuencia conceptual:

**primero eliminar el archivo → después eliminar la carpeta ya vacía.**

No conviertas esta parte en otro cuestionario largo.

Basta con una comprobación final breve:

**¿Por qué ahora sí puede eliminarse `sub/` con `rmdir`?**

Usa el flujo:

**PREDECIR → EJECUTAR EN TERMINAL REAL → OBSERVAR → COMPROBAR → PISTA SI HACE FALTA → CORREGIR**

Nunca recomiendes `rm -r` o `rm -ri` como rutina ni pidas borrar archivos del proyecto real.

---

#### Antes de trabajar con el proyecto real

Al terminar las dos microprácticas, presenta el mapa de la estructura canónica de S4 y recuerda:

- las pruebas se hicieron en `prueba-s4/`;
- el proyecto real se construye paso a paso en `~/proyecto/`;
- al organizar archivos importantes, primero se copia y se verifica antes de considerar mover;
- `data/source/` contiene datos originales y no debe editarse.

La app debe acompañar estas decisiones, pero **no debe construir una interfaz que parezca ejecutar comandos Unix**.


### 4. Verifica y documenta

Esta pestaña acompaña la Tarea 3 sin cambiarla. Presenta, como lista de verificación de trabajo real:

- crear la estructura directamente dentro de `~/proyecto/`;
- comprobar dos caminos al mismo `data/source/`: uno absoluto obtenido con `pwd` y uno relativo desde `~/proyecto/`;
- comprobar desde `~/proyecto/doc/` la ruta relativa a `pacientes.md`;
- copiar primero los tres archivos de S3 a sus ubicaciones;
- comparar el checksum de `pacientes.md` con el valor registrado en S3;
- transferir `bitacora-ia.md` desde `[LOCAL]` a `~/proyecto/doc/` con `scp`;
- verificar el árbol con `tree` o `ls -R`;
- editar `README.md` y actualizar `doc/protocolo.md` con `nano`.

Incluye dos interacciones breves:

1. **Integridad:** la persona marca si comparó el checksum de S4 con el valor de S3 y decide `Coinciden`, `No coinciden` o `Aún no comparo`. Si decide que no coinciden, el feedback indica detenerse y volver a copiar desde el original, sin borrar copias. Si aún no compara, queda como pendiente. No inventes hashes ni solicites que copie cadenas largas.
2. **Edición con nano:** ordenar el ciclo `abrir → editar → guardar → salir → comprobar fuera del editor`; pedir una sola reflexión: por qué `pacientes.md` no debe abrirse con `nano`. Después de comprobar, explica que es un dato original y que editarlo cambiaría su checksum.

Incluye una tarjeta claramente identificada `[LOCAL]` para `scp` y otra `[REMOTO]` para acciones del servidor. Para `scp`, pide confirmar solo si pudo transferir `bitacora-ia.md` y, si hubo un problema, describirlo brevemente de forma opcional. No pidas datos sensibles ni la ruta absoluta real.

Ofrece un área breve de “Evidencia para mi protocolo” con campos opcionales y neutrales: qué comprobó, problema si ocurrió y cómo lo resolvió. No lo conviertas en una copia de toda la Tarea 3.

### 5. Revisión con IA

Esta actividad se realiza después de construir la estructura manualmente. La IA revisa; no opera el servidor ni reemplaza la solución propia.

Muestra estas instrucciones de seguridad: sustituir datos institucionales por `[SERVIDOR]`, `[USUARIO]` y `[RUTA]`; nunca pegar contraseñas, IP, huellas, llaves o tokens.

Incluye un bloque de prompt sugerido editable, derivado de la sesión, para pedir a una IA que proponga comandos para crear y verificar la misma estructura dentro del *home*, que señale riesgos de sobrescritura o borrado y que no use `/export/space3`. El bloque debe decir explícitamente que la propuesta se valida con `man` y con `prueba-s4/`, nunca directamente sobre `proyecto/`.

La interacción debe pedir solo:

- una observación de la IA que la persona aceptó, rechazó o dejó pendiente;
- cómo la comprobó de manera independiente;
- una decisión final breve.

No presupongas que usó IA ni inventes respuesta alguna. En el resumen, si no hay respuesta, mostrar `Pendiente` o `Sin respuesta`.

### ✓ Resumen

Esta pestaña debe estar siempre accesible y reflejar fielmente el estado real de la app. Organiza en secciones:

- Razonamiento de rutas A–F: respuestas, decisiones, pistas usadas y correcciones.
- Comprobación real en Unix: confirmaciones y reflexión.
- Operaciones cuidadosas: decisiones de `mv`, seguridad de borrado y cualquier dificultad opcional.
- Verificación y documentación: estado de checksum, `scp`, ciclo de `nano` y evidencia breve.
- Revisión con IA: observación, verificación independiente y decisión final.

Para ausencias usa `Sin respuesta`, `Pendiente` o `Aún no comprobado`. Nunca inventes resultados, rutas, hashes ni acciones realizadas.

Muestra estados formativos como `Pendiente`, `Requiere revisar`, `Corregido`, `Comprobado` o `Registrado`; no uses porcentajes, calificaciones, estrellas, rankings ni puntos.

## Descargas Markdown

Incluye siempre el botón **⬇ Descargar resultados de la práctica**. Debe generar un archivo Markdown real usando `Blob`, `URL.createObjectURL` y un enlace `<a download>`, sin backend.

El archivo debe tener un nombre seguro como `bitacora-s4-rutas-y-proyecto.md` e incluir fecha local, título de sesión y todas las secciones del Resumen. Debe conservar las respuestas reales, decisiones iniciales y corregidas cuando existan, uso de pistas, estados pendientes y reflexiones. No debe inventar datos ni incluir información sensible.

Incluye además el botón **⬇ Descargar notas para protocolo.md**, que genere Markdown breve y copiable para la sección de S4 del protocolo: evidencia de rutas, verificación de integridad, comandos o acciones que la persona decidió registrar, problemas y solución, y una conclusión. Si algo no se capturó, debe aparecer como `Pendiente` o `Sin respuesta`.

## Validaciones obligatorias antes de devolver el HTML

Comprueba explícitamente:

- La app abre offline, sin recursos externos y sin errores de JavaScript.
- Las pestañas funcionan con mouse y teclado, hay navegación libre y `✓ Resumen` siempre está disponible.
- El estado inicial no contiene respuestas preseleccionadas ni feedback anticipado.
- `localStorage` conserva pestaña, respuestas, intentos, pistas, correcciones y textos; reiniciar borra solo el estado de esta app tras confirmación.
- La Micropráctica 1 conserva exactamente A–F y su progresión: ubicarme, subir un nivel, subir varios niveles, cambiar de rama, comparar absoluta/relativa y detectar/corregir un error.
- La app no simula la terminal, SSH, `scp`, `nano`, checksums ni IA; orienta a usar las herramientas reales.
- Las pistas no revelan antes de tiempo la solución y el feedback relaciona decisión y evidencia cuando corresponde.
- El lenguaje es claro para primer semestre, los placeholders son neutrales y no se añade contenido posterior a S4.
- Resumen y ambas descargas Markdown reflejan exactamente los datos disponibles, incluidos pendientes y correcciones.

Devuélveme el HTML COMPLETO, autónomo y funcional. No un parche. No fragmentos.
