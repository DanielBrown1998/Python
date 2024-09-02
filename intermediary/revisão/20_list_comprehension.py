import random

TAM_MIN, TAM_MAX = 1, 10
LISTA = [random.randint(TAM_MIN, TAM_MAX) for c in range(TAM_MAX)]  
print(*LISTA)
LISTA = map(
    lambda x: x**2,
    LISTA
)
print(*list(LISTA))