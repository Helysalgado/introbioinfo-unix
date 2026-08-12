# Introducción a la Bioinformática


## 1. Identificación del curso

  -----------------------------------------------------------------------
  Elemento                            Descripción
  ----------------------------------- -----------------------------------
  **Nombre**                          Introducción a la Bioinformática

  **Enfoque**                         Unix aplicado a la bioinformática

  **Programa**                        Licenciatura en Ciencias Genómicas

  **Institución**                     Universidad Nacional Autónoma de
                                      México · Centro de Ciencias
                                      Genómicas

  **Ubicación curricular**            Primer semestre; inicio de la línea
                                      de formación en bioinformática y
                                      programación

  **Modalidad**                       Presencial con componente en línea
                                      bajo un modelo de aula invertida

  **Requisitos previos**              Ninguno formal; el curso parte de
                                      cero en Unix

  **Plan operativo 2026**             34 sesiones de 2 horas, S1--S34

  **Organización temática**           6 unidades, con un bloque
                                      transversal de integración y
                                      evaluación entre S14--S17

  **Producto articulador**            Protocolo bioinformático
                                      reproducible que evoluciona durante
                                      el semestre

  **Ejes transversales**              Reproducibilidad y buenas
                                      prácticas; problemas biológicos
                                      reales; uso crítico y responsable
                                      de IA
  -----------------------------------------------------------------------

> **Nota curricular.** El Programa 2026 original describe una duración
> orientativa de aproximadamente 60 horas y 28--30 sesiones. El plan
> operativo desarrollado posteriormente organiza el curso en **34
> sesiones de 2 horas** y desglosa con mayor detalle la automatización,
> HPC y la interpretación de similitud y homología. Esta descripción
> sigue el **plan operativo final S1--S34**.

------------------------------------------------------------------------

## 2. Descripción general

**Introducción a la Bioinformática** es la materia de entrada a la
formación bioinformática de la Licenciatura en Ciencias Genómicas. Su
propósito no es enseñar una colección de comandos ni convertir Unix en
el objeto central del curso. Busca que el estudiante aprenda a
**resolver preguntas biológicas mediante datos y herramientas
computacionales**, documentando cada decisión de forma reproducible y
defendiendo sus conclusiones con evidencia.

El curso introduce simultáneamente tres dimensiones que un
bioinformático necesita aprender a relacionar desde el inicio:

1.  **la dimensión biológica**, que permite comprender qué representan
    una secuencia, un gen, una proteína, una anotación, un genoma o una
    relación de homología;
2.  **la dimensión computacional**, que proporciona el entorno
    Unix/Linux, herramientas de línea de comandos, scripts, servidores y
    cómputo de alto rendimiento;
3.  **la dimensión científica**, que exige formular preguntas,
    identificar la evidencia necesaria, verificar datos, validar
    resultados, reconocer limitaciones y comunicar conclusiones
    reproducibles.

La progresión del curso puede resumirse así:

``` text
pregunta biológica
        ↓
¿qué evidencia necesito?
        ↓
¿qué datos contienen esa evidencia?
        ↓
¿qué operación necesito realizar?
        ↓
¿qué herramienta puede ejecutar esa operación?
        ↓
resultado
        ↓
verificación / validación
        ↓
interpretación
        ↓
conclusión + límites
```

Por ello, una salida correcta de terminal no constituye por sí misma una
respuesta. El estudiante debe ser capaz de explicar **qué hizo, por qué
lo hizo, qué obtuvo, cómo sabe que es correcto y qué puede concluir
biológicamente**.

------------------------------------------------------------------------

## 3. Propósito formativo

Al finalizar el curso, el estudiante deberá ser capaz de abordar un
problema bioinformático básico desde la obtención de los datos hasta la
construcción de una conclusión argumentada.

Esto implica que pueda:

-   organizar un proyecto computacional de manera reproducible;
-   recuperar datos biológicos de fuentes públicas y documentar su
    procedencia;
-   reconocer e interpretar formatos biológicos como FASTA, GenBank y
    GFF3;
-   trabajar con archivos desde Unix/Linux;
-   inspeccionar, filtrar, transformar, resumir y contrastar datos
    genómicos;
-   construir tuberías de procesamiento transparentes;
-   convertir un procedimiento documentado en un script reutilizable;
-   procesar múltiples archivos sin repetir manualmente el análisis;
-   ejecutar tareas en infraestructura remota y comprender el papel de
    un cluster;
-   comparar secuencias y realizar búsquedas de similitud;
-   interpretar métricas de alineamiento y BLAST;
-   distinguir similitud observada de inferencias de homología;
-   formular hipótesis biológicas y declarar los límites de la
    evidencia;
-   utilizar IA generativa como apoyo al razonamiento, sometiendo sus
    respuestas a verificación independiente.

El objetivo final no es que el estudiante recuerde muchos comandos, sino
que desarrolle una forma de pensar transferible a problemas
bioinformáticos posteriores.

------------------------------------------------------------------------

## 4. Principio pedagógico central

El curso se organiza alrededor de una idea:

> **Las preguntas biológicas permanecen; las estrategias de análisis
> evolucionan.**

Una misma pregunta puede reaparecer varias veces durante el semestre. Lo
que cambia es la capacidad del estudiante para responderla.

Por ejemplo:

``` text
inspeccionar manualmente
        ↓
filtrar
        ↓
extraer campos
        ↓
normalizar
        ↓
combinar condiciones
        ↓
calcular
        ↓
integrar el procedimiento
        ↓
automatizarlo
        ↓
ejecutarlo sobre varios archivos
```

La repetición, por tanto, no consiste en rehacer el mismo ejercicio.
Cada regreso debe producir una respuesta **más precisa, más robusta, más
reproducible o mejor sustentada**.

Las herramientas aparecen cuando una limitación del procedimiento
anterior hace evidente su necesidad. El estudiante aprende primero a
reconocer el problema y después incorpora la herramienta que permite
resolverlo.

------------------------------------------------------------------------

## 5. Modelo didáctico

### 5.1 Aula invertida

Los contenidos conceptuales se estudian antes de la sesión mediante
lecciones, lecturas, ejemplos y materiales de consulta. El objetivo es
reservar el tiempo presencial para las actividades que más se benefician
de la interacción:

-   predecir resultados;
-   ejecutar análisis;
-   comparar estrategias;
-   diagnosticar errores;
-   discutir resultados;
-   interpretar evidencia;
-   corregir procedimientos;
-   documentar decisiones;
-   defender conclusiones.

La preparación previa no sustituye la clase: **la habilita**.

### 5.2 Aprendizaje basado en problemas

Los comandos no se practican en abstracto. Se aplican sobre datos
biológicos y preguntas que requieren una decisión analítica.

El patrón esperado es:

``` text
pregunta → dato → operación → herramienta
```

y no:

``` text
herramienta → comando → buscar después para qué sirve
```

### 5.3 Prácticas progresivas e intercaladas

Las prácticas aparecen después del concepto que las hace posibles y
forman una escalera acumulativa. Cuando aplica, cada práctica tiene tres
momentos:

1.  **Antes de clase --- Primer intento.** El estudiante predice,
    propone o intenta una solución.
2.  **Durante el taller.** Ejecuta, compara, diagnostica y mejora.
3.  **Después del taller --- Entrega final.** Corrige, interpreta y
    documenta.

Cada práctica recupera resultados anteriores y debe contribuir al
producto acumulativo del curso.

### 5.4 Aprender a verificar

Se distinguen cuatro niveles:

-   **Reproducibilidad:** otra persona puede repetir el procedimiento.
-   **Verificación:** se comprueba que una operación produjo lo
    esperado.
-   **Validación:** el resultado o interpretación se contrasta con
    evidencia independiente.
-   **Robustez:** se examina si la conclusión resiste estrategias
    alternativas o casos controlados.

------------------------------------------------------------------------

## 6. El protocolo como cuaderno de laboratorio computacional

Desde las primeras sesiones el estudiante construye un `protocolo.md`.

No es un reporte que se escribe al final. Es un **documento vivo** que
registra cómo evoluciona la investigación.

El protocolo conserva:

-   pregunta biológica;
-   subpreguntas;
-   procedencia de los datos;
-   estrategia;
-   comandos y parámetros;
-   archivos de entrada y salida;
-   verificaciones;
-   resultados;
-   interpretación;
-   discrepancias;
-   limitaciones;
-   decisiones;
-   preguntas pendientes.

Una respuesta anterior no necesariamente se borra cuando aparece una
estrategia mejor. Comparar la primera solución con la solución refinada
permite hacer visible el aprendizaje.

La estructura de trabajo recomendada es:

``` text
proyecto/
├── data/
│   ├── source/
│   └── processed/
├── src/
├── results/
└── doc/
```

Los datos originales permanecen intactos en `data/source/`. Las
transformaciones producen nuevos archivos y los scripts se conservan en
`src/`.

------------------------------------------------------------------------

## 7. Competencias del curso

El curso se organiza por **familias de competencias**, no por
herramientas aisladas.

### A. Trabajo reproducible y comunicación científica

El estudiante aprende a:

-   documentar protocolos y reportes en Markdown;
-   organizar proyectos computacionales;
-   aplicar principios FAIR;
-   registrar metadatos de datos y software;
-   comunicar procedimientos y resultados con suficiente información
    para repetirlos.

### B. Dominio del entorno Unix y del cómputo científico

El estudiante aprende a:

-   navegar el sistema de archivos;
-   crear, copiar, mover y gestionar archivos y directorios;
-   comprender permisos y procesos;
-   utilizar ayuda y documentación;
-   conectarse a servidores mediante SSH;
-   transferir archivos de forma verificable;
-   comprender y utilizar infraestructura de cómputo remoto y un sistema
    de colas a nivel usuario.

### C. Manejo de datos y bases de datos biológicas

El estudiante aprende a:

-   relacionar secuencias, genes, proteínas y anotaciones;
-   interpretar FASTA, GenBank y GFF3;
-   distinguir registro, identificador, versión y anotación;
-   recuperar información de bases de datos biológicas;
-   documentar procedencia;
-   verificar integridad;
-   reconocer que distintas fuentes o versiones pueden producir
    discrepancias legítimas.

### D. Análisis y exploración de datos genómicos

El estudiante aprende a:

-   inspeccionar archivos biológicos;
-   reconocer delimitadores, encabezados y valores faltantes;
-   construir redirecciones y tuberías;
-   filtrar con `grep`;
-   utilizar expresiones regulares;
-   ordenar, contar y resumir;
-   transformar texto con `tr` y `sed`;
-   seleccionar campos y expresar condiciones con `awk`;
-   calcular medidas derivadas;
-   interpretar conteos, longitudes, distribuciones y densidades en
    contexto biológico;
-   confrontar resultados con una fuente independiente.

### E. Automatización y programación en shell

El estudiante aprende a transformar un procedimiento manual en una
herramienta reproducible:

-   escribir scripts;
-   utilizar variables;
-   separar procedimiento y datos;
-   recibir parámetros;
-   validar entradas;
-   procesar colecciones de archivos;
-   utilizar ciclos;
-   generar resultados y bitácoras;
-   documentar el contrato de uso de un script;
-   probar un programa con datos distintos de aquellos con los que fue
    desarrollado.

### F. Comparación de secuencias y homología

El estudiante aprende a:

-   interpretar un alineamiento;
-   distinguir identidad, similitud, cobertura, gaps y sustituciones;
-   comprender por qué una búsqueda en una base de datos no equivale a
    realizar muchos alineamientos exhaustivos;
-   ejecutar BLAST;
-   interpretar identidad, cobertura, E-value, bit score y HSP;
-   ordenar candidatos por la calidad conjunta de la evidencia;
-   distinguir similitud observada de homología inferida;
-   razonar sobre ortología, paralogía y xenología;
-   transferir función con cautela;
-   construir y defender una hipótesis biológica reconociendo
    alternativas y evidencia faltante.

### G. Uso responsable de Inteligencia Artificial

El estudiante aprende a:

-   formular prompts útiles para tareas científicas;
-   reconocer cuándo una respuesta de IA necesita verificación;
-   identificar alucinaciones técnicas y sobreinterpretaciones
    biológicas;
-   comparar una propuesta asistida con una línea base construida por él
    mismo;
-   validar con documentación, `man`, pruebas controladas o evidencia
    independiente;
-   registrar el uso relevante de IA;
-   utilizarla como apoyo sin delegar la competencia que debe demostrar.

------------------------------------------------------------------------

## 8. Ejes transversales

### 8.1 Reproducibilidad y buenas prácticas

La reproducibilidad comienza en S1 y atraviesa todo el curso. No aparece
como un tema que se abandona después de aprender Markdown.

Evoluciona así:

``` text
documentar
→ organizar
→ registrar procedencia
→ preservar datos originales
→ registrar comandos
→ verificar
→ integrar
→ automatizar
→ validar
→ defender una conclusión reproducible
```

### 8.2 Razonamiento biológico

Unix es un medio. El estudiante debe regresar continuamente a preguntas
como:

-   ¿qué representa este dato?;
-   ¿qué propiedad biológica estoy midiendo?;
-   ¿qué evidencia necesito?;
-   ¿mi operación realmente responde la pregunta?;
-   ¿qué significa el resultado?;
-   ¿qué otra explicación es posible?;
-   ¿qué no puedo concluir todavía?

### 8.3 IA crítica

La regla central es:

> **Primero a mano; después con IA.**

El flujo esperado es:

``` text
resolución propia
→ línea base
→ consulta a IA
→ contraste
→ verificación independiente
→ corrección
→ decisión final
→ registro en bitacora-ia.md
```

La línea base manual tampoco se considera automáticamente correcta. La
validación debe ser independiente de ambas respuestas.

------------------------------------------------------------------------

# 9. Arquitectura del curso

## Unidad 1 --- Trabajo reproducible y comunicación técnica

**Sesiones:** S1--S2

### Propósito

Establecer desde el inicio una cultura de trabajo reproducible y una
forma científica de documentar el análisis.

### Núcleo conceptual

El estudiante descubre que un análisis bioinformático no consiste
únicamente en obtener un resultado. Debe conservarse la información
necesaria para reconstruir cómo se obtuvo.

### Contenidos principales

-   Markdown;
-   fases de un análisis de datos;
-   pregunta, subpreguntas y estrategia;
-   organización de un proyecto;
-   principios FAIR;
-   metadatos;
-   introducción a IA generativa;
-   prompting científico;
-   alucinaciones, validación y uso ético.

### Evolución esperada

``` text
resultado aislado
        ↓
resultado documentado
        ↓
procedimiento reproducible
```

### Productos

-   inicio de `protocolo.md`;
-   plantilla de reporte;
-   estructura del proyecto;
-   metadatos;
-   apertura de `bitacora-ia.md`.

------------------------------------------------------------------------

## Unidad 2 --- Entorno Unix/Linux y cómputo científico

**Sesiones:** S3--S6

### Propósito

Construir el entorno operativo sobre el que se desarrollará el resto del
curso.

### Contenidos principales

-   Unix y filosofía Unix;
-   shell;
-   ayuda y documentación;
-   sistema de archivos;
-   rutas;
-   archivos y directorios;
-   edición;
-   compresión;
-   permisos;
-   procesos;
-   SSH;
-   transferencia de archivos;
-   verificación de transferencias;
-   panorama de infraestructura de cómputo científico.

El uso operativo de HPC/SGE se recupera posteriormente en S29, cuando el
estudiante ya posee un análisis automatizado que justifica llevar el
trabajo a un cluster.

### Evolución esperada

``` text
usuario de una computadora
        ↓
usuario de Unix
        ↓
usuario de un servidor
        ↓
usuario consciente de infraestructura científica
```

------------------------------------------------------------------------

## Unidad 3 --- Datos y bases de datos biológicas

**Sesiones:** S7--S9

### Propósito

Aprender qué representan los datos biológicos, cómo se estructuran, de
dónde provienen y cómo determinar si el archivo recuperado es realmente
el que se pretende analizar.

### Contenidos principales

-   relación DNA → RNA → proteína;
-   secuencias y anotación;
-   FASTA;
-   GenBank;
-   GFF/GFF3;
-   identificadores y versiones;
-   registros;
-   NCBI y otros recursos biológicos;
-   recuperación documentada;
-   integridad;
-   inspección y transferencia verificable.

### Pregunta formativa central

> **¿Puedo confiar en el dato antes de analizarlo?**

### Evolución esperada

``` text
descargar un archivo
        ↓
comprender qué representa
        ↓
documentar de dónde proviene
        ↓
verificar que llegó íntegro
        ↓
decidir si es adecuado para la pregunta
```

------------------------------------------------------------------------

## Unidad 4 --- Procesamiento y exploración de datos genómicos

**Sesiones:** S10--S23\
**Bloque transversal:** S14--S17

### Propósito

Convertir archivos biológicos en evidencia interpretable mediante flujos
transparentes de inspección, filtrado, transformación, resumen,
contraste y cálculo.

La unidad se desarrolla como una investigación progresiva sobre un
genoma.

### Primera etapa --- Establecer los hechos

**S10--S13**

El estudiante aprende a reconocer la anatomía de los archivos y
construir los primeros inventarios del genoma mediante redirecciones,
tuberías, selección de campos, filtros, ordenamiento y conteos.

La pregunta deja de ser:

> "¿qué comando tengo que usar?"

y se transforma en:

> "¿qué dato necesito localizar y qué operación debo realizar sobre él?"

### Bloque de integración --- S14--S17

S14--S15 recuperan lo aprendido en una investigación guiada con datos
reales.

S16 incorpora **revisión por pares**: el estudiante debe evaluar si la
evidencia de otra persona es suficiente y utilizar esa crítica para
mejorar su propio análisis.

S17 es una **evaluación individual demostrativa** frente a la máquina.
El objetivo es comprobar que la competencia pertenece al estudiante y no
al grupo, al protocolo o a una herramienta de IA.

### Segunda etapa --- Refinar y confrontar la evidencia

**S18--S23**

La progresión conceptual es:

``` text
S18 Precisar
        ↓
S19 Extraer
        ↓
S20 Normalizar
        ↓
S21 Confrontar
        ↓
S22 Condicionar y calcular
        ↓
S23 Integrar
```

El estudiante incorpora expresiones regulares, extracción de
identificadores, normalización, contraste con fuentes independientes y
`awk`.

S23 transforma el protocolo acumulado en un **cuaderno de laboratorio
ejecutable**: una secuencia ordenada y verificable de operaciones capaz
de reconstruir los resultados del análisis.

### Evolución esperada

``` text
analizo mi archivo
        ↓
sé exactamente qué busco
        ↓
extraigo y normalizo
        ↓
contrasto con otra fuente
        ↓
calculo
        ↓
integro un procedimiento reproducible
```

La limitación final es deliberada: el procedimiento funciona, pero
repetirlo manualmente es tedioso y propenso a errores. Esa limitación
crea la necesidad de la Unidad 5.

------------------------------------------------------------------------

## Unidad 5 --- Automatización de análisis bioinformáticos con Shell

**Sesiones:** S24--S29

### Propósito

Transformar el procedimiento reproducible de U4 en una herramienta
reutilizable.

La unidad no comienza preguntando "¿cómo se escribe un script?".
Comienza con un procedimiento que ya funciona y plantea:

> **¿Cómo hago para no tener que ejecutarlo manualmente cada vez?**

### Progresión

``` text
S24 Guardar el procedimiento
        ↓
S25 Separar procedimiento y datos
        ↓
S26 Procesar por lotes
        ↓
S27 Convertirlo en herramienta científica
        ↓
S28 Demostrar que funciona con datos nuevos
        ↓
S29 Ejecutarlo en infraestructura HPC
```

### S24 --- Del protocolo al script

El estudiante reconoce que una secuencia de comandos ya probada puede
convertirse en un programa ejecutable.

### S25 --- Separar procedimiento y datos

Variables, parámetros y validación permiten que el mismo análisis deje
de depender de un archivo específico.

### S26 --- Procesamiento por lotes

Los ciclos permiten analizar colecciones de archivos y generar resúmenes
del conjunto.

### S27 --- Herramienta científica

El script adquiere un contrato de uso: entradas, salidas, ayuda,
mensajes, estructura y documentación. Otro estudiante debe poder
utilizarlo.

### S28 --- Proyecto integrador de automatización

El análisis se ejecuta con datos nuevos, se somete a revisión cruzada y
se defiende. La evidencia integradora sustituye el segundo examen
práctico previsto en versiones anteriores del programa.

### S29 --- HPC/SGE

Solo ahora aparece la necesidad operativa de llevar el análisis al
cluster: existe un procedimiento automatizado que puede ejecutarse como
trabajo computacional. El estudiante envía, monitorea y verifica la
ejecución y comprueba que cambiar de infraestructura no debe cambiar el
significado del resultado.

### Evolución esperada

``` text
sé reproducirlo
        ↓
puedo ejecutarlo
        ↓
puedo parametrizarlo
        ↓
puedo repetirlo sobre muchos datos
        ↓
otra persona puede usarlo
        ↓
puedo demostrar que funciona
        ↓
puedo ejecutarlo en otra infraestructura
```

------------------------------------------------------------------------

## Unidad 6 --- Comparar secuencias para construir hipótesis biológicas

**Sesiones:** S30--S34

### Propósito

Integrar las competencias anteriores en un problema clásico de
bioinformática: utilizar la comparación de secuencias para construir una
hipótesis biológica defendible.

La unidad está deliberadamente organizada como una secuencia de
operaciones intelectuales:

``` text
S30 Comparar
        ↓
S31 Buscar
        ↓
S32 Interpretar
        ↓
S33 Inferir
        ↓
S34 Integrar
```

### S30 --- Comparar

El alineamiento se presenta como una hipótesis de correspondencia entre
posiciones.

Se trabajan:

-   coincidencias;
-   sustituciones;
-   inserciones/deleciones;
-   gaps;
-   identidad;
-   similitud;
-   cobertura;
-   comparación de nucleótidos y proteínas.

### S31 --- Buscar

La pregunta cambia de comparar dos secuencias conocidas a localizar
candidatos en una colección.

Se introduce BLAST como búsqueda heurística y se razona sobre:

-   base de datos;
-   consulta;
-   tamaño de palabra;
-   semillas;
-   extensión;
-   HSP;
-   sensibilidad y velocidad.

### S32 --- Interpretar

Una lista de hits no es una conclusión.

El estudiante integra:

-   identidad;
-   cobertura;
-   E-value;
-   bit score;
-   HSP;
-   alineamientos parciales;
-   ranking de evidencia.

Aprende que una sola métrica puede ser engañosa y que el primer hit no
necesariamente constituye la mejor explicación biológica.

### S33 --- Inferir

Se establece una frontera epistemológica central:

> **La similitud se observa; la homología se infiere.**

Se trabajan:

-   homología;
-   ortología;
-   paralogía;
-   xenología;
-   duplicación;
-   especiación;
-   transferencia cautelosa de función;
-   evidencia suficiente e insuficiente.

El estudiante debe distinguir con precisión qué proviene directamente
del resultado computacional y qué constituye una interpretación
evolutiva.

### S34 --- Integrar

La sesión final utiliza una **secuencia ciega** cuya anotación funcional
fue ocultada sin modificar su secuencia.

El estudiante debe:

1.  inspeccionar el caso;
2.  formular una pregunta;
3.  diseñar una estrategia;
4.  realizar la búsqueda;
5.  seleccionar evidencia;
6.  interpretar resultados;
7.  construir una hipótesis principal;
8.  considerar alternativas;
9.  declarar limitaciones;
10. contrastar críticamente una interpretación asistida por IA;
11. defender su conclusión.

El éxito no consiste necesariamente en recuperar un identificador
exacto. Consiste en formular la **conclusión más fuerte que la evidencia
permite sin afirmar más de lo que los datos sostienen**.

------------------------------------------------------------------------

## 10. Progresión global del estudiante

El curso busca producir una transformación observable:

``` text
S1
“puedo documentar lo que hago”
        ↓
“puedo trabajar en Unix”
        ↓
“entiendo qué representan mis datos”
        ↓
“puedo obtenerlos y verificarlos”
        ↓
“puedo inspeccionarlos y filtrarlos”
        ↓
“puedo transformarlos y medirlos”
        ↓
“puedo contrastar mis resultados”
        ↓
“puedo integrar el análisis”
        ↓
“puedo automatizarlo”
        ↓
“puedo ejecutarlo sobre varios datos”
        ↓
“puedo llevarlo a otra infraestructura”
        ↓
“puedo comparar y buscar secuencias”
        ↓
“puedo interpretar evidencia”
        ↓
“puedo inferir con cautela”
        ↓
S34
“puedo construir y defender una hipótesis bioinformática reproducible”
```

------------------------------------------------------------------------

## 11. Papel de Unix en el curso

Unix es el entorno que permite hacer visibles las operaciones sobre los
datos.

Las herramientas se incorporan progresivamente, entre ellas:

-   navegación y gestión del sistema de archivos;
-   `head`, `tail`, `wc`;
-   `cut`;
-   `sort`;
-   `uniq`;
-   `grep`;
-   expresiones regulares;
-   `tr`;
-   `sed`;
-   `awk`;
-   redirecciones;
-   tuberías;
-   scripts de shell;
-   variables;
-   parámetros;
-   ciclos;
-   SSH y transferencia;
-   sistema de colas/HPC;
-   herramientas de alineamiento y BLAST.

Sin embargo, el dominio esperado no es memorístico. El estudiante debe
saber **qué operación necesita y por qué una herramienta es adecuada
para realizarla**.

------------------------------------------------------------------------

## 12. Papel de la biología

El curso introduce la biología necesaria para interpretar los datos con
los que trabaja.

Entre los conceptos articuladores se encuentran:

-   DNA, RNA y proteínas;
-   genes y productos génicos;
-   coordenadas genómicas;
-   anotación;
-   regiones codificantes;
-   cadenas `+` y `−`;
-   replicones;
-   genomas;
-   secuencias de nucleótidos y aminoácidos;
-   relación entre registro y evidencia;
-   similitud;
-   alineamiento;
-   homología;
-   duplicación y especiación;
-   ortología, paralogía y xenología;
-   transferencia de función.

La biología no aparece como un bloque independiente de teoría. Se
introduce cuando es necesaria para comprender qué representa el archivo,
qué significa una operación o hasta dónde puede sostenerse una
conclusión.

------------------------------------------------------------------------

## 13. Papel de la Inteligencia Artificial

La disponibilidad de IA generativa modifica una pregunta pedagógica
importante: ya no basta con evaluar si el estudiante puede producir una
respuesta, porque una herramienta puede producirla por él.

Por ello, el curso pone mayor énfasis en capacidades que deben
permanecer bajo control del estudiante:

-   formular la pregunta;
-   descomponer el problema;
-   elegir evidencia;
-   detectar supuestos;
-   comprobar una salida;
-   contrastar alternativas;
-   interpretar;
-   reconocer incertidumbre;
-   justificar una decisión;
-   detectar una afirmación no sustentada.

La IA se utiliza para **comparar, revisar, criticar y mejorar** trabajo
que ya posee una línea base.

Ejemplos de errores que el estudiante aprende a detectar incluyen:

-   opciones de comandos inexistentes;
-   sintaxis plausible pero incorrecta;
-   confusión entre variantes de expresiones regulares;
-   comandos que ignoran encabezados o comentarios;
-   conteos biológicamente incorrectos;
-   interpretación excesiva de un hit de BLAST;
-   confusión entre similitud y homología;
-   transferencia injustificada de función.

La bitácora de IA registra el objetivo de la consulta, prompt, respuesta
relevante, estrategia de verificación, correcciones y decisión final.

------------------------------------------------------------------------

## 14. Evaluación y evidencias de aprendizaje

La evaluación privilegia **competencias demostradas** sobre
memorización.

A lo largo del semestre se reúnen evidencias como:

-   protocolos;
-   reportes;
-   metadatos;
-   bitácora de IA;
-   transferencias verificadas;
-   recuperación documentada de datos;
-   análisis de FASTA/GFF3;
-   tablas derivadas;
-   contrastes entre fuentes;
-   scripts;
-   documentación de uso;
-   revisiones por pares;
-   ejecución con datos nuevos;
-   trabajo en cluster;
-   rankings de evidencia;
-   hipótesis de homología;
-   informe final de una secuencia desconocida;
-   defensa de decisiones.

La arquitectura operativa 2026 incluye:

-   tareas y evidencias continuas;
-   mini-proyecto de investigación;
-   revisión por pares;
-   evaluación individual demostrativa;
-   proyecto integrador de automatización en S28;
-   evidencia integradora final de comparación e inferencia en S34.

> **Pendiente de sincronización normativa.** El documento del Programa
> 2026 todavía conserva en su esquema de evaluación la referencia a dos
> exámenes prácticos. El plan operativo final reemplaza el segundo por
> la evidencia integradora de S28. Antes de publicar el programa
> definitivo conviene actualizar esa sección para que Programa, Plan de
> clases y materiales coincidan.

------------------------------------------------------------------------

## 15. Productos acumulativos

El curso no está diseñado como una sucesión de tareas independientes.

Los principales artefactos evolucionan durante el semestre:

### `protocolo.md`

Registra la investigación y sus refinamientos.

### `bitacora-ia.md`

Documenta el uso crítico de asistentes de IA.

### `data/source/`

Conserva los datos originales y su procedencia.

### `data/processed/`

Contiene transformaciones derivadas y trazables.

### `results/`

Reúne resultados producidos por el análisis.

### `src/`

Conserva los scripts que convierten el procedimiento en una herramienta
reutilizable.

La intención es que al final pueda reconstruirse la historia completa:

``` text
dato original
→ procedencia
→ transformación
→ análisis
→ resultado
→ verificación
→ interpretación
→ conclusión
```

------------------------------------------------------------------------

## 16. Rol del docente

El docente no funciona únicamente como demostrador de comandos.

Durante el curso:

-   plantea problemas;
-   hace visibles los criterios de decisión;
-   modela cómo diagnosticar errores;
-   pregunta por la evidencia;
-   solicita predicciones antes de ejecutar;
-   ayuda a distinguir resultado de interpretación;
-   introduce una herramienta cuando la limitación anterior la hace
    necesaria;
-   proporciona retroalimentación durante el proceso;
-   diseña casos donde el estudiante debe decidir y justificar;
-   evita que la IA sustituya la competencia que se pretende
    desarrollar.

------------------------------------------------------------------------

## 17. Rol del estudiante

Se espera que el estudiante pase gradualmente de seguir instrucciones a
tomar decisiones.

Al inicio puede trabajar con pasos muy guiados. Conforme avanza el curso
debe asumir mayor responsabilidad sobre:

-   qué necesita averiguar;
-   qué archivo debe consultar;
-   qué campo contiene el dato;
-   qué operación corresponde;
-   cómo comprobar el resultado;
-   qué estrategia alternativa podría utilizar;
-   cómo documentar el análisis;
-   qué conclusión está sustentada;
-   qué información falta.

El objetivo es construir **autonomía analítica**, no solo autonomía
técnica.

------------------------------------------------------------------------

## 18. Perfil de egreso

Al acreditar el curso, el estudiante debe poder demostrar que:

1.  organiza y documenta un proyecto bioinformático reproducible;
2.  trabaja con soltura básica en Unix/Linux;
3.  utiliza servidores remotos e infraestructura científica a nivel
    usuario;
4.  recupera y verifica datos de bases biológicas;
5.  comprende los principales formatos de secuencia y anotación;
6.  procesa archivos biológicos mediante herramientas de línea de
    comandos;
7.  construye flujos transparentes de filtrado, transformación y
    resumen;
8.  interpreta medidas derivadas en contexto biológico;
9.  contrasta resultados y reconoce discrepancias;
10. automatiza procedimientos mediante scripts reutilizables;
11. procesa múltiples archivos;
12. documenta y prueba sus herramientas;
13. compara secuencias;
14. ejecuta e interpreta búsquedas BLAST;
15. distingue similitud de inferencias de homología;
16. argumenta relaciones de ortología, paralogía o xenología con
    cautela;
17. construye hipótesis a partir de evidencia y declara sus límites;
18. utiliza IA de forma crítica, ética y verificable.

------------------------------------------------------------------------

## 19. Continuidad curricular

El curso constituye el cimiento para asignaturas posteriores de
programación, análisis de datos y bioinformática avanzada.

El estudiante no termina como desarrollador de software bioinformático
completo. Termina con algo previo y fundamental:

-   un entorno computacional funcional;
-   hábitos reproducibles;
-   experiencia trabajando con datos reales;
-   capacidad para descomponer problemas;
-   familiaridad con automatización;
-   criterios para validar resultados;
-   una primera disciplina de interpretación científica.

De esta manera, cuando avance hacia programación formal, algoritmos,
estadística, aprendizaje automático o análisis bioinformáticos
especializados, no partirá únicamente de sintaxis: partirá de una
**forma de trabajo científico-computacional**.

------------------------------------------------------------------------

## 20. Síntesis del diseño

La arquitectura completa puede resumirse en cuatro grandes movimientos:

``` text
I. PREPARAR
U1 — Documentar y trabajar reproduciblemente
U2 — Habitar el entorno Unix/Linux
U3 — Comprender, obtener y verificar los datos

II. ANALIZAR
U4 — Inspeccionar, filtrar, transformar, medir y confrontar

III. AUTOMATIZAR
U5 — Convertir el análisis en una herramienta reutilizable

IV. INTERPRETAR
U6 — Comparar, buscar, interpretar, inferir e integrar
```

Los tres ejes transversales atraviesan los cuatro movimientos:

``` text
                 REPRODUCIBILIDAD
                        │
                        │
PREGUNTA BIOLÓGICA ─────┼───── RAZONAMIENTO CRÍTICO
                        │
                        │
                  IA RESPONSABLE
```

El punto de llegada del curso no es un comando, un script ni un
resultado de BLAST.

Es la capacidad de sostener una afirmación como esta:

> **"Esta es mi conclusión; esta es la evidencia que la sostiene; este
> es el procedimiento con el que la obtuve; así verifiqué el resultado;
> estas son las alternativas que consideré y estos son los límites de lo
> que puedo afirmar."**

Ese es el núcleo de la formación bioinformática que propone el curso.
