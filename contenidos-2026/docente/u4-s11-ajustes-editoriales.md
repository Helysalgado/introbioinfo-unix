# S11 — Ajustes editoriales propuestos (para incorporación manual)

> **Cómo usar este documento.** Cada cambio indica **dónde** va, **qué texto sustituye** (citado por
> sus primeras palabras) y el **texto nuevo** listo para pegar. No altera estructura, orden de
> secciones, prácticas, resultados de aprendizaje, rúbrica ni protocolo. Los bloques colapsables
> siguen el formato `<details>` ya usado en el curso.

---

## 1. Lista de cambios propuestos

| # | Sección | Motivo | Beneficio didáctico |
| ---: | --- | --- | --- |
| C1 | §1, callout final | La idea "una pregunta apunta a una columna" ya se enuncia al cerrar *Relación con lo que ya sabes* | Elimina el eco y aprovecha el espacio para introducir la distinción **dato / operación** (Ajuste 4) |
| C2 | §2, lista de tres condiciones | La frase posterior ("Esa regularidad…") explica lo que la condición 3 ya dice | Un párrafo menos; la idea queda dentro de la condición que la genera |
| C3 | §2.1, párrafo "El FASTA no es peor…" | Reformula en prosa lo que la tabla comparativa acaba de mostrar | Reduce lectura redundante y conserva el argumento de fondo (representan objetos distintos) |
| C4 | §2.2, "trampa clásica" + ADVERTENCIA | Ambos dicen lo mismo: el delimitador equivocado no produce error | Un solo aviso, más contundente, con la comprobación en colapsable |
| C5 | §4, caja `cut -d` | Su justificación repite el argumento de §2.2 | Caja más corta; la justificación queda donde corresponde |
| C6 | §5, callout ¿SABÍAS QUE? | **Duplica casi literalmente** el ¿SABÍAS QUE? de S10 §2.2 (NA, NULL, celda vacía) | Evita repetir entre sesiones; lo sustituye una remisión breve y una pregunta de reflexión |
| C7 | §6, callout IMPORTANTE | Anticipa la conclusión que el cierre de la sesión desarrolla mejor | Evita decir dos veces "no puedes elegir qué líneas entran" |
| C8 | Práctica 2, pasos 2 y 4 | "Ve anotando qué aparece" es observación pasiva | Convertida en pregunta con hipótesis; respuesta en colapsable (Ajuste 2) |
| C9 | Práctica 3, pasos 3, 5 y 6 | Tres instrucciones de "anota" seguidas | Preguntas que exigen explicar el origen del dato; incorpora la reflexión **dato / operación** (Ajuste 4) y una respuesta colapsable |
| C10 | Práctica 4, paso 2 y cierre | Falta la valoración crítica de las evidencias | Nuevo bloque: jerarquizar tres evidencias y justificar el criterio (Ajuste 3), con respuesta colapsable |
| C11 | Práctica 5A, paso 3 | Las tres preguntas quedan sin cierre para quien estudia solo | Respuesta colapsable que confirma el diagnóstico sin adelantar S12 |
| C12 | Práctica 5B, tras el paso 3 | La aritmética es correcta pero abstracta | **Figura propuesta** que descompone visualmente los bytes del FASTA (Ajuste 5) |
| C13 | Práctica 5B, nota final | Oportunidad natural de reforzar la identidad de la unidad | Una frase: no mejoró el comando, mejoró la **evidencia** (Ajuste 6) |

Balance aproximado: **−28 líneas** por compactación, **+34 líneas** por preguntas y colapsables. La
sesión queda prácticamente igual de larga, pero con menos prosa expositiva y más razonamiento.

---

## 2. Texto nuevo

### C1 · Sección 1 — callout final

**Sustituye a:** `> **IMPORTANTE:** Esa es la operación que aprendes hoy, y es más conceptual que técnica…` (hasta *"¿qué dato mínimo necesito y dónde está?"*).

```markdown
> **IMPORTANTE:** Antes de ejecutar nada, dos preguntas ordenan todo el análisis: **¿qué dato mínimo
> necesito y dónde está?** y **¿basta con tenerlo o hace falta hacer algo con él?** La primera se
> resuelve localizando una columna; la segunda —contar, restar, ordenar— es una **operación**, y
> puede requerir herramientas que todavía no tienes. Distinguirlas evita buscar en el archivo lo que
> el archivo no puede darte.
```

---

### C2 · Sección 2 — lista de condiciones

**Sustituye a:** la condición 3 y el párrafo `Esa regularidad es lo que permite decir…`.

```markdown
3. Los campos están separados siempre por el mismo carácter, el **delimitador**, y aparecen siempre
   en el mismo orden. Gracias a eso, "el tercer campo" significa lo mismo en la línea 1 que en la
   línea 9 000.
```

---

### C3 · Sección 2.1 — párrafo posterior a la tabla

**Sustituye a:** `El FASTA no es peor ni está peor diseñado…` (párrafo completo).

```markdown
El FASTA no está peor diseñado: **representa otra cosa**. Un GFF3 describe objetos con atributos —esto
es un gen, empieza aquí, termina allá— y eso se organiza naturalmente en columnas. Un FASTA guarda una
cadena continua de caracteres, y una cadena continua no tiene columnas que pedir.
```

---

### C4 · Sección 2.2 — cierre del apartado

**Sustituye a:** el párrafo `Y hay una trampa clásica…` **y** el callout `> **ADVERTENCIA:** Si eliges el delimitador equivocado…`.

```markdown
Y aquí está la trampa: **el tabulador y los espacios se ven igual en pantalla**. No se distinguen
mirando, se distinguen probando.

> **ADVERTENCIA:** Elegir mal el delimitador **no produce ningún error**. Produce columnas
> equivocadas, o la línea entera tratada como un solo campo. Es el mismo error silencioso de las
> tuberías (S10, sección 6.1): el comando funciona, el resultado es válido, la respuesta es
> incorrecta.

<details>
<summary>¿Qué devuelve exactamente <code>cut</code> con el delimitador equivocado?</summary>

Si le pides `cut -d','` a una línea separada por tabuladores, `cut` busca comas, no encuentra
ninguna y concluye que la línea entera es **un solo campo**. Al pedirle el campo 1 devuelve la línea
completa; al pedirle el campo 3 no devuelve nada. Ninguna de las dos salidas es un mensaje de error:
por eso el problema puede pasar inadvertido durante todo un análisis.

</details>
```

---

### C5 · Sección 4 — caja de *Sintaxis mínima* de `cut -d`

**Sustituye a:** `**¿Por qué aparece en esta sesión?** Porque el tabulador es la excepción cómoda…`.

```markdown
**¿Por qué aparece en esta sesión?** Porque el tabulador de tu GFF3 es la excepción cómoda (§2.2): en
cuanto trabajes con una tabla descargada de un portal, tendrás que declarar el delimitador tú.
```

---

### C6 · Sección 5 — callout final

**Sustituye a:** el callout `> **¿SABÍAS QUE?:** Cada formato elige su propia marca de ausencia…` (duplica el de S10 §2.2).

```markdown
> **TIP:** Ya viste en S10 que cada formato elige su propia marca de ausencia. Antes de seguir,
> pregúntate: si mañana recibes una tabla donde las celdas vacías se rellenaron con `0`, ¿podrías
> distinguir una medición nula de un dato inexistente? ¿Qué información necesitarías pedir a quien te
> entregó el archivo?
```

---

### C7 · Sección 6 — callout final

**Sustituye a:** `> **IMPORTANTE:** Fíjate en que la última columna de esa tabla repite tres veces…`.

```markdown
> **IMPORTANTE:** Lee la última columna de la tabla completa: dice tres veces lo mismo con palabras
> distintas. Cuando una sola limitación bloquea tres preguntas a la vez, deja de ser un inconveniente
> y se convierte en el siguiente problema a resolver.
```

---

### C8 · Práctica 2 — pasos 2 y 4

**Sustituye a:** en el paso 2, la frase `Repite cambiando -f3 por -f1, -f2, -f4… hasta -f9. Ve anotando qué aparece en cada una.`

```markdown
   Repite cambiando `-f3` por `-f1`, `-f2`, `-f4`… hasta `-f9`. Antes de ejecutar cada uno, **predice
   qué esperas ver**; después compara. ¿En qué columnas te equivocaste y qué te hizo suponer otra cosa?
```

**Sustituye a:** en el paso 4, `¿Qué devolvió? ¿Por qué? Anótalo: es la demostración de que un delimitador mal elegido **no produce un error**.`

```markdown
   ¿Qué obtuviste en cada caso: un mensaje de error, nada, o la línea completa? ¿Qué hipótesis
   explica esa diferencia?

<details>
<summary>Ver retroalimentación</summary>

Pedir una columna inexistente (`-f15`) no devuelve nada: el campo simplemente no existe. Pedirla con
el delimitador equivocado (`-d','`) devuelve la **línea completa**, porque sin comas `cut` considera
que toda la línea es el campo 1. En ninguno de los dos casos hay mensaje de error: la herramienta
hace exactamente lo que se le pidió, aunque no sea lo que querías.

</details>
```

---

### C9 · Práctica 3 — pasos 3, 5 y 6

**Sustituye a:** en el paso 3, `**Anota lo que ves al principio del archivo.** Esa observación es la clave del cierre de la sesión.`

```markdown
   ¿Todo lo que aparece ahí es un tipo de *feature*? ¿Qué hipótesis explica lo que no lo es? Guarda tu
   respuesta: es la clave del cierre de la sesión.
```

**Sustituye a:** en el paso 5, `¿Qué columna tiene más puntos? ¿Es coherente con lo explicado en la Sección 5?`

```markdown
   ¿Cuál de las dos columnas tiene más puntos? ¿La causa es la misma en ambas? Relaciona tu respuesta
   con la diferencia entre "no aplica" y "no disponible" (Sección 5).
```

**Sustituye a:** el paso 6 completo (`Calcula a mano la longitud del primer feature…`).

```markdown
6. Calcula a mano la longitud del primer *feature* de tu archivo con las coordenadas del paso 4.
   Antes de hacerlo responde: **¿ya tienes el dato que responde "qué longitud tiene este gen", o
   todavía necesitas una operación sobre él?** ¿Cuál?

<details>
<summary>Ver retroalimentación</summary>

El dato no está en el archivo: en el GFF3 no existe ninguna columna "longitud". Lo que tienes son dos
datos —inicio y fin— y lo que falta es una **operación** sobre ellos: `end - start + 1`. El `+1`
existe porque ambos extremos se incluyen; un elemento que va de 190 a 255 mide 66 bases, no 65.

Esta distinción reaparecerá en toda la unidad: algunas preguntas se responden **localizando** un dato
y otras exigen **operar** sobre varios. Las segundas necesitan herramientas que aún no tienes.

</details>
```

---

### C10 · Práctica 4 — paso 2 y nuevo bloque de valoración crítica

**Sustituye a:** el paso 2, `Anota qué identificadores distintos aparecen en esas dos ventanas. ¿Son los mismos al principio y al final del archivo?`

```markdown
2. ¿Qué identificadores distintos aparecen en cada ventana? ¿Son los mismos al principio y al final
   del archivo? Si lo son, ¿qué te permite concluir eso… y qué no?
```

**Se añade** justo después del paso 5 (el bloque `Evidencia 1 / Evidencia 2 / Evidencia 3…`), antes de **Producto**:

```markdown
6. **Valora tus evidencias.** Tienes tres, pero no tienen por qué valer lo mismo. Responde por
   escrito:

   - ¿Cuál de las tres consideras más confiable para responder esta pregunta? ¿Por qué?
   - ¿Alguna de ellas es *independiente* de las otras, o dos provienen en el fondo de la misma fuente?
   - Si una contradijera a las otras dos, ¿cuál conservarías y qué harías para decidir?

<details>
<summary>Ver retroalimentación</summary>

No hay una única respuesta correcta, pero sí un razonamiento esperable.

Las directivas `##sequence-region` son la evidencia más fuerte: son una **declaración explícita** de
quien construyó el archivo, y además aportan la longitud de cada replicón. Los encabezados del FASTA
son igual de explícitos, pero solo dicen cuántas secuencias hay, no qué son.

La columna 1 del GFF3 es la evidencia **más débil de las tres**, aunque parezca la más "de datos": la
obtuviste mirando dos ventanas del archivo, no el archivo entero, así que como mucho demuestra que
esos identificadores existen — nunca que no haya otros en medio.

Sobre la independencia: FASTA y GFF3 del mismo ensamblado provienen del mismo proceso de anotación, de
modo que su coincidencia es menos informativa de lo que parece. Coinciden porque describen el mismo
material, no porque dos laboratorios independientes hayan llegado al mismo resultado.

Y si hubiera contradicción, lo correcto no es elegir: es **documentar la discrepancia** y buscar una
fuente externa —la página del ensamblado en la base de datos de origen, registrada en tu ficha de
procedencia de U3—.

</details>
```

---

### C11 · Práctica 5A — respuesta colapsable del paso 3

**Se añade** inmediatamente después de las tres preguntas del paso 3, antes del callout `> **IMPORTANTE:** cut no distingue…`.

```markdown
<details>
<summary>Ver retroalimentación</summary>

Las tres respuestas son "no", y por razones distintas:

1. **No puedes garantizarlo.** Viste 60 líneas de más de nueve mil. Una ventana no es una muestra
   representativa: es simplemente lo que cabía en pantalla.
2. **No puedes enumerarlos.** Aunque las vieras todas, tendrías una lista con miles de repeticiones y
   ninguna forma de reducirla a los valores distintos sin contarlos a mano.
3. **No puedes quitar los comentarios.** `cut` corta por columnas, no elige líneas.

Que tu respuesta sea provisional no es un defecto del trabajo: es una descripción honesta del alcance
de la evidencia. Anotarlo así en el protocolo vale más que un número presentado como definitivo.

</details>
```

---

### C12 · Práctica 5B — figura propuesta *(no generada)*

**Lugar de inserción:** dentro de la **Práctica 5, Parte B**, inmediatamente después del bloque de
texto del **paso 3** (el esquema `líneas de secuencia ≈ … / bases estimadas ≈ …`) y antes del paso 4.

**Título del archivo sugerido:** `images/figura-u4-s11-composicion-fasta.png` (+ `.svg` editable).

**Pie de figura:**

```markdown
*Figura 2. De qué están hechos los bytes de un archivo FASTA. Solo una parte del archivo es secuencia
biológica: el resto son encabezados y saltos de línea. Medir el archivo no es medir el genoma.
Elaboración propia.*
```

**Texto alternativo:**

```markdown
![Barra horizontal que representa el total de bytes de un archivo FASTA descompuesta en tres partes: una franja muy pequeña de encabezados, una franja delgada de saltos de línea que equivale aproximadamente al 1.4 % del total, y una franja mayoritaria de secuencia biológica que constituye el tamaño real del genoma; debajo, la resta que permite estimar las bases a partir de los bytes totales.](../images/figura-u4-s11-composicion-fasta.png)
```

**Descripción para quien la dibuje.** Una **barra horizontal apilada** que ocupe el ancho útil,
etiquetada arriba como *"bytes totales del archivo (lo que mide `wc -c`)"*, dividida en tres
segmentos, de izquierda a derecha y **a escala real**:

1. un segmento mínimo, casi una línea, en color de acento cálido → `encabezados (>...)`;
2. un segmento delgado, ≈ 1.4 % del total, en color de aviso → `saltos de línea (uno cada 70 bases)`;
3. el resto, dominante, en el verde del curso → `secuencia biológica = el genoma`.

Debajo de la barra, una llave que abarque solo el tercer segmento con la etiqueta *"esto es lo que
querías medir"*. Y al pie, la resta en tipografía monoespaciada:

```text
bases estimadas  ≈  bytes totales  −  saltos de línea  −  encabezados
```

Mismo estilo gráfico que las figuras previas de la unidad (1600 × 900, paleta y tipografías de
`figura-u4-s10-flujos-estandar.svg`). Debe quedar claro visualmente que **la exageración del error de S10
es pequeña pero sistemática**: los dos primeros segmentos son estrechos, no despreciables.

---

### C13 · Práctica 5B — nota final

**Se añade** al final del callout `> **NOTA — esto es una estimación, no una medición.**`, como última
frase del mismo callout.

```markdown
> Aun así, compara ambos momentos: en S10 tenías un número del que solo sabías que estaba mal; hoy
> tienes uno con el error acotado y contrastado contra una fuente independiente. No cambió la
> pregunta ni apareció un comando milagroso: mejoró la **calidad de tu evidencia**.
```
