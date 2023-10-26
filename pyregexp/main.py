import re

# findall, search, sub
# compile
# esse módulo (re) é case sensitive: Teste != teste


string = "Este é um teste de expressões regulares"


# nesse caso, teste fora compilado apenas uma vez

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('expressão', string))

# ou

print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'expressão', string))
