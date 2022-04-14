#Importa las clases
import LeerLotes
import ModificarLotes
import NuevoLote
import Ejecutar
import leerBitacora 
import borrarLote

# Loop Infinito
while (True):

    try:
        # Opciones.
        print("\n"+"Menú")
        print("Opción 1: Leer Lotes.")
        print("Opción 2: Modificar Lotes.")
        print("Opción 3: Crear un nuevo lote.")
        print("Opción 4: Copiar o Mover Files.")
        print("Opción 5: Leer Bitacora.")
        print("Opción 6: Borrar Lote.")
        print("Opción 7: Salir del programa."+"\n")

        num = int(input("Ingrese la opción a elegir: "))

        # Determina si la variable num es interger menor a 5 y diferente de 0.
        if isinstance(num, int) and num <= 10 and num != 0:
            #Opcion 1 función copy.
            if num == 1:
                LeerLotes.leer()
            #Opcion 2 función move.
            if num == 2:
                ModificarLotes.modificar()
            #Opcion 3 salir del programa.
            if num == 3:
                NuevoLote.newLote()
            if num == 4:
                Ejecutar.ejec()
            if num == 5:
                leerBitacora.leerBita()
            if num == 6:
                borrarLote.borrar()
            if num == 7:
                break

    # Muestra error en pantalla.
    except ValueError:
        print('\n',"Opción invalida.",'\n')