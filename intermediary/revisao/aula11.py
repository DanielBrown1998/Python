import sys

import aula10


def gen(stop: int, start: int = 0, step: int = 1) -> int:
    """
    this function works like range
    :rtype: list | tuple
    """
    while start < stop:
        yield start
        start += step
    else:
        return start


print(__name__)
print(*sys.path, sep='\n')
