count = 0

def adivinanza():
    respuesta = input("De qué color es el cabello blanco de Santiago? ")
    if respuesta != "blanco":
        if globals()["count"] < 3:
            globals()["count"] += 1
            print("Este el el intento número " + str(count))
            if count < 3:
                adivinanza()
            else:
                print("Ha llegado a 3 intentos y ha perdido...")
    elif respuesta == "blanco" and globals()["count"] < 3:
        globals()["count"] += 1
        print("Ha ganado con " + str(count) + " intentos!!!")

adivinanza()

        

