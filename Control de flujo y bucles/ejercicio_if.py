print("Yo elijo entre pedra, papel o tijera")
yo = input()
print("Tu elijes entre pedra, papel o tijera")
tu = input()

if (yo == tu):
    resultado = "empate!"
    print("Tu jugada es " + tu + " y mi jugada es " + yo + ", por lo tanto " + resultado)
elif ((yo == "piedra" and tu == "tijeras") or (yo == "tijeras" and tu == "papel") or (yo == "papel" and tu == "piedra")):
    resultado = "yo gano!"
    print("Tu jugada es " + tu + " y mi jugada es " + yo + ", por lo tanto " + resultado)
else:
    resultado = "yo pierdo..."
    print("Tu jugada es " + tu + " y mi jugada es " + yo + ", por lo tanto " + resultado)
print("Final del programa")