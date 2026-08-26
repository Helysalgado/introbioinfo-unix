# Prompt maestro — Gemini Canvas

Crea una aplicación web educativa autónoma para:

`[ LCG UNAM 2026 ]   Introducción a la Bioinformática • Sesión 3`

# Bitácora de laboratorio: conectar, transferir y verificar

## Propósito e identidad

Construye una única aplicación complementaria para toda la sesión S3: el shell, acceso remoto y transferencia de archivos. Debe acompañar las Prácticas 1–5 y el cierre como una **bitácora de laboratorio interactiva**, no como una simulación de terminal ni como un examen de comandos.

La experiencia real ocurre en SSH, la terminal, `man`, Tab, historial, `Ctrl-C`, SFTP o FileZilla, y los comandos reales para calcular checksums. La app acompaña con este ciclo:

**predecir → ejecutar en la herramienta real → observar → registrar evidencia → interpretar → corregir → documentar**

Usar como caso conductor los archivos reales de la sesión: `pacientes.md`, `pacientes-metadatos.md` y, durante el cierre, `protocolo.md`. No inventar datos, servidores, usuarios, rutas, contraseñas, huellas SSH, hashes ni ejemplos que introduzcan contenidos posteriores.

## Perfil del estudiante

Dirigirse a estudiantes de primer semestre de la Licenciatura en Ciencias Genómicas de la UNAM, recién egresados de preparatoria. Usar lenguaje claro y preciso. No asumir experiencia previa con Unix, programación, terminal, servidores, protocolos, formatos biológicos o estadística.

El estudiante ya conoce, por S2, la importancia de reproducibilidad, metadatos, conservación de datos originales, `pacientes.md`, `pacientes-metadatos.md`, `protocolo.md` y uso crítico de IA. S3 presenta terminal, shell, SSH, SFTP, FileZilla, anatomía de comandos, `hostname`, `whoami`, `pwd`, `ls`, `man`, Tab, historial, `Ctrl-C` y checksum.

No introducir rutas, navegación entre directorios, organización del proyecto, `scp`, `rsync`, permisos, `nano` ni otros contenidos de S4.

## Objetivos de aprendizaje

Al terminar, el estudiante debe poder:

1. Confirmar dónde está, con qué cuenta trabaja y en qué contexto opera antes de manipular archivos.
2. Desarrollar autonomía progresiva para entrar, reconocer el entorno remoto y salir.
3. Orientarse, consultar ayuda y controlar acciones en la terminal real sin depender de memorizar todo.
4. Transferir datos y metadatos juntos, distinguiendo lado local y remoto.
5. Explicar y aplicar la diferencia entre ver un archivo y demostrar que llegó intacto.
6. Documentar evidencia, dificultades, decisiones y correcciones reales en `protocolo.md`.
7. Usar IA solo después del trabajo manual, como revisora crítica y no como autoridad u operadora del servidor.

## Límites obligatorios

No simular SSH, una terminal, SFTP, FileZilla ni cálculo de hashes. No pedir ni guardar credenciales, contraseñas, llaves privadas, tokens, direcciones IP ni huellas institucionales. No automatizar lo que el estudiante debe aprender a hacer.

La app no se conecta al servidor, no transfiere archivos, no ejecuta comandos y no calcula checksums. Debe enviar al estudiante a la herramienta real y volver para registrar lo observado.

No usar puntos, estrellas, porcentajes, rankings, aprobado/reprobado ni calificaciones. Usar estados formativos: `Pendiente`, `Registrado`, `Revisado`, `Corregido` y `Requiere revisar`.

## Economía de interacción

Pedir una respuesta o registro solo si aporta al menos una de estas cosas: evidencia de aprendizaje, una decisión, una dificultad, una corrección o una reflexión relevante. No convertir la bitácora en una transcripción de cada comando ni pedir la misma información dos veces.

Recuperar automáticamente en la vista de documentación y en Resumen las decisiones y evidencias ya registradas en otras pestañas. Cuando baste una decisión breve, usar una selección con espacio opcional para justificar; reservar los campos de texto para observaciones que no puedan expresarse de otro modo.

## Arquitectura y navegación

Crear pestañas accesibles, siempre disponibles y de navegación libre:

1. `1. Antes de conectarme`
2. `2. De acompañamiento a autonomía`
3. `3. Orientarme, consultar y controlar`
4. `4. Del equipo local al servidor`
5. `5. Evidencia antes de confianza`
6. `6. Documentar y revisar con IA`
7. `✓ Resumen`

Implementar una función central `activateTab(tabName)`. No bloquear ninguna pestaña por progreso. El estudiante debe poder regresar, corregir, explorar y abrir Resumen aunque haya actividades incompletas. Un error en una actividad no debe romper la navegación.

## Pestaña 1 — Antes de conectarme

Basar esta pestaña en la Práctica 1: entrar al servidor, reconocer el entorno y salir.

Presentar la rutina de trabajo:

> Antes de trabajar con archivos, confirmo dónde estoy.

Antes de usar SSH, pedir una predicción con campos vacíos:

- “¿Qué crees que puede cambiar al pasar de tu computadora al servidor?”
- “¿Qué comando puede ayudarte a confirmar la computadora, la cuenta y la ubicación?”

Mostrar una guía breve, no una respuesta preseleccionada:

```bash
[LOCAL]
ssh usuario@servidor

[REMOTO]
hostname
whoami
pwd
exit
```

Indicar que `usuario@servidor` es una estructura, no un dato para copiar; las credenciales se reciben en clase y nunca se registran en la app.

Después de la conexión real, pedir registrar únicamente evidencia no sensible y relevante:

- una observación sobre el cambio de *prompt*;
- una decisión breve que complete “Antes de trabajar, confirmo…” con `hostname`, `whoami` y `pwd`;
- opcionalmente, una dificultad o corrección si ocurrió.

No exigir copiar la salida literal si contiene información institucional. Permitir respuestas descriptivas.

## Pestaña 2 — De acompañamiento a autonomía

Basar esta pestaña en la Práctica 2. Explicar que conectarse es una habilidad que se afianza con repetición, no una prueba de velocidad.

Mostrar tres rondas no evaluativas:

1. `Con guía del docente`
2. `Con mis notas`
3. `Intento de memoria`

Para cada ronda, el estudiante realiza realmente:

```text
conectarse → hostname → whoami → pwd → exit
```

Después de cada ronda, pedir solo dos datos: el apoyo que necesitó y, cuando exista, una dificultad o corrección. Al terminar las tres rondas, pedir una sola reflexión: qué acción ya puede explicar con sus propias palabras.

Usar checkboxes inicialmente vacíos solo como registro de que se realizó la ronda, no como calificación. Si una ronda está pendiente, mostrar `Pendiente`, nunca una sanción ni una barrera para continuar.

Al final, pedir una reflexión: “¿Por qué conviene dominar esta secuencia antes de transferir datos?”

## Pestaña 3 — Orientarme, consultar y controlar

Basar esta pestaña en la Práctica 3 y estructurarla en tres ideas: **orientarme → consultar → controlar**.

### Orientarme

Antes de ejecutar en la terminal real, preguntar:

- “¿Qué esperas que cambie entre `ls` y `ls -l`?”
- “¿Qué crees que aporta `-h` en `ls -lh`?”

Después pedir ejecutar realmente:

```bash
pwd
ls
ls -l
ls -lh
```

Solicitar un único registro: qué cambió entre `ls` y `ls -l`, o qué aporta `-h`. Después explicar que `ls -lh` ayuda a comprobar presencia, pero no integridad.

### Consultar

Pedir ir a la terminal real y usar:

```bash
man ls
```

Solicitar localizar la opción `-h`, salir con `q` y registrar en una sola frase qué encontró y cómo `man` le ayuda cuando no recuerda una opción.

Explicitar que consultar ayuda es una estrategia de autonomía, no señal de incapacidad.

### Controlar

Pedir realizar en la terminal real estas experiencias:

- Tab para completar un nombre existente;
- flecha ↑ e `history` para recuperar una instrucción;
- `sleep 30` y `Ctrl-C` para detener un proceso seguro.

Después pedir elegir o describir una sola acción que le resultó útil (Tab, historial o `Ctrl-C`) y en qué situación la usaría. No pedir un registro separado para las tres si no hubo dificultad relevante.

No simular `man`, Tab, historial, `sleep` ni `Ctrl-C`.

## Pestaña 4 — Del equipo local al servidor

Basar esta pestaña en la Práctica 4. Presentar cuatro preguntas antes de cualquier transferencia real:

1. ¿Qué archivos deben viajar?
2. ¿Desde dónde salen?
3. ¿A dónde deben llegar?
4. ¿Qué evidencia permitirá comprobar que llegaron?

Usar únicamente los archivos reales de S3: `pacientes.md` y `pacientes-metadatos.md`.

Crear una actividad de decisión con checkboxes inicialmente vacíos:

- `pacientes.md`
- `pacientes-metadatos.md`
- `protocolo.md`
- “Solo el archivo de datos”

Al comprobar, explicar que en esta transferencia inicial viajan datos y metadatos. Si se selecciona `protocolo.md`, aclarar que ese archivo se transfiere como tercer archivo al cierre de S3, no durante esta práctica inicial. Si se elige solo el dato, ofrecer primero una pista sobre qué necesita otra persona para interpretar un archivo y después explicar la función de los metadatos.

Crear una actividad accesible para distinguir contextos **LOCAL ↔ REMOTO**. Pedir clasificar estas acciones, sin respuestas anticipadas:

- localizar archivos antes de conectarse;
- usar `lpwd` o el panel izquierdo de FileZilla;
- usar `pwd` o el panel derecho de FileZilla;
- ejecutar `put pacientes.md`;
- confirmar con `ls -lh` tras entrar por SSH.

Después de decidir, permitir comprobar y ofrecer feedback textual, una pista y reintento. No depender solo de color.

Mostrar dos rutas de acción reales:

### SFTP en terminal

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

### FileZilla

- Usar SFTP, no FTP plano.
- Distinguir panel local a la izquierda y remoto a la derecha.
- Subir ambos archivos.
- No mostrar ni registrar credenciales.

Decir explícitamente: “La aplicación no realiza la transferencia por ti.”

Después de usar la herramienta real, pedir registrar:

- herramienta utilizada;
- cómo distinguió local y remoto;
- confirmación de que ambos archivos aparecieron en el servidor;
- dificultad y corrección, solo si ocurrió.

## Pestaña 5 — Evidencia antes de confianza

Basar esta pestaña en la Práctica 5. Mostrar el principio central:

> Ver el archivo ≠ demostrar que llegó intacto.

Explicar que `ls -lh` confirma presencia, nombre y tamaño, pero no asegura que el contenido sea idéntico. La comprobación requiere comparar checksums de origen y destino usando SHA-256.

Mostrar, como consulta, los comandos de la sesión:

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

```powershell
# PowerShell local
Get-FileHash .\pacientes.md -Algorithm SHA256
Get-FileHash .\pacientes-metadatos.md -Algorithm SHA256
```

No calcular hashes ni generar valores de ejemplo en la app. Pedir al estudiante usar los entornos reales.

Para cada archivo, incluir campos vacíos para:

- checksum local;
- checksum remoto;
- decisión previa: `Coinciden`, `No coinciden` o `Aún no puedo decidir`;
- justificación breve de la decisión.

El flujo obligatorio es:

**DECIDIR → COMPROBAR → FEEDBACK → PISTA → CORREGIR**

Al comprobar:

- Si faltan hashes, indicar que falta evidencia real.
- Si las cadenas son idénticas, explicar que la huella del contenido coincide y pedir revisar si la decisión inicial fue coherente.
- Si son distintas, reforzar la conducta correcta: **no usar el archivo → repetir transferencia → volver a verificar**.
- Si el estudiante se equivoca, dar primero una pista: “Compara las cadenas carácter por carácter; el nombre y el tamaño no bastan.” Permitir reintentar antes de mostrar una explicación completa.

No mostrar ✓, ✗, verde o rojo antes de comprobar, y no usar solo color después.

Incluir una pregunta final: “¿Por qué el archivo puede estar presente y aun así no estar listo para usarse?”

## Pestaña 6 — Documentar y revisar con IA

### Documentar lo que hice

El cierre integra toda la sesión. El producto central sigue siendo `protocolo.md`, no una pantalla de “actividad completada”. La app debe construir progresivamente un borrador con información real ya capturada durante el recorrido. No volver a pedir datos que ya estén guardados. Solicitar solo lo que complete la evidencia:

- objetivo de transferencia;
- sistema local y cliente usado;
- acciones o comandos distinguiendo `[LOCAL]`, `[REMOTO]` y `[SFTP]`;
- observaciones de contexto;
- transferencia;
- checksums locales y remotos;
- decisión sobre integridad;
- dificultades, mensajes relevantes y correcciones;
- resultado sustentado;
- reflexión sobre reproducibilidad.

Presentar una vista previa Markdown editable. Para datos faltantes usar `Pendiente` o `Sin respuesta`; nunca inventar comandos, resultados o hashes.

Recordar de forma visible: no escribir contraseñas, llaves privadas, tokens, IP, huellas institucionales ni otros datos sensibles.

### Revisión crítica con IA — después del trabajo manual

Mantener esta actividad después de ejecutar y documentar manualmente. Explicar:

> Primero ejecuto y documento; después utilizo IA para revisar críticamente.

La IA no opera el servidor ni propone comandos nuevos para que se ejecuten sin comprensión y verificación.

Guiar al estudiante para crear un registro independiente en `bitacora-ia.md` que distinga:

- lo que realmente hizo y observó;
- lo que sugirió la IA;
- qué aceptó o rechazó;
- qué evidencia usó para verificarlo;
- qué corrigió en `protocolo.md`;
- conclusión sobre la confiabilidad de la revisión.

Pedir anonimizar la copia que comparte con IA usando marcadores como `[SERVIDOR]` y `[USUARIO]`, y conservar el original. No incluir credenciales ni datos sensibles.

## Persistencia y estado inicial

Abrir siempre sin respuestas preseleccionadas, sin ✓ o ✗ anticipados, sin colores de corrección y con radios vacíos. Los campos de texto deben estar vacíos; los selects deben comenzar en `Selecciona...`.

Usar `localStorage` para persistir pestaña activa, predicciones, registros pertinentes de rondas, observaciones, decisiones, hashes, intentos, pistas consultadas, correcciones, reflexiones y borrador del protocolo. No guardar datos sensibles.

Agregar `Reiniciar práctica` con confirmación. Al confirmar, borrar solo los datos de esta práctica y regresar al estado inicial.

## ✓ Resumen

La pestaña `✓ Resumen` debe estar disponible siempre y funcionar como la vista acumulada de la bitácora de S3. Mostrar exclusivamente trabajo real del estudiante:

- predicciones;
- observaciones de contexto;
- rondas de autonomía y apoyos requeridos;
- consultas y acciones de control;
- decisiones de transferencia;
- evidencias reales;
- dificultades, errores y correcciones;
- checksums y decisión sobre integridad;
- texto para `protocolo.md`;
- reflexión final;
- registro pendiente o completado de revisión con IA.

Para campos sin contenido usar `Pendiente` o `Sin respuesta`.

Incluir el botón `⬇ Descargar resultados de la práctica`. Debe generar un `.md` mediante JavaScript usando `Blob`, `URL.createObjectURL` y `<a download>`, sin backend. Sugerir el nombre `u2-s3-bitacora-interactiva-resultados.md`.

El Markdown debe contener solo secciones pertinentes y trabajo real:

```markdown
# Sesión 3 — Bitácora de laboratorio

## Antes de conectarme
## De acompañamiento a autonomía
## Orientarme, consultar y controlar
## Transferencia de datos y metadatos
## Verificación de integridad
## Errores, pistas y correcciones
## Borrador para protocolo.md
## Revisión crítica con IA
## Reflexión final
```

Agregar también `⬇ Descargar borrador para protocolo.md`, que exporte solo la documentación del procedimiento real. Cuando corresponda, ofrecer `⬇ Descargar plantilla para bitacora-ia.md` como plantilla vacía y claramente marcada para completar después; no generar una bitácora de IA con información inventada.

## Diseño visual y accesibilidad

Usar diseño universitario moderno y sobrio: azul oscuro institucional, badge dorado `LCG UNAM 2026`, fondos claros, buena jerarquía, código y nombres de archivo en tipografía monoespaciada. Evitar apariencia infantil, encabezados enormes y exceso de tarjetas.

Implementar HTML semántico, `label`, `fieldset`, `legend`, foco visible, navegación por teclado, contraste adecuado y `aria-live` para retroalimentación. Implementar pestañas con `role="tablist"`, `role="tab"`, `role="tabpanel"` y `aria-selected`.

## Restricciones técnicas

Entregar un único HTML autónomo con HTML, CSS y JavaScript. Debe funcionar completamente offline, incluso sin conexión a Internet.

No usar React, frameworks, backend, login, tracking, APIs, CDNs, Tailwind CDN, Bootstrap CDN, Google Fonts, Font Awesome, scripts externos, hojas de estilo externas ni ninguna dependencia remota. Incluir todo CSS y JavaScript directamente dentro del HTML. Usar fuentes del sistema y recursos visuales creados con CSS o texto cuando hagan falta.

## Validación funcional obligatoria

Antes de entregar, comprobar que:

1. La app abre correctamente.
2. Todas las pestañas funcionan y se puede navegar libremente.
3. Nada aparece precontestado.
4. Las respuestas persisten al cambiar de pestaña y con `localStorage`.
5. Resumen abre siempre y refleja solo trabajo real.
6. Las descargas Markdown funcionan y contienen información real.
7. Reiniciar práctica funciona con confirmación.
8. Una actividad incompleta o un error no rompe la app.
9. La app conserva diseño y funcionalidad con el equipo completamente desconectado de Internet.
10. El HTML no carga CDNs, fuentes, scripts, estilos ni otros recursos remotos.

## Validación pedagógica obligatoria

Antes de entregar, comprobar que:

1. La app conserva la progresión P1 → P2 → P3 → P4 → P5 → documentación.
2. No adelanta contenidos de S4.
3. No simula ni sustituye herramientas reales.
4. El estudiante decide antes de recibir corrección.
5. Las pistas ayudan sin regalar la solución.
6. La app distingue presencia de un archivo e integridad comprobada.
7. Datos y metadatos permanecen vinculados durante la transferencia.
8. La IA aparece después del trabajo manual y como revisora crítica.
9. El Resumen documenta razonamiento, evidencia, errores y correcciones, no solo aciertos.
10. Cada campo solicitado aporta una decisión, evidencia, dificultad, corrección o reflexión; no se pide registrar por rutina.

Devuélveme el HTML COMPLETO, autónomo y funcional. No un parche. No fragmentos.
