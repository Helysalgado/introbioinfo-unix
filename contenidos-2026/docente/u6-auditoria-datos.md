# Unidad 6 — Auditoría de los datos y su función narrativa

> **NOTA:** Documento **docente**, no material para el estudiante. Responde a lo que exige
> `prompts-ia/arquitectura-pedagogica-unidad-6.md` §15: *«Antes de construir las sesiones deberá
> documentarse con precisión qué representa cada archivo y cuál será su función pedagógica»*.
>
> Todo lo que sigue está **verificado sobre los archivos reales** de
> [`ejemplos/datos-alineamientos/`](../ejemplos/datos-alineamientos/): número de secuencias, organismos, longitudes y
> tipo de molécula se comprobaron leyendo los archivos, no se dan por supuestos.

---

## 1. Resumen

31 archivos, 216 KB. Tres conjuntos con funciones narrativas distintas:

| Conjunto | Archivos | Qué es | Para qué sirve en la unidad |
| --- | --- | --- | --- |
| **A · `ubiE` en Rickettsiales** | 12 | Un gen, en pares y grupos de distancia evolutiva creciente | Comparar y alinear (el gradiente que motiva los gaps) |
| **B · tres familias × 19 organismos** | 6 | `ubiE`, `era` y `hemE` en los mismos 19 organismos | Construir una base local y buscar en ella |
| **C · globinas de vertebrados** | 15 | 15 proteínas RefSeq: α, β y ζ en 9 especies | Ortología, paralogía y transferencia de función |

Cada conjunto viene en **dos versiones paralelas** cuando aplica: `.fna` (nucleótido) y `.faa`
(proteína). Eso permite una comparación que la arquitectura pide explícitamente: **la misma pregunta
sobre DNA y sobre proteína**, y por qué no dan lo mismo.

---

## 2. Conjunto A — la familia `ubiE` en Rickettsiales

`ubiE` codifica una metiltransferasa de la ruta de biosíntesis de ubiquinona/menaquinona. Los
archivos vienen anotados con un encabezado muy rico —identificador RefSeq, organismo, ensamblado,
gen, longitud, coordenadas, hebra y **genes vecinos**— lo que permite trabajar procedencia y contexto
genómico sin salir del archivo.

### 2.1 La consulta

| Archivo | Contenido | Longitud |
| --- | --- | --- |
| `ubiE_con.faa` / `.fna` | *Rickettsia conorii* str. Malish 7, `WP_010977615.1` | 248 aa / 747 nt |

Es **la secuencia consulta** de toda la unidad. Todo lo demás se compara contra ella.

### 2.2 Los tres pares: un gradiente de distancia evolutiva

Aquí está, en mi opinión, la mejor pieza del conjunto.

| Archivo | Pareja | Longitudes (aa) | Qué ocurre al alinear |
| --- | --- | --- | --- |
| `ubiE_con_afr` | *R. conorii* + *R. africae* | 248 y **248** | Misma longitud: **no hacen falta gaps** |
| `ubiE_con_typ` | *R. conorii* + *R. typhi* | 248 y 248 | Mismo género, otro grupo: más sustituciones |
| `ubiE_con_tsu` | *R. conorii* + *Orientia tsutsugamushi* | 248 y **257** | Distinta longitud: **aparecen los gaps** |

> **Por qué importa.** El estudiante empieza por el par que **no** necesita gaps y descubre que puede
> comparar posición por posición. Al llegar al par lejano, las secuencias ya no tienen la misma
> longitud y la comparación posicional se rompe: **el gap aparece porque el dato lo exige**, no porque
> la lección lo introduzca. Es exactamente el motor que pide la arquitectura (§10: «las herramientas
> aparecen únicamente cuando resuelven una limitación»).

### 2.3 Los grupos

| Archivo | Contenido |
| --- | --- |
| `ubiE_4_org.faa` / `.fna` | Los 4 organismos anteriores juntos: *R. conorii*, *R. typhi*, *R. africae*, *O. tsutsugamushi* |
| `ubiE_19_org.faa` / `.fna` | 19 organismos de Rickettsiales · proteínas de **230 a 257 aa** |

Los 19 organismos, por género:

| Género | n | Organismos |
| --- | ---: | --- |
| *Rickettsia* | 5 | conorii, africae, typhi, prowazekii, rickettsii |
| *Anaplasma* | 6 | capra, centrale, marginale, ovis, phagocytophilum, platys |
| *Ehrlichia* | 3 | canis, chaffeensis, ruminantium |
| *Wolbachia* | 2 | pipientis, endosymbiont of *Anopheles demeilloni* |
| *Orientia* | 1 | tsutsugamushi |
| *Neoehrlichia* | 1 | mikurensis |
| *Neorickettsia* | 1 | risticii |

> **Función narrativa.** El salto de 4 a 19 no es «más datos»: es un **cambio de pregunta**. Con 4
> organismos se comparan secuencias; con 19 aparece la estructura de la familia —qué posiciones se
> conservan en todo el grupo y cuáles varían por género—, que ninguna comparación por parejas
> contenía. Es el mismo movimiento de S26: *el conjunto admite preguntas que ningún elemento admite*.

---

## 3. Conjunto B — tres familias en los mismos 19 organismos

| Archivo | Familia | n | Longitudes (aa) |
| --- | --- | ---: | --- |
| `ubiE_19_org.faa` | `ubiE` — metiltransferasa | 19 | 230–257 |
| `6951_era.faa` | `era` — GTPasa ribosomal | 19 | 289–339 |
| `6960_hemE.faa` | `hemE` — uroporfirinógeno descarboxilasa | 19 | 312–350 |

**Verificado:** los tres archivos contienen **exactamente los mismos 19 organismos**. Eso no es
casualidad y tiene consecuencias pedagógicas importantes.

> **Función narrativa.** Tres familias × 19 organismos = **57 proteínas** con las que construir una
> base de datos local (`makeblastdb`). Y con ella, la pregunta que da sentido a BLAST: si busco
> `ubiE` de *R. conorii* en esa base, ¿aparecen solo las 19 de su familia? ¿Con qué diferencia
> respecto a `era` y `hemE`? Es un caso **controlado**: sabemos la respuesta correcta, así que el
> estudiante puede evaluar si las métricas de BLAST separan bien lo que debe separar.
>
> Y permite el matiz que la arquitectura pide en §12.3: qué pasa cuando dos familias comparten un
> dominio o un plegamiento, y por qué un hit no se descarta solo por tener otro nombre.

---

## 4. Conjunto C — globinas de vertebrados

15 proteínas de RefSeq, todas cortas (142–147 aa), en 9 especies:

| Cadena | Secuencias |
| --- | --- |
| **α (alfa)** | humano `NP_000508`, humano `NP_000549`, macaco ×2, vaca, ratón ×2, perro, pez cebra, *Xenopus* |
| **β (beta)** | chimpancé, ratón, perro |
| **ζ (zeta)** | humano, *Xenopus* |

Este conjunto es el que sostiene la parte más difícil de la unidad, y tiene **tres casos que valen
oro**:

### 4.1 Ortólogos: la misma cadena en especies distintas

α de humano, macaco, vaca, ratón, perro, pez cebra y *Xenopus*. Separadas por **especiación**, con
identidad decreciente conforme aumenta la distancia filogenética. El pez cebra y *Xenopus* son los
casos interesantes: identidad claramente menor y aun así homología sólida.

### 4.2 Parálogos: α, β y ζ en la misma especie

Humano tiene α, ζ; ratón tiene α y β; perro tiene α y β. Separadas por **duplicación génica**, no por
especiación. Y aquí está el punto que la arquitectura declara irrenunciable (§12.2 y S34): **α de
humano se parece más a α de ratón que a β de humano** — es decir, la similitud no sigue la frontera
de la especie, sino la de la historia del gen.

### 4.3 El regalo: dos identificadores, una sola proteína

> **`NP_000508` y `NP_000549` tienen secuencias idénticas** (verificado byte a byte). Son **HBA1 y
> HBA2**: dos genes humanos distintos, producto de una duplicación reciente, que codifican
> exactamente la misma proteína.

Es un caso de enseñanza inmejorable, y toca varios principios de la arquitectura a la vez:

- **100 % de identidad no significa «el mismo gen»** (§12.1);
- explica la **redundancia de las bases de datos** y por qué el «mejor hit» puede estar duplicado
  (§12.3);
- obliga a distinguir **secuencia, gen y entrada de base de datos**, que los estudiantes confunden;
- y es un parálogo con identidad máxima: el contraejemplo perfecto contra «más identidad = más
  cercano evolutivamente».

---

## 5. Lo que estos datos permiten hacer

| Pregunta de la arquitectura | Con qué datos se responde |
| --- | --- |
| ¿Qué aprendo al comparar esta secuencia con otra? | `ubiE_con` + los tres pares |
| ¿Por qué aparecen gaps? | `ubiE_con_tsu` (248 vs 257 aa) frente a `ubiE_con_afr` (248 vs 248) |
| ¿Identidad frente a similitud? | Pares de `ubiE`, en `.faa` y `.fna` |
| ¿Qué cambia entre DNA y proteína? | Los mismos pares en sus dos versiones |
| ¿Qué se conserva en toda una familia? | `ubiE_19_org` |
| ¿Cómo busco en una colección? | Base local con `ubiE` + `era` + `hemE` (57 proteínas) |
| ¿Separan bien las métricas de BLAST? | Buscar `ubiE_con` en esa base: la respuesta correcta se conoce |
| ¿Ortólogo o parálogo? | Globinas α/β/ζ en 9 especies |
| ¿Identidad alta implica misma historia? | `NP_000508` = `NP_000549` (HBA1/HBA2) |
| ¿Se puede transferir la anotación? | Globinas: α y ζ tienen funciones distintas y son muy similares |

---

## 6. Lo que falta o hay que decidir

| # | Asunto | Estado |
| --- | --- | --- |
| D1 | **Procedencia formal.** Los encabezados traen identificador RefSeq y ensamblado, pero no hay ficha con fecha de descarga ni versión de la base. La unidad la exige (§17). Propuesta: construirla **con los estudiantes** en S30, a partir de los propios encabezados — es un ejercicio de U3 aplicado | **Propuesta** |
| D2 | **Origen de los encabezados de `ubiE`/`era`/`hemE`.** El formato (`ID:…\|[organismo]\|…\|neighbours:…`) procede de una herramienta cuya referencia exacta no está localizada. En el material se describirá **el formato** —que es lo que el estudiante necesita para extraer campos con Unix— sin atribuirlo a una fuente concreta | **Pendiente, sin bloquear** |
| D3 | **Alineador: Clustal Omega, en el clúster.** Resuelto (ago-2026). Cubre el alineamiento múltiple de `ubiE_4_org` y `ubiE_19_org`. **Consecuencia de diseño:** para las parejas de S30 no se usará un alineador global por parejas —no hay EMBOSS decidido—, sino Clustal Omega sobre dos secuencias, que es equivalente para el propósito de la sesión. Conviene confirmar el nombre del ejecutable (`clustalo`) y su versión | **Resuelto** |
| D4 | **BLAST+ instalado**: `makeblastdb`, `blastn` y `blastp` disponibles. Resuelto (ago-2026) | **Resuelto** |
| D5 | **Ubicación final de los datos.** Ahora están en `contenidos-2026/ejemplos/datos-alineamientos/`. Para el estudiante deberían llegar a `data/source/` de su proyecto, con su ficha | **Propuesta** |
| D6 | **Los archivos `.fna` de globinas no existen** — el conjunto C es solo proteína. Es coherente (las globinas se comparan mejor como proteína), pero conviene decirlo en el material para que nadie los busque | **Resuelto: se declara** |

---

## 6.b Herramientas confirmadas

| Herramienta | Dónde | Qué cubre en la unidad |
| --- | --- | --- |
| **Clustal Omega** | Clúster `chaac` | Alineamiento por parejas y múltiple: los tres pares de `ubiE`, `ubiE_4_org`, `ubiE_19_org` y las globinas |
| **BLAST+** (`makeblastdb`, `blastn`, `blastp`) | Clúster `chaac` | Base local con las tres familias; búsquedas de nucleótido y de proteína |
| **Unix** (U4) | — | Extraer campos de los encabezados, filtrar la salida tabular de BLAST, resumir hits |
| **SGE** (U5, S29) | Clúster `chaac` | Las búsquedas y los alineamientos grandes se envían como trabajos |

> **NOTA — continuidad con U5.** Que todo viva en el mismo clúster no es un detalle logístico: es la
> primera vez que los estudiantes usan la infraestructura de S29 para una herramienta que **no
> escribieron ellos**. Conviene aprovecharlo explícitamente — el *job script* de S29 sirve igual para
> lanzar un BLAST.

---

## 7. Recomendación de reparto por sesión

Suponiendo la arquitectura de sesiones que se decida, los datos se reparten así de forma natural:

```text
Comparar / Alinear   →  ubiE_con · los tres pares · ubiE_4_org
                        (el gradiente de distancia; .faa y .fna)
        ↓
Buscar (BLAST)       →  base local con ubiE + era + hemE (57 proteínas)
                        consulta: ubiE_con
        ↓
Interpretar          →  hits de esa búsqueda · ubiE_19_org para el contexto de familia
        ↓
Inferir              →  globinas: α/β/ζ · ortólogos y parálogos · HBA1 = HBA2
        ↓
Defender             →  una secuencia "desconocida" tomada del conjunto sin decir cuál es
```

> **Sobre la última fila.** La evidencia integradora pide una *secuencia desconocida*. Se puede
> construir sin datos nuevos: entregar a cada equipo una secuencia del conjunto **con el encabezado
> eliminado**, y que tenga que averiguar qué es. Conviene preparar esas secuencias anonimizadas antes
> de la sesión y decidir cuáles: hay margen para dar casos de dificultad distinta —una `ubiE` de un
> género no visto, una globina de otra especie, algo con cobertura parcial—.
