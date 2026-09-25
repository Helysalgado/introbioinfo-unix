# Protocolo del proyecto — E. coli K-12

> **Estado al cierre de S2:** se conserva la pregunta y estrategia de S1 y se incorpora la descripción del dato, su organización y las decisiones FAIR relevantes.

## Introducción

Este proyecto utilizará información genómica de *Escherichia coli* K-12 para practicar un flujo de trabajo bioinformático reproducible. El objetivo no es comenzar por una herramienta, sino definir primero la pregunta biológica, dividirla en subpreguntas y establecer qué evidencia permitiría responderlas.

El protocolo es un documento vivo: se completará durante el curso conforme se incorporen los datos, los comandos, las verificaciones, los resultados y su interpretación.

## Pregunta central

**¿Cuántos genes tiene el genoma de *E. coli* K-12 y cómo se distribuyen en el cromosoma?**

## Subpreguntas

1. ¿Cuál es el tamaño del genoma de *E. coli* K-12?
2. ¿Cuántos genes están anotados en el genoma?
3. ¿Cuántos genes se encuentran en la hebra `+` y cuántos en la hebra `-`?

## Datos

### Archivo principal

- **Archivo:** `genes_ecoli.gff`
- **Organismo:** *Escherichia coli* K-12 MG1655
- **Referencia:** `NC_000913.3`
- **Formato:** GFF
- **Función en el proyecto:** archivo de anotación genómica utilizado como dato fuente.
- **Metadatos asociados:** `genes_ecoli-metadatos.md`
- **Integridad:** el campo de checksum queda reservado hasta calcularlo en una sesión posterior.

La ficha `genes_ecoli-metadatos.md` registra la procedencia y el contexto del dato. La información que no esté comprobada debe quedar marcada como pendiente, no inferirse ni inventarse.

### Política de organización de datos

- Los datos originales se conservarán sin modificaciones en `data/source/`.
- Los archivos transformados o derivados se guardarán en `data/processed/`.
- Los resultados regenerables se almacenarán en `results/`.
- Los scripts se almacenarán en `src/`.
- La documentación del proyecto se almacenará en `doc/`.

Estas decisiones contribuyen a la localización, trazabilidad y reutilización del trabajo; FAIR se aplica de forma progresiva y no se considera resuelto únicamente por crear carpetas o una ficha de metadatos.

### Ubicación de los datos fuente

```text
~/proyecto-ecoli/data/source/
├── genes_ecoli.gff
└── genes_ecoli-metadatos.md
```

Los archivos de `data/source/` se consideran datos originales del proyecto y no deben editarse directamente. Los derivados futuros se almacenarán en `data/processed/`.


## Estrategia

| Subpregunta | Evidencia necesaria | Datos | Operación conceptual | Validación prevista |
|---|---|---|---|---|
| ¿Cuál es el tamaño del genoma? | Longitud total del genoma | `genes_ecoli.gff` / registro asociado | Localizar la longitud declarada | Contrastar con el registro de referencia |
| ¿Cuántos genes hay? | Número de registros `gene` | `genes_ecoli.gff` | Filtrar conceptualmente por tipo `gene` y contar | Comparar con referencia externa |
| ¿Cuántos genes hay por hebra? | Conteos `+` y `-` para genes | `genes_ecoli.gff` | Agrupar conceptualmente por hebra y contar | `+` + `-` = total de genes |


## Comandos y procedimiento

### Sesion 3

### 1. Acceso al servidor

**Contexto: LOCAL**

```bash
ssh [USUARIO]@[SERVIDOR]
```

**Contexto: REMOTO**

```bash
hostname
whoami
pwd
exit
```

No se registran contraseñas, llaves privadas ni credenciales en el protocolo.

### 2. Transferencia de datos y metadatos

**Contexto: LOCAL → SFTP**

```bash
sftp [USUARIO]@[SERVIDOR]
lpwd
pwd
put genes_ecoli.gff
put genes_ecoli-metadatos.md
exit
```

También se transfiere via Filezilla, pero no es automatizable.

### 3. Comprobación de presencia

**Contexto: REMOTO**

```bash
ssh [USUARIO]@[SERVIDOR]
ls -lh genes_ecoli.gff genes_ecoli-metadatos.md
```

### 4. Comprobación de integridad

**Contexto: LOCAL**

```bash
sha256sum genes_ecoli.gff
sha256sum genes_ecoli-metadatos.md
```

> En macOS puede utilizarse `shasum -a 256`.

**Contexto: REMOTO**

```bash
sha256sum genes_ecoli.gff
sha256sum genes_ecoli-metadatos.md
```

### Registro de checksums

| Archivo | SHA-256 local | SHA-256 remoto | Estado |
|---|---|---|---|
| `genes_ecoli.gff` | `[REGISTRAR]` | `[REGISTRAR]` | Deben coincidir |
| `genes_ecoli-metadatos.md` | `[REGISTRAR]` | `[REGISTRAR]` | Deben coincidir |


### Sesion 4

### 1. Confirmar contexto

```bash
hostname
whoami
cd ~
pwd
ls -lah
```

### 2. Crear y verificar la estructura

```bash
mkdir proyecto-ecoli
cd proyecto-ecoli
pwd
mkdir -p data/source data/processed
mkdir src results doc
touch README.md
tree
```

Si `tree` no está disponible:

```bash
ls -R
```

### 3. Copiar datos fuente

Desde `~/proyecto-ecoli`:

```bash
cp -i ~/genes_ecoli.gff data/source/
cp -i ~/genes_ecoli-metadatos.md data/source/
ls -lh data/source/
```

Se usa copia antes de mover para conservar un punto de regreso hasta verificar.

### 4. Colocar documentación

```bash
mv -i ~/protocolo.md doc/
```

La bitácora de IA, si permanece en el equipo local, se transfiere al servidor y se verifica en `doc/`.

### 5. Verificar integridad del GFF

```bash
sha256sum data/source/genes_ecoli.gff
```

La suma debe coincidir con la registrada para el archivo fuente en S3.



## sesion 6

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


