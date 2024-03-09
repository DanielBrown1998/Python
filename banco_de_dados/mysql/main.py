import pymysql
import dotenv
import os

DEBUG = 0

dotenv.load_dotenv()

TABLE_NAME = 'customers'

connection = pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_ROOT_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
    cursorclass=None,
)
with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )
    connection.commit()

    if DEBUG == 1:
        with connection.cursor() as cursor:
            sql = (
                f'INSERT INTO {TABLE_NAME} '
                f'(nome, idade) VALUES (%(name)s, %(age)s) '
            )
            data = {
                "name": 'Rafaela',
                "age": 25,
            }
            result = cursor.execute(sql, data)

        connection.commit()

        with connection.cursor() as cursor:
            sql = (
                f'INSERT INTO {TABLE_NAME} '
                f'(nome, idade) VALUES (%(name)s, %(age)s) '
            )
            data_1 = (
                {"name": 'Sara', "age": 21, },
                {"name": 'Thiago', "age": 41, },
                {"name": 'Rose', "age": 30, },
                {"name": 'Júlia', "age": 37, },
            )
            result_2 = cursor.executemany(sql, data_1)

        connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'select * from {TABLE_NAME}'
        )
        cursor.execute(sql)
        receive_data = cursor.fetchall()
        print(*receive_data, sep='\n')
