from pathlib import Path
caminho_projeto = Path(__file__)
caminho_abs_main = caminho_projeto.absolute()  # caminho absoluto do main
caminho_abs_projeto = caminho_abs_main.parent  # esse atributo (parent) retorna o diretório anterior, o pai de main
# print(caminho_abs_projeto, caminho_abs_main, sep='\n')

new_pasta = caminho_abs_projeto / 'pasta'
new_file = caminho_abs_projeto / 'file.txt'
new_other_file = new_pasta/'new_other_file.txt'

new_pasta.mkdir(exist_ok=True)
new_file.touch(exist_ok=True)
new_other_file.touch(exist_ok=True)

with new_file.open('w+') as file:
    file.write('Olá, Mundo!!!\n')
    file.write('livrei-me da maldição\n')

print(new_file.read_text())
# print(new_file)


