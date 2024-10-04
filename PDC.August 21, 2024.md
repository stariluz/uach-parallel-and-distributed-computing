
### Paralelismo
Las computadoras deben tener múltiples núcleos de procesador.
#### Casos de uso
- IA
- Simulación numérica
- Renderización de gráficos
- Big Data

### Computo distribuído
Paradigma de procesamiento en el cual un conjunto de computadoras interconecatas colaboran para resolver un problema. La distribución ocurre entre múltiples nodos de una red.

#### Casos de uso
- Cómputo de la Nube (Cloud Computing)
- Redes de sensores y monitoreo
- Redes de IoT

### Características
- Multiples nodos autónomos.
- Computación descentralizada.
- Concurrencia.
- Ejecución paralela.
- Almacenamiento distribuído.
- Tolerancia a fallos.
- Entornos heterogéneos.


El problema computacional debe ser capaz de descomponerse en piezas discretas de trabajo que pueden reacilarse simultaneamente.

### Taxonomía de Flynn
Define 4 categorías básicas que describen como se ejecutan las instrucciónes y como se manejan los datos en un sistema de cómputo.

*Instruciton stream* es la secuencia de instrucciones.

#### SIMD. Instrucción única, datos múltiples.
- Tipo de computadora paralela.
- Una única instrucción se ejecuta en paralelo en múltiplles conjuntos de datos.

#### MISD. Instrucciones múltiples, datos múltiples.
- Múltiples instrucciones se aplican a un solo flujo de datos.
- 
#### MIMD. Instrucciones múltiples, datos múltiples.


#### Casos de uso
- Procesamiento de imagenes y gráficos SIMD 
- Simulaciones científicas MIMD
- Big Data SIMD/MIMD
- Computo en la nube MIMD
- Machine learning SIMD/MIMD
