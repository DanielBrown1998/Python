import random

TAM_MIN, TAM_MAX = 1, 10
LISTA = [random.randint(TAM_MIN, TAM_MAX) for c in range(TAM_MAX)]  
print(*LISTA)
LISTA = map(
    lambda x: x**2,
    LISTA
) # map
LISTA = list(LISTA)
print(*LISTA)
LISTA = [
    (item, e) for e, _ in enumerate(LISTA) for item in LISTA 
    if item % 2 == 0 and item % 3 == 0] #  filter
LISTA = sorted(LISTA, key=lambda x: x[1])
print(*LISTA)
