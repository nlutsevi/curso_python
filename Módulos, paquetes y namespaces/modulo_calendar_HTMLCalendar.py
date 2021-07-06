import calendar

año = eval(input("Escriba un año: "))
mes = eval(input("Escriba un mes: "))

calendario = calendar.LocaleHTMLCalendar(locale='')
calendario.cssclasses = ["lun", "mar", "mie", "jue", "vie", "sab", "dom"]
calendario.cssclass_noday = "enblanco"
calendario.cssclass_month = "mes"
calendario.cssclass_year = "anyo"
calendario.cssclass_year_head = "anyo_h"

cal = calendario.formatyearpage(año, 4, 'calendario_estilos.css')
nombre = 'calendario_%s.html' % año
file = open(nombre, 'wb')
file.write(cal)
file.close()
print("Archivo '%s' creado en la misma ubicación que este programa." % nombre)