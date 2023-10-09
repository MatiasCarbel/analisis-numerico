import numpy as np
from tabulate import tabulate

def adams_moulton(f, h, x, y0):
    n = len(x)
    y = np.zeros(n)
    y[0] = y0

    for i in range(1, 4):  # Usamos el método de Euler para las primeras 3 iteraciones
        y[i] = y[i - 1] + h * f(x[i - 1], y[i - 1])

    for i in range(4, n):
        y[i] = y[i - 1] + (h / 24) * (
            9 * f(x[i], y[i]) + 19 * f(x[i - 1], y[i - 1]) -
            5 * f(x[i - 2], y[i - 2]) + f(x[i - 3], y[i - 3])
        )

    return y

# Definición de la ecuación diferencial y los parámetros
f = lambda x, y: np.exp(0.8 * x) - 0.5 * y
h = 0.1  # Tamaño del paso
x = np.arange(0, 4 + h, h)
y0 = 2  # Condición inicial

# Resolvemos la ecuación diferencial utilizando Adams-Moulton
y = adams_moulton(f, h, x, y0)

# Crear una lista de resultados para tabulate
results = []
for i, xi in enumerate(x):
    results.append([i, xi, y[i]])

# Mostrar los resultados en una tabla
table_headers = ["Iteración", "x", "y"]
print(tabulate(results, headers=table_headers, tablefmt="grid"))
