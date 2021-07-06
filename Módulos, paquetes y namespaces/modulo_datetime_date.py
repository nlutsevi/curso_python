from datetime import date

cadena = input("Dime la fecha de tu cumpleaños en formato(YYYY-MM-DD): ")
cumple = date.fromisoformat(cadena)
print("Naciste el año %d mes %d y día %d" % (cumple.year, cumple.month, cumple.day))
print("La semana del año fue:", cumple.isocalendar()[1])

hoy = date.today()
print("Hoy es", hoy)
diferencia = hoy - cumple
print("Diferencia (objeto timedelta):", diferencia)