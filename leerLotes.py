def leer():
    try:
        # Lee el file configuracion.
        with open('Configuracion.txt', 'r') as f:
            #Almacena la lectura en la variable lines.
            lines = f.read()
            #Muestra en pantalla las lineas del file configuracion.
            print("\n"+lines+"\n")
    
    # Muestra error en pantalla.
    except ValueError:
        print('\n',"Error.",'\n')