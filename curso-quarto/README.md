# Sitio Quarto del curso

Proyecto **Quarto Website** para publicar el material de `contenidos-2026/`.

Estado: **U1–U6 + transversal**, callouts Quarto y workflow de Pages listos.
Pendiente al publicar: configurar `origin`, `site-url` / `repo-url` en `_quarto.yml`.

## Vista previa local

```bash
cd curso-quarto
quarto preview
```

## Si aparece `ERROR: BadResource` (SassCache / Deno KV)

El repo vive en **Google Drive** (`CloudStorage`). La caché Deno KV de Quarto se corrompe o bloquea ahí.

Mitigación ya aplicada: `.quarto` es un **enlace simbólico** a

`~/Library/Caches/curso-quarto-quarto`

(disco local, fuera de Drive).

Si el error vuelve:

1. Cierra el `quarto preview` (Ctrl+C).
2. Borra la caché local y recrea el enlace:

```bash
cd curso-quarto
rm -rf .quarto
rm -rf ~/Library/Caches/curso-quarto-quarto
mkdir -p ~/Library/Caches/curso-quarto-quarto
ln -sfn ~/Library/Caches/curso-quarto-quarto .quarto
quarto preview
```

No abras dos `quarto preview` a la vez sobre el mismo proyecto.

## Contenido

- `_quarto.yml` — Website completo (navbar + sidebar por unidad)
- `index.qmd`, `programa.qmd`, `recursos.qmd` — marco del sitio
- `u*.md`, `s*.md`, `mini-proyecto*.md` — lecciones
- `images/` — figuras PNG
- `ejemplos/` — datos y plantillas
- `referencias/bioinformatics-data-skills.pdf` — Buffalo

La fuente canónica del contenido sigue siendo `../contenidos-2026/`. Este directorio es la capa de publicación.

Ver: [`../planificacion-quarto/02-plan-implementacion-sitio-quarto.md`](../planificacion-quarto/02-plan-implementacion-sitio-quarto.md).
