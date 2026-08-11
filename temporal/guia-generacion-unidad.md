# Prompt para generar una unidad del curso (Introducción a la Bioinformática)

> Copia y pega este prompt en un chat nuevo. Cambia **`<UNIDAD N>`** por la unidad que quieras
> generar (p. ej. "Unidad 3. Datos y bases de datos biológicas"). El asistente debe tener acceso a la
> carpeta del proyecto `introbioinfo-unix/`.

---

Actúa como especialista en enseñanza universitaria de bioinformática, aula invertida, reproducibilidad
científica y comunicación técnica. Vas a redactar el **contenido didáctico de la `<UNIDAD N>`** del
curso *Introducción a la Bioinformática* (primer semestre, Licenciatura en Ciencias Genómicas, UNAM).
Los alumnos parten de cero en Unix. El resultado es un archivo **Markdown**, autocontenido y listo
para revisar.

Ten presente en todo momento que **no estás escribiendo un curso de Unix ni un manual de comandos**:
escribes material de bioinformática en el que las herramientas aparecen únicamente como medio para
responder preguntas biológicas. El principio rector del curso —*las preguntas biológicas permanecen;
las estrategias de análisis evolucionan*— está desarrollado en `contenidos-2026/README.md`, sección
**Identidad del curso**; léelo antes de escribir.

## 1. Antes de escribir, lee (sin modificar) estos documentos de referencia

- `Programa-IntroBioinfo-2026.docx` — programa del curso (unidades, competencias A–G, evaluación).
- `Plan-Clases-BioInfo-2026.xlsx` — plan operativo sesión por sesión (tareas, evidencias, ajustes).
- `contenidos-2026/plantilla-unidad.md` — **plantilla y estándar de unidad**: el esqueleto en orden
  fijo, la **checklist de calidad de 16 puntos** y la tabla de parámetros por unidad. Es la fuente de
  verdad; genera y **verifica** la unidad contra su checklist.
- `contenidos-2026/README.md` — **guía de estilo y convenciones** (callouts, figuras, práctica,
  referencias, etiquetas de ajuste, sección "Cierre con IA"). Es de lectura obligatoria.
- `contenidos-2026/u1-trabajo-reproducible-v3.md` — **unidad de referencia (estándar de oro)**. Imita
  su estructura, tono y nivel de detalle.
- La unidad previa en `contenidos-2026/` (para enlazar y no repetir).
- **La arquitectura de la unidad**, si existe (`uN-arquitectura.md`): hilo conductor, propuesta de
  sesiones, matriz de evolución de las preguntas y evolución del producto acumulativo. Si la unidad
  aún no la tiene, **diséñala y sométela a visto bueno antes de redactar ninguna sesión**.
- **La sesión inmediatamente anterior, completa**: no basta con conocer su temario. Necesitas saber
  con qué limitación terminó, qué resultados quedaron pendientes de corregir y qué pregunta dejó
  abierta.
- Material clásico de la unidad en `introBioInfo/lecciones/` (úsalo como base, no lo copies tal cual).
- Acervo en `introBioInfo/referencias/` (Buffalo 2015; Ritchie et al. 2015; Fitzgerald, regex) y
  `introBioInfo/ejemplos/` (formatos de protocolo, metadatos, datos de ejemplo).

> **NOTA — alcance: unidad completa vs. módulo.** Algunos requisitos de esta guía y de la plantilla se
> aplican a la **unidad completa** (p. ej. la ficha de unidad, los resultados generales y la tabla
> acumulativa de competencia). Otros se aplican a cada **módulo/sesión**. En particular, la **Unidad 2**
> no es un documento único: está dividida en una **portada** (`u2-entorno-unix-hpc.md`) y **cuatro
> módulos** de dos horas, **S3–S6**. Cada módulo es autocontenido y conserva su propia **nota de aula
> invertida, preparación previa, prácticas (tres momentos), evidencia, criterios/rúbricas, tiempos,
> alineación (anexos), glosario y referencias**; la portada solo aporta la visión de conjunto, la ruta
> S3–S6 y los enlaces. Al verificar la checklist de 16 puntos, aplícala al módulo o a la portada según
> corresponda (una "unidad" dividida se verifica por módulo + portada).

## 2. Estándares de contenido

- **Lectura previa autocontenida:** el material se lee ANTES de clase; debe describir por completo lo
  que se quiere transmitir y **definir cada concepto**. No dejes nada como "se verá en clase".
- **No reduzcas el contenido por su longitud.** La parte conceptual es para estudiar antes; el aula
  se usa para practicar.
- **Aula invertida explícita:** nota inicial con los tres momentos (lectura orientada → primer intento
  → taller guiado → corrección → entrega final), qué llevar al taller y cómo se evalúa cada momento.
- **No presupongas comandos aún no enseñados.** Si el alumno no los ha visto, preséntalos como
  "posibles herramientas" y remite a la unidad donde se aprenden.
- **Nunca menciones Quarto en el material del alumno** (Quarto es interno para publicar; el alumno no
  lo verá). Habla de Markdown, StackEdit, etc.
- **Cita SIEMPRE la fuente de una buena práctica** (p. ej. organización de proyectos → Noble 2009;
  FAIR → Wilkinson et al. 2016; FAIR4RS → Barker et al. 2022). No inventes referencias; verifica las
  nuevas y añádelas a la sección Referencias.
- **Matriz de evolución de las preguntas.** Antes de redactar, construye una tabla con todas las
  preguntas biológicas de la unidad y, para cada una: en qué sesión aparece por primera vez, con qué
  estrategia se responde inicialmente, cómo se refina después, qué herramienta permite cada
  refinamiento y en qué sesión queda resuelta. Al escribir cada sesión, consúltala: las preguntas que
  **aparecen** definen el contenido nuevo; las que se **refinan** definen las actividades de retorno.
  **Una sesión que no refina ninguna pregunta anterior está mal situada en la unidad.**
- **Cada herramienta nueva entra por una necesidad, y se presenta en formato mínimo.** Antes de
  introducirla, el material debe haber mostrado la limitación que resuelve. La presentación no excede
  cuatro elementos: **Sintaxis mínima** (un bloque de código), **¿Qué hace?** (dos líneas como
  máximo), **¿Por qué aparece en esta sesión?** (qué limitación de la estrategia anterior corrige) y
  uno o dos **prompts al asistente del curso** para explorar opciones adicionales por cuenta propia.
  El material no es un manual: las opciones exhaustivas se delegan a `man` y al asistente.
- **Continuidad entre sesiones.** Cada sesión debe poder responder tres preguntas, aunque no las
  formule literalmente: **¿qué problema resolvió la sesión anterior?**, **¿qué mejora aporta esta?** y
  **¿qué limitación queda abierta para la siguiente?** La sesión termina dejando una limitación viva
  —no un suspense artificial, sino la consecuencia natural del análisis— y la siguiente abre
  resolviéndola. Incluye además una orientación breve que permita al estudiante situarse: qué
  preguntas de la unidad se trabajan hoy y cuáles quedan para más adelante.
- **Idioma:** español claro y cercano a primer semestre; corrige ortografía y terminología. Incluye un
  **glosario español–inglés** de los términos nuevos.

## 3. Estructura obligatoria de la unidad

1. **Nota de aula invertida** (cómo se estudia la unidad).
2. **Ficha de la unidad** (tabla: sesiones, competencias, propósito, ajustes integrados, lectura base).
3. **Resultados de aprendizaje demostrables** (verbos observables).
4. **Ruta de aprendizaje** (tiempos, secciones indispensables vs. de consulta, productos mínimos al
   taller, productos a entregar).
5. **Secciones conceptuales** numeradas, con conceptos definidos, ejemplos reales y figuras.
6. **Prácticas** con TRES apartados cada una: *Antes de clase (primer intento)* → *Durante el taller*
   → *Después del taller (entrega final)*. Pasos explícitos y numerados. Ligadas a las **Tareas** del
   plan operativo (no rompas la numeración de tareas; si hay contradicción con el plan, alinéate a él
   y **registra la discrepancia**).
   Además, las prácticas de una misma unidad forman una **escalera**: cada una recupera un resultado
   anterior, lo compara, lo refina y documenta qué mejoró. Toda práctica arranca de una **pregunta
   biológica**, nunca de un comando, y cierra con una **interpretación** al nivel que la evidencia
   permita. Cuando una práctica tenga muchos pasos, marca cada uno con una etiqueta breve en negrita
   (*Predice, Localiza, Comprueba, Contrasta, Interpreta, Documenta*) para facilitar su navegación
   durante el taller.
7. **Rúbricas** (primer intento / taller / entrega final), acotadas al alcance real de la unidad.
8. **Glosario** español–inglés.
9. **Cierre de la unidad** (checklist de habilidades, tareas a entregar, lecturas para la siguiente
   unidad).
10. **Cierre con IA: clásico vs. asistido** (ver §5).
11. **Anexos**: correspondencia resultados–actividades–evidencias, y alineación transversal
    (columnas: reproducibilidad, verificación, validación, robustez).
12. **Referencias** (con DOI/URL; no inventadas).

## 4. Convenciones de estilo

Las convenciones —callouts, figuras, bloques de código, etiquetas de ajuste, referencias inline y
lenguaje del curso— están definidas en `contenidos-2026/README.md` y son de aplicación obligatoria.
No se reproducen aquí para evitar divergencias. Al generar la unidad, **verifica** que se cumplen; si
detectas una convención que el README no cubre, propón añadirla allí en vez de resolverla solo en esta
unidad.

Lo único que esta guía añade: **verifica toda referencia nueva** antes de incluirla (DOI o URL
comprobable) y no la des por buena si no puedes localizar la fuente.

## 5. Reglas específicas ya acordadas (respétalas)

- **Estructura de proyecto:** la definida en `contenidos-2026/README.md` (`data/source/`,
  `data/processed/`, `src/`, `results/`, `doc/`; cita Noble 2009). Los datos originales pueden
  leerse y copiarse, nunca editarse: toda transformación genera un archivo nuevo fuera de
  `data/source/`.
- **FAIR se ve en dos momentos:** el *estándar* (concepto, principios, "FAIR nace en la obtención") va
  junto al manejo de datos; la *aplicación* (ficha/plantilla de metadatos con diccionario de
  variables) va junto al protocolo. Los metadatos viven en `data/source/`.
- **Protocolo de resolución de un problema bioinformático:** documento vivo con estructura de artículo
  (Introducción, Metodología, Resultados, Discusión, Conclusiones), donde se integran las **fases del
  análisis** y las **fases de resolución** (pregunta → subpreguntas → evidencia → datos → operación →
  herramienta → verificación → interpretación → conclusión). El orden es siempre
  **pregunta → evidencia → datos → operación → herramienta**; nunca empezar por el comando.
- **Ejemplos:** el genoma de *E. coli* K-12 es **uno** de varios ejemplos del curso (también sRNAs,
  datos de ratón, red de regulación). El mismo razonamiento aplica a todos. Verifica que cualquier
  ejemplo esté alineado con la teoría; ajústalo si no lo está.
- **Cuatro principios como acciones observables** en las prácticas: reproducibilidad, verificación,
  validación, robustez (con una comprobación de robustez apropiada al nivel: comparar dos caminos,
  probar en pequeño, contrastar con fuente independiente…).
- **Uso responsable de IA:** la política completa —regla *primero a mano*, línea base, validación
  independiente, bitácora y asistente del curso— está en `contenidos-2026/README.md`. Aquí solo
  aplica **cómo redactarla** en la unidad: eje en espiral (inicio breve, refuerzo continuo, cierre
  crítico) y una sección de cierre construida sobre tareas que el estudiante ya resolvió a mano.
- **Sección "Cierre con IA: clásico vs. asistido"** al final de la unidad. Regla: **primero a mano,
  luego con IA**. Se reproducen con IA una o dos tareas ya resueltas paso a paso; el resultado a mano
  es la **línea base de comparación, no una verdad absoluta** contra la que se valida (también puede
  contener errores; se contrasta con la documentación, `man` y pruebas controladas). Estructura: idea y regla → herramientas
  (ChatGPT o Claude en el chat, o los GPTs del curso: Profesor de Unix / guía de razonamiento) → por
  cada tarea: recordatorio de lo hecho a mano + prompt sugerido/formulado + comparación (qué omitió o
  inventó, qué se corrigió) + registro en la bitácora → reflexión (cuándo conviene cada enfoque, qué
  no delegar). Aprovecha para mostrar **alucinaciones técnicas reales** (p. ej. que la IA mezcle
  Slurm con SGE) que el alumno solo detecta por haberlo hecho a mano.
- **Infraestructura real** (cuando aplique): servidor/cluster `chaac.lcg.unam.mx`, espacio
  `/export/space3/users/$USER`, planificador **SGE** (`.jdl`, `qsub`/`qstat`/`qdel`, `qhost`). Lo
  avanzado (threads, arrayjobs, GNU parallel) se marca como "cursos posteriores".

## 6. Flujo de trabajo

- Trabaja **sección por sección** y **detente para mi visto bueno** antes de avanzar.
- Al terminar, **presenta el archivo** (`contenidos-2026/uN-<nombre>.md`) y un resumen breve de
  decisiones y de cualquier discrepancia con el programa/plan.
- No modifiques los documentos de referencia; solo crea/edita el archivo de la unidad (y sus figuras
  o notas si lo pido).

## 7. Verificación final

Recorre la **checklist de calidad de 16 puntos** de `contenidos-2026/plantilla-unidad.md` y confirma
cada punto.

Cuando la unidad esté terminada, realiza además una **revisión horizontal** —leyendo todas sus
sesiones seguidas— para comprobar:

- **consistencia terminológica**: los mismos conceptos se nombran siempre igual;
- **continuidad narrativa**: cada sesión enlaza con la anterior y prepara la siguiente;
- **longitud y ritmo de las prácticas**: pasos comparables, sin bloques de texto excesivos;
- **estilo de las figuras**: paleta, tipografía y formato de pie coherentes en toda la unidad;
- **referencias cruzadas**: los reenvíos entre sesiones apuntan a secciones que existen;
- **equilibrio de callouts**: destacan lo importante sin saturar;
- **evolución del protocolo**: cada sesión añade su apartado, ninguno se reinicia ni se duplica;
- **redundancias entre sesiones**: ninguna explicación se repite en dos sesiones distintas; la
  segunda vez se sustituye por una remisión breve.
 Además, comprueba que un estudiante pueda responder: ¿qué leo antes de clase?, ¿qué
intento?, ¿qué llevo al taller?, ¿qué entrego y cómo se evalúa?, ¿cómo paso de una pregunta biológica
a datos y operaciones?, ¿cómo verifico, valido e interpreto?, ¿cómo se hace clásico vs. con IA? Y que
cada resultado de aprendizaje tenga práctica, evidencia y criterio de evaluación.
