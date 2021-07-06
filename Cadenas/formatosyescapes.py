linea="\tPaís\tMoneda\n"
pais=""
while "salir" not in pais:
    pais=input("Nombre del país (escribe \"salir\" para salir): ")
    if "salir" not in pais:
        moneda=input("Moneda para \'" + pais + "\': ")
        linea += "\t" + pais + "\t" + moneda + "\n"
print("\n\nRESULTADOS:\n %s" % linea)

cuentaEuros=linea.lower().count("euro")
cuentaLineas = linea.count("\n")-1
print("Hay %i veces \"euro\", lo cual es un %.2f%% de países" % (cuentaEuros, cuentaEuros/cuentaLineas*100))