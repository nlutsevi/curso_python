incidencia = input("Indique la incidencia: ")

problema = incidencia.upper()

print("Gestión de incidencias".upper().center(80, '-'))
print("Indique la incidencia: " + incidencia.capitalize())

if ('ERROR' in problema):
	paneles = problema.count("PANEL")
	if (paneles == 0):
		print("INCIDENCIA NO RECONOCIDA\n")
	elif (paneles == 1):
		print("Detectado un error en 1 panel\n")
	else:
		print("Detectado un error en " + str(paneles) + " paneles\n")
elif ("AVISO" in problema):
	conmutador = problema.count("CONMUTADOR")
	if (conmutador == 0):
		print("INCIDENCIA NO RECONOCIDA\n")
	else:
		if ('VERDE' in problema):
			print("Atasco en la puerta de salida\n")
		elif ('AZUL' in problema):
			print("Reponer aceite en cinta")
		else:
			print("INCIDENCIA NO RECONOCIDA\n")
else:
	print("INCIDENCIA NO RECONOCIDA\n")
