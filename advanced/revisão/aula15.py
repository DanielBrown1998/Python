from typing import Any


class Multiplicar:
    def __init__(self, func):
        self.func = func


    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(args, kwds)
        return self.func(*args, **kwds)


@Multiplicar
def soma(x, y):
    return x + y

dois_mais_dois = soma(2, 2)
print(dois_mais_dois)
