from create import DB_FILE, TABLE_NAME
import sqlite3
DATA = []
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("SELECT * FROM " + TABLE_NAME)
for row  in cursor.fetchall():
    DATA.append(row)
    print(*row)
connection.commit()
cursor.close()
connection.close()
