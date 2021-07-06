# def ordenLongitud(elem):
# 	return len(elem)

nombres = []
nuevo = ""

while (nuevo.upper() != "FIN"):
	nuevo = input("Introduce un nombre (FIN para acabar): ")
	if (nuevo.upper() != "FIN"):
		veces = nombres.count(nuevo)
		if (veces == 0):
			nombres.append(nuevo)

nombres.sort(key=lambda e:len(e))
print("La lista ordenada es: ")
for n in nombres:
	print(n.capitalize() + " ")
