# Plan de implementación — Sitio Quarto (Website)

**Decisión previa:** [01-estudio-formatos-quarto-github.md](01-estudio-formatos-quarto-github.md) → **Quarto Website**.  
**Fuente:** `contenidos-2026/`  
**Meta:** sitio elegante, poco complejo, que preserve Curso → Unidades → Sesiones.

Este documento es el plan operativo. La implementación (esqueleto, migración, Pages) se hace en pasos posteriores, cuando se indiquen.

---

## 1. Principios de la implementación

1. **Un solo proyecto Quarto** (`type: website`). Sin Book paralelo ni diapositivas como shell.
2. **No reescribir la pedagogía.** Solo formateo, navegación y publicación.
3. **`contenidos-2026/` sigue siendo la fuente canónica** del Markdown didáctico. El sitio Quarto es la capa de publicación.
4. **Excluir del sitio:** `docente/`, `README.md` y `plantilla-unidad.md` de contenidos (canon editorial), `images/archivadas/`, `images/fuentes/`, `.docx`.
5. **Español en la UI:** `lang: es`.
6. **Build fuera de `main`:** render → `_site/` → desplegar a `gh-pages` (no commitear el HTML generado en la rama de trabajo).

---

## 2. Dónde vive el proyecto

| Ruta | Rol |
| --- | --- |
| `contenidos-2026/` | Fuente didáctica (Markdown, imágenes, ejemplos) |
| `curso-quarto/` | Proyecto Quarto Website (nuevo) |
| `planificacion-quarto/` | Documentos de diseño (esta carpeta) |

**Estrategia de contenido en v1 (simple):** copiar al proyecto Quarto las páginas publicables y los assets necesarios (`images/` activos + `ejemplos/`), manteniendo rutas relativas como en los `.md` actuales. Así no se inventa una estructura de carpetas por unidad ni se rompen enlaces `images/…` y `ejemplos/…`.

Alternativa descartada en v1: symlinks o render directo desde `contenidos-2026/` como raíz del proyecto (mezclaría canon editorial, `docente/` y riesgo de publicar de más).

```text
curso-quarto/
├── _quarto.yml
├── index.qmd                 # Inicio del curso
├── programa.qmd              # Ruta breve U1–U6 + transversal
├── recursos.qmd              # Datos, lecturas, enlaces
├── styles.css                # Ajustes mínimos de tipografía/ancho
├── .gitignore                # _site/, .quarto/
├── images/                   # Copia de PNG (+ SVG si se desea)
├── ejemplos/                 # Copia de ejemplos/datos
├── u1-trabajo-reproducible.md
├── u1-s1-documentar-markdown-fases.md
├── …                         # resto de portadas y sesiones
├── s14-s15-mini-proyecto-investigacion-I.md
├── s16-mini-proyecto-revision-pares.md
├── s17-evaluacion-individual-demostrativa.md
└── mini-proyecto-dictamen-cientifico.md
```

Los archivos de lección pueden permanecer en `.md` al inicio. Pasar a `.qmd` solo cuando se añada YAML de página o callouts nativos de Quarto.

---

## 3. Esqueleto de `_quarto.yml`

Valores orientativos (se ajustarán al implementar):

```yaml
project:
  type: website
  output-dir: _site

lang: es

website:
  title: "Introducción a la Bioinformática"
  site-url: https://USER.github.io/REPO/   # completar al publicar
  repo-url: https://github.com/ORG/REPO    # completar
  repo-actions: [edit, issue]
  reader-mode: true
  navbar:
    background: primary
    left:
      - href: index.qmd
        text: Inicio
      - href: programa.qmd
        text: Programa
      - text: Unidades
        menu:
          - href: u1-trabajo-reproducible.md
            text: "U1 — Trabajo reproducible"
          - href: u2-entorno-unix.md
            text: "U2 — Entorno Unix"
          - href: u3-datos-bases-datos.md
            text: "U3 — Datos y bases"
          - href: u4-procesamiento-exploracion.md
            text: "U4 — Procesamiento genómico"
          - href: u5-automatizacion-scripting.md
            text: "U5 — Automatización"
          - href: u6-comparacion-homologia.md
            text: "U6 — Comparar / hipótesis"
      - href: recursos.qmd
        text: Recursos
  sidebar:
    style: docked
    search: true
    collapse-level: 1
    contents:
      - section: "Unidad 1"
        contents:
          - u1-trabajo-reproducible.md
          - u1-s1-documentar-markdown-fases.md
          - u1-s2-organizar-fair-ia.md
      - section: "Unidad 2"
        contents:
          - u2-entorno-unix.md
          - u2-s3-shell-acceso-remoto.md
          - u2-s4-sistema-archivos-v3.md
          - u2-s5-archivos-permisos-procesos-v2.md
          - u2-s6-consolidacion-entorno-unix.md
      - section: "Unidad 3"
        contents:
          - u3-datos-bases-datos.md
          - u3-s7-secuencias-formatos-genbank.md
          - u3-s8-bases-datos-descarga-integridad.md
          - u3-s9-inspeccion-transferencia-verificable.md
      - section: "Unidad 4"
        contents:
          - u4-procesamiento-exploracion.md
          - u4-s10-anatomia-flujos-datos.md
          - u4-s11-estructura-tabular-anotacion.md
          - u4-s12-filtrado-conteos-genoma.md
          - u4-s13-inventario-resumen-genoma.md
          - u4-s18-precision-patrones-expresiones-regulares.md
          - u4-s19-extraccion-identificadores-correspondencia.md
          - u4-s20-normalizar-datos-comparables.md
          - u4-s21-confrontar-fuente-independiente.md
          - u4-s22-condicionar-calcular-columnas.md
          - u4-s23-protocolo-ejecutable-genoma.md
      - section: "Unidad 5"
        contents:
          - u5-automatizacion-scripting.md
          - u5-s24-del-protocolo-al-script.md
          - u5-s25-separar-procedimiento-datos.md
          - u5-s26-procesamiento-por-lotes.md
          - u5-s27-herramienta-cientifica.md
          - u5-s28-proyecto-integrador.md
          - u5-s29-cluster-hpc-sge.md
      - section: "Unidad 6"
        contents:
          - u6-comparacion-homologia.md
          - u6-s30-comparar-alinear.md
          - u6-s31-buscar-blast.md
          - u6-s32-interpretar-inferir.md
          - u6-s33-defender-hipotesis.md
          - u6-s34-integrar-hipotesis-casos-ciegos.md
      - section: "Transversal"
        contents:
          - s14-s15-mini-proyecto-investigacion-I.md
          - s16-mini-proyecto-revision-pares.md
          - s17-evaluacion-individual-demostrativa.md
          - mini-proyecto-dictamen-cientifico.md
      - recursos.qmd

format:
  html:
    theme: cosmo
    css: styles.css
    toc: true
    toc-depth: 3
    toc-location: right
    code-copy: true
    code-overflow: wrap
    link-external-newwindow: true
```

**Tema.** `cosmo` (o `flatly`) como base Bootstrap limpia; `styles.css` solo para ancho de lectura, tipografía de código y detalles de callouts — sin rediseño pesado.

**Títulos en el sidebar.** Quarto usará el H1 de cada página. Si algún H1 es demasiado largo, se puede acortar con YAML `title:` / `short-title:` al pasar a `.qmd`.

---

## 4. Páginas de marco (no son lecciones)

| Página | Contenido |
| --- | --- |
| `index.qmd` | Identidad del curso, principio *preguntas permanecen / estrategias evolucionan*, cómo usar el sitio (aula invertida), enlace a U1 |
| `programa.qmd` | Vista compacta U1–U6 + transversal; sin volcar el README editorial |
| `recursos.qmd` | Dónde están `ejemplos/`, lecturas (Buffalo), cluster, enlaces útiles |

Estas páginas **sí** pueden mencionar Quarto/navegación. El texto de las lecciones **no** debe hablar de Quarto (regla ya en la guía de generación).

---

## 5. Orden de trabajo (fases de ejecución)

### Paso A — Esqueleto vacío

1. Crear `curso-quarto/` con `_quarto.yml`, `index.qmd`, `programa.qmd`, `recursos.qmd`, `styles.css`, `.gitignore`.
2. Sidebar mínimo (solo Inicio + una unidad de prueba, p. ej. U1).
3. `quarto preview` local hasta que la navegación se vea bien.

### Paso B — Primera unidad completa (piloto)

1. Copiar U1 (portada + S1 + S2) + `images/` necesarios + `ejemplos/` usados por U1.
2. Verificar enlaces internos y figuras.
3. Ajustar CSS si el TOC o los callouts en blockquote se ven pobres.
4. Criterio de salida del piloto: un tercero navega U1 sin instrucciones extra.

### Paso C — Resto del curso

1. Copiar U2–U6 + transversal en el orden del sidebar (§3).
2. Copiar el resto de `images/` (PNG activos) y `ejemplos/` completo.
3. Ampliar `_quarto.yml` al árbol completo.
4. Corregir enlaces rotos hacia `../introBioInfo/...` (PDF Buffalo → `recursos/` o `referencias/` del sitio; plantillas ya en `ejemplos/`).

### Paso D — Callouts Quarto (pasada editorial)

Conversión según el mapa del README de contenidos:

| Marcador actual | Callout Quarto |
| --- | --- |
| `> **NOTA:**` / `> **NOTA — …**` | `::: {.callout-note}` |
| `> **IMPORTANTE:**` | `::: {.callout-important}` |
| `> **TIP:**` / `¿SABÍAS QUE?` / `COMENTARIO` | `::: {.callout-tip}` |
| `> **ADVERTENCIA:**` | `::: {.callout-warning}` |

- Se puede hacer por unidad, empezando por U1 (estándar de oro).
- Conservar `<details><summary>Ver retroalimentación</summary>` sin convertir.
- No inventar callouts nuevos; solo mapear los existentes.

### Paso E — Publicación

1. Documentar en `03-despliegue-github-pages.md`.
2. GitHub Action: instalar Quarto → `quarto render` en `curso-quarto/` → publicar `_site/` a `gh-pages`.
3. Activar GitHub Pages desde esa rama.
4. Completar `site-url` y `repo-url` en `_quarto.yml`.

---

## 6. Qué se copia y qué no

### Incluir en `curso-quarto/`

- Las 6 portadas y todas las sesiones listadas en el sidebar (§3).
- Material transversal (4 archivos).
- `images/*.png` (y opcionalmente SVG pareados); **no** `archivadas/` ni `fuentes/`.
- `ejemplos/` completo (datos U1, plantillas, `datos-alineamientos/`, zip S34).
- PDF Buffalo al publicar (hoy en `introBioInfo/referencias/`), con ruta actualizada en las lecciones que lo enlacen.

### Excluir

- `contenidos-2026/docente/`
- `contenidos-2026/README.md`, `plantilla-unidad.md`
- `*.docx` en contenidos
- `.DS_Store`
- Cualquier HTML/Rmd legacy de `introBioInfo/lecciones/` como contenido del sitio nuevo

---

## 7. Riesgos y mitigaciones

| Riesgo | Mitigación |
| --- | --- |
| H1 demasiado largos en el sidebar | `title` / texto corto en YAML al convertir a `.qmd` |
| Callouts aún en blockquote se ven “planos” | Paso D; mientras tanto, CSS ligero sobre blockquotes |
| Rutas `../introBioInfo/` rotas en el sitio | Checklist de grepeo antes del primer deploy |
| Sitio publica material docente por error | Nunca copiar `docente/`; lista blanca de archivos en el sidebar |
| Duplicar contenido y olvidar sincronizar | En v1: copiar al publicar/hitos; más adelante se puede automatizar un script `sync-contenidos.sh` |
| `_site/` en el repo | `.gitignore` + deploy solo a `gh-pages` |

---

## 8. Criterios de aceptación (v1)

Cumplidos el 2026-08-11 — ver [04-cierre-v1.md](04-cierre-v1.md).

- [x] `quarto preview` muestra Curso → U1–U6 → sesiones en el orden del plan.
- [x] Portadas y sesiones conservan H1, prácticas, tablas y código.
- [x] Figuras de `images/` y enlaces a `ejemplos/` resuelven.
- [x] `<details>` de retroalimentación funciona en el navegador.
- [x] `docente/` no aparece en el sitio ni en el sidebar.
- [x] Página de inicio explica aula invertida sin jerga de implementación.
- [x] Deploy a GitHub Pages sirve el sitio por HTTPS.
- [x] No hay segundo proyecto Book ni carpeta de slides obligatoria.

---

## 9. Fuera de alcance (v1)

- PDF/EPUB del curso.
- RevealJS por sesión.
- Ejecutar código bash dentro de Quarto (las lecciones son estáticas).
- Reorganizar `contenidos-2026/` en subcarpetas por unidad.
- Rediseño visual elaborado (gradients, tipografías custom pesadas).
- Traducir o reescribir lecciones.

---

## 10. Checklist de arranque (siguiente indicación)

Cuando se pida **Paso A — esqueleto**:

1. Crear `curso-quarto/` con los archivos de marco.
2. `_quarto.yml` con sidebar de U1 solamente (o completo vacío de archivos aún no copiados — preferible U1 piloto).
3. `quarto preview` y captura de decisión de tema/CSS.
4. No migrar U2–U6 hasta validar el piloto.

---

## 11. Relación con los otros documentos

| Documento | Estado |
| --- | --- |
| [01-estudio-formatos-quarto-github.md](01-estudio-formatos-quarto-github.md) | Hecho — decide Website |
| **Este archivo (02)** | Hecho — plan operativo |
| [03-despliegue-github-pages.md](03-despliegue-github-pages.md) | Hecho — Action + Pages en producción |
| [04-cierre-v1.md](04-cierre-v1.md) | Hecho — criterios v1 cumplidos |
