import os
import time

# verificando a existencia das pastas
for _, _, files in os.walk('.'):
    if "tarefas.txt" not in files:
        with open(r"tarefas.txt", 'w', encoding='utf-8') as file:
            pass
    if "excluidos.txt" not in files:
        with open(r"excluidos.txt", 'w', encoding='utf-8') as file:
            pass

# inserindo os dados

with open("tarefas.txt", "r", encoding="utf-8") as file:
    tarefas = file.readlines()

with open("excluidos.txt", "r", encoding="utf-8") as file:
    excluidos = file.readlines()

# print(tarefas)


def refatorar(lista_origem, lista_destino, backup=True):
    if not lista_origem.__len__():
        if backup:
            print('Não há itens a serem recuperados!')
        else:
            print('Não há itens a serem excluídos!')
    else:
        if backup:
            print(f"{lista_origem[-1]}".replace('\n', ''), "recuperado com sucesso!")
        else:
            print(f"{lista_origem[-1]}".replace('\n', ''), "excluído com sucesso!")
        lista_destino.append(lista_origem[-1])
        lista_origem.pop()


comandos = ["listar", "desfazer", "refazer"]

while True:
    print("\033[31mPara sair digite: sair\033[m")
    print("\033[32mCOMANDOS:\033[m ", end='')
    print(*comandos, sep=',')
    opc = input("Selecione um comando ou digite: ").lower().strip()
    while opc.isspace() or opc == '':
        print("não entendi, repita, por favor!!!")
        opc = input("Selecione um comando ou digite: ").lower().strip()

    if opc == 'sair':
        print('Saindo...')
        time.sleep(1)
        break
    elif opc == 'clear':
        os.system('cls')

    elif opc not in comandos:
        if opc in tarefas:
            print(f"{opc} já está na lista!")
            print("TAREFAS: ")
            print(*tarefas)
        else:
            tarefas.append(f"{opc}\n")
            print(f'{opc} foi adicionado com sucesso!')
        continue
    else:
        if opc == "listar":
            if not tarefas.__len__():
                print('Não há itens a serem listados!')
            else:
                print("TAREFAS: ")
                print(*tarefas)
            continue

        elif opc == "desfazer":
            refatorar(tarefas, excluidos, backup=False)
            continue

        elif opc == 'refazer':
            refatorar(excluidos, tarefas)
            continue

# salvando as listas

with open("tarefas.txt", "w", encoding="utf-8") as file:
    file.writelines([c for c in tarefas])

with open("excluidos.txt", "w", encoding="utf-8") as file:
    file.writelines([c for c in excluidos])
