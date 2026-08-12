# S8 — Recuperar: bases de datos, descarga y verificación de integridad

::: {.callout-note title="Aula invertida"}
Antes de clase lee las secciones marcadas como **indispensables** y
realiza el primer intento sin IA: la estrategia de búsqueda de tu conjunto de datos. Durante el
taller navegarás recursos reales de NCBI, corregirás tu estrategia y practicarás con roles
distintos (responsable de laboratorio, curador de datos, revisor de una revista). Después
completarás la Tarea 4 en tu propio proyecto. El primer intento es formativo: importa que muestre
tu razonamiento inicial, aunque contenga errores corregibles.
:::

## Ficha del módulo

| Elemento | Descripción |
| --- | --- |
| **Sesión** | S8, 2 horas |
| **Unidad** | U3. Datos y bases de datos biológicas |
| **Competencia principal** | C. Manejo de datos y bases de datos biológicas |
| **Competencias integradas** | A. Documentación reproducible |
| **Propósito** | Recuperar mediante la interfaz web un conjunto coherente de archivos de un ensamblado real, documentar su procedencia y preparar la evidencia necesaria para verificar su integridad en S9. |
| **Consulta previa del Plan** | Material clásico L4, diapositivas 32–60; este módulo lo sustituye como lectura autocontenida |
| **Lectura indispensable** | Secciones 1–6 y Práctica 1 de este módulo, 60–75 min |
| **Lectura de consulta** | Documentación oficial de NCBI enlazada en cada sección, 15–20 min |
| **Primer intento** | Estrategia de búsqueda (organismo → cepa → ensamblado → versión → registro), 20–25 min |
| **Evidencia** | Estrategia corregida y avance de la Tarea 4 |
| **Tarea numerada** | Tarea 4 — Construcción de un conjunto de datos reproducible |

## Relación con lo que ya sabes

En S7 aprendiste a **interpretar** objetos biológicos y sus representaciones: FASTA, GFF3 y GenBank.
Supiste leer un registro, reconocer un accession y una versión, y comparar qué aporta cada formato.
Pero interpretar un fragmento no es lo mismo que recuperarlo de forma reproducible. Esta sesión
responde la pregunta que quedó pendiente al cerrar S7:

> **¿De dónde provienen esos archivos y cómo puedo demostrar que descargué exactamente los datos
> correctos?**

El orden de razonamiento sigue siendo el mismo que en toda la unidad:

```text
Pregunta → Evidencia → Datos → Base de datos → Registro → Archivos → Verificación 
```

Ahora el énfasis cambia: en S7 el objetivo era interpretar la evidencia y los datos; en S8 el
objetivo es **recuperarlos de un lugar real y demostrar que lo que llegó a tu computadora es lo que
creías haber pedido**.

::: {.callout-warning}
NCBI no es un tema de esta sesión; es un ejemplo. Lo que aprendes aquí —elegir un
registro con criterio y verificar una descarga— aplica a cualquier base de datos biológica, no solo
a NCBI.
:::

## Resultados de aprendizaje

Al finalizar la sesión podrás:

1. **Explicar** qué es una base de datos biológica y distinguirla de un registro y de un ensamblado.
2. **Reconocer** el propósito de las principales bases de datos de NCBI (Assembly, Genome,
   Nucleotide, Gene, Protein, Taxonomy, PubMed) sin memorizar su interfaz.
3. **Seleccionar** un registro apropiado para responder una pregunta biológica, siguiendo la cadena
   organismo → cepa → ensamblado → versión → registro.
4. **Reconocer** la familia de archivos asociada a un ensamblado y justificar cuáles necesita cada
   pregunta.
5. **Explicar** por qué `data/source/` conserva la evidencia del origen de los datos.
6. **Explicar** cómo se verifica la integridad de una descarga mediante la comparación entre un checksum publicado y uno calculado, y registrar el checksum de referencia que se utilizará en S9.
7. **Documentar** la procedencia completa de un conjunto de datos sin inventar metadatos ausentes.

## Lista de verificación previa

Antes de comenzar confirma:

- [ ] Recuerdas qué representa un accession y una versión (S7, sección 3).
- [ ] Tienes a la vista tu pregunta y subpreguntas de `doc/protocolo.md`.
- [ ] Conservas la estructura `data/source/`, `data/processed/`, `src/`, `results/`, `doc/`.
- [ ] Tienes a la mano tu selección provisional de datos (cierre de S7).
- [ ] No pegarás credenciales, rutas institucionales privadas ni datos sensibles en una IA.

No necesitas haber descargado nada todavía. Esta sesión te lleva desde la pregunta hasta una
descarga verificada; el comando para calcular un checksum lo practicarás en S9, junto con la
transferencia entre contextos.

> IMPORTANTE: En esta sesión consultarás NCBI mediante su interfaz web. Los archivos seleccionados se descargarán desde el navegador y se colocarán en tu proyecto dentro del servidor. La recuperación mediante wget o curl y la verificación mediante comandos se trabajarán en S9.

## Ruta de S8

| Momento | Actividad | Producto | Tiempo estimado |
| --- | --- | --- | ---: |
| Antes de clase | Leer secciones 1–6 | Notas y dudas | 60–75 min |
| Antes de clase | Práctica 1: estrategia de búsqueda | Cadena organismo–ensamblado–registro | 20–25 min |
| Taller | Recuperación y comparación del primer intento | Estrategia corregida | 15 min |
| Taller | Prácticas 2–4 con roles distintos | Evidencias anotadas | 70 min |
| Taller | Práctica 5: registro colaborativo de procedencia | Ficha de procedencia avanzada | 20 min |
| Después | Completar la Tarea 4 en `doc/protocolo.md` | Conjunto de datos documentado | 40–60 min |

## 1. De un objeto biológico a un registro dentro de una base de datos [Indispensable]

En S7 viste que un objeto biológico no es lo mismo que un archivo: un gen es una región del genoma,
no un archivo, y un archivo es una representación de texto de esa región o de la secuencia completa.
Ahora falta un eslabón: ¿dónde vive ese archivo antes de que lo descargues?

```text
objeto biológico → base de datos → registro → archivos → formatos (FASTA, GFF3, GenBank)
```

Una **base de datos biológica** es el sistema que organiza, versiona y expone registros de forma
consultable. Un **registro** es la entrada de esa base de datos que reúne, para una entidad concreta
—una secuencia, un ensamblado, una publicación—, sus campos, su identificador y, casi siempre, más de
un archivo para descargarlo. El registro pertenece a la base de datos, no al revés: primero existe el
sistema que lo organiza y solo dentro de él aparece la entrada concreta que buscas. El registro
tampoco es el objeto biológico —sigue siendo una representación—, pero es el punto de partida
obligado para llegar a un archivo con procedencia conocida.

![El camino de siete pasos que va de una pregunta a un conjunto de datos reproducible, cada uno con la pregunta que responde: la pregunta biológica (qué quiero responder), el objeto biológico que contiene esa información (genoma, gen, proteína, variante), la base de datos donde encontrarlo, el registro que identifica exactamente ese objeto con su accession y versión, el conjunto de archivos en los formatos que el análisis necesita, la verificación de integridad mediante checksums, y el proyecto reproducible bien organizado y documentado. El pie enuncia la idea que ordena la sesión: un análisis bioinformático no empieza ejecutando programas, sino identificando, recuperando, documentando y verificando los datos adecuados.](images/figura-u3-s08-reproducibilidad.png)
**Figura 1.** De la pregunta biológica al proyecto reproducible: un archivo descargado es el resultado de una cadena de decisiones, no el punto de partida. Elaboración propia.

::: {.callout-important}
Empezar por "voy a buscar en NCBI" salta directamente a la herramienta. El orden
correcto sigue siendo pregunta → evidencia → datos: primero decides qué necesitas demostrar, y
solo después decides en qué base de datos y con qué registro.
:::

#### Qué debes recordar

- Un objeto biológico no vive "en un archivo": vive en un registro, y el registro vive en una base
  de datos.
- La base de datos organiza; el registro identifica una entidad concreta; el archivo es una de sus
  representaciones posibles.
- El orden de decisión siempre es pregunta → evidencia → datos → base de datos → registro, nunca al
  revés.

## 2. El ecosistema de bases de datos de NCBI [Indispensable]

NCBI no es una sola base de datos: es un conjunto de bases de datos relacionadas entre sí. No
necesitas memorizar todas; necesitas reconocer para qué sirve cada una y cuándo consultarla.

| Base de datos | Qué contiene | Ejemplo de identificador | Cuándo la consultas |
| --- | --- | --- | --- |
| **Assembly** | Ensamblados genómicos completos, con su nivel de organización y versión | `GCF_...` / `GCA_...` | Cuando necesitas el genoma completo de un organismo, cepa o aislamiento |
| **Genome** | Vista integrada de los ensamblados disponibles para un organismo, con enlaces a Assembly y otros recursos relacionados. | (vista integrada, sin accession propio) | Cuando quieres comparar cuántos ensamblados existen para una especie |
| **Nucleotide** | Registros de secuencias de ácidos nucleicos individuales (no siempre genomas completos) | `NC_...` / `NZ_...` | Cuando buscas una secuencia concreta, como un gen o un cromosoma específico |
| **Gene** | Información curada sobre un gen: función, ubicación, sinónimos, referencias | GeneID | Cuando necesitas contexto biológico de un gen, más allá de su secuencia |
| **Protein** | Secuencias y anotaciones de proteínas | `WP_...` | Cuando la evidencia que necesitas es la secuencia o función de una proteína |
| **Taxonomy** | Clasificación taxonómica y nombres científicos | taxid | Cuando necesitas confirmar el organismo exacto o su lugar en la clasificación |
| **PubMed** | Registros bibliográficos de artículos científicos | PMID | Cuando necesitas la publicación que respalda un registro (el campo `REFERENCE` que viste en GenBank, S7) |

::: {.callout-tip}
Genome no es una base de datos de secuencias independiente ni compite con Assembly:
es una **vista integrada** que agrupa, por organismo, todos los ensamblados disponibles y su nivel
de completitud. Por eso no tiene un accession propio: para descargar archivos siempre terminas en
un registro de Assembly.
:::

::: {.callout-tip}
Puedes explorar el ecosistema completo desde un solo punto de entrada:
[NCBI — todas las bases de datos](https://www.ncbi.nlm.nih.gov/gquery/) permite buscar un término
y ver en cuántas bases de datos aparece, sin tener que adivinar cuál abrir primero.
:::

No conviertas esta tabla en un catálogo que memorizar. Lo que importa es el criterio: **la base de
datos se elige después de la pregunta, nunca antes.**

#### Qué debes recordar

- NCBI es un ecosistema de bases de datos, no una sola base de datos.
- Genome es una vista integrada de ensamblados, no una fuente de secuencias por sí misma.
- Cada base de datos tiene su propio tipo de identificador; reconocer el prefijo te dice de qué base
  de datos proviene un accession.
- La base de datos se elige según la pregunta, nunca por costumbre.

### Micropráctica 1 — ¿Qué base de datos consultarías?

Para cada necesidad, escribe qué base de datos de la tabla anterior consultarías primero:

1. Confirmar si *araC* es el nombre oficial del gen o solo un sinónimo.
2. Descargar el genoma completo de *E. coli* K-12 MG1655 en su versión más reciente.
3. Leer el artículo que originalmente describió el ensamblado que vas a usar.
4. Obtener la secuencia de la proteína que produce un gen concreto.
5. Tu pregunta requiere únicamente la secuencia de un solo gen ya conocido, no el genoma completo ni
   sus coordenadas de anotación. ¿Consultarías Assembly o Nucleotide? Justifica tu elección.

<details>
<summary>Ver retroalimentación</summary>

1. Gene (y, para confirmar la clasificación del organismo, Taxonomy).
2. Assembly.
3. PubMed, a partir del campo `REFERENCE` del registro GenBank o de Assembly.
4. Protein.
5. Nucleotide. Assembly te da el ensamblado completo con toda su familia de archivos, que sería
   excesivo si solo necesitas una secuencia puntual ya identificada; Nucleotide te permite recuperar
   directamente el registro de esa secuencia. Assembly se justifica cuando la pregunta requiere el
   genoma completo o su anotación, no una sola secuencia aislada.

</details>

## 3. Elegir el registro correcto: de la pregunta al accession [Indispensable]

"El genoma de *E. coli*" no identifica un conjunto de datos reproducible, como ya viste en S7. Para
llegar a un registro concreto necesitas tomar varias decisiones, una tras otra, en este orden:

```text
pregunta biológica → organismo → cepa o aislamiento → ensamblado → versión → registro
```

A esta secuencia ordenada de decisiones la llamaremos **cadena de decisiones**: cada decisión (cada
**eslabón** de la cadena) reduce las opciones que dejó abiertas la anterior, hasta que solo queda un
registro posible.

| Decisión | Qué descarta |
| --- | --- |
| Organismo | Todas las demás especies |
| Cepa o aislamiento | Otras cepas de la misma especie, que pueden diferir en secuencia |
| Ensamblado | Otros intentos de reconstrucción del mismo genoma, con distinto nivel de calidad |
| Versión | Estados anteriores o posteriores del mismo ensamblado |
| Registro (accession) | Cualquier ambigüedad restante: el accession con versión identifica una secuencia exacta |

::: {.callout-tip}
No todos los organismos tienen un único ensamblado "de referencia". Cuando existen
varios, NCBI distingue niveles de ensamblado (por ejemplo, *complete genome*, *chromosome*,
*scaffold*, *contig*). Un nivel más completo generalmente ofrece coordenadas más confiables, pero
el nivel apropiado depende de tu pregunta, no siempre del "mejor" disponible.
:::

Para el organismo que has usado en S7, *Escherichia coli* K-12 MG1655, la cadena completa se ve así:

```text
organismo:    Escherichia coli
cepa:         K-12
aislamiento:  MG1655
ensamblado:   ASM584v2 (RefSeq: GCF_000005845.2)
versión:      .2
registro:     NC_000913.3 (cromosoma principal del ensamblado)
```

::: {.callout-tip}
`ASM584v2` y `GCF_000005845.2` no son lo mismo. `ASM584v2` es el **nombre** que el
grupo que ensambló el genoma le asignó a esa reconstrucción; es legible, pero no es estable como
identificador entre bases de datos. `GCF_000005845.2` es el **accession** que NCBI/RefSeq asigna a
ese ensamblado: es el identificador que debes citar y buscar, porque no cambia de significado.
:::


La Figura 2 resume cómo se relacionan las colecciones GenBank y RefSeq, las principales bases de datos de NCBI y los distintos tipos de accession que encontrarás al recuperar un ensamblado.

![Cómo se relacionan un ensamblado y las secuencias que lo componen dentro del ecosistema NCBI. Arriba se distinguen las colecciones —GenBank, pública y menos curada, y RefSeq, curada— de las bases especializadas: Assembly, Nucleotide, Gene, Protein, Taxonomy y PubMed. Debajo, cuatro niveles encadenados: el ensamblado, identificado con un accession GCA o GCF y ofrecido como una familia de archivos descargables (FASTA, GFF3, GBFF, protein.faa, cds.fna, rna.fna); las secuencias individuales que lo componen —cromosoma, plásmido, scaffold, contig—, cada una con su propio accession NC, NW o NZ; los genes, con su GeneID, anclados a coordenadas de esas secuencias; y las proteínas, con accession WP o NP. La idea clave es que cada nivel responde a una pregunta distinta y usa un tipo de accession específico.](images/figura-u3-s08-ncbi-db.png)
**Figura 2.** Relación entre un ensamblado y las secuencias que lo componen en NCBI. Un ensamblado, identificado por un accession `GCA_...` o `GCF_...`, agrupa una o más secuencias del genoma y sus archivos asociados. Cada secuencia (por ejemplo, un cromosoma o un plásmido) posee un accession propio en la base de datos Nucleotide, mientras que las anotaciones de genes y proteínas se enlazan mediante las bases de datos Gene y Protein. Esta organización permite relacionar de forma consistente ensamblados, secuencias, anotaciones y productos génicos. Elaboración propia. Nota: Los accession mostrados son ejemplos de los tipos de identificadores utilizados por NCBI.

::: {.callout-important}
El accession del **ensamblado** (`GCF_000005845.2`) y el accession de la
**secuencia** dentro de ese ensamblado (`NC_000913.3`) no son intercambiables. Un ensamblado puede
incluir varias secuencias (cromosomas, plásmidos); cada una tiene su propio accession.
:::

#### Qué debes recordar

- La cadena organismo → cepa o aislamiento → ensamblado → versión → registro descarta opciones en
  cada paso, hasta llegar a un dato reproducible.
- El nombre de un ensamblado (por ejemplo, `ASM584v2`) no sustituye a su accession estable
  (`GCF_000005845.2`).
- El accession del ensamblado y el de una secuencia dentro de él son identificadores distintos y no
  intercambiables.

### Práctica 1 — Estrategia de búsqueda (primer intento)

#### Antes de clase — primer intento individual

1. Retoma tu selección provisional de datos del cierre de S7 (o, si aún no tienes una pregunta de
   proyecto definida, usa esta: *¿qué genes están anotados en el ensamblado de referencia de tu
   organismo de interés?*).
2. Completa la cadena de decisiones de la sección 3 (organismo → cepa → ensamblado → versión →
   registro) sin consultar todavía ninguna base de datos:

| Eslabón | Tu decisión | Cómo la confirmarías |
| --- | --- | --- |
| Organismo | | |
| Cepa o aislamiento | | |
| Ensamblado esperado | | |
| Versión | | |
| Base de datos que consultarías primero | | |

3. Escribe una duda auténtica sobre algún eslabón. No la resuelvas todavía.

#### Durante el taller — comparación y corrección

1. Intercambia tu tabla con otra persona.
2. Señalen juntos cualquier eslabón que se haya saltado (por ejemplo, ir directo de "organismo" a
   "registro" sin pasar por cepa o ensamblado).
3. Corrijan la tabla después de revisar la sección 2 y buscar el organismo en NCBI (Taxonomy o
   Assembly, según lo que falte confirmar).
4. Conserven el primer intento visible junto con la corrección.

#### Después del taller — evidencia final

Incorpora la tabla corregida a `doc/protocolo.md`, en una sección `## Estrategia de búsqueda`, y
señala cualquier eslabón que siga pendiente de confirmar.

**Criterio de logro:** la cadena de decisiones de la sección 3 está completa y coherente con la
pregunta; ningún eslabón se salta ni se inventa.

**Para cerrar:** ¿cuál fue el eslabón más difícil de justificar? No hace falta responderlo por
escrito; basta con que lo identifiques antes de seguir.

## 4. Un ensamblado genera una familia de archivos [Indispensable]

Un solo ensamblado no es un solo archivo. Al descargar un ensamblado de NCBI encontrarás, entre
otros, estos archivos:

| Archivo | Contenido | Formato que ya conoces (S7) |
| --- | --- | --- |
| `genome.fna` (o `*_genomic.fna`) | Secuencia completa del ensamblado | FASTA |
| `genomic.gff` | Anotación de features sobre esa secuencia | GFF3 |
| `genomic.gbff` | Registro completo, con secuencia y anotación integradas | GenBank (flat file) |
| `protein.faa` | Secuencias de las proteínas anotadas | FASTA (proteína) |
| `cds.fna` (o `cds_from_genomic.fna`) | Secuencias de nucleótidos de las regiones codificantes | FASTA (nucleótidos) |
| `rna.fna` | Secuencias de los transcritos de ARN anotados | FASTA (nucleótidos) |


Ningún archivo de la tabla sustituye a los demás: `genome.fna` no contiene anotaciones, `genomic.gff`
no contiene la secuencia completa por sí sola (recuerda de S7 que un GFF3 necesita el FASTA
correspondiente), y `genomic.gbff` integra ambas cosas a costa de una estructura más compleja de
interpretar en bloque.

::: {.callout-warning}
No todos los ensamblados incluyen los seis archivos. Un ensamblado a nivel
*contig*, por ejemplo, puede no tener anotación todavía. Verifica qué archivos existen realmente
para tu registro antes de asumir que todos estarán disponibles.
:::

#### Qué debes recordar

- Un ensamblado no es un archivo: es una familia de archivos relacionados, cada uno con un propósito
  distinto.
- Ningún archivo de la familia sustituye a otro; un GFF3 sin su FASTA correspondiente no es
  utilizable.
- No todos los ensamblados tienen los seis archivos disponibles; verifica antes de asumir.

En las siguientes unidades trabajarás principalmente con una parte de esta familia de archivos. Saber que existen los demás te permitirá justificar por qué elegiste unos y descartaste otros.

### Práctica 2 — Como responsable del laboratorio: ¿qué archivos pido?

#### Objetivo

Decidir, para preguntas de investigación distintas, qué archivos de la familia de un ensamblado son
necesarios y cuáles serían descargas innecesarias.

---

#### Caso

Eres responsable de un laboratorio pequeño. Tres integrantes te piden ayuda para descargar datos del
mismo ensamblado de referencia. La conexión del laboratorio es lenta ese día: solo pueden descargar
los archivos estrictamente necesarios para cada tarea, no la familia completa "por si acaso".

---

##### Actividad 1. Tres peticiones

Para cada integrante, marca los archivos indispensables y explica por qué los demás no lo son.

| Integrante | Necesita... | Archivos indispensables |
| --- | --- | --- |
| A | Contar cuántos genes están anotados | |
| B | Diseñar cebadores sobre una región genómica específica | |
| C | Comparar la secuencia de una proteína con la de otro organismo | |

<details>
<summary><strong>Ver respuesta sugerida</strong></summary>

- A necesita `genomic.gff` (los features de tipo `gene`); no necesita la secuencia completa para
  *contar*, aunque conviene conservarla para trabajo posterior.
- B necesita `genome.fna` (para diseñar sobre la secuencia genómica real, con coordenadas) y
  `genomic.gff` (para ubicar la región de interés).
- C necesita únicamente `protein.faa`; descargar `genome.fna` completo sería innecesario para esa
  pregunta.

</details>

---

##### Actividad 2. El error del integrante D

Un cuarto integrante descargó solo `genomic.gff` y luego intentó extraer la secuencia de un gen
directamente del archivo. ¿Qué le falta y por qué su plan no puede funcionar?

<details>
<summary><strong>Ver respuesta sugerida</strong></summary>

Le falta `genome.fna`. El GFF3 solo contiene coordenadas y atributos; no contiene los nucleótidos.
Sin el FASTA correspondiente al mismo ensamblado y versión, las coordenadas no se pueden traducir en
una secuencia.

</details>

---

#### Criterio de logro

Distingues qué archivo de la familia responde cada tipo de pregunta, reconoces cuándo un archivo por
sí solo es insuficiente, y bajo la restricción de conexión limitada eliges solo lo estrictamente
necesario para cada caso, sin descargar la familia completa por precaución.

## 5. `data/source/`: la evidencia del origen de los datos [Indispensable]

Desde U1 conservas la estructura:

```text
proyecto/
├── data/
│   ├── source/
│   └── processed/
├── src/
├── results/
└── doc/
```

`data/source/` no es "la carpeta donde se guardan los datos": es la **evidencia de procedencia**. Un
archivo que entra a `data/source/` se conserva con su nombre original, sin editarse, y acompañado de
la información suficiente para volver a localizarlo (Noble, 2009; Wilson et al., 2017). Cualquier
transformación —descomprimir, renombrar, filtrar— genera un archivo nuevo en `data/processed/`; el
original permanece intacto.

Para los archivos que descargarás en esta unidad, una organización coherente es:

```text
data/source/
    GCF_000005845.2/
        genome.fna
        genomic.gff
        genomic.gbff
        md5checksums.txt
```

::: {.callout-important}
El nombre de la carpeta (`GCF_000005845.2`) no es una elección estética: es el
accession del ensamblado. Cualquier persona que abra tu proyecto debe poder saber, sin preguntarte,
de qué ensamblado provienen esos archivos.
:::

#### Qué debes recordar

- `data/source/` conserva la evidencia del origen de los datos, no es una carpeta de trabajo.
- Ningún archivo dentro de `data/source/` se edita ni se renombra; cualquier transformación produce
  un archivo nuevo en `data/processed/`.
- El nombre de la carpeta debe permitir identificar el ensamblado sin tener que preguntar.

## 6. Verificación de integridad: ¿cómo sabes que descargaste lo correcto? [Indispensable]

![El flujo de recuperación y verificación en cinco pasos: definir la pregunta biológica, elegir el registro que mejor la responde, descargar los archivos asociados, comparar el checksum publicado con el calculado localmente y documentar todo en data/source/. El cuarto paso se bifurca: si los checksums coinciden el archivo es íntegro y se continúa; si no coinciden, una flecha de retroalimentación vuelve al paso de descarga, con la instrucción de volver a descargar y no editar el archivo. El último paso enumera qué debe registrarse: archivos descargados, URL del registro, fecha, accession, y algoritmo y checksum calculado.](images/figura-u3-s08-flujo-recuperacion.png)
**Figura 3.** Flujo de recuperación y verificación de integridad de un conjunto de datos. Elaboración propia.

Observa que el flujo comienza después de haber completado la cadena de decisiones de la sección 3. Verificar una descarga no sustituye elegir correctamente el registro.


Una descarga puede fallar de formas que no siempre son visibles: una conexión interrumpida puede
dejar un archivo incompleto que aun así "se abre"; un archivo puede corromperse durante la
transferencia; o pudiste, sin darte cuenta, descargar una versión distinta a la que creías. Ninguno
de estos problemas se nota con solo mirar el tamaño del archivo o abrirlo en un editor.

::: {.callout-tip title="¿Sabías que?"}
Un archivo FASTA truncado a la mitad puede seguir teniendo una línea de
definición válida y miles de líneas de secuencia con apariencia normal. Nada en el contenido avisa
que falta la otra mitad, a menos que la compares contra algo.
:::

La solución es un **checksum**: un valor corto, calculado a partir de todo el contenido de un
archivo, que cambia si un solo carácter del archivo cambia. Dos funciones comunes para calcularlo son
**MD5** (Rivest, 1992) y **SHA-256** (NIST, 2015). Si el checksum que tú calculas sobre el archivo
descargado coincide con el que publica la fuente, tienes evidencia de que el archivo llegó completo y
sin alteraciones.

```text
Checksum publicado por NCBI para genome.fna:   4c090bf78a5bf49a95b0ad293b6960a8
Checksum que tú calculas sobre tu descarga:    4c090bf78a5bf49a95b0ad293b6960a8
                                                ¿coinciden? → si sí, la descarga está verificada
```

::: {.callout-tip}
NCBI publica un archivo `md5checksums.txt` junto con cada ensamblado, con un checksum por
cada archivo de la familia. No necesitas calcular nada a mano: solo necesitas comparar.
:::

::: {.callout-warning}
Un checksum verifica que el archivo **no cambió entre la fuente y tu copia**. No
verifica que hayas elegido el registro, la versión o el organismo correctos: eso lo decidiste en
las secciones 1 a 3. Integridad y selección correcta son dos verificaciones distintas.
:::

El comando para calcular un checksum (`md5sum`, `sha256sum` o equivalentes) lo practicarás en **S9**,
junto con la transferencia de archivos entre contextos. Aquí interesa el concepto: **una descarga sin
checksum verificado es una descarga sin evidencia de integridad**, sin importar qué tan segura se
vea.

#### Qué debes recordar

- Un checksum verifica integridad (el archivo no cambió), no selección correcta (el archivo era el
  adecuado).
- Si el checksum calculado no coincide con el publicado, la respuesta es volver a descargar, nunca
  usar el archivo de todas formas.
- NCBI publica los checksums junto con cada ensamblado; no hace falta calcular nada a mano para
  comparar.

### Práctica 3 — Como revisor de una revista científica: ¿la descarga es verificable?

#### Objetivo

Evaluar, a partir de un checksum publicado y uno calculado, si una descarga puede considerarse
íntegra, y distinguir esa verificación de la verificación de que el registro elegido sea el correcto.


En esta práctica interpretarás una comparación ya proporcionada. No calcularás todavía el checksum de tus propios archivos. Esa comprobación operativa se realizará en S9.


#### Caso de estudio

Un autor documentó en su protocolo:

```text
Archivo: genome.fna
Checksum publicado (NCBI): 4c090bf78a5bf49a95b0ad293b6960a8
Checksum calculado (local): 4c090bf78a5bf49a95b0ad293b6960a7
```

---

##### Actividad 1. Como revisor de una revista científica

**¿Aceptarías este archivo como parte de un análisis reproducible?**

- ☐ Sí
- ☐ No

Justifica tu respuesta.

<details>
<summary><strong>Ver respuesta sugerida</strong></summary>

**No.** Los checksums no coinciden (difieren en el último carácter). Esto indica que el archivo
descargado no es idéntico, byte a byte, al publicado por la fuente. No se puede confiar en ese
archivo hasta descargarlo de nuevo y volver a verificar.

</details>

---

##### Actividad 2. ¿Qué NO demuestra un checksum correcto?

Marca verdadero o falso.

| Afirmación | V | F |
| --- | :--: | :--: |
| Un checksum que coincide demuestra que el archivo no se alteró en la descarga. | | |
| Un checksum que coincide demuestra que elegiste el organismo correcto. | | |
| Un checksum que coincide demuestra que elegiste la versión más reciente del ensamblado. | | |
| Un checksum que no coincide siempre significa que alguien alteró el archivo intencionalmente. | | |

<details>
<summary><strong>Ver respuesta</strong></summary>

- Verdadero. Falso. Falso. Falso.
- Un checksum correcto solo demuestra integridad de la copia, no que la selección (organismo,
  versión) haya sido la adecuada. Un checksum incorrecto puede deberse a una descarga incompleta o
  interrumpida, no necesariamente a una alteración intencional.

</details>

---

##### Actividad 3. Reflexión

¿Por qué un checksum que coincide **no** es evidencia suficiente para documentar toda la procedencia
de un dato?

<details>
<summary><strong>Ver respuesta sugerida</strong></summary>

Porque la procedencia también requiere saber qué organismo, cepa, ensamblado, versión y accession se
consultaron, cuándo, y con qué licencia. El checksum responde una sola pregunta: ¿el archivo que
tengo es idéntico al publicado? No responde si ese archivo era el correcto para tu pregunta
biológica.

</details>

---

#### Criterio de logro

Distingues verificación de integridad (el archivo no cambió) de verificación de selección (el
archivo era el correcto), y reconoces que ambas son necesarias, no intercambiables.

### Práctica 4 — Como curador de datos: organiza `data/source/`

#### Objetivo

Aplicar la convención de `data/source/` a un conjunto de archivos reales, decidiendo qué se conserva
tal cual y qué información de procedencia debe acompañarlo.

---

#### Caso

Recibiste, sin más contexto, estos cuatro archivos en una memoria USB:

```text
genome.fna
genomic.gff
genomic.gbff
md5checksums.txt
```

---

##### Actividad 1. ¿Puedes usarlos de inmediato?

Enumera, como curador de datos, qué información **falta** antes de poder documentar la procedencia de
estos archivos en un proyecto reproducible.

<details>
<summary><strong>Ver respuesta sugerida</strong></summary>

Falta, como mínimo: organismo, cepa o aislamiento, accession del ensamblado, versión, colección
(GenBank o RefSeq), fecha en que se descargaron, y de dónde provienen exactamente (URL o base de
datos consultada). Sin esta información, los archivos son técnicamente utilizables pero no
reproducibles: nadie —ni tú en unas semanas— podría volver a localizar la fuente exacta.

</details>

---

##### Actividad 2. Organización correcta

Propón, siguiendo la convención de la sección 5, la ruta completa donde colocarías cada archivo
dentro de la estructura del proyecto (asume que después de investigar confirmas que provienen del
ensamblado `GCF_000005845.2`).

<details>
<summary><strong>Ver respuesta</strong></summary>

```text
data/source/GCF_000005845.2/genome.fna
data/source/GCF_000005845.2/genomic.gff
data/source/GCF_000005845.2/genomic.gbff
data/source/GCF_000005845.2/md5checksums.txt
```

Ninguno de estos archivos se edita ni se renombra. Cualquier transformación posterior (por ejemplo,
descomprimir o filtrar) produce un archivo nuevo en `data/processed/`.

Los archivos fueron seleccionados y descargados mediante la interfaz web. Una vez disponibles, deben colocarse sin modificaciones en el directorio correspondiente del proyecto en el servidor. En esta sesión no se automatiza la recuperación ni se calcula todavía el checksum.

</details>

---

##### Actividad 3. La propuesta de un compañero

Un compañero de equipo propone renombrar `genome.fna` como `ecoli.fasta` dentro de `data/source/`,
"porque es más claro". ¿Por qué **no** deberías hacerlo ahí?

<details>
<summary><strong>Ver respuesta sugerida</strong></summary>

Porque `data/source/` conserva los archivos con su nombre original como parte de la evidencia de
procedencia: el nombre `genome.fna` (junto con la ruta `GCF_000005845.2/`) es lo que permite
rastrear de qué descarga exacta proviene el archivo. Renombrarlo ahí borra esa trazabilidad, aunque
el nuevo nombre sea más legible. Si se quiere un nombre más claro para trabajar, la solución es
copiarlo (con ese nombre nuevo) a `data/processed/`, dejando el original intacto en `data/source/`.

</details>

---

#### Criterio de logro

Reconoces qué metadatos de procedencia son indispensables antes de considerar "listo para usar" un
conjunto de archivos, ubicas los archivos originales sin alterarlos, y justificas por qué renombrar
dentro de `data/source/` rompe la evidencia de procedencia.

### Práctica 5 — Registro colaborativo de procedencia

#### Objetivo

Elaborar, en equipo, la ficha de procedencia iniciada en S7 con la información que S8 permite
completar: registro consultado, accession, versión, archivos recuperados y verificación de
integridad.

---

Trabajen como **integrantes de un proyecto colaborativo**: cada persona aporta una parte de la ficha
y el equipo la revisa en conjunto antes de darla por completa.

1. Retomen la selección provisional de datos del cierre de S7 (Pregunta, Evidencia necesaria,
   Formatos candidatos, Qué aporta cada formato, Información pendiente de confirmar).
2. Complementen cada campo pendiente con lo que investigaron en las Prácticas 1 a 4:

```markdown
## Ficha de procedencia del conjunto de datos

- Pregunta biológica:
- Organismo, cepa o aislamiento:
- Base de datos y colección (GenBank o RefSeq):
- Accession del ensamblado, con versión:
- Accession de la(s) secuencia(s) principal(es):
- Archivos recuperados:
- Checksum publicado por la fuente:
- Archivo al que corresponde:
- Algoritmo utilizado por la fuente:
- Checksum calculado en el servidor: pendiente de S9
- Resultado de la comparación: pendiente de S9
- Fecha de consulta y descarga:
- Licencia o condiciones de uso:
- Información no documentada o pendiente de confirmar:
```

3. Cada integrante explica en voz alta un campo de la ficha y de dónde salió esa información
   (¿Assembly? ¿Taxonomy? ¿el propio archivo descargado?).
4. Marquen con honestidad cualquier campo que siga sin confirmarse; no lo completen por inferencia.

<details>
<summary>Ver ejemplo de ficha completada (con el organismo de ejemplo del curso)</summary>


```markdown
## Ficha de procedencia del conjunto de datos

### Identificación del conjunto de datos

- Pregunta biológica:
- Organismo, cepa o aislamiento:
- Base de datos y colección (GenBank o RefSeq):
- Accession del ensamblado, con versión:
- Accession de la(s) secuencia(s) principal(es):

### Archivos recuperados

- Archivos recuperados:

### Evidencia de integridad

- Algoritmo de checksum publicado por la fuente:
- Checksum publicado por la fuente:
- Archivo al que corresponde:
- Checksum calculado localmente: **Pendiente (S9)**
- Resultado de la comparación: **Pendiente (S9)**

### Procedencia

- Fecha de consulta:
- Fecha de descarga:
- Licencia o condiciones de uso:
- Información no documentada o pendiente de confirmar:
```


</details>

**Criterio de logro:** la ficha distingue claramente lo confirmado de lo pendiente, y cada campo
puede rastrearse hasta la base de datos o el archivo que lo originó.

## Tarea 4 — Construcción de un conjunto de datos reproducible

La Tarea 4 no consiste únicamente en descargar archivos. Consiste en **construir un conjunto de datos
del que puedas demostrar el origen completo**.

### Producto esperado

```text
proyecto/
├── data/
│   └── source/
│       └── GCF_xxxxxxxxx.x/
│           ├── genome.fna
│           ├── genomic.gff
│           ├── genomic.gbff
│           └── md5checksums.txt
├── doc/
│   └── protocolo.md
└── results/
```

### Debes documentar en `doc/protocolo.md`

- organismo, cepa o aislamiento;
- ensamblado y accession, con versión;
- colección (GenBank o RefSeq);
- fecha de descarga;
- checksum (publicado; el cálculo y la comparación se completan en S9);
- archivos utilizados y su función;
- justificación de la selección: por qué este registro y no otro respondía tu pregunta.

::: {.callout-important}
Si algún dato no está disponible en la fuente consultada, escribe "no documentado"
o "pendiente de confirmar". No lo completes por inferencia ni le pidas a una IA que lo invente.
:::

### Lista de control antes de entregar

- [ ] Organismo
- [ ] Cepa o aislamiento
- [ ] Ensamblado
- [ ] Versión
- [ ] Colección (GenBank o RefSeq)
- [ ] Archivos utilizados
- [ ] Fecha de descarga
- [ ] Campos pendientes de confirmar claramente marcados como tales


Si durante la tarea descubres que elegiste un ensamblado distinto al que realmente necesitabas, no modifiques la ficha anterior. Conserva ambas decisiones y documenta el cambio. La reproducibilidad también implica dejar evidencia de las correcciones realizadas.


## Evidencia de la sesión

Entrega o conserva, según indique el docente:

1. estrategia de búsqueda inicial y corregida (Práctica 1);
2. decisiones de archivos indispensables por caso (Práctica 2);
3. evaluación de integridad de una descarga (Práctica 3);
4. organización propuesta de `data/source/` (Práctica 4);
5. ficha de procedencia colaborativa (Práctica 5);
6. avance de la Tarea 4 registrado en `doc/protocolo.md`.

La descarga real y la comparación de checksums con un comando se completan en S9; en S8 basta con
identificar el registro, recuperar los archivos y registrar el checksum publicado.

## Errores frecuentes y estrategias de diagnóstico

| Error | Por qué ocurre | Estrategia de diagnóstico |
| --- | --- | --- |
| Buscar "el genoma de la especie" sin especificar cepa ni ensamblado | Se asume que existe un único genoma por especie | Revisar Assembly: ¿cuántos ensamblados aparecen para esa especie? |
| Confundir el accession del ensamblado con el de una secuencia dentro de él | Ambos empiezan con letras similares (GCF/GCA vs. NC/NZ) | Verificar el prefijo y el contexto: ¿describe todo el ensamblado o una sola molécula? |
| Descargar solo un archivo de la familia y asumir que basta | Se ignora qué formato aporta cada tipo de información | Revisar la tabla de la sección 4 antes de descargar |
| Tratar un checksum que coincide como prueba de que el registro era el correcto | Se confunde integridad con selección | Recordar que integridad y selección son verificaciones distintas (sección 6) |
| Editar o renombrar un archivo dentro de `data/source/` | Parece más cómodo para el análisis siguiente | Recordar que cualquier transformación va a `data/processed/`, nunca sobre el original |
| Inventar la fecha de descarga o la licencia cuando no se registró a tiempo | Se quiere completar la ficha | Escribir "no documentado" o "pendiente de confirmar" |
| Usar PubMed como si fuera una base de datos de secuencias | Se agrupan todas las bases de NCBI como si fueran intercambiables | Revisar la tabla de la sección 2: PubMed es literatura, no secuencia |

## Rúbricas

| Criterio | Logrado | Parcialmente logrado | Aún no logrado |
| --- | --- | --- | --- |
| Primer intento | Presenta la cadena organismo–ensamblado–registro completa, con razonamiento propio antes del taller | Presenta una cadena incompleta pero permite discutir decisiones | No presenta evidencia previa o fue generada sin razonamiento explicable |
| Ecosistema de bases de datos | Elige la base de datos correcta según la pregunta, sin confundir su propósito | Reconoce las bases de datos, pero duda al elegir cuál usar | Trata todas las bases de datos como intercambiables |
| Selección del registro | La cadena organismo–cepa–ensamblado–versión–registro es completa y justificada | Hay uno o dos eslabones débiles o sin justificar | Elige un registro sin poder explicar por qué |
| Familia de archivos | Identifica qué archivos necesita cada pregunta y por qué los demás no son necesarios | Identifica los archivos, pero no justifica cuáles son indispensables | Descarga o solicita archivos sin relación con la pregunta |
| Verificación de integridad | Distingue integridad de selección correcta; interpreta un checksum sin inventar certeza | Reconoce el concepto, pero confunde integridad con selección | No puede explicar para qué sirve un checksum |
| Documentación (Tarea 4) | La ficha permite a otra persona reconstruir el origen completo del dato | Ficha incompleta o con campos inferidos | No documenta o completa datos por inferencia |

La rúbrica es formativa para las Prácticas 1–5; la evaluación calificada corresponde a la Tarea 4.

## Autoevaluación

### Comprobación rápida — formativa, al final del taller

1. ¿Qué diferencia hay entre un registro y una base de datos?
2. ¿Qué base de datos de NCBI consultarías para confirmar el organismo exacto de una muestra?
3. ¿Por qué el accession de un ensamblado y el de una secuencia dentro de él no son intercambiables?
4. ¿Qué archivo de la familia de un ensamblado necesitas si tu pregunta requiere coordenadas de
   genes?
5. ¿Qué demuestra —y qué no demuestra— que dos checksums coincidan?
6. ¿Por qué un archivo dentro de `data/source/` nunca se edita directamente?
7. ¿Qué escribirías si todavía no puedes confirmar la fecha de descarga de un archivo?

### Semáforo

- 🟢 **Verde:** elijo la base de datos correcta para cada pregunta, sigo la cadena completa hasta un
  registro, reconozco qué archivos necesito y distingo integridad de selección correcta.
- 🟡 **Amarillo:** reconozco los conceptos, pero aún dudo al elegir entre bases de datos o confundo
  algún archivo de la familia con otro.
- 🔴 **Rojo:** elijo un registro sin poder justificarlo, o trato un checksum correcto como prueba de que elegí bien el organismo o la versión.

Si estás en amarillo o rojo, conserva tu evidencia y lleva una pregunta concreta a S9. No consideres
cerrada la Tarea 4 hasta poder explicar cada campo de tu ficha de procedencia.


Si otra persona descargara hoy exactamente los mismos archivos siguiendo tu protocolo, ¿obtendría el mismo conjunto de datos? ¿Qué información de tu ficha garantiza esa reproducibilidad?


## Cierre de S8 y puente hacia S9

En esta sesión pasaste de interpretar formatos (S7) a recuperar un conjunto de datos real y
documentar su procedencia. Todavía falta un paso: **demostrar que el archivo que tienes en tu
computadora es exactamente el mismo, byte a byte, que el que declaraste haber descargado** —y que,
si lo mueves o lo compartes, sigue siendo el mismo archivo al llegar a su destino.

::: {.callout-important}
Conserva los archivos que recuperaste en esta sesión, sin modificarlos. Los
necesitarás intactos para S9.
:::

**[S9 — Inspección y transferencia verificable de datos biológicos](u3-s9-inspeccion-transferencia-verificable.md).**
Inspeccionarás los archivos sin modificar los originales, los transferirás entre contextos y
demostrarás que origen y destino contienen los mismos bytes. Esta sesión desarrolla la **Tarea 5**.

## Anexo A. Correspondencia resultado–actividad–evidencia–criterio

| Resultado | Actividad | Evidencia | Criterio | Momento | Nivel en U3 |
| --- | --- | --- | --- | --- | --- |
| RA1 Explicar base de datos, registro y ensamblado | Secciones 1–3 y Micropráctica 1 | Respuestas de la micropráctica | Distingue los tres niveles sin confundirlos | Antes/taller | Comprensión |
| RA2 Reconocer el ecosistema de NCBI | Sección 2 y Micropráctica 1 | Elección justificada de base de datos | Base de datos elegida según la pregunta, no por costumbre | Taller | Comprensión |
| RA3 Seleccionar un registro apropiado | Práctica 1 | Cadena de búsqueda corregida | Cadena completa y justificada | Antes/taller | Aplicación guiada |
| RA4 Reconocer la familia de archivos de un ensamblado | Práctica 2 | Archivos indispensables por caso | Selección de archivos justificada por la pregunta | Taller | Aplicación guiada |
| RA5 Verificar integridad | Práctica 3 | Evaluación de checksums | Distingue integridad de selección correcta | Taller | Aplicación guiada |
| RA6 Documentar procedencia | Prácticas 4–5 y Tarea 4 | Ficha de procedencia y protocolo actualizado | Registro honesto, completo y reproducible | Taller/después | Aplicación inicial |

## Anexo B. Alineación transversal

| Actividad | Reproducibilidad | Verificación | Validación | Robustez |
| --- | --- | --- | --- | --- |
| Estrategia de búsqueda | Explicita la cadena organismo–ensamblado–registro antes de buscar | Contrasta la cadena con Assembly y Taxonomy | Compara con la definición de accession y versión de S7 | Reconoce cuándo un eslabón sigue sin confirmarse |
| Familia de archivos | Registra qué archivos corresponden a qué ensamblado y versión | Confirma que los archivos declarados existen para ese registro | Contrasta con la tabla FASTA/GFF3/GenBank de S7 | Identifica cuándo un ensamblado no tiene todos los archivos |
| Verificación de integridad | Conserva el checksum publicado junto con los archivos | Compara checksum publicado contra el calculado | Distingue integridad de selección correcta | Reconoce que un checksum correcto no valida la elección del registro |
| `data/source/` | Conserva archivos originales sin editar | Otra persona puede rastrear el accession desde el nombre de la carpeta | No completa metadatos por inferencia | Cualquier transformación queda fuera de `data/source/` |
| Ficha de procedencia | Deja explícitos los campos confirmados y los pendientes | Cada campo se puede rastrear a su fuente | No inventa licencia, fecha ni checksum | Conserva "pendiente de confirmar" cuando corresponde |

## Glosario

| Español | Inglés | Definición breve |
| --- | --- | --- |
| Base de datos | Database | Sistema que organiza, versiona y expone registros consultables |
| Registro | Record | Entrada de una base de datos que reúne los campos de una entidad concreta |
| Ensamblado | Assembly | Conjunto versionado de secuencias que representa un genoma reconstruido |
| Ensamblado de referencia | Reference assembly | Ensamblado designado como representativo de una especie o cepa |
| Nivel de ensamblado | Assembly level | Grado de continuidad de un ensamblado (contig, scaffold, cromosoma, genoma completo) |
| Cepa | Strain | Variante genética de una especie, relevante para identificar un ensamblado |
| Aislamiento | Isolate | Muestra específica de la que se obtuvo el material genético secuenciado |
| Colección | Collection | Conjunto al que pertenece un registro, por ejemplo GenBank o RefSeq |
| Checksum | Checksum | Valor calculado a partir del contenido de un archivo, usado para verificar su integridad |
| Integridad | Integrity | Propiedad de un archivo que no ha sido alterado respecto de su fuente |
| Procedencia | Provenance | Historial documentado del origen y las transformaciones de un dato |
| Familia de archivos | File family | Conjunto de archivos relacionados que describen el mismo ensamblado |
| Ficha de procedencia | Provenance record | Documento que registra el origen, versión y verificación de un conjunto de datos |
| Licencia de uso | Usage license / terms of use | Condiciones bajo las cuales puede reutilizarse un dato publicado |

## Referencias

- Buffalo, V. (2015). *Bioinformatics Data Skills*. O'Reilly Media.
- Noble, W. S. (2009). A quick guide to organizing computational biology projects. *PLoS
  Computational Biology*, 5(7), e1000424. <https://doi.org/10.1371/journal.pcbi.1000424>
- Wilson, G., et al. (2017). Good enough practices in scientific computing. *PLoS Computational
  Biology*, 13(6), e1005510. <https://doi.org/10.1371/journal.pcbi.1005510>
- Rivest, R. (1992). *The MD5 Message-Digest Algorithm*. RFC 1321. Internet Engineering Task Force.
  <https://www.rfc-editor.org/rfc/rfc1321>
- National Institute of Standards and Technology (NIST). (2015). *Secure Hash Standard (SHS)*.
  FIPS PUB 180-4. <https://doi.org/10.6028/NIST.FIPS.180-4>
- National Center for Biotechnology Information (NCBI). (2024). *Assembly help*.
  <https://www.ncbi.nlm.nih.gov/assembly/help/>
- National Center for Biotechnology Information (NCBI). (2024). *NCBI Datasets documentation*.
  <https://www.ncbi.nlm.nih.gov/datasets/>
- National Center for Biotechnology Information (NCBI). (2024). *PubMed User Guide*.
  <https://pubmed.ncbi.nlm.nih.gov/help/>
- National Center for Biotechnology Information (NCBI). (2019). *GenBank release notes: flat-file
  format—ACCESSION and VERSION*. <https://www.ncbi.nlm.nih.gov/genbank/release/230/>
