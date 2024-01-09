"""
retorno de funções (return)

args: argumentos não nomeados
empacotamento e desempacotameto: *args -> <class 'tuple'>
"""


def my_sum(*args: float) -> float:
    return sum(args)



print(f"a soma dos 100 primeiros termos de uma P.A \nsendo o primeiro \
e a razão unitários é : {my_sum(*[c for c in range(101)])}")
