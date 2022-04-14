import re

def borrar():
    lote = input("Ingrese el número de Lote que quiere borrar: ")

    numLote = 'Lote#'+lote

    with open('Configuracion.txt', 'r') as f:
        length = f.readlines()

    with open('Configuracion.txt', 'r') as f:
        for num, line in enumerate(f, 1):
            if numLote in line:
                file = f.readlines()
                file1 = file[0].strip()
                print(file1)
                file2 = file[1].strip()
                print(file2)
                file3 = file[2].strip()
                print(file3)
                num


    with open("Configuracion.txt", "w") as f:
        for line in length:
            if line.strip("\n") != numLote and line.strip("\n") != file1 and line.strip("\n") != file2 and line.strip("\n") != file3:
                    f.write(line)
