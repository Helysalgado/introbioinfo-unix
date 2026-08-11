## Examen Final

Este examen tiene como objetivo evaluar tus habilidades prácticas en la creación y organización de un proyecto, la ejecución de herramientas bioinformáticas como BLAST, y el análisis de resultados. Asegúrate de seguir las instrucciones paso a paso, utilizando comandos correctos y estructurados, y respeta los nombres y rutas especificados.

## Organización del proyecto. [ 20% ]

Sigue las instrucciones que se te indican para generar el repositorio de trabajo ( recuerda poner en un bloque de código las instrucciones a ejecutar ).

**Algoritmo**:

- Ir  al directorio `intro-bioinfo`  de tu usuario.
- Genera una carpeta llamada `scripts` o `bin`
- Dentro de la carpeta `bin`  o `scripts` , crea un script llamado `mk-project.sh` . Este archivo debe tener las siguientes instrucciones/comandos
	a.  Indicar la ruta actual de trabajo
	b. Crear un proyecto llamado `examen-final`  
	c. Crear todas las carpetas de un proyecto `bin data results doc`
	d. Imprimir en pantalla "estructura de proyecto creado!"
- Cambia permisos
- Ejecuta el script. **El script `mk-project.sh` debe ser ejecutado a nivel de `intro-bioinfo` **


**Código/Comandos**

```bash

```


## Sobre blast. [ 20%]

En esta sección vas a ejecutar un `blast` usando como secuencia `query` la hemoglobina beta humana. 

> La beta globina humana es una proteína fundamental que forma parte de la hemoglobina, una molécula esencial para el transporte de oxígeno en los vertebrados, incluida nuestra especie. 
> 
>    Gen asociado: La beta globina está codificada por el gen HBB (ubicado en el cromosoma 11 en humanos).
> 
>    Proteína:
        La beta globina es una cadena polipeptídica compuesta por 147 aminoácidos.
        Es una subunidad de la hemoglobina, que es un tetramero formado por dos cadenas de alfa globina y dos cadenas de beta globina.
> 
> 

Instrucciones:

- Dentro de `data` crea un archivo llamado `hbb.faa` que contenga la hemoglobina beta humana en formato fasta (aquí esta la secuencia ):

```
>gi|4504349|ref|NP_000509.1| beta globin [Homo sapiens]
MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLG
AFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVAN
ALAHKYH
```

- Genera la línea de instrucción de BLAST desde la línea de comandos para realizar una búsqueda en la base de datos no redundante (nr) de manera remota:

Parámetros requeridos:
*  Nombre del programa. Seleccionar el blast adecuado.
* `–query` indica el archivo de entrada (`hbb.faa` que esta dentro de `data`)
* `–remote` indica que la base de datos a utilizar va a buscarla en los servidores de NCBI (si no usamos este argumento buscará la base de datos en el directorio donde está la query)
* `–db  nr` : indica la base de datos (nr en nuestro caso)
* El archivo de salida debe llamarse `hbb.faa.nr.f7` y debe guardarse en la carpeta `results`.
* Usar el formato de salida 7.

Nota: Si quieres ejecutar el blast para probar si tu instrucción esta correcta tardará un poco.  Puedes correrlo en background para liberar tu terminal y seguir con el exámen. (Si tienes error en tu instrucción y no puedes solucionarlo, copia el resultado del blast disponible en `/home/compu2/WelcomeBioinfo/datos/examen-final` para que continúes con las preguntas).
El máximo número de resultados por default es de 500.


```bash

```

## Análisis de los resultados del blast [ 60%]

En esta sección vas a realizar algunos filtros sobre el resultado del blast. Debes estar posicionado en la carpeta  `examen-final`, desde ahí deberás realizar todos los comandos.

¿Qué vamos a evaluar?:

   - Uso de rutas relativas
   - nombrado correcto de archivos
   - comandos correctos, es decir que funcionan.

**Análisis de los datos**

- Explica brevemente los siguientes conceptos

  a. *Alineamiento global* :  
  b. *Alineamiento local* :  
  c. *% de similitud* :  
  d. *% de identidad* :  
  e. *gap* :  
  f. ¿qué se toma en cuenta para decidir que una secuencia es homóloga a otra?

- ¿Cuál es el total de alineamientos encontrados ?
- Manda a un archivo todos los identificadores únicos de las proteínas con los que hizo match la secuencia query.
- ¿Cuantos alineamientos toman en cuenta el tamaño completo de la secuencia query?
- ¿Cuántos secuencias alineadas tienen el mismo tamaño que la secuencia query?
- ¿Cuántas secuencias alineadas son del mismo tamaño que la secuencia query y son 100% idénticas?  
- ¿Cuál es el total de secuencias alineadas con menos de 10 gaps?


