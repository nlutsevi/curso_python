import mysql.connector
import random

conex = mysql.connector.connect(user="root", password="", host="localhost")
cursor = conex.cursor()

def crear_tabla():
        cursor.execute("DROP DATABASE IF EXISTS python_ejercicios")
        cursor.execute("CREATE DATABASE python_ejercicios")
        cursor.execute("USE python_ejercicios")

        cursor.execute("DROP TABLE IF EXISTS progresion")
        cursor.execute("CREATE TABLE progresion (" +
        "anyo INTEGER, " +
        "poblacion CHAR(20), " +
        "sueldos INTEGER, equipamiento INTEGER, ganancias INTEGER, PRIMARY KEY(anyo, poblacion))")
        print("Tabla 'progresion' creada con éxito!\n ")

def rellenar_datos():
        poblacion = ["Sabadell", "Martorell", "Sant Cugat"]
        for ciudad in poblacion:
                anyo = 2019
                while anyo < 2023:
                        sueldos = random.randint(50000, 100000)
                        equipamiento = random.randint(50000, 80000)
                        ganancias = random.randint(80000, 200000)
                        cursor.execute("INSERT INTO progresion (anyo, poblacion, sueldos, equipamiento, ganancias) " +
                        " VALUES(%s, %s, %s, %s, %s)", (anyo, ciudad, sueldos, equipamiento, ganancias))
                        conex.commit()
                        anyo += 1
        print("Tabla 'progresion' rellenada con éxito con valores aleatorios!\n")

def listado_con_balance():
        cursor.execute("USE python_ejercicios")
        cursor.execute("SELECT * FROM progresion")
        milista = cursor.fetchall()
        print("LISTADO CON BALANCE:")
        print("Año".ljust(6), "Población".ljust(15), "Sueldos".ljust(12), "Equipamiento".ljust(15), "Ganancias".ljust(12), "Balance".ljust(12))
        print("-"*72)
        for reg in milista:
                balance = reg[4] - (reg[2] + reg[3])
                print("{:<7}{:<16}{:<13}{:<16}{:<15}{}".format(reg[0], reg[1], reg[2], reg[3], reg[4], balance))
        print("\n")

def listado_agrupado():
        cursor.execute("USE python_ejercicios")
        query = "SELECT poblacion, SUM(sueldos) AS total_sueldos, SUM(equipamiento) AS total_equipamiento, SUM(ganancias) AS total_gaancias FROM progresion GROUP BY poblacion"
        cursor.execute(query)
        milista = cursor.fetchall()
        print("LISTADO GENERAL:")
        print("Población".ljust(15), "Sueldos".ljust(12), "Equipamiento".ljust(15), "Ganancias".ljust(12), "Balance".ljust(12))
        print("-"*66)
        for reg in milista:
                balance = reg[3] - (reg[1] + reg[2])
                print("{:<16}{:<13}{:<16}{:<13}{}".format(reg[0], reg[1], reg[2], reg[3], balance))
        print("\n")

opcion = ""
while opcion != "0":
        opcion = input("Elija una opción del menú:\n" + 
                "1 - Crear tabla\n2 - Rellenar con datos obligatorios\n" + 
                "2 - Rellenar con datos aleatorios\n" +
                "3 - Listado con balance\n4 - Listado agrupado por población\n" +
                "0 - Salir\n")
        if opcion == "1":
                crear_tabla()
        elif opcion == "2":
                rellenar_datos()
        elif opcion == "3":
                listado_con_balance()
        elif opcion == "4":
                listado_agrupado()
print("Ha salido con éxito. Hasta pronto!")

