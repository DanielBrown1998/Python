def func(param1, param2):
    def func_int():
        return f"{param1}{param2}"

    return func_int


exp_1 = func('ok, ', 'funciona!')
exp_2 = func('Daniel ', 'Brown')

print(exp_2(), exp_1(), sep='\n')
