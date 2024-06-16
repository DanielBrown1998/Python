def f(x: float):
    from math import e
    return (x**3)*(e**x)


def trapezio_simples(lim_inf: int, lim_sup: int) -> float:

    """
    :param lim_inf: menor valor do intervalo
    :param lim_sup: maior valor do intervalo
    :return: o valor da integral da funçao passada
    """

    h = lim_sup - lim_inf
    return round(h/2*(f(lim_sup) + f(lim_inf)), 2)


def trapezio_composto(lim_inf: float, lim_sup: float, n: int) -> float:

    """
    :param lim_inf: menor valor do intervalo
    :param lim_sup: maior valor do intervalo
    :param n: número de subdivisões
    :return: o valor da integral de uma função
    """

    h = round((lim_sup - lim_inf)/n, 1)

    print(f"limites: [{lim_inf}, {lim_sup}]\nsubdivisões: {n}")
    dominio: list = []
    x = lim_inf
    while x < lim_sup:
        dominio.append(round(x, 1))
        x += h
    print('Domínio:')
    print(*dominio)

    imagem: list = [round(f(x), 5) for x in dominio]
    print('Imagem:')
    print(*imagem)

    integral = 0
    for y in imagem[1:len(imagem)-1]:
        integral += 2*y
    else:
        integral += f(imagem[0]) + f(imagem[len(imagem)-1])

    return round(integral*h/2, 2)


if __name__ == '__main__':
    limite_inferior = 0
    limite_superior = 1
    print(f'O valor da integral de f(x) através do trapézio simples é '
          f'{trapezio_simples(0, 1)}'
          )
    print(f'O valor da integral de f(x) através do trapézio composto é '
          f'{trapezio_composto(0, 1, 10)}'
          )
