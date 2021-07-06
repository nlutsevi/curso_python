from datetime import datetime

def horario(mifuncion):
    hora_actual = datetime.now().time()
    hora_inicio = datetime.strptime("09:00:00", "%X").time()
    hora_final = datetime.strptime("15:45:00", "%X").time()
    print("Horario de la sala:\n", "- Hora de inicio:", hora_inicio, "\n - Hora del final:", hora_final)
    print("\nHora actual:", hora_actual)
    if hora_actual > hora_inicio and hora_actual < hora_final:
        mifuncion()
    else:
        print("Está fuera del horario!")

def festivos(mifuncion):
    festivos = [datetime(2021, 1, 6).date(), datetime(2021, 11, 1).date(), datetime(2021, 8, 15).date(), datetime(2021, 12, 25).date()]
    fecha_actual = datetime.now().date()
    print("\nLos días festivos son:")
    for festivo in festivos:
        print(festivo)
    print("\nHoy es: ", fecha_actual)
    if fecha_actual in festivos:
        print("Hoy es un festivo, la sala está cerrada!")

@festivos
@horario
def entrar():
    nombre = input("Cómo te llamas? ")
    print("Adelante, puede pasar", nombre.title())
