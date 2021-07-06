import xml.etree.ElementTree as ET 
import xml.dom.minidom as md 

arbol = ET.parse("micatalogo.xml")
raiz = arbol.getroot()

def hazlegible(estruc):
    cadenaorig = ET.tostring(estruc, encoding="unicode")
    doc = md.parseString(cadenaorig)
    return doc.toprettyxml()

def listado():
    print("Cantidad catalogada:", len(raiz))
    for etiqueta in raiz:
        print("-" * 10, "\nID Pelicula:", etiqueta.attrib["id"])
        for subetiqueta in etiqueta:
            print(subetiqueta.attrib, subetiqueta.text)
    print("-"*30, "\nEstructura legible:\n", hazlegible(raiz))

def masdatos():
    peli = raiz[0]
    atributos = {"name": "cat", "value": "comedia"}
    tipo = peli.makeelement("tipo", atributos)
    tipo.text = "comedia"
    peli.append(tipo)
    atributos = {}
    reparto = peli.makeelement("reparto", atributos)
    atributos = {"name": "protagonista"}
    actor1 = reparto.makeelement("interprete1", atributos)
    atributos = {}
    actor2 = reparto.makeelement("interprete2", atributos)
    actor3 = reparto.makeelement("interprete3", atributos)
    actor1.text = "Carles Chaplin"
    actor2.text = "Paulette Goddard"
    actor3.text = "Jack Oakie"
    reparto.append(actor1)
    reparto.append(actor2)
    reparto.append(actor3)
    peli.append(reparto)
    arbol.write("micatalogoAmpliado.xml")

def nuevapeli():
    peli = ET.SubElement(raiz, "palicula")
    titulo = ET.SubElement(peli, "titulo")
    director = ET.SubElement(peli, "director")
    tipo = ET.SubElement(peli, "tipo")
    reparto = ET.SubElement(peli, "reparto")
    actor1 = ET.SubElement(reparto, "interprete1")
    actor2 = ET.SubElement(reparto, "interprete2")
    actor3 = ET.SubElement(reparto, "interprete3")

    peli.set("id", "12346")
    titulo.set("name", "ben-hur")
    titulo.text = "William Wyler"
    tipo.set("name", "cat")
    tipo.set("value", "aventuras")
    tipo.text = "aventuras, drama"
    actor1.set("name", "protagonista")
    actor1.text = "Charlton Heston"
    actor2.text = "Jack Hawkins"
    actor3.text = "Stephen Boyd"
    arbol.write("micatalogoAmpliado.xml")

def localizar(id):
    for etiqueta in raiz.iter("pelicula"):
        if etiqueta.get("id") == id:
            print(etiqueta.find("titulo").text, "Película id", id)
            print("Director:", etiqueta.find("director").text)
            print("Tipo:", etiqueta.find("tipo").text)
            for actor in etiqueta.find("reparto"):
                if actor.get("name") == "protagonista":
                    print("Protagonista:", actor.text)

def modificar():
    for etiqueta in raiz.iter("interprete2"):
        etiqueta.set("name", "secundario")
    for elemento in raiz:
        for tipo in elemento.findall("tipo"):
            if tipo.get("value") == "comedia":
                tipo.set("value", "humor, comedia")
                tipo.text = "humor, comedia"
    arbol.write("micatalogoAmpliado.xml")

def eliminar():
    for etiqueta in raiz.iter("titulo"):
        etiqueta.attrib.pop("name")
    for actor in raiz.iter("reparto"):
        actor.remove(actor.find("interprete3"))
    arbol.write("micatalogoAmpliado.xml")

def vaciar():
    raiz.clear()
    arbol.write("micatalogoAmpliado.xml")


masdatos()
nuevapeli()
modificar()
eliminar()
vaciar()
listado()
localizar("12345")