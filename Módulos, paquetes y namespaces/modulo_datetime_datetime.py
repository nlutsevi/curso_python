from datetime import datetime

hoy = datetime.now()
print("Fecha y hora actual:", hoy)
print("La fecha:", hoy.date(), "y la hora", hoy.time())
desglose = hoy.timetuple()
print("Podemos obtener cualquier atributo desglosado: Hora", desglose.tm_hour, "mes", desglose.tm_mon, 
"día del año", desglose.tm_yday)
enIso = hoy.isoformat("#", "hours")
print("Formato ISO con separador # y sólo la hora:", enIso)
cumple = datetime.fromisoformat("1995-10-22T03:15")
print("Mi cumpleaños fue el día", cumple.day, "a las", cumple.hour, "y", cumple.minute)