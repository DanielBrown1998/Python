import numpy as np

array = ((i, j) for i in range(3) for j in range(3))

while True:
    try:
        print(next(array))
    except StopIteration:
        break
