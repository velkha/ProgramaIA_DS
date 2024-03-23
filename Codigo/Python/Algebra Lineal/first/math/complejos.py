import cmath

def print_complex(z):
    print(f"-------- Complejo {z} ---------")
    print(f"Real: {z.real}, Imaginary: {z.imag}")
    print(f"Type: {type(z)}")
    print(f"Conjugado: {z.conjugate()}")
    print(f"Modulo: {abs(z)}")
    print(f"Argumento principal: {cmath.phase(z)}")

z1 = 1 - 3**0.5j
print_complex(z1)