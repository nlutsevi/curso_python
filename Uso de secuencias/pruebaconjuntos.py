conjunto = "Italia", "Grecia", "Italia", "China", "Grecia", "Brasil"
paises = set(conjunto)
europa = set({"Francia", "Italia", "España", "Grecia", "Alemania", "Portugal"})

def listado(conjunto):
	for pais in conjunto:
		print(pais.ljust(15), end="")

paises.remove("China")
paises.add("Turquia")
paises.add("Alemania")

print("Contenido actual del listado de paises: ")
listado(paises)

print("\n\nContenido actual del listado de Europa: ")
listado(europa)

print("\n\nUnion de los dos conjuntos: \n")
listado(paises | europa)

print("\n\nIntersección de los dos conjuntos (elementos en común): ")
listado(paises.intersection(europa))

print("\n\nDiferencia de los dos conjuntos (elementos de paises que no están en europa): ")
listado(paises.difference(europa))

print("\n\nDiferencia simétrica de los dos conjuntos (elementos que no están a la vez en ambos conjuntos: ")
listado(paises.symmetric_difference(europa))

paises.update(europa)
print("\n\nActualización de paises con el contenido de europa: ")
listado(paises)