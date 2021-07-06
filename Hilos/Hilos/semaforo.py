import threading
from time import sleep
import logging

cantidad = eval(input("Cuántos threads a la vez pueden acceder al código? "))
semaforo = threading.Semaphore(cantidad)

class Hilo(threading.Thread):
   def __init__(self, id):
      super().__init__()
      self.id = id
   def run(self):
       with semaforo:
        logging.info("Thread %s entra.", self.id)
        sleep(2)
        logging.info("Thread %s sale.", self.id)

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,
   datefmt="%H:%M:%S")
hilos = []
for contador in range(1, 1+cantidad*2):
   hilos.append(Hilo(contador))
logging.info("Se han creado %d threads, serán usados en bloques de %d en %d",
   cantidad*2, cantidad, cantidad)
for h in hilos:
    h.start()