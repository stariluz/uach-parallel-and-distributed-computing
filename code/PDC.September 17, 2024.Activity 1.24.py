import threading
import time
import random

# Creamos el semáforo con un valor inicial de 5 para los 5 lugares de estacionamiento
parking_lot = threading.Semaphore(5)

def car_thread(car_id):
    print(f"Auto {car_id} está intentando entrar al estacionamiento.")
    parking_lot.acquire()  # Intentar entrar al estacionamiento
    print(f"Auto {car_id} ha entrado al estacionamiento.")
    
    # Simulamos que el auto está estacionado por un tiempo aleatorio
    time.sleep(random.randint(1, 5))
    
    print(f"Auto {car_id} está saliendo del estacionamiento.")
    parking_lot.release()  # Salir del estacionamiento

# Crear y lanzar los 10 hilos de los autos
def main():
    threads = []
    for car_id in range(1, 11):
        thread = threading.Thread(target=car_thread, args=(car_id,))
        threads.append(thread)
        thread.start()
    
    # Esperar a que todos los autos terminen
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
