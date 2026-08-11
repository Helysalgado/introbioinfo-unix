# Ajuste final de la Sesión S20 — precisión técnica, alcance y carga cognitiva

Actúa como **editor académico y especialista en enseñanza universitaria de bioinformática, reproducibilidad científica y herramientas Unix**.

Debes revisar el archivo:

`u4-s20-normalizar-datos-comparables.md`

La sesión ya fue revisada editorialmente y su contenido conceptual es sólido.

No debes reescribirla desde cero.

Tu tarea consiste en realizar una **revisión final de precisión técnica y coherencia didáctica**, aplicando únicamente los ajustes descritos en este documento.

---

# Principio rector

Este no es un curso de Unix ni de limpieza de datos.

Es un curso de Bioinformática cuyo hilo narrativo es:

```text
S18  Seleccionar la evidencia
S19  Identificar el objeto biológico
S20  Normalizar la evidencia para compararla
S21  Confrontar fuentes independientes
S22  Cuantificar e interpretar
S23  Integrar evidencia
```

S20 debe conservar como competencia central:

> Definir, aplicar y validar una política de normalización antes de comparar datos biológicos.

Las herramientas deben seguir apareciendo únicamente porque permiten responder una pregunta científica.

---

# Objetivo de la revisión

Realiza ajustes puntuales para:

1. mantener a la normalización como centro de la sesión;
2. reducir la carga cognitiva secundaria;
3. corregir inconsistencias técnicas;
4. evitar afirmaciones demasiado absolutas;
5. asegurar que todos los comandos permitan reproducir exactamente los productos solicitados;
6. conservar el puente natural hacia S21.

No agregues nuevos temas.

---

# Ajustes de prioridad alta

## 1. Revisar el alcance de “Tu primer dato derivado”

La sección dedicada a `data/processed/` y la Práctica 7 introducen una segunda competencia importante:

* diseñar una tabla derivada;
* seleccionar columnas;
* agregar encabezados;
* convertir formatos;
* documentar valores faltantes;
* construir un diccionario de datos;
* verificar integridad.

Esto puede desplazar el objetivo central de S20.

Revisa esta sección para que funcione únicamente como una **aplicación breve y natural de la normalización**, no como un segundo módulo completo.

Debes conservar:

* la diferencia entre `data/source/`, `data/processed/` y `results/`;
* la idea de que un derivado debe ser regenerable;
* el diccionario de datos;
* el vínculo con S21.

Pero reduce la explicación secundaria y evita que la creación de la tabla opaque la normalización de identificadores.

La sesión debe seguir recordándose como:

> “Aprendí a construir y validar datos comparables”.

No como:

> “Aprendí a convertir un GFF3 en una tabla”.

---

## 2. Resolver la aplicación de la política a la tabla derivada

Actualmente se muestra un comando que selecciona las columnas:

```bash
grep -Ev '^#' data/source/anotacion.gff3 \
  | cut -f1,3,4,5,7
```

pero ese comando conserva el identificador original de la columna 1.

Después se pide que la columna de replicón use la política de normalización.

Corrige esta inconsistencia.

El procedimiento final debe permitir:

* normalizar únicamente la columna del replicón;
* no modificar por accidente las demás columnas;
* producir exactamente la tabla derivada solicitada;
* utilizar únicamente herramientas ya enseñadas o introducir claramente cualquier herramienta nueva.

Si las herramientas disponibles en S20 no permiten aplicar la política de manera segura a una columna de una tabla, no inventes una solución frágil.

En ese caso:

* conserva la tabla con los identificadores originales;
* incluye una columna adicional de clave normalizada mediante un procedimiento justificable;
* o declara explícitamente que la integración por columnas se completará en la sesión donde se introduzca la herramienta apropiada.

No uses una sustitución sobre toda la línea si podría modificar otras columnas.

---

## 3. Corregir la comprobación de idempotencia

La idempotencia se define como:

> Aplicar la política completa dos veces produce el mismo resultado que aplicarla una vez.

El ejemplo actual solo reaplica una sustitución con `sed`.

Modifícalo para que:

* se reaplique exactamente la misma política usada para producir el archivo;
* incluya todas las transformaciones pertinentes;
* compare la primera salida con la segunda;
* explique qué significa una salida vacía o una diferencia.

No presentes la idempotencia de una sola regla como idempotencia de toda la política.

---

## 4. Revisar el uso de `diff`

Comprueba si `diff` ya fue enseñado en sesiones anteriores.

Si ya fue enseñado:

* indícalo brevemente como herramienta recuperada;
* explica qué significa que no produzca salida.

Si no fue enseñado:

* no lo introduzcas de forma implícita;
* preséntalo con el formato editorial acordado:

```text
Sintaxis mínima
¿Qué hace?
¿Por qué aparece aquí?
```

o reemplázalo por una estrategia que use herramientas ya conocidas.

No presupongas comandos que el estudiante todavía no ha aprendido.

---

## 5. Revisar el tratamiento de líneas vacías

No clasifiques automáticamente eliminar líneas vacías como una transformación conservadora.

Una línea vacía puede indicar:

* un identificador ausente;
* una falla de extracción;
* una regla que eliminó todo el contenido;
* un registro incompleto;
* un problema del archivo.

Ajusta el texto para que una línea vacía:

1. primero se detecte;
2. después se investigue;
3. solo se elimine si se demuestra que es un artefacto sin significado.

Conserva el control de claves vacías dentro de la validación.

---

# Ajustes de prioridad media

## 6. Matizar la procedencia común

Evita afirmar de manera categórica:

> La comparación funcionó porque ambos archivos venían del mismo sitio.

Reformula la idea para expresar que:

* provenir del mismo ensamblado y productor aumenta la probabilidad de compatibilidad;
* no garantiza que los archivos tengan la misma versión o convención;
* precisamente por eso se auditan.

Mantén la continuidad con S19.

---

## 7. Revisar la conversión TSV → CSV

No presentes la sustitución de tabuladores por comas como una conversión general de TSV a CSV.

Aclara que el procedimiento es válido únicamente para la tabla concreta si se ha verificado que:

* los campos no contienen comas;
* no contienen saltos de línea internos;
* no necesitan comillas o escapes especiales.

Si la conversión a CSV no es indispensable para el objetivo de S20, muévela a:

* una nota de ampliación;
* una sección opcional;
* o elimínala de la ruta indispensable.

La tabla TSV debe ser el producto principal.

---

## 8. Revisar la estimación de tiempo

Evalúa si es realista que:

* las secciones 1–9 se lean en 45 minutos;
* las Prácticas 2–6 se completen en 120 minutos.

No reduzcas contenido solo para hacer cuadrar el tiempo.

Puedes:

* aumentar el tiempo estimado de lectura;
* marcar algunos apartados como consulta;
* trasladar controles secundarios al trabajo posterior;
* mantener en el taller únicamente los pasos esenciales.

El núcleo que no debe recortarse es:

```text
auditar
↓
definir política
↓
transformar
↓
validar colisiones
↓
comparar antes y después
```

---

## 9. Matizar “el resultado nunca valida la regla”

Conserva la idea, pero hazla epistemológicamente más precisa.

Debe quedar claro que:

* obtener más coincidencias no valida una regla;
* una salida visualmente limpia no valida una regla;
* el número final por sí solo no valida la transformación.

Pero los controles y la evidencia sí contribuyen a validarla:

* documentación de la fuente;
* cardinalidad;
* claves vacías;
* colisiones;
* idempotencia;
* trazabilidad.

Una formulación posible es:

> El aumento de coincidencias nunca valida por sí solo la regla.

No uses esta frase necesariamente; conserva la intención.

---

## 10. Revisar “por primera vez produces datos”

El estudiante ya produjo listas, inventarios y resultados en sesiones anteriores.

Precisa el cambio real:

> Por primera vez produce un dato derivado reutilizable como entrada de análisis posteriores.

Distingue:

* resultados de una consulta;
* archivos intermedios;
* datos derivados reutilizables.

---

# Ajustes editoriales menores

## 11. Evitar “tabla limpia”

El documento explica que normalizar no equivale a limpiar.

Por coherencia terminológica, sustituye expresiones como:

> tabla limpia

por términos más precisos:

* tabla derivada;
* tabla analítica;
* tabla reducida;
* representación tabular procesada.

Elige uno y úsalo de forma consistente.

---

## 12. Matizar la obligatoriedad universal de los controles

Los cuatro controles son muy valiosos para esta sesión:

* cardinalidad;
* claves vacías;
* colisiones;
* idempotencia.

Preséntalos como el **conjunto mínimo de validación que se aplicará en S20**, no necesariamente como una ley universal para cualquier transformación posible.

Mantén su obligatoriedad dentro de la práctica de esta sesión.

---

# Elementos que no deben cambiar

Conserva íntegramente:

* el título de la sesión;
* la filosofía de aula invertida;
* la narrativa S18 → S19 → S20 → S21;
* la distinción extraer / normalizar / comparar;
* la posibilidad de una política vacía;
* la auditoría previa;
* la clasificación de las transformaciones por riesgo;
* la conservación del original y la clave normalizada;
* la detección de colisiones;
* la comparación antes/después;
* la plantilla completa del protocolo;
* la rúbrica;
* el cierre con IA;
* el puente hacia S21.

No elimines prácticas completas.

No introduzcas `awk`, Python, R u otras herramientas que pertenecen a sesiones posteriores.

---

# Revisión de las prácticas

Después de los ajustes, comprueba que la progresión siga siendo:

```text
Práctica 1
Hipótesis inicial

↓

Práctica 2
Auditoría reproducible

↓

Práctica 3
Política de normalización

↓

Práctica 4
Aplicación de la política

↓

Práctica 5
Validación y colisiones

↓

Práctica 6
Comparación e interpretación

↓

Práctica 7
Dato derivado reutilizable para S21
```

La Práctica 7 debe ser una consecuencia de las anteriores, no una actividad independiente que podría realizarse sin haber normalizado.

---

# Verificación técnica obligatoria

Antes de entregar la nueva versión, revisa cada bloque de código y comprueba:

1. que el comando hace exactamente lo que el texto afirma;
2. que no modifica `data/source/`;
3. que los archivos de entrada existen según las sesiones anteriores;
4. que la salida se guarda en la carpeta correcta;
5. que ninguna regla actúa sobre columnas o fragmentos no deseados;
6. que `comm` recibe listas ordenadas;
7. que la prueba de idempotencia reaplica la política completa;
8. que los resultados solicitados por cada práctica pueden producirse con los comandos enseñados;
9. que una política vacía tiene una ruta reproducible;
10. que la tabla derivada puede regenerarse exactamente.

---

# Forma de trabajo

Realiza el ajuste en dos fases.

## Fase 1 — Informe breve

Antes de modificar el archivo, presenta una tabla con:

| Hallazgo | Sección afectada | Ajuste propuesto | Riesgo que corrige |
| -------- | ---------------- | ---------------- | ------------------ |

Incluye únicamente los ajustes que realmente aplicarás.

## Fase 2 — Documento corregido

Después entrega la sesión completa corregida.

No incluyas comentarios editoriales dentro del material del estudiante.

---

# Criterio final de calidad

La versión final debe permitir que un estudiante responda con claridad:

* ¿qué problema dejó S19?
* ¿por qué no puedo comparar cadenas sin auditar su representación?
* ¿cómo decido qué transformar?
* ¿qué transformaciones pueden destruir información?
* ¿cómo demuestro que no fusioné objetos distintos?
* ¿qué diferencia hay entre el original, la clave normalizada, un resultado y un dato derivado?
* ¿qué puedo llevar de forma confiable a S21?

La sesión debe terminar reforzando:

```text
Seleccionar
↓
Identificar
↓
Normalizar
↓
Confrontar
↓
Cuantificar
↓
Integrar
```

No conviertas la revisión en una expansión del documento.

El resultado debe ser una versión técnicamente más precisa, más enfocada y con menor carga cognitiva, conservando la profundidad científica y la arquitectura actual.



