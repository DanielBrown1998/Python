#generator são funções que conseguem pausar

def generator(stop, start=0, step=1):
    if start < stop:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start -= step

generate = (c for c in generator(10))

#yield pausa a execução do código e volta para a próxima iteração
#o yield é como um return, mas ao invés de terminar a função, ele
#pausa a execução e retorna o valor
#quando a função é chamada novamente, ela continua a partir da próxima iteração
#o yield pode ser usado para criar iteradores personalizados
#o yield é uma forma de criar iteradores sem a necessidade de criar uma classe