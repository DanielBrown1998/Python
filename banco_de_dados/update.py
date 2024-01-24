import sqlite3
from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
id = input('digite um id: ')
name = input('digite o novo nome: ')
cursor.execute(
    f"UPDATE FROM {TABLE_NAME} SET name = ? WHERE id = ?",
    (id, name)
)
connection.commit()
import select  # rodando o select
cursor.close()
connection.close()
