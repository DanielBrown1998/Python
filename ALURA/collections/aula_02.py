from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def sacar(self, valor):
        if valor > self._saldo:
            return False
        self._saldo -= valor

    def depositar(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f"Titular: {self._codigo}, Saldo: {self._saldo}"
    
class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


conta16 = ContaCorrente(16)
conta16.depositar(1000)

conta17 = ContaPoupanca(17)
conta17.depositar(1000)


contas = [conta16, conta17]
for conta in contas:
    conta.passa_o_mes()
    print(conta)
    