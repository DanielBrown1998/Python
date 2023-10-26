import random

lista_a = [c for c in range(15)]
lista_b = [random.randint(1, 11) for c in range(10)]

print(*lista_a)
print(*lista_b)
def soma_de_listas(list1, list2):
    min_items = min(len(list1), len(list2))
    for items in range(min_items):
        if not isinstance(items, (int, float)):
            raise TypeError('\033]31mAs listas devem conter apenas valores numéricos!!!\033]m')
    return [list1[c]+list2[c] for c in range(min_items)]

soma = soma_de_listas(lista_b, lista_a)
# print(*soma)

# outro modo

soma_listas = [x+y for x, y in zip(lista_b, lista_a)]
print(*soma_listas)
