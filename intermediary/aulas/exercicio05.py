import copy

produtos = [
    {'nome': 'produto_5', 'preco': 10.00},
    {'nome': 'produto_1', 'preco': 1220.00},
    {'nome': 'produto_3', 'preco': 123.00},
    {'nome': 'produto_2', 'preco': 30.00},
    {'nome': 'produto_4', 'preco': 20.00},
]
print('produtos originais: ', *produtos, sep='\n')
product_2 = copy.deepcopy(produtos)
product_2 = [
    {**p, 'preco': round(p['preco']*1.1, 2)} for p in product_2
]
print('produtos com preços incrementados', *product_2, sep='\n')
product_2_sorted_price = sorted(
    product_2,
    key=lambda item: item['preco']
)
product_2_sorted_reverse_name = sorted(
    product_2,
    key=lambda item: item['nome'],
    reverse=True
)

print(f'Produtos ordenados por preço: ', *product_2_sorted_price, sep='\n')
print(f'Produtos ordenados reversamente por nome: ', *product_2_sorted_reverse_name, sep='\n')
