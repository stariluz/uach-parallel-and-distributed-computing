import threading
import time

# Función que representa la tarea del daemon thread, que escribe en un archivo
def daemon_task():
    with open("daemon_output.txt", "w") as f:
        for i in range(5):
            print(f"Daemon thread is working... {i+1}/3")
            f.write(f"Daemon thread is running... {i+1}/5\n")
            f.flush()  # Forzar escritura inmediata
            time.sleep(1)

# Función que representa la tarea del hilo no daemon
def non_daemon_task():
    for i in range(3):
        print(f"Non-daemon thread is working... {i+1}/3")
        time.sleep(1)

# Crear los hilos daemon y no daemon
daemon_thread = threading.Thread(target=daemon_task)
daemon_thread.daemon = True  # Configurar el hilo como daemon
non_daemon_thread = threading.Thread(target=non_daemon_task)

# Iniciar ambos hilos
daemon_thread.start()
non_daemon_thread.start()

# Esperar que el hilo no daemon termine
non_daemon_thread.join()

print("El hilo no daemon terminó. El programa principal finalizó.")
