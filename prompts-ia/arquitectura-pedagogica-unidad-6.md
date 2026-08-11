# Unidad 6 — Comparar secuencias para construir hipótesis biológicas

## Arquitectura pedagógica

---

## 1. Identidad de la unidad

La Unidad 6 introduce al estudiante en la comparación de secuencias, los alineamientos, BLAST y los conceptos básicos de homología.

Sin embargo, su propósito no es únicamente enseñar a ejecutar herramientas.

En el contexto actual, una inteligencia artificial puede:

- proponer un comando de BLAST;
- explicar los campos de una salida;
- seleccionar aparentemente el mejor hit;
- redactar una interpretación convincente.

Por ello, la formación del estudiante debe avanzar hacia capacidades cognitivas de mayor nivel:

```text
comprender
↓
analizar
↓
contrastar
↓
interpretar
↓
argumentar
↓
defender una conclusión
```

La unidad debe enseñar a evaluar críticamente la evidencia producida por las herramientas bioinformáticas y a distinguir entre observaciones, inferencias, hipótesis y afirmaciones que todavía no están sustentadas.

---

## 2. Papel de la unidad dentro del curso

Las unidades anteriores prepararon al estudiante para obtener, organizar, procesar y analizar datos biológicos de manera reproducible.

```text
Datos biológicos
↓
Formatos
↓
Bases de datos
↓
Procesamiento con Unix
↓
Protocolo reproducible
↓
Herramienta automatizada
↓
Infraestructura de cómputo
```

Al terminar la Unidad 5, el estudiante ya puede:

- recuperar datos de fuentes científicas;
- reconocer formatos biológicos;
- inspeccionar y transformar archivos;
- construir flujos reproducibles;
- automatizar procedimientos;
- documentar decisiones;
- ejecutar una herramienta sobre infraestructura compartida.

La nueva limitación ya no es operativa.

Ahora el problema es interpretativo:

> ¿Cómo convierto los resultados de una comparación de secuencias en una hipótesis biológica razonable?

---

## 3. Gran pregunta de la unidad

Toda la unidad debe articularse alrededor de una pregunta central:

> **Tengo una secuencia cuya función o relación evolutiva quiero investigar. ¿Qué puedo inferir a partir de su comparación con otras secuencias y qué evidencia necesito para sostener esa inferencia?**

Esta pregunta permite introducir de manera natural:

- alineamientos;
- identidad;
- similitud;
- cobertura;
- gaps;
- alineamientos globales y locales;
- BLAST;
- bases de datos de secuencias;
- score y E-value;
- homología;
- ortología;
- paralogía;
- duplicación;
- especiación;
- límites de la transferencia de función.

---

## 4. Narrativa de la unidad

```text
Tengo una secuencia
↓
aislada aporta información limitada
↓
necesito compararla
↓
construyo un alineamiento
↓
observo coincidencias y diferencias
↓
quiero compararla contra millones de secuencias
↓
necesito una búsqueda eficiente
↓
uso BLAST
↓
obtengo muchos hits
↓
evalúo identidad, cobertura, score, E-value y anotación
↓
distingo observación de inferencia
↓
evalúo hipótesis de homología
↓
reconozco qué evidencia falta
↓
construyo una hipótesis biológica defendible
```

Ninguna sesión debe romper esta historia ni convertirse en una explicación aislada de una herramienta.

---

## 5. Cambio conceptual

En las unidades anteriores, el estudiante se concentró principalmente en construir el análisis.

```text
¿Cómo obtengo y proceso la evidencia?
```

En esta unidad, el foco cambia:

```text
¿Qué significa la evidencia?
```

El cambio fundamental debe quedar explícito:

```text
Resultado de una herramienta
≠
Conclusión biológica
```

Entre ambos existe un proceso de razonamiento que incluye:

- comprobar la calidad de los datos;
- interpretar el alineamiento;
- comparar métricas;
- considerar explicaciones alternativas;
- reconocer incertidumbre;
- establecer el alcance de la inferencia.

---

## 6. Propósito general

Que el estudiante interprete críticamente comparaciones de secuencias y resultados de BLAST para formular hipótesis biológicas fundamentadas, distinguiendo similitud observada, relaciones de homología, transferencia de función, incertidumbre y limitaciones de la evidencia disponible.

---

## 7. Competencia central

Al finalizar la unidad, el estudiante será capaz de:

> **Interpretar críticamente comparaciones de secuencias para construir y defender hipótesis biológicas fundamentadas en evidencia, distinguiendo entre observaciones, inferencias, incertidumbre y afirmaciones no sustentadas.**

---

## 8. Competencias específicas

### 8.1 Comprender

El estudiante podrá:

- explicar por qué se comparan secuencias;
- reconocer qué representa un alineamiento;
- explicar por qué aparecen gaps;
- distinguir identidad de similitud;
- interpretar cobertura;
- distinguir alineamientos globales de locales;
- explicar por qué BLAST utiliza una estrategia heurística.

### 8.2 Analizar

El estudiante podrá:

- examinar alineamientos;
- reconocer regiones conservadas;
- comparar varios hits;
- relacionar identidad y cobertura;
- detectar alineamientos parciales;
- identificar resultados inconsistentes;
- reconocer cuándo una métrica aislada es insuficiente.

### 8.3 Interpretar

El estudiante podrá:

- decidir qué resultados aportan evidencia relevante;
- distinguir entre una coincidencia local y una semejanza de longitud completa;
- reconocer cuándo una anotación puede transferirse con cautela;
- formular explicaciones biológicas y técnicas alternativas;
- reconocer lo que el resultado no permite afirmar.

### 8.4 Argumentar

El estudiante podrá:

- justificar la selección de una base de datos;
- justificar el tipo de BLAST utilizado;
- defender cuál hit considera más informativo;
- explicar qué evidencia apoya una hipótesis de homología;
- indicar qué evidencia adicional sería necesaria;
- responder críticamente a una interpretación propuesta por otra persona o por una IA.

### 8.5 Trabajar de manera reproducible

El estudiante podrá:

- documentar la secuencia consulta;
- registrar la procedencia de los datos;
- conservar parámetros y versiones;
- producir salidas tabulares;
- procesar resultados con Unix;
- distinguir datos originales, resultados derivados e interpretación.

---

## 9. Evolución cognitiva

La unidad debe llevar al estudiante de una lectura descriptiva a una interpretación científica.

```text
Reconocer
↓
Describir
↓
Comparar
↓
Analizar
↓
Interpretar
↓
Cuestionar
↓
Argumentar
↓
Defender
```

La meta no es que el estudiante repita definiciones, sino que pueda justificar una conclusión frente a evidencia incompleta o ambigua.

---

## 10. Papel de las herramientas

Las herramientas aparecen únicamente cuando resuelven una limitación.

### Alineamiento

Aparece porque una secuencia aislada no permite observar de manera explícita qué posiciones se conservan, sustituyen, insertan o eliminan.

### Alineamiento global

Aparece cuando interesa comparar dos secuencias a lo largo de toda su longitud.

### Alineamiento local

Aparece cuando interesa detectar regiones conservadas dentro de secuencias que pueden diferir ampliamente.

### BLAST

Aparece cuando comparar una secuencia mediante programación dinámica contra millones de secuencias sería demasiado costoso.

### Bases de datos

Aparecen porque la interpretación depende de:

- qué secuencias contiene la colección;
- su procedencia;
- su versión;
- el tipo de molécula;
- la calidad y naturaleza de las anotaciones.

### Unix

Se reutiliza para:

- inspeccionar archivos FASTA;
- construir bases locales;
- ejecutar búsquedas;
- seleccionar formatos de salida;
- filtrar resultados;
- resumir hits;
- mantener trazabilidad.

El estudiante debe percibir que Unix continúa siendo una herramienta de apoyo y no el objeto central de aprendizaje.

---

## 11. Conceptos biológicos irrenunciables

La unidad debe conservar, al menos, los siguientes conceptos:

- gen;
- proteína;
- secuencia nucleotídica;
- secuencia de aminoácidos;
- mutación;
- sustitución;
- inserción;
- deleción;
- gap;
- conservación;
- dominio;
- familia génica;
- similitud;
- identidad;
- cobertura;
- homología;
- ortólogo;
- parálogo;
- xenólogo;
- duplicación;
- especiación;
- transferencia horizontal;
- función molecular;
- anotación funcional.

Estos conceptos deben introducirse o recuperarse únicamente cuando sean necesarios para interpretar evidencia.

---

## 12. Principios científicos de la unidad

### 12.1 Homología no es un porcentaje

Dos secuencias son homólogas o no lo son.

La identidad y la similitud pueden expresarse como porcentajes; la homología es una hipótesis sobre un origen evolutivo común.

### 12.2 Similitud no demuestra por sí sola la misma función

Dos secuencias pueden compartir regiones conservadas y realizar funciones diferentes.

### 12.3 El mejor hit no es automáticamente la mejor explicación

El primer resultado puede estar condicionado por:

- la composición de la base de datos;
- secuencias redundantes;
- anotaciones incompletas;
- cobertura parcial;
- dominios compartidos;
- proteínas multidominio.

### 12.4 Una métrica aislada no basta

La interpretación debe integrar:

```text
identidad
+
cobertura
+
E-value
+
score
+
región alineada
+
anotación
+
procedencia
+
contexto biológico
```

### 12.5 La ausencia de evidencia no es evidencia de ausencia

No encontrar un hit puede deberse a:

- distancia evolutiva;
- base de datos inadecuada;
- secuencia corta;
- mala calidad;
- parámetros poco sensibles;
- función realmente novedosa.

### 12.6 Una hipótesis debe declarar sus límites

Toda interpretación debe distinguir:

- qué se observó;
- qué se infirió;
- qué todavía no puede decidirse;
- qué evidencia adicional sería necesaria.

---

## 13. Papel de la inteligencia artificial

La IA forma parte explícita de la arquitectura pedagógica.

No se utiliza como fuente final de respuestas.

Se utiliza como:

### Generadora de hipótesis

Puede proponer posibles funciones o relaciones.

El estudiante debe verificar qué evidencia las sustenta.

### Revisora crítica

Puede formular preguntas, señalar supuestos o proponer interpretaciones alternativas.

### Fuente potencial de error

Puede:

- confundir identidad con similitud;
- afirmar homología a partir de un porcentaje;
- asumir que el mejor hit tiene la misma función;
- interpretar incorrectamente el E-value;
- ignorar la cobertura;
- inventar umbrales universales;
- confundir ortólogos y parálogos;
- redactar conclusiones más fuertes que la evidencia.

### Regla de la unidad

> **La IA puede proponer. Los datos deben demostrar. El estudiante debe argumentar.**

---

## 14. Actividades con IA

Cada sesión debería incorporar una actividad breve titulada:

## ¿Qué respondería la IA y cómo lo verificarías?

Ejemplos:

- evaluar una afirmación de homología basada únicamente en identidad;
- detectar una interpretación que ignora la cobertura;
- comparar dos explicaciones de un alineamiento;
- revisar si una función se transfirió con evidencia suficiente;
- identificar parámetros inventados;
- distinguir lenguaje convincente de evidencia real.

La bitácora de IA debe registrar:

- pregunta;
- respuesta de la IA;
- afirmaciones verificables;
- evidencia utilizada;
- errores detectados;
- conclusión del estudiante.

---

## 15. Datos y casos de estudio

La unidad debe reutilizar datos reales del material anterior:

- secuencias `ubiE` de diferentes organismos;
- subconjuntos de cuatro y diecinueve organismos;
- secuencias nucleotídicas y proteicas;
- proteínas humanas incluidas en la práctica anterior;
- secuencias para búsquedas locales;
- bases de datos construidas con `makeblastdb`.

Los datos no deben presentarse únicamente como archivos.

Cada conjunto debe responder una función narrativa.

### Familia `ubiE`

Puede utilizarse para:

- reconocer conservación;
- comparar nucleótidos y proteínas;
- construir alineamientos múltiples;
- discutir relaciones dentro de una familia;
- observar cómo cambia la interpretación según la escala del conjunto.

### Proteínas humanas

Pueden utilizarse para:

- formular una pregunta de búsqueda;
- seleccionar bases de datos;
- ejecutar BLAST;
- comparar hits;
- discutir anotación funcional y cobertura;
- analizar la diferencia entre secuencia consulta y resultados.

Antes de construir las sesiones deberá documentarse con precisión qué representa cada archivo y cuál será su función pedagógica.

---

## 16. Arquitectura propuesta de sesiones

La unidad se organiza inicialmente en seis sesiones. La distribución puede ajustarse después de reconstruir por completo el uso de los archivos originales.

---

# S30 — Comparar: una secuencia adquiere significado en contexto

## Propósito

Comprender por qué la comparación de secuencias permite formular preguntas sobre conservación, función y evolución.

## Problema

Una secuencia aislada contiene información estructural, pero aporta poco contexto biológico.

## Pregunta central

> ¿Qué puedo aprender al comparar esta secuencia con otras?

## Conceptos principales

- secuencia nucleotídica y proteica;
- identidad;
- similitud;
- sustituciones;
- inserciones y deleciones;
- conservación;
- posiciones homólogas;
- observación frente a inferencia.

## Herramientas

Inspección de FASTA y comparación inicial de secuencias reales.

## Cambio conceptual

```text
Secuencia aislada
↓
Secuencia en contexto
```

## Producto

Descripción razonada de semejanzas y diferencias entre secuencias reales, sin afirmar todavía homología ni función.

## Limitación que abre S31

La comparación visual deja de ser viable cuando las secuencias son largas o las diferencias son numerosas.

---

# S31 — Alinear: representar semejanzas y diferencias

## Propósito

Interpretar un alineamiento como una hipótesis sobre la correspondencia entre posiciones.

## Problema

Las secuencias no siempre tienen la misma longitud y pueden contener inserciones, deleciones y sustituciones.

## Pregunta central

> ¿Qué posiciones pueden compararse de manera razonable?

## Conceptos principales

- alineamiento;
- match;
- mismatch;
- gap;
- penalización;
- score;
- alineamiento global;
- alineamiento local;
- matrices de sustitución;
- programación dinámica como modelo conceptual.

## Alcance algorítmico

La programación dinámica debe explicarse lo suficiente para comprender:

- que existen muchas alineaciones posibles;
- que una función de puntuación permite compararlas;
- que gaps y sustituciones tienen costos;
- que global y local responden preguntas diferentes.

No se espera implementar Needleman–Wunsch ni Smith–Waterman.

## Cambio conceptual

```text
Parecido intuitivo
↓
Correspondencia explícita y evaluable
```

## Producto

Interpretación de alineamientos y justificación del tipo de alineamiento adecuado para una pregunta.

## Limitación que abre S32

El alineamiento exacto funciona para pocas secuencias, pero no para buscar eficientemente en bases con millones de registros.

---

# S32 — Buscar: comparar una secuencia contra una base de datos

## Propósito

Comprender por qué BLAST utiliza una estrategia heurística y diseñar una búsqueda reproducible.

## Problema

No es viable aplicar un alineamiento exacto completo contra millones de secuencias.

## Pregunta central

> ¿Cómo localizo rápidamente candidatos similares dentro de una base de datos?

## Conceptos principales

- secuencia consulta;
- base de datos;
- BLASTN;
- BLASTP;
- BLASTX;
- búsqueda local;
- semillas;
- palabras o k-mers;
- extensión;
- HSP;
- velocidad;
- sensibilidad;
- tamaño de palabra.

## Herramientas

- `makeblastdb`;
- BLAST en línea de comandos;
- ayuda oficial;
- bases locales construidas con los archivos del curso.

## Cambio conceptual

```text
Alinear contra una secuencia
↓
Buscar candidatos en una colección
```

## Producto

Búsqueda BLAST reproducible con selección justificada del programa, la base de datos y los parámetros básicos.

## Limitación que abre S33

BLAST produce muchos resultados; obtenerlos no equivale a saber cuáles son informativos.

---

# S33 — Interpretar: construir evidencia a partir de los hits

## Propósito

Evaluar críticamente resultados de BLAST integrando varias métricas y el contexto de la búsqueda.

## Problema

El primer hit o el E-value más pequeño no constituyen por sí solos una conclusión biológica.

## Pregunta central

> ¿Qué hit aporta la evidencia más sólida y por qué?

## Conceptos principales

- bit score;
- E-value;
- identidad;
- positivos;
- cobertura;
- longitud de la consulta;
- longitud del sujeto;
- HSP múltiples;
- alineamientos parciales;
- formato tabular;
- anotaciones.

## Herramientas

- formatos de salida de BLAST;
- selección de columnas;
- procesamiento con Unix;
- comparación y resumen de hits.

## Cambio conceptual

```text
Lista de resultados
↓
Jerarquía argumentada de evidencia
```

## Producto

Tabla interpretada de candidatos, con selección justificada y alternativas consideradas.

## Limitación que abre S34

Un resultado fuerte de similitud todavía no distingue automáticamente función, ortología, paralogía o historia evolutiva.

---

# S34 — Inferir: similitud, homología y relaciones evolutivas

## Propósito

Distinguir similitud observada de hipótesis de homología y reconocer diferentes relaciones entre genes.

## Problema

Las proteínas similares pueden compartir un ancestro sin desempeñar exactamente la misma función.

## Pregunta central

> ¿Qué relación evolutiva podría explicar la similitud observada?

## Conceptos principales

- homología;
- ortología;
- paralogía;
- xenología;
- duplicación;
- especiación;
- transferencia horizontal;
- familia génica;
- conservación de dominios;
- transferencia de función.

## Cambio conceptual

```text
Se parecen
↓
¿Qué historia explica que se parezcan?
```

## Producto

Evaluación argumentada de distintas hipótesis evolutivas, indicando evidencia disponible y faltante.

## Limitación que abre S35

Las métricas y anotaciones permiten construir hipótesis, pero todavía es necesario integrarlas y defender una conclusión prudente.

---

# S35 — Defender: construir una hipótesis biológica

## Propósito

Integrar toda la evidencia de la unidad en una interpretación científica reproducible y defendible.

## Situación

El estudiante recibe una secuencia o conjunto de secuencias cuya función o relación evolutiva debe investigar.

## Pregunta central

> ¿Qué hipótesis es la más razonable, qué evidencia la sustenta y qué no puedo afirmar todavía?

## Actividades

- inspeccionar la secuencia;
- seleccionar la estrategia de comparación;
- documentar la búsqueda;
- evaluar varios hits;
- revisar alineamientos;
- contrastar anotaciones;
- formular hipótesis alternativas;
- evaluar una interpretación generada por IA;
- elegir una conclusión;
- declarar limitaciones;
- proponer evidencia adicional.

## Producto integrador

Informe científico breve con:

1. pregunta biológica;
2. procedencia de la secuencia;
3. estrategia de comparación;
4. parámetros y base de datos;
5. resultados seleccionados;
6. interpretación de identidad, cobertura y E-value;
7. hipótesis de homología o función;
8. alternativas consideradas;
9. limitaciones;
10. evidencia adicional necesaria;
11. declaración del uso de IA;
12. protocolo reproducible.

## Cambio conceptual final

```text
Ejecutar una búsqueda
↓
Interpretar evidencia
↓
Construir una hipótesis
↓
Defender sus límites
```

---

## 17. Documento reproducible

El protocolo continúa como eje de la unidad.

Debe incorporar una sección dedicada a comparación de secuencias que registre:

- pregunta biológica;
- secuencia consulta;
- tipo de molécula;
- identificador y versión;
- fuente;
- fecha de recuperación;
- base de datos;
- versión o fecha de la base;
- programa utilizado;
- parámetros;
- formato de salida;
- criterios de selección;
- resultados principales;
- interpretación;
- hipótesis alternativas;
- limitaciones;
- evidencia adicional;
- uso de IA y validación.

Nunca debe registrar únicamente comandos o capturas de pantalla.

---

## 18. Figuras sugeridas

La unidad debe diseñarse suponiendo figuras que expliquen razonamiento.

Ejemplos:

- una secuencia aislada frente a una secuencia en contexto;
- sustitución, inserción y deleción;
- alineamiento como hipótesis de correspondencia;
- global frente a local;
- muchas alineaciones posibles y una función de puntuación;
- velocidad frente a sensibilidad;
- ensemillado, extensión y evaluación en BLAST;
- identidad frente a cobertura;
- dos hits con el mismo E-value pero diferente significado;
- similitud frente a homología;
- duplicación y especiación;
- dato, inferencia e hipótesis;
- flujo completo desde la secuencia hasta la conclusión;
- afirmación de IA frente a evidencia disponible.

Las figuras no deben limitarse a ilustrar interfaces o comandos.

---

## 19. Prácticas

Las prácticas deben:

- utilizar secuencias reales;
- conservar continuidad entre sesiones;
- responder una pregunta biológica;
- producir evidencia acumulativa;
- exigir interpretación;
- incluir resultados ambiguos;
- obligar a considerar alternativas;
- registrar decisiones;
- reutilizar Unix para procesar salidas;
- integrar IA como objeto de evaluación crítica.

No deben consistir en seguir instrucciones para obtener una captura.

---

## 20. Evidencia integradora

La evidencia integradora será un:

# Informe de investigación de una secuencia desconocida

El estudiante deberá demostrar que puede:

- formular una pregunta;
- seleccionar una estrategia;
- ejecutar una búsqueda reproducible;
- analizar varios resultados;
- distinguir observación de inferencia;
- construir una hipótesis;
- explicar sus límites;
- evaluar una propuesta generada por IA;
- proponer cómo validar la hipótesis.

La calidad del informe dependerá de la argumentación, no de que el estudiante encuentre una respuesta previamente esperada.

---

## 21. Criterios de evaluación

La evaluación debe privilegiar:

- formulación de la pregunta;
- selección de la estrategia;
- trazabilidad;
- lectura del alineamiento;
- integración de identidad y cobertura;
- interpretación crítica del E-value;
- comparación de hits;
- precisión conceptual sobre homología;
- consideración de hipótesis alternativas;
- declaración de incertidumbre;
- uso de evidencia;
- validación de respuestas de IA;
- reproducibilidad.

No debe privilegiar:

- memorizar opciones;
- reproducir definiciones sin aplicarlas;
- seleccionar automáticamente el primer hit;
- entregar capturas de pantalla;
- redactar conclusiones categóricas sin evidencia.

---

## 22. Preguntas de revisión crítica

Durante el diseño de cada sesión debe comprobarse:

- ¿La herramienta aparece después del problema?
- ¿La pregunta biológica sigue siendo visible?
- ¿El estudiante debe interpretar o solo ejecutar?
- ¿Se distingue observación de inferencia?
- ¿Hay resultados ambiguos?
- ¿Se exige justificar decisiones?
- ¿Se declara qué no puede concluirse?
- ¿La IA obliga a verificar y no sustituye el razonamiento?
- ¿El protocolo conserva trazabilidad?
- ¿La sesión prepara una limitación que impulsa la siguiente?

---

## 23. Mensaje final de la unidad

La unidad debe cerrar con una idea central:

> **La Bioinformática no consiste en ejecutar herramientas para obtener respuestas. Consiste en evaluar críticamente la evidencia que esas herramientas producen para construir hipótesis biológicas defendibles.**

En la era de la inteligencia artificial, esta capacidad se vuelve aún más importante.

La IA puede generar interpretaciones.

El investigador debe decidir cuáles están sustentadas.

```text
La IA propone
↓
los datos sostienen o contradicen
↓
el estudiante analiza
↓
la evidencia delimita
↓
la conclusión se defiende
```
