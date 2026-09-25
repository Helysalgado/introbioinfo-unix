# Protocolo de análisis bioinformático

**Nombre:** Nombre del estudiante  
**Fecha:** 2 de septiembre de 2026  
**Curso:** Introducción a la Bioinformática  

---

## 1. Introducción

El genoma de *Escherichia coli* K-12 ha sido ampliamente estudiado y su secuencia y anotación se encuentran disponibles en bases de datos públicas.

En este análisis se utilizarán datos de su genoma para explorar algunas de sus características generales, como su tamaño, número de genes y distribución de genes entre las dos cadenas de DNA.

---

## 2. Pregunta central

**¿Cuántos genes tiene el genoma de *Escherichia coli* K-12 y cómo se distribuyen en el cromosoma?**

---

## 3. Subpreguntas

1. ¿Cuál es el tamaño del genoma de *E. coli* K-12?
2. ¿Cuántos genes contiene?
3. ¿Cuántos genes se encuentran en la cadena `+` y cuántos en la cadena `-`?

---

## 4. Datos

Para responder las preguntas será necesario trabajar con información de la secuencia y de la anotación del genoma.

| Dato | Formato | Información que contiene | Procedencia |
|---|---|---|---|
| Secuencia del genoma | FASTA | Secuencia de DNA | NCBI |
| Anotación del genoma | GFF | Genes y otros elementos anotados | NCBI |

### Procedencia de los datos

**Organismo:** *Escherichia coli* K-12  
**Fuente:** NCBI  
**Fecha de descarga:** pendiente  
**Versión/accesión:** pendiente  
**URL:** pendiente  
**Integridad/checksum:** pendiente  

> Estos datos deberán completarse cuando se descarguen los archivos.

---

## 5. Estrategia

Antes de elegir comandos, se define qué evidencia necesitamos y qué operación habría que realizar sobre los datos.

| Subpregunta | Evidencia necesaria | Datos | Operación conceptual | Herramienta posible | Validación | Interpretación |
|---|---|---|---|---|---|---|
| ¿Cuál es el tamaño del genoma? | Longitud total en pares de bases | GFF / FASTA | Obtener la longitud del genoma | Visualización de texto | Comparar con el registro de NCBI | Determinar el tamaño del genoma |
| ¿Cuántos genes hay? | Número de elementos anotados como `gene` | GFF | Seleccionar los genes y contarlos | Filtro + conteo | Comparar con NCBI | Estimar la cantidad y densidad de genes |
| ¿Cómo se distribuyen entre las cadenas? | Número de genes `+` y `-` | GFF | Separar los genes por cadena y contarlos | Filtro + conteo | La suma de `+` y `-` debe coincidir con el total | Evaluar la distribución entre ambas cadenas |

---

## 6. Comandos

*Esta sección se completará cuando aprendamos las herramientas necesarias para ejecutar el análisis.*

```bash
# Los comandos se agregarán posteriormente.
```

---

## 7. Resultados

*Pendiente. Aquí se registrará la evidencia obtenida durante el análisis.*

---

## 8. Validación

*Pendiente. Aquí se documentará cómo se comprobó que los resultados obtenidos son correctos y que permiten responder las subpreguntas.*

---

## 9. Discusión

*Pendiente. Aquí se interpretará el significado biológico de los resultados y se discutirán sus limitaciones.*

---

## 10. Conclusiones

### Conclusión provisional

Todavía no es posible responder cuántos genes tiene el genoma ni cómo se distribuyen, porque el análisis de los datos aún no se ha realizado.

Sin embargo, se ha definido qué evidencia será necesaria para responder la pregunta y qué operaciones deberán realizarse.

### Limitaciones actuales

- Los datos todavía no han sido analizados.
- Falta registrar la versión exacta de los archivos utilizados.
- No se han ejecutado ni verificado comandos.
- Los resultados deberán validarse antes de establecer una conclusión biológica definitiva.

---

## Bitácora de cambios

| Fecha | Cambio realizado |
|---|---|
| 2026-09-02 | Creación inicial del protocolo |