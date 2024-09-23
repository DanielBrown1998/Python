class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[>>Codigo {self.codigo} Saldo {self.saldo}<<]"


conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)

contas = [conta_do_gui, conta_da_dani]
print(*[conta for conta in contas], sep='\n')


contas[1].deposita(2000)
print(conta_do_gui)
print(conta_da_dani)
