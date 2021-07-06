def suma(num1, num2):
    resultado = num1 + num2
    return resultado

def resta(num1, num2):
    resultado = num1 - num2
    return resultado

def calculadora():
    operacion = ""

    while operacion != "salir":
        operacion = input("Escriba qué quiere hacer: sumar, restar o salir: ")
        if (operacion == "salir"):
            break
        num1 = eval(input("Dime un número: "))
        num2 = eval(input("Dime otro número: "))
        if (operacion == "sumar"):
            resultado = suma(num1, num2)
            print("La suma es: " + str(resultado))
        elif (operacion == "restar"):
            resultado = resta(num1, num2)
            print("La resta es:", resultado)
        else:
            print("Introduzca una operación válida!")

    print("Gracias por usar la calculadora!")
calculadora()
