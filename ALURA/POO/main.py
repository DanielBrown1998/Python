import os
from typing import List
import random

nome_empresa = """
            ｓａｂｏｒｅｓ ｅｘｐｒｅｓｓ
        """

acoes = {
    1: "Cadastrar Restaurante",
    2: "Listar Restaurantes",
    3: "(Des)Ativar Restaurante",
    4: "Sair"
}

restaurantes = []


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


def des_ativar_restaurantes(restaurantes: List) -> None:
    os.system("cls")

    print("""
            𝕒𝕥𝕚𝕧𝕒𝕣/𝕕𝕖𝕤𝕒𝕥𝕚𝕧𝕒𝕣 𝕣𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖𝕤
          """)
    print("OBS: se ativo, ao inserir o id, ele será desativado!")

    listar_restaurantes(restaurantes, all=True)
    id = in_put("digite o id: ", int)

    for restaurante in restaurantes:
        if restaurante['id'] == id:
            if restaurante['status']:
                restaurante['status'] = False
            else:
                restaurante['status'] = True


def listar_restaurantes(restaurantes: List, all=False) ->  None:
    os.system("cls")
    print("""
            𝕝𝕚𝕤𝕥𝕒𝕣 𝕣𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖𝕤
    """)
    if all:
        for restaurante in restaurantes:
            for k, v in restaurante.items():
                print(f"{k}, {v}", end = " |")
            print("\n")

    else:
        for restaurante in restaurantes:
            if restaurante['status']:
                for k, v in restaurante.items():
                    if k != 'status':
                        print(f"{k}: {v}", end = ' |')
            print("\n")
    

def cadastro_restaurantes(restaurantes: List) -> List:
    
    restaurante_attr = {}
    
    os.system("cls")

    print("""
            𝕔𝕒𝕕𝕒𝕤𝕥𝕣𝕒𝕣 𝕣𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖
    """)

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
    opcao: int = 0
    while opcao != 4:

        print(nome_empresa)
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
