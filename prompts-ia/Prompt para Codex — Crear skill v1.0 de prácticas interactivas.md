Estamos trabajando en el repositorio del curso **Introducción a la Bioinformática — LCG UNAM 2026**.

La estructura de `curso-quarto/` ya fue auditada y corregida. **No quiero reorganizar nuevamente el curso.**

La fuente curricular oficial es:

`curso-quarto/`

La carpeta `contenidos-2026/` contiene material anterior y debe considerarse legado. No debe utilizarse como fuente curricular salvo indicación expresa.

Quiero crear una **skill reutilizable para analizar las prácticas existentes del curso y generar prompts completos para Gemini Canvas**.

# 1. Antes de crear la skill

Primero:

1. Inspecciona brevemente la estructura actual del repositorio.
2. Identifica la convención oficial disponible en este entorno para crear una skill de Codex.
3. Usa esa convención para decidir dónde colocarla.
4. No inventes una estructura incompatible con las skills disponibles en este entorno.
5. No modifiques las sesiones, HTML, imágenes ni `_site/`.
6. No reorganices `curso-quarto/`.

Quiero una implementación **mínima y mantenible**.

# 2. Nombre y misión

Usa un nombre descriptivo como:

`practicas-bioinfo-gemini`

Su misión es:

> Analizar pedagógicamente las prácticas textuales existentes en una sesión de Introducción a la Bioinformática, revisar su implementación interactiva existente cuando la haya, proponer mejoras y, después de la revisión del docente, generar un prompt maestro para que Gemini Canvas construya la aplicación web educativa.

La skill **NO debe generar directamente el HTML de la práctica**.

Su producto final es un **prompt para Gemini Canvas**.

# 3. Perfil de los estudiantes

Este contexto es fundamental.

Los estudiantes son de **primer semestre de la Licenciatura en Ciencias Genómicas de la UNAM** y vienen directamente de preparatoria.

Por tanto:

- usar lenguaje claro y accesible;
- evitar vocabulario avanzado que todavía no haya sido presentado;
- no asumir conocimientos previos de bioinformática;
- no asumir conocimientos de Unix, programación, bases de datos, formatos biológicos, estadística u otras herramientas salvo que las sesiones proporcionadas indiquen que ya fueron vistos;
- no confundir “ya apareció” con “ya lo domina”;
- permitir recordatorios o pistas breves sobre conceptos recientemente introducidos;
- aumentar la dificultad mediante razonamiento, interpretación y toma de decisiones, no mediante vocabulario innecesariamente complejo.

# 4. Fuente curricular

Las sesiones oficiales están en `curso-quarto/`.

Cada sesión contiene la explicación docente y prácticas textuales.

La skill debe considerar la **práctica textual como fuente pedagógica principal**.

Principio:

> **No digitalizar simplemente la práctica. Mejorar su experiencia de aprendizaje.**

Puede:

- reorganizar una actividad;
- dividirla en etapas;
- introducir feedback;
- incorporar pistas;
- pedir predicciones;
- hacer visibles errores;
- solicitar justificación;
- mejorar la documentación del razonamiento;
- proponer otra dinámica interactiva.

Pero debe conservar:

- intención pedagógica;
- nivel;
- conceptos;
- herramientas;
- evidencia esperada;
- progresión curricular.

No inventar contenidos nuevos únicamente para hacer la app más atractiva.

# 5. Contexto curricular

La skill trabajará normalmente con:

- sesión anterior: contexto previo;
- sesión actual: objeto del análisis;
- sesión siguiente: contexto posterior.

Cuando el usuario indique una sesión actual, intenta localizar automáticamente las sesiones vecinas mediante la nomenclatura del curso cuando sea razonablemente seguro hacerlo.

## Sesión anterior

Sirve para determinar:

- qué conceptos ya fueron presentados;
- qué herramientas ya utilizaron;
- qué vocabulario puede resultar familiar;
- qué habilidades pueden empezar a reutilizarse.

No asumir dominio automático.

## Sesión actual

Es la fuente principal.

**Debe leerse COMPLETA antes de analizar las prácticas.**

No diseñar una interacción leyendo solamente el encabezado o texto aislado de la práctica.

## Sesión siguiente

Sirve únicamente para comprender hacia dónde avanza el curso.

**Nunca utilizar contenidos de la sesión siguiente para resolver o enriquecer artificialmente una práctica de la sesión actual.**

La sesión siguiente no autoriza a adelantar conceptos.

# 6. HTML interactivos existentes

Las prácticas interactivas existentes se encuentran principalmente en:

`curso-quarto/html/`

La nomenclatura preferente es:

`uX-sY-pZ-<slug>.html`

Cuando analices una práctica, intenta localizar su HTML existente utilizando:

- unidad;
- sesión;
- número de práctica;
- título;
- palabras clave cuando sea necesario.

Si existe HTML, compáralo con la práctica textual.

La comparación debe responder:

**¿Qué pretende enseñar la práctica?**

versus

**¿Qué experiencia proporciona actualmente el HTML?**

No asumir que el HTML existente es correcto porque ya está implementado.

Tampoco asumir que debe rehacerse.

Puede recomendar:

- conservar;
- ajustar;
- rediseñar parcialmente;
- rediseñar completamente.

Debe justificar pedagógicamente la recomendación.

# 7. Imágenes y recursos

Cuando la sesión o práctica utilice imágenes existentes, identificarlas cuando sea relevante.

No exigir nuevas imágenes si las actuales cumplen la función pedagógica.

No introducir recursos visuales meramente decorativos.

Los recursos visuales deben ayudar a:

- observar;
- comparar;
- interpretar;
- identificar;
- comprender un proceso;
- analizar evidencia.

# 8. Filosofía pedagógica

Las prácticas interactivas deben favorecer:

**observar → pensar → decidir → comprobar → recibir retroalimentación → corregir → justificar → documentar**

La interacción debe tener una razón pedagógica.

Evitar convertir automáticamente las prácticas en cuestionarios.

Según el objetivo pueden considerarse:

- clasificación;
- construcción progresiva;
- ordenar procesos;
- detectar errores;
- comparar alternativas;
- auditorías;
- escenarios;
- laboratorios;
- retos;
- detective científico;
- revisión por pares simulada;
- semáforos epistemológicos;
- construcción de protocolos;
- interpretación de archivos;
- análisis de evidencia;
- juegos de decisión;
- flashcards cuando sean apropiadas.

Nunca elegir primero la dinámica para después intentar meter la práctica dentro de ella.

**Primero comprender el aprendizaje. Después elegir la interacción.**

# 9. Qué NO automatizar

No automatizar aquello que el estudiante debe aprender a hacer.

Ejemplo:

Si el objetivo es aprender a trabajar con una terminal real, no sustituirla con una terminal simulada.

Canvas puede utilizarse para:

1. pedir una predicción;
2. enviar al estudiante a la herramienta real;
3. pedirle registrar lo ocurrido;
4. interpretar el resultado;
5. detectar errores;
6. corregir;
7. justificar.

Aplicar el mismo principio a NCBI, editores, archivos reales, documentación u otras herramientas externas.

No simular herramientas complejas cuando utilizar la herramienta real sea parte del aprendizaje.

# 10. Uso de IA

Cuando una práctica enseñe o utilice IA:

- no presentar la IA como autoridad;
- no presentar la respuesta manual como verdad automática;
- enseñar comparación y validación independiente;
- distinguir conocido, inferido y desconocido;
- hacer visibles alucinaciones, suposiciones y omisiones;
- pedir evidencia;
- registrar el uso de IA;
- mantener la responsabilidad científica en el estudiante.

Principios:

> **Una respuesta plausible no es necesariamente correcta.**

> **Coincidir con la IA tampoco constituye validación.**

# 11. Flujo obligatorio de la skill

La skill debe trabajar en **DOS FASES claramente separadas**.

---

# FASE 1 — ANÁLISIS PEDAGÓGICO

Cuando el usuario pida revisar una sesión:

1. leer la sesión actual completa;
2. consultar la anterior si está disponible;
3. consultar la siguiente únicamente como contexto;
4. localizar todas las prácticas textuales de la sesión actual;
5. localizar sus HTML existentes cuando existan;
6. analizar cada práctica;
7. presentar una propuesta breve.

NO generar todavía el prompt extenso para Gemini Canvas.

Para cada práctica presentar:

## Práctica X — Nombre

### Objetivo central

Explicar en lenguaje sencillo qué debe aprender realmente el estudiante.

### Qué sabe ya

Conceptos y herramientas previamente presentados que puede utilizar.

### Qué debe descubrir, decidir o interpretar

Identificar el trabajo intelectual que no debemos quitarle.

### Qué conservar

Fortalezas de la práctica textual y, cuando exista, del HTML actual.

### Qué puede mejorarse

Problemas u oportunidades pedagógicas.

### Interacción conveniente

Explicar qué tipo de interacción aportaría valor y por qué.

### Qué NO conviene convertir en interacción

Identificar acciones que deben permanecer en herramientas reales o ser realizadas directamente por el estudiante.

### Dinámica o narrativa propuesta

Proponerla solo si aporta valor.

### Evidencia

Qué debería quedar registrado del trabajo y razonamiento del estudiante.

### Archivos descargables

Como mínimo considerar el Markdown general de resultados y cualquier producto específico de la práctica.

### Recomendación sobre HTML existente

Cuando exista:

- Conservar
- Ajustar
- Rediseñar parcialmente
- Rediseñar completamente

Acompañar la decisión con una explicación breve.

Después de analizar todas las prácticas, presentar también una recomendación de arquitectura:

- una app por práctica;
- varias prácticas integradas en una app;
- alguna práctica que no convenga convertir en app;
- otra organización si pedagógicamente es mejor.

**DETENERSE AL FINAL DE FASE 1.**

Esperar la revisión del docente.

---

# FASE 2 — PROMPT PARA GEMINI CANVAS

Ejecutar solamente cuando el usuario apruebe una propuesta o solicite explícitamente generar el prompt.

El prompt debe ser suficientemente completo para que Gemini Canvas construya la aplicación desde cero.

Debe incluir como mínimo:

1. identidad;
2. propósito pedagógico;
3. perfil del estudiante;
4. conocimientos previos;
5. objetivos;
6. caso conductor cuando aporte valor;
7. arquitectura de pestañas o misiones;
8. contenido exacto de cada actividad;
9. estado inicial;
10. interacciones;
11. feedback;
12. pistas;
13. reintentos y correcciones;
14. navegación;
15. persistencia;
16. Resumen;
17. descarga de resultados;
18. productos adicionales;
19. accesibilidad;
20. restricciones técnicas;
21. validación funcional;
22. validación pedagógica.

# 12. Estado inicial obligatorio

Toda app debe abrir sin revelar respuestas.

Exigir:

- ninguna respuesta preseleccionada;
- ningún ✓ o ✗ anticipado;
- ninguna opción verde o roja antes de comprobar;
- dropdowns inicialmente en `Selecciona...`;
- radio buttons vacíos.

Flujo:

**DECIDIR → COMPROBAR → FEEDBACK → PISTA → CORREGIR**

Si el estudiante falla:

1. no revelar inmediatamente la respuesta;
2. proporcionar feedback;
3. ofrecer una pista;
4. permitir reintentar;
5. mostrar explicación cuando corresponda.

No depender exclusivamente del color.

# 13. Navegación libre

Nunca bloquear pestañas por progreso.

El estudiante debe poder:

- avanzar;
- regresar;
- explorar;
- corregir;
- abrir Resumen aunque existan actividades incompletas.

Solicitar una implementación robusta mediante una función central como:

`activateTab(tabName)`

Persistir la pestaña activa cuando corresponda.

Un error en una actividad no debe romper la navegación.

# 14. Persistencia

Utilizar `localStorage` cuando corresponda para conservar:

- pestaña actual;
- respuestas;
- textos;
- decisiones;
- intentos;
- pistas;
- correcciones;
- reflexiones;
- resultados.

Agregar:

**Reiniciar práctica**

con confirmación.

# 15. Resumen — REQUISITO PERMANENTE

TODAS las apps deben terminar con:

**✓ Resumen**

Debe estar disponible siempre.

Debe mostrar el trabajo REAL del estudiante:

- decisiones;
- respuestas;
- resultados;
- errores;
- pistas utilizadas cuando sean relevantes;
- correcciones;
- conceptos;
- reflexiones;
- productos construidos.

Para campos vacíos usar:

**Sin respuesta**

o

**Pendiente**

Nunca inventar resultados en el Resumen.

# 16. Descarga Markdown — REQUISITO PERMANENTE

TODAS las apps deben incluir en Resumen:

**⬇ Descargar resultados de la práctica**

Debe generar un `.md` con el trabajo REAL del estudiante.

Utilizar JavaScript mediante:

- `Blob`;
- `URL.createObjectURL`;
- `<a download>`.

Sin backend.

El archivo puede seguir una estructura como:

```markdown
# Sesión X — Práctica X

## Datos de la práctica

## Mis decisiones

## Mis respuestas

## Evidencia

## Errores detectados

## Correcciones realizadas

## Resultados

## Reflexión final

## Registro formativo
```

Adaptar las secciones al contenido real de cada práctica.

No generar secciones vacías sin sentido únicamente para cumplir una plantilla.

# 17. Productos específicos

Si la práctica construye algo como:

- `protocolo.md`;
- `bitacora-ia.md`;
- `metadatos.md`;
- reporte;
- estrategia;
- ficha;
- evidencia;
- otro producto académico;

agregar un botón de descarga independiente.

# 18. Evaluación formativa

No introducir automáticamente:

- porcentajes;
- notas;
- aprobado/reprobado;
- rankings;
- estrellas.

Preferir:

- Completado
- Pendiente
- Revisado
- Corregido
- Requiere revisar

Los errores razonables son parte del aprendizaje.

# 19. Identidad visual

Mantener una identidad consistente:

`[ LCG UNAM 2026 ]   Introducción a la Bioinformática • Sesión X • Práctica X`

Debajo:

- nombre atractivo;
- subtítulo breve.

Diseño:

- azul oscuro institucional;
- badge dorado `LCG UNAM 2026`;
- fondos claros;
- tarjetas limpias;
- jerarquía clara;
- código y archivos en monoespaciada;
- estilo universitario moderno;
- no infantil;
- evitar encabezados enormes;
- evitar exceso de tarjetas/cuadros cuando otra composición sea más clara.

La simplicidad visual es preferible a llenar la interfaz de componentes.

# 20. Accesibilidad

Solicitar:

- HTML semántico;
- labels;
- fieldsets;
- legends;
- foco visible;
- teclado;
- `aria-live`;
- `role="tablist"`;
- `role="tab"`;
- `role="tabpanel"`;
- `aria-selected`;
- contraste adecuado.

No depender solo del color.

# 21. Restricciones técnicas

Preferentemente:

**un único HTML autónomo con HTML + CSS + JavaScript.**

Evitar salvo necesidad pedagógica o técnica real:

- React;
- frameworks;
- backend;
- login;
- tracking;
- APIs;
- dependencias externas.

Debe funcionar offline cuando la actividad lo permita.

# 22. Herramientas externas

Si la práctica utiliza herramientas reales como:

- NCBI;
- StackEdit;
- Mermaid;
- terminal;
- documentación oficial;
- asistentes de IA;

incluir enlaces claramente identificados cuando sea útil.

No simular herramientas complejas si hacerlo produce una experiencia artificial o frágil.

# 23. Validación funcional obligatoria para Gemini

El prompt debe pedir a Gemini comprobar antes de entregar:

1. la app abre;
2. todas las pestañas funcionan;
3. nada aparece precontestado;
4. se puede navegar sin terminar actividades;
5. las respuestas sobreviven al cambio de pestaña;
6. `localStorage` funciona;
7. Resumen abre siempre;
8. Resumen refleja respuestas reales;
9. las descargas funcionan;
10. el `.md` contiene el trabajo real;
11. Reiniciar práctica funciona;
12. una actividad incompleta no rompe la app.

# 24. Validación pedagógica

Gemini también debe comprobar:

1. que no introdujo conocimientos posteriores;
2. que el vocabulario corresponde a estudiantes de primer semestre;
3. que la app no resolvió por el estudiante lo que este debía razonar;
4. que las pistas ayudan sin regalar inmediatamente la solución;
5. que la interacción tiene una función pedagógica;
6. que la app conserva la intención de la práctica original;
7. que el Resumen documenta aprendizaje y no solamente aciertos.

# 25. Instrucción final obligatoria para Gemini

Todo prompt generado debe terminar exactamente con:

**“Devuélveme el HTML COMPLETO, autónomo y funcional. No un parche. No fragmentos.”**

# 26. Archivos de la skill

Quiero una skill pequeña.

Empieza preferentemente con:

`SKILL.md`

Crea archivos dentro de `references/` solamente si separar contenido mejora claramente la mantenibilidad.

No copies las sesiones del curso dentro de la skill.

No copies los HTML del curso dentro de la skill.

`curso-quarto/` seguirá siendo la fuente curricular.

# 27. Validación de la skill

Después de crearla:

1. valida su estructura según las convenciones de skills disponibles en este entorno;
2. revisa que las instrucciones no sean contradictorias;
3. comprueba que FASE 1 y FASE 2 estén claramente separadas;
4. comprueba que no genere HTML directamente;
5. comprueba que no dependa de `contenidos-2026/`;
6. comprueba que trate `_site/` como salida generada y no como fuente;
7. no modifiques todavía ninguna sesión.

# 28. Prueba posterior

NO pruebes todavía la skill sobre las 37 sesiones.

Después de crearla, indícame:

- ruta de la skill;
- archivos creados;
- propósito de cada archivo;
- cómo invocarla;
- cualquier decisión de diseño que hayas tomado.

Después haremos una primera prueba controlada usando:

**S3 → S4 → S5**

con **S4 como sesión actual**.

En esa primera prueba ejecutaremos únicamente la **FASE 1**.