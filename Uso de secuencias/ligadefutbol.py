print("LIGA DE FUTBOL\n")

goles_barca = int(input("Goles del FC Barcelona: "))
goles_madrid = int(input("Goles del Real Madrid: "))
goles_betis = int(input("Goles del Betis "))
goles_sevilla = int(input("Goles del Sevilla "))
goles = {goles_barca, goles_madrid, goles_betis, goles_sevilla}

dicc = {"FC Barcelona" : goles_barca, "Real Madrid" : goles_madrid, "Betis" : goles_betis, "Sevilla" : goles_sevilla}

promedio = sum(goles)/len(goles)
float(promedio)
print("\nPromedio de goles: " + str(promedio))

maximo = max(goles)
float(maximo)
maximo_key = max(dicc, key = dicc.get)
print("Equipo con máximo de goles(" + str(maximo) + "): " + maximo_key)

minimo = min(goles)
float(minimo)
minimo_key = min(dicc, key = dicc.get)
print("Equipo con mínimo de goles(" + str(minimo) + "): " + minimo_key)

del dicc[maximo_key]
del dicc[minimo_key]
print("\nLa Liga discriminando al máximo y al mínimo queda: ")
print(dicc, "\n")
