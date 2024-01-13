"""
1: Argumentos posicionais e argumentos nomeados em funções python
2: Argumentos posionais sempre vêm à frente de argumentos nomeados
3: Argumentos default são predefinidos nos parâmetros da função
"""


def soma(x: float, y: float, z: float = None) -> str:
    if z is None:
        return f"x,y,z e IR³ | x+y+z = {x+y}"
    else:
        return f"x,y,z e IR³ | x+y+z = {x+y+z}"


print(soma(4, 5))
