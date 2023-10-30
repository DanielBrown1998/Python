import json
from principal import AboutMe

# lendo seus atributos salvos
with open('meus_dados.json', 'r', encoding='utf-8') as file:
    attributes = json.load(file)

# inserindo-os na nova instância
c2 = AboutMe(*attributes.values())

show = (c for c in dict(c2.__dict__).items())
try:
    while True:
        k, c = show.__next__()
        print(f"{k}: {c}")
except StopIteration:
    pass
