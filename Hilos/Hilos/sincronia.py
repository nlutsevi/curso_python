import threading
import concurrent.futures
import time
import logging

class OrigendeDatos():
    def __init__(self):
        self.valor = 0
        self.bloqueo = threading.RLock()
    
    def posiciona(self, tope):
        self.bloqueo.acquire()
        while self.valor < tope:
            self.update("posiciona")
        self.bloqueo.release()

    def update(self, numero):
        with self.bloqueo:
            logging.info("Thread %s: inicio update", numero)
            valor_obtenido = self.valor
            time.sleep(0.5)
            valor_obtenido += 10
            self.valor = valor_obtenido
            logging.info("Thread %s: fin update", numero)

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,
    datefmt="%H:%M:%S")
misdatos = OrigendeDatos()
logging.info("Valor inicial del dato: %d", misdatos.valor)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ejecutor:
    for num in range(2):
        ejecutor.submit(misdatos.update, num)
logging.info("Vamos a actualizar el valor hasta llegar a 50")
hilo = threading.Thread(target=misdatos.posiciona, args=(50,))
hilo.start()
hilo.join()
logging.info("Valor final del dato: %d", misdatos.valor)