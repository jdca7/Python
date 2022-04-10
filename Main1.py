'''
Fecha: 19/03/2022
Autor: Josué David Campos Álvarez
Curso: Programación II
Universidad Internacional de las Américas'''

#Importa las clases
import Clients
import Read
import Letter

# Loop Infinito
while (True):

    try:
        # Opciones.
        print("Opción 1: Ingresar Clientes.")
        print("Opción 2: Mostrar todos los clientes.")
        print("Opción 3: Mostrar los clientes con la letra u.")
        print("Opción 4: Salir del programa."+"\n")

        num = int(input("Ingrese la opción a elegir: "))

        # Determina si la variable num es interger menor a 5 y diferente de 0.
        if isinstance(num, int) and num < 5 and num != 0:
            #Opcion 1 función clients.
            if num == 1:
                Clients.clients()
            #Opcion 2 función readFile.
            if num == 2:
                Read.readFile()
            #Opcion 3 función reading.
            if num == 3:
                Letter.reading()
            #Opcion 4 salir del programa.
            if num == 4:
                break
        
    # Muestra error en pantalla.
    except ValueError:
        print('\n',"Opción invalida.",'\n')
