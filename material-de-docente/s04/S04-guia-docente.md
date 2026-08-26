# S04 — Navegar: el sistema de archivos, su organización y su edición

## Fuente y propósito

- Fuente canónica: `curso-quarto/u2-s4-sistema-archivos.md`.
- Objetivo central: construir y verificar la estructura real `~/proyecto/` en el servidor, sin modificar los datos originales.
- Lectura/exploración previa: módulo S4 completo; Cap. 3 de Buffalo como consulta dirigida; diseño de S2, `protocolo.md` con el checksum de S3 y `bitacora-ia.md` localizada en el equipo local.
- Recursos para el taller: bitácora `curso-quarto/html/u2-s4-sistema-archivos.html`; figuras de árbol/home, rutas y nano del módulo; terminal con acceso al servidor.

## Análisis pedagógico

### Recordar, comprender y hacer

- Recordar: en S3 se transfirieron `pacientes.md`, `pacientes-metadatos.md` y `protocolo.md` al *home*; `bitacora-ia.md` sigue local.
- Comprender: una ruta relativa depende del directorio actual; *home* y `/export/space3/users/$USER` son ramas distintas; copiar y mover no son equivalentes; verificar no es suponer.
- Hacer: comprobar el contexto, construir `~/proyecto/`, navegar por rutas equivalentes, copiar primero, transferir `bitacora-ia.md`, comparar checksum, editar documentación y ensayar borrado solo en `prueba-s4/`.

### Conceptos esenciales y dificultades

Idea intuitiva → término técnico → aplicación: “¿dónde estoy?” → directorio actual/ruta relativa → `pwd` antes de crear, copiar o borrar. “Una dirección completa” → ruta absoluta → llegar a `data/source/` desde cualquier lugar. “Mismo archivo, nuevo lugar” → copia, movimiento e integridad → conservar el original hasta comparar SHA-256.

Dificultades previstas: confundir `~` con el espacio institucional; ejecutar `scp` en el servidor; asumir que `mv` solo renombra; interpretar un error de `rmdir` como falla del sistema; creer que guardar en `nano` prueba que el archivo cambió; usar una ruta relativa sin reconocer el punto de partida.

### Prácticas, decisiones, evidencia y corrección

| Práctica | Acción y decisión | Evidencia | Error productivo y corrección |
|---|---|---|---|
| MP1 rutas | Construir rutas antes de usar la terminal | Respuestas A–F en bitácora | Ruta desde `doc/` sin `..` → identificar dónde buscaría Unix y corregirla |
| MP2 contexto | Comprobar servidor, usuario, home y archivos de S3 | Salidas de `hostname`, `whoami`, `pwd`, `ls -lah` | Tratar home y espacio institucional como iguales → comparar rutas y propósito |
| Tarea 3 | Crear el árbol, copiar archivos y navegar | `tree`/`ls -R`; rutas registradas | Crear proyecto dentro de otro → detenerse, inspeccionar y no duplicar |
| MP3 organizar | Copiar, renombrar y mover en `prueba-s4/` | Árbol con `a.txt` y `sub/c.txt` | Confundir renombrar con mover → comparar origen y destino |
| Integridad/scp | Copiar primero, transferir local→remoto y comparar SHA-256 | Checksum y `bitacora-ia.md` en `doc/` | Usar `$USER` local o mover el original → ruta remota explícita y copia provisional |
| MP5 nano | Abrir, editar, guardar, salir y comprobar | `cat README.md`; protocolo actualizado | Confundir guardar con salir → comprobar fuera del editor |
| MP4 borrar | Ensayar la rutina segura solo en prueba | Primer error de `rmdir`, segundo intento correcto | Usar borrado recursivo → `pwd` + `ls` + `rm -i` + `rmdir` |

### Errores esperados, preguntas y respuestas a reservar

- No revelar la ruta correcta de MP1 hasta que las parejas expliquen el punto de partida.
- Preguntar: “¿Qué evidencia te permite afirmar que estás en el servidor?”; “¿qué ruta intentaría buscar este comando?”; “¿qué no cambió después de copiar?”; “¿qué demuestran dos `pwd` idénticos?”
- No resolver el diagnóstico de `rmdir sub` antes del primer intento. Después conectar el mensaje con el contenido observado.
- Retener el checksum esperado: cada estudiante compara con su propio registro de S3, no con una cadena proyectada.

### Ruta de 120 minutos

La secuencia es: recuperar productos anteriores → predecir rutas → comprobar el contexto real → construir/corregir el proyecto → organizar y transferir → verificar integridad → editar y documentar → practicar eliminación segura → salida breve. La Actividad formativa de IA queda después del taller.

## Mapa del taller

| Tiempo | Momento | Qué hacen los estudiantes | Papel del profesor | Recurso principal |
|---|---|---|---|---|
| 0–8 min | Problema conductor | Recuperan qué archivos existen y dónde están | Hace visibles los productos S2–S3; recoge una duda | PPT + diseño S2 |
| 8–20 min | MP1: rutas | Predicen y justifican los retos A–F | No revela; pide punto de partida y comparación | Bitácora, pestaña Árbol y Rutas |
| 20–35 min | MP2: contexto | Ejecutan y registran `hostname`, `whoami`, `pwd`, `ls` | Circula y detiene confusiones home/espacio institucional | Terminal + bitácora |
| 35–50 min | Proyecto definitivo | Corrigen el intento y construyen el árbol paso a paso | Modela pausa de seguridad antes de crear | Terminal + PPT |
| 50–60 min | MP3: organizar | Prueban `cp -i` y `mv -i` en prueba | Pide predicción antes de cada `mv` | Terminal + bitácora |
| 60–76 min | Ubicar y transferir | Copian archivos, hacen `scp` local→remoto | Revisa origen/destino; no permite mover originales | Terminal |
| 76–88 min | Verificar | Comparan árbol y checksum | Pide evidencia, no “ya quedó” | Terminal + bitácora |
| 88–100 min | MP5: nano | Editan, guardan, salen y comprueban README | Separa guardar de salir; hace comprobar con `cat` | Terminal + figura nano |
| 100–112 min | Documentar | Actualizan `protocolo.md` con evidencia real | Revisa que registren decisiones y problemas | Terminal + plantilla S4 |
| 112–118 min | MP4: borrar seguro | Predicen, prueban y corrigen en `prueba-s4/` | Restringe la práctica a la carpeta de prueba | Terminal + bitácora |
| 118–120 min | Salida | Marcan semáforo y anotan una duda | Identifica apoyo para S5 | PPT + bitácora |

## Storyboard

## Diapositiva 1 — S4 · Navegar y organizar el proyecto

### Propósito
Situar S4 como el momento de materializar el diseño previo en el servidor.

### Contenido visible
Introducción a la Bioinformática · LCG UNAM · 2026. Unidad 2 · Sesión 4. “De archivos sueltos en `~` a un proyecto que otra persona puede entender y verificar.” Aula invertida · Taller práctico de 2 horas.

### Diseño visual
Fondo claro, una ruta que evoluciona de `~/` a `~/proyecto/`; usar iconos mínimos de archivo, carpeta y terminal.

### Notas para el profesor
**Objetivo:** recordar que la lectura ocurrió antes; hoy se ejecuta y corrige. **Transición:** “¿Qué llegó de S3 y qué aún falta?” **Tiempo aproximado:** 2 min.

## Diapositiva 2 — ¿Qué queremos lograr en S04?

### Propósito
Traducir el objetivo a acciones comprobables.

### Contenido visible
Al terminar: 1) sé dónde estoy; 2) construyo `~/proyecto/`; 3) coloco cada archivo sin alterar datos fuente; 4) verifico árbol, rutas y checksum; 5) documento lo que ocurrió.

### Pregunta o dinámica
Votación con mano: ¿cuál de esas cinco acciones te parece más fácil y cuál más riesgosa?

### Diseño visual
Una secuencia abierta de cinco verbos con flechas, no tarjetas.

### Notas para el profesor
**Respuesta esperada:** suelen señalar “mover archivos” como fácil; recuperar que un cambio de ruta puede volverlo riesgoso. **Tiempo aproximado:** 2 min.

## Diapositiva 3 — Ruta del taller: pensar → ejecutar → comprobar → corregir

### Propósito
Hacer visible el ritmo práctico y cuándo usarán cada recurso.

### Contenido visible
Rutas y contexto → construir → organizar/transferir → verificar → editar/documentar → borrar con seguridad. “La bitácora registra evidencia; la terminal produce evidencia.”

### Diseño visual
Línea de tiempo horizontal de 120 min con los seis momentos; integrar las pestañas de la bitácora como hitos.

### Notas para el profesor
**Dinámica:** pedir que abran la bitácora sin intentar completarla. **Qué observar:** acceso a terminal y diseño de S2. **Tiempo aproximado:** 2 min.

## Diapositiva 4 — El reto: ordenar sin alterar el dato

### Propósito
Presentar el problema de S4 y el estado inicial/final.

### Contenido visible
Inicio en `~`: `pacientes.md`, `pacientes-metadatos.md`, `protocolo.md`. Falta local: `bitacora-ia.md`. Destino: `~/proyecto/` con `data/source/`, `doc/`, `src/`, `results/`, `data/processed/` y `README.md`.

### Pregunta o dinámica
En parejas: “¿Dónde pondrías cada archivo y qué evidencia pedirías para confiar en esa decisión?”

### Diseño visual
Dos árboles pequeños conectados por flecha; no mostrar aún comandos.

### Notas para el profesor
**No revelar todavía:** la secuencia de comandos. **Respuesta esperada:** datos y metadatos en `data/source/`; documentación en `doc/`; README en raíz. **Tiempo aproximado:** 2 min.

## Diapositiva 5 — MP1 · Antes de moverte, ubícate

### Propósito
Activar el modelo mental de árbol y rutas antes de terminal.

### Contenido visible
“Estoy aquí” + “quiero llegar aquí” + “¿cuál es el recorrido?” Retos A–F en Bitácora → Árbol y Rutas. Regla: una ruta relativa parte de donde estás, no siempre de `~`.

### Pregunta o dinámica
Realizar Retos A–F individualmente y explicar uno a una pareja.

### Diseño visual
Reutilizar la figura local `figura-u2-s04-rutas-home.png` como apoyo, con un círculo discreto en el punto de partida.

### Notas para el profesor
**Objetivo:** recoger razonamientos, no rapidez. **Qué observar:** uso de `..` y diferencia absoluta/relativa. **Tiempo aproximado:** 10 min.

## Diapositiva 6 — Detective de rutas: ¿qué está mal?

### Propósito
Provocar un diagnóstico antes de mostrar la corrección.

### Contenido visible
Estás en `~/proyecto/doc/`. Alguien escribe: `data/source/pacientes.md`. Pregunta: “¿En qué lugar lo buscaría Unix?” Después: “¿Qué tendrías que cambiar?”

### Evidencia o error a revisar
La búsqueda implícita sería `~/proyecto/doc/data/source/pacientes.md`, que no existe.

### Diseño visual
Un único árbol con una ruta roja que baja equivocadamente y espacio para que el grupo dibuje la corrección.

### Notas para el profesor
**No revelar todavía:** `../data/source/pacientes.md`. **Respuesta esperada:** primero subir con `..`. **Cómo corregir o comprobar:** comparar con el árbol o usar `ls -l` después. **Tiempo aproximado:** 2 min.

## Diapositiva 7 — MP2 · La evidencia inicial: ¿dónde y con quién trabajo?

### Propósito
Convertir la comprobación de contexto en una rutina antes de operar.

### Contenido visible
En el servidor: `hostname` → máquina; `whoami` → cuenta; `cd ~` + `pwd` → home real; `ls -lah` → archivos disponibles. Antes de crear/copy/borrar: contexto primero.

### Pregunta o dinámica
Ejecutar la secuencia y registrar solo las cuatro evidencias solicitadas en Bitácora → Comprueba Unix.

### Diseño visual
Una salida de terminal anotada de arriba abajo; cada comando enlaza con la pregunta que responde.

### Notas para el profesor
**Qué observar:** alguien que solo teclea sin leer salida. **Pregunta de seguimiento:** “¿qué salida demuestra que estás en el servidor y no local?” **Tiempo aproximado:** 8 min.

## Diapositiva 8 — Home ahora; espacio institucional después

### Propósito
Evitar que el grupo mezcle dos ramas distintas.

### Contenido visible
Ahora: `~/proyecto/` para archivos pequeños y aprendizaje. Más adelante: `/export/space3/users/$USER` para datos/análisis grandes. Dos rutas diferentes, dos usos diferentes.

### Diseño visual
Reutilizar `figura-u2-s04-home-espacio-institucional.png` a ancho completo.

### Notas para el profesor
**Dinámica:** pedir que comparen `pwd` con `ls -ld /export/space3/users/$USER`. **Error frecuente:** concluir que son el mismo directorio porque ambos pertenecen al usuario. **Tiempo aproximado:** 5 min.

## Diapositiva 9 — Antes de construir: pausa de seguridad

### Propósito
Prevenir el error de crear un proyecto dentro de otro.

### Contenido visible
1. `cd ~`  2. `ls -ld proyecto`  3. Si existe: detente e inspecciona con `ls -R proyecto`. Si no existe: crea paso a paso. “No corrijas creando otra capa.”

### Pregunta o dinámica
¿Qué riesgo aparece si ejecutas `mkdir proyecto` sin saber qué ya existe?

### Diseño visual
Bifurcación: “¿existe proyecto?” → inspeccionar/consultar o continuar.

### Notas para el profesor
**Respuesta esperada:** duplicar/anidar y perder la lectura del árbol. **Transición:** construirán el proyecto definitivo, no una plantilla opaca. **Tiempo aproximado:** 3 min.

## Diapositiva 10 — Construye el árbol que usarás todo el curso

### Propósito
Conducir la creación directa de la estructura canónica.

### Contenido visible
`mkdir proyecto` → `cd proyecto` → `pwd` → `mkdir -p data/source data/processed` → `mkdir src results doc` → `touch README.md` → `ls -R`. La estructura visible incluye los destinos, no archivos todavía.

### Pregunta o dinámica
Ejecutar por repetición guiada; después cada pareja señala qué rama contendrá dato, documentación y resultado.

### Diseño visual
Árbol central que aparece por niveles (raíz de proyecto → ramas → source/processed); no usar cajas repetidas.

### Notas para el profesor
**Qué observar:** `pwd` tras entrar a proyecto y anidación correcta de `data/source`. **Tiempo aproximado:** 10 min.

## Diapositiva 11 — MP3 · Copiar, renombrar o mover: predice primero

### Propósito
Separar tres efectos de operaciones parecidas usando un espacio seguro.

### Contenido visible
Solo en `prueba-s4/`: `cp -i a.txt b.txt`; predicción A: `mv -i b.txt c.txt`; predicción B: `mv -i c.txt sub/`. “¿Cambia el nombre, el lugar o ambos?”

### Pregunta o dinámica
Registrar predicciones en Bitácora → Organiza con cuidado y ejecutar después.

### Diseño visual
Tres mini-secuencias de archivo/flecha con antes y después; dejar el resultado de `mv` oculto hasta la comprobación.

### Notas para el profesor
**No revelar todavía:** la clasificación de los dos `mv`. **Errores frecuentes:** creer que un archivo “desapareció”. **Tiempo aproximado:** 10 min.

## Diapositiva 12 — Un movimiento no se entiende sin origen y destino

### Propósito
Revisar y corregir MP3 a partir de evidencia observable.

### Contenido visible
`b.txt → c.txt`: mismo directorio, nombre nuevo. `c.txt → sub/`: mismo nombre, ubicación nueva. Verificar con `ls` y `ls -R`; usar `-i` para pedir confirmación antes de sobrescribir.

### Evidencia o error a revisar
Árbol esperado: `prueba-s4/` contiene `a.txt` y `sub/c.txt`.

### Diseño visual
Una comparación abierta antes/después con flechas; evitar paneles de texto.

### Notas para el profesor
**Cómo corregir o comprobar:** pedir una explicación causal: “¿qué comando produjo cada cambio?” **Transición:** en el proyecto real primero se copia, no se mueve. **Tiempo aproximado:** 3 min.

## Diapositiva 13 — Tres caminos, un destino

### Propósito
Comprobar que absoluta y relativa pueden llegar al mismo `data/source/`.

### Contenido visible
Desde cualquier lugar: `/ruta-real/home/proyecto/data/source/`. Desde `~/proyecto/`: `data/source/`. Desde `~/proyecto/doc/`: `../data/source/pacientes.md`. Dos `pwd` deben coincidir para el mismo directorio.

### Pregunta o dinámica
Ejecutar los tres recorridos; comparar las dos salidas de `pwd`; defender por qué la tercera usa `..`.

### Diseño visual
Tres flechas de colores sobre un mismo árbol; punto de inicio visible en cada una.

### Notas para el profesor
**Objetivo:** introducir robustez como llegar al mismo lugar por rutas distintas. **Tiempo aproximado:** 5 min.

## Diapositiva 14 — Copia primero: conserva un punto de regreso

### Propósito
Guiar la ubicación de los archivos de S3 sin arriesgar el original provisional.

### Contenido visible
Desde `~/proyecto`: `cp -i ~/pacientes.md data/source/`; `cp -i ~/pacientes-metadatos.md data/source/`; `cp -i ~/protocolo.md doc/`. “Todavía no borres las copias de `~`.”

### Pregunta o dinámica
Antes de ejecutar: ¿qué debe permanecer en `~` y qué debe aparecer en el proyecto?

### Diseño visual
Flujo origen → copia provisional conservada + destino; resaltar que la flecha no elimina el origen.

### Notas para el profesor
**Error frecuente:** sustituir `cp -i` por `mv`. **Respuesta esperada:** la copia en home permite recuperar si falla la verificación. **Tiempo aproximado:** 6 min.

## Diapositiva 15 — Lo que falta viaja desde tu computadora

### Propósito
Reforzar que `scp` se ejecuta localmente y necesita un destino remoto explícito.

### Contenido visible
`[LOCAL] scp bitacora-ia.md usuario@servidor:/ruta/absoluta/de/tu/home/proyecto/doc/`. Local → canal → remoto. El `:` separa servidor y destino. No usar `$USER` en el comando local.

### Pregunta o dinámica
¿Qué dos cosas comprobarías antes de presionar Enter?

### Diseño visual
Computadora local, conexión y terminal remota; una etiqueta LOCAL claramente separada de REMOTO.

### Notas para el profesor
**Respuesta esperada:** estar local y tener ruta absoluta remota real. **Qué observar:** datos sensibles en pantallas/capturas. **Tiempo aproximado:** 4 min.

## Diapositiva 16 — Verificar no es mirar: árbol + checksum

### Propósito
Convertir la comprobación en evidencia de estructura e integridad.

### Contenido visible
1. `tree` o `ls -R` muestra ubicación. 2. `sha256sum ~/proyecto/data/source/pacientes.md` compara contenido con S3. Si no coincide: detente, conserva copias y vuelve a copiar; no borres.

### Pregunta o dinámica
“¿Qué puede demostrar el árbol y qué no puede demostrar?”

### Diseño visual
Dos pruebas en paralelo: árbol para ubicación, huella SHA-256 para contenido. Una misma conclusión requiere ambas.

### Notas para el profesor
**Respuesta esperada:** árbol no prueba integridad; checksum no muestra organización. **Tiempo aproximado:** 6 min.

## Diapositiva 17 — MP5 · Editar es un ciclo, no un momento

### Propósito
Preparar la práctica de nano sobre documentación, no datos fuente.

### Contenido visible
ABRIR → EDITAR → GUARDAR → SALIR → COMPROBAR. Trabajar en `~/proyecto/README.md`; `data/source/pacientes.md` no se edita.

### Pregunta o dinámica
¿En cuál de los cinco pasos obtienes evidencia independiente de que el cambio permaneció?

### Diseño visual
Ciclo circular con “comprobar” destacado al final; terminal abierta al centro.

### Notas para el profesor
**Respuesta esperada:** después de salir, con `cat README.md`/reabrir. **No revelar todavía:** solución a Ctrl-S. **Tiempo aproximado:** 2 min.

## Diapositiva 18 — Nano: lee la pantalla antes de confirmar

### Propósito
Ubicar las cuatro zonas necesarias y los atajos mínimos.

### Contenido visible
Área de edición; mensajes; atajos visibles; nombre del archivo. `^O` = Ctrl-O guarda; Enter confirma el nombre; `^X` = Ctrl-X sale; `^W` busca.

### Diseño visual
Reutilizar `figura-u2-s04-nano-interfaz.png`.

### Notas para el profesor
**Error frecuente:** usar Ctrl-S y pensar que guardó. **Cómo corregir o comprobar:** si se pausa terminal, Ctrl-Q; volver a usar Ctrl-O. **Tiempo aproximado:** 3 min.

## Diapositiva 19 — Evidencia de edición: no basta con “lo guardé”

### Propósito
Conducir la práctica y revisión de README/protocolo.

### Contenido visible
En `README.md`: descripción y función de cada rama. Después: `ls -l README.md` + `cat README.md` + reabrir sin cambios. Aplicar el mismo ciclo a `doc/protocolo.md` y registrar lo que realmente ocurrió.

### Pregunta o dinámica
Parejas intercambian: una explica qué hizo; la otra exige la evidencia que lo demuestra.

### Diseño visual
Flujo comando → salida visible → afirmación defendible; incluir ejemplo breve de `cat`.

### Notas para el profesor
**Qué observar:** protocolo con comandos inventados o sin problemas/decisiones. **Tiempo aproximado:** 12 min.

## Diapositiva 20 — La entrega es una historia verificable

### Propósito
Conectar ejecución con la evidencia de Tarea 3.

### Contenido visible
En `doc/protocolo.md`: árbol; ubicación de archivos; checksum S3/S4; rutas absoluta y relativa; comandos; problemas/correcciones; conclusión sobre reproducibilidad. Una captura no sustituye estas evidencias.

### Pregunta o dinámica
“Si otra persona recibe tu protocolo, ¿qué parte le permite recrear o discutir tu decisión?”

### Diseño visual
Una hoja de protocolo que recibe flechas desde árbol, checksum, rutas y terminal.

### Notas para el profesor
**Transición:** hacer el registro antes de olvidar decisiones. **Tiempo aproximado:** 3 min.

## Diapositiva 21 — MP4 · Borrar seguro empieza antes de `rm`

### Propósito
Practicar una rutina de eliminación segura sin tocar el proyecto real.

### Contenido visible
Solo en `~/prueba-s4/`: ¿dónde estoy? → ¿qué existe? → ¿qué quiero borrar? → ejecuto. Primero predice `rmdir sub` con `c.txt` dentro; después observa el error; usa `rm -i sub/c.txt`, verifica y vuelve a intentar `rmdir sub`.

### Pregunta o dinámica
Predicción individual antes del primer `rmdir`; comparación en parejas tras ver el mensaje.

### Evidencia o error a revisar
`rmdir: Directory not empty` no indica un sistema roto: indica una condición no cumplida.

### Diseño visual
Secuencia vertical con carpeta no vacía → mensaje → archivo eliminado con confirmación → carpeta vacía; sin iconografía de peligro exagerada.

### Notas para el profesor
**No revelar todavía:** el resultado del primer intento. **Errores frecuentes:** sugerir `rm -r`; recordar que no es parte de la tarea obligatoria. **Tiempo aproximado:** 6 min.

## Diapositiva 22 — Cuando algo falla, lee antes de repetir

### Propósito
Ensayar diagnóstico de errores típicos de S4.

### Contenido visible
`No such file or directory` → `pwd` + `ls` + revisa tipo de ruta. `mkdir` falla → falta padre/usa `-p`. `mv` “desaparece” → revisa destino. Checksum distinto → conserva y vuelve a copiar. `scp` raro → confirma que ejecutas local y la ruta remota.

### Pregunta o dinámica
Cada equipo elige un síntoma y formula una secuencia de diagnóstico, no una solución inmediata.

### Diseño visual
Cinco mensajes de terminal pequeños conectados a preguntas de diagnóstico; no usar tabla ni tarjetas.

### Notas para el profesor
**Objetivo:** normalizar el error como evidencia. **Tiempo aproximado:** 2 min.

## Diapositiva 23 — IA después: revisora, no operadora

### Propósito
Ubicar la actividad formativa de IA después de la construcción manual.

### Contenido visible
Después del taller: anonimiza `[SERVIDOR]`, `[USUARIO]`, `[RUTA]`; pide una propuesta; compara comando por comando; valida con `man` y `prueba-s4/`; registra decisión en `bitacora-ia.md`. Nunca compartir contraseñas, IP, llaves o huellas.

### Pregunta o dinámica
¿Qué propondrías verificar antes de aceptar un comando sugerido por IA?

### Diseño visual
Dos columnas abiertas: “propuesta” → “prueba/control” → “decisión documentada”.

### Notas para el profesor
**Respuesta esperada:** que no borre/sobrescriba, que use home, y que produzca la estructura requerida. **Tiempo aproximado:** 2 min.

## Diapositiva 24 — Quédate con esto

### Propósito
Cerrar con ideas transferibles y recoger el semáforo de salida.

### Contenido visible
1. Una ruta relativa depende de dónde estás: `pwd` te orienta. 2. Home y espacio institucional son ramas y usos distintos. 3. Copia antes de mover; conserva el original hasta verificar. 4. Árbol y checksum responden preguntas diferentes. 5. Editar incluye comprobar fuera del editor. 6. Un error leído y corregido produce evidencia de aprendizaje.

### Pregunta o dinámica
Semáforo: verde/amarillo/rojo y una duda concreta para S5.

### Diseño visual
Fondo oscuro con seis frases breves alineadas sobre una sola ruta de terminal; sin recuadros.

### Notas para el profesor
**Objetivo:** identificar estudiantes que requieren apoyo en rutas, integridad o estructura antes de S5. **Transición:** preparar lectura de S5 y probar `file`/`head`. **Tiempo aproximado:** 2 min.
