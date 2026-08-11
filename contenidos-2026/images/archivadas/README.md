# Figuras archivadas

Figuras que **ya no se usan en el material del alumno** pero se conservan porque documentan una
decisión de diseño o porque podrían recuperarse. No se borran: si alguna vuelve a hacer falta, se
corrige y se devuelve a `images/` con el nombre canónico `figura-u<N>-s<NN>-<slug>`.

Ninguna figura de esta carpeta debe referenciarse desde una sesión. La única excepción vigente es
`docente/u2-s6-cluster-hpc.md`, que es un borrador no publicable.

## Superadas por una versión corregida

Ambas situaban el proyecto del estudiante en `/export/space3/users/$USER`. Se dibujaron cuando el
curso preveía trabajar en el espacio institucional desde la Unidad 2. Al reubicar el trabajo con
cluster en **S29** y fijar el proyecto en `~/proyecto/`, dejaron de ser correctas y se rehicieron.

| Archivada | Sustituida por | Qué cambió |
| --- | --- | --- |
| `figura-u2-arbol-sistema-archivos` (png + svg) | `figura-u2-s04-home-espacio-institucional` | La nueva separa dos ramas desde la raíz —`home/` «AHORA · S4» y `export/space3/` «MÁS ADELANTE»— en lugar de colgar el proyecto de `/export` y etiquetar ese espacio como `(~)`, lo que equiparaba dos directorios que S4 enseña a distinguir |
| `figura-u2-rutas-absolutas-relativas` (png + svg) | `figura-u2-s04-rutas-home` | Misma composición, con `/home/usuario/…` en lugar de `/export/space3/users/$USER/…` |

## Del borrador de HPC reubicado a S29

El contenido de cluster y SGE se trasladó de la Unidad 2 a **S29** (`u5-s29-cluster-hpc-sge.md`),
porque en U2 era demasiado pronto para hablar de cómputo distribuido. S29 tiene cinco figuras
propias. Estas tres pertenecen al borrador previo, `docente/u2-s6-cluster-hpc.md`, que **no se
publica**:

- `figura-u2-pc-servidor-cluster` (png + svg) — tres niveles de cómputo en escala creciente.
- `figura-u2-arquitectura-hpc` (png + svg) — nodo de acceso, sistema de colas, nodos de cómputo y
  almacenamiento compartido.
- `figura-u2-ciclo-sge` (png + svg) — ciclo de vida de un trabajo: `qsub`, cola `qw`, ejecución `r`,
  salida y error.

**Pendiente de decidir:** si alguna mejora a su equivalente en S29, se corrige el nombre a
`figura-u5-s29-<slug>` y se recupera; si no, se quedan aquí.
