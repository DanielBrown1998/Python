class ContaSalario:
    def __init__(self, codigo) -> None:
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor) -> None:
        self._saldo += valor

    def __str__(self) -> str:
        return f'[>>Codigo {self._codigo} Saldo {self._saldo}<<]'

    def __eq__(self, outro) -> bool:
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro) -> bool:
        if type(outro) != ContaSalario:
            raise TypeError(f"{type(outro)} não é do tipo {ContaSalario}")
        if self._codigo != outro._codigo:
            raise KeyError(f"Os códigos das contas não são condizentes!!!")
        return self._saldo < outro._saldo
    
    def __le__(self, outro) -> bool:
        if type(outro) != ContaSalario:
            raise TypeError(f"{type(outro)} não é do tipo {ContaSalario}")
        if self._codigo != outro._codigo:
            raise KeyError(f"Os códigos das contas não são condizentes!!!")
        return self._saldo <= outro._saldo


conta1 = ContaSalario(37)
conta1.deposita(100)
conta2 = ContaSalario(37)
conta2.deposita(1020)
print(conta1 == conta2)
print(conta1 <= conta2)
print(conta1 < conta2)
print(conta1 > conta2)