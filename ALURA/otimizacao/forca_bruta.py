import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean as distance_euclidean
from typing import List, Tuple
from itertools import permutations
from valores import destino, enderecos, origem
# resolução do problema via força bruta
def desenhar_rota(origem: Tuple[int], destino: Tuple[int], enderecos: List[Tuple[int]], show=False) -> Tuple:
    #validacao de origme e destino
    if len(origem) != 2:
        raise ValueError(f"{origem} não tem 2 argumentos")

    elif len(destino) != 2:
        raise ValueError(f"{destino} não tem 2 argumentos")
    
    #validação de enderecos
    for ponto in enderecos:
        if len(ponto) != 2:
            raise AttributeError(f" O ponto {ponto} da posição {e} de enderecos não possui 2 valores")
        
    #setando a distancia percorrida a partir de enderecos
    distancia_percorrida = 0
    for e in range(len(enderecos)):
        if e < len(enderecos) -1:
            distancia_percorrida += distance_euclidean(enderecos[e], enderecos[e+1])

    # percorrendo as possíveis rotas para determinar a menor possível entre origem e destino
    for rota in permutations(enderecos):
        distancia_provisoria = 0
        rota_tam = len(rota)
        for e in range(rota_tam):
            if e < rota_tam -1:
                distancia_provisoria += distance_euclidean(rota[e], rota[e+1])
        #setando a menor distancia entre origem e destino
        if distancia_provisoria < distancia_percorrida:
            distancia_percorrida = distancia_provisoria 
            enderecos = rota
    #resetando distancia_percorrida e determinando rota    
    distancia_percorrida = 0
    rota = [tuple(origem)] + [c for c in enderecos] + [tuple(destino)]
    #print(rota)
    #construindo o gráfico
    for e, ponto in enumerate(rota):
        x, y = ponto
        if show:
            cor = "black"
            if e == 0:
                cor = "blue"
            elif e == len(rota) - 1:
                cor = "red"
            plt.scatter(x, y, color=cor)
    
        if e < len(rota)-1:
            x1, y1 = rota[e+1]
            distancia_percorrida += distance_euclidean(rota[e], rota[e+1])
            # desenhando os vetores
            if show:
                dx = x1 - x
                dy = y1 - y
                plt.arrow(x, y, dx, dy, color="black", head_width=.1)
    # plotando o gráfico
    if show:
        plt.title(f"distância da rota: {round(distancia_percorrida, 2)}")
        plt.show()

    return rota, distancia_percorrida


if __name__ == "__main__":
    
    rota, tam = desenhar_rota(origem, destino, enderecos, show=True)
    print(tam, rota)
