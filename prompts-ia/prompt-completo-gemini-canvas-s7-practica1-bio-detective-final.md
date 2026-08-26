# Prompt completo para Gemini Canvas — S7 · Práctica 1: Bio Detective

> **Versión consolidada.** Este prompt contiene la Práctica 1 completa y todos los ajustes de diseño e interacción acordados. Gemini debe generar directamente la versión final del recurso; no debe asumir que existe un HTML previo.


Actúa como **diseñador instruccional y desarrollador front-end especializado en bioinformática, biología molecular, aprendizaje activo y recursos educativos interactivos**.

Construye un recurso HTML interactivo para **Introducción a la Bioinformática — LCG, UNAM — 2026**, dentro de **S7 — De los objetos biológicos a FASTA, GFF3 y GenBank**.

El recurso transforma **Práctica 1 — Test de repaso: procesos, elementos y alfabetos** en una experiencia interactiva progresiva.

## 1. Restricción pedagógica

NO inventes una práctica nueva. Conserva las tres partes originales:

1. Verdadero o falso — procesos.
2. De la definición al elemento.
3. ¿Qué tipo de secuencia es?

El HTML debe enriquecer/reemplazar el **primer intento individual**, manteniendo después la dinámica:

```text
primer intento individual
→ comparación con otra persona
→ discusión de desacuerdos
→ retroalimentación
→ corrección visible
→ reflexión en protocolo.md
```

No conviertas la actividad en examen de memorización ni uses puntaje competitivo.

## 2. Objetivos

Al terminar, el estudiante debe:

- distinguir replicación, transcripción y traducción;
- reconocer que gen → transcrito → proteína no siempre es uno a uno;
- distinguir promotor, TSS, UTR, CDS, exón, intrón, operón y gen;
- usar alfabetos biológicos como evidencia;
- reconocer cuándo una secuencia puede clasificarse con certeza;
- reconocer cuándo falta evidencia;
- identificar qué contexto adicional resolvería una ambigüedad.

Idea central:

> **Reconocer patrones es útil, pero no debemos inventar certeza cuando la evidencia no alcanza.**

Flujo cognitivo:

```text
observar → identificar evidencia → interpretar → reconocer límites
→ decidir qué información adicional necesito
```

## 3. Nombre

# Bio Detective

> **Procesos, elementos y alfabetos: ¿qué puedes inferir con la evidencia disponible?**

Estética de detective sutil y universitaria, nunca infantil.

## 4. Arquitectura

```text
MISIÓN 1 — Reconstruir el flujo de información
↓
MISIÓN 2 — Identificar las piezas de un gen
↓
MISIÓN 3 — Leer las pistas de una secuencia
↓
CIERRE — ¿Qué sé, qué infiero y qué no puedo afirmar?
```

Mostrar `Misión 1 de 3`. Sin puntos, vidas, ranking, medallas ni velocidad.

## 5. Retroalimentación

Evita `respuesta → correcto/incorrecto`.

Usa:

```text
respuesta → pista → segundo intento → explicación
```

Las pistas deben orientar sin revelar inmediatamente la solución.

# MISIÓN 1 — Procesos

Conserva exactamente:

1. La replicación usa ADN como molde para producir ARN.
2. La traducción usa un ARNm como molde para producir una proteína.
3. Todos los genes producen una proteína.
4. Un mismo gen puede producir más de un transcrito.
5. La transcripción ocurre después de la traducción.
6. Un operón procariota puede producir varias proteínas a partir de un solo ARN policistrónico.

Respuestas:

1. Falso — replicación: ADN → ADN; transcripción: ADN → ARN.
2. Verdadero — ARNm → proteína.
3. Falso — existen genes que producen ARN funcional.
4. Verdadero — por ejemplo, splicing alternativo.
5. Falso — ARN debe producirse antes de traducirse.
6. Verdadero — un ARN policistrónico puede contener varias regiones codificantes traducibles.

Cuando haya error, formula pistas basadas en el **producto** o el **molde** del proceso.

Cierre interactivo: reconstruir

```text
ADN ──replicación──→ ADN
ADN ──transcripción──→ ARN ──traducción──→ proteína
```

y preguntar:

> ¿La relación gen → transcrito → proteína siempre es uno a uno?

Respuesta: **No**.

# MISIÓN 2 — Elementos

Bolsa original:

- promotor
- TSS
- 5′ UTR
- CDS
- 3′ UTR
- exón
- intrón
- operón
- gen

Conserva estas ocho definiciones:

1. Región donde se organiza el inicio de la transcripción.
2. Primera posición transcrita de un gen.
3. Parte del transcrito, anterior a la región codificante, que no se traduce.
4. Parte de un transcrito que se traduce en una secuencia de aminoácidos.
5. Segmento que se elimina del transcrito primario durante el splicing.
6. Segmento que permanece en el ARN maduro después del splicing.
7. Conjunto de regiones codificantes procariotas transcritas juntas en un solo ARN.
8. Región de material genético que contribuye a producir un ARN o una proteína funcional.

Respuestas:

1. Promotor
2. TSS
3. 5′ UTR
4. CDS
5. Intrón
6. Exón
7. Operón
8. Gen

Implementa matching/tarjetas, no ocho dropdowns aburridos. Si usas drag-and-drop, incluye alternativa accesible.

**3′ UTR** está deliberadamente en la bolsa aunque no sea respuesta de las ocho definiciones. No lo elimines. Al final pregunta qué término no se usó y explica brevemente su posición después de la CDS y su carácter no traducido.

Pistas conceptuales:

- promotor vs TSS: región vs posición;
- CDS vs gen: no todo el gen se traduce;
- exón vs intrón: qué permanece tras splicing;
- 5′ UTR vs CDS: ambas pueden estar en el transcrito, pero solo CDS se traduce.

Cierre visual conceptual:

```text
promotor → TSS → 5′ UTR → CDS → 3′ UTR
```

y, separadamente:

```text
exón — intrón — exón
        ↓ splicing
     exón — exón
```

Aclara que no todos los genes tienen exactamente esa arquitectura.

# MISIÓN 3 — Alfabetos y evidencia

Para cada fragmento elegir:

- ADN
- ARN
- proteína
- No se puede determinar sin más contexto

Después pedir:

> ¿Qué letra o letras sustentan tu decisión?

Usa exactamente:

```text
1. ACAATGTT
2. ACAAUGUU
3. PAFFNK
4. ACGT
5. MSTAC
6. LWTKQ
7. NNNNN
```

Respuestas:

1. `ACAATGTT` → ADN. La T descarta ARN en este contexto.
2. `ACAAUGUU` → ARN. Contiene U.
3. `PAFFNK` → proteína. P y F no son símbolos válidos de nucleótido ni códigos IUPAC de ambigüedad.
4. `ACGT` → **no se puede determinar sin más contexto**. Las cuatro letras también son códigos de aminoácidos.
5. `MSTAC` → **no se puede determinar sin más contexto**. Las letras pueden funcionar como códigos de aminoácidos y códigos de ambigüedad de nucleótidos.
6. `LWTKQ` → proteína. Q no es símbolo de nucleótido/código IUPAC y sí de aminoácido.
7. `NNNNN` → **no se puede determinar sin más contexto**. N puede representar base indeterminada y también asparagina.

Los casos 4, 5 y 7 son pedagógicamente cruciales: **no los simplifiques ni fuerces una respuesta inequívoca**.

Para `ACGT`, si elige ADN, pista:

> A, C, G y T son nucleótidos. ¿Pueden esas mismas letras representar aminoácidos?

Mensaje:

> **Una interpretación plausible no siempre es una interpretación demostrada.**

Para `NNNNN`, preguntar qué evidencia adicional ayudaría: encabezado, base de datos de origen, tipo de registro, secuencia más larga o contexto. Puede haber varias respuestas válidas.

## Nivel de certeza

Después de cada clasificación:

```text
¿Con qué nivel de certeza puedes sostenerlo?

○ La evidencia lo distingue
○ Es probable, pero falta contexto
○ No puedo distinguirlo
```

No puntuarlo.

Cierre:

```text
CLASIFICAR NO ES ADIVINAR

evidencia suficiente → afirmación

evidencia ambigua → reconocer límite → pedir contexto
```

# CIERRE — ¿Qué sabes realmente?

Usa cuatro categorías:

```text
OBSERVÉ
INTERPRETÉ
INFERÍ
NO PUEDO AFIRMARLO TODAVÍA
```

Presenta ejemplos derivados de la práctica, por ejemplo:

- “El fragmento contiene U.” → OBSERVÉ.
- “El fragmento representa ARN.” → interpretación sustentada cuando la evidencia lo distingue.
- “Este gen necesariamente produce una proteína.” → afirmación general no sustentada.
- “NNNNN pertenece a ADN.” → NO PUEDO AFIRMARLO TODAVÍA.

La intención es empezar a separar observación, interpretación e inferencia.

## Preparación para el taller

Conserva durante la sesión:

- primera respuesta;
- respuesta corregida;
- casos donde necesitó pista;
- casos ambiguos.

Pantalla final:

# Lleva tus desacuerdos al taller

1. ¿Qué afirmación sobre procesos te hizo cambiar de opinión?
2. ¿Qué elemento genético te costó más distinguir?
3. ¿Qué fragmento te pareció más ambiguo y por qué?

No generes automáticamente esas respuestas.

## Evidencia que debe permanecer fuera del HTML

NO sustituyas la reflexión posterior en `doc/protocolo.md`. El estudiante debe conservar las tres oraciones originales:

1. qué relación gen → transcrito → proteína no es uno a uno y por qué;
2. qué elemento genético le costó más distinguir;
3. qué pista de alfabeto usaría para reconocer una proteína a primera vista.

## Puente al resto de S7

Final:

> Hasta ahora razonaste sobre **objetos y procesos biológicos**. El siguiente paso es preguntar: **¿cómo se representan esos objetos en archivos que una computadora puede almacenar y procesar?**

```text
objeto biológico
      ↓
representación computacional
      ↓
FASTA / GFF3 / GenBank
```

No enseñes todavía en profundidad la sintaxis de esos formatos.

# Diseño

- limpio, científico, universitario y moderno;
- juvenil sin parecer infantil;
- responsive;
- fondo claro;
- buena jerarquía;
- secuencias monoespaciadas;
- esquemas biológicos sencillos;
- animaciones mínimas.

Evita personajes caricaturescos, estética infantil, sonidos, confeti, rankings y exceso de colores.

# Accesibilidad

Implementa HTML semántico, teclado completo, foco visible, botones reales, `fieldset`/`legend`, labels, `aria-live`, contraste suficiente y feedback que no dependa solo del color.

# Restricciones técnicas

- un único HTML;
- CSS y JavaScript embebidos;
- sin frameworks, React ni Node;
- sin backend/login/tracking/APIs;
- sin dependencias externas obligatorias;
- offline;
- listo para Git;
- fácil de integrar en sitio estático;
- sin IA en tiempo real.

No es necesario persistir al recargar. No mostrar nota numérica.

Resumen final permitido:

```text
Procesos        ✓ revisados
Elementos       ✓ revisados
Alfabetos       ✓ revisados
Casos ambiguos  ✓ identificados
```

# Componentes reutilizables

Organiza el código para reutilizar:

- `mission-card`
- `true-false-reasoning`
- `matching-cards`
- `sequence-classifier`
- `certainty-selector`
- `hint-box`
- `progress-indicator`
- `first-attempt-review`
- `concept-summary`

Mantén coherencia visual con **FASTA Detective — Práctica 3**, como parte de una misma familia de interactivos S7.

# Nombre sugerido

```text
interactive/u3/s7-practica1-bio-detective.html
```

# Integración con Markdown

El HTML debe reemplazar pedagógicamente el primer intento individual de Partes A–C.

Mantener en Markdown:

- título y propósito;
- instrucción “primer intento sin IA”;
- enlace/iframe;
- “Durante el taller — comparación y corrección”;
- reflexión en `doc/protocolo.md`;
- criterio de logro;
- transición a representación computacional.

NO modifiques todavía S7.

# Entregables

Genera:

1. HTML completo y funcional;
2. explicación breve de arquitectura;
3. descripción de las tres misiones;
4. instrucciones para probarlo localmente;
5. recomendación de integración en S7;
6. fragmento Markdown para enlace/iframe;
7. nota de accesibilidad;
8. decisiones técnicas importantes.

Antes de terminar verifica:

- 6 afirmaciones originales de Parte A;
- 8 definiciones originales de Parte B;
- 7 fragmentos originales de Parte C;
- respuestas fieles a la práctica;
- casos ambiguos conservados como ambiguos;
- no inventar certeza;
- primer intento distinguible de corrección;
- discusión entre pares aún necesaria;
- reflexión en `protocolo.md` preservada;
- no adelantar innecesariamente FASTA/GFF3/GenBank;
- funcionamiento offline.


---

# ESPECIFICACIONES FINALES OBLIGATORIAS

Las siguientes especificaciones forman parte de la versión final desde el primer renderizado. No las trates como cambios posteriores.

## A. Feedback visual inequívoco en Misión 1

Cuando el estudiante seleccione Verdadero/Falso:

- respuesta correcta: estado visual verde + `✓ Correcto`;
- respuesta incorrecta: estado visual rojo + `✗ Incorrecto`;
- el color nunca será la única señal;
- mantener contraste y accesibilidad;
- conservar la lógica `error → pista → segundo intento → explicación`;
- ante el primer error NO revelar inmediatamente la opción correcta;
- registrar si fue correcto al primer intento y si necesitó pista.

## B. Registro del proceso del estudiante

Para cada reactivo conserva durante la sesión, según corresponda:

- enunciado o fragmento;
- primera respuesta;
- resultado del primer intento;
- segundo intento, si existió;
- uso de pista;
- respuesta final;
- nivel de certeza;
- evidencia o justificación indicada.

No es necesario persistir los datos después de recargar la página.

## C. Descarga de resultados

En la pantalla final incluye:

**⬇ Descargar mis resultados**

Debe generar localmente:

```text
bio-detective-resultados.md
```

Usa JavaScript del navegador (`Blob`, `URL.createObjectURL`, `<a download>` o equivalente), sin servidor ni dependencias.

El reporte debe reflejar el estado REAL de la actividad y contener:

```markdown
# Bio Detective — Resultados

S7 — De los objetos biológicos a FASTA, GFF3 y GenBank
Práctica 1 — Test de repaso: procesos, elementos y alfabetos

Fecha: [automática]

## Misión 1 — Procesos

### Pregunta 1
[enunciado]

Primer intento: [...]
Resultado del primer intento: Correcto / Incorrecto
Usó pista: Sí / No
Respuesta final: [...]

## Misión 2 — Elementos genéticos

Definición: [...]
Primera selección: [...]
Resultado del primer intento: [...]
Usó pista: Sí / No
Respuesta final: [...]

## Misión 3 — Alfabetos

Fragmento: [...]
Primera clasificación: [...]
Respuesta final: [...]
Nivel de certeza: [...]
Evidencia indicada: [...]

## Reflexión para el taller

### ¿Qué afirmación sobre procesos te hizo cambiar de opinión?
[respuesta]

### ¿Qué elemento genético te costó más distinguir?
[respuesta]

### ¿Qué fragmento te pareció más ambiguo y por qué?
[respuesta]

## Resumen descriptivo

Procesos revisados: 6
Elementos revisados: 8
Secuencias revisadas: 7
Preguntas en las que se utilizó una pista: [n]
Casos identificados como ambiguos: [n]
```

Si falta un campo, escribir `Sin respuesta`.

El reporte NO debe incluir calificación, porcentaje, aprobado/reprobado, ranking ni nota.

## D. Misión 2 debe ser un mapa biológico interactivo, NO una bolsa de términos

Sustituye cualquier “bolsa de términos” por una experiencia visual en la que el estudiante construya un modelo conceptual.

La lógica será:

```text
definición
→ observar representación biológica
→ seleccionar región/concepto
→ feedback
→ pista si hace falta
→ segundo intento
→ revelar etiqueta
→ mapa progresivamente construido
```

### Mapa A — Inicio y estructura del transcrito

Debe permitir construir progresivamente:

```text
promotor → TSS → 5′ UTR → CDS → 3′ UTR
```

Inicialmente las regiones NO deben mostrar sus nombres. Conforme se resuelven, las etiquetas aparecen.

### Mapa B — Splicing

Representar conceptualmente:

```text
ANTES
[ EXÓN ] — [ INTRÓN ] — [ EXÓN ]

              ↓ splicing

DESPUÉS
[ EXÓN ] — [ EXÓN ]
```

Debe ayudar a distinguir “permanece” frente a “se elimina”.

### Mapa C — Organización procariota

Representar:

```text
Promotor
   ↓
[ CDS A ][ CDS B ][ CDS C ]
          ↓
    ARN policistrónico
          ↓
Proteína A + Proteína B + Proteína C
```

### Mapa D — Gen

Representar un gen como una región de material genético asociada con la producción de un ARN o producto funcional.

Evitar explícitamente:

```text
gen = CDS
gen = proteína
```

### Tratamiento de 3′ UTR

`3′ UTR` debe aparecer en el mapa, aunque no sea respuesta de las ocho definiciones originales.

Al final preguntar:

> **Hay una región del mapa que observaste pero que ninguna definición te pidió identificar. ¿Cuál es?**

Respuesta: **3′ UTR**.

Después explicar brevemente su posición y que forma parte del transcrito pero no de la región traducida.

## E. Accesibilidad del mapa

Si se usa SVG o regiones clicables:

- navegación por teclado;
- Enter/Space para seleccionar;
- foco visible;
- nombre accesible;
- ARIA apropiado;
- alternativa textual;
- no depender exclusivamente del color.

## F. Fidelidad obligatoria

La versión final debe conservar exactamente:

- las 6 afirmaciones de Misión 1;
- las 8 definiciones de Misión 2;
- los 7 fragmentos de Misión 3;
- los casos ambiguos `ACGT`, `MSTAC` y `NNNNN`;
- la calibración de certeza;
- el segundo intento con pistas;
- la discusión posterior entre pares;
- la reflexión en `doc/protocolo.md`;
- el puente conceptual hacia FASTA/GFF3/GenBank.

No agregues contenido que cambie el alcance de S7.

---

# VALIDACIÓN FINAL ANTES DE ENTREGAR

Prueba mentalmente y revisa el HTML completo antes de entregarlo.

Verifica:

1. Las seis afirmaciones de Misión 1 funcionan.
2. Verde + ✓ + texto identifican una respuesta correcta.
3. Rojo + ✗ + texto identifican una respuesta incorrecta.
4. Un primer error no revela inmediatamente la solución.
5. El segundo intento funciona.
6. Se registra el primer intento.
7. Los ocho conceptos de Misión 2 se trabajan mediante mapas, no mediante una bolsa.
8. El mapa se etiqueta progresivamente.
9. `3′ UTR` permanece y tiene una función pedagógica.
10. No se representa `gen = CDS` ni `gen = proteína`.
11. Los siete fragmentos de Misión 3 están presentes.
12. `ACGT`, `MSTAC` y `NNNNN` conservan su ambigüedad.
13. El nivel de certeza funciona.
14. Las respuestas/reflexiones finales se almacenan.
15. El botón genera `bio-detective-resultados.md`.
16. El archivo descargado refleja respuestas reales, no datos de ejemplo.
17. El reporte no asigna una nota.
18. Todo funciona mediante teclado.
19. Todo funciona offline.
20. No existen dependencias externas obligatorias.
21. El diseño sigue siendo científico, limpio, universitario y coherente con “FASTA Detective”.

# ENTREGA

Entrega directamente:

1. **el HTML completo final**, no parches ni fragmentos;
2. una explicación breve de su arquitectura;
3. instrucciones para probarlo localmente;
4. el fragmento Markdown recomendado para integrarlo en S7;
5. una lista corta de las decisiones de accesibilidad implementadas.

No pidas confirmación antes de generar el recurso.
