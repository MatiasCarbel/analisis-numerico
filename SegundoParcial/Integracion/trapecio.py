from sympy import sympify
from tabulate import tabulate

"""
f = ingreso de la funcion (ej: 8 + 5 * cos(x))
a = parametro inicial de la integral
b = parametro final de la integral
m = numero de particiones(en los ejercicios se lo muestra generalmente con "n")

Resultado
Imprime una tabla con los resultados de cada paso y el valor de la integral
"""


def trapecios(funcion, a, b, m):
    h = (b - a) / float(m)
    s = 0
    n = 0
    a_evaluado = 0
    b_evaluado = 0

    results = []

    for i in range(1, m ):
        n = a + (i * h)
        n_evaluado = funcion.evalf(subs={"x": n})
        s = s + n_evaluado

        a_evaluado = funcion.evalf(subs={"x": a})
        b_evaluado = funcion.evalf(subs={"x": b})
        resul = h / 2 * (a_evaluado + 2 * s + b_evaluado)

        results.append([i, resul])

    return results

print("Super calculo de integrales simples con metodo del trapecio c:")

f = input("Ingrese su funcion en terminos de x:\n")
funcion = sympify(f)

a = float(input("Ingrese su parametro inicial:\n"))
b = float(input("Ingrese su parametro final:\n"))
m = int(input("Ingrese el numero de particiones:\n"))  # Convierte a entero el numero de particiones

results = trapecios(funcion, a, b, m)
print(tabulate(results, headers=["Pasos", "Valor Integral"], tablefmt="fancy_grid"))

