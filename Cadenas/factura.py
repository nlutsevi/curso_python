count = 0

articulo1 = input("Dime el nombre del primer artículo: ")
precio1 = input("Dime el precio de %s: " % articulo1)
articulo2 = input("Dime el nombre del segundo artículo: ")
precio2 = input("Dime el precio de %s: " % articulo2)
articulo3 = input("Dime el nombre del tercer artículo: ")
precio3 = input("Dime el precio de %s: " % articulo3)

price1 = float(precio1)
format_price1 = "{:.2f}".format(price1)
price2 = float(precio2)
format_price2 = "{:.2f}".format(price2)
price3 = float(precio3)
format_price3 = "{:.2f}".format(price3)

print("Primer artículo: %s" % articulo1)
print("Precio: %s" % format_price1)
print("Segundo artículo: %s" % articulo2)
print("Precio: %s" % format_price2)
print("Tercer artículo: %s" % articulo3)
print("Precio: %s" % format_price3 + "\n\n")

print("factura".upper().center(80, "-"))
 
print(articulo1.title().ljust(73, ".") + "%s" % format_price1.zfill(6) + "€")
print(articulo2.title().ljust(73, ".") + "%s" % format_price2.zfill(6) + "€")
print(articulo3.title().ljust(73, ".") + "%s" % format_price3.zfill(6) + "€")
print("-".center(80, "-"))

total = float(precio1) + float(precio2) + float(precio3)
format_total = "{:.2f}".format(total)
iva = total * 21/100
format_iva = "{:.2f}".format(iva)
neto = total + iva
format_neto = "{:.2f}".format(neto)
print(("Precio base: %s" % format_total.zfill(6) + "€").rjust(80))
print(("IVA: %s" % format_iva.zfill(6) + "€").rjust(80))
print(("TOTAL A PAGAR: %s" % format_neto.zfill(6) + "€").rjust(80))

