lote = input("Ingrese el número de Lote que quiere borrar: ")

numLote = 'Lote#'+lote

with open('Clientes.txt', 'r') as f:
    file = f.readlines()
    for num, line in enumerate(file):
        if numLote in line:
            file0 = file[0].strip()
            file1 = file[1].strip()
            file2 = file[2].strip()
            file3 = file[3].strip()


with open("Clientes.txt", "w") as f:
    for line in file:
        if line.strip("\n") != file0 and line.strip("\n") != file1 and line.strip("\n") != file2 and line.strip("\n") != file3:
                f.write(line)
