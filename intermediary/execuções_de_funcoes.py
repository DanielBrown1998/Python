def soma(x, y=0):
    return x + y


def mult(x, y=1):
    return x*y


def exec(func, x):
    intern = lambda y: func(x, y)
    # def intern(y):
    #     return revisao(x, y)
    return intern


sum_with_five = exec(soma, 5)
mult_with_ten = exec(mult, 10)

print(sum_with_five(10), mult_with_ten(5))
