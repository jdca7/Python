'''
Fecha: 24/02/2022
Autor: Josué David Campos Álvarez
Curso: Programación II
Universidad Internacional de las Américas'''

# Importa Calculo.py
import Calculo

# Loop infinito
while (True):
    # Test de codigo
    try:
        # Opciones de menu
        print("Opción 1: Función Normal.")
        print("Opción 2: Función Recursiva.","\n")
        
        # Variable que almacena la opción escogida
        num = int(input("Ingrese la opción a elegir: "))

        # Determina si la variable num es interger menor a 3 y diferente de 0
        if isinstance(num, int) and num < 3 and num != 0:

            # Variable que almacena el numero en el cual termina la suma
            resultado = Calculo.digito(int(input("Introduzca un número a sumar: ")))

            # Opción 1 para calcular usando el metodo normal
            if num == 1:
                Calculo.normal(resultado)

            #Opción 2 para calcular usando el metodo recursivo
            if num == 2:
                print("\n","La suma total es: ", Calculo.recursiva(resultado) ,"\n")
        
        #Solicita ingresar un numero entre 1 y 2
        else:
            print("\n","Ingrese una opción entre 1 y 2","\n")

    # Muestra error en pantalla
    except ValueError:
        print('\n',"Opción invalida.",'\n')
        continue
            

