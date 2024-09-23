"""
Funções são trechos de código usados para replicar determinada ação ao longo do
seu código!
Por padrão funções em python retornam None!
"""


def my_print(txt: str, num=5) -> None:
    print(f"{txt.center(num)}")


my_print('Daniel Brown', num=10)
