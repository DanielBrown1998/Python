
def log():

    with open('log.txt', 'a', encoding='utf-8') as log_text:
        with open(r'./lista_atual.txt', 'r', encoding='utf-8') as lista:
            text = ''
            for item in lista.readlines():
                text += str(item).replace('\n', '-')

            log_text.write(
                f"{text}\n"
            )


def add(element):

    with open(r'./lista_atual.txt', 'r', encoding='utf-8') as lista:
        with open(r'./lista_anterior.txt', 'w', encoding='utf-8') as anterior:
            my_list = lista.readlines()
            log()
            anterior.writelines(
                my_list
            )

    with open(r'./lista_atual.txt', 'a', encoding='utf-8') as lista:
        lista.write(f"{element}\n")

    print(f'{element} adicionado')


def listar():
    with open(r'./lista_atual.txt', 'r', encoding='utf-8') as file:
        print(*file.read(), end='\n')


def refazer():
    with open(r'./lista_atual.txt', 'r', encoding='utf-8') as actual:
        nova_lista_anterior = actual.readlines()
        log()

    with open(r'./lista_anterior.txt', 'r', encoding='utf-8') as lista:
        with open(r'./lista_atual.txt', 'w', encoding='utf-8') as actual:
            actual.writelines(
                lista.readlines()
            )

    with open(r'./lista_anterior.txt', 'w', encoding='utf-8') as lista:
        lista.writelines(
            nova_lista_anterior
        )


def desfazer():

    with open(r'./lista_atual.txt', 'r', encoding='utf-8') as lista:
        with open(r'./lista_anterior.txt', 'w', encoding='utf-8') as anterior:
            anterior.writelines(
                lista.readlines()
            )
    with open(r'./lista_atual.txt', 'w', encoding='utf-8') as lista:
        with open('log.txt', 'r', encoding='utf-8') as log_text:
            for c in log_text.readlines():
                text = c
                c = None
            lista.writelines(
                '\n'.join(text.split('-'))
            )


while True:
    print(
        """
        COMANDOS:
0: sair
1: listar
2: refazer
3: desfazer
    """
    )
    comando = input('digite um comando: ').strip().lower()
    if comando not in ['listar', 'refazer', 'desfazer']:
        add(comando)
        continue
    elif comando == 'listar':
        listar()
        continue
    elif comando == 'refazer':
        refazer()
        continue
    elif comando == 'desfazer':
        desfazer()
        listar()
        continue
    elif comando == 'sair':
        break

