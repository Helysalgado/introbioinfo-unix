# S17 — Demostrar: evaluación individual con datos nuevos

> **NOTA — Qué se evalúa aquí.** Esta sesión no comprueba si recuerdas comandos: comprueba si puedes
> **llegar solo, con datos que nunca has ejecutado, hasta donde tu equipo llegó acompañado**. Se
> califica el camino y su evidencia, no el número final. Una respuesta correcta sin la evidencia que
> la sostiene vale menos que una respuesta equivocada acompañada de la verificación que detecta el
> error.

## Ficha de la evaluación

| Elemento | Descripción |
| --- | --- |
| **Sesión** | S16, 2 horas, presencial |
| **Modalidad** | **Individual**. Sin equipo, sin consulta entre compañeros |
| **Insumo** | Un *Assembly Accession* **rotado**: el genoma que tu equipo revisó en S15, no el que analizó |
| **Alcance** | Unidad 3 (recuperación, integridad, procedencia) y U4 Bloque A (S10–S13) |
| **Punto de partida** | Solo el identificador. **La recuperación y verificación de los archivos forma parte de lo evaluado** |
| **Entregable** | `doc/examen-practico-1.md`, entregado al final de la sesión |
| **Peso** | Ver [Ponderación del bloque](#ponderación-del-bloque) |
| **Material permitido** | Protocolo propio, apuntes, manuales (`man`, `--help`), material del curso |
| **Material no permitido** | Compañeros, asistentes de IA, protocolos ajenos distintos del que revisaste |

## Principio de la evaluación

Durante S14–S15 trabajaste en equipo sobre un genoma. Ese trabajo construyó el andamio; esta sesión
mide **quién puede caminar sin él**.

Por eso el examen se apoya en dos decisiones de diseño:

1. **Rotación de genoma.** No trabajas sobre tu ensamblado, sino sobre el que **revisaste** en S15.
   Ya conoces su protocolo —leerlo con atención te da ventaja real, y esa es justamente la intención—
   pero **nunca ejecutaste un solo comando sobre esos archivos**.
2. **Preguntas que exigen ejecutar.** Ninguna pregunta se responde copiando del protocolo que
   revisaste. Todas requieren producir evidencia nueva sobre los archivos que acabas de recuperar.

> **IMPORTANTE:** La revisión por pares de S15 deja de ser un trámite. El equipo que leyó con
> cuidado el protocolo ajeno llega a S16 sabiendo qué organismo le espera, qué replicones tiene y
> dónde estaban las zonas difíciles. El que lo revisó por encima, no.

## Rotación de genomas

La revisión de S15 sigue un **ciclo cerrado**: el equipo *n* revisa al equipo *n+1*, y el equipo 12
revisa al equipo 1. Así cada protocolo se revisa exactamente una vez y ningún equipo revisa a quien
lo revisó a él.

El genoma de examen de cada estudiante es, por tanto, el del equipo que revisó su equipo:

| Tu equipo | Revisó en S15 al equipo | Tu genoma en S16 |
| ---: | ---: | --- |
| 1 | 2 | `GCF_000009045.1` |
| 2 | 3 | `GCF_000006945.2` |
| 3 | 4 | `GCF_000195955.2` |
| 4 | 5 | `GCF_000016285.1` |
| 5 | 6 | `GCF_000006965.1` |
| 6 | 7 | `GCF_000008525.1` |
| 7 | 8 | `GCF_000006765.1` |
| 8 | 9 | `GCF_000027325.1` |
| 9 | 10 | `GCF_000009605.1` |
| 10 | 11 | `GCF_000010065.1` |
| 11 | 12 | `GCF_000012825.1` |
| 12 | 1 | `GCF_000091005.1` |

> **NOTA:** Los integrantes de un mismo equipo comparten genoma, pero **no comparten preguntas**:
> cada uno recibe una variante distinta (A, B o C) del cuestionario. Ver
> [Variantes por integrante](#variantes-por-integrante).

## Desarrollo de la sesión

| Bloque | Tiempo | Qué haces |
| --- | ---: | --- |
| **1. Recuperación y verificación** | 25 min | Localizar el ensamblado, descargar FASTA y GFF3, verificar integridad y documentar procedencia |
| **2. Reconocimiento del archivo** | 15 min | Describir la organización de los archivos recuperados antes de analizarlos |
| **3. Preguntas de análisis** | 45 min | Responder las tres preguntas de tu variante, cada una con su evidencia |
| **4. Interpretación y límites** | 20 min | Explicar qué significan tus resultados y qué **no** autorizan a afirmar |
| **5. Cierre y entrega** | 15 min | Revisar el documento, comprobar que cada afirmación tiene su comando y su salida, entregar |

> **TIP:** El bloque 5 no es relleno. Un documento entregado sin revisar suele perder más puntos por
> afirmaciones sin evidencia que por errores de análisis.

### Bloque 1 — Recuperación y verificación

Partes únicamente del identificador. Debes:

- localizar el ensamblado en NCBI y confirmar que es el correcto;
- identificar organismo, cepa, versión del ensamblado y fuente de la anotación;
- descargar el FASTA genómico y el GFF3;
- verificar la integridad de los archivos por el procedimiento de la Unidad 3;
- organizar los archivos en la estructura de proyecto del curso.

> **ADVERTENCIA — dependencia de red.** Si la descarga falla por causas ajenas a ti, avisa de
> inmediato. Existe una copia de respaldo de los archivos; usarla **no penaliza**, pero debes
> documentar en tu entregable que la usaste y por qué. Lo que sí se penaliza es no dejar constancia.

### Bloque 2 — Reconocimiento del archivo

Antes de contar nada, demuestra que sabes **qué tienes delante**: cuántas secuencias hay en el FASTA,
cómo están construidos sus encabezados, dónde termina la cabecera del GFF3 y empiezan los datos, qué
delimitador usa y cómo representa los valores faltantes.

> **IMPORTANTE:** Todo conteo hecho sin haber separado antes las líneas de comentario del GFF3 es un
> conteo sospechoso. Este bloque existe para evitar ese error, no para rellenar tiempo.

### Bloque 3 — Preguntas de análisis

Tres preguntas, correspondientes a tu variante. Cada respuesta debe entregarse en el formato de
evidencia descrito más abajo.

### Bloque 4 — Interpretación y límites

Dos cosas, ambas obligatorias:

- **Qué significan tus resultados.** Una lectura biológica breve: qué categoría domina, qué llama la
  atención, cómo se compara con el genoma que analizaste en el mini proyecto.
- **Qué no puedes afirmar.** Al menos dos límites concretos de tu propio análisis, con la razón
  técnica que los produce (por ejemplo: una coincidencia literal que puede incluir casos que no
  quieres, o un conteo de registros que no equivale a un conteo de objetos biológicos).

## Formato de evidencia

Cada respuesta se entrega con **tres elementos**. Una respuesta a la que le falte alguno se considera
incompleta, aunque el número sea correcto:

```text
Pregunta: ...

1. Comando ejecutado
   $ ...

2. Salida obtenida
   ...

3. Qué autoriza a afirmar esta salida
   ... (y qué no autoriza a afirmar)
```

> **NOTA:** El tercer elemento es el que distingue esta evaluación de un examen de comandos. Ahí es
> donde se ve si entiendes lo que acabas de ejecutar.

## Variantes por integrante

Los integrantes de un mismo equipo reciben variantes distintas (A, B, C) construidas a partir de las
mismas plantillas, instanciadas con parámetros diferentes. Todas exigen el mismo nivel de habilidad y
las mismas herramientas.

| Plantilla | Forma de la pregunta | Se parametriza con |
| --- | --- | --- |
| **P1. Dimensión** | ¿Cuál es la longitud del replicón *X* y qué proporción representa del total? | Replicón |
| **P2. Inventario restringido** | ¿Cuántos registros de tipo *T* existen, y cómo se distribuyen entre los replicones? | Tipo de *feature* |
| **P3. Distribución** | ¿Cuáles son las *k* categorías más frecuentes de la anotación y qué proporción acumulan? | Valor de *k* |
| **P4. Procedencia** | ¿Qué fuentes de anotación aparecen y qué proporción aporta la fuente *F*? | Fuente |
| **P5. Contraste** | El protocolo que revisaste afirma *A*. Comprueba esa afirmación con tu propia evidencia y decide si la sostienes, la corriges o la matizas | Afirmación tomada del protocolo revisado |

Cada variante combina **una pregunta de estructura** (P1 o P2), **una de distribución** (P3 o P4) y
**siempre P5**.

> **IMPORTANTE — por qué P5 está en todas las variantes.** Es la pregunta que cierra el círculo:
> obliga a contrastar una afirmación ajena con evidencia propia. Corregir con fundamento un
> resultado del protocolo revisado, o sostenerlo con evidencia independiente, es la demostración más
> completa de que el bloque quedó aprendido. Coincidir con el protocolo revisado **no** es
> automáticamente correcto: lo que se califica es tu evidencia.

## Criterios de evaluación

| Aspecto | Peso |
| --- | ---: |
| Recuperación correcta del ensamblado y documentación de procedencia | 15 % |
| Verificación de integridad | 10 % |
| Reconocimiento de la estructura de los archivos | 10 % |
| Preguntas de análisis: corrección del procedimiento | 25 % |
| Preguntas de análisis: evidencia completa (comando, salida, alcance) | 20 % |
| Interpretación biológica de los resultados | 10 % |
| Declaración honesta de límites | 10 % |
| **Total** | **100 %** |

> **NOTA:** Fíjate en la suma: la **evidencia y los límites** pesan 30 %, más que la corrección del
> procedimiento. No es un descuido — es lo que esta evaluación quiere medir.

## Rúbricas

| Criterio | Logrado | Parcialmente logrado | Aún no logrado |
| --- | --- | --- | --- |
| **Recuperación y procedencia** | Recupera los archivos oficiales y documenta accesión, versión, fecha y fuente de anotación | Recupera los archivos pero la documentación de procedencia es incompleta | No recupera los archivos correctos o no documenta de dónde provienen |
| **Integridad** | Verifica la integridad y explica qué demuestra esa verificación | Ejecuta la verificación sin explicar qué garantiza | No verifica, o afirma integridad sin evidencia |
| **Estructura de los archivos** | Distingue cabecera de datos, describe delimitadores y valores faltantes antes de contar | Describe la estructura de forma parcial; algún conteo queda afectado | Cuenta sin haber reconocido la estructura; los conteos incluyen comentarios |
| **Procedimiento de análisis** | Las tuberías son correctas, verificables y adecuadas a la pregunta | El resultado es correcto pero el procedimiento es frágil o innecesariamente complejo | El procedimiento no responde a la pregunta formulada |
| **Evidencia** | Cada afirmación trae comando, salida y alcance | Falta sistemáticamente uno de los tres elementos | Se presentan números sin la evidencia que los produce |
| **Interpretación** | Lee los resultados en clave biológica y los compara con lo conocido | Describe los números sin interpretarlos | No hay interpretación, solo salidas de terminal |
| **Límites** | Identifica límites concretos y explica su causa técnica | Menciona límites genéricos, sin causa | Presenta todos los resultados como definitivos |

## Ponderación del bloque

El mini proyecto y esta evaluación **califican ambos**, con funciones distintas:

| Componente | Modalidad | Peso del bloque | Qué mide |
| --- | --- | ---: | --- |
| Mini Proyecto de Investigación I (S14–S15) + revisión por pares (S16) | Equipo | 40 % | Capacidad de construir una investigación completa y documentada, y de mejorarla mediante revisión por pares |
| Evaluación individual demostrativa (S17) | Individual | 60 % | Dominio autónomo del flujo completo sobre datos no trabajados previamente |

> **ADVERTENCIA — coherencia documental.** Esta ponderación debe reflejarse también en
> `mini-proyecto-investigacion-I.md` (cuya rúbrica interna suma 100 % **del componente en equipo**,
> no del bloque) y en `u4-procesamiento-exploracion.md`, donde S14–S15 aparece hoy declarado como
> actividad formativa. Ajustar antes de publicar.

## Entregable

Un único archivo, entregado al final de la sesión:

```text
doc/examen-practico-1.md
```

Debe contener, en este orden:

1. identificación del ensamblado recibido y evidencia de procedencia;
2. verificación de integridad;
3. descripción de la estructura de los archivos;
4. las tres preguntas de tu variante, cada una en el formato de evidencia;
5. interpretación biológica;
6. límites del análisis;
7. incidencias, si las hubo (uso de la copia de respaldo, comandos que fallaron y cómo lo resolviste).

> **TIP:** Documentar un intento fallido y cómo lo corregiste **suma**. Es exactamente lo que hace un
> investigador en su cuaderno de laboratorio, y es lo que el curso ha pedido desde la Unidad 1.

## Errores frecuentes en esta evaluación

- **Copiar la estructura del protocolo revisado.** El organismo es el mismo, pero los números deben
  salir de tus propios comandos. Un resultado idéntico sin evidencia propia no se acredita.
- **Contar sobre el archivo completo.** El GFF3 empieza con líneas de comentario; incluirlas infla
  cualquier conteo.
- **Confundir registros con objetos biológicos.** Un gen puede generar varios registros. El número
  que obtienes es de registros mientras no demuestres lo contrario.
- **Coincidencias literales demasiado amplias.** Buscar un texto sin restringirlo al campo correcto
  arrastra coincidencias que aparecen en los atributos.
- **Entregar números sin alcance.** Es el error que más puntos cuesta, y el más fácil de evitar.

## Después de S17

La sesión de retorno no se dedica a publicar respuestas correctas, sino a **analizar los caminos**:
por qué distintas tuberías válidas llegan al mismo resultado, cuáles son más robustas y qué error
conceptual produjo cada fallo frecuente. Conserva tu entregable: será el material de trabajo.
