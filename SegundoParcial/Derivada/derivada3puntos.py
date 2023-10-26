import numpy as np
from tabulate import tabulate

def three_point_difference(func, x, h):
    """
    Calcula la derivada de una función utilizando el método de los 3 puntos de diferenciación numérica.

    :param func: La función de la cual se calculará la derivada.
    :param x: El valor en el que se calculará la derivada.
    :param h: El espaciado entre los puntos.
    :return: El valor de la derivada en x.
    """
    dy_dx = (func(x + h) - func(x - h)) / (2 * h)
    return dy_dx

# Definir la función proporcionada
def custom_function(x):
    return (1/x)+(x**2/2)

# Definir la derivada real de la función (sustituye con la derivada real si la conoces)
def real_derivative(x):
    return -1/(x**2) + x

# Definir los parámetros
a = 1  # Extremo inferior del intervalo
b = 2  # Extremo superior del intervalo
n = 6  # Número de puntos

# Espaciado entre puntos
h = 0.2

# Calcular la derivada utilizando la función three_point_difference
results = []

for i in range(n):
    x = a + i * h
    dy_dx = three_point_difference(custom_function, x, h)
    real_dy_dx = real_derivative(x)
    error = abs(dy_dx - real_dy_dx)
    results.append((i, x, dy_dx, real_dy_dx, error))

# Imprimir los resultados en una tabla
table = tabulate(results, headers=["i", "X", "Fd(X) METODO", "Fd(X) REAL", "Error"], tablefmt="grid")
print(table)
