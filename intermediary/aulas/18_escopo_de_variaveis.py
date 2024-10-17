num: int = 10

def fora():
    num: int = 5
    print(locals())
    def dentro():
        nonlocal num
        num = 2
        print(locals())
    dentro()
    print(locals())

fora()
print(__annotations__)


def concatenar(string_initial):
    valor_inicial = string_initial
    def interna(valor_a_concatenar):
        nonlocal valor_inicial
        valor_inicial += valor_a_concatenar
    
    return interna

a = concatenar('a')
a('b')
a('c')
print(a.__closure__[0].cell_contents)
