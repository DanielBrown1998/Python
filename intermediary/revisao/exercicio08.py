l1 = list(range(1, 8))
l2 = list(range(1, 5))


def soma_listas(lista1: list, lista2: list) -> list:
    return [sum(c) for c in list(zip(lista2, lista1))]


lista = soma_listas(l1, l2)
print(lista)
