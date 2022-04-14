def leerBita():
    with open('Bitacora.log', 'r') as f:
        lines = f.read()
        print("\n"+lines+"\n")