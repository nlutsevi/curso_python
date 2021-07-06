from PyQt5.QtWidgets import *
from PyQt5 import uic
import os

def borrar_registro():
	global fichero
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
		mensaje(ventana.cuadronombre.text() + " eliminado. Operación finalizada.")
		ventana.cuadronombre.setText("")
	else:
		os.remove("agendatemporal.txt")
		mensaje("No se ha encontrado el nombre indicado")

def capacidadarchivo():
	global fichero
	fichero.close()
	fichero = open("agenda.txt", "a")
	longitud = fichero.tell()
	fichero.close()
	fichero = open("agenda.txt", "a+")
	return longitud

def listado():
	final = capacidadarchivo() - 50
	actual = 0
	fichero.seek(actual)
	frase = "contenido de la agenda".upper().center(30, "=") + "\n"
	while actual <= final:
		nombre = fichero.read(20)
		email = fichero.read(30)
		frase += "\nNombre: " + nombre + "\nEmail: " + email + "\n".ljust(45, "-")
		actual += 50
	mensaje(frase)

def agregar_datos():
	minombre = ventana.cuadronombre.text()
	miemail = ventana.cuadroemail.text()
	registro = minombre.ljust(20) + miemail.ljust(30)
	fichero.write(registro)
	frase = "Registro añadido: #" +  registro + "#"
	print(frase)
	mensaje(frase)
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
	mensaje(frase)

def eliminar_archivo():
	if fichero.closed is False:
		fichero.close()
		mensaje("El archivo estaba abierto, ha habido que cerrarlo.")
	os.remove(fichero.name)
	mensaje("Archivo eliminado.")

def mensaje(texto):
	mensaje = QMessageBox()
	mensaje.information(ventana, "Resultado", texto, mensaje.Ok)

app = QApplication([])
ventana = uic.loadUi("ventanarchivo.ui")
ventana.crearabrir.clicked.connect(crear_archivo)
ventana.eliminar.clicked.connect(eliminar_archivo)
ventana.agregar.clicked.connect(agregar_datos)
ventana.listar.clicked.connect(listado)
ventana.borrar.clicked.connect(borrar_registro)

ventana.show()
app.exec_()