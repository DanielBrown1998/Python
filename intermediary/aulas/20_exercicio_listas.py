from typing import List, Generator
capitais = ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Rio de Janeiro']
estados = ['BA', 'SP', 'MG', 'RJ']


def zipper(lista_a: List,lista_b: List) -> Generator:
    TAM = min(
        (len(lista_a), len(lista_b))
        )
    return (
        (lista_a[i], lista_b[i]) for i in range(TAM)
    )



estados_x_capitais = zip(
    estados,
    capitais
)

print(list(zipper(capitais, estados)))

print(list(estados_x_capitais))