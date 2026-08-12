# Unidad 5 — Automatización de análisis bioinformáticos con Shell

> **NOTA — Cómo se estudia esta unidad.** La Unidad 5 no es un documento único: es esta portada más
> **seis módulos** de dos horas, **S24 a S29**. Cada módulo se lee **antes** de su sesión, trae su
> propio primer intento, su taller y su entrega posterior, y es autocontenido. Esta portada te da la
> visión de conjunto: qué problema resuelve la unidad, en qué orden, qué producto se construye y cómo
> se evalúa. Léela una vez, al empezar, y vuelve a ella cuando quieras situarte.

## De qué trata esta unidad

Al cerrar la Unidad 4 conseguiste algo que no tenías: un **protocolo ejecutable**. Una secuencia
ordenada y verificada que lleva de los archivos originales de tu genoma a una síntesis interpretada,
con sus dependencias declaradas y sus puntos de control escritos. Lo probaste desde cero y funcionó.

Y funcionó porque tú estabas delante.

```text
copiar treinta comandos, otra vez
editar la ruta del genoma en cada uno
recordar en qué orden iban
detenerte a comprobar entre bloques
y repetirlo entero cada vez que cambie un archivo
```

Nada de eso es difícil. Es **tedioso y propenso a error**, que en ciencia es peor que difícil: un
error de copiado no avisa. La Unidad 5 se construye alrededor de la pregunta que sale de ahí:

> **¿Cómo hago que un procedimiento se ejecute solo, muchas veces, sobre datos distintos?**

De ella se desprende un conjunto pequeño y estable de preguntas, que son las que ordenan las cinco
sesiones:

- ¿Cómo guardo un procedimiento para que se ejecute sin que nadie lo copie?
- ¿Cómo hago que el mismo procedimiento sirva para datos distintos?
- ¿Cómo lo aplico a muchos casos sin escribirlo muchas veces?
- ¿Cómo sé que hizo lo que yo creía, si ya no estoy mirando la pantalla?
- ¿Cómo dejo registro de lo que hizo, para que otra persona pueda repetirlo?
- ¿Y cuándo un análisis deja de caber en mi sesión de terminal y necesita otra infraestructura?

### La distinción que gobierna toda la unidad

Cada unidad del curso tiene una distinción rectora. En la Unidad 4 fue *un registro no es un objeto
biológico*. En la Unidad 5 es esta:

```text
UN COMANDO                        UN SCRIPT
resuelve un caso                  resuelve una CLASE de casos
lleva los datos dentro            recibe los datos desde fuera
se ejecuta y se olvida            queda como archivo del proyecto
si falla, lo ves                  si falla, puede no verse
```

De ahí sale la frase que conviene tener presente las cinco sesiones:

> **Automatizar no es guardar comandos. Es separar el procedimiento de sus datos.**

Un archivo con los mismos comandos de siempre y las rutas escritas dentro no es automatización: es un
apunte ejecutable. Lo que lo convierte en herramienta es la **parametrización** —la frontera entre lo
que cambia y lo que permanece—, y esa frontera es una decisión de diseño, no una construcción de
shell.

### Lo que cambia respecto a la Unidad 4

| Dimensión | Unidad 4 | Unidad 5 |
| --- | --- | --- |
| Objeto de trabajo | Un archivo y sus registros | **Un procedimiento** |
| Pregunta rectora | ¿Qué contiene y cuánto mide este genoma? | ¿Cómo repito este análisis sin repetirme? |
| Unidad de trabajo | Una línea de comando, un resultado | Un archivo en `src/`, muchos resultados |
| Quién ejecuta | Tú, mirando cada salida | El intérprete, sin nadie mirando |
| Naturaleza del error | Puntual y visible: la salida sale rara | **Sistemático y silencioso**: muchos archivos mal, sin aviso |
| Qué protege del error | Que tú lo notes | Que el script lo compruebe y lo diga |
| Producto | Protocolo que una persona ejecuta | **Herramienta que se ejecuta sola** |

La penúltima fila es la que más importa y aparece ya en S24. En la Unidad 4, si una estrategia de
conteo estaba mal, el número salía raro y tú lo veías. En la Unidad 5 el mismo error se multiplica por
cada ejecución y **nadie lo mira**. Por eso la validación de entradas, los mensajes de error y los
puntos de control no son un refinamiento final de la unidad: **son su contenido**.

> **IDEA CLAVE de la unidad.** Un script no se juzga por lo que hace cuando todo va bien, sino por
> **lo que hace cuando algo falta**.

## Ficha de la unidad

| Elemento | Descripción |
| --- | --- |
| **Sesiones** | S24 a S29 · 2 h cada una · Plan de clases 2026 ajustado (32 sesiones) |
| **Competencia principal** | E. Automatización y programación en shell |
| **Competencias integradas** | A. Trabajo reproducible; B. Entorno Unix; D. Análisis de datos genómicos; G. Uso responsable de la IA |
| **Propósito** | Transformar un protocolo manual reproducible en una herramienta reutilizable capaz de automatizar análisis bioinformáticos sencillos, validar entradas, organizar resultados y documentar su ejecución |
| **Contribución al objetivo del curso** | Cierra el eje de reproducibilidad: lo que en U1 era una promesa documental y en U4 un procedimiento verificado, aquí se vuelve un objeto ejecutable y compartible |
| **Ajustes integrados** | Scripting agrupado en un bloque limpio [Nuevo]; proyecto integrador que **sustituye al examen práctico 2** [Reorganizado]; módulo de HPC reubicado al cierre de la unidad [Reubicado] |
| **Datos de trabajo** | Los mismos de la Unidad 4: FASTA y GFF3 del genoma propio, más el conjunto de genomas del curso para el procesamiento por lotes |
| **Lectura obligatoria (con evidencia)** | Buffalo (2015), Cap. 12 — *Bioinformatics Shell Scripting, Writing Pipelines, and Parallelizing Tasks*, secciones sobre scripts y pipelines (~90 min, evidencia en S26) |
| **Lectura de consulta** | Taschuk & Wilson (2017), *Ten simple rules for making research software more robust* (~30 min, se trabaja en S27); Buffalo, Cap. 2 (organización de proyectos, repaso); documentación del clúster institucional (S29) |
| **Evidencia integradora** | Una herramienta bioinformática reutilizable: recibe FASTA y GFF3, valida sus entradas, automatiza el flujo de la Unidad 4, organiza los resultados, produce un reporte y registra su ejecución — con su `README`, su presentación y su declaración de uso de IA (S28) |
| **Infraestructura** | `chaac.lcg.unam.mx`, planificador **SGE** (S29; retoma S6) |
| **Producto acumulativo** | `doc/protocolo.md`, que **no se reinicia**: pierde los comandos y conserva el razonamiento, y pasa a citar los scripts |

## Resultados de aprendizaje de la unidad

Al finalizar la Unidad 5 podrás:

1. **Explicar** en qué se diferencia un procedimiento documentado de una herramienta ejecutable, y
   por qué el segundo no sustituye al primero.
2. **Escribir** un script que reproduzca un flujo de análisis completo, con su encabezado, sus
   comentarios y sus permisos.
3. **Separar** el procedimiento de sus datos mediante variables y parámetros de entrada, y justificar
   dónde trazaste esa frontera.
4. **Validar** las entradas de un script antes de trabajar con ellas, y hacer que se detenga con un
   mensaje útil cuando algo falta.
5. **Procesar** un conjunto de archivos biológicos con un ciclo, organizando las salidas de forma que
   cada resultado sea identificable.
6. **Construir** un reporte que resuma todas las ejecuciones y responda una pregunta que **ningún
   caso individual** podía responder.
7. **Documentar** una herramienta para que otra persona la use sin preguntarte nada: propósito,
   entradas, salidas, invocación y limitaciones.
8. **Contrastar** todo resultado automatizado contra el resultado manual conocido de la Unidad 4, y
   explicar cualquier diferencia.
9. **Evaluar críticamente** el código propuesto por una IA, identificando construcciones fuera de
   alcance, supuestos no declarados y riesgos sobre los datos originales.
10. **Interpretar biológicamente** los resultados del análisis automatizado, con sus evidencias y sus
    límites.
11. **Decidir** cuándo un análisis justifica ejecutarse en un clúster, y **enviar, monitorear y
    cancelar** un trabajo con el planificador institucional.

> **NOTA — nivel real de la unidad.** *Escribir*, *validar* y *procesar* se ejecutan; *construir una
> herramienta documentada* se diseña y se ejecuta en su versión mínima. Esta unidad **no** forma
> programadores: forma personas capaces de automatizar con criterio un análisis que ya entienden.

## Ruta de la unidad

Seis movimientos. Cada uno resuelve la limitación que dejó abierta el anterior.

```text
    protocolo ejecutable (S23)
            ↓
S24  GUARDAR      el procedimiento    ¿cómo lo ejecuto sin copiarlo?
            ↓
S25  SEPARARLO    de sus datos        ¿cómo sirve para otro genoma?
            ↓
S26  REPETIRLO    sin repetirte       ¿cómo lo aplico a muchos?
            ↓
S27  ENTREGARLO   a otra persona      ¿cómo lo usa alguien que no soy yo?
            ↓
S28  INTEGRARLO   todo                la herramienta completa, sobre datos nuevos
            ↓
S29  ESCALARLO    fuera de mi sesión  ¿y cuando ya no cabe en mi terminal?
            ↓
    herramienta bioinformática reutilizable, y dónde ejecutarla
```

| Sesión | Módulo | Qué resuelve | Con qué limitación cierra |
| --- | --- | --- | --- |
| **S24** | [`u5-s24-del-protocolo-al-script.md`](u5-s24-del-protocolo-al-script.md) — *Guardar: del protocolo ejecutable al script* | El análisis deja de copiarse: se ejecuta con una orden | Las rutas están dentro del archivo: sirve para **este** genoma, y no comprueba nada |
| **S25** | [`u5-s25-separar-procedimiento-datos.md`](u5-s25-separar-procedimiento-datos.md) — *Separar el procedimiento de sus datos* | El dato entra desde fuera; el script comprueba sus entradas y se detiene si falta algo | Sirve para cualquier genoma, **de uno en uno** |
| **S26** | [`u5-s26-procesamiento-por-lotes.md`](u5-s26-procesamiento-por-lotes.md) — *De un genoma a una colección: el análisis por lotes* | Un conjunto completo se procesa con una orden, y el resumen responde una pregunta nueva | Funciona, y aun así otra persona no sabría usarlo |
| **S27** | [`u5-s27-herramienta-cientifica.md`](u5-s27-herramienta-cientifica.md) — *De un script que funciona a una herramienta que otros usan* | Organización, documentación, mensajes, registro de parámetros y pruebas | La herramienta se puede usar, pero aún no se ha sostenido con argumentos |
| **S28** | [`u5-s28-proyecto-integrador.md`](u5-s28-proyecto-integrador.md) — *Defender: demostrar que una herramienta es reproducible* | Se demuestra el recorrido entero con datos nuevos y se sostiene con evidencia | La ejecución sigue atada a tu sesión de terminal |
| **S29** | [`u5-s29-cluster-hpc-sge.md`](u5-s29-cluster-hpc-sge.md) — *Escalar: la misma herramienta, otra infraestructura* | El trabajo se envía a un planificador, se monitorea y se demuestra que el resultado es idéntico | Puerta hacia la comparación de secuencias a escala (U6) |

> **NOTA — los títulos del Plan.** El Plan de clases nombra estas sesiones por su contenido (*Del
> protocolo al script*, *Variables, parámetros y validaciones*, *Automatización por lotes*…). Aquí se
> titulan por **lo que resuelven**, conforme a la regla editorial del curso: ninguna sesión lleva el
> nombre de una herramienta ni de una construcción del lenguaje. El contenido es exactamente el del
> Plan.

### Qué se hace en cada momento

| Momento | Qué leer | Qué intentar | Qué llevar / entregar | Tiempo estimado |
| --- | --- | --- | --- | ---: |
| **Antes de S24** | Portada + módulo S24, secciones 1–6 | Elegir el fragmento a automatizar y predecir los fallos | `doc/s24-primer-intento.md` | 50 + 40 min |
| **S24** | — | Escribir, ejecutar y diagnosticar el primer script | `src/analizar-genoma.sh` | 2 h |
| **Entre S24 y S25** | Buffalo Cap. 12, primera mitad | Ampliar el script a la ruta crítica y validarlo | Registro de validación | 90 min |
| **S25** | Módulo S25 | Parametrizar y validar | Script que recibe el genoma desde fuera | 2 h |
| **Entre S25 y S26** | Buffalo Cap. 12, segunda mitad | Probar el script con un genoma que no es el tuyo | Reporte de lectura (evidencia) | 90 min |
| **S26** | Módulo S26 | Procesar el conjunto y construir el reporte | Reporte del lote | 2 h |
| **Entre S26 y S27** | Taschuk & Wilson (2017) | Auditar la propia herramienta contra las diez reglas | Lista de mejoras priorizadas | 60 min |
| **S27** | Módulo S27 | Documentar, organizar y probar | Herramienta documentada con su `README` | 2 h |
| **Entre S27 y S28** | — | Prueba final e integración; preparar la presentación | Herramienta completa | 120 min |
| **S28** | Módulo S28 | Ejecutar sobre datos nuevos, revisión por pares y presentación | **Evidencia integradora** | 2 h |
| **Antes de S29** | Módulo S29 + documentación del clúster | Estimar qué recursos pediría tu análisis | Borrador del *job script* | 45 min |
| **S29** | Módulo S29 | Enviar, monitorear y cancelar un trabajo; revisar `.out` y `.err` | Registro del trabajo enviado | 2 h |

Los tiempos son **estimaciones**. Las secciones marcadas `[Indispensable]` en cada módulo se leen
siempre; las marcadas `[Consulta]` pueden dejarse para después del taller.

## Matriz de evolución de las preguntas

Ninguna pregunta se responde de una vez: se responde con lo disponible y se refina cuando aparece la
construcción que corrige su limitación. Es el mismo motor que ordenaba la Unidad 4.

| # | Pregunta | 1.ª aparición | Estrategia inicial y su límite | Cómo se refina | Resuelta en |
| --- | --- | --- | --- | --- | --- |
| Q1 | ¿Cómo repito el análisis de la Unidad 4? | S24 | Releer el protocolo y copiar comando por comando | **S24 · script**: un archivo que el sistema ejecuta en orden | S24 |
| Q2 | ¿Cómo lo aplico a otro genoma? | S24 (cierre) | Abrir el script y editar todas las rutas | **S25 · parámetros**: el dato entra desde fuera, el archivo no se toca | S25 |
| Q3 | ¿Cómo sé que el script hizo lo correcto? | S24 | Confiar en que terminó sin error | **S24 · comparación con el resultado manual** · **S25 · validación de entradas** · **S26 · control sobre el lote** | S26 |
| Q4 | ¿Qué pasa si falta el archivo o el argumento? | S24 | El script sigue y produce basura convincente | **S25 · comprobación, mensaje de error y salida con código distinto de cero** | S25 |
| Q5 | ¿Cómo lo aplico a doce genomas? | S26 | Invocarlo doce veces a mano | **S26 · ciclo** sobre el conjunto, con salidas identificables | S26 |
| Q6 | ¿Qué puedo decir del **conjunto** de genomas que no podía decir de ninguno? | S26 | No se podía preguntar: hacía falta el conjunto entero | **S26 · reporte** que resume todas las iteraciones | S26 |
| Q7 | ¿Dónde quedan todos los archivos de salida? | S26 | En el directorio de trabajo, mezclados | **S26 · nombres derivados y organización de `results/`** | S26 |
| Q8 | ¿Puede usar esto alguien que no soy yo? | S27 | Enviarle el archivo y explicárselo | **S27 · documentación de uso, mensajes y pruebas** | S27 |
| Q9 | ¿Funciona con datos que nunca ha visto? | S28 | Se supone que sí | **S28 · ejecución sobre datos nuevos, revisión por pares y presentación** | S28 |
| Q10 | ¿Y si el análisis no cabe en mi sesión de terminal? | S26 | Esperar a que termine, sin cerrar la conexión | **S29 · envío a un planificador**: el trabajo deja de depender de que tu sesión siga abierta | S29 |
| Q11 | ¿Qué son estos genes y existen en otros organismos? | S29 (cierre) | No se puede responder desde los archivos propios | **Unidad 6 · comparación de secuencias** | U6 |

> **Criterio de diseño.** **Q6 es la pregunta más importante de la unidad**: es la única que no
> existía antes del ciclo. Si al llegar a S26 el ciclo te parece una comodidad y no un cambio en lo
> que puedes preguntar, vuelve a esta fila.

## Evidencia integradora y su evolución

El producto de la unidad es **una herramienta**, y se construye por capas: cada sesión añade una y
ninguna tira lo anterior.

| Sesión | Qué añade a la herramienta | Archivo |
| --- | --- | --- |
| **S24** | El procedimiento, ejecutable y comentado | `src/analizar-genoma.sh` |
| **S25** | Los parámetros y la validación de entradas | `src/analizar-genoma.sh` (v2, parametrizado) |
| **S26** | El recorrido del conjunto y el reporte | `src/procesar-lote.sh` + `results/` organizado |
| **S27** | La documentación de uso, el registro de parámetros y las pruebas | `src/`, `README` del proyecto, `doc/` |
| **S28** | La demostración sobre datos nuevos, la revisión por pares y su interpretación biológica | La herramienta completa + reporte + presentación + declaración de uso de IA |
| **S29** | Dónde ejecutarla cuando el conjunto crece | *Job script* + registro de `.out` y `.err` |

### Criterios de la evidencia integradora

| Criterio | Qué se comprueba |
| --- | --- |
| Recibe parámetros | El script no contiene ninguna ruta ni identificador fijo que debiera venir de fuera |
| Valida las entradas | Comprueba lo que necesita, avisa por el canal de error y termina con un código distinto de cero |
| Documenta su uso | Encabezado con propósito, entradas, salidas y una línea de ejemplo de invocación |
| Procesa un conjunto | Recorre varios archivos y deja una salida por cada uno, con nombre identificable |
| Produce un reporte | Una tabla que resume todas las iteraciones y **responde una pregunta biológica** |
| Es verificable | Se compara contra el resultado manual de la Unidad 4, y el documento declara la coincidencia |
| Respeta los originales | No escribe, mueve ni modifica nada en `data/source/` |
| Deja registro | El protocolo cita cada script, sus parámetros y la fecha de ejecución |
| Se interpreta | El resultado del lote termina en una afirmación biológica con sus límites, no en «el script corrió» |

## El protocolo en esta unidad

`doc/protocolo.md` es el mismo documento que abriste en la Unidad 1 y **nunca se reinicia**. En la
Unidad 5 sufre un cambio de estatus que conviene entender bien, porque es donde más gente se
equivoca:

| | Hasta S23 | Desde S24 |
| --- | --- | --- |
| Los comandos exactos viven en… | `doc/protocolo.md` | `src/` |
| El protocolo contiene… | el comando y su razonamiento | el **razonamiento**, y una **cita** del script |
| Para reproducir hay que… | leer el protocolo y copiar | ejecutar la herramienta |
| Para entender **por qué** hay que… | leer el protocolo | leer el protocolo |

> **IMPORTANTE — el protocolo no se vacía.** Pierde una función y conserva la más importante. Las
> decisiones metodológicas —la definición de gen, la política de normalización, el universo
> comparable, las fórmulas y unidades— siguen exactamente donde estaban, porque un script no las
> contiene ni las puede contener. Quien reciba tu herramienta sin tu protocolo podrá obtener tus
> números y **no sabrá defenderlos**.

Cada sesión añade su apartado, sin sustituir ninguno anterior:

| Sesión | Apartado nuevo en `doc/protocolo.md` |
| --- | --- |
| S24 | *Automatización del protocolo: primer script* — ficha del script, correspondencia con los bloques, validación frente al trabajo manual y limitaciones |
| S25 | *Parametrización y validación* — qué entra desde fuera, qué se comprueba y qué ocurre cuando falta |
| S26 | *Análisis en lote* — qué conjunto se recorrió, dónde quedaron los resultados y qué dice el reporte |
| S27 | *La herramienta* — organización, documentación de uso, registro de parámetros, pruebas realizadas y errores encontrados |
| S28 | *Cierre de la unidad* — ejecución sobre datos nuevos, interpretación biológica, limitaciones globales y preguntas abiertas |
| S29 | *Ejecución en el clúster* — qué análisis se envió, con qué recursos, qué devolvieron `.out` y `.err` y qué criterio justifica usar HPC |

## Los cuatro principios, en esta unidad

- **Reproducibilidad.** Deja de ser una aspiración y se vuelve un archivo. Un script con sus
  parámetros y su bloque de uso **es** el registro del análisis (Sandve et al., 2013).
- **Verificación.** Cada script comprueba sus entradas antes de trabajar y avisa si algo falta. Un
  script que continúa con una entrada inexistente produce basura convincente.
- **Validación.** El resultado automatizado se contrasta contra el resultado manual conocido de la
  Unidad 4. La primera vez que se ejecuta un script, la pregunta no es «¿funcionó?» sino **«¿da lo
  mismo que a mano?»**.
- **Robustez.** Se prueba con lo que no está previsto —un archivo vacío, un nombre con espacios, un
  genoma que no existe— y se decide qué debe pasar en cada caso (Taschuk & Wilson, 2017).

## Lo que esta unidad NO enseña

Esta lista importa tanto como el temario, porque el riesgo de la unidad es convertirse en un curso de
programación.

**Queda explícitamente fuera:** funciones definidas por el usuario; `while` y `until`; `case`;
arreglos; `getopts`; sustitución aritmética `$((...))`; expresiones regulares dentro de `[[ ]]`;
`set -euo pipefail`; `trap`; procesos en segundo plano y paralelismo; `xargs`; scripts de Python o R.

**Criterio:** cuatro construcciones bien dominadas —**variable, parámetro, condición simple y
ciclo**— bastan para todo lo que la unidad necesita. Una quinta construcción que no se use en ningún
ejercicio es contenido muerto.

> **NOTA — sobre `set -e`.** Es tentador incluirlo como buena práctica. Se deja fuera a propósito: su
> comportamiento con tuberías y con condiciones tiene excepciones que un primer semestre no puede
> distinguir, y da una falsa sensación de seguridad. La comprobación explícita enseña más y engaña
> menos.

**Tampoco se desarrollan aquí:** BLAST, alineamientos, homología ni comparación de secuencias. Cuando
la limitación aparezca —sobre todo al cierre de S29— se nombra como puerta hacia la Unidad 6, sin
desarrollarla.

**En S29, sobre HPC, se trabaja a nivel usuario:** arquitectura del clúster, *job script* mínimo,
`qsub`, `qstat`, `qdel` y lectura de `.out` y `.err`. Quedan explícitamente para cursos posteriores
los hilos (*threads*), los *array jobs* y el paralelismo con herramientas externas.

## Uso crítico de la IA en esta unidad

La política completa está en el [`README.md`](README.md) de esta carpeta y se aplica sin cambios:
**primero a mano, después con IA**, con validación independiente y registro en `doc/bitacora-ia.md`.

Esta unidad merece un aviso propio, y conviene leerlo antes de S24:

> **ADVERTENCIA:** Pedir un script es lo que mejor hace un asistente, y por eso es donde resulta más
> fácil aceptar código que no entiendes. Un comando mal copiado se nota; un script mal entendido, no.
> Además, los asistentes proponen casi siempre construcciones que esta unidad excluye —`set -e`,
> funciones, `while`, `getopts`—, y un script que escribe en el sitio equivocado puede destruir un
> archivo original sin preguntar. **Si no puedes explicar una línea, no entra en tu `src/`.**

Cada módulo incluye su cierre *clásico vs. asistido*, construido sobre tareas que ya resolviste a
mano.

## Evaluación

| Momento | Qué se evalúa | Tipo |
| --- | --- | --- |
| Primer intento de cada módulo | Preparación: predicciones, auditorías y decisiones tomadas antes del taller | Formativa, con puntos por preparación |
| Participación en el taller | Diagnóstico, comparación con el resultado manual, argumentación | Formativa |
| Reporte de lectura (Buffalo, Cap. 12) | Comprensión de la lectura obligatoria | Con calificación |
| Evidencia de S25 | Script parametrizado que valida sus entradas | Con calificación |
| Evidencia de S26 | Procesamiento por lotes con resultados separados y su reporte | Con calificación |
| Avance de S27 | Herramienta documentada, probada y reproducible | Con calificación |
| **Evidencia integradora (S28)** | Script reutilizable + `README` + reporte + presentación + declaración de uso de IA | Con calificación |
| Evidencia de S29 | Trabajo enviado, monitoreado y finalizado o cancelado, con revisión documentada de `.out` y `.err` | Con calificación |

> **IMPORTANTE — no hay examen práctico en esta unidad.** El Plan de clases ajustado sustituye el
> examen práctico 2 por el **proyecto integrador de S28**: la evaluación se hace sobre un producto
> auténtico, no sobre un ejercicio aislado. Lo que se demuestra es el recorrido completo —comandos →
> protocolo → script → herramienta— y la capacidad de sustentarlo ante otras personas.

Las rúbricas detalladas, con descriptores en tres niveles —*Logrado / Parcialmente logrado / Aún no
logrado*—, están en cada módulo.

## Qué llevas acumulado al terminar

| Unidad | Qué sabías hacer al cerrarla |
| --- | --- |
| U1 | Documentar un análisis y organizar un proyecto de forma reproducible |
| U2 | Moverte en un entorno Unix remoto y operar archivos, permisos y procesos |
| U3 | Obtener datos biológicos y demostrar que son los que dices tener |
| U4 | Interrogar un genoma y construir evidencia: seleccionar, identificar, normalizar, confrontar, cuantificar e integrar |
| **U5** | **Convertir ese razonamiento en una herramienta que se ejecuta sola, sobre datos distintos, y que otra persona puede usar** |

El mensaje central de la unidad cabe en una línea, y conviene tenerlo presente desde S24:

> **Una herramienta bioinformática es la evolución natural de un protocolo científico reproducible —
> no un atajo para saltárselo.**

Automatizar un flujo que no entiendes produce errores más rápido. Por eso esta unidad viene **después**
de la Unidad 4 y no antes.

## Referencias

- Barker, M., Chue Hong, N. P., Katz, D. S., Lamprecht, A.-L., Martinez-Ortiz, C., Psomopoulos, F.,
  et al. (2022). Introducing the FAIR Principles for research software. *Scientific Data*, 9, 622.
  <https://doi.org/10.1038/s41597-022-01710-x>
- Buffalo, V. (2015). *Bioinformatics Data Skills*. O'Reilly Media. — Cap. 12, *Bioinformatics Shell
  Scripting, Writing Pipelines, and Parallelizing Tasks*; Cap. 2, organización de proyectos.
- Free Software Foundation. (2024). *GNU Bash Reference Manual*.
  <https://www.gnu.org/software/bash/manual/bash.html>
- Noble, W. S. (2009). A quick guide to organizing computational biology projects. *PLoS
  Computational Biology*, 5(7), e1000424. <https://doi.org/10.1371/journal.pcbi.1000424>
- Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible
  computational research. *PLoS Computational Biology*, 9(10), e1003285.
  <https://doi.org/10.1371/journal.pcbi.1003285>
- Taschuk, M., & Wilson, G. (2017). Ten simple rules for making research software more robust. *PLoS
  Computational Biology*, 13(4), e1005412. <https://doi.org/10.1371/journal.pcbi.1005412>
- Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough
  practices in scientific computing. *PLoS Computational Biology*, 13(6), e1005510.
  <https://doi.org/10.1371/journal.pcbi.1005510>

---

> **NOTA DOCENTE — no forma parte del material del estudiante.**
>
> **Plan operativo de referencia.** `Plan-Clases-BioInfo-2026-final-S34.xlsx`, pestaña
> **`PlanClases-2026-final S34`** (34 sesiones). Es la única pestaña vigente; las anteriores
> ---incluida `PlanClases-2026-HPC`, de 32 sesiones--- se conservan solo como historial.
>
> **Parámetros de la unidad** (según `plantilla-unidad.md` §3):
>
> | Parámetro | Unidad 5 |
> | --- | --- |
> | Sesiones (plan) | S24–S29 |
> | Competencias | E (principal); A, B, D, G (integradas) |
> | Ajustes integrados | Scripting en bloque limpio [Nuevo]; S28 sustituye al examen práctico 2 [Reorganizado]; HPC reubicado a S29 [Reubicado] |
> | Lectura obligatoria (con evidencia) | Buffalo, Cap. 12 |
> | Lectura de consulta | Taschuk & Wilson (2017); Buffalo, Cap. 2; documentación del clúster |
> | Dataset(s) de ejemplo | FASTA y GFF3 del genoma propio (U3–U4); conjunto de genomas del curso |
> | Evidencias del plan | S24 primer script · S25 script parametrizado · S26 lote con resultados separados · S27 herramienta documentada · **S28 evidencia integradora** · S29 trabajo en el clúster |
> | Infraestructura | `chaac.lcg.unam.mx`, planificador SGE (S29) |
> | Tareas para el "Cierre con IA" | S24: conversión del protocolo a script; S26: propuesta de ciclo y su fallo silencioso; S27: revisión clásica vs. asistida de la herramienta |
>
> **Alineación con el Plan ajustado.** Las siete discrepancias registradas contra el plan anterior
> quedan **resueltas**: el plan ajustado sitúa U5 en S24–S29 en bloque limpio, confirma que S28
> sustituye al examen práctico 2, elimina la Tarea 8 de BLAST del bloque de scripting, reubica HPC en
> S29 y lleva la Unidad 6 a S30–S32 (alineamientos · BLAST · homología). No queda ninguna discrepancia
> abierta en esta unidad.
>
> **Dos observaciones para revisión, no discrepancias:**
>
> 1. **S6 y S29 se solapan parcialmente.** Ambas presentan la arquitectura del clúster y el ciclo
>    `qsub`/`qstat`/`qdel`. Conviene decidir el reparto: S6 como panorama a nivel usuario y S29 como
>    construcción del *job script* sobre el pipeline propio, con S29 remitiendo a S6 sin repetir. El
>    borrador existente `docente/u2-s6-cluster-hpc.md` es material de partida para **S29**.
> 2. **S29 se declara como U5 en el Plan.** Es coherente —el trabajo que se envía es el pipeline de la
>    propia unidad—, pero conviene que el módulo deje claro que la competencia principal ahí es B con
>    E, no al revés.
>
> **Títulos de los módulos.** El Plan nombra las sesiones por su contenido (*Variables, parámetros y
> validaciones*; *Automatización por lotes*). Aquí se titulan por **lo que resuelven**, conforme a la
> regla editorial de `README.md`, conservando íntegro el contenido de cada una. La correspondencia
> está en la tabla de la *Ruta de la unidad*.
>
> **Estado de redacción.** **Unidad completa**: portada y S24–S29 redactadas.
>
> **Requisitos materiales.**
>
> - **S25:** cada estudiante o equipo necesita un **segundo genoma** (FASTA + GFF3, con ficha de
>   procedencia) descargado antes del taller. Anunciarlo al cerrar S24.
> - **S26:** una **colección de al menos cuatro organismos** (el conjunto del curso tiene doce),
>   organizada en `data/source/genomas/<organismo>/` con `genome.fna` y `annotation.gff3`. Anunciarlo
>   al cerrar S25 y dejar un conjunto de respaldo en el servidor.
>
> - **S29:** **cuentas activas en `chaac` y acceso comprobado antes del taller** — es la única sesión
>   que depende de infraestructura externa. Y completar la plantilla de la Sección 4.4 del módulo
>   (espacio de trabajo, colas, directivas de memoria y tiempo), que queda marcada como *pendiente de
>   validación* y **sin valores inventados**.
> - **S28:** una **colección de organismos que los equipos no hayan visto**, con la estructura del
>   contrato y, deliberadamente, **un organismo con la anotación ausente o mal nombrada**: es la
>   prueba más informativa de la sesión. Y decidir de antemano cómo caben las defensas en dos horas
>   si hay más de seis equipos.
> - **S27:** **parejas de equipos asignadas** para la prueba cruzada, y una fecha límite antes de S28.
>   El informe que reciba cada equipo alimenta la evidencia integradora. Conviene formar las parejas
>   al cerrar S26 y anunciar entonces el experimento del compañero mudo, que se hace **antes** de S27.
>
> **Cambio en la herramienta durante S26.** `analizar-genoma.sh` recibe un **tercer parámetro**: el
> directorio de salida. Sin él, todos los organismos del lote escribirían en el mismo sitio. Es un
> cambio de una línea y se presenta como consecuencia de la lección de S25.
>
> **Micro-extensión del alcance en S27.** Aparece el operador `||` en la comprobación de `-h` /
> `--help`. Es la única construcción de shell nueva desde S26 y no figura en las exclusiones; queda
> registrada por si se prefiere limitar la ayuda a `-h`.
