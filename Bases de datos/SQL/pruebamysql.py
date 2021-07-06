import mysql.connector

conex = mysql.connector.connect(user="root", password="", host="localhost")
cursor = conex.cursor()

def creacion():
    cursor.execute("CREATE DATABASE python")
    cursor.execute("USE python")

    cursor.execute("CREATE TABLE usuario (" +
    "id INTEGER PRIMARY KEY UNIQUE NOT NULL, " +
    "nombre TEXT, fecha_registro DATE)")

    cursor.execute("CREATE TABLE webs (" +
    "idusuario INTEGER, web TEXT, descripcion TEXT, " +
    "FOREIGN KEY(idusuario) REFERENCES usuario(id))")

def insercion():
    cursor.execute("USE python")
    cursor.execute("insert into USUARIO (id, nombre, fecha_registro) " +
    " VALUES(%s, %s, %s)", (140, "Jorge Ibarra", "2019-10-20"))
    cursor.execute("INSERT INTO usuario (id, nombre, fecha_registro) " +
    " VALUES(%s, %s, %s)", (150, "Irene Vaquero", "2020-05-15"))
    conex.commit()
    print("2 usuarios agregados")
    colecction = [(140, "www.msn.com", "Informacion general"),
    (140, "www.android.com", "Página oficial Android"),
    (150, "www.recetasdiarias.com", "Recetas de cocina"),
    (150, "www.dciencia.es", "Blog Mundo científico"),
    (140, "www.xataka.com", "Blog sobre tecnología")]
    cursor.executemany("INSERT INTO webs (idusuario, web, descripcion) " +
    " VALUES(%s, %s, %s)", colecction)
    conex.commit()
    print("Varias webs agregadas")
    
def listado():
    cursor.execute("USE python")
    cursor.execute("SELECT u.id, u.nombre, w.web, w.descripcion " +
    "FROM usuario u, webs w " +
    "WHERE u.id=w.idusuario")
    milista = cursor.fetchall()
    for reg in milista:
        print("Socio {0}: {1}, {2} ({3})".format(reg[0], reg[1], reg[2], reg[3]))

# creacion()
# insercion()
listado()