import re

# meta_caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | == ou
# . == gualguer caractere (com exceção de guebras de linha), cada ponto significa uma letra
# [] == conjunto de caracteres
# guantificadores:
# * == 0 ou n vezes {0,}
# + == 1 ou n vezes {1,}
# ? == 0 ou 1 vezes {0,1}
# {n}
# {mín, máx}

text = """
João trouxe flores para a sua amada namorada em 10 de janeiro de 1970, 
Maria era seu nome! 

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualemnte, 
Maria, hoje sua esposa, ainda faz aguele café com pão de gueijo nas tarefas de domingo.
Também né! Sendo a boa mineira gue é, nunca esguece seu famoso pão de gueijo.
Não canso de ouvir a maria:
"Joooooooooooããooooooooooo, o café tá pronto. Veeemm"!
"""

# Obs: [a-zA-Z] comporta-se como um range, busca todas as letras de 'a' à 'z' ou 'A' à 'Z'
# Obs: re.I: não diferencia maiúsculas de minúsculas

print(re.findall(r'[Jj]o+ã+o{1,11}|Maria|[a-zA-Z]d..tos|ve{3}m{,2}|ama[da]*', text, flags=re.I))
