# Protocolo del proyecto — E. coli K-12

> **Estado al cierre de S1:** protocolo iniciado. En esta sesión se documenta el razonamiento del problema; todavía no se ejecuta el análisis.

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

Se utilizará un archivo de anotación genómica en formato GFF de *E. coli* K-12.

**Estado en S1:** la procedencia, versión, identificador, fecha de obtención e integridad del archivo se documentarán en las siguientes sesiones. No se inventará información faltante.

## Estrategia

| Subpregunta | Evidencia necesaria | Dato esperado | Operación conceptual | Validación prevista |
|---|---|---|---|---|
| ¿Cuál es el tamaño del genoma? | Longitud total del genoma en pares de bases | Encabezado/registro asociado al genoma | Identificar la longitud declarada | Contrastar con el registro de referencia |
| ¿Cuántos genes hay? | Número de registros de tipo `gene` | Columna de tipo de feature del GFF | Identificar registros `gene` y contarlos | Comparar con una fuente de referencia |
| ¿Cuántos genes hay por hebra? | Conteo de genes con `+` y `-` | Columna de hebra del GFF | Separar genes por hebra y contar | La suma `+` + `-` debe coincidir con el total de genes |

## Comandos

_Pendiente. Los comandos se documentarán cuando la estrategia se traduzca a operaciones ejecutables._

## Resultados

_Pendiente._

## Validación

_Pendiente._

## Discusión

_Pendiente._

## Conclusiones

_Pendiente._

## Actualizaciones

- **S1:** se definieron la pregunta central, las subpreguntas y la estrategia inicial. Se creó la estructura del protocolo como documento vivo.
