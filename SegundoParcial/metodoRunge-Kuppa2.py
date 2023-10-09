import numpy as np
from tabulate import tabulate

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
