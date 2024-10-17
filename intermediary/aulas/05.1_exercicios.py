def operacao(num):
    def func(mult):
        return num * mult
    return func

num_base_x_1 = 2
num_base = operacao(num_base_x_1)

num_base_x_2 = num_base(2)
num_base_x_3 = num_base(3)
num_base_x_4 = num_base(4)

print(num_base_x_1, num_base_x_2, num_base_x_3, num_base_x_4)
