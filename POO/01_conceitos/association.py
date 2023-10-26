class Escritor:
    def __init__(self, nome):
        self._name = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class Ferramenta:
    def __init__(self, nome):
        self._name = nome

    def escrever(self):
        print(f"{self._name} está escrevendo")


escritor = Escritor("Daniel")
caneta = Ferramenta("BIC")

print(caneta.escrever())
escritor.ferramenta = caneta
print(escritor.ferramenta.escrever())
