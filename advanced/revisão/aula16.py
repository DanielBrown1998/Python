#metaclasses

from typing import Any


def myrepr(self):
    return f"{type(self).__name__} {self.__dict__}"


class Meta(type):

    # constrói a classe
    def __new__(mcs, name, bases, dct):
        print('my new')
        cls = super().__new__(mcs, name, bases, dct)
        cls.__repr__ = myrepr

        if 'escrever' not in cls.__dict__ or \
            not callable(cls.__dict__['escrever']):  #isso é para garantir que seja um método
            raise NotImplementedError('implemente o método escrever!')

        return cls
    

    # trata da instância 
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        instancia = super().__call__(*args, **kwds)
        if 'nome' not in instancia.__dict__ or \
            callable(self.__dict__['nome']):  # verifica se é um método
            raise NotImplementedError('crie o atributo instancia')
        print(f"{self.__dict__['nome']} was add")
        return instancia
    
    

class Pessoa(object, metaclass=Meta):

    # constrói a instância
    def __new__(cls, *args, **kwargs) :
        print("new")
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome) -> None:
        print('init')
        self.nome = nome

    def escrever(self) -> None:
        print(f'{self.nome} está escrevendo')


eu  = Pessoa('Daniel')
print(eu.__repr__())