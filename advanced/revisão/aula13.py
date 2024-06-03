def add_repr(cls):
    def my_repr(self):
        name_cls = self.__class__.__name__
        cls_dict = self.__dict__
        cls_repr = f"{name_cls} -> {cls_dict}"
        return cls_repr

    cls.__repr__ = my_repr
    return cls


def decora(func):
    def intern(self, *args, **kwargs):
        result = None
        if hasattr(self, 'liga'):
            result = func(self, *args, **kwargs)
        return result
    return intern


@add_repr
class Time:
    def __init__(self, name=None):
        self.name = name
        
    @decora
    def liga(self):
        return f"O {self.__class__.__name__} joga o Brasileirão!"


flamengo = Time('Flamengo')

print(flamengo, flamengo.liga() if flamengo.liga() is not None else 'sem liga', sep='\n')
