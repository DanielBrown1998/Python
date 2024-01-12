
def double(n: float) -> float:
    return 2 * n


def quad(n: float) -> float:
    return 2 * double(n)


def multiplos_num(function):
    def resp(msg: str, n: float) -> str:
        return (f"{msg}"
                f"{function(n)}"
                )
    return resp


num = 10
num_2 = multiplos_num(double)
print(f'{num_2(f"O dobro de {num} é ", num)}')
num_3 = multiplos_num(lambda x: 3*x)
print(f'{num_3(f"O triplo de {num} é ", num)}')
num_4 = multiplos_num(quad)
print(f'{num_4(f"O quádruplo de {num} é ", num)}')
