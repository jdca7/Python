def borrar():
    #Ingresar lote ha borrar
    lote = input("Ingrese el número de Lote que quiere borrar: ")

    #Almacena número de lote
    numLote = 'Lote#'+lote

    #Abre el file para lectura
    with open('Configuracion.txt', 'r') as f:
        #Almacena las lineas del file
        length = f.readlines()

    #Abre el file para lectura
    with open('Configuracion.txt', 'r') as f:
        # Enumera las lineas
        for num, line in enumerate(f, 1):
            #Si el número de lote en la linea
            if numLote in line:
                #Almacene las lineas
                file = f.readlines()

                # Almacene la primer linea sin espacios
                file1 = file[0].strip()
                #Imprime la linea
                print(file1)

                # Almacene la segunda linea sin espacios
                file2 = file[1].strip()
                #Imprime la linea
                print(file2)

                # Almacene la segunda linea sin espacios
                file3 = file[2].strip()
                #Imprime la linea
                print(file3)
                #Numero
                num

    #Abre el file para escritura
    with open("Configuracion.txt", "w") as f:
        #Para cada linea
        for line in length:
            #Si la linea no es parte del lote
            if line.strip("\n") != numLote and line.strip("\n") != file1 and line.strip("\n") != file2 and line.strip("\n") != file3:
                #Vuelve a escribir la linea
                f.write(line)
        # Espacio
        f.write("\n")