import os 
import json
import pathlib
NOME_ARQUIVO = 'meu_arquivo.json'

DIR_ABS_JSON = pathlib.Path(__file__).parent
dir_abs_py = os.path.abspath(__file__)

# Cria um dicionário
dicionario = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

DIRETORIO = DIR_ABS_JSON / NOME_ARQUIVO
print(DIRETORIO)
# Salva o dicionário em um arquivo JSON
with open(DIRETORIO, "w", encoding='UTF-8') as arquivo:
    json.dump(dicionario, arquivo, ensure_ascii=True, indent=4)

