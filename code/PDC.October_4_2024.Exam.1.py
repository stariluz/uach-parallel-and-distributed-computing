import threading
import logging
import time
import random
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

CARS_AMMOUNT=20

# Los vehículos que quieren cruzar el puente desde un lado, esperarán a que no haya vehículos de la
# dirección opuesta.

# Generar carros de norte a sur, y generar carros de sur a norte durante toda la ejecución del carro.
class Bridge:
    def __init__(self) -> None:
        # Candado que evita condiciones de carrera en los atributos de la clase
        self.mutex=threading.Lock() 
        # Cantidad de carriles que se pueden usar a la vez
        self.semaphore=threading.Semaphore(2)
        self.north_queue=[]
        self.south_queue=[]
        self.current_direction=None
        self.cars_dispatched=0
    
    # Llego un nuevo carro, así que se agrega a una de las colas del puente
    def add_to_queue(self, index, direction, car):
        with self.mutex:
            if self.current_direction==None:
                self.current_direction=direction
            if direction=='north':
                logging.info(f"Carro nuevo {index} llego desde el {direction}")
                self.north_queue.append(car)
            elif direction=='south':
                logging.info(f"Carro  nuevo {index} cruzando desde el {direction}")
                self.south_queue.append(car)
            else:
                logging.warning("Dirección no valida para el puente")

            
    def next_car(self,):
        # El puente puede ser usado por hasta 2 carros que vengan en la misma dirección
        with self.semaphore:
            car_crossing=None
            
            with self.mutex:
                if self.current_direction == 'north' and len(self.north_queue) > 0:
                    car_crossing = self.north_queue.pop(0)
                elif self.current_direction == 'south' and len(self.south_queue) > 0:
                    car_crossing = self.south_queue.pop(0)
                else:
                    logging.info("Ningun carro esperando...")
                    time.sleep(1)
                    return
            
            car_crossing.start()
            car_crossing.join()

            with self.mutex:
                self.cars_dispatched+=1
                # Hasta que no haya carros en la direccion actual
                # podemos cambiar de dirección de cruce
                if self.current_direction=='north' and len(self.north_queue)==0:
                    self.current_direction='south'
                if self.current_direction=='south' and len(self.south_queue)==0:
                    self.current_direction='north'
    
    def run(bridge):
        # Despachamos los carros que haya, hasta que se acaben
        while bridge.cars_dispatched<CARS_AMMOUNT:
            bridge.next_car()

def cross_car(index, direction):
    logging.info(f"Carro {index} cruzando desde el {direction}")
    time.sleep(3)
    logging.info(f"Carro {index} cruzó")


bridge=Bridge()

# Generamos carros cada ciertos segundos aleatorios
# en dirección aleatorias
def generate_cars():
    for i in range(20): # 20 carros en total
        random_number = random.randint(0, 1)
        direction=None
        if random_number==0:
            direction='north'
        else:
            direction='south'
            
        new_car=threading.Thread(target=cross_car, kwargs={
            "index": i,
            "direction": direction
        })
        bridge.add_to_queue(i,direction,new_car)
        time.sleep(random.randint(0,5))

        

if __name__=="__main__":
    thread_1=threading.Thread(target=generate_cars)
    thread_2=threading.Thread(target=Bridge.run, kwargs={'bridge':bridge})
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()