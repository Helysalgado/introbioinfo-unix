Estamos trabajando en el proyecto **Introducción a la Bioinformática — LCG UNAM 2026**.

La versión actual y oficial del curso está en:

`curso-quarto/`

La carpeta `contenidos-2026/` contiene material anterior y NO debe considerarse la fuente oficial.

Quiero preparar `curso-quarto/` para posteriormente crear una skill que analice las prácticas educativas y genere prompts para Gemini Canvas.

## IMPORTANTE

En esta primera fase NO muevas, renombres, borres ni modifiques ningún archivo.

Haz solamente una auditoría de la estructura.

## Necesito que identifiques

1. Las sesiones del curso y su nomenclatura.
2. Las prácticas textuales contenidas o referenciadas por cada sesión.
3. Los HTML interactivos existentes.
4. La relación entre cada HTML y su sesión/práctica correspondiente.
5. Las imágenes y otros recursos utilizados.
6. Los enlaces relativos entre QMD/Markdown, HTML, imágenes, CSS, JavaScript y otros recursos.
7. Archivos antiguos, prototipos o archivos cuya nomenclatura no siga el patrón principal.
8. Archivos aparentemente huérfanos, pero NO los elimines.
9. Cualquier dependencia de rutas que pudiera romperse si reorganizamos carpetas.

## Convención que parece existir

Los HTML recientes utilizan aproximadamente:

`u<unidad>-s<sesion>-p<practica>-<nombre>.html`

Por ejemplo:

`u1-s2-p1-data_steward_lab.html`

`u1-s2-p2-ia_bajo_la_lupa.html`

`u3-s7-p4-gff3_explorer.html`

Sin embargo, existen archivos antiguos como:

`interactive_s7_qu_archivo_necesito.html`

No asumas que un archivo es obsoleto únicamente porque no cumple la convención.

## Objetivo de la reorganización

Quiero que posteriormente resulte sencillo determinar:

**sesión → prácticas textuales → HTML interactivos → imágenes/recursos**

También quiero que una futura skill pueda recibir una sesión y localizar fácilmente:

- sesión anterior;
- sesión actual;
- sesión siguiente;
- prácticas de la sesión actual;
- HTML existentes de esas prácticas;
- recursos relacionados.

## Entregable

Después de inspeccionar el repositorio:

1. Muéstrame un mapa de la estructura actual.
2. Señala inconsistencias.
3. Propón una estructura futura mínima.
4. Propón una convención uniforme de nombres.
5. Genera una tabla de migración:

`ruta actual → ruta propuesta → motivo → riesgo`

6. Identifica todos los enlaces o referencias que habría que actualizar.
7. Clasifica cada movimiento propuesto como riesgo bajo, medio o alto.

NO ejecutes todavía la reorganización.

Quiero revisar primero el plan de migración.