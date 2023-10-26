import datetime
import sys

# sys.path : busca os módulos do python

print(f'Esse módulo se chama {__name__}')
print(f"Ele está inserido em {sys.path[0]}")
print(f"hora: {datetime.datetime.now()}")
