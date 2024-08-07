import os
from time import sleep

import exercicio10_json as data


class Person:

    def __init__(self, *,
                 age=None, name=None,
                 occupation=None, register=None,
                 function=None, cellphone=None):

        self.age: str | None = age
        self.name: str | None = name
        self.occupation: str | None = occupation
        self.register: str | None = register
        self.function: str | None = function
        self.cellphone: str | None = cellphone


if __name__ == '__main__':
    while True:
        print("""
        COMANDOS
    1: ler dados
    2: inserir novos dados
    3: sair
        """)
        opc = input("Digite a opção desejada: ").strip().lower()
        while not opc.isnumeric() or int(opc) not in [1, 2, 3]:
            if not opc.isnumeric():
                print('digite um número...')
            else:
                print('opção inválida...')
            opc = input("Digite a opção desejada: ").strip().lower()

        if int(opc) == 1:
            attr = data.load_attr()
            im = Person(**attr)
            print('Verificando...')
            sleep(1)
            print('Ok...')
            print(*[f"{key}: {value}" for key, value in im.__dict__.items()], sep="\n")

        elif int(opc) == 2:
            os.system('cls')
            you = Person()
            attr = you.__dict__
            for key in attr.keys():
                value = input(f'informe (o/a) novo {key}: ').strip().lower()
                attr[key] = value
            data.save_json(attr)
        else:
            break

