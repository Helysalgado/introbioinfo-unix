# Bitácora de uso de IA

## Actividad
Revisión de la estrategia para responder la pregunta:

**¿Cuántos genes tiene el genoma de E. coli K-12 y cómo
se distribuyen en el cromosoma?**

## Fecha
4 de septiembre de 2026

## Herramienta y modelo
- Aplicación: ChatGPT
- Modelo: [anotar el modelo utilizado]

## Material proporcionado

- `protocolo.md`
- `genes_ecoli.gff`
- `genes_ecoli-metadatos.md`

## Prompt

Evalúa la estrategia que propuse para responder mi pregunta
biológica utilizando los datos disponibles.

Para cada subpregunta, indica qué está bien, qué debería revisar
y por qué.

No proporciones comandos y no sustituyas mi estrategia por una
nueva. No asumas información que no esté en los materiales
proporcionados.

Para cada observación, indica en qué información te basaste.
Si necesitas información adicional, señálalo.

## Respuesta relevante de la IA

La IA indicó, entre otras cosas:

1. Contar los registros de tipo `gene` en el GFF es una estrategia
   adecuada para estimar el número de genes anotados.

2. La hebra `+` o `-` puede utilizarse para estudiar la distribución
   de los genes por hebra.

3. El tamaño total del genoma no debería obtenerse simplemente
   a partir de la última coordenada de un gen del archivo.

## Verificación

### Observación 1
**IA:** contar registros `gene`.

**¿Cómo lo comprobé?**
Revisé `genes_ecoli.gff` y observé que existen registros cuyo tipo
es `gene`.

**Decisión:** ACEPTAR.

**¿Por qué?**
El tipo de registro está presente directamente en los datos.

### Observación 2
**IA:** utilizar `+` y `-` para distinguir las hebras.

**¿Cómo lo comprobé?**
Revisé el archivo GFF y encontré esos símbolos en el campo
correspondiente a la hebra.

**Decisión:** ACEPTAR.

### Observación 3
**IA:** no usar la última coordenada de un gen como tamaño
del genoma.

**¿Cómo lo comprobé?**
No puedo comprobarlo únicamente observando los registros de genes.

**Decisión:** FALTA VERIFICAR.

**¿Qué necesito?**
Consultar los metadatos o una fuente de referencia del genoma.

## Cambios a nuestra estrategia

Después de revisar la respuesta:

- Mantendremos el conteo de registros `gene`.
- Mantendremos la separación de genes por hebra.
- Revisaremos cómo obtener el tamaño del genoma antes de decidir
  el procedimiento.

## Conclusión

La IA ayudó a revisar nuestra estrategia, pero no aceptamos sus
observaciones automáticamente. Comprobamos cuáles estaban
sustentadas por nuestros datos y dejamos como pendiente lo que
requiere otra fuente.


