import threading
import random

def resultados():
    print("Esperando a que se genere la lista...")
    condicion.acquire()
    condicion.wait()
    condicion.release()
    for num in lista:
        print(num, " ", end="")
    print("\nTotal de elementos:", len(lista))

def proceso():
    print("Hilo que genera la lista...")
    condicion.acquire()
    for numeros in range(200):
        valor = random.randint(1, 100)
        lista.append(valor)
    print("200 números generados")
    condicion.notifyAll()
    condicion.release()

lista = []
condicion = threading.Condition()
hilo1 = threading.Thread(target=resultados)
hilo2 = threading.Thread(target=proceso)
hilo1.start()
hilo2.start()