from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, msg) -> None:
        self.mensagem = msg

    @abstractmethod
    def send(self) -> bool:
        ...

class Email(Notificacao):
    def send(self):
        print("Enviando a mensagem ->", self.mensagem)
