tarifas = "sencillo", 1500, "doble", 1900

def imprime():
	i = 0
	while (i < len(tarifas)):
		print(tarifas[i].ljust(10) +
		str(tarifas[i+1]).rjust(5))
		i += 2
	
print("Tupla original: ")
imprime()
tarifas = list(tarifas)
tarifas[1] = 1700
tarifas = tuple(tarifas)
print("\nTupla alterada: ")
imprime()