# Prompt para Cursor --- Auditoría de prácticas interactivas y flashcards

Actúa como **diseñador instruccional especializado en bioinformática,
aprendizaje activo, evaluación formativa y desarrollo de recursos
educativos digitales**.

Estás trabajando sobre el repositorio completo del curso **Introducción
a la Bioinformática --- LCG, UNAM --- 2026**.

## Objetivo

Revisa sistemáticamente las sesiones **S1--S34** y detecta qué elementos
podrían beneficiarse de convertirse en:

1.  **actividades HTML interactivas**;
2.  **flashcards** para recuperación activa y repaso espaciado;
3.  actividades que funcionen bien en **ambos formatos**;
4.  actividades que deban permanecer en **Markdown, terminal, bases de
    datos, BLAST, HPC u otra práctica auténtica**.

Analiza prácticas, ejercicios, preguntas, autoevaluaciones,
diagnósticos, evaluaciones formativas, casos de interpretación,
predicciones, clasificaciones, comparaciones, árboles de decisión,
glosarios, conceptos, distinciones, errores frecuentes y relaciones
concepto ↔ significado.

**No generes todavía HTML ni mazos de flashcards. Primero realiza una
auditoría pedagógica razonada y priorizada.**

## 1. Lee primero el canon del curso

Localiza y lee:

-   `README.md`;
-   guía vigente de generación/revisión;
-   plantilla de unidad/sesión;
-   descripción detallada del curso;
-   Programa 2026 actualizado;
-   Plan de clases vigente;
-   sesiones S1--S34.

Considera filosofía pedagógica, competencias, progresión, aula
invertida, prácticas intercaladas, protocolo acumulativo, política de
IA, reproducibilidad, evidencias y evaluación.

## 2. Principio pedagógico

El curso NO busca memorizar comandos. Su progresión es:

``` text
pregunta biológica
→ evidencia necesaria
→ datos
→ operación
→ herramienta
→ resultado
→ verificación
→ interpretación
→ conclusión y límites
```

El **HTML** debe ayudar a razonar, decidir, comparar, predecir, detectar
errores o interpretar.

Las **flashcards** deben ayudar a recuperar con fluidez unidades
pequeñas de conocimiento que serán necesarias para razonamientos
posteriores.

Ni HTML ni flashcards deben sustituir una competencia auténtica.

## 3. Decide el formato

Para cada actividad o contenido relevante clasifica:

-   `HTML`
-   `FLASHCARDS`
-   `AMBOS`
-   `MANTENER COMO ESTÁ`

Justifica siempre la decisión.

## 4. Candidatos a HTML

Busca actividades de:

-   selección con retroalimentación;
-   predicción;
-   clasificación;
-   ordenamiento;
-   emparejamiento;
-   detección de errores;
-   comparación de evidencia;
-   casos progresivos;
-   árboles de decisión;
-   construcción visual.

Da prioridad a experiencias del tipo:

``` text
caso
→ decisión
→ pista
→ segundo intento
→ nueva evidencia
→ interpretación
```

La retroalimentación no debe limitarse a "correcto/incorrecto"; debe
provocar revisión del razonamiento.

## 5. Qué NO convertir a HTML

No sustituyas la ejecución real de:

-   Unix/shell;
-   SSH y transferencia;
-   `grep`, `sed`, `awk`;
-   scripts;
-   BLAST;
-   SGE/HPC;
-   consulta auténtica de bases de datos.

La combinación deseada es:

``` text
HTML: decidir/predicir
        ↓
terminal o herramienta real: ejecutar
        ↓
protocolo: interpretar y documentar
```

No recomiendes simuladores que eviten practicar la competencia real.

## 6. Auditoría específica de flashcards

Busca contenidos adecuados para recuperación activa:

### Buenos candidatos

-   **Concepto → significado**
-   **Término español ↔ inglés**
-   **Distinciones conceptuales**
-   **Formato → función**
-   **Símbolo/campo → significado**
-   **Métrica → interpretación**
-   **Comando → operación conceptual**
-   **Error frecuente → corrección conceptual**
-   **Pregunta breve → razonamiento breve**

Ejemplos potenciales:

``` text
¿Qué es un replicón?
¿Qué representa un E-value?
¿Qué significa HSP?

identidad vs similitud
similitud vs homología
ortólogo vs parálogo
verificación vs validación

FASTA → secuencia
GFF3 → anotación y coordenadas
GenBank → secuencia + anotación + metadatos

$1
$NF
NR
NF

grep → localizar líneas mediante patrones
sort → ordenar
uniq → resumir repeticiones adyacentes
```

### Malos candidatos

No recomiendes flashcards para memorizar:

-   pipelines completos;
-   comandos largos;
-   opciones raras;
-   scripts;
-   respuestas de prácticas;
-   procedimientos que deben razonarse;
-   listas extensas sin contexto;
-   resultados específicos de un dataset;
-   identificadores arbitrarios;
-   valores numéricos fácilmente consultables;
-   conclusiones biológicas complejas.

Pregunta para cada candidata:

> **¿Vale la pena recuperar rápidamente este conocimiento porque libera
> capacidad cognitiva para resolver un problema más complejo?**

Si no, descártala.

## 7. Tipos de flashcards

Etiqueta cada candidata como una o más de:

-   `CONCEPTO`
-   `DISTINCIÓN`
-   `ES-EN`
-   `FORMATO`
-   `COMANDO-OPERACIÓN`
-   `MÉTRICA`
-   `ERROR-FRECUENTE`
-   `BIOLOGÍA`
-   `REPRODUCIBILIDAD`
-   `IA-CRÍTICA`
-   `OTRO`

## 8. Flashcards acumulativas

Detecta conceptos que deben reaparecer después y márcalos:

`FLASHCARD ACUMULATIVA`

Ejemplo:

``` text
U3: ¿Qué es una coordenada genómica?
        ↓
U4: ¿Cómo se obtiene la longitud de un feature?
        ↓
U5: ¿Qué debe conservar un script para que ese cálculo sea reproducible?
```

Busca recuperación espaciada, no mazos aislados por sesión.

## 9. HTML + flashcards

Identifica casos complementarios.

Ejemplo:

``` text
FLASHCARDS
identidad · cobertura · E-value · bit score
        ↓
HTML
comparar Hit A vs Hit B vs Hit C
        ↓
BLAST REAL
ejecutar búsqueda
        ↓
PROTOCOLO
interpretar y documentar
```

Márcalos como:

`AMBOS — funciones complementarias`

## 10. IA y pensamiento crítico

Busca actividades donde pueda presentarse una respuesta generada por IA
y pedir al estudiante detectar:

-   alucinaciones;
-   errores técnicos;
-   estrategias de verificación deficientes;
-   sobreinterpretaciones;
-   confusión similitud/homología;
-   transferencia injustificada de función.

Mantén:

``` text
primero a mano
→ IA
→ contraste
→ validación
```

## 11. Evalúa cada candidato

Asigna:

### Formato

`HTML / FLASHCARDS / AMBOS / MANTENER`

### Valor pedagógico

`ALTO / MEDIO / BAJO`

### Complejidad

HTML: `BAJA / MEDIA / ALTA`\
Flashcards: `BAJA / MEDIA`

### Prioridad

-   `P1` --- debería desarrollarse
-   `P2` --- sería útil
-   `P3` --- opcional
-   `NO` --- conservar formato actual

No confundas atractivo visual con valor pedagógico.

## 12. Revisa S1--S34 completas

No busques solo encabezados "Práctica". Revisa también:

-   teoría;
-   glosarios;
-   preguntas conceptuales;
-   ejercicios;
-   autoevaluaciones;
-   callouts;
-   Antes de clase;
-   Durante el taller;
-   Después del taller;
-   evaluaciones;
-   mini-proyectos;
-   ejercicios de IA;
-   tablas;
-   figuras;
-   errores frecuentes;
-   preguntas de interpretación.

## 13. Entregable 1 --- Inventario completo

Genera:

`auditoria-recursos-interactivos-2026.md`

  -----------------------------------------------------------------------------------------------------
  Sesión   Actividad/contenido   Formato       Tipo     Valor        Complejidad   Prioridad   Razón
                                 recomendado            pedagógico                             
  -------- --------------------- ------------- -------- ------------ ------------- ----------- --------

  -----------------------------------------------------------------------------------------------------

Incluye también actividades revisadas que deban mantenerse.

## 14. Entregable 2 --- Shortlist HTML

Genera:

`shortlist-practicas-html-2026.md`

Selecciona aproximadamente las **10--15 mejores candidatas HTML** del
curso, sin imponer cuotas por unidad.

Para cada una incluye:

-   sesión y nombre;
-   actividad original;
-   oportunidad pedagógica;
-   interacción propuesta;
-   tipo de interacción;
-   antes;
-   después;
-   qué NO debe sustituir;
-   valor pedagógico;
-   complejidad;
-   prioridad.

## 15. Entregable 3 --- Inventario de flashcards

Genera:

`inventario-flashcards-2026.md`

Organízalo por unidad.

Para cada mazo explica su propósito y usa:

  -----------------------------------------------------------------------------------
  ID         Sesión     Tipo       Frente      Reverso    ¿Acumulativa?   Prioridad
             origen                propuesto   esperado                   
  ---------- ---------- ---------- ----------- ---------- --------------- -----------

  -----------------------------------------------------------------------------------

El frente y reverso son propuestas, no el mazo definitivo.

**Evita generar cientos de tarjetas. Prioriza calidad, utilidad y
recuperación espaciada.**

## 16. Entregable 4 --- Top 5 HTML

  ------------------------------------------------------------------------
  Rank        Sesión      Actividad   Beneficio    Esfuerzo    Por qué
                                      pedagógico   técnico     empezar
                                                               aquí
  ----------- ----------- ----------- ------------ ----------- -----------

  ------------------------------------------------------------------------

Selecciona las cinco con mejor relación beneficio/esfuerzo.

## 17. Entregable 5 --- Mejores mazos de flashcards

  ---------------------------------------------------------------------------------
  Rank       Unidad /   Mazo       Conceptos   Nº           Beneficio   Prioridad
             sesiones                          aproximado               
  ---------- ---------- ---------- ----------- ------------ ----------- -----------

  ---------------------------------------------------------------------------------

No necesariamente deben corresponder a cinco sesiones. Piensa en
conjuntos conceptuales.

## 18. Entregable 6 --- Matriz HTML + flashcards

Genera:

`matriz-html-flashcards-2026.md`

  --------------------------------------------------------------------------
  Sesión         Flashcards     HTML aplica    Práctica       Valor
                 preparan                      auténtica      
                                               posterior      
  -------------- -------------- -------------- -------------- --------------

  --------------------------------------------------------------------------

Busca secuencias:

``` text
flashcards
→ HTML
→ práctica auténtica
→ protocolo
```

## 19. Entregable 7 --- Patrones HTML reutilizables

Analiza la reutilización de componentes como:

-   `multiple-choice-feedback`
-   `predict-then-reveal`
-   `classify-cards`
-   `match-concepts`
-   `order-pipeline`
-   `find-the-error`
-   `compare-evidence`
-   `progressive-case`
-   `decision-tree`
-   `ai-error-detection`

  Componente   Función pedagógica   Sesiones donde podría reutilizarse
  ------------ -------------------- ------------------------------------

## 20. Entregable 8 --- Arquitectura futura

Propón, sin crear todavía los directorios:

``` text
interactive/
├── components/
├── u1/
├── u2/
├── u3/
├── u4/
├── u5/
└── u6/

flashcards/
├── u1/
├── u2/
├── u3/
├── u4/
├── u5/
├── u6/
└── acumulativas/
```

Sugiere también si las flashcards conviene mantenerlas en un formato
fuente neutral (por ejemplo CSV/TSV/Markdown estructurado) para después
exportarlas a la plataforma elegida.

## 21. Restricciones futuras de HTML

Evalúa suponiendo que posteriormente deberán:

-   funcionar directamente en navegador;
-   ser autocontenidos;
-   usar HTML + CSS + JavaScript;
-   evitar frameworks salvo necesidad real;
-   no requerir servidor;
-   funcionar offline cuando sea posible;
-   ser responsive;
-   ser accesibles por teclado;
-   utilizar HTML semántico;
-   dar retroalimentación sin IA en tiempo real;
-   no enviar respuestas a servicios externos;
-   almacenarse en Git;
-   publicarse junto al curso.

No implementar todavía tracking, login, bases de datos ni calificaciones
centralizadas.

## 22. No modificar todavía

En esta fase:

-   NO modifiques S1--S34;
-   NO generes HTML;
-   NO generes archivos de Anki/Quizlet;
-   NO elimines prácticas;
-   NO cambies evaluaciones;
-   NO cambies el Plan;
-   NO cambies README;
-   NO cambies la guía;
-   NO cambies figuras;
-   NO crees directorios.

Solo analiza.

## 23. Informe final

Reporta:

1.  total de actividades/contenidos revisados;
2.  candidatas HTML;
3.  candidatas a flashcards;
4.  candidatas `AMBOS`;
5.  distribución P1/P2/P3/NO;
6.  Top 5 HTML;
7.  mejores mazos de flashcards;
8.  número total aproximado de tarjetas recomendado;
9.  flashcards acumulativas;
10. patrones HTML reutilizables;
11. mejores secuencias
    `flashcards → HTML → práctica auténtica → protocolo`;
12. riesgos pedagógicos detectados.

## 24. Criterio final

Para HTML:

> **¿La interactividad obliga al estudiante a pensar mejor o solamente
> hace que la práctica se vea más bonita?**

Para flashcards:

> **¿Recordar con fluidez este concepto ayudará al estudiante a razonar
> mejor después o solamente lo hará memorizar información que podría
> consultar?**

Recomienda el recurso únicamente cuando exista una respuesta pedagógica
clara.
