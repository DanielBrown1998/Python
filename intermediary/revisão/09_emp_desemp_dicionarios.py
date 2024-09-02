lista = [
    {'nome': 'João', 'idade': 25, 'sexo': 'M'},
    {'nome': 'Maria', 'idade': 27, 'sexo': 'F'},
    {'nome': 'José', 'idade': 30, 'sexo': 'M'},
    {'nome': 'Ana', 'idade': 22, 'sexo': 'F'},
]


def read_arg(func):
    
    def func(*args):
        if len(args) == 0:
            print('Nenhum argumento foi passado')
            return
        lista = sorted([item for item in args], key= lambda x: x['idade'])
        return lista
    return func

@read_arg
def exp_dict(*args):
    ...


print(exp_dict(*lista))

