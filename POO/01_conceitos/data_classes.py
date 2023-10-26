from dataclasses import dataclass, field


@dataclass(init=False)
class Pessoa:
    nome: str
    under_name: str
    enderecos: list[str] = field(default_factory=list)

    # o post_init não será executado!!!
    # def __post_init__(self):
    #     print("É executado após o __init__")

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
