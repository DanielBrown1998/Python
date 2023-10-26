class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []


    def inserir_endereco(self, rua, numero):
        self.enderecos.append(
            Endereco(rua, numero)
        )

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero


cliente = Cliente("Daniel Brown")
cliente.inserir_endereco('Travessa Mário Avena', 45)
cliente.lista_enderecos()
