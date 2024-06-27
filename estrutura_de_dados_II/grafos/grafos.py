class Grafo:
    def __init__(self, num_vertices: int, graus_max: int, eh_ponderado: bool = False) -> None:
        self.eh_ponderado = eh_ponderado
        self.num_vertices = num_vertices
        self.grau_max = graus_max
        self.arestas = [[0]*self.grau_max for c in range(self.num_vertices)]
        if self.eh_ponderado:
            self.pesos = [[0]*self.grau_max for c in range(self.num_vertices)]
        self.grau = [0]*self.num_vertices

    def insere_aresta(self, origem, destino, eh_digrafo: bool = False, peso: int = 1) -> int:
        #if origem < 0 or origem >= self.num_vertices or destino < 0 or destino >= self.num_vertices:
        #    raise IndexError("out index range")
        self.arestas[origem][self.grau[origem]] = destino
        if self.eh_ponderado:
            self.pesos[origem][self.grau[origem]] = peso
        self.grau[origem] += 1
        if not eh_digrafo:
            self.arestas[self.grau[origem]][origem] = destino
            if self.eh_ponderado:
                self.pesos[self.grau[origem]][origem] = peso
            self.grau[destino] += 1
        return 1

    def remove_aresta(self, origem, destino, eh_digrafo: bool = False, peso: int = 1) -> int:
        if  destino >= self.num_vertices or destino < 0 or origem < 0 or origem > self.num_vertices:
            raise IndexError(f'insira números entre 0 e {len(self.num_vertices)-1} nos parâmetros origem e destino')
        self.arestas[origem][destino] = 0
        if self.eh_ponderado:
            self.pesos[origem][destino] = peso
        self.grau[origem] -= 1
        if not eh_digrafo:
            self.arestas[destino][origem] = 0
            if self.eh_ponderado:
                self.pesos[destino][origem] = peso
            self.grau[destino] -= 1

    def aux_profundidade(self, vertice_inicio: int, vertices_visitados: list, cont: int) -> None:
        vertices_visitados[vertice_inicio] = cont
        for i in range(self.grau[vertice_inicio]):
            if not vertices_visitados[self.arestas[vertice_inicio][i]]:
                print(vertice_inicio, end=' ')
                self.aux_profundidade(self.arestas[vertice_inicio][i], vertices_visitados, cont+1)
        print(vertice_inicio, end=' ')

    def busca_profundidade(self, vertice_inicio: int, vertices_visitados: list[int]):
        if vertice_inicio < 0 or vertice_inicio >= self.num_vertices:
            raise IndexError(f'{vertice_inicio} not in [0, {self.num_vertices-1}]')
        cont: int = 1
        for i in range(self.num_vertices):
            vertices_visitados.insert(i, 0)
        print("sequecia_profundidade: ", end="-> ")
        self.aux_profundidade(vertice_inicio, vertices_visitados, cont)

    def busca_largura(self, vertice_inicio: int, vertice_visitados: list[int]):
        IF, FF, cont, vert = 0, 0, 1, None
        vertice_visitados = [0]*self.num_vertices
        num_vertice = self.num_vertices
        fila = [0]*num_vertice
        FF += 1
        fila[FF] = vertice_inicio
        vertice_visitados[vertice_inicio] = cont
        print('sequencia_largura', end=': ')
        while IF != FF:
            IF += 1
            vert = fila[IF]
            print(vert, end=' ')
            for i in range(self.grau[vert]):
                if not vertice_visitados[self.arestas[vert][i]]:
                    FF += 1
                    fila[FF] = self.arestas[vert][i]
                    vertice_visitados[self.arestas[vert][i]] = cont + 1
        return vertice_visitados
#-----------------------FIM-CLASSE---------------------
