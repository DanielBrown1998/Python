#Lucro por quiilo de cada tipo de alimento


lucro_por_tipo = {
    'tomate': 2.00,
    'alface': 1.50,
}

demanda_por_tipo = {
    'tomate': {'agua': 3, 'espaco': 2.2},
    'alface': {'agua': 2, 'espaco': 3},
}

disponibilidade_recursos = {
    'agua': 5900,
    'espaco': 5400
}


max_tomate = min(
    disponibilidade_recursos['agua']/demanda_por_tipo['tomate']['agua'],
    disponibilidade_recursos['espaco']/demanda_por_tipo['tomate']['espaco']
)

max_alface = min(
    disponibilidade_recursos['agua']/demanda_por_tipo['alface']['agua'],
    disponibilidade_recursos['espaco']/demanda_por_tipo['alface']['espaco']
)



def calcular_lucro_e_viabilidade(qtd_tomate, qtd_alface):
    uso_agua = qtd_alface*demanda_por_tipo['alface']['agua'] + qtd_tomate*demanda_por_tipo['tomate']['agua']
    uso_espaco = qtd_alface*demanda_por_tipo['alface']['espaco'] + qtd_tomate*demanda_por_tipo['tomate']['espaco']
    
    restricoes = {
        'agua': uso_agua,
        'espaco': uso_espaco,
        'dicersificacao': (qtd_alface, qtd_tomate)
    }

    viola_restricoes = (
        uso_agua > disponibilidade_recursos['agua'] or 
        uso_espaco > disponibilidade_recursos['espaco'] or 
        qtd_tomate < 0.1*qtd_alface
    )

    lucro = qtd_tomate*lucro_por_tipo['tomate']+qtd_alface*lucro_por_tipo['alface']

    return lucro, viola_restricoes, restricoes


if __name__ == '__main__':
    print(calcular_lucro_e_viabilidade(16, 0))
    