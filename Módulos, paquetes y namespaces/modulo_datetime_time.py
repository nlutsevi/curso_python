from datetime import time
hora = time(20, 50, 34)
print(hora.strftime("%H horas, %M minutos"))
print("La hora hasta los minutos:", hora.isoformat("minutes"))
hora = hora.replace(minute=35)
print("Igual pero con los minutos cambiados:", hora.isoformat("minutes"))