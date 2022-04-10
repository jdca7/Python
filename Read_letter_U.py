'''
Fecha: 19/03/2022
Autor: Josué David Campos Álvarez
Curso: Programación II
Universidad Internacional de las Américas'''

def reading():
    try:
        result = ""
        file = open("Clientes.txt","r")
        for line in file:
            if "u" in line or "U" in line:
                aux = line
                result = result +"\r" + aux
        print(result)
    except OSError as oE:
        file.close()
        print(oE.strerror)
    except BaseException as bE:
        file.close()
        print(bE)