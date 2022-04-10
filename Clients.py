'''
Fecha: 19/03/2022
Autor: Josué David Campos Álvarez
Curso: Programación II
Universidad Internacional de las Américas'''

# Función
def clients():
    try:
        # Lee el archivo.
        file = open("Clientes.txt","at")
        while (True):
            #Ingresa los clientes en el archivo.
            file.write(input("Escriba el nombre de un cliente o presione Ctrl + C para salir: ") + "\r")
    
    # Determina si hay un error.
    except OSError as oE:
        
        file.close()
        print(oE.strerror)
    
    # Cierra el file inclusive si hay error o no.
    except BaseException as bE:
        file.close()
        print(bE)