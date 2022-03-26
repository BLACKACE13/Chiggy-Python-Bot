import mysql.connector as mc
import os
from py_dotenv import read_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
read_dotenv(dotenv_path)


def create_conn():
    conn = mc.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        database=os.getenv("database"),
        autocommit = True
    )
    return conn
