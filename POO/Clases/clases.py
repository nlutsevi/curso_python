"""
import os

archivo = open("archivo.txt", "a")
print(dir(archivo))
print(type(archivo.name))
print(type(archivo.write))
archivo.close()
os.remove(archivo.name)

nombre = "Jose"
print(type(nombre))

longitud = 850
print(type(longitud))

precio = 940.65
print(type(precio))
"""
"""
class Coordenada:
	def __init__(self, valorx=0, valory=0):
		self.x = valorx
		self.y = valory

coor = Coordenada(20, 35)
print("valor x:", coor.x, "su classe es:", type(coor.x))
print("valor y:", coor.y, "su classe es:", type(coor.y))
print("\nel tipo de la intancia coor es:", type(coor))
print("\nsus atributos son:", dir(coor))

coor2 = Coordenada(85, 120)
print("\nLas coordenadas x de las dos instancias:", coor.x, coor2.x)
coor.x = 39
print("La primera cambiada no afecta al valor de la segunda", coor.x, coor2.x)

coor.comentario = "Esta es la primera instancia de coordenada"
print("\nLos atributos actuales de coor son:", dir(coor))

try:
	print("Comentario de coor:", coor.comentario)
	print("Comentario de coor2:", coor2.comentario)
except:
	print("Error, no existe el atributo")

del coor.y
print(coor.x, coor.y)
"""

class Coordenada:
	def __init__(self, valorx=0, valory=0):
		if isinstance(valorx, (int, float)):
			self.x = valorx
		else:
			raise TypeError("valor x no válido, debe de ser numérico")
		if isinstance(valory, (int, float)):
			self.y = valory
		else:
			raise TypeError("valor y no válido, debe de ser numérico")
		
	def distancia(self, otra):
		# distx = otra.x - self.x
		# disty = otra.y - self.y
		# return((distx * distx) + (disty * disty)) ** 0.5
		nuevacoor = self.restar(otra)
		return nuevacoor.norma()

	def restar(self, otra):
		return Coordenada(otra.x - self.x, otra.y - self.y)

	def norma(self):
		return ((self.x * self.x) + (self.y * self.y)) ** 0.5

	def __str__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ")"

	def __add__(self, otra):
		return Coordenada(self.x + otra.x, self.y + otra.y)

	def __sub__(self, otra):
		return Coordenada(self.x - otra.x, self.y - otra.y)

# try:
# 	coor1 = Coordenada(20, 35)
# 	coor2 = Coordenada(50, 63)
# 	print("Primera coordenada: %i, %i" % (coor1.x, coor1.y))
# 	print("Segunda coordenada: %i, %i" % (coor2.x, coor2.y))
# 	print("Distancia:", coor1.distancia(coor2))	
# except TypeError as textoerror:
# 	print(textoerror)

# coor1 = Coordenada(0,0)
# coor2 = Coordenada(10, 10)
# print("Primera coordenada: %i, %i" % (coor1.x, coor1.y))
# print("Segunda coordenada: %i, %i" % (coor2.x, coor2.y))
# coor3 = coor1.restar(coor2)
# print("Coordenada de la resta: %i, %i" % (coor3.x, coor3.y))
# norma = coor3.norma()
# print("Norma (distancia):", norma)
# print("Coincide con distancia:", coor1.distancia(coor2))

# inicial = Coordenada(35, 78)
# print("\nLa Coordenada creada es: " + str(inicial))
# print("Es lo mismo que imprimirla directamente:", inicial)

inicio = Coordenada(100, 100)
fin = Coordenada(250, 250)
print("\nPrimera coordenada:", inicio)
print("Segunda coordenada:", fin)
print("La suma de coordenadas es:", inicio + fin)
print("La resta de coordenadas es:", inicio - fin)
