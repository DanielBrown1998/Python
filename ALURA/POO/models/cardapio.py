class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome: str = nome
        self._preco: float = preco

    def __str__(self):
        return f'{self.nome} - R$ {self.preco:.2f}'
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco