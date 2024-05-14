def decompose(n):
    num: int = n**2
    quad: list = []
    more: int = 0
    for c in range(n-1, 0, -1):
        more += c**2
        quad.append(c)
        if more > num:
            quad.pop()
            more -= c**2
    quad.reverse()
    return quad


print(decompose(50))
print(decompose(8))
