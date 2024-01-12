from copy import deepcopy


def imprimi_dicio(dicio: dict) -> None:
    for key, value in dicio.items():
        print(f'{key}: {value}')


dicio = {
    "nome": 'Daniel',
    "sobrenome": 'Brown',
    "idade": 26
}

pessoa = dict(nome='Daniel Brown')

#  criando chaves dinâmicas
dicio['profissão'] = 'desenvolvedor de software'

# copiando dicionários
dicio_copy = dicio  # dicio_copy aponta para o mesmo dicionário que dicio


# para retirar essa ligação, copie o dicionário

# shallow copy
dicio2 = dicio.copy()  # copia apenas as chaves
# deep copy
dicio3 = deepcopy(dicio)

# atualizando o dicio3
dicio3.update(
    {'salário': 9500}
)

imprimi_dicio(dicio3)
