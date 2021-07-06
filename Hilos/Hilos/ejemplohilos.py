import threading
import time
import logging

def trabajo(numero):
    logging.info("Thread %s: iniciado", numero)
    time.sleep(3)
    logging.info("Thread %s: finalizado", numero)

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO,
    datefmt="%H:%M:%S")
hilos = list()
for num in range(3):
    logging.info("Thread pincipal, crea y lanza thread %d", num)
    hilo = threading.Thread(target=trabajo, args=(1,))
    hilos.append(hilo)
    hilo.start()

for num, mihilo in enumerate(hilos):
    logging.info("Thread principal, esperando al thread %d", num)
    mihilo.join()
    logging.info("Thread principal, thread %d finalizado", num)