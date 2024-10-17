from itertools import combinations, permutations, product


pessoas = ['João', 'Maria', 'José', 'Pedro', 'Ana', 'Carlos']
transporte = ["carro", "moto"]
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte',
              'Curitiba', 'Porto Alegre', 'Salvador']
# Exemplo de uso das funções itertools
combinacoes = [i for i in combinations(pessoas, 2)]
permutacoes = [i for i in permutations(cidades, 2)]
produtos = [i for i in product(pessoas, transporte, cidades)]
    
print(*permutacoes, sep='\n')
print(*produtos, sep='\n')
print(*combinacoes, sep='\n')