import random

listas_de_listas = []
for k in range(10):
    listas_de_listas.append([random.randint(0, 10) for c in range(10)])


def check_sequencial(*lista: tuple[int] | list[int]) -> int:
    my_var = 0
    for e in lista:
        if e != 1:
            my_var += 1
    return -1 if my_var == 0 else my_var


# verificando a duplicação
for i in listas_de_listas:
    print(*[c for c in i])
    my_possibilities = set()
    my_possibilities.update(i)
    print(*[my_possibilities])
    my_times = list()
    for element in my_possibilities:
        x = i.count(element)
        my_times.append(x)
    my_possibilities.clear()
    resp = check_sequencial(*my_times)
    print(f'Existe(m) {resp} número(s) com mais de uma ocorrência')
    my_times.clear()
