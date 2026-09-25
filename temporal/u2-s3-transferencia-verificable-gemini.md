# Prompt maestro — Gemini Canvas

Crea una aplicación web educativa autónoma para:

`[ LCG UNAM 2026 ]   Introducción a la Bioinformática • Sesión 3 • Prácticas 4 y 5`

# Traslado verificable

## Transferir datos, comprobar su integridad y documentar evidencia

## Identidad y propósito

La aplicación acompaña —sin reemplazar— las Prácticas 4 y 5 de la sesión S3. Su función es ayudar al estudiante a pensar, decidir, registrar y justificar la transferencia real de `pacientes.md` y `pacientes-metadatos.md` entre su computadora y el servidor del curso.

La app no debe simular SSH, SFTP, FileZilla, contraseñas, huellas de servidor ni una terminal. El estudiante debe usar las herramientas reales proporcionadas por su docente. La aplicación funciona como guía de razonamiento, registro de evidencia y preparación de contenido real para `protocolo.md`.

## Perfil del estudiante

Estudiantes de primer semestre de la Licenciatura en Ciencias Genómicas de la UNAM, recién egresados de preparatoria.

Usa español claro, directo y respetuoso. No supongas experiencia previa con Unix, terminales, servidores, protocolos, programación ni formatos biológicos. No uses vocabulario adicional innecesario.

## Conocimientos previos permitidos

El estudiante ya ha trabajado con:

- `pacientes.md`, un conjunto de datos sintético;
- `pacientes-metadatos.md`;
- `protocolo.md` como documento vivo;
- la idea de que los datos deben conservarse con sus metadatos;
- reproducibilidad, evidencia y verificación;
- la diferencia básica entre terminal y shell;
- SSH, SFTP y FileZilla como herramientas introducidas en S3;
- `ls -lh` para comprobar presencia y tamaño de archivos;
- el concepto de checksum como huella del contenido de un archivo.

No introducir rutas, directorios, `scp`, `rsync`, organización del proyecto, permisos ni otros contenidos de S4.

## Objetivos de aprendizaje

Al terminar, el estudiante debe poder:

1. Distinguir claramente el lado local y el lado remoto durante una transferencia.
2. Decidir qué archivos deben viajar juntos y justificarlo.
3. Transferir realmente `pacientes.md` y `pacientes-metadatos.md` mediante SFTP o FileZilla.
4. Confirmar con evidencia real que los archivos están en el servidor.
5. Comparar los checksums locales y remotos con el mismo algoritmo SHA-256.
6. Explicar por qué la presencia o el tamaño de un archivo no prueban su integridad.
7. Documentar comandos, decisiones, resultados y problemas reales para incorporarlos en `protocolo.md`.

## Restricción pedagógica central

Seguir este ciclo:

**OBSERVAR → PENSAR → DECIDIR → USAR LA HERRAMIENTA REAL → COMPROBAR → RECIBIR RETROALIMENTACIÓN → CORREGIR → JUSTIFICAR → DOCUMENTAR**

No resolver por el estudiante la distinción local/remoto ni la comparación de checksums antes de que tome una decisión. No inventar resultados, nombres de servidor, usuario, rutas, huellas, contraseñas ni hashes.

## Arquitectura de pestañas

Implementar navegación libre con estas pestañas:

1. `1. Antes de transferir`
2. `2. Transferencia real`
3. `3. Verificar integridad`
4. `4. Documentar evidencia`
5. `✓ Resumen`

Usar una función central robusta llamada `activateTab(tabName)`. Las pestañas nunca deben bloquearse por progreso. El estudiante debe poder avanzar, regresar, corregir y abrir Resumen en cualquier momento.

## Pestaña 1 — Antes de transferir

Presentar el problema:

> `pacientes.md` y `pacientes-metadatos.md` están en tu computadora. El trabajo posterior se realizará en el servidor. Antes de transferir, decide qué archivos deben viajar y qué evidencia te permitirá saber que llegaron correctamente.

Actividad 1: decisión de archivos.

Mostrar estas opciones con checkboxes inicialmente vacíos:

- `pacientes.md`
- `pacientes-metadatos.md`
- `protocolo.md`
- “Solo el archivo de datos”

Pedir:

- “Selecciona los archivos necesarios para esta transferencia.”
- “Explica brevemente por qué el dato no debe viajar solo.”

Al comprobar:

- Si elige `pacientes.md` y `pacientes-metadatos.md`, reconocer que son los dos archivos requeridos para esta práctica y explicar que los metadatos permiten interpretar el dato.
- Si incluye `protocolo.md`, indicar con claridad que el protocolo se transferirá como tercer archivo al cierre de S3, pero no forma parte de esta transferencia inicial.
- Si elige solo el dato, explicar que un archivo sin información de interpretación reduce su reutilización y trazabilidad.
- Ofrecer una pista antes de revelar la explicación completa: “Piensa en qué información necesita otra persona para comprender el contenido de un archivo.”

Actividad 2: distinguir contextos.

Mostrar dos tarjetas sin respuestas preseleccionadas:

- Lado local: tu computadora.
- Lado remoto: el servidor del curso.

Pedir que el estudiante clasifique, mediante selección o arrastre accesible, estas acciones:

- Localizar los archivos antes de conectarse.
- Usar `lpwd` o el panel izquierdo de FileZilla.
- Usar `pwd` o el panel derecho de FileZilla.
- Ejecutar `put pacientes.md`.
- Confirmar con `ls -lh` después de entrar por SSH.

No presentar la clasificación correcta antes de comprobar. Tras un error, explicar qué pista contextual permite decidir: palabras como “local”, “remoto”, `lpwd`, `pwd`, paneles y contexto SSH/SFTP.

## Pestaña 2 — Transferencia real

Explicar claramente:

> Ahora realiza la transferencia con la herramienta real indicada por tu docente. Esta aplicación no se conecta al servidor ni mueve archivos por ti.

Ofrecer dos rutas de trabajo, con botones o secciones expandibles:

### Usaré SFTP en terminal

Mostrar únicamente los comandos ya enseñados en S3, con etiquetas de contexto:

```text
[LOCAL]
sftp usuario@servidor

[SFTP]
lpwd
lls
pwd
ls
put pacientes.md
put pacientes-metadatos.md
exit
```

No usar un servidor real ni datos inventados. Recordar que las credenciales se reciben en clase y no deben escribirse en la app.

### Usaré FileZilla

Mostrar instrucciones breves:

- Usar SFTP, no FTP plano.
- Identificar panel local a la izquierda y remoto a la derecha.
- Subir los dos archivos.
- No incluir credenciales en capturas, notas ni la aplicación.

Después, pedir un registro real:

- Herramienta utilizada: SFTP en terminal / FileZilla / Otra autorizada.
- ¿Cómo distinguí el lado local del remoto?
- ¿Qué archivos confirmé en el servidor?
- ¿Apareció un problema? Sí / No.
- Si apareció, describir el mensaje o situación sin incluir datos sensibles.

No calificar automáticamente si la transferencia fue exitosa. Mostrar un aviso formativo: “La presencia de un archivo es una evidencia inicial, pero todavía no prueba que su contenido sea idéntico.”

## Pestaña 3 — Verificar integridad

Presentar el principio:

> Que un archivo aparezca en el servidor no demuestra que llegó intacto. Para comprobarlo, compara la huella del contenido en origen y destino.

Mostrar los comandos por sistema, sin cambiar ni simplificar el alcance:

```bash
# macOS local
shasum -a 256 pacientes.md
shasum -a 256 pacientes-metadatos.md

# Linux, WSL o Git Bash local
sha256sum pacientes.md
sha256sum pacientes-metadatos.md

# Servidor Linux remoto
sha256sum pacientes.md
sha256sum pacientes-metadatos.md
```

Y para PowerShell:

```powershell
Get-FileHash .\pacientes.md -Algorithm SHA256
Get-FileHash .\pacientes-metadatos.md -Algorithm SHA256
```

No calcular hashes en la app. Pedir que el estudiante los obtenga mediante las herramientas reales y registre solo las cadenas que esté autorizado a documentar.

Para cada archivo, crear un bloque con:

- Checksum local: campo de texto.
- Checksum remoto: campo de texto.
- “Antes de comprobar, mi decisión es”: Coinciden / No coinciden / Aún no puedo decidir.
- “¿Qué evidencia utilicé para decidir?”: campo breve.

Al pulsar `Comprobar mi comparación`:

- Si ambos campos están vacíos, indicar que falta evidencia real.
- Si los campos son idénticos, mostrar que la decisión correcta es “Coinciden” y explicar que se comparó la huella del contenido usando SHA-256.
- Si los campos son distintos, mostrar que la decisión correcta es “No coinciden”; indicar que no debe usarse el archivo, que debe repetirse la transferencia y verificarse otra vez.
- Si los hashes son iguales pero el estudiante marcó “No coinciden”, pedirle revisar qué comparó.
- Si los hashes son distintos pero eligió “Coinciden”, ofrecer primero una pista: “Compara carácter por carácter las dos huellas; el nombre y el tamaño no bastan.”
- No depender solo de verde o rojo; usar texto, iconos y `aria-live`.

Incluir una pregunta de justificación:

> ¿Por qué no basta con que el archivo aparezca al ejecutar `ls -lh`?

La retroalimentación debe reconocer que `ls -lh` sirve para observar presencia, nombre y tamaño, pero no garantiza que el contenido sea idéntico al archivo original.

## Pestaña 4 — Documentar evidencia

Explicar que la evidencia principal de S3 es `protocolo.md`, actualizado con lo que realmente se hizo. La app no debe crear comandos inventados.

Ofrecer campos editables para preparar una sección Markdown:

- Sistema local.
- Cliente utilizado.
- Protocolo de transferencia.
- Registro de acciones en una tabla con columnas: Contexto, Acción o comando, Propósito.
- Checksum local y remoto de ambos archivos.
- Resultado sustentado.
- Problemas encontrados y solución.
- Reflexión: “¿Qué acción comprobaría primero si volviera a transferir un archivo?”

Generar una vista previa de Markdown que use exclusivamente los textos y decisiones reales del estudiante. Si un campo está vacío, mostrar `Pendiente` o `Sin respuesta`; nunca rellenar datos de ejemplo como si fueran reales.

Incluir un aviso permanente:

> No registres contraseñas, llaves privadas, tokens, direcciones IP ni otros datos sensibles.

## Persistencia y reinicio

Usar `localStorage` para guardar:

- pestaña activa;
- selecciones;
- respuestas;
- textos;
- decisiones previas a comprobar;
- intentos;
- pistas consultadas;
- resultados de comparación;
- contenido de la documentación.

Agregar el botón `Reiniciar práctica`, con diálogo de confirmación. Al confirmar, borrar únicamente los datos de esta práctica almacenados en `localStorage` y volver al estado inicial.

## Resumen

La pestaña `✓ Resumen` debe estar siempre disponible y presentar el trabajo real del estudiante:

- Archivos seleccionados y justificación.
- Clasificación local/remoto.
- Herramienta real utilizada.
- Registro de transferencia.
- Checksum local y remoto de cada archivo.
- Decisión inicial, resultado comprobado, errores y correcciones.
- Evidencia pendiente.
- Texto preparado para `protocolo.md`.
- Reflexión final.

Para cualquier elemento no completado usar `Pendiente` o `Sin respuesta`.

Incluir el botón:

`⬇ Descargar resultados de la práctica`

Debe descargar un archivo Markdown mediante JavaScript con `Blob`, `URL.createObjectURL` y un enlace `<a download>`. Usar un nombre de archivo como `s3-transferencia-verificable-resultados.md`.

El Markdown descargado debe adaptar su contenido real a estas secciones:

```markdown
# Sesión 3 — Traslado verificable

## Mis decisiones antes de transferir
## Distinción entre lado local y remoto
## Transferencia real
## Verificación de integridad
## Errores, pistas y correcciones
## Evidencia para protocolo.md
## Reflexión final
## Registro formativo
```

No incluir secciones vacías sin sentido. No inventar resultados.

Agregar un segundo botón:

`⬇ Descargar borrador para protocolo.md`

Debe descargar solo la sección de documentación preparada por el estudiante, con su contenido real.

## Diseño visual

Usar un diseño universitario moderno, sobrio y claro:

- fondo claro;
- azul oscuro institucional;
- badge dorado `LCG UNAM 2026`;
- código y nombres de archivo en tipografía monoespaciada;
- tarjetas solo cuando ayuden a separar decisiones o evidencia;
- evitar apariencia infantil, encabezados enormes, puntos, estrellas, rankings o porcentajes;
- usar estados formativos: Pendiente, Revisado, Corregido, Requiere revisar.

## Accesibilidad

Implementar HTML semántico y accesible:

- `label` asociado a cada campo;
- `fieldset` y `legend` para decisiones relacionadas;
- foco visible;
- navegación completa con teclado;
- `aria-live` para retroalimentación;
- pestañas con `role="tablist"`, `role="tab"`, `role="tabpanel"` y `aria-selected`;
- contraste adecuado;
- no usar solo color para comunicar resultados.

## Restricciones técnicas

Crear un único archivo HTML autónomo con HTML, CSS y JavaScript. No usar React, frameworks, backend, login, analítica, APIs ni dependencias externas. Debe funcionar offline.

## Validación funcional obligatoria

Antes de entregar, comprobar que:

1. La app abre correctamente.
2. Todas las pestañas funcionan.
3. Ninguna respuesta aparece preseleccionada.
4. Los selects comienzan en `Selecciona...` y los radios están vacíos.
5. Se puede navegar libremente sin terminar actividades.
6. Las respuestas sobreviven al cambio de pestaña.
7. `localStorage` conserva el trabajo y la pestaña activa.
8. Resumen abre siempre y refleja solo respuestas reales.
9. Las descargas Markdown funcionan.
10. El Markdown descargado contiene el trabajo real.
11. Reiniciar práctica funciona con confirmación.
12. Una actividad incompleta no rompe la app.

## Validación pedagógica obligatoria

Antes de entregar, comprobar que:

1. No se introdujeron rutas, directorios, `scp`, `rsync` ni contenidos de S4.
2. El vocabulario es adecuado para estudiantes de primer semestre.
3. La aplicación no sustituye SSH, SFTP, FileZilla ni la terminal real.
4. El estudiante toma una decisión antes de comprobar resultados.
5. Las pistas ayudan sin revelar de inmediato la respuesta.
6. La transferencia conserva la intención de trasladar dato y metadatos juntos.
7. La verificación enfatiza que presencia y tamaño no prueban integridad.
8. El Resumen documenta razonamiento, errores, correcciones y evidencia, no solo aciertos.

Devuélveme el HTML COMPLETO, autónomo y funcional. No un parche. No fragmentos.
