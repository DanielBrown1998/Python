import time
game = list([['     ', '     ', '     '],
             ['     ', '     ', '     '],
             ['     ', '     ', '     ']])


def validador(*game):
    # chocador de linha
    for c in game:
        if c.count('  X  ') == 3:
            return 1
        elif c.count('  O  ') == 3:
            return 2
    # checador de coluna
    for coluna in range(3):
        if game[0][coluna] == game[1][coluna] == game[2][coluna]:
            if game[0][coluna] == '  X  ':
                return 1
            elif game[0][coluna] == '  O  ':
                return 2
    #checador de diagonal principal:
    if game[0][0] == game[1][1] == game[2][2]:
        if game[1][1] == '  X  ':
            return 1
        elif game[1][1] == '  O  ':
            return 2
    #checador de diagonal secundária:
    elif game[0][2] == game[1][1] == game[2][0]:
        if game[1][1] == '  X  ':
            return 1
        elif game[1][1] == '  O  ':
            return 2

    return 0


def player(x='Digite seu movimento: ', pc=True):
    if pc is False:
        n = input(x)
        while n.isalpha() or n.isspace() or n in '':
            n = input(x)
        while int(n) not in [v for v in range(9)]:
            n = input(x)
            while n.isalpha() or n.isspace() or n in'':
                n = input(x)
        shape = list([(0, 0), (0, 1), (0, 2),
                      (1, 0), (1, 1), (1, 2),
                      (2, 0), (2, 1), (2, 2)])
        return shape[int(n)]
    else:
        from random import randint
        n = randint(0, 9)
        while n not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            n = randint(0, 9)
        shape = list([(0, 0), (0, 1), (0, 2),
                      (1, 0), (1, 1), (1, 2),
                      (2, 0), (2, 1), (2, 2)])
        return shape[n]


def jogada(opc):
    x = player(pc=opc)
    while str(game[x[0]][x[1]]) not in '     ':
        if opc is True:
            x = player(pc=opc)
        else:
            print('opção já preenchida, repita.')
            x = player(pc=opc)
    if opc is True:
        game[x[0]][x[1]] = '  X  '
    else:
        game[x[0]][x[1]] = '  O  '


#atualiza o tabuleiro
def tabuleiro(*lista):
    # plotando o tabuleiro
    for i in lista:
        print('|', end='')
        for j in i: print(f'  {j}  ', end='|')
        print('\n', '-'*30)


# código principal

print('essas são suas opções')
tabuleiro(*list([['  0  ', '  1  ', '  2  '],
                ['  3  ', '  4  ', '  5  '],
                ['  6  ', '  7  ', '  8  ']]))


print('O computador irá começar: ')
time.sleep(1)
cont = 1
game[1][1] = str('  X  ')
tabuleiro(*game)


time.sleep(1)
for c in range(8):
    time.sleep(1)
    if c % 2 == 0:
        print('sua vez')
        jogada(False)
    else:
        print('o computador está jogando... ')
        jogada(True)
        time.sleep(1)
    tabuleiro(*game)
    if validador(*game) == 0:
        continue
    elif validador(*game) == 0 and c == 7:
        print('Deu \033[34mVELHA\033[m!')
    elif validador(*game) == 2:
        print('\033[32mVocê Ganhou!!!\033[m')
        break
    elif validador(*game) == 1:
        print('\033[31mVocê Perdeu!!!\033[m')
        break
time.sleep(1)
print('FIM DE JOGO!!!')
