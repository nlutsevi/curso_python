import json

archivo = open("participantes.json", "r")
mijson = json.load(archivo)
archivo.close()

print("LECTURA DE PARTICIPANTES:\n")
for persona in mijson["participantes"]:
    aficiones=""
    for aficion in persona["aficiones"]:
        aficiones += aficion + " "
    print(persona["nombre"], "de", persona["ciudad"], ", tiene", persona["edad"], "años, sus aficiones son", aficiones)