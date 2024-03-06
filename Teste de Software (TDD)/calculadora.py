def soma(x, y) -> None | int | float:
    if isnumber(x) and isnumber(y):
        return x + y


def mult(x, y) -> None | int | float:
    if isnumber(x) and isnumber(y):
        return x*y


def sub(x, y) -> None | float:
    """
    :param x: dividendo
    :param y: divisor
    :return: x/y | y != 0
    """
    if isnumber(x) and isnumber(y) and y != 0:
        return x/y


def isnumber(num):
    if isinstance(num, (int, float)):
        return True
    return False
