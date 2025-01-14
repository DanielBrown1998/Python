import requests
import json
from pathlib import Path

# Criação de diretório para armazenar os arquivos JSON
LOCAL_RESTAURANTES = Path(__file__).parent / 'restaurantes/'
print(LOCAL_RESTAURANTES)



url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
dados_restaurante = {}
if response.status_code == 200:
    restaurantes = response.json()
    for restaurante in restaurantes:
        dados = {
                'Item': [restaurante['Item']],
                'Preço': [restaurante['price']],
                'description': [restaurante['description']]
            }
        if restaurante['Company'] not in dados_restaurante:
            dados_restaurante[restaurante['Company']] = [dados]
            continue
        dados_restaurante[restaurante['Company']].append(dados)
    for empresa, dados in dados_restaurante.items():
        nome_empresa = f"{empresa.split(' ')[0]}.json"
        with open(LOCAL_RESTAURANTES / nome_empresa, 'w') as file:
            json.dump(dados, file)
        for dado in dados:
            print(f' {empresa} => Item: {dado["Item"]} | Preço: {dado["Preço"]} | Descrição: {dado["description"]}')
            print("_"*30)
else:
    print('Erro ao acessar a API de restaurantes')
