Procesadores vs Núcleos vs Procesadores Lógicos vs Hilo
Un procesador es la pieza completa que se encarga de realizar todos los calculos que la computadora (el resto de piezas de hardware) mediante el software le vaya pidiendo.
single-core-hyperthreading-cpu-diagram
Los nucleos se pueden entender como subprocesadores dentro de un gran CPU. El CPU es el encargado de hacerlos funcionar en sintonía como si fuera un solo procesador, no obstante, este tendra la capacidad ejecución en paralelo.
quad-core-hyperthreading-cpu-diagram

Logical CPU. Los CPUs lógicos o procesadores lógicos son el equivalente a la cantidad de hilos que se pueden ejecutar entre todos los nucleos del procesador. Si tenemos 8 cpus lógicos, y nuestro procesador es de 4 nucleos, entonces cada nucleo puede ejecutar 2 hilos a la par.


Hilo. El hilo es una secuencia lógica de procesamiento de un programa, diseñada para trabajar en concurrencia, dicho de otra forma, se podra ejecutar a partes para que otros programas también puedan ejecutarse en intervalos que determine el CPU.
Two threads Running Concurrently in a Single Program

¿Qué es el Hyper-Threading?
HT consiste en duplicar algunos componentes internos de la CPU dentro del mismo chip, como registros o cachés de primer nivel, de forma que se pueda compartir información entre dos hilos de ejecución diferentes sin tener que pasar por el bus del sistema con los correspondientes cuellos de botella y problemas de pérdida de velocidad. Esto también permite que si un proceso tiene que esperar una interrupción, otro proceso pueda seguir utilizando la CPU sin que se detenga.
Caractersticas equipo actual


Bibliografia
https://www.daniloaz.com/en/differences-between-physical-cpu-vs-logical-cpu-vs-core-vs-thread-vs-socket/
https://www.iitk.ac.in/esc101/05Aug/tutorial/essential/threads/definition.html