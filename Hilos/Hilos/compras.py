import time
import logging
import concurrent.futures

def suma(cliente):
    nombre = cliente[0]
    lista = cliente[1:]
    logging.debug("Contabilizando compra de %s", nombre)
    total = 0
    for precio in precios:
        total += precio
        time.sleep(.2)
    logging.info("Total a cobrar a %s: %d", nombre, total)

logging.basicConfig(format="%(levelname)s %(asctime)s: %(message)s", level=logging.DEBUG, datefmt="%H:%M:%S")
cliente1 = ("Jose", 100, 200, 300, 400, 500)
cliente2 = ("Marisa", 50, 70, 10, 20, 50, 70, 10, 20)
cliente3 = ("Patri", 2000, 3500, 5000)
cliente4 = ("Carlos", 85000, 25000, 130000)
clientes = (cliente1, cliente2, cliente3, cliente4)
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ejecutor:
    ejecutor.map(suma, clientes)