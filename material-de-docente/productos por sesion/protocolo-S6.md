# Protocolo del proyecto — E. coli K-12

> **Estado al cierre de S6 / Unidad 2:** el entorno Unix del proyecto queda consolidado y verificado. Las afirmaciones sobre acceso, estructura, integridad y permisos quedan respaldadas por evidencia reproducible.

## Introducción

Este proyecto utilizará información genómica de *Escherichia coli* K-12 para practicar un flujo de trabajo bioinformático reproducible. Al cierre de la Unidad 2, el objetivo es demostrar que el entorno de trabajo construido en S3–S5 está íntegro, organizado, protegido y suficientemente documentado para comenzar a trabajar con datos biológicos.

## Pregunta central

**¿Cuántos genes tiene el genoma de *E. coli* K-12 y cómo se distribuyen en el cromosoma?**

## Subpreguntas

1. ¿Cuál es el tamaño del genoma?
2. ¿Cuántos genes están anotados?
3. ¿Cuántos genes se encuentran en la hebra `+` y cuántos en la hebra `-`?

## Datos

### Datos fuente

```text
~/proyecto-ecoli/data/source/
├── genes_ecoli.gff
└── genes_ecoli-metadatos.md
```

- Los originales se conservan sin modificaciones.
- `genes_ecoli-metadatos.md` documenta procedencia y contexto.
- La integridad queda respaldada por un archivo de sumas en `doc/checksums-u2.txt`.

### Preparación para datos futuros

El proyecto ya dispone de separación entre:

- `data/source/` — originales.
- `data/processed/` — derivados regenerables.
- `src/` — scripts.
- `results/` — resultados.
- `doc/` — documentación y evidencia.

Cuando se incorporen datos externos reales, deberán registrarse su procedencia, versión, fecha de acceso, formato, licencia/condiciones de uso e integridad.

## Estrategia

La estrategia biológica sigue sin ejecutarse. Antes de hacerlo, se cierra la verificación del entorno mediante cuatro preguntas:

1. ¿Puedo acceder al servidor y demostrar dónde estoy?
2. ¿El árbol real del proyecto coincide con el declarado o puedo explicar sus diferencias?
3. ¿Los datos fuente siguen idénticos a los registrados previamente?
4. ¿Los permisos y la documentación son suficientes y justificables?

## Comandos y evidencia de cierre de U2

### 1. Verificar acceso y contexto

```bash
hostname
whoami
pwd
cd ~/proyecto-ecoli
pwd
```

**Ruta absoluta observada:** `[REGISTRAR SALIDA DE pwd]`

### 2. Verificar estructura real

```bash
ls -R ~/proyecto-ecoli
```

Para cada elemento adicional creado en S5 se toma una decisión explícita: conservar, mover o eliminar, con justificación. No se elimina nada de `data/source/`.

### 3. Verificar integridad de los originales

```bash
cd ~/proyecto-ecoli/data/source
sha256sum genes_ecoli.gff genes_ecoli-metadatos.md > ../../doc/checksums-u2.txt
sha256sum -c ../../doc/checksums-u2.txt
```

**Salida esperada:**

```text
genes_ecoli.gff: OK
genes_ecoli-metadatos.md: OK
```

Además, las sumas actuales deben compararse con las registradas en S3. La coincidencia actual demuestra integridad respecto al archivo de sumas; la comparación con S3 demuestra continuidad desde la transferencia inicial.

### 4. Verificar permisos

```bash
ls -l ~/proyecto-ecoli/data/source/
ls -l ~/proyecto-ecoli/src/
```

Criterios:

- Datos fuente: lectura; sin permiso de ejecución.
- Documentación: lectura y escritura para el dueño según necesidad.
- Scripts: ejecución únicamente cuando el script deba ejecutarse.

Cualquier corrección con `chmod` debe documentar archivo, permiso modificado y justificación.

### 5. Verificar reproducibilidad del protocolo

El protocolo se revisa por pares. La persona revisora debe poder identificar:

- dónde se ejecuta cada comando;
- de dónde proviene cada archivo o valor;
- qué evidencia produce cada procedimiento;
- por qué se tomó cada decisión;
- qué información permanece pendiente o limitada.

No deben existir credenciales ni información sensible en el documento.

## Resultados

### Evidencia de consolidación

| Afirmación | Evidencia | Estado |
|---|---|---|
| Puedo reconectar y ubicarme en el servidor | `hostname`, `whoami`, `pwd` | `[COMPROBADO/PENDIENTE]` |
| El proyecto tiene una estructura conocida | `ls -R ~/proyecto-ecoli` | `[COMPROBADO/PENDIENTE]` |
| Los originales no cambiaron | comparación S3 + `sha256sum -c` | `[COMPROBADO/PENDIENTE]` |
| Los permisos son justificables | `ls -l` + correcciones documentadas | `[COMPROBADO/PENDIENTE]` |
| Otra persona puede seguir el protocolo | revisión por pares | `[COMPROBADO/PENDIENTE]` |

## Validación

La Unidad 2 se considera cerrada cuando las afirmaciones anteriores están respaldadas por salidas observables y registradas, no únicamente por recuerdo o confianza.

Una frase válida de cierre es:

> Puedo afirmar que los datos fuente conservan su integridad porque los checksums actuales coinciden con los registrados previamente y la comprobación queda automatizada en `doc/checksums-u2.txt`.

Si un checksum produce `FAILED`, no se interpreta automáticamente como corrupción: primero se revisan ruta, archivo comparado, cambios accidentales y errores de transcripción del checksum.

## Discusión

El cierre de U2 muestra la diferencia entre "me funcionó" y "puedo demostrar que funciona". La organización, los metadatos, las rutas, los checksums, los permisos y la documentación son parte del análisis reproducible porque permiten reconstruir el estado del proyecto antes de comenzar el análisis biológico.

## Conclusiones

El entorno Unix del proyecto está preparado para continuar con el análisis de datos biológicos una vez que las verificaciones de acceso, estructura, integridad, permisos y documentación estén marcadas como comprobadas.

La pregunta biológica todavía no se ha respondido; hasta S6 se ha construido y validado el entorno que permitirá responderla de manera reproducible.

## Actualizaciones

- **S1:** pregunta, subpreguntas y estrategia.
- **S2:** datos, metadatos y principios de organización/FAIR.
- **S3:** transferencia al servidor y comprobación de integridad.
- **S4:** estructura `~/proyecto-ecoli/`, ubicación definitiva de archivos y verificación.
- **S5:** práctica operativa sin alterar el protocolo científico ni los datos fuente.
- **S6:** consolidación de evidencias de U2, archivo `doc/checksums-u2.txt`, revisión de permisos y revisión por pares del protocolo.
