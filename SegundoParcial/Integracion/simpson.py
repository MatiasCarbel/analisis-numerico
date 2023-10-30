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


def simpson(funcion, a, b, m):
    h = (b - a) / float(m)
    s = 0
    x = a

    results = []

    for i in range(1, m + 1):
        n = x + (i * h)
        n_evaluado = funcion.evalf(subs={"x": n})
        s = s + 2 * (i % 2 + 1) * n_evaluado

        a_evaluado = funcion.evalf(subs={"x": a})
        b_evaluado = funcion.evalf(subs={"x": b})

        resul = h / 3 * (a_evaluado + s + b_evaluado)

        results.append([i, n, resul]) 

    return results


print ("Super calculo de integrales simples con el metodo de simpson c:")

x = Symbol('x')
f = exp(0.1*x)*cos(x)
funcion = sympify(f)

a =  -1.57079 # -pi/2
b = 7.85398 # 5/2*pi
m = 20 # 20 particiones


results = simpson(funcion, a, b, m)
print(tabulate(results, headers=["Pasos", "Valor de x", "Valor Integral"], tablefmt="grid"))