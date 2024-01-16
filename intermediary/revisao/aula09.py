# funções anônimas

lista = [
    {'nome': 'Daniel', 'idade': 26},
    {'nome': 'Dayse', 'idade': 49},
    {'nome': 'Rafaela', 'idade': 25},
    {'nome': 'Rafael', 'idade': 23},
]
lista.sort(key=lambda item: item['idade'])
print(*lista)
