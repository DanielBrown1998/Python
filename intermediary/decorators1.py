
def decoradora(func):
    print('Decoradora 1')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        res = func(*args, **kwargs)
        return res
    return aninhada


@decoradora
def soma(x, y):
    print(f'nome real da função: {soma.__name__}')
    return x + y


sum_5_10 = soma(5, 10)
print(sum_5_10)
