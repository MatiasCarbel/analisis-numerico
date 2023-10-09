from tabulate import tabulate

def simpson(x_values, y_values):
    m = len(x_values) - 1
    h = (x_values[-1] - x_values[0]) / float(m)
    s = 0

    results = []

    for i in range(1, m):
        x = x_values[i]
        n_evaluado = y_values[i]
        s += 2 * (i % 2 + 1) * n_evaluado

        a_evaluado = y_values[0]
        b_evaluado = y_values[-1]
        resul = h / 3 * (a_evaluado + s + b_evaluado)

        results.append([i, resul])

    return results

def trapecios(x_values, y_values):
    m = len(x_values) - 1
    h = (x_values[-1] - x_values[0]) / float(m)
    s = 0

    results = []

    for i in range(1, m):
        s += y_values[i]

        a_evaluado = y_values[0]
        b_evaluado = y_values[-1]
        resul = h / 2 * (a_evaluado + 2 * s + b_evaluado)

        results.append([i, resul])

    return results

# Ejemplo de entrada de valores X e Y
x_values = [0.0000, 0.1000, 0.2000, 0.3000, 0.4000, 0.5000]
y_values = [1.0000, 7.0000, 4.0000, 3.0000, 5.0000, 9.0000]

results_simpson = simpson(x_values, y_values)
results_trapecios = trapecios(x_values, y_values)

print("Super cálculo de integrales simples con el método de Simpson c:")
print(tabulate(results_simpson, headers=["Pasos", "Valor Integral"], tablefmt="grid"))

print("Super cálculo de integrales simples con el método del trapecio c:")
print(tabulate(results_trapecios, headers=["Pasos", "Valor Integral"], tablefmt="grid"))
