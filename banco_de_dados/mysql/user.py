import pymysql
import dotenv
import os

DEBUG = 0

dotenv.load_dotenv()

TABLE_NAME = 'user'

connection = pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_ROOT_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
    cursorclass=None,
)

