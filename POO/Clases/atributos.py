class vivienda:
	def __init__(self, tipo="casa", precio=0):
		self.tipo = tipo
		self.precio = precio

micasa = vivienda(precio=230000)
print("Tipo de vivienda:", micasa.tipo, "Precio:", micasa.precio)

if hasattr(micasa, "habitaciones"):
	print("Tiene atributo 'habitaciones'")
else:
	print("No tiene atributo 'habitaciones'")
if hasattr(micasa, "tipo"):
	print("Tiene atributo 'tipo'")
else:
	print("No tiene atributo 'tipo'")

salas = getattr(micasa, "habitaciones", 0)
valor = getattr(micasa, "precio", 3000)
print("Tiene %i habitaciones y vale como mínimo %i" % (salas, valor))

setattr(micasa, "tipo", "chalet")
setattr(micasa, "zona", "centro")
print("El tipo es", micasa.tipo, "y la ubicación es", micasa.zona)

delattr(micasa, "zona")
listado = ["tipo", "precio", "zona"]
delattr(micasa, listado[1])
print("\nListado de atributos usados:")
for atributo in listado:
	valor = getattr(micasa, atributo, "(no existe)")
	print("Atributo:", atributo, "valor:", valor)