class MinhaSoma:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


@MinhaSoma
def sum_n(*args):
    return sum([c for c in args])

my_sum = sum_n(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(my_sum)
