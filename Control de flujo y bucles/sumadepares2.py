i = 0
resultado = 0

while i <= 100:
    if (i % 2 == 0): #si el número es par
        if (i >= 20 and i <= 30):
            i += 1
            continue
        resultado += i
    i += 1
print("La suma de los números pares entre 1 y 100 es: " + str(resultado))
