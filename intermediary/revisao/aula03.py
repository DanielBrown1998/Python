"""
- Escopo de funções em Python
- Escopo significa o local onde aguele código pode atingir
- Existe o escopo global e local
- O escopo global pe o escopo onde to-do o código é alcançável.
- O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados
"""
y = 0


def escopo(arg: float) -> None:
    global y  # altera a váriavel global y
    y = arg
    x = y
    print(f"dentro da função {y=}")
    print(f"na função {x=}")


print(f"antes da função: {y=}")
escopo(5)
print(f"depois da função: {y=}")
