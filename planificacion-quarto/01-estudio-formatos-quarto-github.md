# Estudio de formatos Quarto para publicar el curso en GitHub Pages

**Curso:** Introducción a la Bioinformática (LCG, UNAM)  
**Fuente de contenido:** `contenidos-2026/`  
**Objetivo de este documento:** decidir *cómo* publicar el material en la web con Quarto, antes de implementarlo.  
**Criterios guía:** elegancia, poca complejidad, fidelidad a la estructura de las lecciones.

---

## 1. Qué hay que publicar

El material vigente no es un conjunto de diapositivas ni un blog. Es un curso de **aula invertida** con esta jerarquía:

```text
Curso
└── Unidades (portadas U1–U6)
    └── Sesiones / módulos (S1–S34, con hueco intencional S14–S17)
        └── Secciones conceptuales + prácticas intercaladas
```

Además existen páginas **transversales** (mini-proyecto S14–S17, dictamen científico) que no pertenecen a una sola unidad.

### Inventario relevante de `contenidos-2026/`

| Tipo | Qué es | Publicar |
| --- | --- | --- |
| Portadas `uN-*.md` | Ficha, ruta y módulos de la unidad | Sí |
| Sesiones `uN-sNN-*.md` | Lecciones largas (concepto → práctica → evidencia) | Sí |
| Transversal `s14-…`, `s16-…`, `s17-…`, `mini-proyecto-…` | Trabajo entre unidades | Sí |
| `images/*.png` | Figuras para la web | Sí |
| `ejemplos/` | Datos y plantillas enlazados desde las lecciones | Sí |
| `README.md`, `plantilla-unidad.md` | Guía editorial interna | No (o solo como doc interno) |
| `docente/` | Notas, auditorías, originales | **No** |
| `images/archivadas/`, `images/fuentes/` | Archivo / fuentes de figura | **No** |

El README de contenidos ya anticipa Quarto como fase posterior: callouts, `.qmd`, tema y navegación. Hoy el repo **no** tiene `_quarto.yml` ni `.qmd`. El sitio legacy (`introBioInfo/`) es bookdown/HTML antiguo; sirve de referencia, no de molde.

### Rasgos de las lecciones que el formato debe respetar

- Un solo H1 por sesión (`# S22 — …`).
- Callouts en blockquote: `NOTA`, `IMPORTANTE`, `TIP`, `ADVERTENCIA`, etc.
- Prácticas intercaladas después del concepto (no un apéndice al final).
- Retroalimentación en `<details><summary>Ver retroalimentación</summary>`.
- Figuras con `![alt](images/…)` + pie `**Figura N.**`.
- Bloques de código (`bash`, etc.) y tablas densas (fichas, rúbricas).
- Enlaces relativos entre portada ↔ sesión y a `ejemplos/`.
- Texto en español; la UI del sitio debe ir en español (`lang: es`).

---

## 2. Criterios de decisión

| Criterio | Pregunta concreta |
| --- | --- |
| Fidelidad jerárquica | ¿Se ve Curso → Unidad → Sesión sin forzar otra metáfora? |
| Fidelidad de lección | ¿Soporta páginas largas, callouts, código, figuras y `<details>`? |
| Elegancia | ¿La primera impresión es de sitio de curso serio, no de plantilla genérica? |
| Simplicidad | ¿Un solo proyecto Quarto, configuración breve, un flujo de despliegue? |
| Navegación | ¿Puedo saltar a U4 / S22 sin recorrer un “siguiente capítulo”? |
| GitHub Pages | ¿Sale HTML estático desplegable con Actions o `quarto publish`? |
| Migración | ¿Parte de los `.md` actuales sin reescribir la pedagogía? |

---

## 3. Formatos Quarto evaluados

### 3.1 Quarto Website (`project: type: website`)

**Idea.** Un sitio estático con `navbar` + `sidebar`. Cada portada y cada sesión es una página.

**Fortalezas para este curso**

- El sidebar anidado mapea directo a **Unidades → Sesiones**.
- Las páginas son independientes: la portada no “es el capítulo 0” de un libro.
- HTML completo: callouts Quarto, `<details>`, figuras, código, búsqueda.
- Hueco para páginas extra (programa, recursos, FAQ) sin forzar el modelo.
- Complejidad baja: un `_quarto.yml` y un árbol de navegación.

**Debilidades**

- No trae numeración automática tipo libro ni PDF/EPUB del curso entero.
- Las referencias cruzadas (`@sec-`, `@fig-`) entre archivos no son el centro del diseño (se pueden enlazar en Markdown a mano, como hoy).

**Navegación sugerida**

- **Navbar:** Inicio · Programa · Unidades · Recursos.
- **Sidebar:** una sección por unidad (portada + sesiones en orden del plan) + bloque transversal (S14–S17 / dictamen).

**Despliegue GitHub Pages.** Salida `_site/` → Action a `gh-pages`, o `quarto publish gh-pages`.

**Veredicto parcial.** Mejor encaje como formato principal.

---

### 3.2 Quarto Book (`project: type: book`)

**Idea.** Un libro HTML (también es un sitio) con Parts y Chapters; opcional PDF/EPUB.

**Fortalezas**

- Parts ≈ unidades, chapters ≈ sesiones; TOC elegante y orden de lectura claro.
- Numeración y referencias cruzadas fuertes.
- Misma calidad HTML que el Website para callouts, figuras y código.

**Debilidades**

- Metáfora de **libro**: numeración, “siguiente/anterior”, sensación de texto continuo.
- Las portadas y el material transversal encajan peor (hay que marcar capítulos sin número / apéndices).
- Un poco más de YAML y de política de numeración.
- El estudiante puede percibir “manual” en lugar de “sitio del curso”.

**Despliegue.** Igual que Website; salida típica `_book/`.

**Veredicto parcial.** Alternativa sólida **si** más adelante se prioriza PDF/EPUB o referencias cruzadas numeradas. No es la opción más simple para un sitio de curso 2026.

---

### 3.3 Quarto Manuscript

Pensado para **un artículo** académico (HTML/PDF/Docx, notebooks asociados).

No escala a Curso → Unidades → Sesiones. La arquitectura de información es la de un paper, no la de un temario. **Descartado** como shell del curso (a lo sumo, un entregable puntual tipo dictamen en el futuro).

---

### 3.4 RevealJS (diapositivas) como vehículo principal

Útil para el **taller presencial**, malo como contenedor del curso.

Las lecciones son documentos largos (preparación previa, prácticas, rúbricas, glosario). En diapositivas se pierden `<details>`, tablas densas y la lectura previa. Mantener lección + deck por sesión duplica mantenimiento.

**Veredicto.** Complemento opcional más adelante (un deck por taller enlazado desde la sesión). **No** como formato primario.

---

### 3.5 Híbrido: Website + Book (dos proyectos)

| Patrón | Idea | Coste |
| --- | --- | --- |
| A. Solo Website con sidebar ordenado | “Sabor a libro”, un proyecto | Bajo — recomendado |
| B. Solo Book con navbar ligera | Libro con links de curso | Medio |
| C. Dos proyectos (portal + libro) | Landing + `_book` | Alto: dos renders, rutas, temas |

Dos proyectos Quarto duplican CI, rompen con facilidad rutas a `images/` y `ejemplos/`, y complican el base URL en GitHub Pages. **Fuera de alcance en v1.**

---

### 3.6 Quarto Blog

Orden cronológico y posts. Las sesiones no son entradas de blog; las unidades no son categorías naturales.

**Veredicto.** No como shell. Más adelante se puede añadir un listing de “novedades / errata” *dentro* del Website si hace falta.

---

## 4. Tabla comparativa

| Formato | Jerarquía del curso | Lecciones largas (HTML) | Elegancia / simplicidad | Navegación | GitHub Pages | Complejidad |
| --- | --- | --- | --- | --- | --- | --- |
| **Website** | Excelente | Excelente | Alta | Navbar + sidebar anidado | `_site/` | Baja–media |
| **Book** | Excelente (lineal) | Excelente | Alta si se acepta “libro” | TOC Parts/Chapters | `_book/` | Media |
| Manuscript | Pobre | Solo artículo | Herramienta equivocada | Artículo | Como sitio | Media / inútil |
| RevealJS primario | Pobre | Débil | Baja a escala | Decks | HTML en sitio | Alta a escala |
| Híbrido dual | Buena si se disciplina | Buena | Baja (operación) | Partida | Dos salidas | Alta |
| Blog | Pobre como shell | OK para posts | Shell equivocado | Cronológica | Como sitio | Baja / inútil |

---

## 5. Mapeo al árbol real de `contenidos-2026`

Propuesta de sidebar (orden pedagógico, no alfabético):

```text
Inicio (index)
Programa
Recursos

Unidad 1 — Trabajo reproducible
  Portada          u1-trabajo-reproducible.md
  S1               u1-s1-documentar-markdown-fases.md
  S2               u1-s2-organizar-fair-ia.md

Unidad 2 — Entorno Unix
  Portada          u2-entorno-unix.md
  S3–S6            u2-s3-… … u2-s6-…

Unidad 3 — Datos y bases
  Portada + S7–S9

Unidad 4 — Procesamiento genómico
  Portada + S10–S13 + S18–S23   (S14–S17 no van aquí)

Unidad 5 — Automatización
  Portada + S24–S29

Unidad 6 — Comparar / hipótesis
  Portada + S30–S34

Transversal
  Mini-proyecto S14–S15, S16, S17, dictamen
```

Los archivos hoy viven **planos** en la raíz de `contenidos-2026/` (sin carpetas `u1/`, `u2/`). Eso es compatible con Quarto: el sidebar declara el orden; no hace falta reorganizar carpetas en v1. Si más adelante se desea `curso-quarto/u4/s10-….qmd`, sería una migración de rutas, no un cambio de formato.

---

## 6. Implicaciones técnicas comunes (Website o Book)

| Tema | Orientación |
| --- | --- |
| Idioma | `lang: es` en el proyecto |
| Origen `.md` | Quarto puede renderizar `.md`; pasar a `.qmd` cuando haga falta YAML o callouts nativos |
| Callouts | Mapa ya definido en el README de contenidos → `::: {.callout-note\|important\|tip\|warning}` |
| Retroalimentación | Conservar `<details>` en HTML; funciona en web; no en PDF |
| Figuras | Preferir PNG en el sitio; SVG como fuente editable |
| Assets | Mantener `images/` y `ejemplos/` dentro del proyecto; corregir enlaces `../introBioInfo/…` al publicar |
| Exclusiones | `docente/`, plantilla editorial, archivadas/fuentes |
| Despliegue limpio | Código en `main`; build en Action → `gh-pages` (evitar commitear `_site/` en `main`) |

---

## 7. Recomendación

**Elegir Quarto Website** como formato de publicación del curso.

Motivos, en orden:

1. Respeta **Curso → Unidades → Sesiones** con una barra lateral anidada, sin imponer numeración de libro.
2. Conserva lecciones largas: prácticas, callouts, figuras, código y retroalimentación colapsable.
3. Es el camino **más simple** para un sitio elegante en GitHub Pages (un proyecto, un `_quarto.yml`, un deploy).
4. Encaja con lo que ya dice el material: Quarto es fase de *formateo*, no reescritura pedagógica.
5. Deja abierta la puerta a diapositivas de taller o a un Book/PDF **más adelante**, sin amarrar v1 a ese coste.

**Quarto Book** queda como alternativa explícita solo si, en una fase posterior, se exige PDF/EPUB del curso completo o un aparato fuerte de referencias cruzadas numeradas.

**No elegir en v1:** Manuscript, Blog como shell, RevealJS como vehículo principal, ni dos proyectos Website+Book.

---

## 8. Decisión (texto listo para actas / README de planificación)

> Publicaremos el curso con **Quarto Website** en GitHub Pages. La navegación será **navbar + sidebar por unidad**, de modo que se preserve la jerarquía Curso → Unidades → Sesiones y el modelo de aula invertida de `contenidos-2026`. Quarto Book, diapositivas y un PDF global quedan fuera del alcance de la primera versión; se reconsiderarán solo si aparece un requisito concreto de libro o de material presencial complementario.

---

## 9. Siguiente paso (fuera de este documento)

Cuando se indique, la siguiente entrega en esta carpeta es el **plan de implementación** operativo (`02-plan-implementacion-sitio-quarto.md`): esqueleto del proyecto, `_quarto.yml` propuesto, orden de migración, exclusiones y criterios de aceptación — siempre asumiendo Website como formato fijado aquí.
