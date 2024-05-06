# criando o meu erro
class MyError(Exception):
    pass


num = input('digite um número inteiro: ')
if isinstance(num, int):
    print(f'você digitou {num}')
else:
    _exception = MyError('houve um erro')
    _exception.add_note('ponha um número inteiro.')
    raise _exception

