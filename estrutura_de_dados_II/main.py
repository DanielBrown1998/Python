# estrutura de de dados II
from pathlib import Path

file_dir = str(Path(__file__).parent / '_arquivo.txt'), str(Path(__file__).parent / 'arquivo2.txt')


class No:
    def __init__(self, word, file):
        self.valor: str = word
        self.esquerda: No | None = None
        self.direita: No | None = None
        self.altura: int = 1
        self.arquivos = {}
        if file not in self.arquivos.keys():
            self.arquivos[file] = 1


class Arvore:
    def altura(self, no: No) -> int:
        # Se o no for o inicial
        if no is None:
            return 0
        # Se não retone a altura
        else:
            return no.altura

    def balanceado(self, no: No) -> int:
        # Se o no for o inicial
        if no is None:
            return 0
        # Se não retorne a altura da esquerda menos a altura da direita (fator de balanceamento)
        else:
            return self.altura(no.esquerda) - self.altura(no.direita)

    def rotacao_direita(self, no: No) -> No:
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

    def rotacao_esquerda(self, no: No) -> No:
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

    def inserir(self, val: str, raiz: No, file: str) -> No | None:

        # Se o no for o inicial
        if raiz is None:
            return No(val, file[-12::1])

        # Se o valor do no for menor ou igual que o valor da raiz
        elif val < raiz.valor:
            # O no será inserido na esquerda do no raiz
            raiz.esquerda = self.inserir(val, raiz.esquerda, file)

        elif val == raiz.valor:
            try:
                raiz.arquivos[file[-12::]] += 1
            except KeyError:
                raiz.arquivos.update({f"{file[-12::]}": 1})

        # Se o valor do no for maior que o valor da raiz
        elif val > raiz.valor:
            # O no será inserido na direita do no raiz
            raiz.direita = self.inserir(val, raiz.direita, file)

        # Seta uma nova altura no nó (pega a maior e adiciona 1)
        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))

        # atribui as localizações do arquivo e suas devidas ocorrências

        # Chama a funução balanceado
        balanceado = self.balanceado(raiz)

        # Se o retorno da função balanceado for maior que 1 e o valor do no esquerdo dele for maior que o no a ser inserido
        if balanceado > 1 and raiz.esquerda.valor > val:
            # O no a ser inserido rotaciona para a direita
            return self.rotacao_direita(raiz)

        # Se o retorno da função balanceado for menor que -1 e o valor do no direito dele for menor que o no a ser inserido
        if balanceado < -1 and val > raiz.direita.valor:
            # O no a ser inserido rotaciona para a esquerda
            return self.rotacao_esquerda(raiz)

        # Se o retordo da função balanceado for maior que 1 e o valor do no esquerdo dele for menor que a do no a ser inserido
        if balanceado > 1 and val > raiz.esquerda.valor:
            # O no da esquerda rotaciona para a esquerda
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            # O no a ser inserido rotaciona para a esquerda
            return self.rotacao_direita(raiz)

        # Se o retorno da função balanceado for menor que -1 e o valor do no direito dele for maior que o no a ser inserido
        if balanceado < -1 and val < raiz.direita.valor:
            # O no da direita rotaciona para a direita
            raiz.direita = self.rotacao_direita(raiz.direita)
            # O no a ser inserido rotaciona para a esquerda
            return self.rotacao_esquerda(raiz)

        return raiz

    # percorrendo a matriz
    def in_order(self, raiz: No) -> None:
        # Funcão para imprimir
        if raiz is None:
            return
        self.in_order(raiz.esquerda)
        print(f"{raiz.valor}->{raiz.arquivos}")
        self.in_order(raiz.direita)

    def pre_order(self, raiz: No) -> None:
        #Funcão para imprimir
        if raiz is None:
            return
        print(raiz.valor)
        self.pre_order(raiz.esquerda)
        self.pre_order(raiz.direita)

    def pos_order(self, raiz: No) -> None:
        # Funcão para imprimir
        if raiz is None:
            return
        self.pos_order(raiz.esquerda)
        self.pos_order(raiz.direita)
        print(raiz.valor)

    def find_no(self, raiz: No, valor: str) -> No | None:

        if raiz is None:
            return  # se a arvore estiver vazia

        while raiz.valor != valor:

            if valor < raiz.valor:
                raiz = raiz.esquerda
            else:
                raiz = raiz.direita

            # encontrou uma folha
            if raiz is None:
                return None

        return raiz


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
        # lendo os arquivos
        for e, arquivo in enumerate(args):
            try:
                with open(arquivo, 'r', encoding='utf-8') as file:
                    lista = file.readlines()
            except FileNotFoundError:
                print("Arquivo não encontrado")
                print("criando...")
                with open(arquivo, 'w', encoding='utf-8') as file:
                    print(f"arquivos criados, agora ponha algum texto nele!")
                    lista = file.readlines()
            # lendo as linhas
            for c in lista:
                # percorrendo as linhas
                sub_lista = c.split()

                # adicionando os elementos da linha na Árvore
                for item in sub_lista:
                    # caso a palavra contenha menos de 3 letras
                    if len(item) < 3:
                        continue
                    # todo regex
                    item = item.lower().strip().replace('\n', '')
                    item = item.replace(',', '').replace('"', '')
                    item = item.replace('.', '').replace("'", '')
                    item = item.replace('?', '').replace('!', '')
                    raiz = tree.inserir(item, raiz, arquivo)

        # executa em 2°
        while True:
            print("""
ordenar -> põe os vocábulos em ordem alfabética;
buscar -> buscar palavra;
sair -> para sair;
            """)

            opc = input('digite a opção desejada: ').strip().lower()
            while opc.isspace() or opc in "":
                print('Não entendi, repita, por favor!!!')
                opc = input('digite a opção desejada: ').strip().lower()
            if opc == 'ordenar':
                tree.in_order(raiz)
            elif opc == "buscar":
                valor = input('digite a palavra desejada: ').strip().lower()
                check_value = tree.find_no(raiz, valor)
                if check_value:
                    print(f'{check_value.valor} foi encontrado nos arquivos: ')
                    print(*[f"{k}: {v} vezes" for k, v in check_value.arquivos.items()], sep='\n')
                else:
                    print('Valor não encontrado')
            elif opc == 'sair':
                break
            # retornando a arvore

        return tree

    # retornando a função interna e a repassando para execute
    return intern_func


@main
def execute(lista: list | tuple):
    """
    :param lista: busca os destinos do arquivo
    :return: None
    """
    # executa em 3°


if __name__ == '__main__':
    execute(*file_dir)
