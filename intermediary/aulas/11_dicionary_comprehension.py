produto = {
    'nome': 'Caneta Bic Preta',
    'preco': 3.50,
    'importada': True,
    'estoque': 1000
}
# Dicionary Comprehension
# {chave: valor for chave, valor in iterável}
# {chave: valor for chave, valor in iterável if condição}
# {chave: valor for chave, valor in iterável if condição else valor}
# {chave: valor for chave, valor in iterável if condição for chave, valor in iterável}
# {chave: valor for chave, valor in iterável if condição else valor for chave, valor in iterável}
# {chave: valor for chave, valor in iterável for chave, valor in iterável}

# Exemplo 1
# Duplicar o valor de cada chave
print({
    chave: valor * 2  if isinstance(valor, (int, float)) else valor for chave, valor in produto.items()})
# Exemplo 2
# Duplicar o valor de cada chave se for inteiro
print({
    chave: valor * 2  if isinstance(valor, (int)) else valor for chave, valor in produto.items()})
# Exemplo 3
# Duplicar o valor de cada chave se for inteiro e menor que 10
print({
    chave: valor * 2  if isinstance(valor, (int)) and valor < 10 else valor for chave, valor in produto.items()})
# Exemplo 4
# Duplicar o valor de cada chave se for inteiro e menor que 10 e adicionar a chave 'teste'
print({
    chave: valor * 2  if isinstance(valor, (int)) and valor < 10 else valor for chave, valor in produto.items()} | {'teste': 1})


