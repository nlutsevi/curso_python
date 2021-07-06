from tkinter import *
from tkinter import ttk 

# CREAMOS LA FUNCIÓN QUE OBTENDRÁ EL NOMBRE Y APELLIDO INTRODUCIDOS Y LOS GUARDARÁ EN RESULTADO
def calcula():
	resultado.set(varnombre.get() + " " + varapellidos.get())

# CREAMOS LA VENTANA
ventana = Tk()
ventana.title("Mi primera ventana en Python")
ventana.geometry("350x150+400+200")
ventana.resizable(False, False)

# AÑADIMOS ESTILOS
ttk.Style().configure("TLabel", foreground="green")
ttk.Style().configure("TBotton", foreground="red")
ttk.Style().configure("Resul.TLabel", background="pink", foreground="brown", relief="ridge")

# CREAMOS ETIQUETAS NOMBRE Y APELLIDOS
etiqueta1 = ttk.Label(ventana, text="Nombre: ", padding=(30,10))
etiqueta1.grid(row=0, column=0)
etiqueta2 = ttk.Label(ventana, text="Apellidos: ", padding=(30, 10))
etiqueta2.grid(row=1, column=0)

# CREAMOS CUADROS DE TEXTO PARA INTRODUCIR NOMBRE Y APELIIDOS
varnombre = StringVar()
cuadro1 = ttk.Entry(ventana, textvariable=varnombre, width=20)
cuadro1.grid(row=0, column=1)
varapellidos = StringVar()
cuadro2 = ttk.Entry(ventana, textvariable=varapellidos, width=20)
cuadro2.grid(row=1, column=1)

# CREAMOMOS EL BOTON ACEPTAR
boton1 = ttk.Button(ventana, text="Aceptar", command=calcula)
boton1.grid(row=2, column=0)

# IMPRIMIMOS EN RESULTADO EN UNA ETIQUETA

resultado = StringVar()
etiqueta3 = ttk.Label(ventana, textvariable=resultado, style="Resul.TLabel")
etiqueta3.grid(row=2, column=1)

ventana.mainloop()
