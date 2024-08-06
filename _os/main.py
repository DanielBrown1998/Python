import os
import shutil
from pathlib import Path
import size

#os.system('cls')
#os.system('echo "Hello world"')

# os.path:
# -> trabalha com caminhos em Windows, Linux e Mac!
# os.path.abspath: retorna o caminho absoluto de um arquivo ou diretório!
# os.path.join: junta os argumentos passados! 
# os.path.split: separa o diretorio do arquivo!
# os.splitext: pega o diretório do arquivo!
# os.path.exists: verifica se um caminho especificado existe -> bool!

"""
caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
diretorio, arquivo = os.path.split(caminho)
nome, ext = os.path.splitext(arquivo)
print(ext)
print(os.path.exists(caminho))
"""
caminho_absoluto = os.path.abspath('./visualizacao_dados') # C:\Users\Danie\OneDrive\Documentos\GitHub\Python
#print(os.path.exists(caminho_absoluto))

# os.listdir: navega em caminhos


#dir = Path(__file__).parent.parent  # c:\Users\Danie\OneDrive\Documentos\GitHub\Python
#for pasta in os.listdir(dir):
#    if os.path.isdir(pasta):
#        print(f"{pasta}/")
#        for item in os.listdir(pasta):
#            print(f"=-->{item}")
#    else:
#        print(f"{pasta}")

#os.walk é uma função que permite percorrer uma estrutura de diretórios de maneira recursiva.
#os.walk retorna um generator com 3 valores: caminho(root), diretórios, arquivos

#for root, dirs, files in os.walk(caminho_absoluto):
#    if 'my_tdd.py' in files:
#        print(f"Encontrei o arquivo em {root}")

#for root, dirs, files in os.walk(caminho_absoluto): 
#    print(f"{root}-> {size.formata_tamanho(os.path.getsize(root), formatacao=5)}")
#    for dir_ in dirs:
#        print(f"=-->{dir_}, {size.formata_tamanho(os.path.getsize(os.path.join(root, dir_)), formatacao=5)}")
#    for file_ in files:
#        print(f"=--=-->{file_}, {size.formata_tamanho(os.path.getsize(os.path.join(root, file_)), formatacao=5)}")


# os + shutil -> copiar, mover e apagar diretórios

# mover/renomear (mesma coisa) -> shutil.move / os.rename
# copiar -> shutil.copy / shutil.copytree (recursivamente)
# apagar -> os.unlink / shutil.rmtree (recursivamente)

HOME = os.path.expanduser('~') # caminho do usuário
DIR_TEST = os.path.join(HOME, 'meu_diretorio_teste')
DIR_TEST_2 = os.path.join(HOME, 'meu_diretorio_teste_2')
os.makedirs(DIR_TEST_2, exist_ok=True) # criar diretório
os.makedirs(DIR_TEST, exist_ok=True) # criar um diretório

for root, dirs, files in os.walk(DIR_TEST_2): 
    print(f"{root}-> {size.formata_tamanho(os.path.getsize(root), formatacao=5)}")
    for dir_ in dirs:
        caminho_dir = os.path.join(root, dir_)
        #print(caminho_dir, DIR_TEST)
        caminho_destino = os.path.join(
            root.replace(DIR_TEST_2, DIR_TEST), dir_
        )
        try:
            shutil.copy(caminho_dir, caminho_destino)
        except PermissionError:
            print(f"Não foi possível copiar {caminho_dir} para {caminho_destino}")
        except:
            print('outro erro!')
        #print(f"=-->{dir_}, {size.formata_tamanho(os.path.getsize(caminho_dir), formatacao=5)}")
    

#os.rmdir(HOME + '/meu_diretorio_teste') # apagar