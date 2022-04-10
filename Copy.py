'''
Fecha: 30/03/2022
Autor: Josué David Campos Álvarez
Curso: Programación II
Universidad Internacional de las Américas'''

import os, shutil

def copy():
    with open('Configuracion.txt', 'r') as f:
        lines = f.read()

    for line in lines.splitlines():
        if "Origen" in line:
            source = line.split("=")[1]

        if "CopyFiles" in line:
                copyExt = line.split("=")[1]
                copyExt1 = copyExt.split(",")
        
        if "Destino" in line:
            destination = line.split("=")[1]

    
    sourcefiles = os.listdir(source)
    for Ext in copyExt1:
        for file in sourcefiles:
            if file.endswith(Ext):
                shutil.copy(os.path.join(source,file), os.path.join(destination,file))
    print("Files copiados exitosamente."+"\n")

