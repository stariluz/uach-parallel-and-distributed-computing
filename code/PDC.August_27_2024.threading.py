import threading
import time

def worker(number):
    print(f"Thread {number} starting")
    # Simulamos una tarea más pesada
    start = time.time()
    while time.time() - start < 5:  # 5 segundos de trabajo
        pass
    print(f"Thread {number} finished")

if __name__ == '__main__':
    start_time = time.time()

    # Crear hilos
    threads = []
    for i in range(50):  # Aumentar el número de hilos
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Todos los hilos han terminado en {end_time - start_time:.2f} segundos.")
