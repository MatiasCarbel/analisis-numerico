import numpy as np
import matplotlib.pyplot as plt


# F = ODE escrita en forma estándar.(Cada vez que se quiera usar un exponente es necesitaro np.exp(x) al principio)
# h = Tamaño del paso
# x = Vector de valores de x (Las primeras dos posiciónes son los valores iniciales de x, osea el intervalo ej [0,4])
# y0 = Condición inicial de y osea y(0) = 1, hace referencia al valor de y en la primera posición de x, y es lo que aproximas

#Resultado: Imprime una tabla con los valores de x y y en cada iteración, y al final imprime el último valor de x y y
#El ultimo valor de y es el resultado final de la aproximación

plt.style.use('seaborn-poster')

# Definición de la ecuación diferencial y los parámetros
f = lambda x, y: 2 * x * np.exp(3) + 12 * x * np.exp(2) - 20 * x + 8.5
h = 0.5
x = np.arange(0, 4 + h, h)
y0 = 1  # Condición inicial

# Euler's method
y = np.zeros(len(x))
y[0] = y0

# Output header
print("---RESULTS---")
print("X\t\tY")

for i in range(0, len(x) - 1):
    y[i + 1] = y[i] + h * f(x[i], y[i])
    print(f"{x[i]:.2f}\t\t{y[i]:.4f}")

# Print the last point
print(f"{x[-1]:.2f}\t\t{y[-1]:.4f}")