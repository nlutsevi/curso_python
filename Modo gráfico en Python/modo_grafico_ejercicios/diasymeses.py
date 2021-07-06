import tkinter as tk
from tkinter import *
from tkinter import ttk 

dias = ("LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO")
meses = ("ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE")

def comprobar():
	nombre = cuadro1.get().upper()
	if nombre in dias:
		cuadrodias.insert(END,nombre)
	elif nombre in meses:
		cuadromeses.insert(0,nombre + "\n")
	else:
		texto.set("Error\n Escriba un día o un mes")

ventana = Tk()
ventana.title("Días y meses")
ventana.geometry("580x300+200+200")

etiqueta_nombre = ttk.Label(ventana, text="Escriba el nombre: ", padding=(0,15))
etiqueta_nombre.grid(row=0, column=0)

varnombre = StringVar()
cuadro1 = ttk.Entry(ventana, textvariable=varnombre, width=20)
cuadro1.grid(row=0, column=1)

texto = StringVar()
etiqueta_error = ttk.Label(ventana, textvariable=texto)
etiqueta_error.grid(row=1, column=0)

etiqueta_dias = ttk.Label(ventana, text="DÍAS:")
etiqueta_dias.grid(row=2, column=0)
etiqueta_meses = ttk.Label(ventana, text="MESES:")
etiqueta_meses.grid(row=2, column=3)

vardias = StringVar()
cuadrodias = tk.Listbox(ventana, listvariable=vardias, height=10, bg="lightblue", justify=CENTER)
cuadrodias.grid(row=3, column=0)

varmeses = StringVar()
cuadromeses = tk.Listbox(ventana, listvariable=varmeses, height=10, bg="lightblue", justify=CENTER)
cuadromeses.grid(row=3, column=3)


boton1 = ttk.Button(ventana, text="Introducir", command=comprobar)
boton1.grid(row=0, column=3)

ventana.mainloop()
