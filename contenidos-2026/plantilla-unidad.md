# Plantilla y estándar de unidad — Introducción a la Bioinformática (2026)

> **Qué es esto.** La estructura y el estándar de calidad de una unidad, destilados de la Unidad 1.
> Úsalo como **fuente de verdad**: genera o ajusta cada unidad siguiendo este esqueleto y verifícala
> contra la checklist. El prompt disparador es `prompts-ia/guia-generacion-unidad.md`; las
> convenciones de estilo (callouts, figuras, referencias) están en `contenidos-2026/README.md`.
>
> **Cómo trabajar cada unidad:** generar/redactar → revisar contra la **checklist de calidad** →
> ajustar sección por sección con visto bueno. Unidad de referencia (estándar de oro):
> `u1-s1-s2-trabajo-reproducible-v3.md`.
>
> **Alcance: unidad completa vs. módulo.** Algunos requisitos de esta plantilla se aplican a la
> **unidad completa** (ficha de unidad, resultados generales, tabla acumulativa de competencia);
> otros, a cada **módulo/sesión**. Una unidad puede estar **dividida en una portada y varios módulos**:
> por ejemplo, la **Unidad 2** se compone de una **portada** (`u2-entorno-unix.md`) y **cuatro
> módulos** de dos horas, **S3–S6**. En ese caso, **cada módulo** conserva su propia **nota de aula
> invertida, preparación previa, prácticas (tres momentos), evidencia, criterios/rúbricas, tiempos,
> alineación (anexos), glosario y referencias**, y la portada aporta solo la visión de conjunto, la
> ruta entre módulos y los enlaces. La checklist de 16 puntos se aplica **al módulo o a la portada
> según corresponda**.

---

## 1. Esqueleto de la unidad (orden fijo)

Cada unidad `uN-<nombre>.md` sigue este orden. Entre paréntesis, qué debe lograr cada parte.

1. **Nota de aula invertida** (callout inicial, **sin encabezado propio**): los tres momentos, qué llevar al taller, cómo se evalúa cada momento.
2. **Ficha de la unidad** (tabla): sesiones, competencias (A–G), propósito, contribución al objetivo del curso, ajustes integrados, **lecturas** (distinguir la obligatoria con evidencia de la de consulta, con tiempos).
3. **Resultados de aprendizaje (demostrables)**: verbos observables, **al alcance real de la unidad** (distinguir *comprender* / *diseñar* / *ejecutar*; marcar lo provisional o conceptual).
4. **Ruta de aprendizaje** (tabla por momentos): *antes de S1 · S1 · entre S1–S2 · S2 · después de S2*, con qué leer, qué intentar, qué llevar/entregar y **tiempo estimado por momento** (aclarar que son estimaciones). Indicar secciones **indispensables** vs. **opcionales**.
5. **Secciones conceptuales numeradas**: cada concepto definido, con ejemplos reales y figuras. Orden de razonamiento **pregunta → evidencia → datos → operación → herramienta** (nunca el comando primero). No presuponer comandos aún no enseñados.
6. **Prácticas** (`### Práctica N`), cada una con **tres momentos**: *Antes de clase (primer intento)* → *Durante el taller* → *Después del taller (entrega final)*. Pasos numerados; ligadas a las **Tareas** del plan operativo (sin romper su numeración; si hay contradicción, alinear al plan y registrar la discrepancia). Ninguna práctica depende de un producto que aún no se elaboró.
7. **Rúbricas** (`## Rúbricas`): descriptores observables en tres niveles **Logrado / Parcialmente logrado / Aún no logrado**. Mínimo: primer intento (formativa), participación (formativa), **Tarea 1**, **Tarea 2**. Aclarar el valor del primer intento (formativo, puntos por preparación).
8. **Glosario** español–inglés de los términos nuevos.
9. **Cierre de la unidad**: evidencias de habilidades (checklist), comprobación de comprensión (quiz), reto aplicado, autoevaluación y semáforo de salida — **con momento y tipo** (obligatorio / formativo / opcional), sin evaluar dos veces lo mismo. La calificación viene de las Tareas, no del cierre.
10. **Actividad de uso crítico de IA**, cuando aporte: reproducir con IA 1–2 tareas ya hechas a mano; comparar y validar. El trabajo manual es **línea base** (no “verdad de referencia”). Herramientas: ChatGPT/Claude o los GPTs del curso. Registrar en la bitácora de IA. **No es una sección obligatoria en cada unidad**: su obligatoriedad y ubicación las fija `README.md`.
11. **Anexos**: (A) correspondencia *Resultado–Actividad–Evidencia–Criterio–Momento–Nivel en U N*; (B) alineación transversal con columnas reproducibilidad / verificación / validación / robustez.
12. **Referencias** con DOI/URL (no inventadas; verificar las nuevas).

---

## 2. Checklist de calidad (verificar antes de cerrar la unidad)

> **Alcance.** Esta checklist evalúa **módulos de contenido**. No se
> aplica al material transversal (práctica integradora, revisión por
> pares, evaluaciones), que tiene su propia estructura corta en
> `README.md`, sección *Material transversal*.

Derivada de la revisión de la Unidad 1. Marca cada punto.

- [ ] **1. Dos sesiones.** La unidad está distribuida en 2 sesiones de 2 h con trabajo antes, entre y después, en una tabla clara.
- [ ] **2. Carga declarada por momento.** Tiempos separados: lectura de la unidad, lectura base, cada práctica, y por momento; marcados como estimaciones.
- [ ] **3. Ruta sin ambigüedad.** Responde: qué leo antes de S1, qué intento, qué llevo, qué hago entre sesiones, qué llevo a S2, qué entrego después. Secciones indispensables vs. opcionales marcadas (incluir Markdown/producción si la tarea lo exige).
- [ ] **4. Resultados al alcance real.** Distinguen *diseñar* de *ejecutar*; lo provisional/conceptual está marcado; no se declara alcanzado lo que solo se evaluará después.
- [ ] **5. Alineación RA–práctica–evidencia.** Cada RA tiene actividad, evidencia, criterio, momento y **nivel en la unidad** (comprensión / diseño anticipado / ejecución). No se atribuyen ejecuciones que aún no ocurren.
- [ ] **6. Rúbricas con descriptores** observables (Logrado / Parcial / Aún no), incluidas Tarea 1 y Tarea 2; criterios para pregunta/subpreguntas, estrategia, protocolo, reporte de lectura, estructura de proyecto, metadatos/diccionario, reconocimiento de información no documentada, Markdown funcional, bitácora de IA, validación de IA, conclusión provisional y limitaciones.
- [ ] **7. Metadatos honestos.** Ningún ejemplo afirma información no comprobable; se usa “no documentado / pendiente de confirmar / inferido, no confirmado”.
- [ ] **8. “Primero a mano”.** El trabajo manual es **línea base**, no verdad absoluta; la validación es independiente de la IA y del primer intento.
- [ ] **9. FAIR como principios guía** (no “estándar”); no equivale a datos abiertos; no se cumple con solo guardar un archivo local; la tabla lista “acciones que contribuyen a cada principio”.
- [ ] **10. Metadatos de datos vs. software** distinguidos (software introducido conceptualmente; no exigir versiones de herramientas no usadas).
- [ ] **11. Directorios** consistentes: `data/source/`, `data/processed/`, `src/`, `results/`, `doc/`. Nota de alineación si el programa usa otra convención.
- [ ] **12. Enlaces funcionales.** Los archivos que el estudiante abre van como enlaces Markdown; recursos que deben copiarse al sitio Quarto quedan anotados; lista de pendientes por resolver.
- [ ] **13. Cierre sin redundancia.** Actividades del cierre etiquetadas por momento y tipo (obligatorio/formativo/opcional); no evalúan lo mismo varias veces.
- [ ] **14. Lecturas diferenciadas.** La lectura obligatoria (con evidencia) se distingue de la de consulta; con tiempos.
- [ ] **15. Terminología de datos.** Datos ficticios = **sintéticos** (no “anónimos”); no asignar significado no documentado a códigos.
- [ ] **16. Fortalezas conservadas.** Reproducibilidad/replicabilidad/verificación/validación/robustez; orden pregunta→herramienta; datos originales vs. derivados; protocolo vivo; Markdown funcional; FAIR temprano; validación independiente de IA; bitácora; aula invertida con primer intento y corrección argumentada.
- [ ] **Extra.** Sin mención a Quarto en el texto del alumno. Toda buena práctica citada. Español claro para primer semestre sin Unix previo.

---

## 3. Parámetros que cambian por unidad

Rellena esta tabla al inicio de cada unidad para fijar su alcance (referencia: Programa 2026 y Plan operativo).

| Parámetro | Unidad 1 (ejemplo) | Unidad N |
| --- | --- | --- |
| Sesiones (plan) | S1–S2 | |
| Competencias | A, G | |
| Ajustes integrados | Prompting/IA responsable [Nuevo] | |
| Lectura obligatoria (con evidencia) | Buffalo Cap. 1 | |
| Lectura de consulta | Buffalo Cap. 2 | |
| Dataset(s) de ejemplo | `ejemplos/pacientes.md` (sintético); *E. coli* GFF | |
| Tareas del plan | T1 protocolo+reporte; T2 estructura+metadatos+bitácora | |
| Infraestructura (si aplica) | — | `chaac`, SGE (U2+) |
| Tareas para el “Cierre con IA” | metadatos y estrategia con IA | |

---

## 4. Convenciones

Se usan las del `README.md` de esta carpeta: marcadores de callout (`> **NOTA:**`, `**IMPORTANTE**`,
`**TIP**`, `**¿SABÍAS QUE?**`, `**COMENTARIO**`, `**ADVERTENCIA**`), figuras (revisar `images/`,
integrar con alt text + pie numerado o describir la que falte), etiquetas de ajuste
(**[Nuevo]/[Reforzado]/[Integración]**) y referencias inline + sección final. **Toda buena práctica
cita su fuente.**
