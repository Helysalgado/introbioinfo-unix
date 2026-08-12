# Despliegue en GitHub Pages

Publicar el sitio Quarto de [`curso-quarto/`](../curso-quarto/) como HTML estático.

## Modelo elegido

| Pieza | Valor |
| --- | --- |
| Fuente | rama `main`, carpeta `curso-quarto/` |
| Build | GitHub Action con Quarto |
| Publicación | rama `gh-pages` (solo el contenido de `_site/`) |
| URL típica | `https://<usuario-o-org>.github.io/<repo>/` |

No se commitea `_site/` en `main`.

## Estado del remoto

Si el repo **aún no tiene** `origin`, créalo en GitHub y enlázalo:

```bash
git remote add origin git@github.com:ORG/REPO.git
git push -u origin main
```

Luego activa Pages:

1. GitHub → **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `gh-pages` / `/ (root)`

El workflow crea `gh-pages` en el primer push exitoso a `main` (o al lanzarlo a mano).

## Workflow

Archivo: [`.github/workflows/publish-quarto.yml`](../.github/workflows/publish-quarto.yml)

- Disparo: push a `main` que toque `curso-quarto/**`, o `workflow_dispatch`
- Pasos: checkout → instalar Quarto → `quarto render` en `curso-quarto/` → publicar `_site/` a `gh-pages` con `peaceiris/actions-gh-pages`

## Probar en local antes del deploy

```bash
cd curso-quarto
# caché fuera de Google Drive (ver README del sitio)
quarto render
quarto preview   # opcional
```

## Tras el primer deploy

Completa en `curso-quarto/_quarto.yml`:

```yaml
website:
  site-url: https://ORG.github.io/REPO/
  repo-url: https://github.com/ORG/REPO
```

Vuelve a hacer push para que los enlaces canónicos y “Edit” apunten bien.

## Si falla el Action

| Síntoma | Qué mirar |
| --- | --- |
| Permission denied al publicar `gh-pages` | Settings → Actions → General → Workflow permissions: **Read and write** |
| Quarto no encontrado | Versión del Action `quarto-dev/quarto-actions/setup` |
| Rutas rotas a `images/` / `ejemplos/` | Que el render se ejecute con `working-directory: curso-quarto` |

## Fuera de este paso

- Custom domain
- PDF del curso
- Publicar desde `docs/` en `main` (alternativa más simple, pero ensucia el historial con HTML)
