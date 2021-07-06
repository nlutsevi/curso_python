import json

archivo = open("json_socios.json", "r")
mijson = json.load(archivo)
archivo.close()

def agregar_compra(lista):
    producto = ""
    while producto != "salir":
        producto = input("Número del arículo ('salir' para finalizar): ")
        if producto != "salir":
            cantidad = input("Cantidad comprada: ")
            lista.append({"codigo": producto, "cantidad": cantidad})

num_socio = input("Escribe el número del socio a buscar: ")
print("BUSQUEDA DE SOCIO:\n")
existe = False
for socio in mijson["socios"]:
    if socio["num-socio"] == num_socio:
        existe == True
        agregar_compra(socio["compras"])
if existe == False:
    print("El socio", num_socio, "no existe, procedemos a darle de alta")
    nombre = input("Nombre del socio ")
    producto = ""
    compras = []
    agregar_compra(compras)
    mijson["socios"].append({
        "num-socio": num_socio,
        "nombre": nombre,
        "compras": compras})

archivo = open("json_socios.json", "w")
json.dump(mijson, archivo, ensure_ascii=False, indent=3)
archivo.close()
print("Guardarmos todos los cambios realizados, la estructura es:\n", mijson)