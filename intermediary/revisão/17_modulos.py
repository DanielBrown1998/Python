
#alterando (adicionando um novo caminho para 
#importação de pacotes) a perspectiva do meu arquivo.

import pathlib
new_dir = pathlib.Path(__file__).parent.parent
from modulos import modulo_principal, modulo_secundário
try:
    import sys
    sys.path.append(str(new_dir))
    print(*sys.path, sep='\n')
    from aulas.aula01 import my_print
except ModuleNotFoundError as error:
    print("Modulo não encontrado")
    print(error)
else:
    print("Modulo adicionado ao path")




if __name__ == '__main__':
    my_print(
        'CÓDIGO PRINCIPAL'
    )
    print(f'{__name__}: CÓDIGO PRINCIPAL')
    print(__file__)

