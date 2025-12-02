print( "hola")

def combinacion(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    k = min(k, n - k)  # optimización
    res = 1
    
    for i in range(1, k + 1):
        res = res * (n - i + 1) // i
    
    return res

# Programa principal
n = int(input("Ingrese n: "))
k = int(input("Ingrese k: "))

print(f"C({n}, {k}) = {combinacion(n, k)}")
