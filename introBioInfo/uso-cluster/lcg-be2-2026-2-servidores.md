# Notas BE2

## Conexión

```
ssh USUARIO@chaac.lcg.unam.mx
```

## Archivos de trabajo
```
cd /export/space3/users/$USER
cp -R /export/space3/users/ajhernan/be2 .
cd be2
```

## Monitoreo de procesos

### ps
```
ps -f -u $USER
ps --pid PID

```
Columnas -f:
```
UID PID PPID C STIME TTY TIME CMD
```


### top

Columnas: 
```
PID USER PRioridad NIce VIRT/RES/SHR Status %CPU %MEM TIME COMMAND
```
Comandos:
- c muestra toda la línea de comandos 
- 1 muestra todos los cores
- d permite establecer el periodo de actualización, default 3 segundos
- f permite controlar las columnas, ej seleccionar %mem y s para ordenar por memoria
- q para salir


### htop
Cores
Memoria/Swap
Tasks, carga, uptime
Columnas:
```
PID USER PRioridad NIce VIRT/RES/SHR Status %CPU %MEM TIME COMMAND
```
Comandos:
- u para seleccionar el usuario
- P ordenar por %CPU
- M ordenar por %MEM
- T ordenar por TIME
- / o F3 buscar
- F4 filtrar
- t o F5 mostrar árbol, + o -
- F7/F8 modificar nice
- k o F9 enviar señal kill
- c para "colorizar", U para descolorizar
- TAB muestra la siguiente pestaña I/O
- Se pueden usar las flechas y el ratón
- q para salir

### watch

```
watch -n 3 "ps -f -u $USER"

watch -n 3 "ps -o pid,ni,pri,%cpu,stat,comm -u $USER |(sed -u 1q; sort -n -r -k 4)"

watch -n 3 "ps -o pid,ni,pri,%cpu,stat,comm -u $USER --sort -%cpu"

watch -n 1 qstat
```
Nota: se sale con Ctrl-c


## Ejecución de programas

### Ejecución en primer plano
```
blastn -db BlastDB/ntRed -query sequences.fa

blastn -db BlastDB/ntRed -query sequences.fa -out salida-blastn.txt
```
Hay que esperar que termine.


### Ejecución en segundo plano

#### Con ampersand al final
```
blastn -db BlastDB/ntRed -query sequences.fa -out salida-blastn.txt &
```
Nota: mandar salida de blast a archivo con -out  
Opción: ejecutar en primer plano, ctrl-z, bg

#### Con nohup y &
```
nohup blastn -db BlastDB/ntRed -query sequences.fa &
```
Nota: lo que se mande a pantalla se guardará en el archivo nohup.out  
Cuidado con ejecutar varios nohup en el mismo directorio al mismo tiempo, el archivo nohup.out tendrá todas las salidas mezcladas.

#### Con screen
```
screen
```
Despegar o salir del screen (detach) con Ctrl-a d

Ver el ID del screen:
```
screen -list
```
Unirse o regresar al screen (attach) con:
```
screen -r SCREENID
```
#### Con tmux
```
tmux
```
Dividir la sesión: Ctrl-b " (vertical), Ctrl-b % (horizontal)

Despegar de la sesión (detach): Ctrl-b d

Ver el ID de la sesión:
```
tmux ls
```
Unirse o regresar a la sesión (attach) con:
```
tmux a -t ID
```


### Ejecución desde un script en bash

Crear archivo:
```shell
nano blastn.sh
```
Contenido del script:
```bash
#!/bin/bash

CWD=$(dirname "$(realpath "$0")")
BLASTDB=$CWD/BlastDB # blast usa BLASTDB
BLASTDBNAME=ntRed
BLASTQUERY=sequences.fa
TS=$(date +%Y%m%d)
BLASTOUT=salida-blastn-$BLASTDBNAME-${BLASTQUERY%%.*}-$TS.txt

echo blastn -db $BLASTDB/ntRed -query $BLASTQUERY -out $BLASTOUT
blastn -db $BLASTDB/$BLASTDBNAME -query $BLASTQUERY -out $BLASTOUT
echo Hecho.
```

Ejecutar el script:
```
bash blastn.sh
```
Nota: chmod +x blastn.sh; ./blastn.sh

### Ejecutar varios programas

#### Ejecuciones secuenciales:
```bash
for f in {1..99}
do
  blastn -db BlastDB/ntRed -query BlastIn/sequences_${f}.fasta -out salida-blastn-${f}.txt 
done
```

O ejecutar script:
```
bash blastn-for.sh
```


#### Ejecuciones concurrentes (al mismo tiempo):

Primero un ejemplo sencillo de parallel:
```
parallel -j 4 "echo {1}" ::: uno dos tres cuatro cinco seis siete ocho nueve diez once doce trece catorce quince
```
Nota: ejecutar parallel --citation, escribir "will cite"

Ejecutar 4 blastn al mismo tiempo:
```bash
parallel -j 4 "blastn -db BlastDB/ntRed -query BlastIn/sequences_{1}.fasta -out salida-blastn-{1}.txt" ::: {1..99}
```
O ejecutar script:
```
bash blastn-parallel.sh
```

Ejecutar blastn-for y blast-parallel con time y comparar tiempos.

### Ejecución usando un planificador de trabajos

#### SGE: resumen de comandos

Listar nodos y estado
```
qhost
```

Listar colas y estado
```
qstat -g c
```

Iniciar un trabajo interactivo
```
qrsh
```

Enviar a ejecutar un trabajo
```
qsub script.jdl
```

Mostrar los trabajos actuales enviados por todos los usuarios
```
qstat -u \*
```

Monitorear continuamente mis trabajos
```
watch -n 1 qstat
```

Eliminar un trabajo
```
qdel JOBID
```

#### Enviar un trabajo que ejecuta Blastn

Script blastn.jdl, define los nombres de los archivos de salida (-o) y error (-e) estándar 
```bash
#!/bin/bash
#$ -N Blastn
#$ -cwd
#$ -S /bin/bash
#$ -o salida-$JOB_NAME-$JOB_ID.out
#$ -e salida-$JOB_NAME-$JOB_ID.err
source /etc/bashrc
BLASTDB=$PWD/BlastDB # blast usa BLASTDB
BLASTDBNAME=ntRed
BLASTQUERY=sequences.fa

time blastn -db $BLASTDBNAME -query $BLASTQUERY
```
Enviar trabajo:
```
qsub blastn.jdl
```
La salida de blast va a la salida estándar, ver el archivo .out

**Blastn definiendo archivo de salida**

Script blastn-out.jdl, define que use la cola long, y en la línea de comandos de blastn se usa -out para definir el nombre del archivo de salida de blastn.
```bash
#!/bin/bash
#$ -N BlastnOut
#$ -cwd
#$ -S /bin/bash
#$ -o salida-$JOB_NAME-$JOB_ID.out
#$ -e salida-$JOB_NAME-$JOB_ID.err
#$ -q long
source /etc/bashrc

BLASTDB=$PWD/BlastDB # blast usa BLASTDB
BLASTDBNAME=ntRed
BLASTQUERY=sequences.fa
TS=$(date +'%Y%m%d%M%H%S')
BLASTOUT=salida-${JOB_NAME}-${JOB_ID}-${BLASTDBNAME}-${BLASTQUERY%%.*}-${TS}.txt

time blastn -db $BLASTDBNAME -query $BLASTQUERY -out $BLASTOUT
```

Enviar trabajo:
```
qsub blastn-out.jdl
```
La salida de blast queda en el archivo .txt

**Blastn definiendo el número de threads**

```bash
#!/bin/bash
#$ -N BlastnThreads
#$ -cwd
#$ -S /bin/bash
#$ -o $JOB_NAME-$JOB_ID.out
#$ -e $JOB_NAME-$JOB_ID.err
#$ -q default
#$ -pe smp 8
#$ -l s_rt=00:55:00
#$ -l h_rt=01:00:00
source /etc/bashrc
BLASTQUERY=sequences.fa

TS=$(date +'%Y%m%d%M%H%S')
BLASTOUT=salida-${JOB_NAME}-${JOB_ID}-${BLASTDBNAME}-${TS}.txt
BLASTDB=$PWD/BlastDB # blast usa BLASTDB
BLASTDBNAME=ntRed

echo "blastn -db $BLASTDBNAME -query $BLASTQUERY -num_threads $NSLOTS -out $BLASTOUT"
blastn -db $BLASTDBNAME -query $BLASTQUERY -num_threads $NSLOTS -out $BLASTOUT
```
Enviar el trabajo:
```
qsub blastn-threads.jdl
```
Ver -pe smp 8 y $NSLOTS

Script blastn-threads-nt.jdl, busca sobre la base de datos nt (casi 400GB), por lo que tarda un poquito más.


**Blastn en arrayjob definiendo el número de threads**

Script blastn-arrayjob-threads.jdl, reserva 4 cores, define un arrayjob de 1 a 99 tareas, y un tiempo de ejecución límite duro de 1 hora. En la línea de comandos de blastn se usa -num_threads NSLOTS para hacer coincidir el número de cores reservados.
```bash
#!/bin/bash
#$ -N BlastnArrayThreads
#$ -cwd
#$ -S /bin/bash
#$ -q default
#$ -pe smp 4
#$ -t 1-99:1
#$ -l h_rt=01:00:00
#  -o $JOB_NAME-$JOB_ID.out
#  -e $JOB_NAME-$JOB_ID.err
source /etc/bashrc
BLASTDB=$PWD/BlastDB # blast usa BLASTDB
BLASTDBNAME=ntRed
BLASTIN=/export/storage/users/ati/BlastIn/sequences_${SGE_TASK_ID}.fasta
OUTDIR="salidas-${JOB_NAME}-${BLASTDBNAME}"
mkdir -p $OUTDIR
BLASTOUT=${OUTDIR}/salida-${JOB_ID}-${SGE_TASK_ID}.txt

if [[ ! -f "${BLASTIN}" ]]; then echo "$0: archivo $BLASTIN no existe" >&2; exit 2; fi 

echo "blastn -db ${BLASTDBNAME} -query ${BLASTIN} -num_threads ${NSLOTS} -out ${BLASTOUT}"
blastn -db ${BLASTDBNAME} -query ${BLASTIN} -num_threads ${NSLOTS} -out ${BLASTOUT}
```
Enviar trabajo:
```
qsub blastn-arrayjob-threads.jdl
```
Genera 99 archivos de salida con terminación -out.txt


