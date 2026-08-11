# Análisis de secuencias genómicas con `sed`

## 🎯 Objetivo del caso
Explorar el comando `sed` para procesar y analizar archivos de secuencia en formato FASTA. Los alumnos aprenderán a hacer sustituciones, eliminar líneas, trabajar con rangos y usar patrones para modificar archivos de manera eficiente.


-   **Cognitivo**: Comprender el funcionamiento de `sed` y reconocer cuándo y cómo utilizarlo en el procesamiento de archivos de texto genómico.
    
-   **Procedimental**: Usar comandos `sed` para editar, limpiar y transformar archivos FASTA mediante sustituciones, eliminaciones y rangos de líneas.
    
-   **Actitudinal**: Desarrollar autonomía y criterio para elegir herramientas adecuadas que mejoren la eficiencia y reproducibilidad en análisis bioinformáticos.


## 📁 Archivos a usar

### `secuencias.fasta`

```fasta
>gene1
ATGCGTAGGGTTA
>gene2
atgccctagaaatg
>gene3
ATGCGNNTAGCAT
>gene4
ATGCATGCATGC
>gene5
ATGCTA
>gene6
TTATTG
```

Este archivo contiene 4 secuencias genómicas, algunas en minúsculas, otras con bases ambiguas (como `N`).

---

## 🧠 ¿Qué es `sed`?
`sed` es un **editor de flujo de texto**. Permite **buscar, reemplazar, eliminar o modificar** texto, línea por línea, usando expresiones regulares y comandos compactos. Es ideal para automatizar cambios en archivos de texto.

### 🛠️ Sintaxis básica

```bash
sed 'comando' archivo
```
- `'comando'`: operación a realizar (como `s/patrón/reemplazo/`)
- `archivo`: archivo de texto de entrada

**Opciones y comandos comunes de `sed`**

| Opción / Comando       | Qué hace                                                                 |
|------------------------|--------------------------------------------------------------------------|
| `s/pat/reemp/`         | Sustituye el patrón por el reemplazo (solo la **primera coincidencia**) |
| `s/pat/reemp/g`        | Sustituye **todas** las coincidencias en la línea                       |
| `d`                    | Elimina la línea que coincide con el patrón                             |
| `p`                    | Imprime la línea (usado con `-n`)                                       |
| `-n`                   | Suprime la salida normal (se usa con `p`)                               |
| `#,#`                  | Aplica una operación a un rango de líneas por número                    |
| `/pat/,/pat/`          | Aplica una operación entre dos patrones                                 |
| `!`                    | Niega una operación (actúa sobre las líneas que **no** coinciden)       |
| `-e`                   | Permite usar varios comandos `sed` en una misma instrucción             |


### Ejemplos

Simulando un cat

```bash
sed ''  ecuencias.fasta
```

A veces queremos imprimir **solo las líneas que coincidan** con un patrón. Para eso usamos:

```bash
sed -n '/patrón/p' archivo
```

-   `-n` → desactiva la impresión automática de `sed`.  
-   `p` → imprime **solo** las líneas que coincidan con el patrón.
    


```bash
sed  '/^>/p' secuencias.fasta  # que pasa?
```


```bash
sed -n '/^>/p' secuencias.fasta
```

👉 Muestra solo los encabezados (líneas que empiezan con `>`).


---

## 🧩 preguntas a responder

### 🔹 Preguntas básicas

1. **¿Cómo ver solo las secuencias (sin encabezados)? Es decir borrar las lineas que empizan con `>`.**

   ```bash
   sed '/^>/d' secuencias.fasta
   ```
   - `^>` indica líneas que comienzan con `>`.
   - `d` elimina esas líneas.
   ✅ Esto deja solo las secuencias (sin los nombres de los genes).

2. **¿Cómo reemplazar una base (por ejemplo, `G` por `g`) en todo el archivo?**

   ```bash
   sed 's/G/g/g' secuencias.fasta
   ```
   - `s/` → sustituir
   - `G` → buscar letra
   - `g` → reemplazo
   - `/g` al final → global (todas las apariciones en la línea)

3. **¿Cómo cambiar la primera `A` de cada línea por `*`?**

   ```bash
   sed 's/A/*/' secuencias.fasta
   ```
   - Solo afecta la primera `A` por línea.

4. **¿Cómo reemplazar `ATG` por `XXX`, solo una vez por línea?**

   ```bash
   sed 's/ATG/XXX/' secuencias.fasta
   ```
   - `s/ATG/XXX/` reemplaza la primera coincidencia de `ATG`.

---

### 🔹 Preguntas intermedias

1. **¿Cómo convertir todas las secuencias a mayúsculas?**

   ```bash
   tr 'a-z' 'A-Z' < secuencias.fasta
   ```
   - `tr` convierte caracteres uno por uno.
   - Este paso no lo hace `sed`, pero es útil para preprocesamiento.

2. **¿Cómo eliminar las líneas que contienen letras ambiguas (como `N`)?**

   ```bash
   sed '/N/d' secuencias.fasta
   ```
   - Busca líneas con `N` y las elimina.
   - No discrimina si es encabezado o secuencia.

3. **¿Cómo modificar solo una línea específica del archivo?**

   ```bash
   sed '6s/N/-/g' secuencias.fasta
   ```
   - En la línea 6, reemplaza `N` por `-`.

4. **¿Cómo cambiar una base solo en un rango de líneas?**

   ```bash
   sed '2,4s/A/a/g' secuencias.fasta
   ```
   - De la línea 2 a la 4 (rango), reemplaza todas las `A` por `a`.


5. **Pero si quiero reemplazar 2 líneas, no un rango? por ejemplo reemplazar las `A` por `a` de la linea 2 y la 4 (no rango).**

   ```bash
   sed -e '2s/A/a/g' -e '4s/A/a/g' secuencias.fasta
   ```
   - `-e` permite ejecutar varios comandos de sed.

   o bien
   
   ```bash
   sed '2s/A/a/g; 4s/A/a/g' secuencias.fasta
   ```
   Usa punto y coma `;` para separar instrucciones.
   
---

### 🔹 Preguntas avanzadas

1. **¿Cómo sustituir una base específica en un gen determinado usando patrones?**

   ```bash
   sed '/>gene2/,/>gene3/{s/T/U/g}' secuencias.fasta
   ```
   - Del encabezado `>gene2` hasta el siguiente `>gene3`, cambia `T` por `U`.


   ✅ **Regla práctica**

   > Siempre que uses un **rango** y una acción, pon la acción dentro de `{}`.


12. **¿Cómo modificar todas las secuencias excepto una en particular?**

   ```bash
   sed '/>gene4/,/>gene5/!s/T/U/g' secuencias.fasta
   ```
   - `!` aplica la sustitución a todo **menos** ese rango.


   Como funciona `!`

   ```txt
   <rango o patrón>!comando
   ```
   
   -   `2,4!d` → elimina **todas las líneas excepto** de la 2 a la 4.  
   -   `/^>/!d` → elimina todo **excepto** las líneas que **empiezan con `>`**.   
    El `!` **se coloca inmediatamente después** del rango o patrón, y **antes del comando**.

   

---

## 🎯 Actividades para los alumnos

1. Cambia todas las apariciones de `G` por `g` solo en las secuencias (no en los encabezados).
   - 💡 Pista: evita líneas que empiecen con `>`.
  
2. Reemplaza `TAG` por `***` solo si está dentro de `gene3`.
   - 💡 Busca `>gene3`, aplica cambio hasta `>gene4`.

3. Cambia todas las letras minúsculas por mayúsculas en todo el archivo.


4. Reemplaza todas las `T` por `U`, excepto en `gene4`.
   - 💡 Puedes usar `!` con un rango o hacer dos pasos con `sed`.

---

## 🧾 Conclusiones
Este caso enseña a usar `sed` paso a paso, desde operaciones básicas hasta manipulaciones complejas de archivos FASTA. A medida que los alumnos entienden cómo combinar patrones, rangos y sustituciones, ganan herramientas muy poderosas para automatizar procesos en bioinformática.
