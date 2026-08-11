## Ejercicio: Análisis de Referencias de Reguladores Transcripcionales en E. coli

A lo largo de los años, se ha documentado la regulación transcripcional de Escherichia coli en RegulonDB. Para cada regulador o factor de transcripción (TF), contamos con una lista de referencias identificadas por su PubMed Identifier (PMID), que están asociadas a cada interacción del TF con su región promotora.

Con estas listas de PMIDs para cada TF, se ha descargado la información de las publicaciones correspondientes en formato PubMed, que tiene el siguiente formato:

```
PMID- 36972330
OWN - NLM
STAT- MEDLINE
DCOM- 20230329
LR  - 20230519
IS  - 1465-2080 (Electronic)
IS  - 1350-0872 (Print)
IS  - 1350-0872 (Linking)
VI  - 169
IP  - 3
DP  - 2023 Mar
TI  - Regulation of phosphate starvation-specific responses in Escherichia coli.
LID - 10.1099/mic.0.001312 [doi]
LID - 001312
AB  - Toxic agents added into the medium of rapidly growing Escherichia coli induce 
      specific stress responses through the activation of specialized transcription 
      factors. Each transcription factor and downstream regulon (e.g. SoxR) are linked 
      to a unique stress (e.g. superoxide stress). Cells starved of phosphate induce 
      several specific stress regulons during the transition to stationary phase when 
      the growth rate is steadily declining. Whereas the regulatory cascades leading to 
      the expression of specific stress regulons are well known in rapidly growing 
      cells stressed by toxic products, they are poorly understood in cells starved of 
      phosphate. The intent of this review is to both describe the unique mechanisms of 
      activation of specialized transcription factors and discuss signalling cascades 
      leading to the induction of specific stress regulons in phosphate-starved cells. 
      Finally, I discuss unique defence mechanisms that could be induced in cells 
      starved of ammonium and glucose.
FAU - Moreau, Patrice L
AU  - Moreau PL
AD  - Laboratoire Chimie Bactérienne, LCB-UMR 7283, Institut Microbiologie 
      Méditerranée, CNRS/Université Aix-Marseille, Marseille, France.
LA  - eng
PT  - Journal Article
PT  - Research Support, Non-U.S. Gov't
PT  - Review
PL  - England
TA  - Microbiology (Reading)
JT  - Microbiology (Reading, England)
JID - 9430468
RN  - 0 (Escherichia coli Proteins)
RN  - 0 (Bacterial Proteins)
RN  - 0 (Phosphates)
RN  - 0 (Transcription Factors)
SB  - IM
MH  - *Escherichia coli/metabolism
MH  - *Escherichia coli Proteins/genetics/metabolism
MH  - Bacterial Proteins/genetics
MH  - Phosphates/metabolism
MH  - Transcription Factors/genetics/metabolism
MH  - Regulon
MH  - Gene Expression Regulation, Bacterial
PMC - PMC10191379
OTO - NOTNLM
OT  - CpxR
OT  - Kdp
OT  - LexA
OT  - PtsN
OT  - RpoE
OT  - SoxR
COIS- The author declares there are no conflicts of interest.
EDAT- 2023/03/28 06:00
MHDA- 2023/03/29 06:05
PMCR- 2023/03/27
CRDT- 2023/03/27 13:53
PHST- 2023/03/29 06:05 [medline]
PHST- 2023/03/27 13:53 [entrez]
PHST- 2023/03/28 06:00 [pubmed]
PHST- 2023/03/27 00:00 [pmc-release]
AID - 001312 [pii]
AID - 10.1099/mic.0.001312 [doi]
PST - ppublish
SO  - Microbiology (Reading). 2023 Mar;169(3):001312. doi: 10.1099/mic.0.001312.
```

Los siguientes campos son los que utilizaremos en este análisis:

- `PMID-`: Identificador único de PubMed para el artículo.
- `DP`: Fecha de publicación, donde se especifica el año y mes (abreviado).
- `TI`: Título del artículo.
- `JT`: Título de la revista donde se publicó el artículo.
    

## Análisis de los datos

**Datos de Entrada**

Disponemos de varios archivos que contienen referencias en formato PubMed para diferentes regulones. Cada archivo tiene múltiples referencias, y una nueva referencia comienza con el campo PMID, seguido por una línea en blanco que separa las referencias.

Archivos de ejemplo:

```
- AraC_references_pubmed.txt
- CRP_references_pubmed.txt
- LexA_references_pubmed.txt
- MicF_references_pubmed.txt
```



**Instrucciones**

0. **Estructura del Proyecto**.   
    Genera la estructura para organizar el proyecto, siguiendo las buenas prácticas. Recuerda que los nombres de archivos no deben llevar espacios en blanco, ni caracteres especiales como acentos, y el nombre del archivo debe estar relacionado con el contenido.

1. **Conteo de referencias por regulón**.  
    Queremos contar cuántas referencias hay en cada archivo, lo cual se puede hacer buscando cuántos campos PMID hay por regulón.

2. **Distribución de publicaciones a lo largo de los años**.  
    Para cada regulón, nos interesa conocer la distribución de las publicaciones a lo largo de los años (sin importar los meses). Esto se obtiene a partir del campo DP.

3. **Frecuencia de publicación en diferentes revistas**.  
    Deseamos conocer en qué revistas se ha publicado con más frecuencia, para cada regulón. Este análisis se hace a partir del campo JT. Al final, se debe mostrar también una distribución global combinando todos los regulones.

4. **Extracción de títulos de publicaciones**.  
    Finalmente, queremos extraer todos los títulos de las publicaciones (campo TI) para cada regulón y guardarlos en un archivo separado por regulón.



### Extra

 



