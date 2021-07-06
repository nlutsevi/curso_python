"""
dicc = {"precio1" : 2300, "precio2" : 3450, "precio3" : 2760}

print("Diccionario original: ")
print(dicc)

print("Añadimos un nuevo elemento: ")
dicc["precio4"] = 1000
print(dicc)

print("Eliminamos un elemento: ")
del dicc["precio1"]
print(dicc)

print("Las claves son: ")
print(dicc.keys())

print("Los valores son: ")
print(dicc.values())
"""

def agregar():
	clave = input("Escriba el nombre: ")
	valor = input("Escriba la edad: ")
	dicc.setdefault(clave, valor)

def eliminar():
	clave = input("Escriba el nombre a eliminar: ")
	print("Eliminando %s ... %s" % (clave, dicc.pop(clave, "No encontrado")))

def listar():
	print("Contenido del diccionario: ")
	print(dicc)
	print("nombres".ljust(15) + "edades".rjust(5))
	for clave in dicc.items():
		print(clave[0].ljust(15) + clave[1].rjust(5))

dicc = dict()
opcion = -1
while opcion != 0:
	print("\nMENU DE OPCIONES")
	print("1 - Agregar elementos")
	print("2 - Eliminar elementos")
	print("3 - Listar contenido")
	print("0 - Salir")
	opcion = eval(input("Escriba opcion: "))
	if opcion == 1:
		agregar()
	elif opcion == 2:
		eliminar()
	elif opcion == 3:
		listar()
print("Gracias por usar el programa!")