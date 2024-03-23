import sympy
import numpy
x = sympy.symbols('x')

p = sympy.Poly(x**2 + 3*x + 2)

print(p)

print("Coeficientes")
print(p.coeffs())

print("grado del polinomio:")
print(p.degree())

print("Evaluar el polinomio en 1 y 2:")
print(p.eval(1))
print(p.eval(2))

print("NUEVO POLINOMIO ----")

q = numpy.poly1d([1, 3, 2])
print(q)
print("Coeficientes")
print(q.coeffs)
print("grado del polinomio:")
print(q.order)

print("Evaluar el polinomio en 1 y 2:")
print(q(1))
print(q(2))

q = numpy.poly1d([1, 3, 2])
p = numpy.poly1d([1, 3, 2,5,6,7])
print(p/q)
print(p*q)
print(p-q)
print(p+q)
print(p.r)


print("NUEVO POLINOMIO ----")

q = sympy.Poly(x**2 + 3*x + 2)
p = sympy.Poly(x**2 + 3*x + 2 +5*x**3 +6*x**4 +7*x**5)
print(p/q)
print(p*q)P
print(p-q)
print(p+q)

