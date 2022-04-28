#Importar modulos
from datetime import datetime
from datetime import timedelta
import threading
import logging
import os
import shutil
import re
    

def ejec():
    try:  
        # Ingresar el lote ha ejecutar
        lote = input("Ingrese el número de Lote que quiere ejecutar: ") 
        #Cantidad de segundos a esperar
        secs = int(input("Ingrese la cantidad de segundos: "))
        #Número de lote
        numLote = 'Lote#'+lote
        #Ejecuta la función newTarea
        newTarea()
        # Escribe en bitacora
        logging.debug('Trabajando en Lote#'+lote)
        # Escribe en bitacora
        logging.debug('Tiempo para Ejecutar: '+str(secs)+" segundos.")

        # Leer el configuracion.txt
        with open('Configuracion.txt', 'r') as f:
            
            # Recorrer cada linea y enumerarla
            for num, line in enumerate(f, 1):
                    #Hace un recorrido en cada linea
                    if numLote in line:
                        #Lee las lineas del file
                        file = f.readlines()

                        #Divide y almacena la ultima fraccion de la variable de origen en la funciona ejec
                        ejec.var_ori = file[0].split("=")[1]
                        # Elimina los espacios en blanco
                        ejec.var_ori = ejec.var_ori.strip()
                        
                        #Divide y almacena la ultima fraccion de la variable de destino en la funciona ejec
                        ejec.var_des = file[1].split("=")[1]
                        # Elimina los espacios en blanco
                        ejec.var_des = ejec.var_des.strip()
                        
                        #Divide y almacena la ultima fraccion de la variable de type en la funciona ejec
                        ejec.var_type = file[2].split("=")[1]
                        # Elimina los espacios en blanco
                        ejec.var_type = ejec.var_type.strip()
                        
                        #Divide y almacena la ultima fraccion de la variable de accion en la funciona ejec
                        ejec.var_acc = file[2].split("=")[0]
                        # Elimina los espacios en blanco y almacena un str
                        ejec.var_acc = str(ejec.var_acc.strip())
                        
                        #Numero
                        num
                        # La hora en este momento
                        now = datetime.now()
                        # La hora actual mas los segundos que agregamos
                        run_at = now + timedelta(seconds=secs)
                        #Total de tiempo de espera
                        delay = (run_at - now).total_seconds()
                        # Hace el proces de multi thread con los segundos a esperar y la tarea a ejecutar
                        time = threading.Timer(delay, tarea)
                        # Inicia la ejecucion
                        time.start()

    # Muestra error en pantalla.
    except ValueError:
        print('\n',"Error.",'\n')
                    
# Configuracion de formato, file a escribir para bitacora y el nivel
logging.basicConfig(filename='Bitacora.log', format='%(message)s', level=logging.DEBUG)

def newTarea():
    try:
        # Lee la bitacora
        with open('Bitacora.log', 'r') as f:
                # Almacena las lineas en lines
                lines = f.read()
                # Encuentra la palabra tarea
                r1 = re.findall(r'Tarea#\d',lines)
                # Hace un if para ver si la palabra tarea existe
                if not r1:
                    # Almacena la fecha
                    now = datetime.now()
                    #Almacena la Tarea#1 y la fecha como string
                    numTarea = "Tarea#1 "+str(now)

                    # Abre la bitacora para agregar contenido
                    with open('Bitacora.log', 'a') as f:
                        # Escribe la Tarea#1 en la bitacora
                        f.write(numTarea+"\n")
                # En caso de que tarea si exista hace un else
                else:
                    #Obtiene la parte donde dice Tarea
                    r1 = r1[-1]
                    #Separa Tarea#1 y selecciona el número
                    r1 = r1.split("#")[1]
                    # Le suma 1 a el número anterior
                    newr1 = int(r1)+1
                    # Almacena la fecha
                    now = datetime.now()
                    # El tarea más el nuevo número
                    numTarea = "Tarea#"+str(newr1)+" "
                    #Agrega la fecha
                    numTarea = numTarea+str(now)

                    # Abre la bitacora para agregar contenido
                    with open('Bitacora.log', 'a') as f:
                        # Escribe la Tarea#X en la bitacora
                        f.write(numTarea+"\n")
                # Cierra la bitacora
                f.close()       

    # Muestra error en pantalla.
    except ValueError:
        print('\n',"Error.",'\n')            

def tarea():
    try:
        # Escribe en bitacora el origen
        logging.debug("Origen: "+ejec.var_ori)
        # Escribe en bitacora el destino
        logging.debug("Destino: "+ejec.var_des)
        # Escribe en bitacora el tipo de files
        logging.debug("Extensiones: "+ejec.var_type)
        # Escribe en bitacora la acción a realizar
        logging.debug("Accion: "+ejec.var_acc)

        # Si la variable contiene CopyFiles entonces ejecute el proceso de copiado
        if ejec.var_acc == "CopyFiles":
            #Almacena los tipos de files
            copyExt1 = ejec.var_type.split(",")
            #Almacena los diferentes nombres de files en el origen
            sourcefiles = os.listdir(ejec.var_ori)
            # Escribe en bitacora
            logging.debug("Files copiados:")
            # Por cada uno de las extensiones o tipos de file
            for Ext in copyExt1:
                # Por cada uno de los files en el origen
                for file in sourcefiles:
                    # Si el file termina en alguna de las extensiones
                    if file.endswith(Ext):
                        #Copie el file del origen al destino
                        shutil.copy(os.path.join(ejec.var_ori,file), os.path.join(ejec.var_des,file))
                        # Agregue el file a la bitacora
                        logging.debug(file)
            #Agregue un espacio
            logging.debug("\n")
        
        # Si la variable contiene CopyFiles entonces ejecute el proceso de mover
        if ejec.var_acc == "MoveFiles":
            #Almacena los tipos de files
            moveExt1 = ejec.var_type.split(",")
            #Almacena los diferentes nombres de files en el origen
            sourcefiles = os.listdir(ejec.var_ori)
            # Escribe en bitacora
            logging.debug("Files movidos:")
            # Por cada uno de las extensiones o tipos de file
            for Ext in moveExt1:
                # Por cada uno de los files en el origen
                for file in sourcefiles:
                    # Si el file termina en alguna de las extensiones
                    if file.endswith(Ext):
                        #Copie el file del origen al destino
                        shutil.move(os.path.join(ejec.var_ori,file), os.path.join(ejec.var_des,file))
                        # Agrega el file a la bitacora
                        logging.debug(file)
            #Agrega un espacio
            logging.debug("\n")
    
    # Muestra error en pantalla.
    except ValueError:
        print('\n',"Error.",'\n')