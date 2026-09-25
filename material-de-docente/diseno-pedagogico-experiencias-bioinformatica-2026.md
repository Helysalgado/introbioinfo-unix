# Diseño pedagógico de experiencias activas e interactivas

## Introducción a la Bioinformática · LCG--UNAM · 2026

> **Documento de diseño pedagógico.** Este documento traduce la
> descripción detallada del curso y el Plan de Clases S1--S34 en una
> propuesta razonada de experiencias de aprendizaje. No reemplaza el
> Plan de Clases: explica **qué dinámica conviene, dónde, para qué y por
> qué**.

## 1. Punto de partida

El curso no busca enseñar una colección de comandos. Integra tres
dimensiones: **biológica**, **computacional** y **científica**. La
progresión central es:

``` text
pregunta biológica
→ evidencia necesaria
→ datos
→ operación
→ herramienta
→ resultado
→ verificación / validación
→ interpretación
→ conclusión + límites
```

Por ello, una salida correcta de terminal no basta. El estudiante debe
explicar qué hizo, por qué, qué obtuvo, cómo sabe que es correcto y qué
puede ---y no puede--- concluir.

## 2. Principio de diseño

Las dinámicas no se incorporan para decorar una sesión. Se incorporan
cuando provocan una acción cognitiva que conviene practicar
explícitamente:

``` text
¿Qué debe aprender?
→ ¿qué debe hacer cognitivamente?
→ ¿qué evidencia mostraría que aprendió?
→ ¿qué experiencia provoca esa acción?
→ ¿qué herramienta o dinámica conviene?
```

**Primero se selecciona la competencia; después la dinámica.**

## 3. Progresión cognitiva

``` text
RECORDAR → COMPRENDER → PREDECIR → DECIDIR → EJECUTAR
→ VERIFICAR → INTERPRETAR → ARGUMENTAR → DEFENDER → AUDITAR
```

  Acción                   Medio preferente
  ------------------------ ---------------------------------------
  Recuperar conceptos      Flashcards
  Reconocer / clasificar   HTML, tarjetas
  Predecir                 HTML + discusión
  Elegir estrategia        Caso, árbol de decisión
  Ejecutar                 Terminal, BLAST, servidor, HPC
  Diagnosticar             Bug Hunt, Incident Response
  Comparar                 Battle of Pipelines
  Interpretar              Caso progresivo
  Argumentar               Peer Review, juicio
  Integrar                 Mini-proyecto, Boss Battle, Hackathon
  Auditar IA               Catch the AI, Humano vs IA

## 4. La interactividad no sustituye la autenticidad

Unix, SSH, `grep`, `sed`, `awk`, scripting, BLAST, bases de datos y HPC
deben practicarse realmente.

``` text
FLASHCARDS
recuperar
   ↓
HTML / CASO
predecir y decidir
   ↓
TERMINAL / BLAST / HPC
ejecutar
   ↓
VERIFICACIÓN
comprobar
   ↓
PROTOCOLO
interpretar y documentar
   ↓
DEFENSA
argumentar
```

## 5. Familias de experiencias

### Recuperación

Flashcards, matching y mini-quizzes para conceptos que deben estar
disponibles mentalmente: formatos, métricas, distinciones, vocabulario y
símbolos.

### Razonamiento

HTML interactivo, clasificación, prediction--reveal, casos progresivos y
árboles de decisión para obligar a decidir antes de ejecutar.

### Ejecución auténtica

Terminal, bases, BLAST, scripts y cluster. Una competencia operacional
no se adquiere observando una simulación.

### Argumentación científica

Peer Review, Galería de soluciones, Defiende tu interpretación y Juicio
científico para aprender a justificar y reconocer límites.

### Auditoría

Catch the AI, Humano vs IA y Bug Hunt para evaluar respuestas plausibles
en lugar de delegar el juicio.

# 6. Dinámicas transversales

## Catch the AI

**Por qué:** la regla del curso es "primero a mano; después con IA".
Conviene convertir la verificación de IA en una práctica recurrente.

``` text
U1–U2: error conceptual/sintaxis
→ U3: fuente, formato, versión
→ U4: filtro, conteo, transformación
→ U5: script no robusto/reproducible
→ U6: sobreinterpretación biológica
```

La meta es pasar de "¿me dio un comando?" a "¿qué afirmó, cómo lo
verifico y hasta dónde está sustentado?".

## ¿Qué sabes realmente?

Clasificación recurrente:

``` text
OBSERVÉ
CALCULÉ
INTERPRETÉ
INFERÍ
```

**Por qué:** hace visible que salida computacional, evidencia e
inferencia no son equivalentes.

## Predice antes de ejecutar

Antes de Enter: **¿qué esperas obtener y por qué?**

``` text
predicción → ejecución → contraste → explicación
```

**Por qué:** evita el ensayo y error sin modelo mental.

# 7. Diseño por unidades y sesiones

## U1 · S1--S2 --- Trabajo reproducible y comunicación

**Propósito pedagógico:** establecer hábitos antes de la complejidad
técnica.

### S1 --- Markdown y fases del análisis

**Dinámica:** Mapa de decisiones
`pregunta → evidencia → dato → operación → herramienta → verificación → conclusión`.

**Razón:** establece desde el principio que el comando es solo un
peldaño del razonamiento.

**Complemento:** Galería de protocolos: comparar uno reproducible con
otro incompleto.

### S2 --- FAIR + IA

**Dinámica:** Catch the AI #1.

**Dinámica:** ¿Qué falta para reproducirlo? Dar un resultado sin
versión, fuente, parámetros o identificador.

**Razón:** vuelve observable la necesidad de metadatos y validación.

------------------------------------------------------------------------

## U2 · S3--S6 --- Entorno Unix/Linux

**Propósito:** fluidez operacional real. La mayor parte del tiempo debe
permanecer en terminal.

### S3 --- SSH

**Dinámica:** Mapa del viaje del dato: local → red → servidor →
directorio remoto.

**Razón:** construir el modelo mental local/remoto antes de memorizar
comandos.

### S4 --- Sistema de archivos

**Dinámica:** Path Challenge: predecir rutas absolutas/relativas y
después comprobar.

### S5 --- Permisos y procesos

**Dinámica:** Incident Cards: "el script no ejecuta", "no puedo
modificar el archivo", "el proceso sigue corriendo".

**Razón:** aprender comandos como herramientas de diagnóstico.

### S6 --- Consolidación

**Dinámica:** Mini Escape Room del servidor: conectar → localizar →
inspeccionar → corregir permiso → transferir → verificar.

**Razón:** S6 integra sin introducir conceptos nuevos. Los retos deben
ejecutarse en el servidor real.

------------------------------------------------------------------------

## U3 · S7--S9 --- Datos y bases biológicas

**Propósito:** Unix comienza a operar objetos biológicos, no archivos
genéricos.

### S7 --- FASTA / GFF3 / GenBank

**Dinámica:** ¿Qué archivo necesito?

**Formato:** HTML + flashcards.

**Razón:** las flashcards construyen fluidez formato↔representación; el
HTML obliga a elegir a partir de una pregunta biológica.

### S8 --- Descarga e integridad

**Dinámica:** Unlock the Next Dataset. No avanzar sin registrar fuente,
identificador, versión y checksum.

**Razón:** convierte integridad y procedencia en condición operativa.

### S9 --- Transferencia

**Dinámica:** Cadena de custodia del dato: origen → descarga → checksum
→ transferencia → checksum → destino.

**Razón:** conecta transferencia con trazabilidad científica.

------------------------------------------------------------------------

## U4 · S10--S23 --- Investigación progresiva sobre un genoma

La progresión es:

``` text
reconocer → inventariar → filtrar → contar → resumir
→ precisar → extraer → normalizar → confrontar
→ condicionar/calcular → integrar
```

### S10 --- Flujos

**Dinámica:** Pipeline Cards; ordenar entrada→operación→salida antes de
construir tuberías reales.

### S11 --- Estructura tabular

**Dinámica:** Anatomía de un archivo, señalando columnas, delimitador,
encabezado, faltantes y campo biológico.

### S12 --- Filtrar y contar

**Dinámica:** Prediction Market. Predecir si dos estrategias producirán
el mismo conteo y justificar.

**Razón:** los conteos son evidencia, no números aislados.

### S13 --- Inventario

**Dinámica:** Galería de evidencia:
`afirmación → evidencia → comando → verificación`.

### S14--S15 --- Mini Proyecto I

**Dinámica:** Bioinfo Detective Agency.

**Razón:** ya son sesiones de investigación guiada; una narrativa de
expediente aporta coherencia sin sustituir datos ni terminal.

**No premiar velocidad:** evaluar evidencia, trazabilidad, verificación
e interpretación.

### S16 --- Revisión por pares

**Dinámica:** Peer Review científico: autor → revisor →
respuesta/corrección.

**Razón:** aprender evaluando evidencia ajena antes de la evaluación
individual.

### S17 --- Evaluación individual

**Dinámica:** ninguna gamificación.

**Razón:** debe conservar autenticidad y atribución individual de
competencia.

### S18 --- Regex

**Dinámica:** Regex Arena / Pattern Duel.

``` text
predice → prueba → detecta falso positivo/negativo → refina
```

**Razón:** excelente candidata a HTML interactivo.

### S19 --- Extracción

**Dinámica:** Match the Evidence: relacionar identificadores con
registros originales.

**Razón:** enfatiza correspondencia y trazabilidad.

### S20 --- Normalización

**Dinámica:** Same data or different data?

**Razón:** antes de `sed`/`tr`, decidir qué transformación conserva
significado.

### S21 --- Fuente independiente

**Dinámica:** Caso forense de discrepancia.

Hipótesis: versión, anotación, estrategia de conteo, faltantes o
normalización.

**Razón:** la validación deja de ser autorreferencial.

### S22 --- awk

**Dinámica:** Pipeline Auction.

**Razón:** obliga a decidir qué operaciones son necesarias antes de
pensar en sintaxis.

### S23 --- Protocolo ejecutable

**Dinámica:** Bioinfo Relay.

Un compañero debe reproducir parte del análisis usando solo archivos y
documentación.

**Razón:** hace tangible la reproducibilidad y crea la necesidad de U5:
repetir manualmente ya es tedioso.

------------------------------------------------------------------------

## U5 · S24--S29 --- Automatización

Narrativa:

``` text
guardar procedimiento → separar procedimiento/datos → iterar
→ herramienta → defender reproducibilidad → escalar
```

### S24 --- Protocolo a script

**Dinámica:** Manual vs Script.

**Razón:** automatizar debe preservar la lógica y reproducir la línea
base.

### S25 --- Parámetros

**Dinámica:** Break My Script. Otro estudiante prueba entradas
alternativas.

**Razón:** hace visible la necesidad de parámetros, validación y
mensajes.

### S26 --- Lotes

**Dinámica:** Batch Challenge.

**Razón:** la competencia no es escribir `for`, sino mantener
trazabilidad entrada→salida en una colección.

### S27 --- Herramienta científica

**Dinámica:** Clínica de pipelines.

Diagnosticar README insuficiente, sobrescritura, ausencia de validación,
mensajes pobres o pérdida de parámetros.

**Razón:** la calidad científica del software se convierte en evidencia.

### S28 --- Proyecto integrador

**Dinámica:** Hackathon reproducible + Peer Review.

Categorías: reproducibilidad, validación, documentación, prueba con
datos nuevos, límites, auditoría de IA.

**Razón:** aporta energía al cierre sin convertirlo en carrera; la
evidencia auténtica sigue siendo herramienta + README + reporte +
defensa.

### S29 --- HPC/SGE

**Dinámica:** Mission Control.

Interpretar estado, `.out`, `.err`, éxito/fallo y justificar necesidad
de HPC.

**Razón:** comprender infraestructura sin perder la lógica científica.

------------------------------------------------------------------------

## U6 · S30--S34 --- Comparar, buscar, interpretar, inferir y defender

``` text
S30 COMPARAR
→ S31 BUSCAR
→ S32 INTERPRETAR
→ S33 INFERIR
→ S34 INTEGRAR Y DEFENDER
```

Aquí la interactividad tiene su mayor valor.

### S30 --- Alineamientos

**Dinámica:** Alignment Detective + flashcards.

Flashcards: match, mismatch, gap, identidad, similitud, cobertura.

**Razón:** recuperar conceptos reduce carga cognitiva; el caso obliga a
interpretarlos.

### S31 --- BLAST

**Dinámica:** BLAST Inside: semilla → extensión → evaluación; después
BLAST real.

**Razón:** evitar aprender BLAST como "pegar secuencia y pulsar botón".

### S32 --- Lista de hits

**Dinámica:** Compare the Evidence.

Comparar identidad, cobertura, E-value, bit score y HSP según la
pregunta.

**Feedback:** elección → pista → revisar otra métrica → segundo intento
→ explicación.

**Razón:** candidata prioritaria a HTML. Confronta la intuición de que
una sola métrica o el primer hit equivalen a conclusión.

### S33 --- Homología

**Dinámica emblemática:** Juicio de la Homología.

Afirmación: "X es ortóloga de Y".

Roles: Defensa, Fiscalía, Jurado.

**Razón:** obliga a separar similitud observada de inferencia evolutiva
y a declarar evidencia faltante.

**IA:** Catch the AI avanzado sobre transferencia injustificada de
función.

### S34 --- Caso ciego

**Dinámica emblemática:** Final Boss --- La secuencia desconocida.

``` text
verificar FASTA → pregunta → estrategia → búsqueda
→ evidencia → interpretación → hipótesis → alternativas
→ auditoría IA → límites → defensa
```

**Razón:** integra competencias; no introduce contenido nuevo.

**Éxito:** no "adivinar la proteína", sino construir una hipótesis
reproducible y defendible con límites explícitos.

# 8. Cuatro experiencias que pueden dar identidad al curso

1.  **Catch the AI** --- auditoría crítica transversal.
2.  **Bioinfo Relay (S23)** --- experimentar la necesidad de
    reproducibilidad.
3.  **Juicio de la Homología (S33)** --- argumentar inferencia
    científica.
4.  **Final Boss: secuencia desconocida (S34)** --- integrar el curso
    completo.

Estas cuatro representan competencias centrales y no son decoración.

# 9. Papel de las flashcards

Son **infraestructura cognitiva**, no evaluación central.

Sí: conceptos, distinciones, ES--EN, formato↔propósito,
métrica↔interpretación, símbolos y errores frecuentes.

No: comandos largos, scripts, pipelines, opciones raras, resultados
específicos o conclusiones complejas.

> Si recordar el concepto libera recursos mentales para razonar después,
> la flashcard tiene sentido.

# 10. Papel del HTML

El HTML vale cuando permite:

``` text
predecir → elegir → recibir pista → revisar → reintentar → explicar
```

Candidatas fuertes: **S7, S11, S12, S18, S20, S21, S30, S31, S32 y
S33**.

No debe usarse solo para trasladar preguntas de Markdown a una pantalla
bonita.

# 11. Aula invertida

### Antes

Flashcards, lectura, predicción, mini-caso.

### Durante

Ejecución real, contraste, diagnóstico, discusión y corrección.

### Después

Interpretación, documentación y actualización del protocolo.

La preparación previa **habilita** la clase; no la sustituye.

# 12. El protocolo como hilo conductor

Las dinámicas no deben desaparecer al acabar la clase:

``` text
dinámica → decisión → ejecución → evidencia → interpretación → protocolo
```

Ejemplos:

-   Prediction Market → predicción + resultado.
-   Caso forense → causa de discrepancia.
-   Relay → mejoras documentales.
-   Juicio → límites/evidencia faltante.
-   Final Boss → informe reproducible.

# 13. Progresión de IA

  Unidad   Pregunta de auditoría
  -------- -----------------------------------------------------------
  U1       ¿La respuesta parece confiable y cómo la verificaría?
  U2       ¿El comando existe y hace lo que afirma?
  U3       ¿Fuente, formato, identificador y versión son correctos?
  U4       ¿El procedimiento produce y valida el resultado esperado?
  U5       ¿El script es robusto, reutilizable y reproducible?
  U6       ¿La interpretación biológica está sustentada?

La dificultad progresa de **verificación técnica** a **juicio
científico**.

# 14. Evaluación

### Formativa

Flashcards, HTML, Prediction Market, Bug Hunt, Catch the AI y
colaboración.

### Evidencia auténtica

Terminal, datos reales, protocolo, script, BLAST, documentación y
defensa.

### Individual

S17 debe conservar condiciones que permitan atribuir la competencia al
estudiante.

# 15. Riesgos y mitigación

  Riesgo                      Mitigación
  --------------------------- -----------------------------------------------
  Gamificación superficial    Declarar la acción cognitiva que provoca
  Demasiadas plataformas      Pocos patrones reutilizables
  Sustituir terminal          HTML prepara; terminal demuestra
  Competencia por velocidad   Evaluar evidencia y reproducibilidad
  Flashcards mecánicas        Solo conocimiento de alta utilidad conceptual
  IA como árbitro             Verificación independiente
  Dinámicas aisladas          Regresar decisiones/evidencia al protocolo

# 16. Implementación gradual

## Fase 1 --- Alto impacto

1.  Catch the AI recurrente.
2.  Flashcards acumulativas.
3.  HTML S18 --- Regex.
4.  HTML S32 --- evidencia BLAST.
5.  Bioinfo Relay S23.
6.  Juicio de la Homología S33.
7.  Final Boss S34.

## Fase 2

S7 formato/evidencia; S11 anatomía; S20 normalización; S21 caso forense;
S27 Clínica; S29 Mission Control.

## Fase 3

Escape Room, Detective Agency extendida, Sala de juego, Hackathon y Boss
Battles adicionales.

# 17. Evaluar si una dinámica debe permanecer

Después de probarla:

1.  ¿Hizo que los estudiantes razonaran antes de ejecutar?
2.  ¿Hizo visible un error conceptual?
3.  ¿Mejoró la discusión?
4.  ¿Produjo evidencia útil?
5.  ¿Se transfirió a la práctica/protocolo?
6.  ¿Su costo de preparación fue razonable?
7.  ¿Una pregunta sencilla habría logrado exactamente lo mismo?

Si la respuesta a la última es sí, probablemente la dinámica no necesita
existir.

# 18. Arquitectura pedagógica resultante

``` text
PREGUNTA BIOLÓGICA
        ↓
RECORDAR — flashcards
        ↓
RAZONAR — HTML / casos / tarjetas
        ↓
PREDECIR
        ↓
HACER — Unix / bases / BLAST / scripts / HPC
        ↓
VERIFICAR — controles / contraste
        ↓
INTERPRETAR — protocolo
        ↓
DEFENDER — peer review / juicio / proyecto
        ↓
AUDITAR — humano ↔ IA
        ↓
REVISAR LA HIPÓTESIS
```

# 19. Síntesis

El diseño no transforma el curso en una colección de juegos. Crea
**experiencias diferentes para operaciones cognitivas diferentes**.

La terminal sigue siendo central para ejecutar; el protocolo para
documentar; los datos reales para investigar. Las nuevas dinámicas
ocupan espacios específicos:

-   flashcards para **recuperar**;
-   HTML para **decidir**;
-   predicción para **anticipar**;
-   Bug Hunt para **diagnosticar**;
-   Relay para **experimentar reproducibilidad**;
-   Peer Review para **evaluar evidencia**;
-   Juicio para **argumentar**;
-   Catch the AI para **auditar**;
-   Final Boss para **integrar**.

La meta final no es que el estudiante diga solamente "sé usar Unix,
`awk` y BLAST", sino que pueda demostrar:

> **Sé enfrentar una pregunta bioinformática, identificar qué evidencia
> necesito, elegir y ejecutar una estrategia, verificar sus resultados,
> interpretar qué significan, reconocer hasta dónde llega la evidencia y
> defender una conclusión reproducible.**

## Documentos internos de referencia

-   `descripcion-detallada-curso-introduccion-bioinformatica-2026.md`
-   `Plan-Clases-BioInfo-2026-final-S34.xlsx` --- hoja
    `PlanClases-2026-final S34`
-   `Programa-Introduccion-Bioinformatica-2026-actualizado.md`
-   `repertorio-experiencias-aprendizaje-bioinformatica-2026.md`

Este documento debe actualizarse si cambia el Plan operativo o el canon
pedagógico del curso.
