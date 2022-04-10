#import os, shutil

def leerLotes():
    with open('Configuracion.txt', 'r') as f:
        lines = f.read()
        print(lines)

#def modificarLotes():
file = open("Configuracion.txt","w")
file.write(input() + "\r")
file.close()