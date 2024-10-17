from itertools import count

def gerador(lim: int):
    contador = count()
    for i in contador:
        if i >= lim:
            break
        yield i

