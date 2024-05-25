

class Ponto:
    def __init__(self, x, y, z=None):
        import math
        self.x = x
        self.y = y
        self.z = z
        self.modulo = math.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))

    def __str__(self):  # representação de string para o objeto

        if self.z is None:
            return f"({self.x!s}, {self.y!s})"
        else:
            return f"({self.x!s}, {self.y!s}, {self.z!s})"

    def __repr__(self):

        if self.z is None:
            return f"{type(self).__name__}: x={self.x!r}, y={self.y!r}"
        else:
            return f"{type(self).__name__}: x={self.x!r}, y={self.y!r}, z={self.z!r}"

    def __add__(self, other):

        if self.z is None:
            return Ponto(self.x + other.x, self.y + other.y)
        else:
            return Ponto(self.x + other.x, self.y + other.y, self.z + other.z)

    def __gt__(self, other):

        if type(other).__name__ != type(self).__name__:
            raise TypeError(f"{other} not is Ponto")
        if self.modulo > other.modulo:
            return True
        return False

    def __ge__(self, other):

        if type(other).__name__ != type(self).__name__:
            raise TypeError(f"{other} not is Ponto")
        if self.modulo >= other.modulo:
            return True
        return False

    def __lt__(self, other):

        if type(other).__name__ != type(self).__name__:
            raise TypeError(f"{other} not is Ponto")
        if self.modulo < other.modulo:
            return True
        return False

    def __le__(self, other):

        if type(other).__name__ != type(self).__name__:
            raise TypeError(f"{other} not is Ponto")
        if self.modulo <= other.modulo:
            return True
        return False

    def __eq__(self, other):
        if type(other).__name__ != type(self).__name__:
            raise TypeError(f"{other} not is Ponto")
        if self.modulo == other.modulo:
            return True
        return False


p1 = Ponto(0, 0, 0)
p2 = Ponto(1, 1, 1,)
p3 = p1 + p2
print(type(p3).__name__)
print(p2 > p1)
print(p2 == p1)
print(p3)
