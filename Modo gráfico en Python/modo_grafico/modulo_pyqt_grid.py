from PyQt5.QtWidgets import *

def abandonar():
	mensaje = QMessageBox()
	respuesta = mensaje.information(w, "Cerrar", "Deseas cerrar?", mensaje.Ok, mensaje.Cancel)
	if respuesta == mensaje.Ok:
		app.instance().quit()

def enviarform():
	f = QDialog(w)
	f.setWindowTitle("Formulario")
	f.resize(200, 250)
	f.setFixedWidth(200)
	formnombre = QLabel("Nombre:\n" + cuadronombre.text())
	formemail = QLabel("Email:\n" + cuadroemail.text())
	formpetic = QLabel("Petición:\n" + cuadropetic.toPlainText())
	formpetic.setWordWrap(True)
	cierradialog = QPushButton("Cerrar")
	cierradialog.clicked.connect(f.close)
	q = QVBoxLayout()
	q.addWidget(formnombre)
	q.addWidget(formemail)
	q.addWidget(formpetic)
	q.addWidget(cierradialog)
	f.setLayout(q)
	f.show()
	cuadronombre.setText("(enviado)")
	cuadroemail.setText("(enviado)")
	cuadropetic.setText("(enviado)")

app = QApplication([])

w = QWidget()
w.setWindowTitle("Formulario de peticiones")
w.resize(350, 250)

nombre = QLabel("Nombre: ")
email = QLabel("Email: ")
petic = QLabel("Petición: ")

cuadronombre = QLineEdit()
cuadroemail = QLineEdit()
cuadropetic = QTextEdit()

enviar = QPushButton("Enviar")
enviar.clicked.connect(enviarform)
cerrar = QPushButton("Cerrar")
cerrar.clicked.connect(abandonar)

grid = QGridLayout()
grid.setSpacing(15)

grid.addWidget(nombre, 1, 0)
grid.addWidget(cuadronombre, 1, 1, 1, 2)

grid.addWidget(email, 2, 0)
grid.addWidget(cuadroemail, 2, 1, 1, 2)

grid.addWidget(petic, 3, 0)
grid.addWidget(cuadropetic, 3, 1, 5, 2)

grid.addWidget(enviar, 8, 1)
grid.addWidget(cerrar, 8, 2)

w.setLayout(grid)
w.show()

app.exec_()
