# Metadatos — `pacientes.md`

> **Ejemplo corregido (modelo de buena práctica).** Esta ficha documenta el archivo `pacientes.md`
> registrando **solo lo que puede comprobarse a partir del propio archivo**. Todo lo que no está
> documentado se marca de forma explícita como **“no documentado”**, **“pendiente de confirmar”** o
> **“inferido, no confirmado”**. Así se modela la conducta esperada del estudiante: no inventar
> información.

## Información del archivo

- **Nombre del archivo:** `pacientes.md`
- **Formato interno:** texto plano con valores separados por comas (CSV), a pesar de la extensión `.md` — *inferido del contenido, no confirmado por metadatos*
- **Delimitador:** `,`
- **Número de filas de datos:** 3 (más una fila de encabezado)
- **Número de columnas:** 6
- **Origen / fuente:** no documentado
- **Fecha de creación o descarga:** no documentada
- **Responsable (quién lo generó/obtuvo):** no documentado
- **Licencia o condiciones de uso:** no documentada
- **Checksum (integridad):** pendiente de calcular
- **Naturaleza de los datos:** conjunto de datos **sintéticos**, creado exclusivamente con fines educativos (no proviene de personas reales)

## Diccionario de variables

| Columna | Descripción | Tipo (inferido) | Unidades | Valores observados en el archivo |
|---------|-------------|-----------------|----------|----------------------------------|
| `id`    | Identificador del registro | texto | — | 001, 002, 003 |
| `peso`  | Peso corporal | numérico | **no documentadas** (probablemente kg, sin confirmar) | 65, 78, 70 |
| `altura`| Altura | numérico | **no documentadas** (probablemente cm, sin confirmar) | 170, 180, 165 |
| `sexo`  | Sexo registrado | categórico | — | F, M (significado no documentado en el archivo) |
| `edad`  | Edad | numérico | **no documentadas** (probablemente años, sin confirmar) | 23, 45, 38 |
| `dx`    | Código de diagnóstico | texto | — | A23, B15, C12 — **significado no documentado**; no puede determinarse a partir del archivo |

## Información pendiente de confirmar

Para poder analizar e interpretar estos datos correctamente sería necesario documentar:

- Las **unidades** de `peso`, `altura` y `edad`.
- El **sistema o diccionario de códigos** de la variable `dx`.
- El **origen, la fecha y el responsable** de los datos.
- La **licencia o condiciones de uso**.
- Cuántos registros hay por categoría de `dx` (en este archivo, **uno por código**).

## Notas

- Uso exclusivo con fines educativos.
- Al tratarse de datos **sintéticos**, no aplican las consideraciones de anonimización de datos de personas reales.
