class cabecera:
    def __init__(self, funcion):
        self.mifuncion = funcion

    def __call__(self, *args):
        resultado = self.mifuncion(*args)
        print("El resultado de la función es el siguiente:")
        return resultado

class numerador:
    def __init__(self, numera=False):
        self.numera = numera

    def __call__(self, mifuncion):
        def gestor(*args):
            self.listado = mifuncion(*args)
            if self.numera:
                return self.numerado()
            else:
                return self.calculototal()
        return gestor

    def numerado(self):
        texto = ""
        contador = 1
        for elemento in self.listado:
            texto += "%d: --- %5.2f\n" % (contador, elemento)
            contador += 1
        return texto

    def calculototal(self):
        total = 0
        for elemento in self.listado:
            total += elemento
        return "%5.2f" % total 



@cabecera
@numerador()
def conIVA(iva, lista):
    listaIVA=[]
    for dato in lista:
        listaIVA.append(dato + (dato * (iva/100)))
    return listaIVA

precios = [300.56, 450.5, 234.86, 200.15]
print(conIVA(21, precios))