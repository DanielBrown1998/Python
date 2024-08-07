def exec_decorator(function):
    def intern_decorator(*args, **kwargs):
        for arg in args:
            is_string(arg)
        return function(*args, **kwargs)
    return intern_decorator


# def decorator(func):
#     return func


# @decorator(exec)
@exec_decorator
def invert_string(string):
    return string[::-1]


def is_string(string: str):
    if not isinstance(string, str):
        raise TypeError(f"'{string}' deve ser uma string")


print(invert_string.__name__)
my_str_invert = invert_string('Daniel')
print(my_str_invert)
