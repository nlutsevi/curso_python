nombre = "Señora Alfredo Villar"
print("Nombre original: " + nombre)

nombre = nombre.replace("Señora", "Señor")
print("Género cambiado: " + nombre)

nombre = nombre.lstrip("Señor ")
print("Sin formalismos: " + nombre)

print("\nCambio de texto dinámico:")
cadena = "bienvenido a mi programa {0}"
print("\nOriginal: " + cadena)
print("Formateado: " + cadena.format("En Python"))

cadena = "Importe bruto: {0}€ + IVA: {1}€ = Importe neto: {2}€"
print("\nOriginal: " + cadena)
print("Formateado: ", cadena.format(100, 21, 121))

cadena = "Importe bruto: {bruto}€ + IVA: {iva}€ = importe neto: {neto}€"
print("\nOriginal: " + cadena)
print("Formateado: " + cadena.format(iva=21, neto=121, bruto=100))