class Clase1:
    def __init__(self, mivalor):
        self.valor = mivalor
    def __str__(self):
        return "###" + self.valor + "###"
    
class Clase2:
    def __init__(self, mivalor):
        self.valor = mivalor
    def __str__(self):
        return "@@@" + self.valor + "@@@"

c1 = Clase1("Hola")
c2 = Clase2("Adiós")
print(c1)
print(c2)