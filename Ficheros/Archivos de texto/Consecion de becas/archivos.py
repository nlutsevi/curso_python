from PyQt5.QtWidgets import *
from PyQt5 import uic
import os

def borrar_registro():
	global fichero
	try:
		fichero.readline()
	except NameError:
		mensaje = QMessageBox()
		mensaje.information(ventana, "Resultado", "ERROR! El archivo no se ha abierto aun.", mensaje.Ok)	
		exit()
	ultimo = capacidadarchivo() - 50
	actual = 0
	fichero.seek(actual)
	nombre_saltar = ventana.cuadronombre.text().ljust(20)
	ficherotemp = open("agendatemporal.txt", "w")
	localizado = False
	while actual <= ultimo:
		nombre = fichero.read(20)
		email = fichero.read(30)
		if nombre != nombre_saltar:
			ficherotemp.write(nombre + email)
		else:
			localizado = True
		actual += 50
	fichero.close()
	ficherotemp.close()
	if localizado:
		os.remove("agenda.txt")
		os.rename("agendatemporal.txt", "agenda.txt")
		fichero = open("agenda.txt", "a+")
		frase = ventana.cuadronombre.text() + " eliminado. Operación finalizada."
		mensaje = QMessageBox()
		mensaje.information(ventana, "Resultado", frase, mensaje.Ok)
		ventana.cuadronombre.setText("")
	else:
		os.remove("agendatemporal.txt")
		mensaje = QMessageBox()
		mensaje.information(ventana, "Resultado", "No se ha encontrado el nombre indicado", mensaje.Ok)


def capacidadarchivo():
	global fichero
	fichero.close()
	fichero = open("agenda.txt", "a")
	longitud = fichero.tell()
	fichero.close()
	fichero = open("agenda.txt", "a+")
	return longitud

def listado():
	try:
		fichero.readline()
	except NameError:
		mensaje = QMessageBox()
		mensaje.information(ventana, "Resultado", "ERROR! El archivo no se ha abierto aun.", mensaje.Ok)
		exit()
	final = capacidadarchivo() - 50
	actual = 0
	fichero.seek(actual)
	frase = "contenido de la agenda".upper().center(30, "=") + "\n"
	while actual <= final:
		nombre = fichero.read(20)
		email = fichero.read(30)
		frase += "\nNombre: " + nombre + "\nEmail: " + email + "\n".ljust(45, "-")
		actual += 50
	mensaje = QMessageBox()
	mensaje.information(ventana, "Resultado", frase, mensaje.Ok)


def agregar_datos():
	try:
		fichero.readline()
	except NameError:
		mensaje = QMessageBox()
		mensaje.information(ventana, "Resultado", "ERROR! El archivo no se ha abierto aun.", mensaje.Ok)
		exit()
	minombre = ventana.cuadronombre.text()
	miemail = ventana.cuadroemail.text()
	registro = minombre.ljust(20) + miemail.ljust(30)
	fichero.write(registro)
	frase = "Registro añadido: #" +  registro + "#"
	print(frase)
	mensaje = QMessageBox()
	mensaje.information(ventana, "Resultado", frase, mensaje.Ok)
	ventana.nombre.setText("")
	ventana.email.setText("")


def crear_archivo():
	global fichero
	fichero = open("agenda.txt", "a+")
	frase = "archivo " + fichero.name + " preparado."
	if fichero.closed:
		frase += "\nEstà cerrado."
	else:
		frase += "\nEstà abierto. Modo de apertura: " + fichero.mode
	mensaje = QMessageBox()
	mensaje.information(ventana, "Resultado", frase, mensaje.Ok)

def eliminar_archivo():
	try:
		fichero.readline()
	except NameError:
		mensaje = QMessageBox()
		mensaje.information(ventana, "Resultado","ERROR! El archivo no se ha abierto aun.", mensaje.Ok)
		exit()
	fichero.close()
	mensaje = QMessageBox()
	mensaje.information(ventana, "Resultado", "El archivo estaba abierto, ha habido que cerrarlo.", mensaje.Ok)
	os.remove(fichero.name)
	mensaje = QMessageBox()
	mensaje.information(ventana, "Resultado", "Archivo eliminado.", mensaje.Ok)


app = QApplication([])
ventana = uic.loadUi("ventanarchivo.ui")
ventana.crearabrir.clicked.connect(crear_archivo)
ventana.eliminar.clicked.connect(eliminar_archivo)
ventana.agregar.clicked.connect(agregar_datos)
ventana.listar.clicked.connect(listado)
ventana.borrar.clicked.connect(borrar_registro)

ventana.show()
app.exec_()