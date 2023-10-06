import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

# Definición de la ecuación diferencial y los parámetros
f = lambda x, y: np.exp(0.8 * x) - 0.5 * y
h = 0.1
x = np.arange(0, 4 + h, h)
y0 = 2  # Condición inicial

# Método de Euler explícito
y = np.zeros(len(x))
y[0] = y0

for i in range(0, len(x) - 1):
    y[i + 1] = y[i] + h * f(x[i], y[i])

# Cálculo de la ecuación exacta
exact_solution = np.exp(0.8 * x) - 0.5 * y

plt.figure(figsize=(12, 8))
plt.plot(x, y, 'bo--', label='Aproximada')
plt.plot(x, exact_solution, 'g', label='Exacta')  # Corregir el uso de x en lugar de y0
plt.title('Solución Aproximada y Exacta para Ecuación Diferencial')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid()
plt.legend(loc='lower right')
plt.show()
