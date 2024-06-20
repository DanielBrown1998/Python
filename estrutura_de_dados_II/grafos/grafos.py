class Grafo:
    def __init__(self, num_vertices: int, graus_max: int, eh_ponderado: bool = False) -> None:
        self.eh_ponderado = eh_ponderado
        self.num_vertices = num_vertices
        self.grau_max = graus_max
        self.arestas = [[0 for i in range(self.num_vertices)] for c in range(self.num_vertices)]
        if self.eh_ponderado:
            self.pesos = [ [0 for i in range(self.num_vertices)] for c in range(self.num_vertices)]
        self.grau = [0 for c in range(self.num_vertices)]

    def insere_aresta(self, origem, destino, eh_digrafo: bool = False, peso: int = 1) -> int:
        if origem < 0 or origem >= self.num_vertices or destino < 0 or destino >= self.num_vertices:
            raise IndexError(f'insira números entre 0 e {len(self.num_vertices)-1} nos parâmetros origem e destino')
        self.arestas[origem][destino] = 1
        if self.eh_ponderado:
            self.pesos[origem][destino] = peso
        self.grau[origem] += 1
        if not eh_digrafo:
            self.arestas[destino][origem] = 1
            if self.eh_ponderado:
                self.pesos[destino][origem] = peso
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

    def aux_profundidade(self, vertice_inicio: int, vertices_visitado: list, cont: int) -> None:
        vertices_visitado[vertice_inicio] = cont
        for i in range(self.grau[vertice_inicio]):
            if not vertices_visitado[self.arestas[vertice_inicio][i]]:
                print(vertice_inicio, i)
                self.aux_profundidade(self.arestas[vertice_inicio][i], vertices_visitado, cont+1)

    def busca_profundidade(self, vertice_inicio: int, vertice_visitados: list[int]):
        if vertice_inicio < 0 or vertice_inicio >= self.num_vertices:
            raise IndexError(f'{vertice_inicio} não pertence ao intervalo [0, 9]')

        cont: int = 1
        vertice_visitados = [0]*self.grau[vertice_inicio]
        self.aux_profundidade(vertice_inicio, vertice_visitados, cont)

    def busca_largura(self, vertice_inicio: int, vertice_visitados: list[int]):
        cont = 1
        FF = 0
        IF = 0
        vertice_visitados = [0]*self.num_vertices
        fila = []
        num_vertice = self.num_vertices
        FF += 1
        fila.insert(vertice_inicio, FF)
        vertice_visitados.insert(vertice_inicio, cont)
        while (IF != FF):
            IF = (IF + 1)% num_vertice
            print(fila)
            try:
                vert = fila[IF]
            except IndexError:
                vert = 0
            cont += 1
            for i in range(self.grau[vert]):
                if (not vertice_visitados[self.arestas[vert][i]]):
                    FF = (FF + 1) % num_vertice
                    fila.insert(self.arestas[vert][i], FF)
                    vertice_visitados.insert(self.arestas[vert][i], cont)  
                    print(vertice_visitados[self.arestas[vert][i]])

    def procura_menor_distancia(self, distancia_inicial_ate_vertice: list[float],
                                vertices_visitados: list[int], num_vertices: int)-> int:
        menor: int = -1 
        primeiro: int  = 1
        for i in range(num_vertices):
            if distancia_inicial_ate_vertice[i] >= 0 and vertices_visitados[i] == 0:
                if primeiro:
                    menor = i
                    primeiro = 0
                elif distancia_inicial_ate_vertice[menor] > distancia_inicial_ate_vertice[i]:
                    menor = i
        return menor  #índice da menor distância  

    def dijsktra(self, vertice: int, vertices_anteriores: list[int], 
                 distancia_inicial_ate_vertice: list[float]):
        cont  = num_vertice = self.num_vertices
        vertices_visitados = [0] * num_vertice
        for i in range(num_vertice):
            vertices_anteriores.insert(i, -1)
            distancia_inicial_ate_vertice.insert(i, -1)
            vertices_anteriores.insert(i, 0)
        distancia_inicial_ate_vertice.insert(vertice, 0)
        while cont > 0:
            u = self.procura_menor_distancia(distancia_inicial_ate_vertice, vertices_visitados, num_vertice)
            if u == -1:
                break
            vertices_visitados.insert(u, 1)
            cont -= 1
        for i in range(self.grau[u]):
            ind = self.arestas[u][i]
            if distancia_inicial_ate_vertice[ind] < 1:
                distancia_inicial_ate_vertice.insert(ind, distancia_inicial_ate_vertice[u] + 1)
                vertices_anteriores.insert(ind, u)
            elif distancia_inicial_ate_vertice[ind] > distancia_inicial_ate_vertice[u] + 1:
                distancia_inicial_ate_vertice.insert(ind, distancia_inicial_ate_vertice[u] + 1)
                vertices_anteriores.insert(ind, u)
            

V = 10
grau = 10
meu_grafo = Grafo(V, grau)
for i in range(V):
    choices = []
    from random import choice
    for gr in range(choice(range(grau))):
        escolhido_destino= choice(range(V))
        while (i, escolhido_destino) in choices:
            escolhido_destino = choice(range(V))
        par = (i, escolhido_destino)
        meu_grafo.insere_aresta(*par)
        choices.append(par)

visitados: list[int] = [0]*V
anteriores: list[int] = [0]*V
meu_grafo.busca_profundidade(
    0, visitados
)
print(*meu_grafo.arestas, sep='\n')
print(*meu_grafo.grau)