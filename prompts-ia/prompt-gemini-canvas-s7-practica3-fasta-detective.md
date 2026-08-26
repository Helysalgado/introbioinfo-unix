# Prompt para Gemini Canvas --- Práctica 3 interactiva: "FASTA Detective"

Actúa como **diseñador instruccional y desarrollador front-end
especializado en bioinformática, aprendizaje activo y recursos
educativos interactivos**.

Vas a construir un recurso HTML interactivo para integrarlo al sitio web
del curso:

**Introducción a la Bioinformática --- LCG, UNAM --- 2026**

Este recurso pertenece a:

**S7 --- De los objetos biológicos a FASTA, GFF3 y GenBank**

y transforma la actividad existente:

**Práctica 3 --- Interpretar la estructura de un archivo FASTA**

en una experiencia interactiva progresiva.

------------------------------------------------------------------------

# 1. Restricción pedagógica principal

NO debes inventar una práctica nueva.

Debes conservar los objetivos, contenidos y secuencia conceptual de la
**Práctica 3 original**, que busca que el estudiante:

-   identifique la estructura de un archivo FASTA;
-   distinga entre identificador, accession, versión y descripción;
-   interprete qué información puede obtener directamente del archivo;
-   reconozca qué información requiere consultar el registro de la base
    de datos;
-   comprenda por qué conservar el accession con versión es importante
    para la reproducibilidad.

El HTML debe **reemplazar o enriquecer las cinco actividades de la
Práctica 3**, no agregar una sexta práctica.

------------------------------------------------------------------------

# 2. Objetivo pedagógico del interactivo

Al terminar, el estudiante debe poder responder:

> **¿Qué puedo afirmar únicamente observando este archivo FASTA y qué
> información requiere consultar una fuente externa?**

La progresión conceptual debe ser:

``` text
observar el archivo
→ reconocer registros
→ interpretar el encabezado
→ separar identificador y descripción
→ distinguir evidencia directa de información externa
→ interpretar accession y versión
→ conectar versión con reproducibilidad
```

El foco no es memorizar definiciones.

El estudiante debe construir una regla mental útil:

> **Un archivo FASTA contiene secuencias y encabezados, pero no
> sustituye al registro de la base de datos.**

------------------------------------------------------------------------

# 3. Archivo FASTA que debe utilizarse

Usa exactamente este ejemplo conceptual:

``` text
>NC_000001.11 Homo sapiens chromosome 1, GRCh38.p14 Primary Assembly
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN...

>NC_000002.12 Homo sapiens chromosome 2, GRCh38.p14 Primary Assembly
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN...

>NC_000003.12 Homo sapiens chromosome 3, GRCh38.p14 Primary Assembly
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN...
```

Muestra claramente que las secuencias están truncadas únicamente para
simplificar la actividad.

No cambies los accessions ni la estructura del ejemplo.

------------------------------------------------------------------------

# 4. Nombre de la experiencia

Usa como título principal:

# FASTA Detective

Subtítulo sugerido:

> **¿Qué puedes saber realmente mirando solo el archivo?**

La estética puede recuperar ligeramente la idea de
investigación/detective, pero sin verse infantil.

------------------------------------------------------------------------

# 5. Arquitectura de la experiencia

Convierte las cinco actividades originales en **cinco estaciones
consecutivas**:

``` text
ESTACIÓN 1
Observar

        ↓

ESTACIÓN 2
Desarmar el encabezado

        ↓

ESTACIÓN 3
¿Qué puedes afirmar?

        ↓

ESTACIÓN 4
Interpretar la versión

        ↓

ESTACIÓN 5
Construir la regla
```

Incluye un indicador de progreso discreto:

``` text
Estación 2 de 5
```

No utilices puntaje, ranking, vidas, medallas ni competencia.

La meta es mejorar el razonamiento.

------------------------------------------------------------------------

# 6. Estación 1 --- Observación

Esta estación corresponde a la **Actividad 1 original**.

Muestra el FASTA completo y pide trabajar únicamente con lo visible.

## Primera interacción

Pregunta:

> **¿Cuántos registros contiene este archivo?**

Opciones:

-   1
-   2
-   3
-   No se puede saber

Respuesta esperada:

**3**

Pero no reveles inmediatamente la respuesta si falla.

Primera pista:

> Busca qué marca el inicio de un nuevo registro.

Segundo intento.

## Segunda interacción

Pregunta:

> **Haz clic o selecciona la parte que indica el inicio de cada registro
> FASTA.**

Permite que el estudiante identifique las líneas que comienzan con `>`.

Después pregunta:

> **¿Qué carácter te permitió reconocerlas?**

Opciones:

-   `#`
-   `>`
-   `@`
-   `;`

Respuesta:

`>`

## Tercera interacción

Pregunta:

> **¿Cuántas secuencias contiene el archivo?**

Respuesta esperada:

**3**

Retroalimentación:

> En este ejemplo, cada encabezado inicia un registro y cada registro
> contiene una secuencia.

## Cierre de estación

Mostrar:

``` text
FASTA
registro 1 = encabezado + secuencia
registro 2 = encabezado + secuencia
registro 3 = encabezado + secuencia
```

No avanzar automáticamente: usar botón **Continuar**.

------------------------------------------------------------------------

# 7. Estación 2 --- Desarmar el encabezado

Corresponde a la **Actividad 2 original**.

Mostrar:

``` text
>NC_000001.11 Homo sapiens chromosome 1, GRCh38.p14 Primary Assembly
```

## Interacción visual

Divide el encabezado visualmente en piezas seleccionables:

``` text
> | NC_ | 000001 | .11 | Homo sapiens chromosome 1, GRCh38.p14 Primary Assembly
```

No expliques todavía qué representa cada una.

### Pregunta A

> Selecciona el **accession con versión**.

Respuesta:

``` text
NC_000001.11
```

### Pregunta B

> Selecciona el **accession sin versión**.

Respuesta:

``` text
NC_000001
```

### Pregunta C

> Selecciona únicamente el **número de versión**.

Respuesta:

``` text
11
```

### Pregunta D

> ¿Qué parte corresponde a la descripción?

Respuesta:

``` text
Homo sapiens chromosome 1, GRCh38.p14 Primary Assembly
```

## Pregunta conceptual

> **¿Todo el encabezado corresponde al identificador?**

-   Sí
-   No

Respuesta:

**No**

Si responde Sí, mostrar:

> El encabezado contiene más información que el identificador.\
> Intenta separar qué parte funciona como accession y qué parte describe
> el registro.

Segundo intento.

## Explicación final

Mostrar:

``` text
>NC_000001.11 Homo sapiens chromosome 1, GRCh38.p14 Primary Assembly
  └────┬─────┘ └───────────────────────────────┬──────────────────────────────┘
    accession                                 descripción
    + versión
```

La explicación debe enfatizar:

> **NC_000001.11** es el identificador versionado.\
> El resto del encabezado es una descripción legible del registro.

------------------------------------------------------------------------

# 8. Estación 3 --- ¿Qué puedes afirmar únicamente con el archivo?

Esta estación corresponde exactamente a la **Actividad 3 original**.

Presenta las siguientes afirmaciones una por una.

Para cada afirmación el estudiante debe elegir:

-   **Sí, puedo afirmarlo con el archivo**
-   **No**
-   **Necesito consultar el registro o la base de datos**

Afirmaciones:

1.  El archivo contiene tres registros.
2.  El primer accession es `NC_000001.11`.
3.  El primer registro corresponde al cromosoma 1 humano.
4.  El ensamblado indicado es `GRCh38.p14`.
5.  El cromosoma tiene exactamente `248,956,422` nucleótidos.
6.  Este es el ensamblado más reciente disponible en NCBI.

## Respuestas esperadas

### 1

**Sí**

### 2

**Sí**

### 3

**Sí**

### 4

**Sí**

La información aparece en la descripción del encabezado.

### 5

**Requiere consultar el registro**

La secuencia del ejemplo está truncada y el archivo mostrado no
demuestra esa longitud exacta.

### 6

**Requiere consultar la base de datos**

El archivo puede indicar qué ensamblado representa, pero no demuestra
que siga siendo el más reciente.

------------------------------------------------------------------------

# 9. Retroalimentación de la Estación 3

Esta estación es especialmente importante.

NO uses únicamente:

> Correcto / Incorrecto.

Usa:

``` text
elección
→ pista
→ segundo intento
→ explicación
```

Ejemplo para:

> "Este es el ensamblado más reciente disponible en NCBI."

Si responde Sí:

> El encabezado te dice qué ensamblado representa **este archivo**.\
> ¿También te permite saber si NCBI publicó uno más reciente después?

Permite un segundo intento.

Después explicar:

> Para afirmar cuál es el ensamblado más reciente debes consultar una
> fuente actualizada.

El objetivo conceptual de esta estación es distinguir:

``` text
LO VEO EN EL ARCHIVO
vs.
NECESITO UNA FUENTE EXTERNA
```

------------------------------------------------------------------------

# 10. Estación 4 --- Interpretar la versión

Corresponde a la **Actividad 4 original**.

Muestra:

``` text
NC_000001.11
```

Divídelo visualmente:

``` text
NC_ | 000001 | .11
```

## Actividad de emparejamiento

Relacionar:

### `NC_`

con:

> Prefijo RefSeq para una secuencia cromosómica.

### `000001`

con:

> Identificador estable del registro.

### `.11`

con:

> Número de versión del registro.

Puedes implementar matching mediante selección, tarjetas o menús
desplegables accesibles.

------------------------------------------------------------------------

# 11. Mini-caso sobre reproducibilidad

Después del matching presenta:

> Un estudiante escribe en su protocolo:
>
> `NC_000001`
>
> pero omite `.11`.

Pregunta:

> **¿Cuál es el principal problema?**

Opciones:

-   El accession deja de identificar a *Homo sapiens*.
-   Otra persona podría recuperar una versión diferente del registro.
-   El archivo deja de ser FASTA.
-   NCBI no permite usar accession sin versión.

Respuesta:

**Otra persona podría recuperar una versión diferente del registro.**

Retroalimentación:

> El accession identifica el registro, pero la versión identifica el
> estado específico utilizado en el análisis.

Mostrar visualmente:

``` text
NC_000001
registro

NC_000001.11
registro + estado/version específica
```

Concluir:

> **La versión forma parte de la reproducibilidad.**

------------------------------------------------------------------------

# 12. Estación 5 --- Construir la regla

Corresponde a la **Actividad 5 original**.

No la conviertas simplemente en opción múltiple.

Usa una actividad de clasificación.

Presenta tarjetas con:

-   secuencia;
-   accession;
-   versión;
-   descripción;
-   número de registros;
-   longitud oficial;
-   anotaciones completas;
-   referencias bibliográficas;
-   taxonomía completa;
-   historial de cambios;
-   ensamblado descrito en el encabezado;
-   si existe actualmente una versión más reciente.

El estudiante debe clasificarlas en dos zonas:

``` text
PUEDO OBTENERLO
DIRECTAMENTE DEL FASTA

vs.

NECESITO CONSULTAR
EL REGISTRO / BASE DE DATOS
```

Permite revisar y corregir antes de mostrar la solución.

------------------------------------------------------------------------

# 13. Cierre reflexivo

Después de la clasificación, mostrar una pregunta abierta:

> **En una o dos frases, explica por qué un archivo FASTA no sustituye
> al registro de una base de datos.**

No necesitas evaluar automáticamente esta respuesta.

Proporciona después una respuesta modelo colapsable:

> Un FASTA proporciona secuencias y encabezados con identificadores y
> descripciones, pero información como anotaciones completas,
> referencias, taxonomía, historial y estado actual del registro
> requiere consultar la base de datos.

Después preguntar:

> **¿Por qué conservarías siempre el accession junto con su versión en
> un protocolo reproducible?**

Permitir respuesta breve antes de mostrar retroalimentación.

------------------------------------------------------------------------

# 14. Síntesis visual final

Mostrar al final:

``` text
ARCHIVO FASTA
│
├── encabezado
│   ├── accession
│   ├── versión
│   └── descripción
│
└── secuencia

PERO NO CONTIENE POR SÍ SOLO
│
├── historial completo del registro
├── referencias completas
├── anotación completa
├── estado actual de la base de datos
└── toda la procedencia necesaria
```

Mensaje principal:

> **El archivo es evidencia. El registro aporta contexto.**

Y:

> **El accession con versión conecta ambos de forma reproducible.**

------------------------------------------------------------------------

# 15. Transición hacia la siguiente parte de S7

Al terminar, no añadas otra tarea.

Mostrar:

> Ya sabes leer un FASTA y reconocer sus límites.
>
> Ahora aplicarás el mismo principio a otros formatos:
>
> **¿qué información representa cada uno y qué preguntas permite
> responder?**

Esto debe servir de puente hacia GFF3 y posteriormente hacia la
comparación FASTA/GFF3/GenBank.

------------------------------------------------------------------------

# 16. Qué debe permanecer fuera del HTML

El recurso NO debe sustituir:

-   inspección posterior de archivos reales;
-   consulta de registros reales;
-   navegación de NCBI;
-   trabajo de S8;
-   actualización de `doc/protocolo.md`.

El interactivo desarrolla **interpretación**, no recuperación real de
datos.

------------------------------------------------------------------------

# 17. Diseño visual

Diseño:

-   limpio;
-   científico;
-   moderno;
-   universitario;
-   juvenil sin parecer infantil;
-   responsive;
-   fondo claro;
-   excelente legibilidad;
-   código FASTA con tipografía monoespaciada;
-   las partes del encabezado pueden resaltarse visualmente al
    seleccionarse;
-   iconografía discreta;
-   animaciones mínimas y funcionales.

La estética "detective" debe ser sutil.

Evita:

-   lupas enormes;
-   personajes caricaturescos;
-   estética infantil;
-   exceso de colores;
-   gamificación competitiva.

El protagonismo es del archivo FASTA.

------------------------------------------------------------------------

# 18. Accesibilidad

Implementa:

-   HTML semántico;
-   navegación completa por teclado;
-   foco visible;
-   botones reales;
-   `fieldset` y `legend`;
-   labels explícitos;
-   `aria-live` para feedback;
-   contraste suficiente;
-   no comunicar correcto/incorrecto solo mediante color;
-   targets táctiles cómodos;
-   responsive para computadora y tableta.

Para elementos tipo drag-and-drop, proporciona siempre una alternativa
accesible mediante selección o botones.

------------------------------------------------------------------------

# 19. Restricciones técnicas

Genera:

-   **un único archivo HTML**;
-   CSS embebido;
-   JavaScript embebido;
-   sin frameworks;
-   sin React;
-   sin Node;
-   sin dependencias externas obligatorias;
-   sin APIs;
-   sin backend;
-   sin login;
-   sin tracking;
-   sin enviar respuestas a servicios externos;
-   funcional offline;
-   listo para Git;
-   fácil de incluir en un sitio estático.

No uses IA en tiempo real.

------------------------------------------------------------------------

# 20. Estado y progreso

Mantén únicamente durante la sesión:

-   estación actual;
-   número de intentos;
-   respuestas;
-   progreso.

No es necesario persistir al recargar.

No uses puntaje.

Indicador:

``` text
Estación 3 de 5
```

------------------------------------------------------------------------

# 21. Componentes reutilizables

Organiza el código para poder reutilizar posteriormente patrones como:

-   `sequence-viewer`
-   `clickable-header`
-   `multiple-choice-feedback`
-   `classify-evidence`
-   `matching-cards`
-   `hint-box`
-   `progress-indicator`
-   `reflection-box`
-   `concept-summary`

Comenta el JavaScript y CSS de manera suficientemente clara para
reutilizarlos en otros interactivos del curso.

------------------------------------------------------------------------

# 22. Nombre sugerido del archivo

``` text
interactive/u3/s7-fasta-detective.html
```

------------------------------------------------------------------------

# 23. Integración futura con el Markdown

La intención es que este recurso **reemplace pedagógicamente las
Actividades 1--5 de la Práctica 3**, manteniendo en el Markdown:

-   título de la práctica;
-   objetivo;
-   breve introducción;
-   enlace o iframe al recurso;
-   criterio de logro;
-   transición hacia GFF3.

NO modifiques todavía el Markdown de S7.

Al final de tu respuesta indica específicamente:

1.  qué contenido del Markdown podría sustituirse por el interactivo;
2.  qué contenido debe mantenerse;
3.  dónde insertar el enlace/iframe;
4.  cómo debería verse una versión mínima de esa sección después de
    integrar el recurso.

------------------------------------------------------------------------

# 24. Entregables

Genera:

1.  el HTML completo y funcional;
2.  explicación breve de su arquitectura;
3.  listado de las cinco estaciones implementadas;
4.  instrucciones para probarlo localmente;
5.  recomendación de integración en S7;
6.  fragmento Markdown sugerido para enlazarlo o embeberlo;
7.  nota sobre accesibilidad;
8.  cualquier decisión técnica importante.

Antes de terminar, verifica que:

-   las cinco actividades originales estén representadas;
-   no hayas añadido contenido que cambie el objetivo de S7;
-   las respuestas esperadas coincidan con la práctica original;
-   no se sustituya la consulta de datos reales;
-   la retroalimentación favorezca segundo intento y razonamiento;
-   el recurso funcione sin conexión a internet.
