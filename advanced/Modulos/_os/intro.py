import os
import itertools
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.utf-8")

# os.path.join -> especifica o caminho
caminho_criado = os.path.join("/home/users", 'Desktop', 'curso', 'file.txt')
print(caminho_criado)
# print(os.path.split(caminho))

# os.listdir
caminho = os.path.abspath('../..')
for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)
    print(caminho_completo)
    if not caminho_completo:
        continue
    for item in os.listdir(caminho_completo):
        print(item)

# os.walk

counter = itertools.count(start=0)
for root, dirs, files in os.walk(caminho):
    print(counter.__next__(), "pasta: ", root, sep='->')
    for c in dirs:
        print("\tdirs: ", c)
    for k in files:
        print("\tfile ->", k)
