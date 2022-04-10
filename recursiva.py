def recursiva(numero):
    if numero == 0:
        return numero
    else:
        aux = numero
        numero = numero - 1
        return aux + recursiva(numero)

print(recursiva(9))