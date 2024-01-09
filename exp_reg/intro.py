import re

# findall, search, sub
# compile
# esse módulo (re) é case sensitive: Teste != teste

string = "Este é um teste de expressões regulares"

# nesse caso, teste fora compilado apenas uma vez

regexp = re.compile(r'teste')
print(regexp.search(string))  # encontra a primeira ocorrência e retorna o índice
print(regexp.findall(string))  # encontra todas as ocorrências e retorna uma lista com a respectiva palavra
print(regexp.sub('expressão', string))  # substitui a expressão

# ou

print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'expressão', string))
