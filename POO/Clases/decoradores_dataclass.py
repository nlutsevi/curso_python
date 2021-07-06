from dataclasses import dataclass

@dataclass(order=True)
class Elemento:
    nombre: str
    proveedor: str
    precio: float
    stock: int = 0

    def __post_init__(self):
        self.etiqueta: str = self.nombre.ljust(20) + "(" + self.proveedor + ")"

    def valorstock(self):
        return "%4.2f" % (self.precio * self.stock)

producto1 = Elemento("Smartwatch TDR", "Zonama", 45.4, 500)
print(producto1)
print(producto1.etiqueta)
producto1.precio = 55.8
print("Cambio de precio:", producto1.precio)
print("El valor del stock es", producto1.valorstock())
producto2 = Elemento("Tablet IPack 12", "Orange", 850.75, 120)
print(producto2)
print("Los dos so iguales?", producto1 == producto2)
print("El primero va antes que el segundo?", producto1 < producto2)