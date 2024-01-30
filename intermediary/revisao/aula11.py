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


num = gen(10, 1, 2)
print(*[c for c in num])
