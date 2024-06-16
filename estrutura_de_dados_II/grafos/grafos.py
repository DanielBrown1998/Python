class Grafo:
    def __init__(self, num_vertices: list, graus_max: int, eh_ponderado: bool = False) -> None:
        self.eh_ponderado = self.eh_ponderado
        self.num_vertices = num_vertices
        self.grau_max = graus_max
        self.arestas = [[0 for c in range(self.graus_max)] for i in range(self.num_vertices)]
        if eh_ponderado:
            self.pesos = [[0 for c in range(self.graus_max)] for i in range(self.num_vertices)]
        self.grau = [0 for c in range(self.num_vertices)]
