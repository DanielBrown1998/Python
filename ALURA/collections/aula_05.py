
from random import randint

A = set()
B = set()
iterações = 0
a, b = 0, 0
while a < 50 or b < 0:
    iterações += 1
    num = randint(1, 100)
    num2 = randint(1, 100)
    if num not in A:
        a += 1
    if num2 not in B:
        b += 1
    A.add(num)   
    B.add(num2)

print(A)
print(B)
print(iterações)

print(A & B) # AND
print(A | B) # OR
print(A - B) # tudo que está somente em A
print(B - A) # tudo que está somente em B
print((A - B) | (B - A)) # XOR
print(A ^ B) # XOR
