# abstract class
from abc import ABC, abstractmethod


class AbstractFoo(ABC):

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def method_abstract(self):
        raise NotImplementedError("Implemente-me")

    @property
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, value):
        self._name = value


class Foo(AbstractFoo):

    def method_abstract(self):
        print("method_abstract created")

    @AbstractFoo.name.setter
    def name(self, value):
        self._name = value


