print(f'Ao importar o módulo {__name__}, o código aqui será executado')
import modulos.modulo_secundário as modulo
print(f'o módulo {__name__} importou o {modulo.__name__}')
