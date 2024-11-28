from cardapio import ItemCardapio
class Bebida(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao: str = descricao
    
    def desconto(self, frac=0.1):
        if frac > .5:
            raise ValueError('Desconto máximo de 50%')
        if frac < 0:
            raise ValueError('Desconto não pode ser negativo')
        return self.preco * frac