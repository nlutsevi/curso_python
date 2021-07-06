import json

archivo = open("json_socios.json", "r")
mijson = json.load(archivo)
archivo.close()

print("LISTADO DE SOCIOS Y COMPRAS:\n")
print("Socio".ljust(6), "Nombre".ljust(15))
for socio in mijson["socios"]:
    print(socio["num-socio"].ljust(6), socio["nombre"].ljust(15))
    print("Código".rjust(6), "Cantidad".ljust(15))
    for compra in socio["compras"]:
        print(compra["codigo"].ljust(6), compra["cantidad"].ljust(15))
