'''
Fecha: 30/03/2022
Autor: Josué David Campos Álvarez
Curso: Programación II
Universidad Internacional de las Américas'''

import os, shutil

def move():
    with open('Configuracion.txt', 'r') as f:
        lines = f.read()

    for line in lines.splitlines():
        if "Origen" in line:
            source = line.split("=")[1]

        if "MoveFiles" in line:
            move = line.split("=")[1]
        
        if "Destino" in line:
            destination = line.split("=")[1]

    
    sourcefiles = os.listdir(source)
    for file in sourcefiles:
        if file.endswith(move):
            shutil.move(os.path.join(source,file), os.path.join(destination,file))
    
    print("Files movidos exitosamente."+"\n")
