import numpy as np
from tabulate import tabulate

# F = ODE escrita en forma estándar.(Cada vez que se quiera usar un exponente es necesitaro np.exp(x) al principio)
# h = Tamaño del paso
# x = Vector de valores de x (Las primeras dos posiciónes son los valores iniciales de x, osea el intervalo ej [0,4])
# y0 = Condición inicial de y osea y(0) = 1, hace referencia al valor de y en la primera posición de x, y es lo que aproximas

#Resultado: Imprime una tabla con los valores de x y y en cada iteración, y al final imprime el último valor de x y y
#El ultimo valor de y es el resultado final de la aproximación


# Define the differential equation and parameters
f = lambda x, y: np.exp(0.8 * x) - 0.5 * y
h = 0.1  # Step size
x = np.arange(0, 4 + h, h)  # Adjust the range to match your desired output
y0 = 2  # Initial condition

# Improved Euler Method (Heun's Method)
y = np.zeros(len(x))
y[0] = y0

# Almacenar resultados en una lista
results = []

# Iteración para calcular resultados
for i in range(0, len(x) - 1):
    y_predictor = y[i] + h * f(x[i], y[i])
    y[i + 1] = y[i] + 0.5 * h * (f(x[i], y[i]) + f(x[i + 1], y_predictor))
    results.append([x[i], y[i]])

# Agregar el último punto
results.append([x[-1], y[-1]])

# Mostrar los resultados en formato de tabla
table_headers = ["X", "Y"]
print(tabulate(results, headers=table_headers, tablefmt="grid"))
