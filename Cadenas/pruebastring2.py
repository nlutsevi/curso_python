print("resultado del clásico".upper())
cadena = input("Indique el resultado en formato Equipo Goles Equipo2 Goles: ")
espacios = cadena.count(" ") #solo admitiremos 3 espacios
if espacios != 3:
    print("El formato escrito es erróneao!")
else:
    posBarc = cadena.lower().find("barcelona")
    posMad = cadena.lower().find("madrid")
    if posBarc == -1 or posMad == -1:
        print("Los equipos no son correctos!")
    else:
        if posBarc < posMad:
            print("El partido se jugó en el Camp Nou")
        else:
            print("El partido se jugó en Santiago Bernabeu")