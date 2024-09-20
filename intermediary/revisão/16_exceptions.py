try:
    file = open(r'./arquivo.txt', 'r', encoding='utf-8') 
    print(file.read())
    file.close()
except FileNotFoundError:
    print('Erro ao abrir o arquivo')