import calendar

año = eval(input("Escriba el año: "))
mes = eval(input("Escriba el mes: "))

calendario = calendar.TextCalendar()
print("El calendario del mes :\n", calendario.formatmonth(año, mes, 5, 3))
print("El calendario anual, en dos files:")
calendario.pryear(año, m=6)