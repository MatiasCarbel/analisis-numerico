import numpy as np
from tabulate import tabulate

"""
# F = ODE escrita en forma estándar.(Cada vez que se quiera usar un exponente es necesitaro np.exp(x) al principio)
# h = Tamaño del paso
# x = Vector de valores de x (Las primeras dos posiciónes son los valores iniciales de x, osea el intervalo ej [0,4])
# y0 = Condición inicial de y osea y(0) = 1, hace referencia al valor de y en la primera posición de x, y es lo que aproximas


El resultado va a ser mostrado en una lsita por interaciones, y al final se imprime el último valor de x y y

"""

# Definición de la ecuación diferencial y los parámetros
f = lambda x, y: x + y*np.exp(2)
h = 0.25  # Tamaño del paso
x = np.arange(1, 5 + h, h)
y0 = 0  # Condición inicial

# Método de Runge-Kutta de cuarto orden
y = np.zeros(len(x))
y[0] = y0

# Almacenar resultados en una lista
results = []

# Iteración para calcular resultados
for i in range(0, len(x) - 1):
    k1 = h * f(x[i], y[i])
    k2 = h * f(x[i] + h/2, y[i] + k1/2)
    k3 = h * f(x[i] + h/2, y[i] + k2/2)
    k4 = h * f(x[i] + h, y[i] + k3)
    
    y[i + 1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    results.append([x[i], y[i]])

# Agregar el último punto
results.append([x[-1], y[-1]])

# Mostrar los resultados en formato de tabla
table_headers = ["X", "Y"]
print(tabulate(results, headers=table_headers, tablefmt="grid"))
