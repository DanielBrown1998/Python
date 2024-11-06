import os
from typing import List
try:
    from models.restaurante import Restaurante
except ImportError as e:
    print(f"Módulo não encontrado")
    print(f"Erro: {e.args}")
    exit(1)
nome_empresa = """ｓａｂｏｒｅｓ ｅｘｐｒｅｓｓ"""

acoes = {
    1: "Cadastrar Restaurante",
    2: "Listar Restaurantes",
    3: "(Des)Ativar Restaurante",
    4: "Inserir Avaliação",
    5: "Listar Avaliações",
    6: "Sair"
}

restaurantes: List[Restaurante] = []

def titulo(msg: str) -> None:
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

def buscar_restaurante(nome):
    """
    Função para buscar um restaurante
    """
    for restaurante in restaurantes:
        if nome.lower() in restaurante.nome.lower() \
            and len(nome) == len(restaurante.nome):
            print(f"{restaurante.nome} encontrado")
            return restaurante
        else:
            print("Restaurante não encontrado")
            return 
    
def des_ativar_restaurantes(restaurantes: List[Restaurante]) -> bool:
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
        restaurante = buscar_restaurante(nome)
        if not restaurante:
            return False
        if restaurante.status:
            restaurante.desativar()
            print(f"Restaurante {restaurante.nome} desativado")
        else:
            restaurante.ativar()
            print(f"Restaurante {restaurante.nome} ativado")
        input("Aperte uma tecla para continuar: ")        
        return restaurante.status
    except Exception as e:
        print(f"Erro: {e.args}")
        input("Aperte uma tecla para continuar: ")
        return False

def listar_restaurantes(restaurantes: List[Restaurante], all=False) ->  None:
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
            print(restaurante)
            print("\n")

    else:
        for e, restaurante in enumerate(restaurantes):
            if restaurante.status:
                print(f"{e+1} ->", end=' ')
                print(restaurante)
                print("\n")
        
def cadastro_restaurantes(restaurantes: List[Restaurante]) -> Restaurante:

    """
    Função para cadastrar um restaurante
    :param restaurantes: List: Lista de restaurantes
    :return: List: Lista de restaurantes atualizada
    """

    titulo("""𝕔𝕒𝕕𝕒𝕤𝕥𝕣𝕒𝕣 𝕣𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖""")

    nome = in_put("nome: ", str)
    endereco = in_put("endereço: ", str)
    telefone = in_put("telefone com DDD (só números) | Ex: (21999999999): ", int)
    while len(str(telefone)) != 11: 
        print("telefone inválido")
        telefone = in_put("telefone com DDD (21999999999): ", int)

    restaurante = Restaurante(
        nome=nome,
        local=endereco,
        telefone=[telefone]
    )
    restaurantes.append(restaurante)    
    print(f"Restaurante {nome} cadastrado com sucesso!")
    input("Aperte uma tecla para continuar: ")
    return restaurantes

def main():
    """
    Função principal
    """
    
    opcao: int = 0
    LIM = 6
    while opcao != LIM:

        titulo(nome_empresa)
        print(*[f"{k}: {v}" for k, v in acoes.items()], sep='\n')
        opcao = in_put("Escolha uma opção: ", int)
        while opcao not in range(1, LIM+1):
            print("Opção inválida")
            opcao = in_put("Escolha uma opção: ", int)

        if opcao == 1:
            cadastro_restaurantes(restaurantes)    
            
        elif opcao == 2:
            listar_restaurantes(restaurantes)
            input("Aperte uma tecla para continuar: ")

        elif opcao == 3:
            des_ativar_restaurantes(restaurantes)
        elif opcao == 4:
            nome = in_put(
                "Digite seu nome: ", str
            )
            listar_restaurantes(restaurantes, all=True)
            nome_restaurante = in_put("Digite o nome do restaurante: ", str)
            restaurante = buscar_restaurante(nome_restaurante)
            if not restaurante:
                input("Aperte uma tecla para continuar: ")
                continue
            nota = in_put("Digite a nota: ", float)
            comentario = in_put("Digite o comentário: ", str)
            restaurante.adicionar_avaliacao(nome, restaurante, nota, comentario)
            input("Aperte uma tecla para continuar: ")

        elif opcao == 5:
            listar_restaurantes(restaurantes, all=True)
            nome_restaurante = in_put("Digite o nome do restaurante: ", str)
            restaurante = buscar_restaurante(nome_restaurante)
            if not restaurante:
                print(f"Restaurante não encontrado!")
                input("Aperte uma tecla para continuar: ")
                continue
            print(f"Avaliações do {restaurante.nome}")
            print("=="*20)
            for avaliacao in restaurante.avaliacoes:
                print(f"Usuario: {avaliacao.usuario}\n nota: {avaliacao.nota}\n comentário: {avaliacao.avaliacao}")
                print("=="*20)
            input("Aperte uma tecla para continuar: ")

        elif opcao == 6:
            os.system("cls")
            print("""
                𝕒𝕥𝕖́ 𝕞𝕒𝕚𝕤...
    """) 
            break

if __name__ == '__main__':
    main()
