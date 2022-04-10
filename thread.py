import logging
import threading
import time

#Este metodo se ejecutara a traves de un hilo de ejecución 
#a parte del hilo de ejecución principal
def MetodoA(name): 
    logging.info("Thread %s: Iniciando hilo#1....", name)
    time.sleep(10)
    logging.info("Thread %s: Finalizando hilo#1....", name)

def MetodoB(name): 
    logging.info("Thread %s: Iniciando hilo#2....", name)
    time.sleep(5)
    logging.info("Thread %s: Finalizando hilo#2....", name)

if __name__ == "__main__":  #main es el hilo de ejecución principal
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Hilo Principal(Main): antes de crear hilo#1 (thread)")
    x = threading.Thread(target=MetodoA, args=(60,)) #Apenas se creo el hilo que encapsula el MetodoA
    logging.info("Hilo Principal(Main): antes de iniciar hilo#1 (thread)")
    x.start() 
    logging.info("Hilo Principal(Main): esperar a que hilo#1 termine")
    #x.join() #Hacer que hilo#1 retorne al flujo de ejecución pricipal
    logging.info("Hilo Principal(Main): termino")
    


    logging.info("Hilo Principal(Main): antes de crear hilo#2 (thread)")
    x = threading.Thread(target=MetodoB, args=(30,)) #Apenas se creo el hilo que encapsula el MetodoA
    logging.info("Hilo Principal(Main): antes de iniciar hilo#2 (thread)")
    x.start() 
    logging.info("Hilo Principal(Main): esperar a que hilo#2 termine")
    #x.join() #Hacer que hilo#1 retorne al flujo de ejecución pricipal
    logging.info("Hilo Principal(Main): termino")
    #input()