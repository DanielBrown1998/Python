from typing import List
import random
from models.avaliacao import Avaliacao
from models.prato import Prato
from models.bebida import Bebida

class Restaurante:
    def __init__(self, nome: str, local: str, telefone: List) -> None:
        self.nome = nome.title().strip()
        self.status = False
        self.endereco = local.strip().capitalize()
        self.avaliacoes: List[Avaliacao] = []
        self.telefone = []
        self.pratos: List[Prato] = []
        self.bebidas: List[Bebida] = []
        for tel in telefone:
            self.telefone.append(tel)
        self._id = int(random.randint(1, 1000000))
    
    def __str__(self) -> str:
        return f"Nome: {self.nome}, Endereço: {self.endereco}, Telefone(s): {self.telefone}, Status: {'ativo' if self.status else 'inativo'}"
    
    def __repr__(self) -> str:
        return f"Nome: {self.nome}, Endereço: {self.endereco}, Telefone(s): {self.telefone}, Status: {'ativo' if self.status else 'inativo'}"
    
    def ativar(self) -> bool:
        self.status = True
        print(f"Restaurante {self.nome} ativado com sucesso!")
        return self.status

    def desativar(self) -> bool:
        self.status = False
        print(f"Restaurante {self.nome} desativado com sucesso!")
        return self.status

    def adicionar_avaliacao(self, nome: str, restaurante, nota: float, comentario: str) -> None:
        avaliacao = Avaliacao(nome, restaurante, nota, comentario)
        self.avaliacoes.append(avaliacao)
        print(f"Avaliação adicionada com sucesso!")
        
    def adicionar_prato(self, prato: Prato) -> None:
        self.pratos.append(prato)
        print(f"Prato {prato.nome} adicionado com sucesso!")
    
    def adicionar_bebida(self, bebida: Bebida) -> None:
        self.bebidas.append(bebida)
        print(f"Bebida {bebida.nome} adicionada com sucesso!")

    @property
    def id(self):
        return self._id

