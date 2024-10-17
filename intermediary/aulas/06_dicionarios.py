from copy import deepcopy
dicionario = {} # dict()
dicionario = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}

print(dicionario)
print(type(dicionario))
print(dicionario['nome'])
print(dicionario['idade'], dicionario.get('endereço', 'Não tem endereço'), sep='\n')
print(dicionario['cidade'])

print('Alterando valores: ')
dicionario['nome'] = 'Maria'
print(dicionario['nome'])
dicionario['idade'] = 30
print(dicionario['idade'])
dicionario['cidade'] = 'Rio de Janeiro'
print(dicionario['cidade'])

print('Adicionando valores: ')
dicionario.setdefault('bairro', 'Centro')
dicionario['estado'] = 'RJ'
print(dicionario)
for key, value in dicionario.items():
    print(f'{key} = {value}')

# cópia rasa
dicionario2 = dicionario.copy()
print(dicionario2)
# cópia profunda
dicionario3 = deepcopy(dicionario)
print(dicionario3)