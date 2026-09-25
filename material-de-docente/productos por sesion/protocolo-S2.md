# Protocolo del proyecto — E. coli K-12

> **Estado al cierre de S2:** se conserva la pregunta y estrategia de S1 y se incorpora la descripción del dato, su organización y las decisiones FAIR relevantes.

## Introducción

Este proyecto utilizará información genómica de *Escherichia coli* K-12 para practicar un flujo de trabajo bioinformático reproducible. El objetivo no es comenzar por una herramienta, sino definir primero la pregunta biológica, dividirla en subpreguntas y establecer qué evidencia permitiría responderlas.

El protocolo es un documento vivo: se completará durante el curso conforme se incorporen los datos, los comandos, las verificaciones, los resultados y su interpretación.

## Pregunta central

**¿Cuántos genes tiene el genoma de *E. coli* K-12 y cómo se distribuyen en el cromosoma?**

## Subpreguntas

1. ¿Cuál es el tamaño del genoma de *E. coli* K-12?
2. ¿Cuántos genes están anotados en el genoma?
3. ¿Cuántos genes se encuentran en la hebra `+` y cuántos en la hebra `-`?

## Datos

### Archivo principal

- **Archivo:** `genes_ecoli.gff`
- **Organismo:** *Escherichia coli* K-12 MG1655
- **Referencia:** `NC_000913.3`
- **Formato:** GFF
- **Función en el proyecto:** archivo de anotación genómica utilizado como dato fuente.
- **Metadatos asociados:** `genes_ecoli-metadatos.md`
- **Integridad:** el campo de checksum queda reservado hasta calcularlo en una sesión posterior.

La ficha `genes_ecoli-metadatos.md` registra la procedencia y el contexto del dato. La información que no esté comprobada debe quedar marcada como pendiente, no inferirse ni inventarse.

### Política de organización de datos

- Los datos originales se conservarán sin modificaciones en `data/source/`.
- Los archivos transformados o derivados se guardarán en `data/processed/`.
- Los resultados regenerables se almacenarán en `results/`.
- Los scripts se almacenarán en `src/`.
- La documentación del proyecto se almacenará en `doc/`.

Estas decisiones contribuyen a la localización, trazabilidad y reutilización del trabajo; FAIR se aplica de forma progresiva y no se considera resuelto únicamente por crear carpetas o una ficha de metadatos.

## Estrategia

| Subpregunta | Evidencia necesaria | Datos | Operación conceptual | Validación prevista |
|---|---|---|---|---|
| ¿Cuál es el tamaño del genoma? | Longitud total del genoma | `genes_ecoli.gff` / registro asociado | Localizar la longitud declarada | Contrastar con el registro de referencia |
| ¿Cuántos genes hay? | Número de registros `gene` | `genes_ecoli.gff` | Filtrar conceptualmente por tipo `gene` y contar | Comparar con referencia externa |
| ¿Cuántos genes hay por hebra? | Conteos `+` y `-` para genes | `genes_ecoli.gff` | Agrupar conceptualmente por hebra y contar | `+` + `-` = total de genes |

## Comandos

_Pendiente. En S2 todavía se priorizan organización, metadatos y estrategia._

## Resultados

_Pendiente._

## Validación

- Se revisó que la estrategia responda a las subpreguntas antes de elegir comandos.
- Se distinguió entre información conocida, información pendiente e información que no debe inventarse.

## Discusión

_Pendiente._

## Conclusiones

_Pendiente._

## Actualizaciones

- **S1:** pregunta, subpreguntas y estrategia inicial.
- **S2:** se añadió la descripción del dato, la referencia `NC_000913.3`, la ficha de metadatos y la política de separación entre originales, derivados, código, resultados y documentación.
