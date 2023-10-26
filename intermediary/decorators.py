def is_string(param):
    if isinstance(param, str) is False:
        raise TypeError(f'{param} não é uma string')


def criar_funcao(func):
    def interno(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print(f'O seu resultado foi {result}')
        print('Ok, agora você foi decarada')
        return result
    return interno


@criar_funcao
def inverter_str(string):
    return string[::-1]


normal = 'Luiz'

inverso = inverter_str(normal)
print(inverso)
 