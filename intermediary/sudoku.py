import random


def ler_matriz(*args):
    for line in args:
        for pos, element in enumerate(line):
            if pos != len(line) - 1:
                print(element, end=' ')
            else:
                print(element)


def validador_sudoku(*args):
    print("checando linhas...")
    for line in args:
        for c in line:
            if line.count(c) != 1:
                return 0

    print("checando as colunas...")
    for line in range(9):
        colums = (args[col][line] for col in range(9))
        while True:
            try:
                lista = list([])
                element_column = colums.__next__()
                if element_column in lista:
                    return 0
                else:
                    lista.append(element_column)
            except StopIteration:
                break
    print("checando sessões...")
    sessao = ([], [], [], [], [], [], [], [], [])
    for e, row in enumerate(args):
        if e < 3:
            for item in row[:3]:
                sessao[0].append(item)
            for item in row[3:6]:
                sessao[1].append(item)
            for item in row[6:]:
                sessao[2].append(item)
        elif 3 <= e < 6:
            for item in row[:3]:
                sessao[3].append(item)
            for item in row[3:6]:
                sessao[4].append(item)
            for item in row[6:]:
                sessao[5].append(item)
        else:
            for item in row[:3]:
                sessao[6].append(item)
            for item in row[3:6]:
                sessao[7].append(item)
            for item in row[6:]:
                sessao[8].append(item)
    sessao_lite = (c for c in sessao)
    del sessao
    for line in sessao_lite:
        print("checando...", *line)
        for c in line:
            if line.count(c) != 1:
                return 0

    print("\nTudo Ok!")
    return 1


matriz = [[2, 9, 5, 7, 4, 3, 8, 6, 1],
          [4, 3, 1, 8, 6, 5, 9, 2, 7],
          [8, 7, 6, 1, 9, 2, 5, 4, 3],
          [3, 8, 7, 4, 5, 9, 2, 1, 6],
          [6, 1, 2, 3, 8, 7, 4, 9, 5],
          [5, 4, 9, 2, 1, 6, 7, 3, 8],
          [7, 6, 3, 5, 2, 4, 1, 8, 9],
          [9, 2, 8, 6, 7, 1, 3, 5, 4],
          [1, 5, 4, 9, 3, 8, 6, 7, 2]]


ler_matriz(*matriz)
msg1 = "\033[32mEssa matriz pode ser um tabuleiro de sudoku!!!\033[m"
msg2 = "Essa matriz \033[31mNÃO\033[m pode ser um tabuleiro de sudoku!!!"
print(msg1 if validador_sudoku(*matriz) == 1 else msg2)
