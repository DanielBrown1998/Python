import sqlite3

from main import DB_FILE, TABLE_NAME

if __name__ == '__main__':
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    id = input('digite um id: ')
    comand = f"DELETE FROM {TABLE_NAME} WHERE id = ? "

    cursor.execute(
        comand, id
    )
    connection.commit()
    import select  # rodando o select
    cursor.close()
    connection.close()
