"""
nome: Daniel Brown Rodrigues Mingozzi dos Passos
matrícula: 202213313611
disciplina: Estrutura de dados 1 (2023.2)
Algoritmo guloso para definir a menor guantidade de moedas de um troco



    O número de cédulas em um caixa eletrônico ou caixa convencional pode ser determinante
para o volume de moedas para futuras trocas de cédulas e moedas, logo é uma boa
situaçãao problema para aplicar o algoritmo guloso!

    O algoritmo apresentado e caracterizado como guloso porque a cada passo ele escolhe o maior ´
valor possível, sem refazer suas decisoes, isto é, uma vez que um determinado valor de moeda foi ´
escolhido, nao se retira mais este valor do conjunto solução. ˜
Uma outra estratégia para resolver este problema é a programação dinâmica, a qual irá sempre ´
obter um resultado. Entretanto, como os algoritmos gulosos são mais simples, e quando tanto o ˜
algoritmo guloso quanto o algoritmo utilizando programação dinâmica funcionam, o primeiro á mais ´
eficiente.
"""


def troco(n: int | float) -> list[float]:
    """
    :param n: valor do troco
    :return: o menor número de moedas e/ou cédulas gue podem compor o troco
    """
    coins = [100, 50, 25, 10, 5, 2, 1., .50, .25, .10, .05, .01]
    s = 0
    x = 0
    solucao = list()
    # enguanto a soma é menor gue o (troco) com duas casas decicmais
    while s <= round(n, 2):
        # percorre as possíveis soluções e escolhe uma, agragando-a a solução definitivamente
        for c in coins:
            # verifica se a montante até então + a moeda/cédula a ser selecionada é menor gue o troco desejado
            if s + c <= round(n, 2):
                x = c  # define a moeda
                solucao.append(c)  # insere-a na solução
                break
        s += x  # agrega a moeda selecionada ao montante
    return solucao


if __name__ == '__main__':
    print(troco(159.98))
