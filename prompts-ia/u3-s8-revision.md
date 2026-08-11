# Revisión editorial integral de la Sesión S8

Actúa como **editor académico**, **profesor de bioinformática** y **revisor de un libro universitario** para la asignatura **Introducción a la Bioinformática** de la **Licenciatura en Ciencias Genómicas (LCG)**.

No estás escribiendo una nueva sesión.

Estás realizando la **última revisión editorial** antes de publicar el material.

La sesión ya está prácticamente terminada.

Tu objetivo es mejorarla sin cambiar su filosofía, estructura general ni estilo.

---

# Contexto

Esta sesión forma parte de una secuencia didáctica.

La S7 enseñó:

- genoma
- ensamblado
- accession
- versiones
- FASTA
- GFF3
- GenBank

La S8 enseña:

- bases de datos biológicas
- recuperación de datos
- selección de registros
- procedencia
- reproducibilidad
- verificación de integridad

La sesión NO debe convertirse en un manual de NCBI.

Debe seguir enseñando a pensar como un bioinformático.

---

# Filosofía

Mantener siempre el hilo conductor

Pregunta biológica

↓

Evidencia

↓

Datos

↓

Registro

↓

Archivos

↓

Reproducibilidad

Las herramientas son un medio.

Nunca el objetivo.

---

# Objetivos de esta revisión

NO cambiar el contenido conceptual.

NO agregar nuevas secciones.

NO aumentar considerablemente el tamaño del documento.

Sí realizar mejoras editoriales, didácticas y de coherencia.

---

# Ajustes obligatorios

## 1. Corregir la jerarquía conceptual de la sección 1

Actualmente aparece

Objeto biológico

↓

Registro

↓

Base de datos

↓

Formato

Debe quedar

Objeto biológico

↓

Base de datos

↓

Registro

↓

Archivos

↓

Formatos

porque un registro pertenece a una base de datos.

---

## 2. Mejorar la tabla del ecosistema NCBI

Agregar una columna adicional

**Ejemplo de identificador**

Ejemplo:

Assembly → GCF...

Genome → (vista integrada, sin accession propio)

Nucleotide → NC...

Gene → GeneID

Protein → WP...

Taxonomy → taxid

PubMed → PMID

La tabla debe complementar visualmente la Figura 2.

---

## 3. Aclarar Genome

Genome no debe parecer otra base de secuencias.

Explicar que funciona como una vista integrada de los ensamblados disponibles para un organismo.

---

## 4. Explicar ASM584v2

Agregar una nota indicando que

ASM584v2

es el nombre del ensamblado,

mientras que

GCF_000005845.2

es el accession estable de RefSeq.

---

## 5. Mejorar la Micropráctica 1

Agregar una pregunta que obligue a decidir entre

Assembly

y

Nucleotide.

Debe requerir razonamiento.

No memoria.

---

## 6. Mejorar la Práctica 1

Agregar al final una breve reflexión.

Ejemplo

¿Cuál fue el eslabón más difícil de justificar?

No requiere respuesta.

Solo reflexión.

---

## 7. Mejorar la Práctica 2

Agregar una restricción realista.

Ejemplo

"La conexión es lenta y solo puedes descargar los archivos estrictamente necesarios."

La actividad debe obligar a optimizar la selección.

---

## 8. Mejorar la Práctica 3

Usar un checksum realista (MD5 válido) en lugar de una cadena claramente inventada.

No importa el archivo.

Lo importante es que el formato sea auténtico.

---

## 9. Mejorar la Práctica 4

Agregar una actividad adicional.

Caso:

Un compañero propone renombrar

genome.fna

como

ecoli.fasta

porque "es más claro".

El estudiante debe justificar por qué NO debe hacerse dentro de

data/source.

---

## 10. Reubicar la Figura 4

Colocar la figura inmediatamente después del título de la sección de checksums,

antes del desarrollo del texto,

para que primero se vea el flujo completo.

---

## 11. Eliminar repeticiones

En varias prácticas vuelve a aparecer

organismo

↓

cepa

↓

ensamblado

↓

versión

↓

registro

Si ya fue explicado antes,

referenciar la sección correspondiente,

en lugar de repetir la cadena completa.

---

## 12. Sustituir "preflight"

Cambiar el encabezado

Preparación previa o preflight

por

Lista de verificación previa

o

Comprobación inicial.

Mantener consistencia editorial.

---

## 13. Agregar recuadros

Al final de las secciones principales agregar un pequeño cuadro

### Qué debes recordar

Con únicamente

3–4 ideas clave.

No repetir el contenido.

Solo reforzar.

---

## 14. Mejorar la Tarea 4

Agregar una lista de comprobación final.

Ejemplo

☐ Organismo

☐ Cepa

☐ Ensamblado

☐ Versión

☐ Colección

☐ Archivos

☐ Fecha

☐ Campos pendientes claramente marcados

Debe servir como lista de control antes de entregar.

---

## 15. Revisar congruencia

Verificar cuidadosamente que

- cada práctica utilice únicamente conceptos ya explicados;
- las figuras aparezcan inmediatamente después del texto que las introduce;
- no existan saltos conceptuales;
- la dificultad aumente progresivamente;
- cada práctica contribuya a los resultados de aprendizaje.

Si detectas una mejor ubicación para una figura, propón el cambio.

---

# Nivel esperado

Evalúa el documento como si fuera un manuscrito destinado a estudiantes de una

**Licenciatura en Ciencias Genómicas**.

No simplifiques.

No infantilices.

No conviertas la sesión en un tutorial de NCBI.

Debe conservar un nivel universitario.

---

# Entregable

Modifica directamente el documento.

No escribas un listado de sugerencias.

Aplica los cambios.

Si decides NO aplicar alguno de los ajustes anteriores, justifica brevemente por qué antes de continuar.

