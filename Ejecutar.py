from datetime import datetime
from datetime import timedelta
import threading
import logging
import os
import shutil
import re

def newTarea():
    with open('Bitacora.log', 'r') as f:
            lines = f.read()
            r1 = re.findall(r'Tarea#\d',lines)
            if not r1:
                now = datetime.now()
                numTarea = "Tarea#1 "+str(now)
                with open('Bitacora.log', 'a') as f:
                    f.write(numTarea+"\n")
            else:
                r1 = r1[-1]
                r1 = r1.split("#")[1]
                newr1 = int(r1)+1
                now = datetime.now()
                numTarea = "Tarea#"+str(newr1)+" "
                numTarea = numTarea+str(now)
                with open('Bitacora.log', 'a') as f:
                    f.write(numTarea+"\n")

            f.close()



def tarea():
    logging.debug("Origen: "+ejec.var_ori)
    logging.debug("Destino: "+ejec.var_des)
    logging.debug("Extensiones: "+ejec.var_type)
    logging.debug("Accion: "+ejec.var_acc)

    if ejec.var_acc == "CopyFiles":
        copyExt1 = ejec.var_type.split(",")
        sourcefiles = os.listdir(ejec.var_ori)
        logging.debug("Files copiados:")
        for Ext in copyExt1:
            for file in sourcefiles:
                if file.endswith(Ext):
                    shutil.copy(os.path.join(ejec.var_ori,file), os.path.join(ejec.var_des,file))
                    logging.debug(file)
        logging.debug("\n")
                 
    if ejec.var_acc == "MoveFiles":
        moveExt1 = ejec.var_type.split(",")
        sourcefiles = os.listdir(ejec.var_ori)
        logging.debug("Files movidos:")
        for Ext in moveExt1:
            for file in sourcefiles:
                if file.endswith(Ext):
                    shutil.move(os.path.join(ejec.var_ori,file), os.path.join(ejec.var_des,file))
                    logging.debug(file)
        logging.debug("\n")  

    

def ejec():
    lote = input("Ingrese el número de Lote que quiere ejecutar: ") 
    secs = int(input("Ingrese la cantidad de segundos: "))
    numLote = 'Lote#'+lote
    newTarea()
    logging.debug('Trabajando en Lote#'+lote)
    logging.debug('Tiempo para Ejecutar: '+str(secs)+" segundos.")

    with open('Configuracion.txt', 'r') as f:
        
        for num, line in enumerate(f, 1):
                if numLote in line:
                    file = f.readlines()
                    ejec.var_ori = file[0].split("=")[1]
                    ejec.var_ori = ejec.var_ori.strip()
                    
                    ejec.var_des = file[1].split("=")[1]
                    ejec.var_des = ejec.var_des.strip()
                    
                    ejec.var_type = file[2].split("=")[1]
                    ejec.var_type = ejec.var_type.strip()
                    
                    ejec.var_acc = file[2].split("=")[0]
                    ejec.var_acc = str(ejec.var_acc.strip())
                    
                    num
                    now = datetime.now()
                    run_at = now + timedelta(seconds=secs)
                    delay = (run_at - now).total_seconds()
                    threading.Timer(delay, tarea).start()


logging.basicConfig(filename='Bitacora.log', format='%(message)s', level=logging.DEBUG)
