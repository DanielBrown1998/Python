import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# cria tabela
cursor.execute(
      f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
          f'('
          f'id INTEGER PRIMARY KEY AUTOINCREMENT,'
          f'name TEXT NOT NULL,'
          f'idade INTEGER'
          f');'
)
connection.commit()
# registrando valores
my_data = "Rafaela", 26
sql = f'INSERT INTO {TABLE_NAME} (name, idade) VALUES (?, ?);'
cursor.execute(sql, my_data)
connection.commit()

opc = input('apagar tabela customers? [S/N] ').lower()
while opc[0] not in 'SsNn' or opc.isspace() or opc in '':
    opc = input('apagar tabela customers? [S/N] ').lower()

if opc in 'Ss':
    cursor.execute(
        f'DELETE FROM {TABLE_NAME};'
    )
connection.commit()


cursor.close()
connection.close()
