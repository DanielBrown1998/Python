
import networkx as nx
import valores
from scipy.spatial.distance import euclidean  as distance_euclidean

def desenhar_grafo(origem, destino, enderecos, tsp=False):

    G = nx.DiGraph()
    G.add_node("origem", local=origem)
    G.add_node("destino", local=destino)

    for e, endereco in enumerate(enderecos):
        G.add_node(e, local=endereco)

    for e, endereco in enumerate(enderecos):
        G.add_edge("origem", e, weight=distance_euclidean(origem, endereco))
        G.add_edge(e, "destino", weight=distance_euclidean(endereco, destino))
        for e2, endereco2 in enumerate(enderecos):
            if e != e2:
                G.add_edge(e, e2, weight=distance_euclidean(endereco, endereco2))

    if tsp:
        G.add_edge("destino", "origem", weight=0)
    return G


def algoritmo_grafo(origem, endereco, destino):
    G = desenhar_grafo(origem, destino, endereco, tsp=True)
    rota = nx.approximation.traveling_salesman_problem(G, cycle=False, weight="weight")

    indice_origem = rota.index("origem")

    rota_rotacionada = rota[indice_origem:] + rota[:indice_origem]

    rota_rotacionada.remove("origem")
    rota_rotacionada.remove("destino")

    melhor_rota = [origem] + [endereco[i] for i in rota_rotacionada] + [destino]

    distancia_percorrida = 0
    for e in range(len(melhor_rota)):
        if e < len(melhor_rota) - 1:
            distancia_percorrida += distance_euclidean(melhor_rota[e], melhor_rota[e+1])
    
    return melhor_rota, distancia_percorrida

if __name__ == "__main__":
    melhor_rota, distancia = algoritmo_grafo(valores.origem, valores.enderecos, valores.destino)
    print(melhor_rota, distancia)
