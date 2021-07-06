import threading
import time

def conexion():
    print("Simulando una conexión... Barrera establecida para %d threads" % barrera.parties)
    time.sleep(3)
    print("Tarea de conexión finalizada. Hay %d threads esperando" % barrera.n_waiting)
    barrera.wait()
    print("Conexión establecida")

def acceso1():
    barrera.wait()
    print("Se realiza el acceso 1")

def acceso2():
    barrera.wait()
    print("Se realiza el acceso 2")

barrera = threading.Barrier(3)
hilo1 = threading.Thread(target=conexion)
hilo2 = threading.Thread(target=acceso1)
hilo3 = threading.Thread(target=acceso2)
hilo1.start()
hilo2.start()
hilo3.start()