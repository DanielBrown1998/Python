questions = [
    {
        'pergunta': '2+2?',
        'alternativas': ['6', '1', '3', '4', '5'],
        'respostas': '4'
    },
    {
        'pergunta': 'O valor de 5x5?',
        'alternativas': ['10', '15', '20', '55', '25'],
        'respostas': '25'
    },
    {
        'pergunta': 'O valor de 10/2?',
        'alternativas': ['6', '0.2', '5', '0.5', '0.4'],
        'respostas': '5'
    }
]
soma = 0


for c in questions:
    tent = 2
    print(c['pergunta'])
    for e, k in enumerate(c['alternativas']):
        print(f"{e})", k)
    resp = str(input('escolha uma opção-> ')).strip()
    while int(resp) not in list(range(5)) and tent != 0:
        tent -= 1
        print(f'\033[31mFora das opções\033[m')
        print(c['pergunta'])
        for e, k in enumerate(c['alternativas']):
            print(f"{e})", k)
        resp = str(input('escolha uma opção-> ')).strip()

    else:
        if tent == 0:
            print("n°. de tentativas alcançadas!")

    if tent != 0:
        if c['alternativas'][int(resp)] == c['respostas']:
            soma += 1

print(f"Você teve {soma} acertos de 3 perguntas!")
