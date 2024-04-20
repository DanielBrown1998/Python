# estrutura de de dados II
from pathlib import Path

file_dir = str(Path(__file__).parent / 'arquivo.txt'), str(Path(__file__).parent / 'arquivo2.txt')


class No:
    def __init__(self, num):
        self.valor = num
        self.esquerda = None
        self.direita = None
        self.altura = 1


class Arvore:
    def altura(self, no: No):
        # Se o no for o inicial
        if no is None:
            return 0
        # Se não retone a altura
        else:
            return no.altura

    def balanceado(self, no: No):
        # Se o no for o inicial
        if no is None:
            return 0
        # Se não retorne a altura da esquerda menos a altura da direita (fator de balanceamento)
        else:
            return self.altura(no.esquerda) - self.altura(no.direita)

    def rotacao_direita(self, no: No):
        # Setando os nos em variaveis
        a = no.esquerda
        b = a.direita
        # Setando os nos nas novas variaveis
        a.direita = no
        no.esquerda = b
        # Seta a nova altura do no
        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))
        a.altura = 1 + max(self.altura(a.esquerda), self.altura(a.direita))
        return a

    def rotacao_esquerda(self, no: No):
        # Setando os nos em variaveis
        a = no.direita
        b = a.esquerda
        # Setando os nos nas novas variaveis
        a.esquerda = no
        no.direita = b
        # Seta a nova altura do no
        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))
        a.altura = 1 + max(self.altura(a.esquerda), self.altura(a.direita))
        return a

    def inserir(self, val, raiz):
        # Se o no for o inicial
        if raiz is None:
            return No(val)
        # Se o valor do no for menor ou igual que o valor da raiz
        elif val <= raiz.valor:
            # O no será inserido na esquerda do no raiz
            raiz.esquerda = self.inserir(val, raiz.esquerda)
        # Se o valor do no for maior que o valor da raiz
        elif val > raiz.valor:
            # O no será inserido na direita do no raiz
            raiz.direita = self.inserir(val, raiz.direita)
        # Seta uma nova altura no nó (pega a maior e adiciona 1)
        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))
        # Chama a funução Balanceado
        Balanceado = self.balanceado(raiz)
        # Se o retorno da função Balanceado for maior que 1 e o valor do no esquerdo dele for maior que o no a ser inserido
        if Balanceado > 1 and raiz.esquerda.valor > val:
            # O no a ser inserido rotaciona para a direita
            return self.rotacao_direita(raiz)
        # Se o retorno da função Balanceado for menor que -1 e o valor do no direito dele for menor que o no a ser inserido
        if Balanceado < -1 and val > raiz.direita.valor:
            # O no a ser inserido rotaciona para a esquerda
            return self.rotacao_esquerda(raiz)
        # Se o retordo da função Balanceado for maior que 1 e o valor do no esquerdo dele for menor que a do no a ser inserido
        if Balanceado > 1 and val > raiz.esquerda.valor:
            # O no da esquerda rotaciona para a esquerda
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            # O no a ser inserido rotaciona para a esquerda
            return self.rotacao_direita(raiz)
        # Se o retorno da função Balanceado for menor que -1 e o valor do no direito dele for maior que o no a ser inserido
        if Balanceado < -1 and val < raiz.direita.valor:
            # O no da direita rotaciona para a direita
            raiz.direita = self.rotacao_direita(raiz.direita)
            # O no a ser inserido rotaciona para a esquerda
            return self.rotacao_esquerda(raiz)
        return raiz

    def in_order(self, raiz):
        # Funcão para imprimir
        if raiz is None:
            return
        self.in_order(raiz.esquerda)
        print(raiz.valor)
        self.in_order(raiz.direita)

    def pre_order(self, raiz):
        #Funcão para imprimir
        if raiz is None:
            return
        print(raiz.valor)
        self.pre_order(raiz.esquerda)
        self.pre_order(raiz.direita)

    def pos_order(self, raiz):
        # Funcão para imprimir
        if raiz is None:
            return
        self.pos_order(raiz.esquerda)
        self.pos_order(raiz.direita)
        print(raiz.valor)


# teste
# Arvore = Arvore()
# R = None
# R = Arvore.inserir(3, R)
# R = Arvore.inserir(5, R)
# R = Arvore.inserir(7, R)
# R = Arvore.inserir(2, R)
# R = Arvore.inserir(4, R)
# R = Arvore.inserir(6, R)
# R = Arvore.inserir(8, R)
#
# print("---InOrder---")
# Arvore.in_order(R)
# print("---PreOrder")
# Arvore.pre_order(R)
# print("---PosOrder")
# Arvore.pos_order(R)


def main(func):
    # executa em 1°
    tree = Arvore()

    def intern_func(*args):
        raiz = None
        total_words = []
        # lendo os arquivos
        for arquivo in file_dir:
            with open(arquivo, 'r', encoding='utf-8') as file:
                lista = file.readlines()
            # lendo as linhas
            for c in lista:
                # percorrendo as linhas
                sub_lista = c.split()
                # adicionando os elementos da linha na Árvore
                for item in sub_lista:
                    total_words.append(item)
                    raiz = tree.inserir(item, raiz)

        # todo implementar uma lista com a frequencia dos items ...
        # todo ... e em qual arquivo ela aparece

        result = func(total_words)
        # executa em 2°
        return result

    return intern_func


@main
def execute(lista: list):
    # executa em 3°
    print(*[lista])

    return lista


if __name__ == '__main__':
    execute()
