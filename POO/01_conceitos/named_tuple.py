from collections import namedtuple


cartas = namedtuple("Carta", ["valor", "naipe"])
as_espadas = cartas('A', 'espada')
print(as_espadas)
print(as_espadas.naipe)
