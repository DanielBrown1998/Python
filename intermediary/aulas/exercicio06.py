def soma(x, y):
    return x + y


def mult(x, y):
    return x*y


def exec_func(funcao, x):
    def resp(y):
        return funcao(x, y)
    return resp


soma_cinco = exec_func(soma, 5)
multiplica_dez = exec_func(mult, 10)
print(soma_cinco(5), multiplica_dez(10))
