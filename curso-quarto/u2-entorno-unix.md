# Unidad 2 — Entorno Unix/Linux y cómputo científico

::: {.callout-note title="Aula invertida:"}
Esta unidad se estudia en cuatro sesiones. Antes de cada una leerás las
secciones indispensables del módulo y harás un primer intento breve. Durante el taller ejecutarás en
vivo sobre el servidor del curso, compararás decisiones y corregirás con evidencia. Después
integrarás las correcciones en `doc/protocolo.md` y, cuando corresponda, en `doc/bitacora-ia.md`.
Los primeros intentos son formativos: se evalúa que llegues preparado y puedas explicar tus
decisiones. La entrega calificada de la unidad es la **Tarea 3**.
:::

## Ficha de la unidad

| Elemento | Descripción |
| --- | --- |
| **Sesiones** | S3–S6, cuatro sesiones de 2 horas |
| **Competencia principal** | B. Dominio del entorno Unix y del cómputo científico |
| **Competencias integradas** | A. Trabajo reproducible y comunicación científica; G. Uso responsable de IA |
| **Propósito** | Trabajar con soltura en un servidor remoto: conectarse, navegar, organizar, inspeccionar y proteger los archivos de un proyecto sin alterar los datos originales |
| **Contribución al curso** | Convierte el proyecto que en la Unidad 1 existía en papel en un espacio de trabajo real sobre el servidor del curso, listo para recibir datos biológicos en la Unidad 3 |
| **Ajustes integrados** | **[Reubicado]** el trabajo con cluster y SGE ya no se imparte aquí: se desarrolla en **S29**, después de scripting, cuando un análisis lo justifica |
| **Lectura base** | Material de cada módulo y Buffalo (2015), cap. 3 (filosofía Unix y shell) |
| **Lecturas de consulta** | Shotts (2019), capítulos sobre permisos, procesos y control de trabajos; documentación de OpenSSH |
| **Producto acumulativo** | `~/proyecto/` construido y verificado en el servidor + actualización de `doc/protocolo.md` |
| **Tareas del Plan** | Tarea 3: estructura de directorios del proyecto en el servidor (S4) |

::: {.callout-note title="dónde queda el cluster"}
Esta unidad trabaja en tu *home* del servidor, con archivos
pequeños. No necesitas el planificador de trabajos ni el espacio institucional
`/export/space3/users/$USER`. El cómputo en cluster con SGE se retoma en **S29**, cuando ya tengas
una herramienta propia que valga la pena ejecutar ahí.
:::

## Punto de partida y continuidad

En la Unidad 1 definiste una pregunta, iniciaste `protocolo.md` como documento vivo, elaboraste los
metadatos de `pacientes.md` y **diseñaste en papel** la organización del proyecto. Esta unidad
materializa ese diseño: al terminar, la estructura existirá de verdad, en un servidor, con tus
archivos dentro y con la evidencia de que llegaron intactos.

La estructura a la que se llega es:

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

La política de datos empieza aquí y no cambia en todo el curso: los archivos de `data/source/` se
**leen y se copian, nunca se editan**. Toda transformación genera un archivo nuevo fuera de esa
carpeta (Noble, 2009; Wilson et al., 2017).

## Resultados de aprendizaje de la unidad

Al finalizar, podrás:

1. **Explicar** por qué la bioinformática trabaja en Unix y en la línea de comandos, en términos de
   reproducibilidad.
2. **Identificar** las partes de un comando y **consultar** su ayuda con autonomía.
3. **Conectarte** a un servidor remoto por SSH, reconocer el entorno y salir correctamente.
4. **Transferir** archivos entre tu equipo y el servidor **comprobando su integridad** con
   *checksums*.
5. **Navegar** el sistema de archivos con rutas absolutas y relativas, y **construir** la estructura
   del proyecto con operaciones seguras.
6. **Editar** archivos en el servidor con un editor de terminal.
7. **Inspeccionar** archivos sin modificar los originales y **comprimir y restaurar** una copia.
8. **Conceder** a un archivo el permiso mínimo que necesita y **explicar** qué habilita cada uno.
9. **Ejecutar y controlar** un proceso propio, y **diagnosticar** cómo terminó.
10. **Documentar** el procedimiento en `doc/protocolo.md` de modo que otra persona pueda repetirlo.

## Ruta de aprendizaje

Los tiempos son estimaciones; varían según la experiencia previa y la conectividad.

| Momento | Trabajo | Producto | Tiempo estimado |
| --- | --- | --- | ---: |
| Antes de S3 | Leer S3 y preparar los archivos a transferir; instalar FileZilla si falta | Archivos listos y entorno preparado | 60–75 min |
| S3 | Conectarse por SSH, transferir y verificar integridad | `protocolo.md` transferido y verificado | 120 min |
| Entre S3 y S4 | Leer S4 y hacer el primer intento de la estructura | Borrador de la estructura | 30–45 min |
| S4 | Construir `~/proyecto/` y colocar cada archivo en su lugar | **Tarea 3** iniciada | 120 min |
| Entre S4 y S5 | Leer S5 y predecir resultados dentro de `~/proyecto/` | Predicciones escritas | 40–50 min |
| S5 | Inspeccionar, comprimir, ajustar permisos y controlar un proceso | Registro en `protocolo.md` | 120 min |
| Entre S5 y S6 | Repasar S3–S5 y reunir las evidencias | Evidencias localizadas | 20–30 min |
| S6 | Verificar el entorno completo y dejar el proyecto listo para datos reales | Evidencia de cierre de U2 | 120 min |
| Después de S6 | Corregir el protocolo y entregar | `protocolo.md` y `bitacora-ia.md` | 30–45 min |

## Módulos de la unidad

### [S3 — Conectar: el shell, el acceso remoto y la transferencia de archivos](u2-s3-shell-acceso-remoto.md)

Partiendo de un problema real —trasladar un archivo de datos y sus metadatos al servidor, comprobar
que llegaron intactos y documentar el procedimiento—, abrirás una terminal, entenderás qué es un
comando, te conectarás por SSH y transferirás verificando integridad.

### [S4 — Navegar: el sistema de archivos, su organización y su edición](u2-s4-sistema-archivos-v3.md)

Te moverás por el sistema de archivos con rutas absolutas y relativas, y crearás por primera vez la
estructura real del proyecto en tu espacio del servidor, colocando dentro los archivos ya
transferidos. Esta sesión desarrolla la **Tarea 3**.

### [S5 — Gestionar: archivos, compresión, permisos y procesos](u2-s5-archivos-permisos-procesos-v2.md)

Sin reiniciar el proyecto ni traer datos nuevos, inspeccionarás sus archivos sin modificar los
originales, comprimirás y restaurarás una copia, concederás a un script solo el permiso que necesita
y controlarás un proceso ligero creado por ti.

### [S6 — Consolidar: el entorno Unix listo para datos biológicos](u2-s6-consolidacion-entorno-unix.md)

No construirás nada nuevo: demostrarás que lo construido está bien. Comprobarás el acceso, la
estructura, la integridad de los originales y los permisos; someterás tu protocolo a la lectura de
otra persona; y dejarás el proyecto listo para recibir datos que no inventaste tú. **No introduce
herramientas nuevas** y **no cubre cluster ni SGE**, que se desarrollan en S29. Esta sesión produce la
**evidencia de cierre de la Unidad 2**.

## Producto acumulativo: el proyecto en el servidor

El proyecto se transfiere en S3, se estructura en S4, se protege e inspecciona en S5 y se verifica en
S6. Al cerrar la unidad debe cumplir:

- la estructura completa existe en el servidor y cada archivo está en la carpeta que le corresponde;
- `data/source/` conserva los originales **sin modificaciones**, y puedes demostrarlo con un
  *checksum* comparable con el de tu equipo;
- `doc/protocolo.md` registra el procedimiento de transferencia, la construcción de la estructura y
  las decisiones de permisos, con comandos suficientes para repetirlo;
- `doc/bitacora-ia.md` está en el servidor y recoge los usos de IA declarados;
- `README.md` describe qué contiene el proyecto y cómo está organizado.

::: {.callout-important}
Si algo no se pudo comprobar, escríbelo como “pendiente de confirmar” en el
protocolo. Una limitación declarada vale más que una afirmación no verificada.
:::

## Evidencias y evaluación

| Evidencia | Momento | Tipo | Qué demuestra |
| --- | --- | --- | --- |
| Transferencia verificada con *checksum* | S3 | Formativa | Acceso remoto y control de integridad |
| **Tarea 3** — estructura del proyecto en el servidor | Después de S4 | Calificada | Navegación, operaciones seguras y organización reproducible |
| Ejercicios de permisos y procesos | S5 | Formativa | Inspección sin alterar originales, permiso mínimo y control de procesos |
| Evidencia de cierre de U2 | S6 | Calificada | Entorno completo y verificable, listo para datos reales |
| `doc/protocolo.md` | S3–S6 | Acumulativa | Decisiones, comandos, verificaciones y limitaciones |
| `doc/bitacora-ia.md` | S3–S6 | Formativa | Uso declarado de IA, comparación y validación independiente |

## Cierre de la Unidad 2

Al terminar verifica que puedes responder:

- ¿Por qué la bioinformática trabaja en Unix y no en una interfaz gráfica?
- ¿Qué diferencia hay entre tu equipo y el servidor, y cómo sabes en cuál de los dos estás?
- ¿Qué evidencia demuestra que un archivo llegó íntegro al servidor?
- ¿Cuándo conviene una ruta absoluta y cuándo una relativa?
- ¿Dónde viven los datos originales y por qué no se editan nunca ahí?
- ¿Qué habilita cada permiso y cuál es el mínimo que un script necesita?
- ¿Cómo compruebas que un proceso terminó bien y no solo que terminó?
- ¿Podría otra persona repetir tu procedimiento leyendo solo tu `protocolo.md`?

Confirma además que conservas las evidencias de S3, S4 y S5, y que tu proyecto en el servidor cumple
las condiciones del producto acumulativo.

En este momento **no** necesitas el cluster ni el espacio institucional: el planificador de trabajos
se retomará en **S29**, después de practicar procesamiento de datos y scripting, cuando un análisis
bioinformático justifique ejecutarlo en otra infraestructura.

El entorno que dejas listo aquí es donde la **Unidad 3** colocará los primeros datos biológicos
reales, con su procedencia y su verificación de integridad.

## Referencias generales

- Buffalo, V. (2015). *Bioinformatics Data Skills*. O’Reilly Media.
- Noble, W. S. (2009). A quick guide to organizing computational biology projects. *PLoS
  Computational Biology*, 5(7), e1000424. <https://doi.org/10.1371/journal.pcbi.1000424>
- Shotts, W. E. (2019). *The Linux Command Line* (2.ª ed.). No Starch Press.
- Wilson, G., et al. (2017). Good enough practices in scientific computing. *PLoS Computational
  Biology*, 13(6), e1005510. <https://doi.org/10.1371/journal.pcbi.1005510>
