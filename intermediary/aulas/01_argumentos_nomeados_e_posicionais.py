#argumentos nomeados e  não nomeados

TAM: int = 10

def func(func: function, y=0, **kwargs) -> float | int :
    x = func()
    return x + y
k = 2
soma = [func(lambda: c**k, e+1) for e, c in enumerate(range(TAM, 0, -1))]
print(*soma ,sep='\n')
