class Dispositivo:
	def __init__(self, puntuacion=0, precio=100000, fabricante="(no indicado)", modelo="(no indicado)", tipo="Smartphone"):
		self.fabricante = fabricante
		self.tipo = tipo
		self.modelo = modelo
		if isinstance(puntuacion, (int, float)):
			self.puntuacion = puntuacion
		else:
			raise TypeError("La puntuación tiene que ser un número")
		if isinstance(precio, (int, float)):
			if precio > 0:
				self.precio = precio
			else:
				self.precio = 100000
		else:
			raise TypeError("El precio debe ser un número")
	
	def __str__(self):
		return self.tipo + " fabricado por " + self.fabricante + "\nModelo: " + self.modelo + "\nPuntuación: " + str(self.puntuacion) + "\nPrecio: " + str(self.precio) + "€"

	def calidadprecio(self):
		return ((self.puntuacion * self.puntuacion) * 10) / self.precio

	def __gt__(self, disp2):
		if self.tipo == disp2.tipo:
			diferencia = self.calidadprecio() - disp2.calidadprecio()
			return diferencia > 0
		else:
			raise TypeError("Los dispositivos no son del mismo tipo")

	def __lt__(self, disp2):
		if self.tipo == disp2.tipo:
			diferencia = self.calidadprecio() - disp2.calidadprecio()
			return diferencia < 0

		else:
			raise TypeError("Los dispositivos no son del mismo tipo")
	
	def dimePuntuacion(self):
		return self.puntuacion
	
	def dimePrecio(self):
		return self.precio

# d1 = Dispositivo(3.25, 159, "Samsung", "Galaxy Tab 15", "Tablet")
# print(d1)
# print("...")
# d2 = Dispositivo(4.75, 260, "Oppo")
# print(d2) 

def calidad_precio(disp1, disp2):
	print("\nComparamos la relación calidad-precio de %s %s con %s %s" % (disp1.fabricante, disp1.modelo, disp2.fabricante, disp2.modelo))
	if (disp1 > disp2):
		return "Es mejor " + disp1.fabricante + " " + disp1.modelo
	elif (disp1 < disp2):
		return "Es mejor " + disp2.fabricante + " " + disp2.modelo
	else:
		return "Tienen la misma relación calidad-precio"

d3 = Dispositivo(8.25, 780, "HTC", "One M80")
d4 = Dispositivo(9.25, 450, "LG", "G25", "Smartphone")
d5 = Dispositivo(9.25, 450, "Sony", "Xperia XZ23")
d6 = Dispositivo(6.82, 329, "BQ", "Tesla W85", "Tablet")

print(calidad_precio(d3, d4))
print(calidad_precio(d4, d3))
print(calidad_precio(d4, d5))
# print(calidad_precio(d4, d6))

lista = [d3, d4, d5, d6]
lista.sort(key=Dispositivo.dimePuntuacion)
print("\nDISPOSITIVOS ORDENADOS POR PUNTUACIÓN:")
for disp in lista:
	print(" Puntuación: %.2f %s %s Precio: %i" % (disp.puntuacion, disp.fabricante, disp.modelo, disp.precio))

lista.sort(key=Dispositivo.dimePrecio)
print("\nDISPOSITIVOS ORDENADOS POR PRECIO:")
for disp in lista:
	print(" Puntuación: %.2f %s %s Precio: %i" % (disp.puntuacion, disp.fabricante, disp.modelo, disp.precio))