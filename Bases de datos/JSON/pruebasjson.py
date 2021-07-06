import json

candidato = {
    "nombre" : "Ramón",
    "edad" : 35,
    "casado" : True,
    "vehículos" : [
        {"modelo": "BMW 230", "cv": 142},
        {"modelo": "Ford Edge", "cv": 238}
    ]
}

cadena_json = json.dumps(candidato, ensure_ascii=False, indent=4)
print("Cadena a partir de datos en formato JSON:", cadena_json)
objeto_json = json.loads(cadena_json)
print("Objeto JSON a partir de cadena:", objeto_json)
print("Tipo de cadena_json:", type(cadena_json))
print("Tipo de objeto_json:", type(objeto_json))