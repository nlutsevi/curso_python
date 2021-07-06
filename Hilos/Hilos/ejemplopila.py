import concurrent.futures
import time
import logging

def trabajo(numero):
    logging.info("Thread %s: iniciado", numero)
    time.sleep(3)
    logging.info("Thread %s: finalizado", numero)

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,
    datefmt="%H:%M:%S")
print("Vamos a ejecutar 3 threads como una pila:")
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ejecutor:
    ejecutor.map(trabajo, range(3))
# concurrent.futures.ThreadPoolExecutor(max_workers=3).map(trabajo, range(3))
print("Esta es la última instrucción")