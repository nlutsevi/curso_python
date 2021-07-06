from PyQt5.QtWidgets import *
from PyQt5 import uic

def calculapre():
	#objeto QCalendar Widget
	fecha = ventana.calendario.selectedDate()
	if fecha.month() == 8:
		plusFecha = 200
	else:
		plusFecha = 0
	#objeto QCombobox
	destino = ventana.destinos.currentText()
	if destino == "Europa":
		plusDestino = 150
	elif destino == "Asia":
		plusDestino = 450
	else:
		plusDestino = 600
	#objueto QRadioButton
	if ventana.envioEstandar.isChecked():
		plusEnvio = 0
	else:
		plusEnvio = 80
	#objeto QLineEdit
	plusPeso = eval(ventana.peso.text())
	precio = plusPeso + plusFecha + plusDestino + plusEnvio
	ventana.resultado.setText(str(precio) + " €")

app = QApplication([])
ventana = uic.loadUi("misventanas/ventana_presupuesto.ui")
ventana.setWindowTitle("Cálculo de Presupuesto")
ventana.calcular.clicked.connect(calculapre)
ventana.show()
app.exec_()