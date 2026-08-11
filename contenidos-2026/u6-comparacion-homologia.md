# Unidad 6 — Comparar secuencias para construir hipótesis biológicas

> **NOTA — Cómo se estudia esta unidad.** La Unidad 6 es esta portada más **cinco módulos** de dos
> horas, **S30 a S34**. Cada uno se lee **antes** de su sesión, trae su primer intento, su taller y su
> entrega posterior. Esta portada te da la visión de conjunto: qué pregunta persigue la unidad, con
> qué datos, y qué se espera que sepas defender al terminar. Es también **el cierre del curso**.

## De qué trata esta unidad

Durante cinco unidades has aprendido a obtener datos, verificarlos, interrogarlos, automatizar el
análisis y ejecutarlo donde haga falta. Al cerrar la Unidad 5 tienes una herramienta que responde,
sobre cualquier colección de genomas, preguntas del tipo *cuántos genes hay* y *cómo se distribuyen*.

Y todas esas preguntas tienen algo en común: **se responden mirando tus propios archivos**.

Ahora aparece una que no:

> **Este gen, ¿existe en otros organismos? ¿Qué hace? ¿De dónde viene?**

No hay forma de responderla contando registros en tu GFF3. Hay que **salir de tus archivos y
comparar con el resto de la vida** — y esa comparación no devuelve una respuesta, devuelve
**evidencia que hay que interpretar**.

### La gran pregunta de la unidad

> **Tengo una secuencia cuya función o relación evolutiva quiero investigar. ¿Qué puedo inferir a
> partir de su comparación con otras secuencias, y qué evidencia necesito para sostener esa
> inferencia?**

De ella salen todos los conceptos de la unidad —alineamiento, identidad, similitud, cobertura, gaps,
BLAST, *E-value*, homología, ortología, paralogía— y ninguno aparece antes de que la pregunta lo
haga necesario.

### El cambio conceptual

En las unidades anteriores la pregunta era *¿cómo obtengo y proceso la evidencia?*. Aquí es otra:

```text
¿QUÉ SIGNIFICA la evidencia?
```

Y de ahí sale la distinción que gobierna la unidad entera:

```text
RESULTADO DE UNA HERRAMIENTA        ≠        CONCLUSIÓN BIOLÓGICA
```

Entre las dos hay un proceso de razonamiento: comprobar la calidad del dato, leer el alineamiento,
integrar varias métricas, considerar explicaciones alternativas, reconocer la incertidumbre y
declarar el alcance de lo que se afirma. **Ese proceso es el contenido de la unidad.**

### Por qué esto importa ahora más que nunca

Conviene decirlo sin rodeos. Hoy una inteligencia artificial puede proponerte un comando de BLAST,
explicarte los campos de la salida, señalarte cuál parece el mejor resultado y redactarte una
interpretación que suena impecable.

Lo que **no** puede hacer es decidir si esa interpretación está sustentada por **tus** datos. Eso
exige mirar la evidencia concreta que tienes delante, y es exactamente lo que esta unidad entrena.

> **La regla de la unidad.** **La IA puede proponer. Los datos deben demostrar. Tú debes argumentar.**

## Ficha de la unidad

| Elemento | Descripción |
| --- | --- |
| **Sesiones** | S30 a S34 · 2 h cada una · **cierre del curso** |
| **Competencia principal** | F. Comparación de secuencias y homología |
| **Competencias integradas** | C. Manejo de datos biológicos; D. Análisis; A. Trabajo reproducible; B. Entorno Unix y cómputo; G. Uso responsable de la IA |
| **Propósito** | Interpretar críticamente comparaciones de secuencias y resultados de BLAST para formular hipótesis biológicas fundamentadas, distinguiendo similitud observada, homología, transferencia de función, incertidumbre y límites de la evidencia |
| **Contribución al objetivo del curso** | Cierra el arco: de *obtener y procesar datos* a *interpretar evidencia y sostener una conclusión* |
| **Datos de trabajo** | La familia `ubiE` en Rickettsiales, dos familias más (`era`, `hemE`) en los mismos 19 organismos, y las globinas α/β/ζ de nueve vertebrados. Ver §«Los datos» |
| **Herramientas** | **Clustal Omega** y **BLAST+** (`makeblastdb`, `blastn`, `blastp`) en el clúster `chaac`; Unix (U4) para procesar salidas; SGE (S29) para lanzar las búsquedas |
| **Lectura obligatoria (con evidencia)** | Pearson (2013), *An Introduction to Sequence Similarity («Homology») Searching* (~60 min, evidencia en S32) |
| **Lectura de consulta** | Fitch (1970) sobre homología; Koonin (2005) sobre ortólogos y parálogos |
| **Evidencia integradora** | **Informe de investigación de una secuencia desconocida** (S34) |
| **Producto acumulativo** | `doc/protocolo.md`, que **no se reinicia**: añade su última sección |

> **IMPORTANTE — lo que esta unidad NO es.** No es un curso de BLAST. Al terminar no habrás
> memorizado opciones de línea de comandos ni umbrales mágicos de *E-value*. Habrás aprendido a mirar
> un conjunto de resultados y decir, con argumentos, **cuál es la mejor explicación de lo que se
> observa y qué haría falta para confirmarla**. Eso último no caduca; las opciones de un programa, sí.

## Resultados de aprendizaje de la unidad

Al finalizar la Unidad 6 podrás:

1. **Explicar** por qué una secuencia aislada aporta poca información biológica y qué se gana al
   compararla.
2. **Interpretar** un alineamiento como una **hipótesis de correspondencia** entre posiciones, y
   explicar por qué aparecen los gaps.
3. **Distinguir** identidad, similitud y cobertura, y explicar por qué ninguna basta por separado.
4. **Justificar** cuándo conviene un alineamiento global y cuándo uno local.
5. **Diseñar y ejecutar** una búsqueda BLAST reproducible, justificando programa, base de datos y
   parámetros.
6. **Explicar** por qué BLAST es heurístico y qué se sacrifica a cambio de la velocidad.
7. **Integrar** varias métricas y el contexto de la búsqueda para **jerarquizar** los resultados con
   argumentos, en vez de tomar el primero.
8. **Distinguir** similitud observada de **homología inferida**, y ortología de paralogía.
9. **Reconocer** los límites de la transferencia de función y formular explicaciones alternativas.
10. **Evaluar críticamente** una interpretación propuesta por una IA, señalando qué afirmaciones
    están sustentadas por los datos y cuáles no.
11. **Construir y defender** una hipótesis biológica declarando su evidencia, su incertidumbre y la
    evidencia adicional que haría falta.

> **NOTA — nivel real.** *Explicar*, *ejecutar* y *distinguir* se alcanzan plenamente. *Construir una
> hipótesis defendible* se alcanza en su versión inicial: con un caso, con datos acotados y con
> acompañamiento. Nadie termina primer semestre siendo capaz de resolver un caso abierto de anotación
> funcional — y decirlo forma parte de la honestidad que la unidad enseña.

## Ruta de la unidad

Cinco movimientos. Cada uno resuelve la limitación que dejó abierta el anterior.

```text
    una herramienta reproducible (U5)
            ↓
S30  COMPARAR y ALINEAR   ¿qué posiciones puedo comparar, y qué veo al hacerlo?
            ↓
S31  BUSCAR               ¿y si quiero compararla contra millones de secuencias?
            ↓
S32  INTERPRETAR          una lista de hits no es una conclusión
            ↓
S33  INFERIR              cuando la similitud no basta
            ↓
S34  INTEGRAR             de la evidencia a la hipótesis biológica
            ↓
    una hipótesis biológica argumentada
```

| Sesión | Módulo | Qué resuelve | Con qué limitación cierra |
| --- | --- | --- | --- |
| **S30** | `u6-s30-comparar-alinear.md` — *Comparar: una secuencia adquiere significado en contexto* | La comparación posicional explícita: qué se conserva, qué cambia y por qué hacen falta los gaps | Funciona con dos o veinte secuencias; no con millones |
| **S31** | `u6-s31-buscar-blast.md` — *Buscar: comparar contra una colección* | Una búsqueda reproducible en una base de datos, con su justificación | Devuelve muchos resultados; tenerlos no es saber cuáles importan |
| **S32** | `u6-s32-interpretar-inferir.md` — *Interpretar: una lista de hits no es una conclusión* | Integrar métricas y jerarquizar candidatos con argumentos | La evidencia ya está rankeada; falta decidir qué significa evolutivamente |
| **S33** | `u6-s33-defender-hipotesis.md` — *Inferir: cuando la similitud no basta* | Distinguir similitud de homología; ortología/paralogía; límites de la transferencia de función | Sabes inferir con límites; falta integrar todo en un caso completo |
| **S34** | `u6-s34-integrar-hipotesis.md` — *Integrar: de la evidencia a la hipótesis biológica* | Evidencia integradora: informe de una secuencia desconocida | — cierre del curso |

> **NOTA — sobre el número de sesiones.** La arquitectura pedagógica propuso seis etapas y el Plan
> ajustado tiene tres. Aquí se adoptan **cinco** (S30–S34): S30 fusiona *comparar*+*alinear*; S32–
> S34 separan *interpretar*, *inferir* e *integrar*. El cierre **no** introduce conceptos nuevos:
> demuestra que el estudiante puede integrar el arco. Queda registrado en la nota docente.

### Qué se hace en cada momento

| Momento | Qué leer | Qué intentar | Qué llevar / entregar | Tiempo estimado |
| --- | --- | --- | --- | ---: |
| **Antes de S30** | Portada + módulo S30 | Comparar dos secuencias a ojo y describir lo que ves | Descripción razonada, sin afirmar homología | 45 + 40 min |
| **S30** | — | Alinear los tres pares y el grupo de 19 | Alineamientos interpretados | 2 h |
| **Entre S30 y S31** | Pearson (2013), primera mitad | Formular la pregunta de búsqueda | Pregunta y estrategia escritas | 60 min |
| **S31** | Módulo S31 | Construir la base local y buscar | Búsqueda reproducible documentada | 2 h |
| **Entre S31 y S32** | Pearson (2013), segunda mitad | Procesar la salida tabular con Unix | Reporte de lectura (evidencia) | 90 min |
| **S32** | Módulo S32 | Jerarquizar hits; construir evidencia sin concluir de más | Tabla interpretada de candidatos | 2 h |
| **Entre S32 y S33** | Fitch (1970) o Koonin (2005) | Separar observación de inferencia | Tabla observación/inferencia | 90 min |
| **S33** | Módulo S33 | Inferir con límites (globinas; transferencia de función) | Sección de inferencia del protocolo | 2 h |
| **Entre S33 y S34** | Repaso del protocolo S30–S33 | Recibir la secuencia desconocida; formular la pregunta | Pregunta + inventario de evidencia | 60 min |
| **S34** | Módulo S34 | Integrar y defender el informe | **Evidencia integradora** | 2 h |

## Los datos: tres conjuntos, tres funciones

Los archivos están en [`ejemplos/datos-alineamientos/`](ejemplos/datos-alineamientos/) y su auditoría completa —qué
contiene cada uno y para qué sirve— está en [`docente/u6-auditoria-datos.md`](docente/u6-auditoria-datos.md).

| Conjunto | Qué es | Qué permite descubrir |
| --- | --- | --- |
| **`ubiE` en Rickettsiales** | Un gen en tres pares de distancia creciente, más grupos de 4 y de 19 organismos | Que la comparación posicional se rompe cuando las secuencias no miden lo mismo, y que una familia tiene posiciones que se conservan en todos sus miembros |
| **Tres familias × 19 organismos** | `ubiE`, `era` y `hemE` en los **mismos** 19 organismos | Una base de datos donde **la respuesta correcta se conoce**: se puede comprobar si las métricas separan lo que deben separar |
| **Globinas α/β/ζ** | 15 proteínas de 9 vertebrados | Que la similitud sigue la historia del gen y no la frontera de la especie: α humana se parece más a α de ratón que a β humana |

> **¿SABÍAS QUE?:** Dos de esos archivos —`NP_000508` y `NP_000549`— contienen **exactamente la misma
> secuencia**. Son HBA1 y HBA2: dos genes humanos distintos, nacidos de una duplicación reciente, que
> producen la misma proteína. Es el contraejemplo perfecto de una idea muy extendida y muy falsa:
> **100 % de identidad no significa «el mismo gen»**.

## Los seis principios de la unidad

No son advertencias sueltas: son las seis formas en que una interpretación de secuencias se
equivoca. Aparecen a lo largo de las cinco sesiones y se evalúan en el informe final.

### 1. La homología no es un porcentaje

Dos secuencias **son o no son** homólogas: comparten un ancestro común o no lo comparten. La
identidad y la similitud se miden en porcentaje; la homología es **una hipótesis sobre el pasado**.

> «Un 80 % de homología» no significa nada. Existe un 80 % de identidad, que es otra cosa.

### 2. La similitud no demuestra la misma función

Dos proteínas pueden compartir regiones muy conservadas y hacer cosas distintas. Las globinas α y ζ
de esta unidad son el ejemplo: muy similares, funciones que no coinciden.

### 3. El mejor hit no es automáticamente la mejor explicación

El primer resultado puede estar condicionado por la composición de la base de datos, por secuencias
redundantes, por anotaciones incompletas, por una cobertura parcial o por un dominio compartido entre
proteínas por lo demás distintas.

### 4. Una métrica aislada no basta

Una interpretación honesta integra:

```text
identidad + cobertura + E-value + score + región alineada
          + anotación + procedencia + contexto biológico
```

### 5. La ausencia de evidencia no es evidencia de ausencia

No encontrar un resultado puede deberse a distancia evolutiva, a una base de datos inadecuada, a una
secuencia demasiado corta, a parámetros poco sensibles… o a que la función sea realmente novedosa.
**Son explicaciones distintas y no se distinguen sin más evidencia.**

### 6. Una hipótesis declara sus límites

Toda interpretación separa cuatro cosas: qué se **observó**, qué se **infirió**, qué **todavía no
puede decidirse** y qué **evidencia adicional** haría falta.

> **IDEA CLAVE.** Estos seis principios son, además, la lista de los errores que una IA comete con más
> frecuencia al interpretar una búsqueda de secuencias. No es casualidad: son los errores que se
> cometen cuando se razona sobre la forma del resultado en vez de sobre la evidencia.

## El papel de la IA en esta unidad

La IA no aparece aquí como una herramienta de apoyo: aparece como **objeto de evaluación crítica**.
Cada sesión incluye una actividad breve titulada *¿Qué respondería la IA y cómo lo verificarías?*, con
un caso real de esta unidad.

| La IA sirve como | Y hay que tratarla como |
| --- | --- |
| **Generadora de hipótesis** — propone funciones o relaciones posibles | Una propuesta que hay que verificar con los datos |
| **Revisora crítica** — formula preguntas, señala supuestos, ofrece alternativas | Un interlocutor útil, no un árbitro |
| **Fuente de error** — confunde identidad con similitud, afirma homología por un porcentaje, ignora la cobertura, inventa umbrales, mezcla ortólogos y parálogos | Un texto que suena convincente **y puede estar mal** |

En `doc/bitacora-ia.md` se registra, en cada uso: la pregunta, la respuesta, qué afirmaciones son
verificables, con qué evidencia se comprobaron, qué errores aparecieron y cuál fue tu conclusión.

> **ADVERTENCIA — el riesgo específico de esta unidad.** En U5 el peligro era aceptar código que no
> entendías; se notaba al ejecutarlo. Aquí el peligro es aceptar **una interpretación bien redactada**,
> y eso no se nota nunca — porque una conclusión falsa y una verdadera se leen exactamente igual. La
> única defensa es pedir la evidencia y comprobarla.

## El protocolo en esta unidad

`doc/protocolo.md` sigue siendo el mismo documento desde U1 y **no se reinicia**. En U6 añade una
sección dedicada a la comparación de secuencias que registra:

| Bloque | Qué contiene |
| --- | --- |
| **La pregunta** | Qué se quiere averiguar sobre la secuencia |
| **La consulta** | Secuencia, tipo de molécula, identificador, versión, fuente y fecha |
| **La estrategia** | Qué comparación, contra qué, y por qué esa y no otra |
| **La ejecución** | Programa, versión, base de datos, parámetros, formato de salida |
| **Los resultados** | Los seleccionados, con su criterio de selección |
| **La interpretación** | Identidad, cobertura y *E-value* leídos juntos |
| **La hipótesis** | De homología o de función, con su alcance |
| **Las alternativas** | Otras explicaciones consideradas, y por qué se descartaron |
| **Los límites** | Qué no puede afirmarse con esta evidencia |
| **Lo que falta** | Qué evidencia adicional resolvería la duda |
| **El uso de IA** | Qué se consultó, qué se validó y cómo |

> **IMPORTANTE — nunca solo comandos ni capturas de pantalla.** Una captura de la salida de BLAST no
> es un registro científico: no dice qué se preguntaba, ni por qué se eligió esa base, ni qué se
> concluyó. El protocolo registra **el razonamiento**; los comandos son su parte más fácil.

## Evidencia integradora

**Un informe de investigación de una secuencia desconocida.** Cada equipo recibe una secuencia sin
identificar y debe averiguar qué es, con la evidencia que pueda construir.

El informe tiene doce apartados:

| # | Apartado |
| --- | --- |
| 1 | La pregunta biológica |
| 2 | Procedencia de la secuencia |
| 3 | Estrategia de comparación, justificada |
| 4 | Parámetros y base de datos |
| 5 | Resultados seleccionados |
| 6 | Interpretación de identidad, cobertura y *E-value* |
| 7 | Hipótesis de homología o de función |
| 8 | Alternativas consideradas |
| 9 | Limitaciones |
| 10 | Evidencia adicional necesaria |
| 11 | Declaración de uso de IA |
| 12 | Protocolo reproducible |

> **IMPORTANTE — cómo se califica.** La calidad del informe depende de **la argumentación, no del
> acierto**. Un informe que llega a una conclusión prudente y bien sostenida vale más que uno que
> «adivina» la respuesta esperada sin poder defenderla. Y una hipótesis honesta que declara no poder
> decidir entre dos explicaciones puede ser un excelente informe.

## Evaluación

| Se evalúa | No se evalúa |
| --- | --- |
| Cómo se formula la pregunta | Memorizar opciones de BLAST |
| La estrategia elegida y su justificación | Reproducir definiciones sin aplicarlas |
| La trazabilidad del análisis | Entregar capturas de pantalla |
| La lectura del alineamiento | Elegir el primer hit |
| La integración de identidad y cobertura | — |
| La lectura crítica del *E-value* | — |
| La precisión conceptual sobre homología | — |
| Las alternativas consideradas | — |
| La declaración de incertidumbre | Conclusiones categóricas sin evidencia |
| La validación de lo que propone una IA | — |
| La reproducibilidad | — |

## Lo que esta unidad NO cubre

Importa decirlo, porque son cosas que la comparación de secuencias sugiere y no resuelve:

- **Filogenia.** Construir árboles, modelos evolutivos y soporte estadístico de ramas. Aquí se
  formulan hipótesis sobre relaciones, no se reconstruyen historias.
- **Alineamiento de genomas completos** y detección de reordenamientos.
- **Predicción estructural** y sus implicaciones funcionales.
- **Anotación automática de genomas** a escala.
- **Perfiles y HMM** (PSI-BLAST, HMMER), que detectan homología más remota.

Todo eso pertenece a cursos posteriores. Lo que sí se lleva de aquí es el criterio para usarlos sin
creerles ciegamente.

## Qué llevas acumulado al terminar

| Unidad | Qué sabías hacer al cerrarla |
| --- | --- |
| U1 | Documentar un análisis y organizar un proyecto de forma reproducible |
| U2 | Moverte en un entorno Unix remoto y operar archivos, permisos y procesos |
| U3 | Obtener datos biológicos y demostrar que son los que dices tener |
| U4 | Interrogar un genoma y construir evidencia |
| U5 | Convertir ese razonamiento en una herramienta reproducible y defendible |
| **U6** | **Comparar con el resto de la vida e interpretar la evidencia para sostener una hipótesis** |

> **El mensaje final del curso.** La bioinformática no consiste en ejecutar herramientas para obtener
> respuestas. Consiste en **evaluar críticamente la evidencia que esas herramientas producen** para
> construir hipótesis biológicas defendibles.
>
> ```text
> la IA propone
>       ↓
> los datos sostienen o contradicen
>       ↓
> tú analizas
>       ↓
> la evidencia delimita
>       ↓
> la conclusión se defiende
> ```

## Referencias

- Altschul, S. F., Gish, W., Miller, W., Myers, E. W., & Lipman, D. J. (1990). Basic local alignment
  search tool. *Journal of Molecular Biology*, 215(3), 403–410.
  <https://doi.org/10.1016/S0022-2836(05)80360-2>
- Altschul, S. F., Madden, T. L., Schäffer, A. A., et al. (1997). Gapped BLAST and PSI-BLAST: a new
  generation of protein database search programs. *Nucleic Acids Research*, 25(17), 3389–3402.
  <https://doi.org/10.1093/nar/25.17.3389>
- Fitch, W. M. (1970). Distinguishing homologous from analogous proteins. *Systematic Zoology*, 19(2),
  99–113. <https://doi.org/10.2307/2412448>
- Henikoff, S., & Henikoff, J. G. (1992). Amino acid substitution matrices from protein blocks.
  *PNAS*, 89(22), 10915–10919. <https://doi.org/10.1073/pnas.89.22.10915>
- Koonin, E. V. (2005). Orthologs, paralogs, and evolutionary genomics. *Annual Review of Genetics*,
  39, 309–338. <https://doi.org/10.1146/annurev.genet.39.073003.114725>
- Needleman, S. B., & Wunsch, C. D. (1970). A general method applicable to the search for similarities
  in the amino acid sequence of two proteins. *Journal of Molecular Biology*, 48(3), 443–453.
  <https://doi.org/10.1016/0022-2836(70)90057-4>
- Pearson, W. R. (2013). An introduction to sequence similarity («homology») searching. *Current
  Protocols in Bioinformatics*, 42, 3.1.1–3.1.8. <https://doi.org/10.1002/0471250953.bi0301s42>
  — **lectura obligatoria de la unidad**
- Sievers, F., Wilm, A., Dineen, D., et al. (2011). Fast, scalable generation of high-quality protein
  multiple sequence alignments using Clustal Omega. *Molecular Systems Biology*, 7, 539.
  <https://doi.org/10.1038/msb.2011.75>
- Smith, T. F., & Waterman, M. S. (1981). Identification of common molecular subsequences. *Journal of
  Molecular Biology*, 147(1), 195–197. <https://doi.org/10.1016/0022-2836(81)90087-5>

---

> **NOTA DOCENTE — no forma parte del material del estudiante.**
>
> **Parámetros de la unidad** (según `plantilla-unidad.md` §3):
>
> | Parámetro | Unidad 6 |
> | --- | --- |
> | Sesiones | S30–S34 (ver discrepancia D1) |
> | Competencias | F (principal); A, B, C, D, G (integradas) |
> | Ajustes integrados | Comparación de secuencias como bloque limpio [Reorganizado] |
> | Lectura obligatoria | Pearson (2013) |
> | Lectura de consulta | Fitch (1970); Koonin (2005) |
> | Datos | `ejemplos/datos-alineamientos/` — auditados en `docente/u6-auditoria-datos.md` |
> | Herramientas | Clustal Omega y BLAST+ en `chaac`; Unix (U4); SGE (S29) |
> | Evidencia integradora | Informe de una secuencia desconocida (S34) |
>
> **Discrepancias y decisiones:**
>
> | # | Asunto | Estado |
> | --- | --- | --- |
> | D1 | **Número de sesiones.** La arquitectura propone seis; el Plan ajustado, tres. Se adoptan **cinco (S30–S34)**: S30 = *comparar*+*alinear*; S32–S34 = *interpretar* / *inferir* / *integrar* (el cierre no añade conceptos) | **Decisión docente (ago-2026); requiere confirmar semanas adicionales** |
> | D2 | **Títulos.** S30 *Comparar…*; S31 *Buscar…*; S32 *Interpretar: una lista de hits no es una conclusión*; S33 *Inferir: cuando la similitud no basta*; S34 *Integrar: de la evidencia a la hipótesis biológica* | Consecuencia de D1 |
> | D3 | **Sin alineador global por parejas.** Solo hay Clustal Omega; no hay EMBOSS (`needle`/`water`). Para los pares de S30 se usará Clustal Omega sobre dos secuencias. La distinción global/local se explica conceptualmente y se observa en la práctica al comparar con el comportamiento de BLAST, que es local | **Resuelto por disponibilidad** |
> | D4 | **Origen de los encabezados** de `ubiE`/`era`/`hemE`: referencia no localizada. Se describirá el formato sin atribuirlo | **Pendiente, sin bloquear** |
> | D5 | **Secuencias «desconocidas» para S34.** Prepararlas antes: secuencias del propio conjunto con el encabezado eliminado, de dificultad variada. Ver `docente/u6-auditoria-datos.md` §7 | **Pendiente** |
> | D6 | **Ubicación de los datos.** Ahora en `contenidos-2026/ejemplos/datos-alineamientos/`; deben llegar a `data/source/` del proyecto del estudiante, con su ficha de procedencia | **Propuesta** |
> | D7 | **Reparto interpretar / inferir / integrar.** S32 solo interpreta; S33 solo infiere; S34 integra. Los nombres de archivo de S32/S33 conservan inercia previa | **Resuelto en redacción (ago-2026)** |
>
> **Estado de redacción.** Redactados: auditoría, portada, S30–S34. Unidad 6 completa a nivel de
> borrador didáctico (faltan PNG de figuras y secuencias desconocidas, D5).
