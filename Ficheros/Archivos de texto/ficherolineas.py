def agregar():
	print("\nAGREGAR PAÍS/CAPITAL")
	pais = input("Escriba el país: ")
	capital = input("Escriba el capital: ")
	fichero.write(pais + "\n")
	fichero.write(capital + "\n")

def buscar():
	print("\nBUSCAR")
	mipais = input("Escriba el país a buscar: ")
	mipais = mipais.title()
	fichero.seek(0)
	pais = "comenzamos"
	micapital = "Lo siento, no se encuentra ese país."
	while pais != "":
		pais = fichero.readline().title()
		capital = fichero.readline().title()
		if pais == mipais + "\n":
			micapital = "La capital de " + mipais + " es" + capital
	print(micapital)

def listar():
	print("\nLISTADO")
	fichero.seek(0)
	contenido = fichero.readlines()
	print("Contenido exacto:")
	print(contenido)
	print("Contenido controlado:")
	print("PAÍS".ljust(20) + "CAPITAL")
	print("-".center(30, "-"))
	pais = "comenzamos"
	fichero.seek(0)
	while pais != "":
		pais = fichero.readline().replace("\n", "")
		capital = fichero.readline().replace("\n", "")
		print((pais.ljust(20) + capital.ljust(20)).title())


fichero = open("paises y capitales.txt", "a+")

opcion = ""
while opcion != "0":
	print("\n\nMENU DE OPCIONES")
	print("1 - Añadir país/capital")
	print("2 - Buscar")
	print("3 - Listar")
	print("0 - Salir")
	opcion = input("Indique la opción: ")
	if opcion == "1":
		agregar()
	elif opcion == "2":
		buscar()
	elif opcion == "3":
		listar()
fichero.close()
print("\nFIN DEL PROGRAMA")
