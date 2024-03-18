import numpy as np
from math import ceil


log_2 = np.log(2)
error = 10 ** (-9)
inicio = 2
fim = 3


def f(x: float):
    return x*np.log(x) - 1


# com calculo de limite de iterações
def bissec_with_limit(a: float, b: float, e: float) -> tuple:
    iteracoes = ceil((np.log(abs(a - b)) - np.log(e)) / log_2)
    medio = 0
    for iter_ in range(iteracoes):
        medio = (a+b)/2
        if f(a)*f(medio) < 0:
            b = medio
        else:
            a = medio

    return iteracoes, medio


# sem calculo de limite de iterações
def bissec_no_limit(a: float, b: float, e: float) -> tuple:
    i, medio = 0, 0
    while True:
        medio = (a+b)/2
        if f(a)*f(medio) < 0:
            b = medio
        else:
            a = medio
        i += 1
        if abs(a-b) < e:
            return i, medio


print(bissec_no_limit(inicio, fim, error))
# print(bissec_with_limit(inicio, fim, error))
