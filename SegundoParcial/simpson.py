from sympy import*

f = ""
print ("Super calculo de integrales simples con el metodo de simpson c:")

f = input("Ingrese su funcion en terminos de x:\n")
funcion = sympify(f)

a = float(input("Ingrese su parametro inicial:\n"))
b = float(input("Ingrese su parametro final:\n"))
m = int(input("Ingrese el numero de particiones:\n"))

def simpson(funcion,a,b,m):
  h = (b-a)/float(m)
  s = 0
  x = a

  for i in range(1,m):
    n = x + (i*h)
    n_evaluado = funcion.evalf(subs = {"x" : n})
    s = s + 2*(i%2+1)*n_evaluado

  a_evaluado = funcion.evalf(subs = {"x" : a})
  b_evaluado = funcion.evalf(subs = {"x" : b})

  resul = h/3 * (a_evaluado + s + b_evaluado)
  return resul

print (simpson(funcion,a,b,m))