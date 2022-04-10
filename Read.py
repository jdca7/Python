'''
Fecha: 19/03/2022
Autor: Josué David Campos Álvarez
Curso: Programación II
Universidad Internacional de las Américas'''

# Función
def readFile():
    try:
        # Lee el archivo.
        file = open("Clientes.txt","r")

        # Imprime los datos.
        print(file.read())
    
    # Determina si hay error.
    except OSError as oE:
        file.close()
        print(oE.strerror)
    
    # Cierra el archivo si hay error o no.
    except BaseException as bE:
        file.close()
        print(bE)