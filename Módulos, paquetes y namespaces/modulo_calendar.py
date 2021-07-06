import calendar, locale

locale.setlocale(locale.LC_ALL, '')
año = eval(input("Escribe un año: "))
mes = eval(input("Escribe un mes: "))

print("\nEl año", año, "sí" if calendar.isleap(año) else "no", "es bisiesto")

print("\nLos días de la semana completos y abreviados son: ")
contador = 0
for nombre in calendar.day_name:
	print(nombre, "-", calendar.day_abbr[contador])
	contador += 1

calendar.setfirstweekday(calendar.SUNDAY)
print("\nAhora el primer día de la semana es:", calendar.firstweekday())
print("\nY este es el calendario del mes indicado:\n")
calendar.prmonth(año, mes)
print("\nUn poco más ancho:\n")
calendar.prmonth(año, mes, 5)
