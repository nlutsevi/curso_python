from datetime import datetime, timedelta

comienzo = datetime.today()
jornada = timedelta(hours=8)
descanso = timedelta(hours=1, minutes=35)
comienzo = comienzo.replace(hour=8, minute=0)

fin = comienzo + jornada + descanso
print("Inicio de jornada:", comienzo.strftime("%H:%M"))
print("Fin de jornada:", fin.strftime("%H:%M"))

vacaciones = timedelta(days=30)
meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
"septiembre", "octubre", "noviembre", "diciembre")
comienzo = comienzo.replace(month=8, day=10)
print("Inicio de las vacaciones: %d de %s" % (comienzo.day, meses[comienzo.month - 1]))
fin = comienzo + vacaciones
print("Fin de las vacaciones: %d de %s" % (fin.day, meses[fin.month - 1]))