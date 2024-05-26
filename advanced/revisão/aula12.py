from contextlib import contextmanager


@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        arquivo = open(caminho_arquivo, modo, encoding='utf-8')
        yield arquivo
    finally:
        arquivo.close()


with my_open('./arquivo.txt', 'a+') as file:
    file.write('Daniel\n')

with my_open('./arquivo.txt', 'r') as file:
    print(file.read())
