from cardapio import ItemCardapio
class Bebida(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao: str = descricao