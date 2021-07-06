nombre = input("Indica el nombre del archivo: ")
try:
	fichero = open(nombre + ".txt", "r")
	raise IOError("Error de comunicación!")
	nombre = fichero.read(20)
	email = fichero.read(30)
	print("Primer nombre:", nombre)
	print("Primer email:", email)
	fichero.close()
except FileNotFoundError:
	print("\nEl archivo indicado no existe")
	# raise
except IOError as mensaje:
	print(mensaje)
else:
	nombre = fichero.read(20)
	email = fichero.read(30)
	print("Primer nombre", nombre)
	print("Primer email:", email)
	fichero.close()
finally:
	try:
		fichero.close()
	except NameError:
		print("No se puede cerrar si no ha llegado a abrir!")
print("\nEl programa ha finalizado correctamente")