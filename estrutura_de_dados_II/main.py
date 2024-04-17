# estrutura de de dados II
from pathlib import Path


file_dir = str(Path(__file__).parent / 'arquivo.txt')


class NoTree:

    def __init__(self, no_ant, no_pos, no):
        self.no: str = no
        self.no_lf: NoTree = no_ant
        self.no_rg: NoTree = no_pos


class Tree:
    ...


def main(func):
    def intern_func(*args):
        with open(file_dir, 'r', encoding='utf-8') as file:
            lista = file.readlines()
        result = func(lista)
        # print(result)
        # todo here...
        return result
    return intern_func


@main
def execute(lista: list):
    # todo here to...

    return lista


if __name__ == '__main__':
    execute()

