def leerBita():
    try:
        #Lee la bitacora
        with open('Bitacora.log', 'r') as f:
            #Almacena la lectura en lines
            lines = f.read()
            #Muestra las lectura
            print("\n"+lines+"\n")
    
    # Muestra error en pantalla.
    except ValueError:
        print('\n',"Error.",'\n')