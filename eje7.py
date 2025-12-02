
from itertools import combinations

# Lista base
elementos = ["A", "B", "C", "D"]

k = int(input("Ingrese el tamaño de la combinación k: "))

print(f"Combinaciones de tamaño {k}:")
for combo in combinations(elementos, k):
    print(combo)
