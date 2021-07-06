from modulo.funciones import azar as crear_numero
from modulo.funciones import mensajeAcierto as acierto
from modulo.funciones import mensajeFallo as fallo 
from modulo.funciones import mensajeFin as fin
import time

# print("Generando número al azar...")
# for i in range(3, 0, -1):
# 	print("%d ..." % i)
# 	time.sleep(1)

numero = crear_numero(10)
contador = 0
while contador < 3:
	num = eval(input("Cuál es el número generado? "))
	if (num == numero):
		acierto()
		break
	elif num != numero and contador < 2:
		fallo()
	else:
		fin(numero)
	contador += 1