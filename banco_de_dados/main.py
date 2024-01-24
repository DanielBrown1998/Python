import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent  # C:\Users\Danie\OneDrive\Documentos\GitHub\Python\banco_de_dados
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME  # C:\Users\Danie\OneDrive\Documentos\GitHub\Python\banco_de_dados\db.sqlite3
TABLE_NAME = 'customers'
if __name__ == '__main__':
    # cria a conexão
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    # sql
    # cria a tabela
    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
        f'('
        f'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        f'name TEXT,'
        f'age INTEGER'
        f')',
    )
    connection.commit()

    # CUIDADO: fazendo delete sem where
    # cursor.execute(
    #     f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
    # )

    # registra os valores nas colunas da tabelas
    # evitando sql-injection

    while True:
        print("inserir dados".center(20))
        name = str(input('nome: ')).title().strip()
        age = input("idade: ").strip()
        while isinstance(age, int):
            age = input("idade: ").strip()
        opc = input('continuar? [S/N]').strip().lower()[0]
        while opc not in "ns":
            opc = input('continuar? [S/N]').strip().lower()[0]

        command = f"INSERT INTO {TABLE_NAME}  (name, age) VALUES (?, ?)"  # as interrogações são bindings
        cursor.execute(
            command, (name, age)
        )
        connection.commit()
        if opc in 'n':
            break


    # encerrando a conexão
    cursor.close()
    connection.close()
