from grafos import Grafo


# questão 1
arestas = [
    [1, 12], 
    [2,13], 
    [3, 4],
    [7],
    [5, 6],
    [5],
    [6, 14], # 14 is Museum
    [14], # is Museum
    [8],
    [8, 9],
    [10],
    [11],
    [12, 5],
    [-1] # -1 porque ele não se conecta a ninguem
    ]
pesos = [ 8, 10, 10, 7, 15, 9, 14, 4, 3, 5, 9, 10, 9, 4, 16, 11, 8, 13, 6, 8, 0 ]
V = 14
grau = 2
g = Grafo(V, grau, eh_ponderado=True)

for origem in range(V):
    for e, destino in enumerate(arestas[origem]):
        g.insere_aresta(
            origem, destino, 
            eh_digrafo=True, 
            peso=pesos[origem+e]
            )
vertices_anteriores = []
distancia_inicial_ate_vertice = []
resp =g.dijsktra(
    vertice=0, 
    distancia_inicial_ate_vertice=distancia_inicial_ate_vertice,
    vertices_anteriores=vertices_anteriores
    )

print(resp)
# questão 2