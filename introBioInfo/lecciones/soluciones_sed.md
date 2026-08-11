## 🎯 Actividades para los alumnos

1. Cambia todas las apariciones de `G` por `g` solo en las secuencias (no en los encabezados).
   - 💡 Pista: evita líneas que empiecen con `>`.

```bash
sed '/^>/!s/G/g/g' secuencias.fasta
```

2. Reemplaza `TAG` por `***` solo si está dentro de `gene3`.
   - 💡 Busca `>gene3`, aplica cambio hasta `>gene4`.

```bash
sed '/>gene3/,/>gene4/{s/TAG/***/g}' secuencias.fasta
```

3. Cambia todas las letras minúsculas por mayúsculas en todo el archivo.
 
   ```bash
   tr 'a-z' 'A-Z' < secuencias.fasta
   ```

4. Reemplaza todas las `T` por `U`, excepto en `gene4`.
   - 💡 Puedes usar `!` con un rango o hacer dos pasos con `sed`.

   ```bash 
   sed '/>gene4/,/>/{!s/T/U/g}' secuencias.fasta
   ```
  