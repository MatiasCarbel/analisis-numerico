import numpy as np

def five_point_difference(points, h):
    """
    Calcula la derivada de una serie de puntos utilizando el método de los 5 puntos de diferenciación numérica.

    :param points: Un arreglo NumPy de puntos [(x0, y0), (x1, y1), ...] ordenados por x.
    :param h: El espaciado entre los puntos.
    :return: Un arreglo NumPy de tuplas con el resultado de la derivada en cada punto [(x0, dy/dx0), (x1, dy/dx1), ...].
    """
    derivative = []

    for i in range(len(points)):
        if i < 2 or i >= len(points) - 2:
            # Para los primeros dos y últimos dos puntos, usamos diferenciación hacia adelante y hacia atrás.
            if i < 2:
                dy_dx = (-3 * points[i][1] + 12 * points[i + 1][1] - 6 * points[i + 2][1] + 2 * points[i + 3][1]) / (6 * h)
            else:
                dy_dx = (-2 * points[i - 3][1] + 6 * points[i - 2][1] - 12 * points[i - 1][1] + 3 * points[i][1]) / (6 * h)
        else:
            # Para los puntos en el medio, usamos los cinco puntos centrados.
            dy_dx = (points[i - 2][1] - 8 * points[i - 1][1] + 8 * points[i + 1][1] - points[i + 2][1]) / (12 * h)
        
        derivative.append((points[i][0], dy_dx))
    
    return np.array(derivative)

# Puntos proporcionados
x_values = [0.0000, 0.5000, 1.0000, 1.5000, 2.0000]
y_values = [0.0000, 0.4207, 0.4546, 0.0706, -0.3784]

# Organizar los puntos en una lista de tuplas
points = np.array(list(zip(x_values, y_values)))

# Espaciado entre puntos
h = x_values[1] - x_values[0]  # Suponemos que los puntos están igualmente espaciados

# Calcular la derivada utilizando la función five_point_difference
result = five_point_difference(points, h)

# Imprimir los resultados
for x, dy_dx in result:
    print(f"x = {x}, dy/dx = {dy_dx}")
