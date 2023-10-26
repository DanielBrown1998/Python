 # uma classe se estende em outra classe
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


class Cliente(Pessoa):
    pass


cliente_1 = Cliente('Daniel', "Brown")
