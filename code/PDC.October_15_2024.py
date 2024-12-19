import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Definir el tamaño de la matriz
N = 4

# Inicializar matrices
if rank == 0:
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)
else:
    A = np.zeros((N, N))
    B = np.zeros((N, N))

# Transmitir la matriz B a todos los procesos
comm.Bcast(B, root=0)

# Distribuir las filas de A entre todos los procesos
filas_por_proceso = N // size
A_local = np.zeros((filas_por_proceso, N))
comm.Scatter(A, A_local, root=0)

# Realizar la multiplicación local de matrices
C_local = np.dot(A_local, B)

# Recoger la matriz resultante
C = None
if rank == 0:
    C = np.zeros((N, N))
comm.Gather(C_local, C, root=0)

if rank == 0:
    print("Matriz resultante C:\n", C)
