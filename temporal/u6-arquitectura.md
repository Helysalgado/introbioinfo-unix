# Unidad 6 — Arquitectura de la unidad (documento de diseño)

**Comparación de secuencias y homología** · Sesiones **S27–S28** · Competencia **F**

> **NOTA:** Este documento **no es material para el estudiante**. Es el diseño previo de la Unidad 6:
> hilo conductor, propuesta de sesiones, matriz de evolución de las preguntas biológicas y evidencia
> integradora. Una vez aprobado, cada sesión se redactará como módulo autocontenido
> (`u6-sNN-<nombre>.md`) siguiendo `contenidos-2026/plantilla-unidad.md` y las convenciones de
> `contenidos-2026/README.md`.

> **IMPORTANTE — orden de las unidades.** Esta unidad va **después** de la Unidad 5 (*Automatización
> y scripting bioinformático*), como fija el Programa 2026. La decisión es deliberada y tiene una
> consecuencia de diseño muy fuerte: cuando el estudiante llega aquí **ya sabe escribir ciclos**, de
> modo que la comparación masiva de secuencias deja de ser una promesa y se vuelve una práctica real
> desde el primer día de la unidad. Ver §1.3.

---

## 1. Visión general de la unidad

### 1.1 Hilo conductor

**La Unidad 6 saca al genoma de su aislamiento.**

Durante la Unidad 4 el estudiante respondió una sola pregunta, cada vez mejor:

> *¿Qué puedo afirmar sobre este genoma a partir de la evidencia contenida en sus archivos?*

En la Unidad 5 aprendió a **repetir** ese razonamiento sin repetirse: a separar el procedimiento de
sus datos y a aplicarlo a muchos objetos a la vez. Pero en ninguna de las dos unidades salió de sus
propios archivos. Al terminar S26 sabe cuántos genes tiene su genoma, cuánto miden, cómo se agrupan
en regulones y cómo procesarlos por lotes —y **sigue sin saber qué es** ninguno de ellos.

La Unidad 6 se construye alrededor de una pregunta nueva:

> **¿Qué puedo afirmar sobre un gen comparándolo con el resto de la vida?**

De ella se desprende un conjunto pequeño y estable de preguntas:

- ¿Se parecen estas dos secuencias, y cuánto?
- ¿Existe algo parecido a mi gen en otros organismos?
- ¿Ese parecido significa que comparten un ancestro?
- Si lo comparten, ¿qué tipo de relación es?
- ¿Qué puedo afirmar de la función de mi gen a partir de eso, y qué no?

### 1.2 La distinción que gobierna toda la unidad

Cada unidad del curso tiene una distinción rectora. En U4 fue *un registro no es un objeto
biológico*; en U5, *un comando resuelve un caso y un script resuelve una clase de casos*. En U6 es
esta:

```text
LA SIMILITUD SE MIDE          LA HOMOLOGÍA SE INFIERE
es una observación            es una hipótesis sobre el pasado
es continua: 34 %, 78 %       es binaria: comparten ancestro o no
se calcula                    se argumenta
está en el alineamiento       no está en ningún archivo
```

De ahí se sigue todo lo demás. **No existe «un 80 % de homología»**: existe un 80 % de identidad, que
es evidencia a favor de una hipótesis de homología. Un alineamiento no descubre parentescos: produce
un número que sostiene, o no, una afirmación evolutiva que hace el investigador.

Esa distinción es la misma operación intelectual que el estudiante practicó en S21 —separar el dato
de la interpretación— aplicada a un objeto nuevo. El material debe hacer ese paralelismo explícito:
no es un tema nuevo, es la misma disciplina sobre otra evidencia.

### 1.3 Lo que cambia por venir después de la Unidad 5

Este es el punto de diseño más importante de la unidad, y conviene explotarlo a fondo.

| Si U6 fuera antes de scripting | Como está: U6 después de U5 |
| --- | --- |
| Una búsqueda, hecha a mano, sobre un gen elegido | **Muchas búsquedas**, con un ciclo, sobre un conjunto con sentido biológico |
| El «BLAST masivo» se menciona como algo que se hace en la vida real | El BLAST masivo **se ejecuta en clase**, y conecta con el trabajo en clúster de S6 |
| La reproducibilidad se declara en prosa | La búsqueda **es** un script con parámetros: la reproducibilidad es el archivo |
| El mejor acierto recíproco se explica con un diagrama | El criterio recíproco **se calcula**: dos búsquedas y una comparación de listas |
| Los umbrales se fijan una vez | Se puede **repetir la búsqueda con otro umbral** y ver cuánto cambia la conclusión |

La consecuencia práctica: **la sensibilidad de una conclusión a sus parámetros deja de ser un
discurso y se vuelve un experimento**. Ese es el mejor argumento a favor de este orden, y el material
debe usarlo, no desaprovecharlo.

> **ADVERTENCIA — el riesgo del orden.** Con la máquina ya disponible, la tentación es que la unidad
> se convierta en un ejercicio de programación con secuencias de fondo. El criterio es firme: **el
> ciclo es infraestructura, no contenido**. Ninguna sesión de U6 enseña una construcción de shell
> nueva; todas usan las de U5. Lo que se evalúa aquí es la interpretación biológica.

### 1.4 Cambio de paradigma respecto a las unidades anteriores

| Dimensión | U4 (un genoma) | U5 (automatizar) | U6 (comparar) |
| --- | --- | --- | --- |
| Objeto | Un archivo y sus registros | Un procedimiento | Una secuencia y su parecido con otras |
| Pregunta | ¿Qué contiene y cuánto mide? | ¿Cómo lo repito sin repetirme? | ¿Con qué se parece y qué significa? |
| Resultado | Descriptivo | Operativo | **Inferencial**: una hipótesis sobre el pasado |
| Fuente | Archivos propios, verificados | Los mismos, en lote | Una base de datos que **no controlas**, con su sesgo |
| Naturaleza del error | La estrategia de conteo era incorrecta | El script hizo algo distinto de lo que creías | El parecido era real y la conclusión evolutiva, no |
| El azar | No participaba | No participaba | Participa: hay parecidos que se explican por casualidad |

Hay un cambio adicional, y es el más difícil: hasta ahora **todo resultado era comprobable dentro de
los archivos**. En U6 aparece una clase de afirmación que **ningún comando puede validar**: que dos
secuencias descienden de un ancestro común. Aprender a sostener ese tipo de afirmación —con
evidencia, con grado de confianza y con sus límites— es el núcleo formativo de la unidad, y lo que
la hace apropiada como cierre del curso.

### 1.5 Los cuatro principios transversales, en esta unidad

- **Reproducibilidad:** una búsqueda no es reproducible sin declarar programa, base de datos,
  **versión de la base**, fecha y parámetros. Una base crece cada día: la misma consulta mañana da
  otro resultado, y eso no es un fallo. Con U5 ya cursada, esa declaración vive en el script.
- **Verificación:** todo acierto se lee con tres números a la vez —identidad, cobertura y
  significancia—, nunca con uno solo.
- **Validación:** una hipótesis de homología se sostiene mejor si sobrevive a un criterio recíproco,
  a un cambio de base de datos o a una comparación en el espacio de proteínas.
- **Robustez:** se identifica qué rompería la conclusión —una región de baja complejidad, un dominio
  compartido, una base sesgada hacia un taxón, un umbral elegido a conveniencia—. Aquí **se prueba**,
  volviendo a correr el script con otro valor.

### 1.6 Principios de diseño de la unidad

1. **Ninguna sesión se llama como una herramienta.** Se nombran por la etapa del razonamiento: medir,
   inferir. `BLAST` aparece dentro de la primera porque resuelve una limitación del alineamiento por
   pares.
2. **El algoritmo se enseña hasta donde explica el resultado, y ni un paso más.** El estudiante debe
   entender por qué un alineamiento óptimo depende del sistema de puntaje y por qué BLAST es una
   heurística que puede no encontrarlo. No debe programar Needleman–Wunsch.
3. **Ninguna construcción de shell nueva.** Variables, `$(...)`, `for` y redirecciones vienen de U5 y
   se usan tal cual (§1.3).
4. **Toda actividad termina en interpretación biológica** y en una **declaración de confianza**: qué
   afirmo, con qué evidencia y qué haría falta para estar seguro.
5. **Las secuencias consultadas salen del proyecto propio.** No se usan ejemplos de catálogo: los
   genes que se comparan son los que el estudiante inventarió en U4 y agrupó en U5.
6. **Datos originales intactos.** Los resultados se escriben en `results/` con su ficha; la base
   consultada se documenta como entrada externa, igual que la tabla de S21.

---

## 2. Propuesta de sesiones

La unidad ocupa **dos sesiones de 2 h**: **S27–S28**. A continuación viene S29 (Examen práctico 2,
competencias D, E y F) y S30 (presentación del proyecto integrador).

```text
U6 — De describir un genoma a situarlo entre otros

S27 Medir el parecido   →  ¿cuánto se parecen, y a qué?      alineamiento · identidad · cobertura · BLAST
S28 Inferir la historia →  ¿qué significa ese parecido?      homología · ortología · límites · escala
                              ↓
        Reporte de una búsqueda con su interpretación argumentada
```

> **IMPORTANTE — dos sesiones son pocas.** El Programa asigna a esta unidad más contenido del que
> cabe holgadamente en cuatro horas de aula. Las medidas de contención están en §5.2 y deben
> aplicarse desde el diseño, no improvisarse en clase.

---

### S27 — Medir el parecido: del alineamiento a la búsqueda

**[Plan: alineamientos y BLAST · Comp. F]**

- **Propósito.** Establecer qué se mide exactamente cuando se dice que dos secuencias «se parecen», y
  convertir esa medición en una **búsqueda** contra una colección.
- **Preguntas biológicas que responde.**
  - ¿En qué se diferencian estas dos secuencias, y de qué tipo son esas diferencias?
  - ¿Cuánto se parecen? ¿Es lo mismo identidad que similitud? ¿Sobre qué fracción?
  - ¿Existe algo parecido a mi gen fuera de mi genoma, y dónde?
  - ¿Cuáles de esos parecidos son mejores de lo que esperaría por azar?
- **Conceptos nuevos.**
  - *Bloque A — el alineamiento.* Coincidencia, sustitución, inserción y deleción, brecha; identidad,
    similitud y **cobertura**; global frente a local; sistema de puntaje y penalización de brechas;
    alineamiento múltiple (conceptual: qué es y para qué, sin ejecutarlo).
  - *Bloque B — la búsqueda.* BLAST como **heurística**: rápida, no exhaustiva, sin garantía de
    encontrar el alineamiento óptimo. Elección de programa según el tipo de secuencia. Elección y
    **versión** de la base. Lectura de la tabla: identidad, longitud del alineamiento, cobertura,
    *bit score* y **valor E**, con su dependencia del tamaño de la base.
- **Herramientas.** Alineamientos pequeños a mano o con un visualizador, y una matriz de puntos como
  representación gráfica. Después, `blastn`/`blastp` con salida tabular (`-outfmt 6`), procesada con
  `cut`, `sort` y `awk` de U4. Material clásico de referencia: `alineamientos` y
  `blast_var_for_scripts` —de este último, **solo la parte de BLAST**; las variables y los scripts ya
  se vieron en U5—.
- **Limitación que resuelve.** «Parecerse» era una impresión; aquí se vuelve tres cantidades que hay
  que reportar juntas, y deja de exigir tener el candidato de antemano.
- **Evolución de la capacidad analítica.** De «estas dos secuencias son parecidas» a «**comparten un
  78 % de identidad sobre el 40 % de la longitud de la consulta, con un valor E de 3e-52 en esta base
  y esta versión**».
- **Limitación con la que cierra (motor de S28).** La lista de aciertos está ordenada por
  significancia estadística, y eso **no es un orden evolutivo**: el mejor acierto no es
  necesariamente el pariente más cercano, y ningún número de la tabla dice qué tipo de relación hay.
- **Actualización del protocolo.** Sección *Búsqueda de similitud*: ficha de la base —nombre,
  versión, fecha, tamaño—, programa, parámetros, umbrales **y su justificación**, y la tabla de
  aciertos conservados.
- **Riesgo didáctico principal.** Que la sesión se convierta en un tutorial de la interfaz de NCBI, o
  en un ejercicio de programación dinámica. El algoritmo se presenta para explicar **por qué no hay
  un alineamiento único**; la interfaz, lo justo para obtener el resultado. El contenido es **cómo se
  lee**.

---

### S28 — Inferir la historia: de la similitud a la homología, y a escala

**[Plan: homología y ciclos · Comp. E, F · nota del Plan: «BLAST masivo → conexión con HPC (S6)»]**

- **Propósito.** Dar el paso que ningún programa da —convertir una medida de parecido en una
  **hipótesis sobre el pasado**— y comprobar que ese razonamiento **resiste la escala**.
- **Preguntas biológicas que responde.**
  - ¿Este parecido se explica mejor por ancestría común o por azar y convergencia?
  - Si hay ancestría común, ¿la relación es de ortología, paralogía o transferencia horizontal?
  - ¿Puedo transferir la función anotada del acierto a mi gen? ¿Con qué riesgo?
  - ¿Se sostiene la misma conclusión para todo un conjunto de genes, o solo para el que elegí?
- **Conceptos nuevos.** Homólogo como categoría binaria; ortólogos y parálogos según especiación o
  duplicación; xenólogos y transferencia horizontal; **mejor acierto recíproco** como heurística —no
  como prueba—; transferencia de anotación y propagación de errores; sensibilidad de la conclusión al
  umbral elegido.
- **Herramientas.** Ninguna nueva de shell: BLAST en las dos direcciones, un `for` de U5 para
  recorrer un conjunto de consultas, y `comm`/`sort`/`awk` de U4 para cruzar las dos listas de
  aciertos —que es exactamente la operación de S21 sobre un objeto nuevo—.
- **Limitación que resuelve.** Un resultado de similitud, por bueno que sea, no es una conclusión
  biológica hasta que alguien declara qué relación propone y con qué evidencia. Y una conclusión
  basada en un solo gen no dice si el patrón es general.
- **Evolución de la capacidad analítica.** De «encontré un acierto con valor E de 1e-90» a
  «**propongo que estos dos genes son ortólogos, sostenido por estas tres evidencias, este es mi
  grado de confianza, y esto es lo que aún no puedo descartar**» —y, además, «este es el porcentaje
  del conjunto para el que la afirmación se sostiene».
- **Cierre del curso.** No abre una unidad nueva: cierra el arco. La última limitación que se enuncia
  es la honesta —**la homología no se demuestra con una búsqueda, se sostiene con evidencia
  convergente**— y queda como puerta hacia filogenia, que este curso no cubre.
- **Actualización del protocolo.** Sección *Inferencia de homología*: hipótesis por acierto
  conservado, evidencia a favor, alternativas abiertas, grado de confianza y evidencia pendiente, con
  el mismo formato de tabla fijado en S21.
- **Riesgo didáctico principal.** Que el estudiante salga creyendo que el mejor acierto define la
  función. Es el error más extendido de la bioinformática aplicada, y esta sesión existe en buena
  medida para prevenirlo.

---

## 2.b El ciclo de la evidencia, aplicado a una búsqueda

La Unidad 4 dejó instalado un ciclo de seis verbos. **No se sustituye: se aplica a un objeto nuevo**,
un acierto de búsqueda. Conviene hacerlo explícito, porque es lo que impide que la unidad se lea como
un tema desconectado del resto del curso.

| Verbo del ciclo | En U4 (un archivo) | En U6 (una búsqueda) |
| --- | --- | --- |
| **Seleccionar** | Qué líneas cuentan | Qué aciertos superan el umbral, y por qué ese umbral |
| **Identificar** | De qué objeto habla cada línea | Qué es cada acierto: organismo, gen, proteína, versión |
| **Normalizar** | Bajo qué forma se compara | Qué espacio de comparación: nucleótidos o aminoácidos |
| **Confrontar** | Contra una fuente ajena | Contra la búsqueda recíproca, u otra base de datos |
| **Cuantificar** | Cuánto mide, en qué proporción | Identidad, cobertura y significancia, leídas juntas |
| **Integrar** | El protocolo ejecutable | El reporte de la búsqueda, con su interpretación |

Cada sesión de U6 incluye la banda **«Tu lugar en el ciclo de la evidencia»** ya usada en S18–S23.
El estudiante debe reconocer que está haciendo lo mismo que ya sabe hacer, sobre datos que no
controla.

---

## 3. Matriz de evolución de las preguntas *(eje de diseño de la unidad)*

| # | Pregunta biológica | Primera aparición | Estrategia inicial y su límite | Cómo se refina | Queda resuelta en |
| --- | --- | --- | --- | --- | --- |
| Q1 | ¿Se parecen estas dos secuencias? | S27 | Inspección visual: impresión no cuantificable | **S27 · alineamiento**: identidad, similitud y cobertura, con su sistema de puntaje declarado | S27 |
| Q2 | ¿Cuánto de mi secuencia participa en el parecido? | S27 | Se ignora: solo se mira el porcentaje de identidad | **S27 · cobertura**: un 95 % de identidad sobre el 5 % de la secuencia no es un parecido | S27 |
| Q3 | ¿Existe algo parecido a mi gen? | S27 | No se podía responder sin tener el candidato | **S27 · BLAST**: búsqueda heurística contra una colección | S27 |
| Q4 | ¿Este acierto es mejor que el azar? | S27 | Confiar en el porcentaje de identidad | **S27 · valor E**, con su dependencia del tamaño de la base | S27 |
| Q5 | ¿Qué base de datos responde mi pregunta? | S27 | Usar la que aparece por defecto | **S27 · elección y ficha de la base**: alcance, sesgo taxonómico, versión | S27 |
| Q6 | ¿Comparten un ancestro común? | S28 | Suponerlo a partir del parecido | **S28 · hipótesis de homología** con evidencia, alternativas y confianza | S28 (provisional por naturaleza) |
| Q7 | ¿Qué tipo de relación es? | S28 | «Son homólogos», sin más | **S28 · ortología, paralogía, xenología** según el evento que los separó | S28 |
| Q8 | ¿Puedo asumir que hacen lo mismo? | S28 | Transferir la función del mejor acierto | **S28 · límites de la transferencia por similitud** y propagación de errores | No se resuelve: **se delimita** |
| Q9 | ¿Se sostiene para todos mis genes, o solo para el que elegí? | S28 | Generalizar desde un caso | **S28 · el mismo análisis en lote**, con el `for` de U5 | S28 |
| Q10 | ¿Cuánto depende mi conclusión del umbral? | S28 | El umbral se elige una vez y no se cuestiona | **S28 · repetir con otro valor** y medir cuánto cambia | S28 |

> **Criterio de diseño.** Q9 y Q10 solo existen porque la Unidad 5 va antes. Son la ganancia neta de
> este orden y deben aparecer explícitamente en el material, no darse por supuestas.

---

## 4. Evidencia integradora: el reporte de la búsqueda

El producto es el que fija el Programa: **un reporte breve de una búsqueda BLAST que documente sus
parámetros y justifique la interpretación de similitud y homología**. Se construye por acumulación y
se integra al `doc/protocolo.md` del proyecto.

| Sesión | Sección que añade | Contenido mínimo |
| --- | --- | --- |
| S27 | *Comparación y búsqueda* | Qué se comparó y por qué; tipo de alineamiento; identidad, similitud y cobertura; ficha de la base (nombre, versión, fecha, tamaño); programa, parámetros y umbrales **con su justificación**; tabla de aciertos conservados |
| S28 | *Inferencia de homología* | Hipótesis por acierto, evidencia a favor, alternativas abiertas, grado de confianza, evidencia pendiente, límites de la transferencia funcional y resultado del análisis en lote |

La tabla de hipótesis reutiliza **exactamente** el formato fijado en S21, lo que refuerza que la
disciplina no cambia aunque cambie el objeto:

| Acierto | Hipótesis principal | Evidencia a favor | Alternativas abiertas | Confianza | Evidencia pendiente |
| --- | --- | --- | --- | --- | --- |

> **NOTA — el script de la búsqueda es parte de la evidencia.** Como U5 va antes, el reporte incluye
> `src/buscar-homologos.sh` con sus parámetros. La reproducibilidad deja de ser una promesa escrita
> en prosa y pasa a ser un archivo que otra persona ejecuta.

---

## 5. Alcance, delimitaciones y discrepancias

### 5.1 Cobertura del alcance oficial

| Contenido del Programa | Sesión |
| --- | --- |
| Alineamientos de pares | S27 |
| Alineamientos múltiples | S27 (**conceptual**: qué son y para qué; no se ejecutan) |
| Coincidencia, sustitución, inserción/deleción, brecha | S27 |
| Identidad, similitud y cobertura | S27, aplicadas en S28 |
| Principios, modalidades y uso básico de BLAST | S27 |
| Selección de base de datos | S27 |
| Lectura crítica de resultados | S27, profundizada en S28 |
| Homólogos, ortólogos, parálogos, xenólogos | S28 |
| Duplicación y especiación | S28 |
| Limitaciones de las búsquedas de similitud | Transversal; se cierra en S28 |
| **Evidencia integradora: reporte de una búsqueda BLAST** | S28 (iniciada en S27) |

### 5.2 Medidas de contención por el tamaño de la unidad

Dos sesiones para todo lo anterior es ajustado. Estas decisiones deben tomarse en el diseño:

1. **Aula invertida reforzada.** La parte conceptual de S27 —tipos de mutación, reloj molecular,
   matriz de puntos, por qué no hay un alineamiento único— se lee **antes** de clase. El aula se
   dedica a medir e interpretar, no a exponer.
2. **Alineamiento múltiple, solo conceptual.** Se explica qué responde y por qué es distinto de un
   alineamiento por pares; no se ejecuta ninguno.
3. **Needleman–Wunsch como explicación, no como ejercicio.** Se usa para justificar que el puntaje
   decide el resultado. No se llena una matriz celda por celda.
4. **El reporte se termina fuera del aula.** S28 produce la tabla de hipótesis y la evidencia; la
   redacción final es trabajo de casa, con rúbrica.
5. **El conjunto de consultas se prepara en U5.** El archivo de secuencias que se buscará en lote sale
   del trabajo de S26: llega hecho, no se construye en S28.

> **ADVERTENCIA.** Si tras el pilotaje S27 se desborda, la partida a sacrificar es la profundidad
> algorítmica, **nunca** la lectura crítica de resultados ni la distinción similitud/homología: son
> las que se evalúan en S29 y las que sostienen el proyecto integrador.

### 5.3 Delimitación con otras unidades

**No se desarrollan en U6:** construcción de árboles filogenéticos; modelos de sustitución;
alineamiento de genomas completos; ensamblado; predicción estructural. Tampoco ninguna construcción
de shell nueva: todo lo que se usa viene de la Unidad 5.

> **NOTA — el reloj molecular.** El material clásico abre con reloj molecular y ancestro común. Es
> buen encuadre para S27, pero debe presentarse como **supuesto con condiciones**, no como ley: la
> tasa de cambio no es uniforme entre linajes ni entre sitios. Enunciarlo sin matiz contradice el
> criterio de honestidad epistemológica del curso.

### 5.4 Discrepancias con el Plan operativo

| # | Plan de clases | Esta arquitectura | Estado |
| --- | --- | --- | --- |
| **D1** | S24 «Alineamientos», S25 «BLAST, variables y scripts» y S26 «Homología y ciclos» reparten U5 y U6 en sesiones **compartidas** | Se separan en **bloques limpios**: U5 ocupa S24–S26 y U6 ocupa S27–S28. Ninguna sesión sirve a dos hilos | **Decisión docente (ago-2026).** Motivo: dar a scripting tres sesiones seguidas de práctica |
| **D2** | S27–S28 figuran como «Semana de práctica: automatización de un pipeline» | Esa práctica se integra en U5 (S26) y en el trabajo en lote de S28. S27–S28 pasan a ser la Unidad 6 | Consecuencia de D1 |
| **D3** | U6 dispondría de tres sesiones (S24, S25, S26 parciales) | Dispone de **dos completas**. El cómputo de horas efectivas es similar, pero el contenido debe contenerse (§5.2) | **Riesgo asumido.** Requiere pilotaje |
| **D4** | S29 (Examen práctico 2) evalúa competencias D, E y F | La competencia F se cubre **íntegramente en S27–S28**, con una sola sesión de margen antes del examen | **Riesgo real.** Conviene que S28 termine con una autoevaluación diagnóstica |
| **D5** | El Plan sugiere `blastn` | Para genes codificantes, la comparación en el **espacio de proteínas** es más sensible a homología lejana. Se propone `blastp` como caso principal y `blastn` para regiones no codificantes, declarando el criterio | Propuesta; requiere visto bueno |
| **D6** | El material clásico usa TP53 humano como ejemplo | El curso trabaja con **genomas bacterianos**. La secuencia consultada debe salir del proyecto del estudiante (§1.6.5). TP53 puede conservarse como ejemplo de clase para ilustrar paralogía en una familia génica | Propuesta |

### 5.5 Decisión pendiente: dónde se ejecuta BLAST

| Vía | A favor | En contra |
| --- | --- | --- |
| **BLAST web (NCBI)** | Sin instalación; muestra el gráfico de aciertos y la alineación; restringir por taxón es trivial | Difícil de documentar de forma reproducible; **no se puede meter en un ciclo**, que es media unidad |
| **BLAST en línea de comandos** | Salida tabular procesable; parámetros explícitos y registrables; **es la única vía compatible con S28** | Requiere instalación o clúster, y descargar o construir la base con `makeblastdb` |

**Propuesta:** la web solo para **aprender a leer** un resultado en la primera media hora de S27; la
línea de comandos para todo lo demás. Con U5 ya cursada, la vía de comandos no es un obstáculo
añadido: es la continuación natural. Esto **obliga** a resolver la infraestructura (clúster o base
local) antes de S27, y conecta con el trabajo en clúster de S6, como anota el propio Plan.

### 5.6 Riesgos técnicos que el material debe prevenir

Son los errores que más se propagan en la práctica profesional. Cada uno debe tener su lugar:

| Riesgo | Dónde se previene |
| --- | --- |
| Decir «80 % de homología» | S27 y S28, como distinción rectora de la unidad |
| Leer la identidad sin la cobertura | S27, con un caso construido: identidad alta sobre un fragmento mínimo |
| Interpretar el valor E sin su base de datos | S27: el mismo acierto cambia de valor E al cambiar de base |
| Suponer que BLAST encuentra siempre el mejor alineamiento posible | S27, al presentarlo como heurística |
| Aciertos espurios por regiones de baja complejidad | S27, al hablar de filtros |
| Tomar el número de aciertos como medida de conservación | S27: depende del contenido de la base, no del gen |
| Confundir similitud por dominio compartido con homología de genes completos | S27 (cobertura) y S28 (interpretación) |
| Tomar el mejor acierto como el ortólogo | S28, con el criterio recíproco como contraste |
| Transferir la función anotada sin más | S28, conectado con las discrepancias de anotación vistas en S21 |
| Generalizar de un gen a todo el genoma | S28, con el análisis en lote (Q9) |
| Elegir el umbral que produce el resultado deseado | S28, repitiendo el análisis con otro valor (Q10) |

---

## 6. Verificación de esta arquitectura

- [ ] S27 cierra con una limitación concreta que S28 resuelve, y S28 cierra el curso sin prometer una
      unidad que no existe.
- [ ] La distinción **similitud medida / homología inferida** aparece en las dos sesiones.
- [ ] Ninguna sesión se titula con el nombre de una herramienta.
- [ ] **Ninguna construcción de shell nueva**: todo viene de U5.
- [ ] Cada sesión incluye la banda **«Tu lugar en el ciclo de la evidencia»**.
- [ ] Las secuencias consultadas proceden del proyecto del estudiante.
- [ ] Toda búsqueda queda documentada con base de datos, **versión**, fecha y parámetros, dentro de un
      script.
- [ ] Los tres números —identidad, cobertura, significancia— se leen siempre juntos.
- [ ] Las hipótesis de homología usan la tabla de S21.
- [ ] Cada sesión termina en interpretación biológica y en una declaración de lo que **no** puede
      afirmarse.
- [ ] Las medidas de contención de §5.2 están aplicadas en el guion de cada sesión.
- [ ] Español claro para primer semestre; glosario español–inglés en cada módulo.
- [ ] Toda buena práctica y toda definición citan su fuente.

---

## 7. Archivos de la unidad

| Sesión | Archivo previsto | Tema del nombre |
| --- | --- | --- |
| — (portada) | `u6-comparacion-secuencias-homologia.md` | Portada de la unidad |
| S27 | `u6-s27-medir-parecido-secuencias.md` | Qué mide un alineamiento y cómo se busca |
| S28 | `u6-s28-similitud-a-homologia.md` | De la similitud a la relación evolutiva |
| — (docente) | `u6-arquitectura.md` | Este documento |

Figuras previstas, en el estilo SVG del curso (paleta y tipografía de U4):

| Figura | Contenido | Sesión |
| --- | --- | --- |
| 27.1 | Los cuatro sucesos de un alineamiento: coincidencia, sustitución, inserción, deleción | S27 |
| 27.2 | Identidad, similitud y cobertura sobre el mismo alineamiento: tres números distintos | S27 |
| 27.3 | Global frente a local: la misma pareja, dos preguntas distintas | S27 |
| 27.4 | Anatomía de una tabla de aciertos: qué dice cada columna y cuál se olvida | S27 |
| 28.1 | Duplicación y especiación: de dónde salen ortólogos y parálogos | S28 |
| 28.2 | Similitud medida frente a homología inferida: la frontera de la unidad | S28 |
| 28.3 | Mejor acierto recíproco: dos búsquedas, dos listas, una intersección | S28 |

---

## 8. Siguiente paso

1. **Visto bueno de las discrepancias** D1 a D6, en especial la compresión a dos sesiones (D3) y el
   margen de una sola sesión antes del examen práctico (D4).
2. **Resolver la infraestructura de BLAST** (§5.5) antes de redactar S27: es la decisión con más
   plazo de entrega, porque puede implicar clúster o descarga de bases.
3. **Elegir los genes de trabajo**: un locus con homólogos claros para el caso guiado, y un conjunto
   —idealmente un regulón del trabajo de U5— para el análisis en lote de S28.
4. **Redactar S27**, verificar contra la checklist de §6, pilotar el tiempo real y solo entonces
   redactar S28.
