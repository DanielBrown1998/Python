
import networkx as nx
import valores
from scipy.spatial.distance import euclidean  as distance_euclidean

def desenhar_grafo(origem, destino, enderecos):

    G = nx.DiGraph()
    G.add_node("origem", local=origem)
    G.add_node("destino", local=destino)

    for e, endereco in enumerate(enderecos):
        G.add_node(e, local=endereco)

    for e, endereco in enumerate(enderecos):
        G.add_edge("origem", e, distancia=distance_euclidean(origem, endereco))
        G.add_edge(e, "destino", distancia=distance_euclidean(endereco, destino))
        for e2, endereco2 in enumerate(enderecos):
            if e != e2:
                G.add_edge(e, e2, distancia=distance_euclidean(endereco, endereco2))

    nx.draw(G, with_labels=True)
    print(*G.edges(data=True), sep="\n")

    return G

if __name__ == "__main__":
    G = desenhar_grafo(valores.origem, valores.destino, valores.enderecos)
    print(G.nodes(data=True))