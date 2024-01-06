import itertools
import os

caminho = os.path.abspath('../..')


# os.walk

counter = itertools.count(start=0)
for root, dirs, files in os.walk(caminho):
    print(counter.__next__(), "pasta: ", root, sep='->')
    for c in dirs:
        caminho_completo = os.path.join(root, c)
        print(f"\tdirs: {c} tamanho = {os.path.getsize(caminho_completo)} bytes")
    for k in files:
        caminho_completo = os.path.join(root, k)
        print(f"\tfile -> {k} tamanho= {os.path.getsize(caminho_completo)} bytes")
