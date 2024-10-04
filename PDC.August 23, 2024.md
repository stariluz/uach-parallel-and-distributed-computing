Los procesos tienen más sobrecarga que los subprocesos, sobretodo en la iniciación y terminación de su ejecución.
Los procesos no comparten la memoria, para hacerlo hay que seguir cierto s mecanismos, por su lado los subprocesos si pueden compartir la memoria.

Para crear cada proceso se requiere llamadas al sistema separadas en cada proceso. 


### Proceso
- Definition: An executing instance of a program.
- Resources: Separate memory space, files, handles.
- Overhead: Higher overhead from OS management.
- Communication: IPC mechanisms like pipes, sockets.
- Concurrency: Multiple processes execute in parallel
- Paralelism: Multiple copies distributed across cores/machines
- Scheduling: Managed by OS process scheduler.
- Synchronization: Locks, semaforos, mutexes.
- Programming: Message passing model

### GIL
GIL es un mecanismo de bloqueo implementado por Python que evita que 2 hilos accedan a la misma memoria.
A pesar de tener múltiples hilos, solo 1 hilo puede ejecutar python a la vez.
GIL puede fectar en el aprovechamiento de los multihios, sin embargo nos evita muchos de los problemas por accesos de memoria, ademas de facilitar la integración de extenciones de C.

Tarea: Un código implementado con GIL, y otro código que no utilice GIL.