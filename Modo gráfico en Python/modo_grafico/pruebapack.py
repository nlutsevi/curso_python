from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("Frames")
ventana.maxsize(300, 300)
ventana.geometry("300x300+450+320")

ttk.Style().configure("Arriba.TFrame", background="green")
ttk.Style().configure("Abajo.TFrame", background="blue")
ttk.Style().configure("Amarillo.TLabel", background="yellow", relief="sunken", padding=10)
ttk.Style().configure("Rojo.TLabel", background="red", relief="ridge", padding=8)

zona1 = ttk.Frame(ventana, width=50, height=50, style="Arriba.TFrame")
zona1.pack(side=TOP, expand=True, fill=BOTH)
eti = ttk.Label(zona1, text="arriba", style="Amarillo.TLabel")
eti.pack()
ttk.Label(zona1, text="abajo", style="Amarillo.TLabel").pack(side=BOTTOM)

zona2 = ttk.Frame(ventana, width=30, height=30, style="Abajo.TFrame")
zona2.pack(side=BOTTOM, expand=True, fill=BOTH)
ttk.Label(zona2, text="izquierda", style="Rojo.TLabel").pack(side=LEFT)
ttk.Label(zona2, text="derecha", style="Rojo.TLabel").pack(side=RIGHT)

ventana.mainloop()
