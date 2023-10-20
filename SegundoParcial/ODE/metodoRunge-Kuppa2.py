import numpy as np
from tabulate import tabulate

"""
# F = ODE escrita en forma estándar.(Cada vez que se quiera usar un exponente es necesitaro np.exp(x) al principio)
# h = Tamaño del paso
# x = Vector de valores de x (Las primeras dos posiciónes son los valores iniciales de x, osea el intervalo ej [0,4])
# y0 = Condición inicial de y osea y(0) = 1, hace referencia al valor de y en la primera posición de x, y es lo que aproximas

El resultado va a ser mostrado en una lista por interaciones, y al final se imprime el último valor de x y y
"""

# Función para el método de Runge-Kutta de segundo orden
def runge_kutta_second_order(f, x, y0, h):
    results = []
    y = y0
    for xi in x:
        results.append([xi, y])
        k1 = h * f(xi, y)
        k2 = h * f(xi + h/2, y + k1/2)
        y = y + k2
    return results

# Definición de la ecuación diferencial y los parámetros
f = lambda x, y: np.exp(0.8 * x) - 0.5 * y
h = 0.1  # Tamaño del paso
x = np.arange(0, 4 + h, h)
y0 = 2  # Condición inicial

# Calcular los resultados utilizando el método de Runge-Kutta   
results = runge_kutta_second_order(f, x, y0, h)

# Mostrar los resultados en una tabla
table_headers = ["x", "y"]
print(tabulate(results, headers=table_headers, tablefmt="grid"))
