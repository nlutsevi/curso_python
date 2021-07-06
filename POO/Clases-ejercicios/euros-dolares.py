from clases.convertidor import convertidor

valor = convertidor(1.37, 220, 350)

print("Establecemos el cambio euro-dolar en", valor.cambio)
print("Indicamos una cantidad impuesta de", valor.eur, "euros")
print(" - Cantidad en euros:", valor.eur)
print(" - Cantidad en dólares:", valor.cantidad_euros(valor.eur))

print("Indicamos una cantidad impuesta de", valor.usd, "dólares")
print(" - Cantidad en euros:", valor.cantidad_dolares(valor.usd))
print(" - Cantidad en dólares:", valor.usd)
