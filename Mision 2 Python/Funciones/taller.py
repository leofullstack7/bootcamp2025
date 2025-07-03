def mostrarmenu():
    menu = int(input('******** MENU ********** \n \n'
    '1. Calcular el producto de todos los elementos de una lista de n posiciones.\n \n' 
    '2. Calcular la suma de todos los elementos de una lista de n posiciones.\n \n' 
    '3. Buscar en una lista de elementos numéricos, los elementos mayores a un valor X ' 
    'dado por el usuario y mostrar cuantos se encontraron. \n \n ' 
    '4. Calcular la suma de todos los elementos de una lista en sus posiciones impares.\n \n'
    '5. Contar en una lista de elementos numéricos cuantos elementos son positivos, cuantos \n \n' 
    'negativos y cuantos son cero.' 
    '6. Calcular los cuadrados de todos los elementos de una lista.\n \n'
    '7. Determinar si un número X dado por el usuario se encuentra repetido o no en una lista' 
    'de elementos numéricos.\n \n' 
    '8. Buscar en una lista de elementos numéricos los elementos menores a un valor X dado ' 
    'por el usuario y mostrar las posiciones donde están ubicados.\n \n'
    '0.salir \n \n '
    'Tu respuesta: '))
    return menu


menu = mostrarmenu()
while (menu !=0):
    if menu == 1:
        print("Este ejercicio multiplicará todos los valores que usted agregue \n \n")
        numeros = []
        multi = 1
        tam = int(input('Ingresa la cantidad de numeros a multiplicar: '))

        for i in range(0,tam,1):
            num = int(input(f'Ingresa numero {i}: '))
            numeros.append(num)
        
        for j in range(0,(len(numeros)),1):
            multi*=numeros[j]
        
        print("El resultado de la multiplicación entre", end=": ")
        for k in range(0,len(numeros),1):
            print(numeros[k], end=", ")
        print("Es el siguiente: ",multi, "\n \n")

        opc = int(input("Desea volver al menu? 1.Si 2.No: "))
        if(opc == 1):
            menu = mostrarmenu()
        if(opc == 2):
            break

    if menu == 2:
        print("Este ejercicio sumará todos los valores que usted agregue \n \n")
        numeros = []
        suma = 0
        tam = int(input('Ingresa la cantidad de numeros a sumar: '))

        for i in range(0,tam,1):
            num = int(input(f'Ingresa numero {i}: '))
            numeros.append(num)
        
        for j in range(0,(len(numeros)),1):
            suma+=numeros[j]
        
        print("El resultado de la suma entre", end=": ")
        for k in range(0,len(numeros),1):
            print(numeros[k], end=", ")
        print("Es el siguiente: ",suma," \n \n")

        opc = int(input("Desea volver al menu? 1.Si 2.No: "))
        if(opc == 1):
            menu = mostrarmenu()
        if(opc == 2):
            break

    if menu == 3:
        contador = 0
        print("Este ejercicio encontrará los valores mayores al numero que usted agregue \n \n")
        numeros = [3,6,8,23,29,33,50,45,23,14,60,17,70,85,92,99]
        numX = int(input('Ingresa un numero: '))

        for numero in numeros:
            if(numero>numX):
                contador+=1
        
        print(f'La cantidad de numeros mayores a {numX} es: ',contador, '\n \n')

        opc = int(input("Desea volver al menu? 1.Si 2.No: "))
        if(opc == 1):
            menu = mostrarmenu()
        if(opc == 2):
            break

    if menu == 4:
        suma = 0
        print("Este ejercicio calculará la suma de unicamente los numeros impares de la lista \n \n")
        numeros = [3,6,8,23,29,33,50,45,23,14,60,17,70,85,92,99]

        for i in range(0,len(numeros),1):
            if(i%2 != 0):
                suma+=numeros[i]
        
        print("La suma es: ",suma," \n \n")

        opc = int(input("Desea volver al menu? 1.Si 2.No: "))
        if(opc == 1):
            menu = mostrarmenu()
        if(opc == 2):
            break

    if menu == 5:
        contadorpositivo=0
        contadornegativo=0
        contadorcero=0
        print("Este ejercicio contará cuantos numeros positivos, negativos o ceros hay en la lista \n \n")
        numeros = [3,6,8,23,29,33,-4,-30,-20,50,45,23,14,60,0,17,-50,70,85,0,92,99]

        for num in numeros:
            if(num>0):
                contadorpositivo+=1
            if(num<0):
                contadornegativo+=1
            if(num==0):
                contadorcero+=1

        print(f"La cantidad de positivos es {contadorpositivo}, negativos: {contadornegativo}, ceros: {contadorcero} \n \n")

        opc = int(input("Desea volver al menu? 1.Si 2.No: "))
        if(opc == 1):
            menu = mostrarmenu()
        if(opc == 2):
            break

    
    if menu == 6:
        print("Este ejercicio calculará el cuadrado de cada numero de la lista \n \n")
        numeros = [3,6,8,23,29,33,50,45,23,14,60,17,70,85,92,99]

        for num in numeros:
            cuadrado = num**2
            print(f"cuadrado de {num} es: {cuadrado} \n \n")

        opc = int(input("Desea volver al menu? 1.Si 2.No: "))
        if(opc == 1):
            menu = mostrarmenu()
        if(opc == 2):
            break
    
    if menu == 7:
        contador = 0
        print("Este ejercicio definirá si hay algun valor en la lista igual al que usted ingrese \n \n")
        numeros = [3,6,8,23,29,33,50,45,23,14,60,17,70,85,92,99]
        numX = int(input('Ingresa un numero: '))

        for num in numeros:
            if(num == numX):
                contador+=1
        
        print(f"El numero {numX} esta repetido en la lista {contador} veces \n \n")

        opc = int(input("Desea volver al menu? 1.Si 2.No: "))
        if(opc == 1):
            menu = mostrarmenu()
        if(opc == 2):
            break
    
    if menu == 8:
        contador = 0
        print("Este ejercicio definirá si hay algun valor menor al numero que usted ingrese y devolverá su posicion \n \n")
        numeros = [3,6,8,23,29,33,50,45,23,14,60,17,70,85,92,99]
        numX = int(input('Ingresa un numero: '))

        for posicion, num in enumerate(numeros):
            if(num < numX):
                print(f"El numero {num} en la posicion {posicion}")

        opc = int(input("Desea volver al menu? 1.Si 2.No: "))
        if(opc == 1):
            menu = mostrarmenu()
        if(opc == 2):
            break
