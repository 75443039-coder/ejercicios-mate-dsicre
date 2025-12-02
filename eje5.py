print("hola")

import math

def combinacion(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

# Programa principal
n = int(input("Ingrese el valor de n: "))
k = int(input("Ingrese el valor de k: "))

resultado = combinacion(n, k)
print(f"C({n}, {k}) = {resultado}")
