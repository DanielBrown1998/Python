questions = [
    {
        "pergunta: ": 'A soma de dois mais dois é?',
        "opções: ": ["um", "dois", "três", "quatro"],
        "resposta": "quatro"
    },
    {
        "pergunta: ": 'O quadrado do número cinco é?',
        "opções: ": [7, 10, 15, 25],
        "resposta": 25
    },
    {
        "pergunta: ": 'A divisão de 10 por 2 no python é?',
        "opções: ": [0.25, .2, 5.0, 5],
        "resposta": 5.0
    }
]


acertos = 0
for c in questions:
    print(c["pergunta: "])
    print(*[f"{e+1}: {k}" for e, k in enumerate(c["opções: "])], sep='\n')
    resposta = input("selecione uma opção: ")
    while isinstance(resposta, int) or int(resposta) < 1 or int(resposta) > 4:
        resposta = input("selecione uma opção: ")
    if c['opções: '][int(resposta)-1] == c['resposta']:
        acertos += 1

print(f"Você acertou {acertos} questões")
