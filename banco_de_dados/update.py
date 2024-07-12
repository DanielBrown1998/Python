from create import DB_FILE, TABLE_NAME
import sqlite3

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("SELECT * FROM " + TABLE_NAME)

names = [name for id, name, age in cursor.fetchall()]


for e, name in enumerate(names):
    sql = f"UPDATE {TABLE_NAME} SET id = {e+1} WHERE name = '{name}'"
    cursor.execute(sql)

connection.commit()
cursor.close()
connection.cursor()

import select
