
def combinacion_recursiva(n, k):
    # Casos base
    if k == 0 or k == n:
        return 1
    
    # Fórmula recursiva
    return combinacion_recursiva(n - 1, k - 1) + combinacion_recursiva(n - 1, k)

# Programa principal
n = int(input("Ingrese el valor de n: "))
k = int(input("Ingrese el valor de k: "))

resultado = combinacion_recursiva(n, k)

print(f"C({n}, {k}) = {resultado}")
