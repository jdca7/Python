
import re
with open('Clientes.txt', 'r') as file :
            filedata = file.read()
            print(filedata)

            # Remplaza el objeto
            filedata = re.sub(r'\n\n', '\n', filedata)

            # Escribe el nuevo parametro al file
            with open('Clientes.txt', 'w') as file:
                file.write(filedata)
