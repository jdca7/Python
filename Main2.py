'''
Fecha: 30/03/2022
Autor: Josué David Campos Álvarez
Curso: Programación II
Universidad Internacional de las Américas'''

#Importa las clases
import Copy
import Move

# Loop Infinito
while (True):

    try:
        # Opciones.
        print("Opción 1: Copiar files.")
        print("Opción 2: Mover files.")
        print("Opción 3: Salir del programa."+"\n")

        num = int(input("Ingrese la opción a elegir: "))

        # Determina si la variable num es interger menor a 5 y diferente de 0.
        if isinstance(num, int) and num <= 3 and num != 0:
            #Opcion 1 función copy.
            if num == 1:
                Copy.copy()
            #Opcion 2 función move.
            if num == 2:
                Move.move()
            #Opcion 3 salir del programa.
            if num == 3:
                break

    # Muestra error en pantalla.
    except ValueError:
        print('\n',"Opción invalida.",'\n')
