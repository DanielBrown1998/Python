from create import DB_FILE, TABLE_NAME
import sqlite3
nome = 'Daniel'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

sql = f" DELETE FROM {TABLE_NAME} WHERE name = '{nome}'"
row = cursor.execute(sql)

connection.commit()
cursor.close()
connection.close()
