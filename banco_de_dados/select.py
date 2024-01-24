

import sqlite3
from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f"SELECT * FROM {TABLE_NAME}"
)

for row in cursor.fetchall():
    _id, name, age = row
    print(_id, name, age)

cursor.close()
connection.close()
