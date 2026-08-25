# Auditoría de estructura — `curso-quarto/` (2026)

**Fecha:** 2026-08-24  
**Alcance:** solo inspección; no se movió, renombró ni eliminó ningún archivo.  
**Origen del encargo:** `prompts-ia/Auditoría de estructura de curso-quarto.md`

## Veredicto

`curso-quarto/` tiene una base usable (sesiones en sidebar, HTML recientes con patrón `uN-sN-pN-…`, recursos en `html/`, `images/`, `ejemplos/`), pero **no cumple aún el objetivo** “sesión → prácticas → HTML → recursos” de forma fiable: hay **1 enlace roto**, **3 HTML sin enlace en lecciones**, nomenclatura mixta y sesiones/prácticas difíciles de indexar de forma automática.

---

## 1. Mapa de la estructura actual

```
curso-quarto/
├── _quarto.yml          # nav + resources: ejemplos/**, images/**, html/**
├── styles.css
├── scripts/sync-from-contenidos.py   # aún asume sync desde contenidos-2026
├── index.qmd, programa*.qmd, acerca.qmd, recursos.qmd, contribuir.qmd
├── u1-…u6-*.md          # intros de unidad
├── uN-sNN-*.md          # sesiones (raíz plana)
├── s14-s15-…, s16-…, s17-…, mini-proyecto-….md
├── html/                # 9 interactivos
├── images/              # figura-uN-sNN-….png
└── ejemplos/            # protocolos, datos alineamientos, zips
```

**Sesiones en sidebar (orden pedagógico):**  
S1–S2 (U1) → S3–S6 (U2) → S7–S9 (U3) → S10–S13, S18–S23 (U4) → mini S14–S17 → S24–S29 (U5) → S30–S34 (U6).

### HTML actuales

| Archivo | Convención | Enlazado desde lección |
| --- | --- | --- |
| `u1-s1-p1-bioinformatics_strategy_lab.html` | OK | S1 P1 |
| `u1-s1-p2-protocol_builder.html` | OK (archivo) | S1 P2 apunta a ruta **incorrecta** |
| `u1-s2-p1-data_steward_lab.html` | OK | **no** |
| `u1-s2-p2-ia_bajo_la_lupa.html` | OK | **no** |
| `u3-s7-p1-bio_detective.html` | OK | S7 P1 |
| `u3-s7-p3-fasta_detective.html` | OK (salta p2) | S7 P3 |
| `u3-s7-p4-gff3_explorer.html` | OK | S7 P4 |
| `u3-s7-p5-reproducibility_review.html` | OK | S7 P5 |
| `interactive_s7_qu_archivo_necesito.html` | legado | **no** |

### Prácticas textuales ↔ HTML (muestra crítica)

| Sesión | Prácticas detectadas (`###`/`## Práctica`) | HTML |
| --- | --- | --- |
| S1 | P1, P2 | P1 OK; P2 enlace roto |
| S2 | P1, P2 | HTML existen, **sin iframe/enlace** |
| S3 | P1–P5 | sin HTML |
| S4 | 2 (nombres irregulares) | sin HTML |
| S5 | 0 con ese patrón | sin HTML |
| S6 | P1–P7 | sin HTML |
| S7 | P1–P5 | P1, P3–P5; P2 solo matriz en MD |
| S8–S34 | varias por sesión | sin HTML interactivo en `html/` |
| Mini S14–S17 | 0 con ese patrón | — |

### Conteo aproximado de encabezados `Práctica` por archivo

| Archivo | N |
| --- | --- |
| `u1-s1-documentar-markdown-fases.md` | 2 |
| `u1-s2-organizar-fair-ia.md` | 2 |
| `u2-s3-shell-acceso-remoto.md` | 5 |
| `u2-s4-sistema-archivos-v3.md` | 2 |
| `u2-s5-archivos-permisos-procesos-v2.md` | 0 |
| `u2-s6-consolidacion-entorno-unix.md` | 7 |
| `u3-s7-secuencias-formatos-genbank.md` | 5 |
| `u3-s8-bases-datos-descarga-integridad.md` | 5 |
| `u3-s9-inspeccion-transferencia-verificable.md` | 5 |
| `u4-s10` … `u4-s23` | 5–7 según sesión |
| `u5-s24` … `u5-s29` | 5–7 según sesión |
| `u6-s30` … `u6-s34` | 6–7 según sesión |
| minis `s14`–`s17`, `mini-proyecto-dictamen-….md` | 0 |

---

## 2. Inconsistencias

1. **Enlace roto (alto impacto):** en S1 P2 se referencia `html/u1-s2-p2-protocol_builder.html`, pero el archivo real es `html/u1-s1-p2-protocol_builder.html`. Además `u1-s2-p2-*` ya es *IA bajo la lupa*.
2. **HTML huérfanos (no borrarlos):** Data Steward Lab, IA bajo la lupa, `interactive_s7_qu_archivo_necesito.html`.
3. **Hueco S7 p2:** no hay `u3-s7-p2-*.html` (P2 es textual); la numeración HTML salta p1→p3.
4. **Nombres de sesión con versión:** `u2-s4-…-v3.md`, `u2-s5-…-v2.md` rompen el patrón limpio `uN-sNN-tema.md`.
5. **Mini-proyectos fuera de `uN-sNN`:** `s14-s15-…`, `s16-…`, `s17-…`, `mini-proyecto-dictamen-….md`.
6. **Encabezados de práctica no uniformes:** `### Práctica N`, `## Práctica N`, `## Práctica S4`, `### Práctica de rutas`; S5 no usa el patrón; minis tampoco.
7. **Doble fuente implícita:** el prompt de auditoría declara `curso-quarto/` como oficial, pero sigue existiendo `scripts/sync-from-contenidos.py` (riesgo de sobrescritura / divergencia).
8. **Objetivo skill:** hoy no hay manifiesto sesión→prácticas→HTML; hay que parsear Markdown + listar `html/` a mano.

---

## 3. Estructura futura mínima (propuesta, sin ejecutar)

### Opción A (mínima, bajo riesgo)

Mantener raíz plana y añadir un índice machine-readable:

```
curso-quarto/
  _manifest/
    sessions.yml   # id, file, prev, next, practices[], html[], images[]
  html/
  images/
  ejemplos/
  uN-sNN-….md
```

### Opción B (más clara para humanos/skill)

```
curso-quarto/sesiones/u3/s07/
  sesion.md
  practicas/p01-….md   # o anclas en sesion.md
  html/u3-s7-p1-….html
```

**Recomendación:** A primero (manifest + arreglar enlaces/nombres); B solo si se acepta mover muchos paths en Quarto.

---

## 4. Convención uniforme de nombres

| Tipo | Patrón |
| --- | --- |
| Sesión | `u{U}-s{SS}-{slug}.md` (SS con 2 dígitos: `s01`…`s34`; sin `-vN`) |
| Intro unidad | `u{U}-{slug}.md` |
| Mini | `u4-s14-…`, `u4-s15-…` (o bloque `u4-s14-s15-…` documentado) |
| HTML | `u{U}-s{SS}-p{P}-{slug}.html` |
| Figura | `figura-u{U}-s{SS}-{slug}.png` (ya casi así) |
| Práctica en MD | siempre `### Práctica {N} — …` |

---

## 5. Tabla de migración (plan, no ejecutado)

| Ruta actual | Ruta propuesta | Motivo | Riesgo |
| --- | --- | --- | --- |
| (fix) S1 → `html/u1-s2-p2-protocol_builder.html` | → `html/u1-s1-p2-protocol_builder.html` | Enlace roto / colisión con IA lupa | **Alto** (sitio roto hoy) |
| `html/u1-s2-p1-data_steward_lab.html` | mismo + enlace en S2 P1 | HTML listo, no integrado | Medio |
| `html/u1-s2-p2-ia_bajo_la_lupa.html` | mismo + enlace en S2 P2 | HTML listo, no integrado | Medio |
| `html/interactive_s7_qu_archivo_necesito.html` | `html/u3-s7-p2-que_archivo_necesito.html` **o** `html/_legacy/…` | Legado; decidir si es P2 o archivo muerto | Medio |
| `u2-s4-sistema-archivos-v3.md` | `u2-s4-sistema-archivos.md` | Quitar sufijo de versión | Medio (sidebar + URLs) |
| `u2-s5-archivos-permisos-procesos-v2.md` | `u2-s5-archivos-permisos-procesos.md` | Idem | Medio |
| `s14-s15-mini-proyecto-investigacion-I.md` | `u4-s14-s15-mini-proyecto-investigacion-I.md` (o dos archivos) | Alinear nomenclatura | Alto (bookmarks/URLs) |
| `s16-…`, `s17-…`, `mini-proyecto-dictamen-….md` | `u4-s16-…`, `u4-s17-…`, `u4-sXX-dictamen-….md` | Idem | Alto |
| (nuevo) `_manifest/sessions.yml` | crear | Habilitar skill Gemini Canvas | Bajo |
| `scripts/sync-from-contenidos.py` | documentar “solo legacy” o retirar del flujo | Conflicto con fuente oficial | Medio |

---

## 6. Referencias a actualizar (si se migra)

- **Ya rotas (arreglar aunque no se reorganice):**  
  `u1-s1-documentar-markdown-fases.md` — Protocol Builder (`u1-s2-p2-protocol_builder` → `u1-s1-p2-protocol_builder`).
- **Añadir (integración, no rename):** iframes/enlaces en `u1-s2-organizar-fair-ia.md` hacia Data Steward e IA bajo la lupa.
- **Si se renombran sesiones:** `_quarto.yml` (todos los `href`), links internos entre lecciones, `recursos.qmd`, README.
- **Si se renombra HTML legado S7:** menciones futuras + posible uso en prompts-ia.
- **Publicación:** Quarto cambia slugs de URL en GitHub Pages al renombrar `.md`.

**Dependencias de ruta frágiles:** todos los `src="html/…"` e `images/…` son relativos a la sesión en la raíz; si se mueven sesiones a subcarpetas, hay que reescribir a `../../html/…` o usar paths absolutos del sitio.

---

## 7. Clasificación de riesgo (movimientos)

| Acción | Riesgo |
| --- | --- |
| Corregir enlace Protocol Builder | Bajo (fix) / impacto alto si no se hace |
| Enlazar HTML S2 existentes | Bajo–medio |
| Renombrar `interactive_s7_…` | Medio |
| Quitar `-v2`/`-v3` de nombres de sesión | Medio |
| Renombrar minis `s14`… a `u4-s…` | Alto |
| Reorganizar a `sesiones/uN/sNN/` | Alto |
| Añadir `_manifest/sessions.yml` | Bajo |

---

## Cumplimiento vs. lo que pide el prompt

| Requisito del prompt | Estado en `curso-quarto/` |
| --- | --- |
| No reorganizar aún | Cumplido (solo auditoría) |
| Identificar sesiones/nomenclatura | Hecho; patrón mayoritario OK, excepciones claras |
| Prácticas por sesión | Parcial: parseable en U3–U6; irregular en U2/minis |
| HTML y relación sesión/práctica | Parcial; S7 bien; S1 P2 roto; S2 desconectado |
| Imágenes/recursos | Convención de figuras sólida; `ejemplos/` activo |
| Enlaces relativos | Funcionan en plano; frágiles ante move |
| Huérfanos / legado | Identificados, no eliminados |
| Mapa + inconsistencias + migración + riesgos | Este informe |

---

## Siguiente paso lógico (cuando se autorice)

1. Arreglar el enlace de Protocol Builder.
2. Enlazar los dos HTML de S2.
3. Decidir destino de `interactive_s7_qu_archivo_necesito.html`.
4. Crear el manifiesto `_manifest/sessions.yml` — sin mover carpetas todavía.
