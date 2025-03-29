from valores import destino, origem, enderecos
from typing import List, Tuple
from scipy.spatial.distance import euclidean  as distance_euclidean
from deap import base, creator, tools, algorithms
import numpy as np
import matplotlib.pyplot as plt


def avaliacao(individuo: List[int], origem: Tuple[int], enderecos: List[Tuple[int]], destino: Tuple[int]) -> Tuple:
    distancia_percorrida = 0
    rota = [origem]
    for i in individuo:
        distancia_percorrida += distance_euclidean(enderecos[i], rota[-1])
        rota.append(enderecos[i])
    distancia_percorrida += distance_euclidean(rota[-1], destino)
    rota.append(destino)

    return distancia_percorrida, 

def algoritmos_geneticos(origem: Tuple[int], 
                         enderecos: List[Tuple[int]], 
                         destino: Tuple[int], 
                         tam_populacao_inicial: int = 100, 
                         prob_cruzamento: float = .7, 
                         prob_mutacao: float = .1, 
                         num_geracoes: int = 100) -> Tuple:

    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individuo", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    toolbox.register("Genes", np.random.permutation, len(enderecos))
    toolbox.register("Individuos", tools.initIterate, creator.Individuo, toolbox.Genes)

    toolbox.register("Populacao", tools.initRepeat, list, toolbox.Individuos)
    populacao = toolbox.Populacao(n=tam_populacao_inicial)
        
    toolbox.register("mate", tools.cxPartialyMatched)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=prob_mutacao)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", avaliacao, origem=origem, enderecos=enderecos, destino=destino)

    algoritmo = algorithms.eaSimple(
        populacao,
        toolbox, 
        cxpb=prob_cruzamento,
        mutpb=prob_cruzamento,
        ngen=num_geracoes, 
        verbose=False
    )

    melhor_ind = tools.selBest(populacao, 1)[0]
    enderecos = [enderecos[i] for i in melhor_ind]
    melhor_rota = [origem]+ enderecos +[destino]

    return melhor_rota, avaliacao(melhor_ind, origem, enderecos, destino) 

if __name__ == "__main__":
    melhor_rota, distancia = algoritmos_geneticos(origem, enderecos, destino)
    for e, ponto in enumerate(melhor_rota):
            x, y = ponto
            cor = "black"
            if e == 0:
                cor = "blue"
            elif e == len(melhor_rota) - 1:
                cor = "red"
            plt.scatter(x, y, color=cor)
    
            if e < len(melhor_rota)-1:
                x1, y1 = melhor_rota[e+1]
                # desenhando os vetores
                dx = x1 - x
                dy = y1 - y
                plt.arrow(x, y, dx, dy, color="black", head_width=.1)
        
    plt.title(f"ditancia percorrida: {distancia}")
    plt.show()
    print(melhor_rota, distancia)
