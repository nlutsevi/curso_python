import threading
import logging
import time
import random

class Concursantes(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        logging.info("Participante %s comienza!!", self.nombre)
        segundos = random.randint(1, 15)
        time.sleep(segundos)
        logging.info("Participante %s llega a la meta!!", self.nombre)
        self.tiempo = segundos
        barrera.wait()
    
def carrera():
    logging.info("preparando la carrera... hay 3 participantes")
    barrera.wait()
    final = []
    final.append((user1.tiempo, user1.nombre))
    final.append((user2.tiempo, user2.nombre))
    final.append((user3.tiempo, user3.nombre))
    final.sort()
    logging.info("Fin de la carrera!! Ganador: %s en %s segundos", final[0][1], final[0][0])

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,
    datefmt="%H:%M:%S")
barrera = threading.Barrier(4)
user1 = Concursantes("Natasha")
user2 = Concursantes("Pablo")
user3 = Concursantes("Alex")
hilo = threading.Thread(target=carrera)
hilo.start()
user1.start()
user2.start()
user3.start()
