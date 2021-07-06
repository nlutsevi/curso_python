import sqlite3

conex = sqlite3.connect('productos.sqlite')
cursor = conex.cursor()

def creacion():
    cursor.execute("CREATE TABLE listado (" +
    "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, " +
    "nombre TEXT NOT NULL, " +
    "proveedor TEXT NOT NULL, " + 
    "precio REAL, " +
    "stock INTEGER DEFAULT 0)")

def insertar():
    nomb = input("Nombre del productto: ")
    prov = input("Proveedor: ")
    prc = input("Precio: ")
    cursor.execute("INSERT INTO listado(nombre, proveedor, precio) " +
    "VALUES (?, ?, ?)", (nomb, prov, prc))
    conex.commit()

def listado1():
    cursor.execute("SELECT * FROM listado")
    milista = cursor.fetchall()
    print("LISTADO GENERAL")
    for reg in milista:
        print('{0} : {1}, de {2}, precio {3}€'.format(reg[0], reg[1], reg[2], reg[3]))

def listado2():
    miid = input("Num de identificacion: ")
    cursor.execute("SELECT * FROM listado WHERE id=?", miid)
    reg = cursor.fetchone()
    if reg is None:
        print("Num no localizado")
    else:
        print('{0} : {1}, de {2}, precio {3}€'.format(reg[0], reg[1], reg[2], reg[3]))

def insertarmultiple():
    productos = [("Bicicleta Indoor S1 Spin Bike", "Reebok", "799,3"),
    ("Bicicleta Indoor Spada Magnetic", "BH Fitness", "850,55"),
    ("Bicicleta elíptica Cross M", "Reebok", "549,82")]
    cursor.executemany("INSERT INTO listado(nombre, proveedor, precio) " +
    "VALUES(?, ?, ?)", productos)
    conex.commit()

def actualizastock():
    cursor.execute("SELECT nombre FROM listado")
    listanombres = cursor.fetchall()
    for nom in listanombres:
        cantidad = input("Stock de " + nom[0] + " (-1 para salir): ")
        if cantidad == "-1":
            break
        else:
            cursor.execute("UPDATE listado SET stock = ? WHERE nombre = ?", 
            (eval(cantidad), nom[0]))
    conex.commit()
    print("Fin de la actualización")

def transaccion():
    print("Actualizamos todos los precios a 2000\n")
    conex.execute("UPDATE listado SET precio = 2000")
    listado1()
    print("\nDeshacemos la transacción\n")
    conex.rollback()
    listado1()

# creacion()
# insertar()
# listado1()
# listado2()
# insertarmultiple()
# actualizastock()
transaccion()
cursor.close()