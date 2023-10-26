import os
import time
from random import randint

def busca_data():
    return []
def check_ordem(dados):
    if dados:
        for e, c in enumerate(dados):
            if c[e]['ids'] > c[e+1]['ids']:
                return 0
        return 1
    return 0
def opc_(msg, msg1="não entendi, repita, por favor"):
    while True:
        try:
            var = int(input(msg))
        except Exception as e:
            print(str(msg1).strip().capitalize())
        else:
            break
    return var
def imprimir(dados):
    if dados:
        print("============DADOS=============")
        for e, c in enumerate(dados):
            print(f"posição: {e} ")
            for key, value in dict(c).items():
                print(f"{key}: {value}")
            print("------------------------------")
    else:
        print("Não há dados a serem listados!!!")
def buscar(dados, ids=None, cpf=None):
    """
    :param dados: estrutura de dados
    :param id: dado usado na busca
    :param cpf: dado usado na busca
    :return: a posição e um dicio com os dados
    """
    if ids:
        for e, c in enumerate(dados):
            if ids in dict(c).values():
                return e, c
    elif cpf:
        for e, c in enumerate(dados):
            if id in dict(c).values():
                return e, c
    else:
        return None
def alterar(dados, ids, nome=False, cpf=False, telefone=False, idade=False):
    for c in dados:
        if ids in dict(c).values():
            if idade:
                c["idade"] = opc_("digite sua idade: ")
            elif cpf:
                c["CPF"] = opc_("digite o CPF (somente números): ")
            elif telefone:
                c["telefone"] = opc_("digite o CPF (somente números): ")
            elif nome:
                while True:
                    try:
                        c["nome"] = str(input("digite o nome: ".strip().capitalize()))
                    except TypeError:
                        print(str("não entendi, repita, por favor").strip().capitalize())
                    else:
                        break
def ordena(dados, fast_sort=False):
    """
    :param dados: estrutura de dados
    :param fast_sort: validador do algoritmo de busca
    :return: None
    """
    def particion(lista, low=0, high=len(dados)-1):
        pivo = lista[low]['id']
        i = low +1
        j = high
        while True:
            while i <= j and lista[i]['id'] <= pivo:
                i += 1
            while i <= j and lista[j]['id'] > pivo:
                j -= 1
            if i <= j:
                lista[i], lista[j] = lista[j], lista[i]
            else:
                break
        lista[low], lista[j] = lista[j], lista[low]
        return j

    def my_sort(lista, low=0, high=len(dados)-1):
        if low < high:
            pivo = particion(lista, low, high)
            my_sort(lista, low, pivo - 1)
            my_sort(lista, pivo + 1, high)



    if not fast_sort:
        dados = sorted(dados, key=lambda x: x['id'])
        return dados
    else:
        high = int(len(dados) - 1)
        my_sort(dados)

def cadastro(dados, order):
    meus_dados = {"nome": None,
                  "idade": None,
                  "CPF": None,
                  "telefone": None,
                  "id": None}
    while True:
        try:
            meus_dados["id"] = randint(0, 10000)
            for c in dados:
                while meus_dados["id"] == c["id"]:
                    meus_dados["id"] = randint(0, 10000)
            while True:
                try:
                    meus_dados["nome"] = str(input("digite o nome: ".strip().capitalize()))
                except TypeError:
                    print(str("não entendi, repita, por favor").strip().capitalize())
                else:
                    break
            meus_dados['idade'] = opc_("idade: ")
            meus_dados['CPF'] = opc_("CPF (somente números): ")
            for c in dados:
                while meus_dados["CPF"] == c["CPF"]:
                    print("CPF já cadastrado!!!")
                    meus_dados['CPF'] = opc_("CPF (somente números): ")
            meus_dados["telefone"] = opc_("telefone (somente números): ")
        except Exception as error:
            if not isinstance(meus_dados['nome'], str):
                print("nome inválido")
            elif not isinstance(meus_dados['idade'], int):
                print("idade inválida")
            elif not isinstance(meus_dados['CPF'], (float, int)):
                print(f"CPF inválido")
            elif not isinstance(meus_dados['telefone'], (float, int)):
                print("telefone inválida")
        else:
            break
    if not len(meus_dados):
        dados.append(meus_dados)
    elif len(meus_dados) and order == 1:
        if dados[0]["id"] > meus_dados["id"]:
            dados.insert(0, meus_dados)
        elif dados[-1]["id"] < meus_dados["id"]:
            dados.append(meus_dados)
    else:
        dados.append(meus_dados)

if __name__ == "__main__":
    data = [c for c in busca_data()]
    sorted_ = check_ordem(data)

    while True:
        print(
        "[1]Incluir dado: \n",
        "[2]Excluir dado: \n",
        "[3]Alterar dado: \n",
        "[4]Ordenar dado: \n",
        "[5]salvar dados: \n",
        "[6]Imprimir dados: \n",
        "[7]Buscar dados: \n",
        "[0]Sair...\n"
        )
        opc = -1
        while opc < 0 or opc > 7:
            opc = opc_("digite uma opção: ",
                       "Uma opção entre 1 e 7, por favor")

        if opc == 1:
            cadastro(data, sorted_)
        elif opc == 2:
            os.system('cls')
            imprimir(data)
            var = opc_("Digite o ID: ",
                       "não entendi, repita, por favor")
            res = buscar(data, ids=var)
            if res:
                print(f"posição: {res[0]}")
                for k, v in res[1]:
                    print(f"{k}: {v}")
            else:
                print("Esse dado não esta cadastrado: ")

        elif opc == 3:
            imprimir(data)
            var = opc_("Digite o ID: ",
                       "não entendi, repita, por favor")
            val = buscar(data, ids=var)
            while not val:
                var = opc_("Digite o ID: ",
                           "não entendi, repita, por favor")
                val = buscar(data, ids=var)
            for k, v in dict(val[1]).items():
                print(f"{k}: {v}")
            print("selecione o atributo do dado a ser alterado: \n"
                  "[1]->nome: \n"
                  "[2]->idade: \n"
                  "[3]->cpf: \n"
                  "[4]->telefone: ")
            atr = opc_("->")
            if atr == 1:
                alterar(data, ids= var, nome=True)
            elif atr == 2:
                alterar(data, ids= var, idade=True)
            elif atr == 3:
                alterar(data, ids=var, cpf=True)
            elif atr == 4:
                alterar(data, ids=var, telefone=True)

        elif opc == 4:
            if len(data) > 10:
                data = ordena(data)
            else:
                ordena(data, fast_sort=True)
            sorted_ = 1
            imprimir(data)
            print("Dados ordenados!!!")

        elif opc == 5:
            pass
        elif opc == 6:
            imprimir(data)

        elif opc == 7:
            if data:
                imprimir(data)
                print("Buscar por: \n"
                      "[1]->ID\n"
                      "[2]->CPF")
                opc = -1
                while opc < 1 or opc > 2:
                    var = opc_("->",
                              "digite 1 ou 2, por favor")
                if opc == 1:
                    var = opc_("Digite seu ID: ",
                               "não entendi, repita, por favor")
                    res = buscar(data, ids=var)
                    if res:
                        print(f"posição: {res[0]}")
                        for k, v in res[1]:
                            print(f"{k}: {v}")
                elif opc == 2:
                    var = opc_("Digite o CPF: ",
                               "não entendi, repita, por favor")
                    res = buscar(data, cpf=var)
                    if res:
                        print(f"posição: {res[0]}")
                        for k, v in res[1]:
                            print(f"{k}: {v}")
                else:
                    print("Esse dado não esta cadastrado!!! ")
            else:
                print("Não existe dados a serem buscados!!!")
        elif opc == 0:
            print("Saindo...")
            time.sleep(2)
            break
