import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# apaga todas as linhas da tabela anterior
sql = f"DELETE FROM {TABLE_NAME}"
print(sql)
cursor.execute(sql)
connection.commit()

# cria tabela
sql = (f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}('
       f'id INTEGER PRIMARY KEY AUTOINCREMENT, '
       f'name TEXT NOT NULL,'
       f'idade INTEGER)'
       f';')
cursor.execute(sql)
print(sql)
connection.commit()
# registrando valores
my_data = "Rafaela", 26
sql = f'INSERT INTO {TABLE_NAME} (name, idade) VALUES (?, ?);'
#sql = f'INSERT INTO {TABLE_NAME} (name, idade) VALUES (:name, :idade);'
cursor.execute(sql, my_data)
#cursor.execute(sql, {'name': my_data[0], 'idade': my_data[1]})
print(sql)
connection.commit()

# registrando vários valores
others_data = (('Daniel', 26), ('Dayse', 48), ('Marcelo', 53))
cursor.executemany(sql, others_data)
print(sql)
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
