import calendar, datetime

calendario = calendar.Calendar()
año = eval(input("Escriba el año: "))
mes = eval(input("Escriba el mes: "))

domingos = ""
for fecha in calendario.itermonthdates(año, mes):
	if fecha.isoweekday() == 7:
		domingos += fecha.strftime("%d/%m/%y") + "   "
print("Los domingos del mes", mes, "son:", domingos)

sabados = ""
for fecha in calendario.itermonthdays4(año, mes):
	if (fecha[3] == 5):
		sabado = datetime.date(fecha[0], fecha[1], fecha[2])
		sabados += sabado.strftime("%d/%m/%y") + "   "
print("Los sabados del mes", mes, "son:", sabados)

mes = calendario.yeardatescalendar(año, 6)
print("Del año", año, "el primer día de la tercera semana del quinto mes del segundo semestre es",
mes[1][4][2][0])