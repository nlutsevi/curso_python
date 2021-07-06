import json

mijson = {}
mijson.setdefault("participantes", [])
nombre = ""
print("INTRODUCCIÓN DE PARTICIPANTES:\n")
while nombre != "salir":
    nombre = input("Indica el nombre ('salir' para finalizar): ")
    if nombre != "salir":
        ciudad = input("indica la ciudad: ")
        edad = input("indica la edad: ")
        aficiones = []
        aficion = ""
        while aficion != "fin":
            aficion = input("Escribe una afición ('fin' para finalizar): ")
            if aficion != "fin":
                aficiones.append(aficion)
            mijson["participantes"].append({
                "nombre": nombre,
                "ciudad": ciudad,
                "edad": int(edad),
                "aficiones": aficiones})
            print("-" * 30)
print("DICCIONARIO FORMADO:", mijson)
archivo = open("participantes.json", "w")
json.dump(mijson, archivo, ensure_ascii=False, indent=3)
archivo.close()