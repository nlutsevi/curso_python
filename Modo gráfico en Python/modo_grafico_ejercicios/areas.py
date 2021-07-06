from PyQt5.QtWidgets import *

def calculartriangulo():
	get_base = eval(cuadrobase.text())
	get_altura = eval(cuadroaltura.text())
	resultado = (get_base * get_altura) / 2
	resultado = round(resultado, 3)
	resultado_triangulo.setText("Resultado: " + str(resultado))

def calcularrectangulo():
	get_base = eval(cuadrobase.text())
	get_altura = eval(cuadroaltura.text())
	resultado = get_base * get_altura
	resultado = round(resultado, 3)
	resultado_rectangulo.setText("Resultado: " + str(resultado))

def calcularcilindro():
	get_radio = eval(cuadrobase.text())
	get_altura = eval(cuadroaltura.text())
	resultado = 2 * 3.141516 * get_radio * get_altura
	resultado = round(resultado, 3)
	resultado_cilindro.setText("Resultado: " + str(resultado))

app = QApplication([])

w = QWidget()
w.setWindowTitle("Cálculo de áreas")
w.resize(350, 250)

base = QLabel("Base / Radio: ")
altura = QLabel("Altura: ")

cuadrobase = QLineEdit()
cuadroaltura = QLineEdit()

triangulo = QPushButton("Triángulo")
triangulo.clicked.connect(calculartriangulo)
resultado_triangulo = QLabel("")

rectangulo = QPushButton("Rectángulo")
rectangulo.clicked.connect(calcularrectangulo)
resultado_rectangulo = QLabel("")

cilindro = QPushButton("Cilindro")
cilindro.clicked.connect(calcularcilindro)
resultado_cilindro = QLabel("")

grid = QGridLayout()
# grid.setSpacing(10)

grid.addWidget(base, 1, 0)
grid.addWidget(cuadrobase, 1, 1, 1, 2)

grid.addWidget(altura, 2, 0)
grid.addWidget(cuadroaltura, 2, 1, 1, 2)

grid.addWidget(triangulo, 3, 0)
grid.addWidget(resultado_triangulo, 3, 1)

grid.addWidget(rectangulo, 4, 0)
grid.addWidget(resultado_rectangulo, 4, 1)

grid.addWidget(cilindro, 5, 0)
grid.addWidget(resultado_cilindro, 5, 1)


w.setLayout(grid)
w.show()

app.exec_()