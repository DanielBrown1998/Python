# associação

class Escritor:

    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, value):
        self._ferramenta = value


class FerramentaEscrever:

    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        print(f'{self.nome} está escrevendo')


escritor = Escritor('Daniel')
pc = FerramentaEscrever('computador')
escritor.ferramenta = pc
# print(escritor.ferramenta.escrever())

# Agregação


class CarrinhoCompras:

    def __init__(self):
        self._produtos: list[object] = []

    @property
    def produtos(self):
        return [c for c in self._produtos]

    def inserir_produtos(self, *args):
        self._produtos.extend(args)
        # self._produtos += args

    def valor_total(self) -> int | float:
        if self._produtos:
            return sum([p.preco for p in self._produtos])
        return 0

    def listar_produtos(self):
        print(*[f"{item.nome}: {item.preco}" for item in self._produtos], sep="\n")


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = CarrinhoCompras()
p1, p2 = Produto("pc", 12000), Produto("notebook", 2000)
carrinho.inserir_produtos(p1, p2)
# carrinho.listar_produtos()
total = carrinho.valor_total()
# print(total)

# Composição


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua: str, num: int) -> None:
        self.enderecos.append(Endereco(rua, num))

    def listar_enderecos(self):
        print(*[f"{item.rua}, {item.numero}" for item in self.enderecos])


class Endereco:
    def __init__(self, rua, num):
        self.rua = rua
        self.numero = num


cliente_1 = Cliente('Maria')
cliente_1.inserir_endereco('Coronel Azevedo Junior', 510)
cliente_1.listar_enderecos()
