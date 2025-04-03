import requests
import json
from pathlib import Path

# Criação de diretório para armazenar os arquivos JSON
LOCAL_RESTAURANTES = Path(__file__).parent / 'restaurantes/'
print(LOCAL_RESTAURANTES)


def get_restaurantes(filtro: str = None, save: bool = False):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    dados_restaurante = {}
    if response.status_code == 200:
        restaurantes = response.json()
        if filtro is None:
            dados_restaurante = restaurantes
        else:
            for restaurante in restaurantes:
                if filtro.lower() in restaurante['Company'].lower():
                    dados = {
                        'Item': [restaurante['Item']],
                        'Preço': [restaurante['price']],
                        'description': [restaurante['description']]
                    }
                    if restaurante['Company'] not in dados_restaurante:
                        dados_restaurante[restaurante['Company']] = [dados]
                        continue
                    dados_restaurante[restaurante['Company']].append(dados)
        if save:
            for empresa, dados in dados_restaurante.items():
                nome_empresa = f"{empresa.split(' ')[0]}.json"
                with open(LOCAL_RESTAURANTES / nome_empresa, 'w') as file:
                    json.dump(dados, file)
            print('Arquivos salvos com sucesso')
        return {"Dados": dados_restaurante}

    else:
        return {'Erro': f"{response.status_code} - {response.text}"}
