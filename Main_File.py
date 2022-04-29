#Importa las clases
import LeerLotes
import ModificarLotes
import NuevoLote
import Ejecutar
import leerBitacora 
import borrarLote
import BorrarBitacora

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
        print("Opción 7: Borrar Bitacora.")
        print("Opción 8: Salir del programa."+"\n")

        # Opción elegida
        num = int(input("Ingrese la opción a elegir: "))

        # Determina si la variable num es interger menor a 10 y diferente de 0.
        if isinstance(num, int) and num <= 10 and num != 0:
            #Opcion 1 función para leer lotes.
            if num == 1:
                LeerLotes.leer()

            #Opcion 2 función para modificar lotes.
            if num == 2:
                ModificarLotes.modificar()

            #Opcion 3 función para crear un lote.
            if num == 3:
                NuevoLote.newLote()

            #Opcion 4 función para mover o copiar.
            if num == 4:
                Ejecutar.ejec()

            #Opcion 5 función para leer la bitacora.
            if num == 5:
                leerBitacora.leerBita()

            #Opcion 6 función para borrar lotes.
            if num == 6:
                borrarLote.borrar()

            #Opcion 7 función para borrar bitacora.
            if num == 7:
                BorrarBitacora.borrarbit()
                
            #Opcion 8 función para salir.
            if num == 8:
                break

    # Muestra error en pantalla.
    except ValueError:
        print('\n',"Opción invalida.",'\n')