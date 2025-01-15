import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean as distance_euclidean

origem = [(0, 0)] 
destino = [(4, 4)]
distancia_percorrida = 0 
enderecos = [(2, 1), (2, 2), (8, 3), (5, 3)]

rota = origem + enderecos + destino

for e, ponto in enumerate(rota):
    x, y = ponto
    cor = "black"
    if e == 0:
        cor = "blue"
    elif e == len(rota) - 1:
        cor = "red"
    plt.scatter(x, y, color=cor)
    if e < len(rota)-1:
        x1, y1 = rota[e+1]
        distancia_percorrida += distance_euclidean(rota[e], rota[e+1])
    dx = x1 - x
    dy = y1 - y
    plt.arrow(x, y, dx, dy, color="black", head_width=.1)

plt.title(f"distância da rota: {round(distancia_percorrida, 2)}")
plt.show()
