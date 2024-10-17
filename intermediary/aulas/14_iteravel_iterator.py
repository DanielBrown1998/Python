
iterable = [c for c in range(10)]
iterator = iter(iterable)
while True:
    try:
        print(next(iterator), end=' ')
    except StopIteration:
        print()
        break
    