class convertidor:
    def __init__(self, cambio):
        self.cambio = cambio
        self.eur = 0
        self.usd = 0

    def cantidad_euros(self, nuevovalor):
        self.cantidad_eur = nuevovalor
        self.cantidad_usd = nuevovalor * self.cambio

    def cantidad_dolares(self, nuevovalor):
        self.cantidad_usd = nuevovalor
        self.cantidad_eur = nuevovalor / self.cambio

    def muestra_euros(self):
        return round(self.cantidad_eur, 2)

    def muestra_dolares(self):
        return round(self.cantidad_usd,2)