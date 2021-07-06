cadena = input("Escriba un texto:")

if cadena.isalnum():
    print("Consta de letras y/o números, sin espacios")
if cadena.isalpha():
    print("Consta de letras, sin números y sin espacios")
if cadena.isdigit():
    print("Consta solo de dígitos, sin espacios")
if cadena.isspace():
    print("Consta solo de espacios")
if cadena.islower():
    print("Contiene solamente minúsculas")