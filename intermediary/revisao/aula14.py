from functools import reduce


def print_iter(iterator):
    print(*list(iterator), sep='\n')


produtos = [
        {'produto': 'p1', 'preço': 25.},
        {'produto': 'p2', 'preço': 19.9},
        {'produto': 'p3', 'preço': 15.9},
        {'produto': 'p4', 'preço': 224.9},
        {'produto': 'p5', 'preço': 24.9},
        {'produto': 'p6', 'preço': 19.9},

]


def aumentar_preco(p):
    return {**p, 'preço': round(1.5*p['preço'] if p['preço'] < 100 else p['preço'], 2)}


novos_precos = map(
    aumentar_preco,
    produtos,
)
# novos_precos = [
#     {**p, 'preço': round(1.5*p['preço'] if p['preço'] < 100 else p['preço'], 2)}  # mapeamento
#     for p in produtos
# ]


print_iter(novos_precos)
print("tipo: ", type(novos_precos))
