import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

# Definición de la ecuación diferencial y los parámetros
f = lambda x, y: np.exp(0.8 * x) - 0.5 * y
h = 0.1
x = np.arange(0, 4 + h, h)
y0 = 2  # Condición inicial

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