from main import ROOT_DIR, DB_NAME, DB_FILE, TABLE_NAME
import sqlite3

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("SELECT * FROM " + TABLE_NAME)
for row  in cursor.fetchall():
    print(*row)

cursor.close()
connection.close()
