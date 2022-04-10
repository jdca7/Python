'''
Fecha: 10/04/2022
Autor: Josué David Campos Álvarez
Curso: Programación II
Universidad Internacional de las Américas
Laboratorio: #7'''

# Importar modulos.
import logging
import random, string
import threading

# Funcion para escribir el archivo.
def EscribirArchivo():
    logging.info("Iniciando Escritura....") # Especifica cuando ha iniciado la escritura.
    try:
        archivo = open("Datos.txt",'at')
        contador = 1
        while (contador <= 10000): #Ctrl+C
            datoEscribir = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(50))
            archivo.write(datoEscribir+"\r") 
            contador += 1; 
        
    except OSError as oE:
        archivo.close()
        print(oE.strerror)
    except BaseException as bE:
        archivo.close()
        print(bE)
    logging.info("Finalizando escritura....") # Especifica cuando ha finalizado la escritura.

# Funcion para leer el archivo.
def LecturaArchivo():
    logging.info("Iniciando Lectura....") # Especifica cuando ha iniciado la lectura.
    try:   
        archivo = open("Datos.txt",'rt')
        lines = 1
        while (lines <= 10000):            
            lineas = archivo.readlines()
            for x in lineas:
                print(x)
                lines += 1
    except OSError as oE:
        archivo.close()
        print(oE.strerror)
    except BaseException as bE:
        archivo.close()
        print(bE)
    logging.info("Finalizando Lectura....") # Especifica cuando ha finalizado la lectura.

if __name__ == "__main__": 
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    
    logging.info("Antes de crear escritura") # Especifica cuando se crea el thread de escritura.
    t = threading.Thread(target=EscribirArchivo) # Thread de escritura.
    logging.info("Antes de iniciar escritura") # Especifica cuando se va a iniciar la escritura.
    t.start() # Iniciar thread de escritura.


    logging.info("Antes de crear lectura") # Especifica cuando se crea el thread de lectura.
    c = threading.Thread(target=LecturaArchivo) # Thread de lectura.
    logging.info("Antes de iniciar lectura") # Especifica cuando se va a iniciar la lectura.
    c.start() # Iniciar thread de lectura.
    c.join() # Esperar a que finalice el thread de lectura.