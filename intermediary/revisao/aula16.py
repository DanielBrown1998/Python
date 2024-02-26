import json

eu = {
    "nome": "Daniel",
    "sobrenome": "Brown Rodrigues Mingozzi dos Passos",
    "altura": 1.84,
    "formação acadêmica": 'Universidade do Estado do Rio de Janeiro',
    "dev": True,
    "experiência": None,
}

with open(r"./my_profile.json", 'w', encoding='utf8') as file:
    json.dump(
        eu,
        file,
        indent=2,
    )


def print_dict(**kwargs):
    print(*[f"{k}: {v}" for k, v in kwargs.items()], sep='\n')


with open(r"./my_profile.json", 'r', encoding='utf8') as file:
    my_file = json.load(file)
    print_dict(**my_file)
