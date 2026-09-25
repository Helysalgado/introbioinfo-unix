# Proyecto E. coli K-12

## Descripción

Este proyecto utiliza datos genómicos de *Escherichia coli* K-12 MG1655
para desarrollar un flujo de trabajo bioinformático reproducible en un
entorno Unix.

Durante las primeras unidades se prepara, organiza y verifica el entorno
de trabajo antes de comenzar el análisis biológico.

## Pregunta biológica

**¿Cuántos genes tiene el genoma de *E. coli* K-12 y cómo se distribuyen
en el cromosoma?**

### Subpreguntas

1.  ¿Cuál es el tamaño del genoma?
2.  ¿Cuántos genes están anotados?
3.  ¿Cuántos genes se encuentran en la hebra `+` y cuántos en la hebra
    `-`?

## Datos

-   **Archivo principal:** `genes_ecoli.gff`
-   **Organismo:** *Escherichia coli* K-12 MG1655
-   **Referencia:** `NC_000913.3`

Los datos originales se conservan sin modificaciones en:

`data/source/`

La información sobre procedencia, versión y contexto de los datos se
encuentra en:

`data/source/genes_ecoli-metadatos.md`

## Estructura del proyecto

``` text
proyecto-ecoli/
├── README.md
├── data/
│   ├── source/
│   │   ├── genes_ecoli.gff
│   │   └── genes_ecoli-metadatos.md
│   └── processed/
├── doc/
│   ├── protocolo.md
│   ├── bitacora-ia.md
│   └── checksums-u2.txt
├── results/
└── src/
```

## Organización

-   `data/source/` --- datos originales; no deben modificarse.
-   `data/processed/` --- datos derivados o transformados.
-   `src/` --- scripts utilizados en el análisis.
-   `results/` --- resultados regenerables.
-   `doc/` --- protocolo, bitácoras y documentación del proyecto.

## Integridad de los datos

La integridad de los archivos fuente se verifica mediante SHA-256.

Los checksums registrados para futuras verificaciones se encuentran en:

`doc/checksums-u2.txt`

## Documentación

El procedimiento, las decisiones y las evidencias del proyecto se
documentan en:

`doc/protocolo.md`

Las interacciones relevantes con herramientas de IA se registran en:

`doc/bitacora-ia.md`

## Estado del proyecto

**Unidad 2 finalizada: preparación del entorno Unix.**

Hasta este punto:

-   se organizaron los archivos del proyecto;
-   se conservaron los datos fuente;
-   se verificó su integridad;
-   se revisaron rutas y permisos;
-   se documentó el procedimiento;
-   se realizó una revisión del protocolo.

El análisis biológico todavía no ha comenzado.

## Siguiente etapa

Utilizar las herramientas de Unix para explorar y analizar
`genes_ecoli.gff` con el objetivo de responder las preguntas biológicas
del proyecto.
