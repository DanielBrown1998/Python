def func_multi(*args: list[int]) -> int:
    total = 1
    for c in args:
        total *= c
    return total


def odd_or_even(num: int) -> str:
    if num % 2 == 0:
        return f"{num} é par"
    return f"{num} é ímpar"


lista = list([c for c in range(1, 50) if c % 2 == 0 or c % 5 == 0])
for c in lista:
    print(odd_or_even(c))
print(f"A multiplicação de todos os elementos da lista é: \n{func_multi(*lista)}")
