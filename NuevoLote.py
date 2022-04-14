#file = open("Configuracion.txt","w")
import os
import re

def folder(dirna):
    try:
        os.mkdir(dirna)
        print("El directorio " , dirna ,  " se creo con éxito.") 
    except FileExistsError:
        print("El directorio " , dirna ,  " ya existe.")

def newLote():
    with open('Configuracion.txt', 'r') as f:
            lines = f.read()
            r1 = re.findall(r'Lote#\d',lines)
            r1 = r1[-1]
            r1 = r1.split("#")[1]
            newr1 = int(r1)+1
            numLote = "Lote#"+str(newr1)
            print("Creando Lote#"+str(newr1))

            with open('Configuracion.txt', 'a') as f:
                f.write(""+"\n")
                f.write("\n"+numLote+"\n")
                origen = input("Ingrese el origen: ")
                f.write("Origen="+origen+"\n")
                dirNameori = origen.split("\\")[-1]
                folder(dirNameori)


                desti = input("Ingrese el destino: ")
                f.write("Destino="+desti+"\n")
                dirNamedest = desti.split("\\")[-1]
                folder(dirNamedest)
                
                print("\n"+"Proceso a ejecutar.")
                print("1: Copiar Files.")
                print("2: Mover Files.")

                copMov = int(input("Ingrese la opción a elegir: "))

                typeFiles = input("Ingrese el tipo de files: ")
                if copMov == 1:
                    f.write("CopyFiles="+typeFiles)
                        
                if copMov == 2:
                    f.write("MoveFiles="+typeFiles)

                f.close()