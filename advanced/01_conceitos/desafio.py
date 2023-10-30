class Motor:
    def __init__(self, combustivel=None, litragem=None, power=None):
        self.combustivel = combustivel
        self.litragem = litragem
        self.power = power


class Carro:
    def __init__(self, modelo, tipo=None,combustivel=None, litragem= None, power=None):
        self.nome = modelo
        self.tipo = tipo
        self.motor = []
        self.engine(combustivel, litragem, power)


    def engine(self, combustivel, litragem, power):
        motor = Motor(combustivel, litragem, power)
        self.motor.append(
            {'combustível': motor.combustivel, 'litragem': motor.litragem, 'power': motor.power}
        )


class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    def carro(self, modelo, tipo=None, combustivel=None, litragem=None, power=None):
        car = Carro(modelo, tipo, combustivel, litragem, power)

        carro = {'modelo': car.nome, 'tipo': car.tipo, 'espec': car.motor}

        self.carros.append(
            carro
        )

    def espec(self):
        for item in self.carros:
            print(f"    {self.nome}            ")
            for key, value in item.items():
                if key == 'espec':
                    for espec in value:
                        for m, n in espec.items():
                            print(f"{m}: {n}")
                else:
                    print(f'{key}: {value}')
            print("\n")

lambo = Fabricante('Lamborghini')
lambo.carro('húracan', tipo='super-sport', power=770, litragem=3.8, combustivel='gasolina')
lambo.carro('Centenario', tipo='hyper-sport', power=770, litragem=6.5, combustivel='gasolina')
lambo.espec()

nissan = Fabricante("Nissan")
nissan.carro('Nissan-GTR-R35-2024', tipo='super-sport', power=570, litragem=3.8, combustivel='gasolina')
nissan.espec()
