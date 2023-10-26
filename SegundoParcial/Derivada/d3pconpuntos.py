import numpy as np
from tabulate import tabulate

def three_point_difference(x_values, y_values, h):
    dy_dx = []
    n = len(x_values)
    
    # Derivada en el primer punto
    dy_dx_first = (y_values[1] - y_values[0]) / (x_values[1] - x_values[0])
    dy_dx.append((x_values[0], dy_dx_first))
    
    # Derivada en los puntos interiores
    for i in range(1, n - 1):
        dy_dx_value = (y_values[i + 1] - y_values[i - 1]) / (2 * h)
        dy_dx.append((x_values[i], dy_dx_value))
    
    # Derivada en el último punto
    dy_dx_last = (y_values[n - 1] - y_values[n - 2]) / (x_values[n - 1] - x_values[n - 2])
    dy_dx.append((x_values[n - 1], dy_dx_last))
    
    return dy_dx

# Ejemplo con 3 puntos en las listas de X e Y
x_values = [1.0, 1.2, 1.4]
y_values = [2.44, 4.0, 5.76]

# Verificar que haya exactamente 3 valores en cada lista
if len(x_values) != 3 or len(y_values) != 3:
    print("Debe proporcionar exactamente 3 valores en cada lista de x e y.")
else:
    # Espaciado entre puntos
    h = 0.2

    # Calcular la derivada utilizando la función three_point_difference
    results = three_point_difference(x_values, y_values, h)

    # Imprimir los resultados en una tabla
    table = tabulate(results, headers=["X", "Fd(X) METODO"], tablefmt="grid")
    print(table)
