from random import randint


def conj(*iter):
    elements = list(iter)[:]
    result_value = set()

    for element in elements:
        cont = elements.count(element)
        if cont > 1:
            result_value.add(element)

    if len(result_value) == 0:
        return -1

    pos = 0
    result_pos = dict()
    for item in result_value:
        for pos, element in enumerate(elements):
            if element == item:
                result_pos[item] = pos

    del pos
    del elements

    pos_maior = 11
    for item in result_value:
        if result_pos[item] < pos_maior:
            pos_maior = result_pos[item]

    del result_value
    del result_pos

    return iter[pos_maior]


lista_de_listas = list()
for k in range(10):
    lista_num = []
    for c in range(10):
        num = randint(0, 10)
        lista_num.append(num)
    lista_de_listas.append(lista_num)
lista_de_listas.append(tuple(c for c in range(0, 10)))
lista_de_listas.append(tuple(c for c in range(10, 0, -1)))

for lista in lista_de_listas:
    if conj(*lista) != -1:
        print(f"O elemento {conj(*lista)} repete primeiro na {tuple(c for c in lista)}")
    else:
        print(f"A lista {tuple(c for c in lista)} não possui elementos repetidos")
