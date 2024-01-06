
# exemplo de uma função não recursiva
def fatorial(n: int) -> int:
    c = 0
    fat = 1
    while True:
        fat *= (n-c)
        if n-c == 1:
            break
        c += 1
    return fat


def fatorial_recursivo(n: int) -> int:
    if n == 1:
        return n
    else:
        return n*fatorial_recursivo(n-1)


print(int(fatorial_recursivo(5)) == float(fatorial(5)))


