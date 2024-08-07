# list comprehension em Python
print(f"Package: {__name__}")
if __name__ == '__main__':

    tabela = [
        {'produto': 'p1', 'preço': 25.4},
        {'produto': 'p2', 'preço': 9.2},
        {'produto': 'p3', 'preço': 15.3},
    ]

    lista = [{**c} if c['preço'] > 20 else {**c, 'preço': round(c['preço'] * 1.5, 2)}  # map
             for c in tabela  # aqui vem o filtro
             ]
    print(*lista, sep='\n')

    coordenadas = list([
        (x, y) for y in range(3)
        for x in range(3)
    ])

    for y in range(3):
        for x in range(3):
            print(x, y)

    print(*coordenadas, sep='\n')
