from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, numero, titular, saldo, limite = 0) -> None:
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.codigo_banco = "001"

    @abstractmethod
    def sacar(self, valor: float) -> float | None:
        pass
    


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo) -> None:
        super().__init__(numero, titular, saldo)

    def sacar(self, valor: float) -> float | None:
        if self.saldo < valor or valor < 0:
            return 
        self.saldo -= valor
        return self.saldo
    
    def deposita(self, valor: float) -> float | None:
        if valor < 0:
            return 
        self.saldo += valor
        return self.saldo

class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo, limite=100) -> None:
        super().__init__(numero, titular, saldo, limite)
        

    def sacar(self, valor: float) -> float | None:
        if self.saldo  + self.limite < valor or valor < 0:
            return 
        self.saldo -= valor
        if self.saldo < 0:
            self.limite += self.saldo            
        return self.saldo, self.limite
        

    def depositar(self, valor: float) -> float | None:
        if valor < 0:
            return
        if self.saldo < 0:
            valor += self.saldo
            self.limite -= self.saldo
            self.saldo += valor
        else:
            self.saldo += valor

        return self.saldo, self.limite
    

class Pessoa(ABC):
    def __init__(self, nome, cpf, idade):
        self._nome = nome
        self._cpf = cpf
        self._idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, cpf, idade, conta):
        super().__init__(nome, cpf, idade)
        self._conta = conta
        if self._conta == 1:
            self._conta = Conta(self._cpf, self._nome, 0)
        else:
            self._conta = ContaPoupanca(self._cpf, self._nome, 0) 

