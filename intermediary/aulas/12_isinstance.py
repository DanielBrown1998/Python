
data = ('nome', 'Daniel Brown Rodrigues M. dos Passos'), ('idade', 26), ('salario', 3000.00), ('status', True)
data = {
    key: value*2 if isinstance(value, float) else value for key, value in data
}
print(data)
# {'nome': 'Daniel Brown Rodrigues M. dos Passos', 'idade': 26, 'salario': 6000.0, 'status': True}
