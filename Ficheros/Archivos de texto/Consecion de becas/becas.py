from PyQt5.QtWidgets import *
from PyQt5 import uic
import os

def capacidadarchivo():
	global fichero
	fichero.close()
	fichero = open("solicitantes.txt", "a")
	longitud = fichero.tell()
	fichero.close()
	fichero = open("solicitantes.txt", "a+")
	return longitud

def agregar():
	global fichero
	fichero = open("solicitantes.txt", "a+")
	nombre = ventana.cuadronombre.text()
	apellidos = ventana.cuadroapellidos.text()
	expediente = ventana.cuadronumexpediente.text()
	if ventana.becasi.isChecked():
		beca = "SI"
	elif ventana.becano.isChecked():
		beca = "NO"
	linea = nombre.ljust(10) + apellidos.ljust(20) + expediente.ljust(10) + beca.ljust(2) + "\n"
	fichero.write(linea)
	fichero.close()

def becasasignadas():
	global fichero
	fichero = open("solicitantes.txt", "a")
	final = capacidadarchivo() + 42
	actual = 0
	fichero.seek(actual)
	texto = "EXPEDIENTE".ljust(15) + "ALUMNO".ljust(20)
	texto += "\n"
	texto += "-".center(35, "-")
	texto += "\n"
	while actual <= final:
		contenido = fichero.readline()
		if "SI" in contenido:
			nombre = fichero.read(10)
			nombre = nombre.strip()
			apellidos = fichero.read(20)
			apellidos = apellidos.strip()
			expediente = fichero.read(10)
			expediente = expediente.strip()
			texto += expediente.ljust(15) + (apellidos + ",  " + nombre).rjust(20)
			texto += "\n"
		actual += 42
	mensaje = QMessageBox()
	mensaje.information(ventana, "Alumnos con becas asignadas", texto, mensaje.Ok)
	fichero.close()

def becasdenegadas():
	global fichero
	fichero = open("solicitantes.txt", "a")
	final = capacidadarchivo() - 42
	actual = 0
	fichero.seek(actual)
	texto = "EXPEDIENTE".ljust(15) + "ALUMNO".ljust(20)
	texto += "\n"
	texto += "-".center(35, "-")
	texto += "\n"
	while actual <= final:
		contenido = fichero.readline()
		if "NO" in contenido:
			nombre = fichero.read(10)
			nombre = nombre.strip()
			apellidos = fichero.read(20)
			apellidos = apellidos.strip()
			expediente = fichero.read(10)
			expediente = expediente.strip()
			texto += expediente.ljust(15) + (apellidos + ",  " + nombre).rjust(20)
			texto += "\n"
		actual += 42
	mensaje = QMessageBox()
	mensaje.information(ventana, "Alumnos con becas denegadas", texto, mensaje.Ok)
	fichero.close()

app = QApplication([])
ventana = uic.loadUi("ventanaBecas.ui")
ventana.agregar.clicked.connect(agregar)
ventana.becasasignadas.clicked.connect(becasasignadas)
ventana.becasdenegadas.clicked.connect(becasdenegadas)

ventana.show()
app.exec_()