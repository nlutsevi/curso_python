import threading
import time

class MiHilo(threading.Thread):
    def __init__(self, valor):
        self.valor = valor
        super().__init__() #hacemos referencia al constructor de la clase hererada
    
    def run(self):
        print("El valor transmitido es:", self.valor)
        time.sleep(.5)
        print("FIn del thread con valor", self.valor)

class MiOperador():
    def __init__(self, valor=1):
        self.numero = valor
    
    def factorial(self, valor="nada"):
        if valor != "nada":
            self.numero = valor
        total = 1
        for valor in range(1, self.numero + 1):
            total *= valor
            time.sleep(.05)
        print("Factorial de", self.numero, "es", total)

print("Lanzamos 5 threads como classes")
for i in range(5):
    hilo = MiHilo(i)
    hilo.start()
    hilo.join()

print("\nEjecutamos el método de un objeto, de forma normal")
calculadora1 = MiOperador(60)
calculadora2 = MiOperador()
calculadora3 = MiOperador(15)
calculadora4 = MiOperador(7)
inicio = time.time()
calculadora1.factorial()
calculadora2.factorial(12)
calculadora3.factorial()
calculadora4.factorial()
final = time.time()
print("Tiempo tardado:", final - inicio)

print("\nEjecutamos el mismo método como thread")
hilo1 = threading.Thread(target=calculadora1.factorial)
hilo2 = threading.Thread(target=calculadora2.factorial)
hilo3 = threading.Thread(target=calculadora3.factorial)
hilo4 = threading.Thread(target=calculadora4.factorial)
inicio = time.time()
hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()
hilo1.join()
final = time.time()
print("Tiempop tardado:", final - inicio)