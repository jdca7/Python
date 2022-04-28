def borrarbit():
    try:
        #Abre la bitacora
        with open("Bitacora.log", "r+") as bita:
            #Borra el contenido del file
            bita.truncate(0)
            #Muestra mensaje por pantalla
            print("Se ha borrado la bitacora.")

        # Muestra error en pantalla.
    except ValueError:
        print('\n',"Error.",'\n')
