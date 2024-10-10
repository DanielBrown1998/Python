

def decorator(func):
    def intern(*args):
        for item in args:
            if not isinstance(item, (int, float)):
                raise ValueError("Only integers or floats are allowed")
        print("Before calling the function")
        return func(*args)
    return intern

@decorator
def soma(a, b):
    print(f'I`ll sum this numbers: {a}, {b}')
    return a + b


print(soma(1, 2))




