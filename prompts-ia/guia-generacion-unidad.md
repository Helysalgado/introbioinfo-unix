# Prompt para generar una unidad del curso (Introducción a la Bioinformática)

> Copia y pega este prompt en un chat nuevo. Cambia **`<UNIDAD N>`** por
> la unidad que quieras generar (p. ej. "Unidad 3. Datos y bases de
> datos biológicas"). El asistente debe tener acceso a la carpeta del
> proyecto `introbioinfo-unix/`.

------------------------------------------------------------------------

Actúa como especialista en enseñanza universitaria de bioinformática,
aula invertida, reproducibilidad científica y comunicación técnica. Vas
a redactar el **contenido didáctico de la `<UNIDAD N>`** del curso
*Introducción a la Bioinformática* (primer semestre, Licenciatura en
Ciencias Genómicas, UNAM). Los alumnos parten de cero en Unix. El
resultado es un archivo **Markdown**, autocontenido y listo para
revisar.

Ten presente en todo momento que **no estás escribiendo un curso de Unix
ni un manual de comandos**: escribes material de bioinformática en el
que las herramientas aparecen únicamente como medio para responder
preguntas biológicas. El principio rector del curso ---*las preguntas
biológicas permanecen; las estrategias de análisis evolucionan*--- está
desarrollado en `contenidos-2026/README.md`, sección **Identidad del
curso**; léelo antes de escribir.

## 1. Antes de escribir, lee (sin modificar) estos documentos de referencia

-   `Programa-IntroBioinfo-2026.docx` --- programa del curso (unidades,
    competencias A--G, evaluación).

-   `Plan-Clases-BioInfo-2026-final-S34.xlsx`, pestaña
    **`PlanClases-2026-final S34`** --- plan operativo vigente sesión
    por sesión (tareas, evidencias, ajustes). Las pestañas y archivos
    anteriores son historial: no se usan como referencia.

-   `contenidos-2026/plantilla-unidad.md` --- **plantilla y estándar de
    unidad**: el esqueleto en orden fijo, la **checklist de calidad de
    16 puntos** y la tabla de parámetros por unidad. Es la fuente de
    verdad; genera y **verifica** la unidad contra su checklist.

-   `contenidos-2026/README.md` --- **guía de estilo y convenciones**
    (callouts, figuras, práctica, referencias, etiquetas de ajuste,
    política de uso crítico de IA). Es de lectura obligatoria.

-   `contenidos-2026/README.md` +
    `contenidos-2026/plantilla-unidad.md` + esta guía constituyen el
    **canon de trabajo**: el README fija principios y convenciones, la
    plantilla fija el esqueleto y esta guía fija el procedimiento para
    generar o revisar. Si hubiera una discrepancia entre una sesión
    existente y estos documentos, se corrige la sesión; no se modifica
    el canon solo para conservar una inconsistencia histórica.

    Las sesiones S30--S34 pueden usarse como referencia de estructura
    reciente, pero no deben copiarse mecánicamente: sus prácticas
    agrupadas y la ausencia de retroalimentación colapsable son
    precisamente aspectos que deben corregirse durante la revisión
    horizontal.

-   La unidad previa en `contenidos-2026/` (para enlazar y no repetir).

-   **La arquitectura de la unidad**, si existe (`uN-arquitectura.md`):
    hilo conductor, propuesta de sesiones, matriz de evolución de las
    preguntas y evolución del producto acumulativo. Si la unidad aún no
    la tiene, **diséñala y sométela a visto bueno antes de redactar
    ninguna sesión**.

-   **La sesión inmediatamente anterior, completa**: no basta con
    conocer su temario. Necesitas saber con qué limitación terminó, qué
    resultados quedaron pendientes de corregir y qué pregunta dejó
    abierta.

-   **Los prompts que construyeron las lecciones**, en `prompts-ia/`
    (`uN_sNN.md`, `uN-sNN-revision.md`, `ajustes_*.md`). Registran el
    encargo con el que se generó cada sesión: alcance asignado,
    limitación que debía resolver, decisiones tomadas y discrepancias
    detectadas. Consúltalos antes de reescribir una sesión existente:
    suelen explicar **por qué** algo quedó como quedó.

-   Material clásico de la unidad en `introBioInfo/lecciones/` (úsalo
    como base, no lo copies tal cual).

-   Acervo en `introBioInfo/referencias/` (Buffalo 2015; Ritchie et
    al. 2015; Fitzgerald, regex) y `introBioInfo/ejemplos/` (formatos de
    protocolo, metadatos, datos de ejemplo).

> **NOTA --- alcance: unidad completa vs. módulo.** Algunos requisitos
> de esta guía y de la plantilla se aplican a la **unidad completa**
> (p. ej. la ficha de unidad, los resultados generales y la tabla
> acumulativa de competencia). Otros se aplican a cada
> **módulo/sesión**. En particular, la **Unidad 2** no es un documento
> único: está dividida en una **portada** (`u2-entorno-unix.md`) y
> **cuatro módulos** de dos horas, **S3--S6**. Cada módulo es
> autocontenido y conserva su propia **nota de aula invertida,
> preparación previa, prácticas (tres momentos), evidencia,
> criterios/rúbricas, tiempos, alineación (anexos), glosario y
> referencias**; la portada solo aporta la visión de conjunto, la ruta
> S3--S6 y los enlaces. Al verificar la checklist de 16 puntos, aplícala
> al módulo o a la portada según corresponda (una "unidad" dividida se
> verifica por módulo + portada).

> **NOTA --- modo revisión de un curso existente.** Si el encargo es
> revisar o homogeneizar sesiones ya redactadas, **no regeneres la
> lección desde cero**. Conserva contenido biológico, datos, resultados,
> comandos válidos y decisiones pedagógicas que sigan vigentes. Aplica
> primero las convenciones mecánicas de bajo riesgo (H1, nombres de
> sección, marcadores, pies, cercado de código); después realiza los
> cambios estructurales con criterio pedagógico (intercalar prácticas,
> añadir retroalimentación, completar secciones, corregir continuidad).
> Registra cualquier cambio que altere tareas, evidencias, datos o
> alcance.

### Orden recomendado de revisión

Cuando la sesión ya existe, aplicar los cambios en este orden:

1.  **Preservar:** identificar contenido biológico, datos, comandos,
    resultados y decisiones pedagógicas válidas.
2.  **Corregir convenciones:** H1, nombres de sección, marcadores,
    bloques de código, nombres/pies de figura.
3.  **Corregir estructura didáctica:** intercalar prácticas, recuperar
    resultados previos, completar la cadena pregunta → evidencia →
    interpretación y añadir retroalimentación donde aporte
    autocorrección.
4.  **Comprobar continuidad:** verificar qué recibe de la sesión
    anterior y qué limitación entrega a la siguiente.
5.  **Alinear evaluación:** resultado → actividad → evidencia →
    criterio.
6.  **Registrar hallazgos:** distinguir correcciones editoriales de
    cambios pedagógicos o científicos.

No reescribir por estilo una explicación correcta si el cambio no mejora
claridad, continuidad o aprendizaje.

## 2. Estándares de contenido

-   **Lectura previa autocontenida:** el material se lee ANTES de clase;
    debe describir por completo lo que se quiere transmitir y **definir
    cada concepto**. No dejes nada como "se verá en clase".
-   **No reduzcas el contenido por su longitud.** La parte conceptual es
    para estudiar antes; el aula se usa para practicar.
-   **Aula invertida explícita:** nota inicial con los tres momentos
    (lectura orientada → primer intento → taller guiado → corrección →
    entrega final), qué llevar al taller y cómo se evalúa cada momento.
-   **No presupongas comandos aún no enseñados.** Si el alumno no los ha
    visto, preséntalos como "posibles herramientas" y remite a la unidad
    donde se aprenden.
-   **Nunca menciones Quarto en el material del alumno** (Quarto es
    interno para publicar; el alumno no lo verá). Habla de Markdown,
    StackEdit, etc.
-   **Cita SIEMPRE la fuente de una buena práctica** (p. ej.
    organización de proyectos → Noble 2009; FAIR → Wilkinson et
    al. 2016; FAIR4RS → Barker et al. 2022). No inventes referencias;
    verifica las nuevas y añádelas a la sección Referencias.
-   **Matriz de evolución de las preguntas.** Antes de redactar,
    construye una tabla con todas las preguntas biológicas de la unidad
    y, para cada una: en qué sesión aparece por primera vez, con qué
    estrategia se responde inicialmente, cómo se refina después, qué
    herramienta permite cada refinamiento y en qué sesión queda
    resuelta. Al escribir cada sesión, consúltala: las preguntas que
    **aparecen** definen el contenido nuevo; las que se **refinan**
    definen las actividades de retorno. **Una sesión que no refina
    ninguna pregunta anterior está mal situada en la unidad.**
-   **Cada herramienta nueva entra por una necesidad, y se presenta en
    formato mínimo.** Antes de introducirla, el material debe haber
    mostrado la limitación que resuelve. La presentación no excede
    cuatro elementos: **Sintaxis mínima** (un bloque de código), **¿Qué
    hace?** (dos líneas como máximo), **¿Por qué aparece en esta
    sesión?** (qué limitación de la estrategia anterior corrige) y uno o
    dos **prompts al asistente del curso** para explorar opciones
    adicionales por cuenta propia. El material no es un manual: las
    opciones exhaustivas se delegan a `man` y al asistente.
-   **Continuidad entre sesiones.** Cada sesión debe poder responder
    tres preguntas, aunque no las formule literalmente: **¿qué problema
    resolvió la sesión anterior?**, **¿qué mejora aporta esta?** y
    **¿qué limitación queda abierta para la siguiente?** La sesión
    termina dejando una limitación viva ---no un suspense artificial,
    sino la consecuencia natural del análisis--- y la siguiente abre
    resolviéndola. Incluye además una orientación breve que permita al
    estudiante situarse: qué preguntas de la unidad se trabajan hoy y
    cuáles quedan para más adelante.
-   **Idioma:** español claro y cercano a primer semestre; corrige
    ortografía y terminología. Incluye un **glosario español--inglés**
    de los términos nuevos.

## 3. Estructura obligatoria de la unidad

> **NOTA — dos tipos de documento.** Esta estructura se aplica a los
> **módulos de contenido**. Las sesiones de **práctica integradora,
> revisión por pares y evaluación** (en 2026, S14–S15, S16 y S17) siguen
> la estructura corta descrita en `contenidos-2026/README.md`, sección
> *Material transversal*: no llevan bloques conceptuales, prácticas
> intercaladas, glosario ni anexos, pero **sí** ficha, entregables,
> criterios y rúbricas. No las midas contra la checklist de módulo.

1.  **Nota de aula invertida** (cómo se estudia la unidad).
2.  **Ficha de la unidad** (tabla: sesiones, competencias, propósito,
    ajustes integrados, lectura base).
3.  **Resultados de aprendizaje demostrables** (verbos observables).
4.  **Ruta de aprendizaje** (tiempos, secciones indispensables vs. de
    consulta, productos mínimos al taller, productos a entregar).
5.  **Secciones conceptuales** numeradas, con conceptos definidos,
    ejemplos reales y figuras.
6.  **Prácticas intercaladas** inmediatamente después de la sección
    conceptual que las habilita; no se agrupan como un bloque al final.
    Cada una tiene TRES apartados: *Antes de clase (primer intento)* →
    *Durante el taller* → *Después del taller (entrega final)*. Pasos
    explícitos y numerados. Ligadas a las **Tareas** del plan operativo
    (no rompas la numeración de tareas; si hay contradicción con el
    plan, alinéate a él y **registra la discrepancia**). Además, las
    prácticas de una misma unidad forman una **escalera**: cada una
    recupera un resultado anterior, lo compara, lo refina y documenta
    qué mejoró. Toda práctica arranca de una **pregunta biológica**,
    nunca de un comando, y cierra con una **interpretación** al nivel
    que la evidencia permita. Cuando una práctica tenga muchos pasos,
    marca cada uno con una etiqueta breve en negrita (*Predice,
    Localiza, Comprueba, Contrasta, Interpreta, Documenta*) para
    facilitar su navegación durante el taller.
7.  **Rúbricas** (primer intento / taller / entrega final), acotadas al
    alcance real de la unidad.
8.  **Glosario** español--inglés.
9.  **Cierre de la unidad** (checklist de habilidades, tareas a
    entregar, lecturas para la siguiente unidad).
10. **Actividad de uso crítico de IA**, cuando aporte. Su
    obligatoriedad, ubicación y estructura las fija
    `contenidos-2026/README.md` (*Uso crítico de IA como eje
    transversal*): **no** es una sección fija por unidad.
11. **Anexos**: correspondencia resultados--actividades--evidencias, y
    alineación transversal (columnas: reproducibilidad, verificación,
    validación, robustez).
12. **Referencias** (con DOI/URL; no inventadas).

## 4. Convenciones de estilo

Las convenciones ---callouts, figuras, bloques de código, etiquetas de
ajuste, referencias inline y lenguaje del curso--- están definidas en
`contenidos-2026/README.md` y son de aplicación obligatoria. No se
reproducen aquí para evitar divergencias. Al generar la unidad,
**verifica** que se cumplen; si detectas una convención que el README no
cubre, propón añadirla allí en vez de resolverla solo en esta unidad.

Lo único que esta guía añade: **verifica toda referencia nueva** antes
de incluirla (DOI o URL comprobable) y no la des por buena si no puedes
localizar la fuente.

## 5. Reglas específicas ya acordadas (respétalas)

-   **Estructura de proyecto:** la definida en
    `contenidos-2026/README.md` (`data/source/`, `data/processed/`,
    `src/`, `results/`, `doc/`; cita Noble 2009). Los datos originales
    pueden leerse y copiarse, nunca editarse: toda transformación genera
    un archivo nuevo fuera de `data/source/`.
-   **FAIR se ve en dos momentos:** el *estándar* (concepto, principios,
    "FAIR nace en la obtención") va junto al manejo de datos; la
    *aplicación* (ficha/plantilla de metadatos con diccionario de
    variables) va junto al protocolo. Los metadatos viven en
    `data/source/`.
-   **Protocolo de resolución de un problema bioinformático:** documento
    vivo con estructura de artículo (Introducción, Metodología,
    Resultados, Discusión, Conclusiones), donde se integran las **fases
    del análisis** y las **fases de resolución** (pregunta →
    subpreguntas → evidencia → datos → operación → herramienta →
    verificación → interpretación → conclusión). El orden es siempre
    **pregunta → evidencia → datos → operación → herramienta**; nunca
    empezar por el comando.
-   **Ejemplos:** el genoma de *E. coli* K-12 es **uno** de varios
    ejemplos del curso (también sRNAs, datos de ratón, red de
    regulación). El mismo razonamiento aplica a todos. Verifica que
    cualquier ejemplo esté alineado con la teoría; ajústalo si no lo
    está.
-   **Cuatro principios como acciones observables** en las prácticas:
    reproducibilidad, verificación, validación, robustez (con una
    comprobación de robustez apropiada al nivel: comparar dos caminos,
    probar en pequeño, contrastar con fuente independiente...).
-   **Uso crítico de IA:** la política completa ---regla *primero a
    mano*, línea base, validación independiente, bitácora, asistente del
    curso y **obligatoriedad y ubicación de la actividad**--- está en
    `contenidos-2026/README.md`. Lo único que esta guía añade es **cómo
    redactarla** cuando se incluya: regla *primero a mano, luego con
    IA*; se reproduce una tarea ya resuelta paso a paso; el trabajo
    manual es **línea base de comparación, no verdad absoluta** ---también
    puede contener errores, y se contrasta con la documentación, `man` y
    pruebas controladas---; y se registra en la bitácora. Aprovecha para
    mostrar **alucinaciones técnicas reales** ---por ejemplo, que la IA
    mezcle Slurm con SGE--- que el alumno solo detecta por haberlo hecho
    a mano. **No la incluyas por rutina**: si en una unidad no hay una
    comparación que aporte, se omite.
-   **Infraestructura real** (cuando aplique): servidor/cluster
    `chaac.lcg.unam.mx`, espacio `/export/space3/users/$USER`,
    planificador **SGE** (`.jdl`, `qsub`/`qstat`/`qdel`, `qhost`). Lo
    avanzado (threads, arrayjobs, GNU parallel) se marca como "cursos
    posteriores".

## 6. Flujo de trabajo

-   Al **generar contenido nuevo**, trabaja sección por sección y
    detente para visto bueno cuando así se solicite. En una **revisión
    integral ya autorizada**, revisa la sesión completa de una pasada,
    conserva el contenido válido y entrega un registro breve de cambios.
-   Al terminar, **presenta el archivo**
    (`contenidos-2026/uN-<nombre>.md`) y un resumen breve de decisiones
    y de cualquier discrepancia con el programa/plan.
-   No modifiques los documentos de referencia; solo crea/edita el
    archivo de la unidad (y sus figuras o notas si lo pido).

## 7. Verificación final

Recorre la **checklist de calidad de 16 puntos** de
`contenidos-2026/plantilla-unidad.md` y confirma cada punto.

Cuando la unidad esté terminada, realiza además una **revisión
horizontal** ---leyendo todas sus sesiones seguidas--- para comprobar:

-   **consistencia terminológica**: los mismos conceptos se nombran
    siempre igual;
-   **continuidad narrativa**: cada sesión enlaza con la anterior y
    prepara la siguiente;
-   **longitud y ritmo de las prácticas**: pasos comparables, sin
    bloques de texto excesivos;
-   **estilo de las figuras**: paleta, tipografía y formato de pie
    coherentes en toda la unidad;
-   **referencias cruzadas**: los reenvíos entre sesiones apuntan a
    secciones que existen;
-   **equilibrio de callouts**: destacan lo importante sin saturar;
-   **evolución del protocolo**: cada sesión añade su apartado, ninguno
    se reinicia ni se duplica;
-   **redundancias entre sesiones**: ninguna explicación se repite en
    dos sesiones distintas; la segunda vez se sustituye por una remisión
    breve.
-   **convenciones editoriales**: H1, nombres de sección, marcadores,
    pies, retroalimentación y nombres de figura siguen el README;
-   **higiene del directorio**: notas de arquitectura, revisiones y
    archivos temporales no conviven con material del alumno; no hay
    duplicados ni figuras huérfanas sin una decisión explícita;
-   **coherencia con el plan operativo**: número, título, unidad,
    material, tarea/evidencia y competencias coinciden con la pestaña
    vigente del Plan de clases. Además, comprueba que un estudiante
    pueda responder: ¿qué leo antes de clase?, ¿qué intento?, ¿qué llevo
    al taller?, ¿qué entrego y cómo se evalúa?, ¿cómo paso de una
    pregunta biológica a datos y operaciones?, ¿cómo verifico, valido e
    interpreto?, ¿cómo se hace clásico vs. con IA? Y que cada resultado
    de aprendizaje tenga práctica, evidencia y criterio de evaluación.

## Referencia operativa del curso 2026

Para la revisión S1--S34, contrastar número de sesión, unidad,
propósito, evidencia y competencias con
`Plan-Clases-BioInfo-2026-final-S34.xlsx`, pestaña
**`PlanClases-2026-final S34`**.

La secuencia final de U6 es:

``` text
S30 Comparar → S31 Buscar → S32 Interpretar → S33 Inferir → S34 Integrar
```

S34 es el cierre del curso. No se proyecta una S35.

## Estabilidad del canon durante la revisión

Una vez iniciada la revisión sistemática S1→S34, README, plantilla y
guía se consideran estables. Si aparece un problema nuevo:

1.  registrar el hallazgo;
2.  decidir si es local o transversal;
3.  corregir primero la sesión si es local;
4.  modificar el canon únicamente si la nueva regla mejora de forma
    demostrable varias sesiones.

Esto evita cambiar las reglas editoriales a mitad de la revisión y
permite comparar las sesiones con un estándar común.
