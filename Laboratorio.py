while (True):
    try:
        #Opciones de menu
        print("Opción 1: Calcular su salario.")
        print("Opción 2: Mostrar su nombre de usuario.")
        print("Opción 3: Determinar si es mayor de edad.")
        print("Opción 4: Presentar todos los numeros impares.")
        print("Opción 5: Terminar el programa.",'\n')
        num = int(input("Ingrese su opción: "))

        # Determina si el numero es mayor que 5 ó 0
        if num > 5 or num == 0:
            print('\n'+"Opción invalida.")
            print("Intente nuevamente una opción entre 1 y 5.",'\n')

        #Calculo de la paga
        if num == 1:
            def paga(horas, costo):
                return horas * costo

            horas = float(input('Número de horas laboradas: '))
            costo = float(input('Costo por hora: '))
            total = paga(horas, costo)
            print("La paga total es de: ", total, " colones.",'\n')


        if num == 2:
            nombre = input("Ingrese su nombre de usuario: ")
            mensaje = '''Bienvenido a la UIA {0}\nBienvenido a la UIA {1}\n'''
            print(mensaje.format(nombre.upper(), nombre.lower()))
            
        
        if num == 3:
            edad = int(input("Introduzca su edad: "))
            print()
            def adulto(edad):
                if edad > 17:
                   return print("Usted es mayor de edad"+'\n')
                return print("Usted es menor de edad"+'\n')
            adulto(edad)
        

        if num == 4:
            n = int(input("Introduzca un número para encontrar todos los impares menores: "))
            def dig(n):
                texto = ''      
                for i in range(1,n):  
                    if i%2!=0:  
                        texto+=str(i)+', ' 
                i += 1  
                return print(texto[:-2],'\n')
            dig(n)
        
        
        if num == 5:
            break

    except ValueError:
        print('\n',"Opción invalida.")
        continue

    
    
 
