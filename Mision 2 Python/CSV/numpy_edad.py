import numpy as np
import matplotlib.pyplot as plt

edades = [38,25,42,18,32,16,22,3,39,27]

suma = np.sum(edades)
print("suma: ",suma)
datos = np.count_nonzero(edades)
print("cantidad: ",datos)

prom = np.mean(edades)
print("promedio: ",prom)

median = np.median(edades)
print("Mediana: ",median)

minimo = np.min(edades)
print("Minimo: ",minimo)

maximo = np.max(edades)
print("Maximo: ",maximo)


ds = np.std(edades)
print("Desviación: ",ds)


x = np.linspace(1, 10, 10) #10 puntos entre 1 y 10  (donde inicia, donde termina, numero de puntos)
y = np.array(edades)

plt.plot(x, y, color='blue', linestyle='--', marker='o')
plt.title("Grafico")
plt.grid()
plt.show()