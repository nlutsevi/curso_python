elementos = "Aluminio", "A1", "Azufre", "S", "Bismuto", "Bi", "Cloro", "Cl", "Mercurio", "Hg"

def buscar_por_elem():
	valor = input("Introduzca el elemento a buscar: ")
	if valor in elementos:
		indice = elementos.index(valor)
		if (indice % 2 == 0):
			print(valor, "............", elementos[indice+1])
		else:
			print("Ha introducido un símbolo en vez de un elemento")
	else:
		print("Elemento no encontrado...\n")

def buscar_por_simbolo():
	valor = input("Introduzca el símbolo a buscar: ")
	if (valor in elementos):
		indice = elementos.index(valor)
		if (indice % 2 != 0):
			print(elementos[indice-1], "..........", valor)
		else:
			print("Ha introducido un elemento en vez de un símbolo")
	else:
		print("Elemento no encontrado...\n")

opcion = -1
while opcion != 0:
	print("TABLA PERIODICA - MENU DE OPCIONES")
	print("1 - Buscar por elemento")
	print("2 - Buscar por símbolo")
	print("0 - Salir")

	opcion = eval(input("Escriba la opcion: "))
	if opcion == 1:
		buscar_por_elem()
	elif opcion == 2:
		buscar_por_simbolo()
print("Gracias por usar el programa!")

