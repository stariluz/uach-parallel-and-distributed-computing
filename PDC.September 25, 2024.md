### Multiprocesing
- Cada proceso tiene su propio intérprete en Python lo que permite la ejecución paralela real,
- Comunicación entre procesos mediante pipes, queues y otros mecanismos.
- API similar a threading.
- Un Pool de procresos.
- 
#### Ventajas
- Aprovecjamiento de múltiples núcleos.
- Evita el Global Interpreter Lock (GIL).
- Mejora en la escalabilidad.
- Comunicación entre procesos.
- Balanceo automático de carga con la clase Pool.
### Desventajas
- Consumo de recursos
- Comunicación más costosa debido a la serialización y deserialización.
- Complejidad de programación para gestionar la comunicación y sincronización.
- Overhead de la creación de procesos. Lleva un overhead de tiempo y recursos.