Calabria = "Catanzaro", "Cosenza", "Crotona", "Reggio de Calabria", "Vibo Valentia"
Campania = "Avellino", "Benevento", "Caserta", "Napoli", "Salerno"
Lacio = "Frosinone", "Latina", "Rieti", "Roma", "Viterbo"
Liguria = "Genova", "Imperia", "La Spezia", "Savona"

def elimina_y_agrupa(conjunto, provincia):
	lista = list(conjunto)
	lista.remove(valor)
	print("Sus provincias son (excepto la que ha indiado): ")
	for i in lista:
		print(i.ljust(15), end="")
	Italia = list(Calabria) + list(Campania) + list(Lacio) + list(Liguria)
	Italia.remove(valor)
	print("\n\nLas provincias de Italia en conjunto son: ")
	for i in Italia:
		print(i.ljust(15), end="")

valor = input("Escriba la provincia Italiana: ")

if valor in Calabria:
	print("La región de " + valor + " es Calabria\n")
	elimina_y_agrupa(Calabria, valor)
elif valor in Campania:
	print("La región de " + valor + " es Campania\n")
	elimina_y_agrupa(Campania, valor)
elif valor in Lacio:
	print("La región de " + valor + " es Lacio\n")
	elimina_y_agrupa(Lacio, valor)
elif valor in Liguria:
	print("La región de " + valor + " es Liguria\n")
	elimina_y_agrupa(Liguria, valor)
else:
	print("No se ha encontrado la provincia indicada...")

