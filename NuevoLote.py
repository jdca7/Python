#Importar modulos
import os
import re

def newLote():
    try:
        #Lee el file
        with open('Configuracion.txt', 'r') as f:
                #Almacena las lineas
                lines = f.read()
                #Busca todas las lineas con Lote
                r1 = re.findall(r'Lote#\d',lines)
                # Selecciona el ultimo lote
                r1 = r1[-1]
                #Divide el ultimo lote para saber cual fue el ultimo digito
                r1 = r1.split("#")[1]
                #Se le suma 1 al ultimo digito
                newr1 = int(r1)+1
                #String del nuevo lote
                numLote = "Lote#"+str(newr1)
                #Imprime el nuevo lote que se va a crear
                print("Creando Lote#"+str(newr1))
                
                #Abre el archivo para anadirle informacion
                with open('Configuracion.txt', 'a') as f:
                    #Escribe un espacio
                    f.write(""+"\n")
                    #Escribe el nuevo lote
                    f.write("\n"+numLote+"\n")
                    #Ingresa el origen
                    origen = input("Ingrese el origen: ")
                    #Escribe el origen
                    f.write("Origen="+origen+"\n")
                    #Divide el origen en \\
                    dirNameori = origen.split("\\")[-1]
                    #Ejecuta la funcion folder
                    folder(dirNameori)

                    #Ingresa el destino
                    desti = input("Ingrese el destino: ")
                    #Escribe el destino
                    f.write("Destino="+desti+"\n")
                    #Divide el destino en \\
                    dirNamedest = desti.split("\\")[-1]
                    #Ejecuta la funcion folder
                    folder(dirNamedest)
                    
                    #Opciones del lote
                    print("\n"+"Proceso a ejecutar.")
                    #Accion de copiar
                    print("1: Copiar Files.")
                    #Accion de mover
                    print("2: Mover Files.")

                    #Ingrese la opcion 1 o 2
                    copMov = int(input("Ingrese la opción a elegir: "))
                    #Ingrese el tipo de files
                    typeFiles = input("Ingrese el tipo de files: ")
                    #Escribe los files a copiar
                    if copMov == 1:
                        f.write("CopyFiles="+typeFiles)
                    
                    #Escribe los files a mover
                    if copMov == 2:
                        f.write("MoveFiles="+typeFiles)

                    #Cierra la lectura del file configuracion
                    f.close()

    # Muestra error en pantalla.
    except ValueError:
        print('\n',"Error.",'\n')

def folder(dirna):
    try:
        #Crea el folder
        os.mkdir(dirna)
        #Mensaje de que el folder fue creado
        print("El directorio " , dirna ,  " se creo con éxito.") 
    except FileExistsError:
        #Mensaje de que el folder ya existe
        print("El directorio " , dirna ,  " ya existe.")