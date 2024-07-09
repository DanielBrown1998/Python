import os
from pathlib import Path

#os.system('cls')
#os.system('echo "Hello world"')

# os.path:
# -> trabalha com caminhos em Windows, Linux e Mac!
# os.path.abspath: retorna o caminho absoluto de um arquivo ou diretório!
# os.path.join: junta os argumentos passados! 
# os.path.split: separa o diretorio do arquivo!
# os.splitext: pega o diretório do arquivo!
# os.path.exists: verifica se um caminho especificado existe -> bool!


#caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
#diretorio, arquivo = os.path.split(caminho)
#nome, ext = os.path.splitext(arquivo)
#print(ext)
#print(os.path.exists(caminho))

#caminho_absoluto = os.path.abspath('.')
#print(caminho_absoluto)
#print(os.path.exists(caminho_absoluto))

# os.listdir: navega em caminhos

dir = Path(__file__).parent.parent  # c:\Users\Danie\OneDrive\Documentos\GitHub\Python
for pasta in os.listdir(dir):
    if os.path.isdir(pasta):
        print(f"{pasta}/")
        for item in os.listdir(pasta):
            print(f"=-->{item}")
    else:
        print(f"{pasta}")