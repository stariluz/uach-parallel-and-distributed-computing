import multiprocessing
import time

def worker(number):
    print(f"Process {number} starting")
    # Simulamos una tarea más pesada
    start = time.time()
    while time.time() - start < 5:  # 5 segundos de trabajo
        pass
    print(f"Process {number} finished")

if __name__ == '__main__':
    start_time = time.time()

    # Crear procesos
    processes = []
    for i in range(50):  # Aumentar el número de procesos
        process = multiprocessing.Process(target=worker, args=(i,))
        processes.append(process)
        process.start()

    # Esperar a que todos los procesos terminen
    for process in processes:
        process.join()

    end_time = time.time()
    print(f"Todos los procesos han terminado en {end_time - start_time:.2f} segundos.")
