import os
from typing import List
import random

nome_empresa = """ｓａｂｏｒｅｓ ｅｘｐｒｅｓｓ"""

acoes = {
    1: "Cadastrar Restaurante",
    2: "Listar Restaurantes",
    3: "(Des)Ativar Restaurante",
    4: "Sair"
}

restaurantes = []

def titulo(msg):
    """
    Função para exibir um título centralizado
    """
    os.system("cls")
    print(f"\033[1;32m {msg:^45} \033[m")
    print(f"{' * ' * 20}\n")


def in_put(msg: str, tipo: object) -> object:
    """
    Função para receber um input do usuário e validar o tipo
    
    :param msg: str: Mensagem a ser exibida ao usuário
    :param tipo: object: Tipo a ser validado
    
    :return: object: Valor convertido para o tipo válido
    """
    if tipo not in [str, int, float]:
        raise ValueError("Tipo inválido")
    while True:
        try:
            if tipo == str:
                return tipo(input(msg).strip())
            return tipo(input(msg))
        except ValueError:
            print("Valor inválido")


def des_ativar_restaurantes(restaurantes: List) -> bool:
    """
    Função para desativar ou ativar um restaurante

    :param restaurantes: List: Lista de restaurantes
    :return: bool: True se o restaurante foi desativado, False se não
    """

    titulo("""𝕒𝕥𝕚𝕧𝕒𝕣/𝕕𝕖𝕤𝕒𝕥𝕚𝕧𝕒𝕣 𝕣𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖𝕤""")

    if not restaurantes:
        print("Nenhum restaurante cadastrado")
        input("Aperte uma tecla para continuar: ")
        return False

    nome = in_put("digite o nome do restaurante: ", str)

    try:
        for restaurante in restaurantes:
            if nome.lower() in restaurante['nome'].lower():
                if restaurante['status']:
                    print(f"Desativando {restaurante['nome']}")
                else:
                    print(f"Ativando {restaurante['nome']}")
                restaurante['status'] = not restaurante['status']
                break
        else:
            print("Restaurante não encontrado")

        input("Aperte uma tecla para continuar: ")
        
        return restaurante['status']
    except Exception as e:
        print(f"Erro: {e.args}")
        input("Aperte uma tecla para continuar: ")
        return False

def listar_restaurantes(restaurantes: List, all=False) ->  None:
    """
    Função para listar os restaurantes cadastrados
    :param restaurantes: List: Lista de restaurantes
    :param all: bool: True para listar todos os restaurantes, False para listar apenas os ativos
    """
    titulo("""𝕝𝕚𝕤𝕥𝕒𝕣 𝕣𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖𝕤""")
    if not restaurantes:
        print("Nenhum restaurante cadastrado")
        input("Aperte uma tecla para continuar: ")
        return
    if all:
        for e, restaurante in enumerate(restaurantes):
            print(f"{e+1} ->", end=' ')
            for k, v in restaurante.items():
                print(f"{k}, {v}", end = " |")
            print("\n")

    else:
        for e, restaurante in enumerate(restaurantes):
            if restaurante['status']:
                for k, v in restaurante.items():
                    if k != 'id':
                        print(f"{e+1} -> {k}: {v}", end = ' |')
            print("\n")
    
    input("Aperte uma tecla para continuar: ")
    
def cadastro_restaurantes(restaurantes: List) -> List:

    """
    Função para cadastrar um restaurante
    :param restaurantes: List: Lista de restaurantes
    :return: List: Lista de restaurantes atualizada
    """
    restaurante_attr = {}
    
    titulo("""𝕔𝕒𝕕𝕒𝕤𝕥𝕣𝕒𝕣 𝕣𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖""")

    restaurante_attr['id'] = int(random.randint(1, 1000000))
    restaurante_attr['nome'] = in_put("nome: ", str)
    restaurante_attr['endereço'] = in_put("endereço: ", str)
    restaurante_attr['telefone'] = in_put("telefone com DDD (só números) | Ex: (21999999999): ", int)
    while len(str(restaurante_attr['telefone'])) != 11: 
        print("telefone inválido")
        restaurante_attr['telefone'] = in_put("telefone com DDD (21999999999): ", int)
    restaurante_attr['status'] = False

    restaurantes.append(restaurante_attr)
    return restaurantes
    

def main():
    """
    Função principal
    """
    
    opcao: int = 0
    while opcao != 4:

        titulo(nome_empresa)
        print(*[f"{k}: {v}" for k, v in acoes.items()], sep='\n')
        opcao = in_put("Escolha uma opção: ", int)
        while opcao not in range(1, 5):
            print("Opção inválida")
            opcao = in_put("Escolha uma opção: ", int)

        if opcao == 1:
            cadastro_restaurantes(restaurantes)    
            
        elif opcao == 2:
            listar_restaurantes(restaurantes)

        elif opcao == 3:
            des_ativar_restaurantes(restaurantes)

        elif opcao == 4:
            os.system("cls")
            print("""
                𝕒𝕥𝕖́ 𝕞𝕒𝕚𝕤...
    """) 
            break


if __name__ == '__main__':
    main()
