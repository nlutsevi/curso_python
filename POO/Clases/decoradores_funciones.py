def decorador(mifuncion):
    def marco(*parametros, **keywords):
        print("\n", "\\"*30)
        mifuncion(*parametros, **keywords)
        print("/"*30, "\n")
    return marco

def decorardatos(extendido=False):
    def principal(funcion):
        def comprueba(*argumentos):
            funcion(*argumentos)
            if extendido:
                texto = ""
                for aficion in argumentos[2:]:
                    texto += aficion + ", "
                print("Mis aficiones son:", texto.rstrip(", "))
        return comprueba
    return principal 

@decorador
@decorardatos(True)
def presentacion(*args):
    print("Me llamo %s y vivo en %s" %  (args[0], args[1]))

@decorador
def mensaje():
    print("Bienvenidos a mi programa!")

@decorador
def despedida(texto):
    print(texto)

mensaje()
presentacion("Jose", "Barcelona", "senderismo", "espeleología", "submarinísmo")
despedida("Hasta pronto, un saludo!")