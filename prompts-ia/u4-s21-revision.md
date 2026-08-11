i# Revisión técnica y didáctica de S21 — Confrontar una fuente independiente

Actúa como **editor académico, diseñador curricular y especialista en bioinformática reproducible**.

Debes revisar y corregir el archivo:

`u4-s21-confrontar-fuente-independiente.md`

La sesión ya tiene una arquitectura conceptual sólida.

No debes reescribirla desde cero.

Tu tarea es hacer una **revisión técnica, metodológica y didáctica**, aplicando únicamente los ajustes descritos abajo.

---

# Contexto obligatorio

Antes de modificar S21, lee completamente:

* `README.md`
* `guia-generacion-unidad.md`
* S18
* S19
* S20
* la arquitectura de la Unidad 4

Debes conservar la narrativa:

```text
S18  Seleccionar
S19  Identificar
S20  Normalizar
S21  Confrontar
S22  Cuantificar
S23  Integrar
```

Este no es un curso de Unix.

Tampoco es un curso de UniProt, Ensembl o BioMart.

Es un curso de Bioinformática cuyo objetivo es enseñar a construir, confrontar e interpretar evidencia científica reproducible.

---

# Propósito de S21

S21 debe enseñar que:

```text
un resultado reproducible
↓
todavía no es una conclusión robusta

una fuente de procedencia distinta
↓
permite poner a prueba ese resultado

las discrepancias
↓
deben explicarse, no eliminarse
```

La novedad de la sesión es intelectual:

> **confrontar evidencia de distinta procedencia y delimitar qué puede afirmarse.**

No introducir herramientas Unix nuevas.

---

# Objetivo de esta revisión

Realiza los ajustes necesarios para:

1. definir con precisión qué fuente externa se utilizará;
2. garantizar que los comandos correspondan al formato real de esa fuente;
3. comparar universos biológicos equivalentes;
4. distinguir archivos originales, normalizados y comparables;
5. corregir contradicciones entre S21 y S22;
6. fortalecer la reproducibilidad de la descarga;
7. moderar afirmaciones epistemológicas demasiado absolutas;
8. reducir riesgos operativos durante el taller.

No agregues temas nuevos.

No conviertas la sesión en un tutorial de UniProt.

---

# Ajustes de prioridad alta

## 1. Elegir una fuente canónica y un formato único

La sesión actualmente permite usar UniProt o una anotación GenBank, pero todos los comandos posteriores dependen de una exportación TSV de UniProt.

Corrige esta ambigüedad.

Para esta sesión utiliza una **tabla canónica real de UniProt en formato TSV**, descargada con una consulta y columnas definidas por el docente.

La alternativa GenBank puede mencionarse únicamente como posibilidad futura o adaptación docente, pero no debe formar parte de la ruta principal si no existe una práctica equivalente para ese formato.

Debe quedar claro que todos los estudiantes trabajan con:

* el mismo tipo de recurso;
* el mismo formato;
* las mismas columnas;
* el mismo orden de columnas;
* una consulta reproducible.

No presentes la sesión como agnóstica respecto de la fuente si los comandos dependen de UniProt.

---

## 2. Definir exactamente la exportación de UniProt

Especifica qué columnas debe contener la tabla y en qué orden.

No dejes el uso de `cut -f3` sin explicación.

La sesión debe incluir una tabla como:

| Columna | Campo de UniProt                    | Uso en S21                          |
| ------: | ----------------------------------- | ----------------------------------- |
|       1 | Entry                               | Identificador del registro proteico |
|       2 | Protein names u otro campo acordado | Contexto                            |
|       3 | Gene Names (ordered locus)          | Identificador comparable            |
|       … | …                                   | …                                   |

Usa los nombres reales de los campos de la exportación elegida.

Aclara que `cut -f3` funciona porque la consulta canónica fija el campo de locus en esa posición.

Si la posición puede cambiar, utiliza un marcador visible como:

```text
<COLUMNA_LOCUS>
```

y pide al estudiante sustituirlo después de auditar el encabezado.

No combines ambas estrategias.

Elige una y sé consistente.

---

## 3. Delimitar correctamente el objeto biológico

La lista externa de UniProt no representa necesariamente todos los genes anotados en el GFF3.

Representa, con mayor precisión:

> loci asociados con registros proteicos incluidos por UniProt.

Por tanto, no compares directamente:

```text
todos los locus_tag del GFF3
vs.
loci con producto proteico en UniProt
```

como si fueran inventarios equivalentes.

Construye dos análisis claramente separados:

### Comparación principal

Comparar universos equivalentes:

* loci de genes codificantes de proteína del GFF3;
* loci asociados con proteínas en UniProt.

### Comparación de cobertura

Caracterizar qué objetos del GFF3 quedan fuera del alcance de UniProt:

* genes de RNA;
* pseudogenes;
* genes sin producto proteico;
* otros tipos no cubiertos.

Debe quedar explícito que una diferencia por alcance no es una discrepancia sobre la existencia del gen.

No llames a ambas listas simplemente “inventario de genes” sin matizar su universo.

---

## 4. Crear la lista propia comparable

La sesión utiliza `results/s19/locus-tags.txt`, pero esa lista puede incluir objetos fuera del alcance de UniProt.

Genera o recupera una lista específica para S21, por ejemplo:

```text
results/s21/locus-codificantes-propio-original.txt
```

Esta lista debe construirse desde el GFF3 seleccionando únicamente los registros adecuados al universo comparable.

No repitas innecesariamente S19: recupera sus operaciones, pero explica qué restricción biológica nueva se aplica y por qué.

Conserva por separado:

```text
locus-codificantes-propio-original.txt
locus-codificantes-propio-normalizado.txt
locus-uniprot-original.txt
locus-uniprot-normalizado.txt
```

La comparación con `comm` debe usar explícitamente las dos listas normalizadas.

No sobrescribas los archivos originales.

---

## 5. Definir nombres de archivos inequívocos

Revisa todos los comandos y productos para distinguir:

* tabla fuente original;
* lista externa extraída;
* lista externa normalizada;
* lista propia comparable;
* lista propia normalizada;
* zonas de la comparación.

Utiliza una convención consistente, por ejemplo:

```text
data/source/uniprot-proteoma.tsv

results/s21/locus-uniprot-original.txt
results/s21/locus-uniprot-normalizado.txt

results/s21/locus-codificantes-propio-original.txt
results/s21/locus-codificantes-propio-normalizado.txt

results/s21/solo-propio.txt
results/s21/en-ambas.txt
results/s21/solo-uniprot.txt
```

Todos los comandos deben apuntar al archivo correcto.

---

## 6. Corregir la comparación

Actualmente se compara la lista de S19 con una lista externa cuyo estado de normalización no está claro.

Modifica la sección para que:

1. ambas listas se auditen;
2. ambas pasen por la política apropiada;
3. se compruebe que estén ordenadas;
4. `comm` reciba las dos listas normalizadas.

Ejemplo estructural:

```bash
comm \
  results/s21/locus-codificantes-propio-normalizado.txt \
  results/s21/locus-uniprot-normalizado.txt
```

No utilices una lista original en un lado y una lista normalizada en el otro.

---

## 7. Corregir el tratamiento de proporciones

S21 puede contar las tres zonas.

No debe exigir cálculos que contradigan el puente hacia S22.

Elige una de estas opciones:

### Opción preferida

En S21 reportar únicamente:

* número solo propio;
* número común;
* número solo externo.

Dejar para S22:

* porcentajes;
* proporciones;
* longitudes;
* distribuciones;
* análisis por grupos.

### Opción alternativa

Permitir una proporción simple, pero declarar explícitamente que:

> S21 usa una razón básica como resumen descriptivo; S22 permitirá calcular proporciones condicionadas, medidas derivadas y resúmenes por múltiples columnas.

No digas que ninguna herramienta actual puede calcular proporciones si ya las calculaste.

---

## 8. Corregir los denominadores

No uses una única columna “% de mi inventario” para las tres zonas.

Si se conservan porcentajes, distingue:

| Zona | N.º | % del inventario propio | % del inventario externo |
| ---- | --: | ----------------------: | -----------------------: |

O bien elimina porcentajes de S21.

“Solo en la fuente externa” no debe expresarse automáticamente como porcentaje del inventario propio.

---

## 9. Añadir un archivo de respaldo real

La sesión depende de un recurso externo.

Incluye una estrategia de contingencia:

* el docente descarga previamente una copia real;
* conserva consulta, fecha y versión;
* registra checksum;
* coloca el archivo de respaldo en la carpeta de datos del curso;
* los estudiantes lo usan si UniProt no responde o cambia su interfaz.

No uses datos artificiales.

La copia de respaldo debe provenir de una consulta real y estar documentada.

Añade una nota indicando que la descarga en vivo es preferible, pero el taller no debe depender de la disponibilidad del recurso.

---

## 10. Completar la ficha de procedencia

La ficha debe permitir identificar exactamente el archivo utilizado.

Añade:

* nombre exacto del archivo;
* tamaño;
* checksum;
* versión o release de UniProt;
* fecha y hora de descarga si procede;
* consulta;
* filtros;
* columnas solicitadas;
* número de registros;
* URL o identificador de la consulta.

No prometas que otra persona obtendrá exactamente la misma tabla únicamente con una URL dinámica.

Distingue:

* reproducir la consulta;
* verificar que se utilizó el mismo archivo.

---

# Ajustes conceptuales

## 11. Matizar reproducibilidad, confianza y robustez

Evita una oposición demasiado binaria entre:

```text
reproducible = no confiable
dos fuentes = confiable
```

Debe quedar claro que:

* la reproducibilidad permite repetir el análisis;
* la coherencia interna verifica relaciones dentro de la misma procedencia;
* la confrontación con otra fuente aporta evidencia adicional;
* el acuerdo aumenta la confianza, pero no demuestra verdad;
* la discrepancia ayuda a caracterizar incertidumbre.

Usa expresiones como:

> “conclusión provisional mejor sustentada”

o

> “resultado que ha superado una prueba externa”.

No presentes la comparación como validación definitiva.

---

## 12. Precisar el tipo de robustez

Distingue:

* robustez del procedimiento ante cambios de formato;
* robustez del resultado ante otra procedencia;
* coherencia interna;
* concordancia entre fuentes.

En S21 se evalúa principalmente:

> la estabilidad del resultado frente a una fuente de procedencia distinta, independiente en aspectos explícitamente declarados.

No uses “robustez” como sinónimo universal de validez.

---

## 13. Corregir la tabla de independencia

No afirmes que FASTA y GFF3 del mismo ensamblado son independientes “en nada relevante”.

Precisa que:

* no son independientes respecto de la procedencia del ensamblado;
* pueden aportar controles cruzados sobre secuencias, replicones, coordenadas o cobertura;
* no aportan una validación independiente del criterio de anotación si provienen del mismo paquete.

La independencia debe tratarse por dimensiones.

---

## 14. Reformular “cinco explicaciones, ningún error”

No excluyas la posibilidad de errores reales.

Una discrepancia puede deberse a:

* alcance;
* versión;
* filtros;
* criterio de anotación;
* estrategia propia;
* archivo equivocado;
* consulta incorrecta;
* error de la fuente.

El mensaje debe ser:

> No llames error a una discrepancia antes de evaluar explicaciones alternativas.

Puedes cambiar el encabezado por algo como:

* “Interpretar: varias explicaciones antes de declarar un error”
* “Interpretar: una discrepancia admite causas alternativas”
* “Interpretar: hipótesis antes que culpables”

Conserva la intención científica.

---

## 15. No exigir descartar todas las alternativas

Revisa frases como:

> “Una hipótesis sin descarte no es una hipótesis”.

Esa formulación es demasiado absoluta.

Una hipótesis válida puede:

* estar apoyada por evidencia;
* generar una predicción;
* competir con alternativas;
* mantener incertidumbre.

Sustitúyela por una exigencia más rigurosa:

> Para cada hipótesis, registra qué evidencia la apoya, qué alternativas siguen abiertas y qué observación permitiría distinguirlas.

La tabla del protocolo debe usar columnas como:

| Grupo | Hipótesis principal | Evidencia a favor | Alternativas abiertas | Grado de confianza | Evidencia pendiente |
| ----- | ------------------- | ----------------- | --------------------- | ------------------ | ------------------- |

No obligues al estudiante a declarar descartes que no ha demostrado.

---

## 16. Matizar la zona común

No digas simplemente:

> “genes sostenidos por dos fuentes independientes”

si ambas fuentes comparten el ensamblado o parte de la anotación.

Usa una formulación como:

> identificadores reportados por dos fuentes de procedencia distinta, concordantes en los aspectos evaluados.

O:

> loci reconocidos por ambas fuentes, cuya independencia parcial quedó documentada.

Conserva la idea de que la zona común fortalece la conclusión, pero no demuestra existencia biológica.

---

# Ajustes técnicos

## 17. No depender del texto exacto del encabezado

Evita depender exclusivamente de:

```bash
grep -v '^Entry'
```

Si la tabla canónica siempre tiene una primera línea de encabezado, usa una estrategia robusta ya enseñada para excluirla por posición.

Si no existe una herramienta previamente enseñada para hacerlo, conserva `grep -v`, pero:

* declara que funciona porque la exportación canónica fija ese encabezado;
* valida que solo elimina una línea;
* no lo presentes como estrategia general para cualquier tabla.

---

## 18. Derivar el separador interno desde la auditoría

No presupongas que los valores múltiples están separados por espacios.

La práctica debe:

1. inspeccionar el campo;
2. determinar el separador real;
3. documentarlo;
4. aplicar la transformación correspondiente.

Si la exportación canónica garantiza separación por espacio, indícalo con referencia a la documentación de UniProt y conserva la comprobación sobre los datos.

No uses `tr ' ' '\n'` como receta universal.

---

## 19. Verificar la semántica de valores múltiples

No afirmes automáticamente que dos identificadores significan una proteína asociada con más de un gen.

Antes debes confirmar qué representa el campo elegido en UniProt.

Describe varias posibilidades solo si la documentación las respalda.

Si la semántica no puede determinarse con el archivo, clasifícalo como caso que requiere documentación externa.

---

## 20. Revisar la muestra de casos

La Práctica 5 pide cinco identificadores por cada zona.

Evalúa si esto cabe en veinte minutos.

Reduce la carga sin perder el objetivo.

Una opción razonable:

* examinar tres casos de cada zona no vacía;
* o cinco casos totales, seleccionados de zonas distintas;
* o trabajar con grupos ya detectados por tipo.

El estudiante debe examinar casos concretos, pero no convertir el taller en quince búsquedas manuales.

---

# Revisión de las prácticas

Después de los ajustes, la progresión debe quedar así:

```text
Práctica 1
Descarga canónica, procedencia e independencia parcial

↓

Práctica 2
Auditoría de la tabla externa y delimitación de su alcance

↓

Práctica 3
Construcción de dos universos comparables:
GFF3 codificante y loci asociados con proteínas en UniProt

↓

Práctica 4
Auditoría y aplicación de la política de normalización

↓

Práctica 5
Confrontación de listas normalizadas y caracterización de las tres zonas

↓

Práctica 6
Hipótesis, evidencia a favor, alternativas abiertas y evidencia pendiente
```

Cada práctica debe:

* comenzar con una pregunta biológica;
* recuperar un producto anterior;
* terminar con una interpretación o límite;
* contribuir al protocolo acumulativo.

---

# Revisión del protocolo

Actualiza la sección del protocolo para incluir:

## Fuente externa

* archivo;
* checksum;
* tamaño;
* release;
* consulta;
* columnas;
* filtros;
* fecha;
* número de registros.

## Declaración de independencia

* independiente respecto de;
* no independiente respecto de;
* qué errores puede detectar;
* qué errores no puede detectar.

## Universo comparable

* definición del conjunto propio;
* definición del conjunto externo;
* objetos excluidos por alcance;
* justificación.

## Listas utilizadas

| Lista | Archivo original | Archivo normalizado | Universo biológico |
| ----- | ---------------- | ------------------- | ------------------ |

## Resultado de la confrontación

Preferentemente conteos en S21.

## Hipótesis

| Grupo | Hipótesis principal | Evidencia a favor | Alternativas abiertas | Confianza | Evidencia pendiente |
| ----- | ------------------- | ----------------- | --------------------- | --------- | ------------------- |

## Conclusión provisional

Debe indicar:

* qué parte concuerda;
* qué parte difiere;
* qué diferencias se explican por alcance;
* qué permanece indecidible;
* qué se medirá en S22.

---

# Preparación para S22

El puente debe ser coherente.

S21 deja:

* listas de discrepancias;
* grupos preliminares;
* conteos simples;
* preguntas de magnitud.

S22 debe responder preguntas como:

* ¿cuánto miden los genes discrepantes?
* ¿qué proporción representan dentro de grupos definidos?
* ¿cómo se distribuyen por replicón?
* ¿qué longitud total aportan?
* ¿qué patrones aparecen al combinar varias columnas?

No afirmes que S21 no puede calcular ninguna proporción si ya utilizó porcentajes.

Mantén como limitación principal:

> comparar identidades no permite medir magnitud, distribución ni relaciones entre múltiples atributos.

---

# Elementos que debes conservar

No cambies:

* el título general de S21;
* la narrativa S18–S23;
* la ausencia de herramientas Unix nuevas;
* la distinción coherencia interna / evidencia externa;
* la política de S20 como hipótesis de partida;
* la confrontación mediante tres zonas;
* la interpretación de discrepancias;
* el protocolo acumulativo;
* la rúbrica;
* el cierre con IA;
* el puente hacia S22;
* las figuras conceptuales, salvo ajustes de texto necesarios.

---

# Verificación técnica obligatoria

Antes de entregar la versión corregida, comprueba:

1. que todos los archivos mencionados se generan previamente;
2. que no se compara una lista original con otra normalizada;
3. que las dos listas representan universos biológicos equivalentes;
4. que `comm` recibe listas ordenadas;
5. que los nombres de archivos son consistentes en toda la sesión;
6. que el encabezado no entra en la lista;
7. que los valores múltiples se procesan según el delimitador real;
8. que cada descarte queda contado;
9. que la descarga puede verificarse mediante checksum;
10. que existe un plan de respaldo;
11. que ninguna proporción contradice el propósito de S22;
12. que los comandos no dependen de columnas no definidas;
13. que el estudiante puede reproducir la exportación canónica;
14. que la interpretación no presenta independencia total cuando solo es parcial.

---

# Forma de trabajo

Realiza el ajuste en dos fases.

## Fase 1 — Informe de cambios

Antes de modificar el archivo, genera una tabla:

| Hallazgo | Sección afectada | Cambio que aplicarás | Riesgo que corrige |
| -------- | ---------------- | -------------------- | ------------------ |

Incluye únicamente cambios que realmente aplicarás.

## Fase 2 — Lección corregida

Entrega el archivo completo corregido.

No insertes comentarios editoriales dentro del material del estudiante.

No resumas.

No generes una sesión nueva.

Haz una edición controlada sobre la lección existente.

---

# Criterio final

La versión final debe permitir que un estudiante responda con precisión:

* ¿qué hace parcialmente independiente a la segunda fuente?
* ¿qué universo biológico representa cada lista?
* ¿por qué no puedo comparar todos los `locus_tag` con todo UniProt?
* ¿qué archivos son originales y cuáles normalizados?
* ¿qué significa cada zona de la confrontación?
* ¿qué diferencias son de alcance y cuáles requieren hipótesis?
* ¿qué evidencia apoya mi hipótesis?
* ¿qué alternativas siguen abiertas?
* ¿qué preguntas requieren medición en S22?

El resultado debe conservar la fuerza narrativa de S21, pero ser técnicamente ejecutable, reproducible y epistemológicamente preciso.



