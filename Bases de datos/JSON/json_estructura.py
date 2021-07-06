import json

mijson = {}
mijson.setdefault("socios", [])

data = {"socios": [{"num-socio": "", "nombre": "", "compras": [{"codigo": "","cantidad": ""}]}]}
archivo = open("json_socios.json", "w")
json.dump(data, archivo, ensure_ascii=False, indent=3)
archivo.close()

