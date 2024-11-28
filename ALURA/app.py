import requests

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
        for dado in dados:
            print(f' {empresa} => Item: {dado["Item"]} | Preço: {dado["Preço"]} | Descrição: {dado["description"]}')
            print()
else:
    print('Erro ao acessar a API de restaurantes')
