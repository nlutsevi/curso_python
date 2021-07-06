class Celsius:
    def __init__(self, temperatura=0):
        self._temperatura = temperatura
    
    def en_farenheit(self):
        return "%3.3f" % ((self._temperatura * 1.8) + 32)
    
    @property
    def temperatura(self):
        return self._temperatura
    
    @temperatura.setter
    def temperatura(self, valor):
        if valor < -273:
            raise ValueError("Esta temperatra no es posible")
        self._temperatura = valor
    
    # temperatura = property(get_temperatura, set_temperatura)

grados = Celsius(37.3)
print(grados.temperatura, "en farenheit:", grados.en_farenheit())
grados.temperatura(-300)
print(grados.temperatura(), "en farenheit:", grados.en_farenheit())