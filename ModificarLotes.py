def modificar ():
    try:
        #Ingresar el lote que se quiere modificar.
        lote = input("Ingrese el número de Lote que quiere modificar: ")
        #Muestra en consola el mensaje
        print("Opciones a modificar"+"\n")

        #Variable para saber el número de lote.
        numLote = 'Lote#'+lote

        #Leer file
        with open('Configuracion.txt', 'r') as f:
            #Hace un recorrido en cada linea
            for num, line in enumerate(f, 1):
                #Hace un if para saber si el lote esta en la linea
                if numLote in line:
                    #Almacena las lineas en file
                    file = f.readlines()
                    #Muestra las opciones
                    print("Opción 1: ",file[0])
                    print("Opción 2: ",file[1])
                    print("Opción 3: ",file[2])
                    num

                    #Numero de opción a elegir.
                    numero = int(input("Ingrese la opción a elegir: "))
                    
                    # If para saber si la opción escogida es un número y es igual o menor a 3
                    if isinstance(numero, int) and numero <= 3 and numero != 0:
                    #Reemplaza los parametros en la opción 1
                        if numero == 1:
                            reemplazo(1)
                    #Reemplaza los parametros en la opción 2
                        if numero == 2:
                            reemplazo(2)
                    #Reemplaza los parametros en la opción 3
                        if numero == 3:
                            reemplazo(3)

    # Muestra error en pantalla.
    except ValueError:
        print('\n',"Error.",'\n')

def reemplazo(linea):
    try:
        # Lee el file configuracion.
        with open('Configuracion.txt', 'r') as f:
            # Almacena las lineas en la variable file.
            file = f.readlines()
            # Almacena la linea correspondiente al número ingresado
            objeto = file[int(linea)]
            #Hace una división en =
            newObjeto = str(objeto.split("=")[1])
            #Ingresar el nuevo parametro.
            newPara = str(input("Ingrese el nuevo parametro: "))

            # Lee el file configuracion.
            with open('Configuracion.txt', 'r') as file :
                filedata = file.read()

                # Remplaza el objeto
                filedata = filedata.replace(newObjeto, newPara+"\n")

                # Escribe el nuevo parametro al file
                with open('Configuracion.txt', 'w') as file:
                    file.write(filedata)

                # Lee el file configuracion.
                with open('Configuracion.txt', 'r') as f:
                    #Muestra en consola el nuevo parametro.
                    file = f.readlines()
                    print("\n")
                    print("Nuevo Parametro: ", file[int(linea)])

    # Muestra error en pantalla.
    except ValueError:
        print('\n',"Error.",'\n')