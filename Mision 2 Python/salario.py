valorHora = input("Ingresa el valor de la hora: ")
valorHora = int(valorHora)

horas = input("Ingresa la cantidad de horas trabajadas para este trabajador: ")
horas = int(horas)

salario = (valorHora*horas)-(valorHora*horas)*0.08


print("El salario del trabajador es: ",salario)