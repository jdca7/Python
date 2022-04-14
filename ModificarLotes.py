def reemplazo(linea):
    with open('Configuracion.txt', 'r') as f:
        file = f.readlines()
        objeto = file[int(linea)]
        newObjeto = str(objeto.split("=")[1])
        newPara = str(input("Ingrese el nuevo parametro: "))

        with open('Configuracion.txt', 'r') as file :
            filedata = file.read()

            # Remplaza el objeto
            filedata = filedata.replace(newObjeto, newPara+"\n")

            # Escribe el nuevo parametro al file
            with open('Configuracion.txt', 'w') as file:
                file.write(filedata)

            with open('Configuracion.txt', 'r') as f:
                file = f.readlines()
                print("\n")
                print("Nuevo Parametro: ", file[int(linea)])



def modificar ():
    lote = input("Ingrese el número de Lote que quiere modificar: ")
    print("Opciones a modificar"+"\n")


    numLote = 'Lote#'+lote

    with open('Configuracion.txt', 'r') as f:

        for num, line in enumerate(f, 1):
            if numLote in line:
                file = f.readlines()
                print("Opción 1: ",file[0])
                print("Opción 2: ",file[1])
                print("Opción 3: ",file[2])
                num

                numero = int(input("Ingrese la opción a elegir: "))

                if isinstance(numero, int) and numero <= 3 and numero != 0:
                #Opcion 1 función copy.
                    if numero == 1:
                        reemplazo(1)
                    
                    if numero == 2:
                        reemplazo(2)

                    if numero == 3:
                        reemplazo(3)