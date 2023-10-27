from sympy import *
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

    for i in range(1, m + 1):  # Modificado para calcular 10 particiones
        n = a + (i * h)
        n_evaluado = funcion.evalf(subs={"x": n})
        s = s + n_evaluado

        a_evaluado = funcion.evalf(subs={"x": a})
        b_evaluado = funcion.evalf(subs={"x": b})
        resul = h / 2 * (a_evaluado + 2 * s + b_evaluado)

        results.append([i, n, resul])

    return results

print("Super cálculo de integrales simples con método del trapecio c:")

f = input("Ingrese su función en términos de x:\n")
funcion = sympify(f)

a = float(input("Ingrese su parámetro inicial:\n"))
b = 2 * pi
m = int(input("Ingrese el número de particiones :\n"))

results = trapecios(funcion, a, b, m)
print(tabulate(results, headers=["Pasos", "Valor de x", "Valor Integral"], tablefmt="grid"))


