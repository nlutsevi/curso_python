import random

def azar(num):
	numero = random.randint(1, num)
	return numero

def mensajeAcierto():
	print("Acertaste!")

def mensajeFallo():
	print("Lo siento, fallaste!")

def mensajeFin(numero):
	print("No hay oportunidades, no acertasete! El número era el " + str(numero))

