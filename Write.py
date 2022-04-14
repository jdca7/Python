'''
Fecha: 19/03/2022
Autor: Josué David Campos Álvarez
Curso: Programación II
Universidad Internacional de las Américas'''

def clients():
        
        file = open("Clientes.txt","w")
        file.write(input() + "\r")
        file.close()


clients()
