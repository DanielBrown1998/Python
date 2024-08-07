#groupby
from itertools import groupby

alunos = [
    {'nome': 'Daniel', 'nota': 'A'},
    {'nome': 'Rony', 'nota': 'D'},
    {'nome': 'Vinicius', 'nota': 'C'},
    {'nome': 'Rodrigo', 'nota': 'C'},
    {'nome': 'Maria', 'nota': 'B'},
    {'nome': 'Paulo', 'nota': 'A'},
    {'nome': 'Alan', 'nota': 'D'},
    {'nome': 'Rafael', 'nota': 'B'},
    {'nome': 'Miguel', 'nota': 'D'},
]

# ordenando
alunos = sorted(alunos, key=lambda item: item['nota'])
# print(*alunos, sep='\n')

grupos = groupby(alunos, key=lambda item: item['nota'])
for key, iterable in grupos:
    print(key)
    print(*[f"{key}: {value}" for item in iterable for key, value in item.items() if key == 'nome'], sep='\n')
