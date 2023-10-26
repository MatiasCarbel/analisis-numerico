import numpy as np
from tabulate import tabulate

def five_point_difference(x_values, y_values, h):
    """
    Calcula la derivada de una serie de puntos utilizando el método de los 5 puntos de diferenciación numérica.

    :param x_values: Un arreglo de puntos x [x0, x1, ...].
    :param y_values: Un arreglo de puntos y correspondientes [y0, y1, ...].
    :param h: El espaciado entre los puntos.
    :return: Un arreglo NumPy de tuplas con el resultado de la derivada en cada punto [(x0, dy/dx0), (x1, dy/dx1), ...].
    """
    derivative = []

    for i in range(len(x_values)):
        x = x_values[i]
        if i < 2 or i >= len(x_values) - 2:
            # Para los primeros dos y últimos dos puntos, usamos diferenciación hacia adelante y hacia atrás.
            if i < 2:
                dy_dx = (-3 * y_values[i] + 12 * y_values[i + 1] - 6 * y_values[i + 2] + 2 * y_values[i + 3]) / (6 * h)
            else:
                dy_dx = (-2 * y_values[i - 3] + 6 * y_values[i - 2] - 12 * y_values[i - 1] + 3 * y_values[i]) / (6 * h)
        else:
            # Para los puntos en el medio, usamos los cinco puntos centrados.
            dy_dx = (y_values[i - 2] - 8 * y_values[i - 1] + 8 * y_values[i + 1] - y_values[i + 2]) / (12 * h)

        derivative.append((x, dy_dx))

    return np.array(derivative)

# Ejemplo de entrada de valores X e Y
x_values = [0.0000, 0.1000, 0.2000, 0.3000, 0.4000]
y_values = [1.0000, 7.0000, 4.0000, 3.0000, 5.0000]

# Espaciado entre puntos
h = 0.1

# Calcular la derivada utilizando la función five_point_difference
result = five_point_difference(x_values, y_values, h)

# Imprimir los resultados
table = tabulate(result, headers=["X", "Fd(X) METODO"], tablefmt="pretty")
print(table)
