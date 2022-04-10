'''
Fecha: 24/02/2022
Autor: Josué David Campos Álvarez
Curso: Programación II
Universidad Internacional de las Américas'''

def digito(numero):
    return numero

def normal(sumar):
    for i in range(0,sumar):
        i = sum(range(0,sumar+1))
    return print("\n","La suma total es: ",i,"\n")

def recursiva(sumar):
    if sumar == 0:
        return sumar
    else:
        aux = sumar
        sumar = sumar - 1
        total = aux + recursiva(sumar)
        return total






