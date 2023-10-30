import time
from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0)->None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float)->float:
        pass

    def depositar(self, valor: float)->float:
        self.saldo += valor
        self.detalhes(msg=f"Depositando: R${valor:.2f}")
        return self.saldo

    def detalhes(self, limite: float = 0, msg: str ='')->None:
        if self.saldo < limite:
            print(f"\t{msg} \n\tSaldo restante: R$\033[31m-{self.saldo:.2f}\033[m")
        else:
            print(f"\t{msg} \n\tSaldo restante: R${self.saldo:.2f}")
        time.sleep(.5)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"{self.agencia!r}, {self.conta!r}, {self.saldo!r}"
        return f"{class_name}{attrs}"
class ContaPoupanca(Conta):
    def sacar(self, valor: float)->float:
        valor_pos_sacar = self.saldo - valor
        print(f"\tSacando... R${valor:.2f}\n")
        if valor_pos_sacar >= 0:
            self.saldo -= valor
            self.detalhes(msg=f"Operação realizada:")
            return self.saldo
        print("\tNão foi possível sacar o valor pedido")
        self.detalhes(msg="negado")
        return self.saldo
class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int , saldo: float = 0, limite: float = 0)->None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite
        self.saldo += self.limite

    def sacar(self, valor: float)->float:
        valor_pos_sacar = self.saldo - valor
        limite_max = -self.limite
        print(f"\tSacando... R${valor:.2f}")
        if valor_pos_sacar >= limite_max:
            self.saldo -= valor
            self.detalhes(self.limite, f"Operação realizada:")
            if self.saldo < self.limite:
                print("\tVocê está utilizando o limite da sua conta \n\t"
                      "e está sujeito a juros e custos adicionais!!!\n")
            return self.saldo
        print("\tNão foi possível sacar o valor pedido")
        self.detalhes(msg="negado")
        return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"\nagency: {self.agencia!r} \nconta: {self.conta!r}\n\
saldo: {self.saldo=!r} \nlimite: {self.limite=!r}"
        return f"{class_name}:  {attrs}"
class Pessoa:
    def __init__(self, name: str, age: int)->None:
        self.nome: str = name
        self.idade: int = age

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, name: str):
        self._nome = name

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, age: int):
        self._idade= age
class Cliente(Pessoa):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.conta: Conta | None = None

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"{self.nome=!r}, {self.idade=!r}"
        return f"{class_name}: {attrs}"

class Bank:
    def __init__(self, agencias: list[int] | None = None,
                 contas: list[Conta] | None = None,
                 clientes: list[Cliente] | None = None)->None:
        self.agencias = agencias or [c for c in range(1000, 10000)]
        self.clientes = clientes or []
        self.contas = contas or []

    def check_agency(self, conta: Conta)->bool:
        if conta.agencia in self.agencias:
            print("check_agency", True)
            return True
        print("check_agency", False)
        return False

    def check_client(self, cliente: Pessoa)->bool:
        if cliente in self.clientes:
            print("check_client", True)
            return True
        print("check_client",False)
        return False

    def _check_conta(self, conta: Conta)->bool:
        if conta in self.contas:
            print("check_conta", True)
            return True
        print("check_conta", False)
        return False

    def _check_conta_client(self, client: Cliente, conta: Conta)->bool:
        if conta is client.conta:
            print("check_conta_client", True)
            return True
        print("check_conta_client", False)
        return False


    def authenticate(self, cliente: Cliente, conta: Conta)->bool:
        return self._check_conta_client(cliente, conta) and self._check_conta(conta) \
            and self.check_client(cliente) and self.check_agency(conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"\nagencys: {self.agencias!r} \ncontas: {self.contas!r}\n\
clientes: {self.clientes!r}"
        return f"{class_name}:  {attrs}"


if __name__ == "__main__":
    cliente1 = Cliente("Daniel", 25)
    cliente1.conta = ContaCorrente(1001, 100101, 100000, 1000)
    # print(f"{cliente}\n{cliente.conta}")
    cliente2 = Cliente("Rafael", 22)
    cliente2.conta = ContaCorrente(1001, 100102, 10000, 100)
    banco = Bank()
    banco.clientes.extend([cliente1, cliente2])
    banco.contas.extend([cliente1.conta, cliente2.conta])
    # print(banco.authenticate(cliente1, cliente1.conta))

    if banco.authenticate(cliente1, cliente1.conta):
        pass
    # implementar uma lógica de interação com o cliente

    # print(banco)