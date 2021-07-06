numeros = range(10,0, -1)
print("Esta es la tabla de multiplicar del 5 al ravés:")
for numero in numeros:
    if numero == 5:
        continue
    print("5 x", numero, "=", 5 * numero)
print("Final del programa")