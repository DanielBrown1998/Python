import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean as distance_euclidean
from typing import List, Tuple
from valores import destino, origem, enderecos

# algoritmo guloso
def heuristica(origem: Tuple, destino: Tuple, enderecos: List[Tuple[int]], show=False) -> Tuple:
    ponto_atual = origem
    enderecos_restantes = enderecos.copy()
    menor_rota = [ponto_atual]
    distancia_percorrida = 0

    while enderecos_restantes:
        distancia_ponto_a_ponto = float("inf")
        # encontrar o ponto mais próximo do atual
        for ponto in enderecos_restantes:
            
            distancia = distance_euclidean(ponto_atual, ponto)

            if  distancia < distancia_ponto_a_ponto:
                ponto_prov = ponto
                distancia_ponto_a_ponto = distancia
                
        # atualizar a distancia        
        distancia_percorrida += distancia_ponto_a_ponto
        #adicionar o ponto a menor rota
        
        menor_rota.append(ponto_prov)
        
        #remover esse ponto dos pontos restantes
        enderecos_restantes.remove(ponto_prov)
        
        #atualiza o ponto
        ponto_anterior = ponto_atual
        ponto_atual = ponto_prov
        #atualiza a posicao dos enderecos

    # adicionando o último ponto
    distancia_percorrida += distance_euclidean(ponto_atual, destino)
    menor_rota.append(destino)
    
    if show:
        for e, ponto in enumerate(menor_rota):
            x, y = ponto
            cor = "black"
            if e == 0:
                cor = "blue"
            elif e == len(menor_rota) - 1:
                cor = "red"
            plt.scatter(x, y, color=cor)
    
            if e < len(menor_rota)-1:
                x1, y1 = menor_rota[e+1]
                # desenhando os vetores
                dx = x1 - x
                dy = y1 - y
                plt.arrow(x, y, dx, dy, color="black", head_width=.1)
        
        plt.title(f"ditancia percorrida: {distancia_percorrida}")
        plt.show()

    return menor_rota, round(distancia_percorrida, 2)


if __name__ == "__main__":
    sol = heuristica(origem, destino, enderecos, show=True)
    print(sol)