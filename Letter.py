'''
Fecha: 19/03/2022
Autor: Josué David Campos Álvarez
Curso: Programación II
Universidad Internacional de las Américas'''

# Función
def reading():
    try:
        result = ""
        # Lee el archivo.
        file = open("Clientes.txt","r")
        # Verifica cada uno de los datos.
        for line in file:
            #Determina si contienen u o U.
            if "u" in line or "U" in line:
                #Auxiliar.
                aux = line
                #Almacena todos los datos con u o U.
                result = result +"\r" + aux
        # Imprime el resultado.
        print(result)

        # Verifica si hay un error.
    except OSError as oE:
        file.close()
        print(oE.strerror)

        # Cierra el archivo si hay error o no.
    except BaseException as bE:
        file.close()
        print(bE)