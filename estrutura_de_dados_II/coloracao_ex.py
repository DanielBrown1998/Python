cores = [
    "BLUE", "GREEN", "RED", "YELLOW", "ORANGE", "PINK",
	"BLACK", "BROWN", "WHITE", "PURPLE", "VOILET"
    ]

V = 6

G = [[0, 1, 0, 0, 1, 1],
     [1, 0, 0, 1, 1, 0],
     [0, 0, 0, 1, 1, 0],
     [0, 1, 1, 0, 0, 0],
     [1, 1, 1, 0, 0, 1],
     [1, 0, 0, 0, 1, 0]]

graus = []
for i in range(V):
    lista = list(filter(lambda x: x==1,G[i]))
    graus.append((i,len(lista)))

graus.sort(key=lambda x: x[1], reverse=True)
print(graus)

def colorir(grafo, graus, tamanho):
   corV = [-1] * tamanho
   atual = 0
   while len(list(filter(lambda x: x==-1, corV)))>0:
       i=0
       while(i<tamanho):
           while(i<tamanho) and (corV[i]!=-1):
              i = i + 1
           if i==tamanho:
               break
           achou = False   
           for j in range(tamanho):
               if corV[j] == atual and grafo[i][j] == 1:
                   achou = True
           if(i<tamanho) and (not achou):
              corV[i] = atual
           i = i + 1
       atual = atual + 1
   return corV 
    
corV = colorir(G,graus,V)
for i in range(V):
    print(cores[corV[i]])


