from typing import List
from collections import namedtuple


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

box = namedtuple('box', 'have_key')


def find_key(boxs: List[box], index: int = 0) -> box:
    #  base case
    if len(boxs) <= index:
        return box(False)

    Box = boxs[index]
    if Box.have_key:
        return Box

    index += 1
    return find_key(boxs, index)


if __name__ == '__main__':
    boxs: List[box] = [
        box(False), box(False), box(False),
        box(False), box(False), box(False),
        box(False), box(True), box(False)
    ]
    print(find_key(boxs))
