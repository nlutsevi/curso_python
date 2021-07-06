import json
import threading
import logging


def ciudades(lista):
    logging.info("Comienzo a recorrer las ciudades")
    for ciudad in lista:
        with condicion:
            info_ciudad.clear()
            info_ciudad.append(ciudad)
            info_ciudad.append("(no encontrado)")
            info_ciudad.append("(no encontrado)")
            logging.info("Esperando datos de %s", info_ciudad[0])
            condicion.wait()
            logging.info("Los datos encontrados son: Nombre: %s Habitantes: %s Alcalde: %s\n", info_ciudad[0], info_ciudad[1], info_ciudad[2])
        
def info():
    archivo = open("lista_ciudades.json", "r")
    mijson = json.load(archivo)
    archivo.close()
    while True:
        with condicion:
            for ciudad in mijson["ciudades"]:
                if ciudad["nombre"] == info_ciudad[0]:
                    info_ciudad[1] = ciudad["habitantes"]
                    info_ciudad[2] = ciudad["alcalde"]
            condicion.notifyAll()


logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,
    datefmt="%H:%M:%S")
condicion = threading.Condition()
lista = ("Macondo", "Moscu", "Barcelona", "Camelot")
info_ciudad = []
hilo1 = threading.Thread(target=ciudades, args=(lista,))
hilo2 = threading.Thread(target=info, daemon=True)
hilo1.start()
hilo2.start()