from clases.convertidor import *

class cuentabancaria(convertidor):
    def __init__(self, numcuenta, cambio, inicial_eur):
        super(cuentabancaria, self).__init__(cambio)
        self.numcuenta = numcuenta
        self.moneda = "e"
        self.cantidad_euros(inicial_eur)
    
    def moneda_actual(self, moneda):
        if moneda == "e":
            self.moneda = "e"
        elif moneda == "d":
            self.moneda = "d"
        else:
            raise TypeError("La moneda solamente puede ser euro(e) o dólar(d)")
    
    def ingresar(self, cantidad):
        if self.moneda == "e":
            self.cantidad_euros(self.muestra_euros() + cantidad)
        elif self.moneda == "d":
            self.cantidad_dolares(self.muestra_dolares() + cantidad)
        else:
            raise TypeError("Falta indicar la moneda!")

    def retirar(self, cantidad):
        if self.moneda == "e":
            self.cantidad_euros(self.muestra_euros() - cantidad)
        elif self.moneda == "d":
            self.cantidad_dolares(self.muestra_dolares() - cantidad)
        else:
            raise TypeError("Falta indicar la moneda!")