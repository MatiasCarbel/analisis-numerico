import numpy as np
from tabulate import tabulate
from sympy import Symbol, exp, cos, sin, sympify

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
    return np.exp(0.1*x) * np.cos(x)

# Definir la derivada real de la función (sustituye con la derivada real si la conoces)
def real_derivative(x):
    return 0.1 * np.exp(0.1*x) * np.cos(x) - np.exp(0.1*x) * np.sin(x)

x = Symbol('x')
f = exp(0.1*x) * cos(x)
funcion = sympify(f)

a = -1.57079 # -pi/2
b = 7.85398 # 5/2*pi
n = 20 # 20 particiones
# Espaciado entre puntos
h = 0.47123

# Calcular la derivada utilizando la función three_point_difference
results = []

for i in range(n):
    x_value = a + i * h
    dy_dx = three_point_difference(custom_function, x_value, h)
    real_dy_dx = real_derivative(x_value)
    error = abs(dy_dx - real_dy_dx)
    results.append((i, x_value, dy_dx, real_dy_dx, error))

# Imprimir los resultados en una tabla
table = tabulate(results, headers=["i", "X", "Fd(X) METODO", "Fd(X) REAL", "Error"], tablefmt="grid")
print(table)
