#generator são funções que conseguem pausar
#yield pausa a execução do código e volta para a próxima iteração
#o yield é como um return, mas ao invés de terminar a função, ele
#pausa a execução e retorna o valor
#quando a função é chamada novamente, ela continua a partir da próxima iteração
#o yield pode ser usado para criar iteradores personalizados
#o yield é uma forma de criar iteradores sem a necessidade de criar uma classe


def informative():
    yield 'executando o Generator: '

def generator(start, stop, step=1):


    if start > stop and step > 0 and step != 1:
        raise ValueError('step must be negative')

    yield from informative()

    if start > stop:
        step = -1
        while start > stop:
            yield start
            start += step
    else:
        while start < stop:
            yield start
            start += step


gen = generator(10, 0)
while True:
    try:
        print(next(gen), end=' ')
    except StopIteration:
        break

