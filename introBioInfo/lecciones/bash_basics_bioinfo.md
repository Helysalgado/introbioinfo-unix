# Clase de Bash: Variables, Bucles `for` y Scripts para Bioinformáticos Novatos

## 🏛 Introducción general

Esta clase cubre tres pilares esenciales para automatizar tareas en bioinformática usando la terminal:

1. **Variables**: para guardar y reutilizar valores.
2. **Bucles `for`**: para repetir tareas en muchos archivos.
3. **Scripts**: para combinar comandos y crear mini programas.

---

## 1. 💪 Variables en Bash

### 🧠 Concepto
Una variable en Bash es un nombre que guarda un **valor** (texto o número) para reutilizarlo más adelante.

### 📌 Sintaxis
```bash
nombre=valor
$nombre
```
- **Sin espacios** alrededor del signo igual.
- Para usar su valor, se antepone un **`$`**.

### ✏️ Ejemplos
```bash
saludo="Hola Bioinforma"
echo $saludo
```
```bash
archivo="genes.gff"
head -n 5 $archivo
```

### 🔬 Ejemplos bioinformáticos
```bash
fasta="secuencias_humanas.fasta"
grep ">" $fasta | wc -l
```
```bash
gff="datos/anotaciones.gff3"
cut -f3 $gff | sort | uniq -c
```

### 🧰 Variables especiales en Bash

Bash también incluye algunas **variables predefinidas** muy útiles:

- **`$PATH`**: Lista de directorios donde el sistema busca comandos.
- **`$HOME`**: Ruta del directorio personal del usuario.
- **`$USER`**: Nombre del usuario actual.
- **`$PWD`**: Directorio actual de trabajo.

✏️ Puedes ver sus valores así:
```bash
echo $PATH
echo $HOME
echo $USER
echo $PWD
```

Estas variables te ayudan a navegar y configurar tu entorno de trabajo.

### 🔬 Ejercicio guiado
1. Declara una variable llamada `ruta` con el valor `datos/archivos/`.
2. Declara una variable `fasta` con el nombre de tu archivo `.fasta` favorito.
3. Usa `echo` para mostrar la ruta completa: `$ruta$fasta`.

---

## 2. 🔁 Bucles `for`

### 🧠 Concepto
Un bucle `for` permite **repetir acciones** para una lista de elementos.

### 📌 Sintaxis
```bash
for var in lista; do
  comando $var
done
```
- `var` es una variable temporal.
- `lista` puede ser una lista de palabras o archivos.

### ✏️ Ejemplos simples
```bash
for fruta in manzana banana uva; do
  echo "Me gusta la $fruta"
done
```
```bash
for archivo in *.fasta; do
  grep ">" $archivo | wc -l
done
```

### 🔬 Ejemplos bioinformáticos
```bash
# Convertir todos los archivos .fastq a .fasta
for f in *.fastq; do
  seqtk seq -A $f > ${f%.fastq}.fasta
done
```
```bash
# Extraer nombres únicos de genes de varios GFF
for file in *.gff; do
  echo "Genes en $file:"
  grep -w "gene" $file | cut -f9 | cut -d";" -f1 | sort | uniq
  echo "-------------"
done
```

### 🔬 Ejercicios propuestos
1. Crea un bucle que imprima el nombre de todos los archivos `.gff` en tu carpeta.
2. Modifica el bucle anterior para contar cuántos genes tiene cada archivo.
3. Crea un bucle que diga "Procesando muestra X" para muestras `muestra1`, `muestra2` y `muestra3`.

---

## 3. 📄 Scripts Bash

### 🧠 Concepto
Un script es un archivo de texto que contiene comandos de Bash, como un **programa automatizado**.

### 📌 Sintaxis
```bash
#!/bin/bash
# Comentarios comienzan con #
comandos
```

- El primer renglón indica que se usará Bash para ejecutar.
- Se guarda como `archivo.sh`
- Se le da permiso de ejecución:
```bash
chmod +x archivo.sh
./archivo.sh
```

### ✏️ Ejemplo simple
Archivo: `saludo.sh`
```bash
#!/bin/bash
nombre="Estudiante"
echo "Hola $nombre, bienvenido a Bioinformática."
```

### 🔬 Ejemplo aplicado a bioinformática

### 🗂️ Crear estructura de proyecto con variables del sistema
Archivo: `crear_proyecto.sh`
```bash
#!/bin/bash

usuario=$USER
fecha=$(date +%Y%m%d)
proyecto=$1

if [ -z "$proyecto" ]; then
  echo "Uso: $0 <nombre_proyecto>"
  exit 1
fi
ruta_base="$HOME/proyectos/${proyecto}-${fecha}"

mkdir -p $ruta_base/{{datos,scripts,resultados,notas}}

echo "Proyecto creado en: $ruta_base"
echo "Usuario: $usuario"
echo "Fecha: $fecha"
```

Este script:
- Usa `$USER` y `$HOME` para personalizar la ruta.
- Usa `date` para incluir la fecha actual.
- Crea carpetas siguiendo buenas prácticas: `datos`, `scripts`, `resultados`, `notas`.
- Informa al usuario lo que hizo.

Archivo: `contar_genes.sh`
```bash
#!/bin/bash
for archivo in *.gff; do
  echo "Archivo: $archivo"
  grep -w "gene" $archivo | wc -l
done
```

### 🎯 ¿Cuándo usar un script?
- Cuando debes repetir el mismo análisis muchas veces.
- Cuando necesitas guardar tu flujo de trabajo.
- Para compartir tu análisis con colegas.
- Cuando trabajas con datos que cambian con frecuencia.
- Para evitar errores al copiar y pegar comandos manualmente.

---

### ⚙️ Paso de parámetros a un script
Los scripts pueden **recibir argumentos** desde la línea de comandos. Esto los hace más flexibles.

### 📌 Sintaxis
```bash
./script.sh valor1 valor2
```
Dentro del script:
```bash
$1  # primer parámetro
$2  # segundo parámetro
$@  # todos los parámetros
```

### ✏️ Ejemplo simple con parámetros
Archivo: `saludo_personalizado.sh`
```bash
#!/bin/bash
nombre=$1
lenguaje=$2
echo "Hola $nombre, bienvenido al mundo de $lenguaje."
```

Ejecución:
```bash
./saludo_personalizado.sh Alicia Bioinformática
```

### 🔬 Ejemplo bioinformático con parámetros
Archivo: `buscar_gen.sh`
```bash
#!/bin/bash
archivo=$1
gen=$2
grep "$gen" $archivo
```
Uso:
```bash
./buscar_gen.sh anotaciones.gff3 AT1G01010
```

---

### 🔬 Ejercicios propuestos
1. Crea un script llamado `contar_fasta.sh` que cuente cuántas secuencias hay en todos los `.fasta`.
2. Crea un script `renombrar_muestras.sh` que imprima: `muestra1 -> muestra_A`, `muestra2 -> muestra_B`, etc.
3. Crea un script que reciba una variable de entrada (`nombre_archivo`) y use `grep` para contar genes.
4. Agrega a un script la opción de recibir un tercer parámetro que indique si debe mostrar el resultado o guardarlo en un archivo.

---

## 📊 Tabla resumen

| Concepto | Sintaxis | Uso típico |
|---------|----------|-------------|
| Variable | `x=valor` | Guardar y reutilizar valores |
| Usar variable | `$x` | Referirse al valor |
| Bucle `for` | `for i in ...; do ...; done` | Repetir comandos |
| Script Bash | `#!/bin/bash` + comandos | Automatizar tareas |
| Parámetros | `$1`, `$2`, `$@` | Recibir datos desde el exterior |

---

## ✅ Respuestas a los ejercicios

### Variables
1. `ruta="datos/archivos/"`
2. `fasta="ejemplo.fasta"`
3. `echo "$ruta$fasta"`

### Bucles
1. ```bash
for f in *.gff; do echo $f; done
```
2. ```bash
for f in *.gff; do grep -w "gene" $f | wc -l; done
```
3. ```bash
for m in muestra1 muestra2 muestra3; do echo "Procesando $m"; done
```

### Scripts
1. `contar_fasta.sh`
```bash
#!/bin/bash
for f in *.fasta; do
  echo "$f:"
  grep ">" $f | wc -l
done
```

2. `renombrar_muestras.sh`
```bash
#!/bin/bash
for i in 1 2 3; do
  echo "muestra$i -> muestra_$(tr 123 ABC <<< $i)"
done
```

3. Script con argumento:
```bash
#!/bin/bash
nombre_archivo=$1
grep -w "gene" $nombre_archivo | wc -l
```

4. Script con parámetro condicional:
```bash
#!/bin/bash
archivo=$1
gen=$2
salida=$3

resultado=$(grep "$gen" $archivo)

if [ "$salida" == "guardar" ]; then
  echo "$resultado" > resultado.txt
else
  echo "$resultado"
fi
```

---

## 🎉 Cierre

Con estos tres pilares (variables, bucles y scripts), puedes automatizar tareas repetitivas, mejorar tu eficiencia y reproducir análisis en proyectos bioinformáticos. 

🎓 **Próximo tema sugerido:** estructuras condicionales `if`, lectura de argumentos y procesamiento de texto con `cut`, `awk` y `sed`.

