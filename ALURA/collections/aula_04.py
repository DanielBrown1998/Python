class ContaSalario:
    def __init__(self, codigo) -> None:
        self.codigo = codigo
        self._saldo = 0

    def deposita(self, valor) -> None:
        self._saldo += valor

    def __str__(self) -> str:
        return f'[>>Codigo {self.codigo} Saldo {self._saldo}<<]'

    def __eq__(self, outro) -> bool:
        if type(outro) != ContaSalario:
            return False

        return self.codigo == outro.codigo and self._saldo == outro._saldo

    def __lt__(self, outro) -> bool:
        if type(outro) != ContaSalario:
            raise TypeError(f"{type(outro)} não é do tipo {ContaSalario}")
        
        diferenca_saldo = self._saldo - outro._saldo

        if diferenca_saldo == 0:
            return self.codigo < outro.codigo

        return self._saldo < outro._saldo
    
    def __le__(self, outro) -> bool:
        if type(outro) != ContaSalario:
            raise TypeError(f"{type(outro)} não é do tipo {ContaSalario}")
        
        diferenca_saldo = self._saldo - outro._saldo

        if diferenca_saldo == 0:
            return self.codigo <= outro.codigo

        return self._saldo <= outro._saldo


conta1 = ContaSalario(37)
conta1.deposita(100)
conta2 = ContaSalario(23)
conta2.deposita(1010)
contas = [conta1, conta2]
contas = sorted(contas)
for conta in contas:
    print(conta)
