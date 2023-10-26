estates = ['RJ', 'MG', 'SP', 'ES', 'BA', 'CE']
capital = ['Rio de Janeiro', 'Belo Horizonte', 'São Paulo', 'Vitória', 'Salvador', 'Fortaleza', 'Manaus', 'Recife']

def decorator(func):
    def estados(lista1, lista2):
        tmp = list()
        if lista1 < lista2:
            for e, c in enumerate(lista1):
                unidade = (c, lista2[e])
                tmp.append(unidade)
        elif lista2 < lista1:
            for e, c in enumerate(lista2):
                unidade = (c, lista1[e])
                tmp.append(unidade)
        func(lista1, lista2)
    return estados

@decorator
def zipper(lista1, lista2):
    print(f'{zipper.__name__}')
    for estado, capital in zip(lista1, lista2):
        print(f'{estado}: {capital}')

zipper(estates, capital)

# decorator(zipper(estates, capital))

