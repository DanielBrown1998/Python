import json

lista = {
    'nome': "Daniel",
    'sabrenome': "Brown",
    "esdereços": {"Rua": "Travessa Mario Avena", "N°": 45},
    "altura": 1.84,
    "dev": True,
    "obs": None
}

with open("file.json", "w+", encoding='utf-8') as file:
    json.dump(lista, file, ensure_ascii=False, indent=6)

with open("file.json", "r", encoding='utf-8') as file:
    pessoa = json.load(file)
    print(type(pessoa))
    print(*pessoa.items(), sep='\n')

num = [c for c in range(10)]
with open("file.json", "w+", encoding='utf-8') as file:
    json.dump(num, file, ensure_ascii=False, indent=10)

with open("file.json", "r", encoding='utf-8') as file:
    number = json.load(file)
    print(*number)
    print(type(number))

with open("file.json", "w+", encoding='utf-8') as file:
    pass
