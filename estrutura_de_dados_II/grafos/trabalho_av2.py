import networkx as nx
import matplotlib.pyplot as plt
import csv
from pathlib import Path


# questão 1

def construir_caminho(inicio, fim, predecessores):
    caminho = []
    atual = fim
    while atual is not None:
        caminho.append(atual)
        atual = predecessores[atual]
    caminho.reverse()  # Inverte o caminho para iniciar do início até o fim
    return caminho

def dijkstra(grafo, inicio):
    
    import heapq
    # Número de vértices no grafo
    num_vertices = len(grafo)
    
    # Inicializa distâncias com infinito para todos os vértices exceto o inicial
    distancias = {vertice: float('inf') for vertice in range(num_vertices)}
    distancias[inicio] = 0
    
    # Dicionário para armazenar o predecessor de cada vértice no caminho mínimo
    predecessores = {vertice: None for vertice in range(num_vertices)}

    # Fila de prioridade para processamento dos vértices (distância, vértice)
    fila_prioridade = [(0, inicio)]  # (distância até o vértice, vértice)
    while fila_prioridade:
        # Extrai o vértice com menor distância
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)
        # Se a distância extraída é maior que a distância atual conhecida, ignoramos
        if distancia_atual > distancias[vertice_atual]:
            continue
        # Itera sobre os vizinhos do vértice atual
        for vizinho, peso in grafo[vertice_atual].items():
            distancia = distancia_atual + peso
            # Se encontramos um caminho mais curto para o vizinho, atualizamos a distância
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                predecessores[vizinho] = vertice_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    caminhos_minimos = {}
    for vertice in range(num_vertices):
        caminho = construir_caminho(inicio, vertice, predecessores)
        caminhos_minimos[vertice] = caminho
            
    return distancias, caminhos_minimos

grafo = [
    {1: 8, 12: 10},                                        #0
    {2: 10, 13: 7},                                        #1
    {3: 12, 4: 9},                                         #2 
    {7: 14},                                               #3
    {5: 4, 6: 3},                                          #4  
    {},                                                    #5
    {5: 5}, # 14 is Museum                                 #6
    {14: 10}, # street Museum                              #7
    {14: 9},                                               #8
    {8: 4},                                                #9
    {8: 16, 9: 11},                                        #10
    {10: 8},                                               #11
    {11: 13},                                              #12
    {12: 6},                                               #13
    {} # {} porque ele não se conecta a ninguem            #14
    ]

print('__'*20, "Questão1", '__'*20)
vertice_inicio = 0
distancias_minimas, caminhos_minimo = dijkstra(grafo, vertice_inicio)
print(f'rota minima: ', end='')
print(*caminhos_minimo[14], sep=' -> ')
print(f"distancia até o Museum: ", distancias_minimas[14])

# questão 2

grafo2 = [
    [1, 3, 4, 8], #0
    [0, 2, 5, 12],#1
    [1, 3, 6, 14],#2
    [0, 2, 7, 10],#3
    [0, 5, 7, 9], #4
    [1, 4, 6, 13],#5
    [2, 5, 7, 15],#6
    [3, 4, 6, 11],#7
    [0, 9, 10],   #8
    [4, 8, 11],   #9
    [3, 8, 11],   #10
    [7, 9, 10],   #11
    [1, 13, 14],  #12
    [5, 12, 15],  #13
    [2, 12, 15],  #14
    [6, 13, 14],  #15
]

# Criando um grafo não direcionado com 16 vértices
G = nx.Graph()

# Adicionando vértices ao grafo
num_vertices = 16
G.add_nodes_from(range(num_vertices))

# Adicionando as arestas
arestas = [(e, y) for e, x in enumerate(grafo2) for y in x]

G.add_edges_from(arestas)

# Função para colorir o grafo
def colorir_grafo(grafo):
    # Lista de cores disponíveis
    cores = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'brown', 'pink']
    
    # Dicionário para armazenar as cores dos vértices
    color_map = {}
    
    # Itera sobre os vértices e atribui cores de forma que vértices adjacentes tenham cores diferentes
    for vertice in grafo.nodes():
        # Cores usadas pelos vizinhos
        cores_usadas = set()
        
        # Verifica cores dos vizinhos
        for vizinho in grafo.neighbors(vertice):
            if vizinho in color_map:
                cores_usadas.add(color_map[vizinho])
        
        # Encontra a primeira cor disponível
        for cor in cores:
            if cor not in cores_usadas:
                color_map[vertice] = cor
                break
    
    return color_map

# Obtém a atribuição de cores
cores = colorir_grafo(G)
print('__'*20, "Questão2", '__'*20)
print("Gráfico Gerado")
# Desenha o grafo colorido
pos = nx.spring_layout(G)  # Layout para posicionar os nós
nx.draw(G, pos, with_labels=True, node_color=[cores[v] for v in G.nodes()], node_size=500, cmap=plt.cm.rainbow)
plt.show()

#Questão 3:

def ler_matriz_adjacencias_csv(nome_arquivo):
    matriz_adjacencias = []
    with open(nome_arquivo, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for linha in csvreader:
            # Converter os elementos da linha para inteiros
            linha = list(map(int, linha))
            matriz_adjacencias.append(linha)
    return matriz_adjacencias

def criar_grafo(matriz_adjacencias):
    # Cria um grafo não direcionado usando NetworkX
    G = nx.Graph()
    num_vertices = len(matriz_adjacencias)
    
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            peso = matriz_adjacencias[i][j]
            if peso != 0:
                G.add_edge(i, j, weight=peso)
    
    return G

def calcular_mst(grafo):
    # Calcula a árvore geradora mínima usando o algoritmo de Prim
    mst = nx.minimum_spanning_tree(grafo)
    return mst

def visualizar_grafo(grafo, mst):
    # Posicionamento dos vértices para visualização
    pos = nx.spring_layout(grafo)
    
    # Desenha o grafo original
    plt.figure(figsize=(10, 6))
    nx.draw_networkx(grafo, pos, with_labels=True, node_size=500, node_color='lightblue')
    
    # Desenha a MST sobreposta
    nx.draw_networkx_edges(mst, pos, edge_color='red', width=2)
    
    # Mostra os pesos das arestas na MST
    labels = nx.get_edge_attributes(mst, 'weight')
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)
    
    plt.title("Árvore Geradora de Custo Mínimo (MST)")
    plt.axis('off')
    plt.show()

print('__'*20, "Questão3", '__'*20)
print("Gráfico gerado")
nome_arquivo = Path(__file__).parent / 'grafo_ponderado.csv'  # Nome do arquivo CSV com a matriz de adjacências
matriz_adjacencias = ler_matriz_adjacencias_csv(nome_arquivo)
grafo = criar_grafo(matriz_adjacencias)
mst = calcular_mst(grafo)
visualizar_grafo(grafo, mst)

#Questão 4
def encontrar_caminho_labirinto(labirinto, inicio, fim):
    def dfs(x, y):
        # Condição de parada: alcançou a célula de saída
        if (x, y) == fim:
            caminho.append((x, y))
            return True
        
        # Marcar a célula atual como visitada
        visitado[x][y] = True
        caminho.append((x, y))
        
        # Movimentos possíveis: cima, baixo, esquerda, direita
        movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy
            # Verificar se o próximo movimento é válido (dentro dos limites e não visitado)
            if 0 <= nx < linhas and 0 <= ny < colunas and not visitado[nx][ny] and labirinto[nx][ny] == 0:
                if dfs(nx, ny):
                    return True
        
        # Se nenhum movimento levar à saída, desfazer o último movimento e retornar False
        caminho.pop()
        return False
    
    # Dimensões do labirinto
    linhas = len(labirinto)
    colunas = len(labirinto[0])
    
    # Inicialização de estruturas auxiliares
    visitado = [[False] * colunas for _ in range(linhas)]
    caminho = []
    
    # Ponto de entrada e saída
    x_inicio, y_inicio = inicio
    x_fim, y_fim = fim
    
    # Chama a função DFS a partir do ponto inicial
    dfs(x_inicio, y_inicio)
    
    # Retorna o caminho encontrado
    return caminho

print('__'*20, "Questão4", '__'*20)
labirinto = [
        [0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,1,0,0,0,1,0,0],
        [0,1,1,0,0,1,0,1,0,1],
        [1,1,1,0,1,1,0,1,0,0],
        [0,1,0,0,0,1,1,0,1,0],
        [0,0,1,1,0,0,0,1,0,0],
        [1,0,1,0,0,1,0,0,0,1],
        [1,1,1,0,1,1,0,1,1,1],
        [1,0,1,1,1,1,0,0,0,0],
    ]
#OBS: O labirinto do Trabalho foi muito difícil de representar, por isso gerei um semelhante

inicio = (0, 0)  # Início do labirinto
fim = (9, 9)     # Fim do labirinto

caminho = encontrar_caminho_labirinto(labirinto, inicio, fim)

if caminho:
    print("Caminho encontrado:")
    print("entrada ->", end="")
    for x, y in caminho:
        print(f"({x}, {y})->", end="")
    else:
        print("Saída")
    print("\n")
else:
    print("Não há caminho para sair do labirinto.")
