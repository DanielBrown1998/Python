from typing import List

def decorator_factory(values: List[int]):    
    def factory_function(func):
        for item in values:
            if not isinstance(item, (int)):
                raise ValueError("Only lists of integers are allowed")
        def inner_function(*args, **kwargs):
            nonlocal values
            values_temp = []
            for item in args:
                if not isinstance(item, (int)):
                    del values_temp
                    raise ValueError("Only params of integers are allowed")
                if item not in values:
                    values_temp.append(item)
            values += values_temp
            print("Before calling the function")
            return func(*args, lista = values)
        return inner_function

    return factory_function

lista = [c for c in range(10)]
@decorator_factory(lista)
def add_lista(*args, lista:List[int] | None = None) -> List[int]:
    return sorted(lista)


lista = add_lista(1, 52, 33, 4, 15, 6, 12, 13, 51, lista=lista)
print(lista)