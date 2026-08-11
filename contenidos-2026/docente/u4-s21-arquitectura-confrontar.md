# Arquitectura de la Sesión S21 — Confrontar: validar un resultado con una fuente independiente

> **Documento docente.** No forma parte del material del estudiante. Expande la entrada de S21 de
> `u4-arquitectura.md` y fija las decisiones previas a redactar la sesión.

## Identidad de la sesión

**Competencia principal.** Confrontar los resultados obtenidos de fuentes biológicas distintas para
evaluar la consistencia de la evidencia e interpretar biológicamente las discrepancias.

**Verbo del ciclo de la evidencia.** `CONFRONTAR` — cuarto paso del bloque B (ver §2.b de
`u4-arquitectura.md`).

## Cambio conceptual

Hasta S20 el estudiante construyó un flujo reproducible:

```text
S18 Seleccionar → S19 Identificar → S20 Normalizar → (comparar dentro del mismo origen)
```

Pero queda una pregunta abierta:

> **¿Puedo confiar en mi conclusión?**

Todavía no. Todo el análisis proviene del **mismo origen de datos**: el FASTA y el GFF3 se
descargaron juntos, del mismo ensamblado y del mismo productor. La comparación de S19 y S20 fue una
comprobación de **coherencia interna**, no una validación.

En S21 el protagonista no es una herramienta ni un recurso: es la **validación mediante una segunda
fuente de evidencia**.

> **Precisión importante.** No se afirma que la conclusión anterior fuera inválida, sino que estaba
> **sin contrastar**. Confrontar no "corrige" el resultado propio: mide su robustez y obliga a
> explicar cualquier diferencia.

## Propósito

Demostrar que el flujo construido en S18–S20 es reutilizable sobre datos que no nacieron con él, y
evaluar críticamente las discrepancias que aparezcan.

## Pregunta biológica central

> **¿Mi inventario del genoma sigue sosteniéndose cuando lo confronto con una fuente independiente?**

### Preguntas secundarias

1. ¿Dos fuentes independientes describen el mismo conjunto de genes?
2. Si difieren, ¿la causa está en el criterio de anotación, en la versión del ensamblado, en los
   filtros aplicados o en mi estrategia de conteo?
3. ¿Qué discrepancias son un problema y cuáles son una característica esperable de cada recurso?
4. ¿Qué evidencia adicional haría falta para decidir entre dos interpretaciones?

## La fuente independiente

> **DECISIÓN TÉCNICA — BioMart no sirve para este curso.** El Plan operativo asigna a S21 *"Ensembl y
> BioMart"*, pero **Ensembl Bacteria no ofrece BioMart**: desde la expansión de 2013 a decenas de
> miles de genomas bacterianos, el mart no escala y el propio recurso lo declara no soportado,
> remitiendo a su API. Como todo el curso trabaja con bacterias —*E. coli* K-12 en clase y doce
> ensamblados bacterianos en el mini proyecto—, la sesión no puede depender de BioMart. Ver
> discrepancia **D8** en `u4-arquitectura.md`.

Fuentes viables, en orden de preferencia:

| Fuente | Qué aporta | Por qué es independiente | Riesgos |
| --- | --- | --- | --- |
| **UniProt (proteoma del organismo, descarga TSV)** | Tabla con un registro por proteína, con *ordered locus name* (el `locus_tag`), nombre de gen y longitud | Curación propia, criterios propios, versión propia; no deriva del GFF3 del estudiante | Cubre **proteínas**, no todos los genes: la diferencia con el GFF3 es real y es justamente el material interpretativo |
| **Anotación GenBank (`GCA_…`) del mismo ensamblado** | Mismo DNA, anotación del autor del depósito en vez de la de PGAP | Mismo genoma, **procedimiento de anotación distinto** | Comparte ensamblado: aísla la variable "criterio de anotación", que es su virtud didáctica |
| **Ensembl Bacteria vía FTP o REST** | Tabla equivalente | Recurso distinto | Requiere navegación menos predecible; queda como opción avanzada |

Se elige **UniProt como fuente principal** y **GCA como alternativa** cuando el organismo asignado no
tenga proteoma de referencia. Ambas están garantizadas para los doce ensamblados del mini proyecto.

> **NOTA.** La sesión debe funcionar igual con cualquiera de las tres: el objeto de estudio es el
> contraste, no el recurso. La descarga se documenta con la ficha de procedencia de la Unidad 3, sin
> convertir la sesión en un tutorial del sitio.

## Herramientas

**Ninguna herramienta Unix nueva.** Se reutiliza todo el repertorio:

```text
head · tail · wc · cat -A · grep + regex · cut (-f y -d) · sort · sort -u · uniq -c
tr · sed · comm · pipes · redirecciones
```

`comm` vuelve a ser el instrumento del contraste, como en S19 y S20. La novedad es intelectual: dos
fuentes que no comparten origen.

## Limitación que resuelve

> Un resultado reproducible todavía no es una conclusión científica.

Una conclusión sostenida por una sola fuente conserva una incertidumbre que ningún control interno
puede eliminar. La confrontación aporta la evidencia que permite empezar a validarla.

## Prácticas

Seis prácticas. La progresión repite deliberadamente el ciclo de S18–S20 sobre datos nuevos, porque
**la reutilización del flujo es en sí misma el resultado**.

| # | Momento | Qué hace | Producto |
| --- | --- | --- | --- |
| 1 | Antes de clase | Registrar la procedencia de la nueva fuente: organismo, ensamblado, versión, fecha, recurso y criterio de inclusión | Ficha de procedencia al estilo U3 |
| 2 | Antes de clase | Auditar la tabla descargada: delimitadores, encabezado, faltantes, cardinalidad | Auditoría reproducible |
| 3 | Taller | Recuperar de la nueva tabla **la misma evidencia biológica** obtenida del GFF3 | Lista de identificadores de la fuente externa |
| 4 | Taller | Poner a prueba la política de normalización de S20 sobre esta fuente | Política revisada, con sus reglas nuevas justificadas |
| 5 | Taller | Confrontar ambas listas y clasificar cada zona del resultado | Tabla de contraste |
| 6 | Después | Formular una hipótesis por cada discrepancia y decir qué evidencia la resolvería | Interpretación argumentada |

> **CORRECCIÓN sobre la propuesta inicial — Práctica 3.** No puede pedirse "extraer exactamente igual,
> sin cambiar la estrategia": la tabla externa no es un GFF3, no tiene una columna 3 con el tipo ni un
> campo de atributos. Lo que se conserva es la **definición del objeto biológico** —qué cuenta como
> gen— y la **secuencia de operaciones**; los comandos concretos cambian, y comprobar que la
> definición sobrevive al cambio de formato es precisamente lo que demuestra que el flujo es general.

> **CORRECCIÓN sobre la propuesta inicial — Práctica 4.** No puede pedirse "aplicar la política de S20
> sin construir una nueva": S20 cierra afirmando que **las reglas no se transfieren a otra fuente sin
> repetir la auditoría**, y contradecirlo aquí desmontaría la lección anterior. La formulación correcta
> es: la política de S20 se toma como **hipótesis de partida**, se somete a la auditoría de la
> Práctica 2 y se **amplía** con las reglas que la nueva fuente exija, cada una con su justificación.
> Lo que no se hace es empezar de cero.

## Figuras

Cuatro figuras originales, en el estilo SVG del curso (paleta y tipografía de U4), con alt text y pie
numerado. No se reutilizan las de S20.

| Figura | Qué muestra | Por qué |
| --- | --- | --- |
| 21.1 | Una conclusión sostenida por una fuente frente a una conclusión confrontada con dos | Hace visible el cambio epistemológico, que es el eje de la sesión |
| 21.2 | Los dos caminos hasta un inventario: FASTA + GFF3 → inventario propio; recurso externo → inventario independiente; y su punto de encuentro | Muestra que lo que se compara son **dos productos**, no dos archivos |
| 21.3 | Las causas posibles de una discrepancia: versión del ensamblado, criterio de anotación, filtros, alcance del recurso, estrategia de conteo | Presenta **explicaciones alternativas**, no errores |
| 21.4 | El ciclo completo con S21 resuelto y la pregunta que queda abierta | Puente hacia S22 |

## Actualización del protocolo

Sección **Contraste con una fuente independiente**, con la estructura habitual: pregunta, hipótesis,
procedencia de la segunda fuente, estrategia de recuperación, política reutilizada y ampliada,
comparación, tabla de discrepancias con una hipótesis por fila, evidencia necesaria para resolverla,
interpretación biológica y limitaciones.

## Limitación con la que cierra (motor de S22)

Las discrepancias que sobrevivan compartirán una característica: **no se resuelven comparando
listas**. Exigirán longitudes, sumas, promedios, densidades y condiciones sobre varias columnas a la
vez. Ninguna herramienta vista lo permite. La limitación debe aparecer por sí sola, sin nombrar la
herramienta de S22.

## Narrativa de la Unidad 4

```text
S18 SELECCIONAR  →  S19 IDENTIFICAR  →  S20 NORMALIZAR  →  S21 CONFRONTAR  →  S22 CUANTIFICAR  →  S23 INTEGRAR
```

## Idea central

Cada sesión introduce una **operación intelectual**, no una herramienta. S21 marca el paso de
*obtener un resultado* a *empezar a construir una conclusión científica*.
