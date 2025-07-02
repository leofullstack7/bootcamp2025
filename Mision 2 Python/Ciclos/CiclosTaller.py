menu = int(input('Ingrese el proceso que desea realizar \n \n \n 1. Escribir un algoritmo que calcule la suma de los n primeros números naturales. '
    'Analizar si se puede implementar con los dos tipos de ciclos. El valor de n es dado por el usuario. \n \n' 
    '2. Escribir un algoritmo que calcule la suma de los cuadrados de los n primeros números' 
    'naturales: 12 + 22 + 32 +… + n2. \n \n' 
    '3. Escribir un algoritmo que calcule la suma de los números enteros de n a m, siendo '
    'm>n, utilizando el algoritmo del ejercicio 1. Los valores de n y m son dados por el '
    'usuario. \n \n' 
    '4. Implementar un algoritmo que calcule el producto de dos números enteros (n*m) '
    'haciendo sólo sumas. \n \n'
    '5. Diseñar un algoritmo que calcule y muestre el promedio de cinco valores de '
    'temperaturas dadas por el usuario. \n \n' 
    '6. Dada las horas Extras trabajadas de una persona por día en una semana, de lunes a '
    'viernes, y la tarifa de pago. Calcular el valor total a pagar e imprimirlo por pantalla. \n \n'
    '7. Calcular y visualizar la suma y el producto de los números pares comprendidos entre ' 
    '20 y 400 ambos inclusive. \n \n'
    '8. Realice un algoritmo que permita adivinar un número preestablecido entre 1 y 10, '
    'dando al usuario tres intentos, e informando si adivino o fallo. (ciclos + condicionales) \n \n'
    '9. Realice un algoritmo que solicite sólo números positivos, muestre su suma y promedio, '
    'hasta que el usuario digite 0, o digite un número negativo. (ciclos + condicionales). \n \n'
    '10. Escriba un algoritmo que genere y muestre la tabla de multiplicar de un número entero '
    'positivo dado por el usuario. \n \n'
    '0. SALIR \n \n' \
    'Tu Respuesta: '))

while (menu != 0):
    if menu == 1:
        suma = 0
        limite = int(input('Ingresa hasta que numero deseas sumar '))
        for i in range(1,(limite+1),1):
            suma+=i
        print("El valor de la suma es: ",suma)    
        break
    if menu == 2:
        suma = 0
        limite = int(input('Ingresa hasta que numero deseas que se sumen los cuadrados '))
        for i in range(1,(limite+1),1):
            suma+=(i**2)
        print("El valor de la suma de los cuadrados de 1 hasta ",limite," es",suma)
        break
    if menu == 3:
        suma = 0
        inicio = int(input('Ingresa desde que numero deseas sumar' ))
        fin = int(input('Ingresa hasta que numero deseas sumar '))
        for inicio in range(inicio,(fin+1),1):
            suma+=inicio
        print("El valor de la suma desde ",inicio," a ",fin," es: ",suma)   
        break
    if menu == 4:
        producto = 0
        num1 = int(input('Ingresa numero 1 a multiplicar '))
        num2 = int(input('Ingresa numero 2 a multiplicar '))
        for i in range(1,(num2+1),1):
            producto+=num1
        print("El valor de la multiplicacion es: ",producto)
        break
    if menu == 5:
        promedio = 0
        numero=1
        for i in range(1,6,1):
            
                if(i==5):
                    numero = int(input('Ingresa el ultimo numero: '))
                    while numero < 0 or numero =='':
                        numero = int(input('Ingresa el ultimo numero: '))
                else: 
                    numero = int(input(f'Ingresa numero {i} para realizar el promedio final: '))
                    while numero < 0 or numero =='':
                        numero = int(input(f'Ingresa numero {i} para realizar el promedio final: '))
                promedio+= numero
        promedio/=5
        
        print("El resultado del promedio total de los 5 numeros es: ",promedio)
        break

    if menu == 6:
        salario = int(input('Ingresa el valor de la hora extra para tu trabajador: '))
        dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
        extras = 0
        for i in range(0,(len(dias)),1):
            num1 = int(input(f'Ingresa las horas extras trabajadas el {dias[i]}: '))
            extras+=(salario*num1)
        
        print('El valor total a pagar es: ',extras)
        break



    

        
