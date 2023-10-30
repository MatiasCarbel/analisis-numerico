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
x_values = [-1.09955, -0.628313, -0.157075, 0.314164, 0.785403, 1.25664, 1.72788, 2.19912, 2.67036, 3.1416, 3.61283, 4.08407, 4.55531, 5.02655, 5.49779, 5.96903, 6.44026, 6.9115, 7.38274, 7.85398]
y_values = [0.255553, 0.494236, 1.10515, 1.41347, 1.89405, 2.00413, 1.8873, 1.65722, 0.926025, 0.495908, -0.307551, -0.585353, -0.740357, -0.579873, 0.19002, 0.732755, 1.91443, 2.42173, 3.01857, 3.01857]

# Espaciado entre puntos (puedes mantener tu valor de h si es adecuado)
h = 0.47123

# Calcular la derivada utilizando la función five_point_difference
result = five_point_difference(x_values, y_values, h)


# Redondear los valores a cuatro decimales
result_rounded = [(x, round(y, 4)) for x, y in result]

# Imprimir los resultados con cuatro decimales
table = tabulate(result_rounded, headers=["X", "Fd(X) METODO"], tablefmt="pretty")
print(table)


