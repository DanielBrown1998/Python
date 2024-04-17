class Stack:

    def __init__(self):
        self.__stack = []

    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        self.__stack.pop()


class Fila:

    def __init__(self):
        self.__fila: dict = {}

    @property
    def fila(self):
        return {k: v for k, v in self.__fila.items()}

    @fila.setter
    def fila(self, val):
        if not isinstance(val, (list, tuple)):
            raise TypeError(f"o parâmetro {val} só aceita os tipo list e tuple")
        self.__fila: dict = {k: v for k, v in enumerate(val)}

    def put(self, val):
        self.__fila[len(self.__fila)] = val

    def get(self):
        if len(self.__fila) == 0:
            raise Exception("não há nada para remover")
        return self.__fila[0]

