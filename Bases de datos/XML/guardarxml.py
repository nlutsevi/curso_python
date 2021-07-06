import xml.etree.ElementTree as ET
import xml.dom.minidom as md

def hazlegible(estruc):
    cadenaorig = ET.tostring(estruc, encoding="unicode")
    doc = md.parseString(cadenaorig)
    return doc.toprettyxml()

principal = ET.Element("catalogo")
comentario = ET.Comment("Classic Movies")
principal.append(comentario)

peli = ET.SubElement(principal, "pelicula")
titulo = ET.SubElement(peli, "titulo")
director = ET.SubElement(peli, "director")

peli.set("id", "12345")
titulo.set("name", "dictador")
titulo.text = "El Gran Dictador"
director.text = "Charles Chaplin"

datos = ET.tostring(principal, encoding="unicode")
archivo = open("micatalogo.xml", "w")
archivo.write(datos)
archivo.close()
print("Estructura formada:\n", datos)

datos = hazlegible(principal)
archivo = open("micatalogoLegible.xml", "w")
archivo.write(datos)
archivo.close()
print("Estructura legible formada:\n", datos)