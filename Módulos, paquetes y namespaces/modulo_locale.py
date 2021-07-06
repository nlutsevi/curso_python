import locale

def imprime(cantidad):
	print("\nUna cantidad monetaria con el símbolo local:", 
	locale.currency(cantidad, symbol=True, grouping=True))
	print("La misma cantidad con el símbolo internacional:",
	locale.currency(cantidad, symbol=True, grouping=True, international=True))

locale.setlocale(locale.LC_ALL, '')
print("El código de lenguaje y codificacion es", locale.getdefaultlocale())
imprime(45640.3645)

japon = locale.normalize("ja")
print("\nCódigo de configuración regional de Japón codificado:", japon)
japon = japon[:japon.find(".")]
print("Código de configuración regional sin codificacion:", japon)
locale.setlocale(locale.LC_ALL, japon)
imprime(45640.3645)