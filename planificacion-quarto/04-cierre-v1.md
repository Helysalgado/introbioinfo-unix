# Cierre v1 — Sitio Quarto Website

**Fecha:** 2026-08-11  
**Sitio:** https://helysalgado.github.io/introbioinfo-unix/  
**Repo:** https://github.com/Helysalgado/introbioinfo-unix  

## Pasos del plan 02 (estado)

| Paso | Descripción | Estado |
| --- | --- | --- |
| A | Esqueleto `curso-quarto/` | Hecho |
| B | Piloto U1 | Hecho |
| C | U2–U6 + transversal + assets | Hecho |
| D | Callouts Quarto | Hecho (~529) |
| E | GitHub Pages + Action | Hecho |

## Criterios de aceptación v1

- [x] Navegación Curso → U1–U6 → sesiones
- [x] Portadas y sesiones con H1, prácticas, tablas y código
- [x] Figuras y `ejemplos/` resuelven
- [x] `<details>` de retroalimentación
- [x] `docente/` excluido del sitio
- [x] Inicio explica aula invertida
- [x] HTTPS en GitHub Pages
- [x] Un solo proyecto Website (sin Book/slides)

## Operación cotidiana

1. Editar la fuente en `contenidos-2026/` (sigue en blockquotes editoriales).
2. Sincronizar al sitio:

```bash
python3 curso-quarto/scripts/sync-from-contenidos.py
cd curso-quarto && quarto preview
```

3. Commit + push a `main` → Action publica `gh-pages`.

## Ajustes de presentación ya incluidos

- Callouts nativos; notas docentes eliminadas en la copia del sitio.
- Tablas: anchos de Pandoc anulados; agendas `Tiempo|Actividad` con clase `.tabla-agenda`.
- Caché Quarto fuera de Google Drive (ver `curso-quarto/README.md`).

## Fuera de v1 (próximas oleadas, si se piden)

- PDF/EPUB del curso  
- RevealJS por taller  
- Reorganizar `contenidos-2026/` en subcarpetas  
- Rediseño visual elaborado  
