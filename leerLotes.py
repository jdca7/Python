def leer():
    with open('Configuracion.txt', 'r') as f:
        lines = f.read()
        print("\n"+lines+"\n")