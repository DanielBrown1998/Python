class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._coord = x, y

    def __repr__(self):
        class_name = self.__class__.__name__
        #class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'
