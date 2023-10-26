from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    under_name: str = ""

    @property
    def nome_completo(self):
        return f"{self.nome} {self.under_name}"

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *under_nome = valor.split()
        self.nome = nome
        self.under_name = " ".join(under_nome)

if __name__ == "__main__":
    p1 = Pessoa(" ")
    p1.nome_completo = "Daniel"
    print(p1.nome, p1.under_name)
