"""
def mensaje():
    print("Hola, qué tal?")

def sumador():
    num1 = 10
    num2 = 15
    return num1 + num2

mensaje()
suma = sumador()
print(suma)
"""
"""
def nombrecompleto(nombre, apellidos="-Sin apellidos-"):
    return "Te llamas " + apellidos + ", " + nombre

print(nombrecompleto("Irene", "Rosales"))
print(nombrecompleto("Juan Carlos"))
print(nombrecompleto(apellidos="Ruiz Sancho", nombre = "Isabel"))
"""
"""
def usuario(nombre, *aficiones):
    print("Te llamas " + nombre + " y tus aficiones son:")
    texto = ""
    for aficion in aficiones:
        texto = texto + aficion + " "
    print(texto)

usuario("Jose", "nadar", "pescar", "bailar")
"""
def usuario(nombre, *aficiones, **datos):
    print("Te llamas " + nombre + " y tus aficiones son:")
    texto = ""
    for aficion in aficiones:
        texto = texto + aficion + " "
    print(texto)
    for dato in datos:
        if dato == "padre":
            print("Tu padre se llama " + datos[dato])
        if dato == "madre":
            print("Tu madre se llama " + datos[dato])

usuario("Jose", "nadar", "pescar", "bailar", madre="Luisa", padre="Mateo")

listadatos = ["Gregorio", "pasear", "montar en bici", "dormir"]
listadatospersonales = {"madre" : "Julia", "padre" : "Manuel"}
usuario(*listadatos, **listadatospersonales)

