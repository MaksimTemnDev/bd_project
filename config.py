import pymysql

host = "127.0.0.1"
user = "root"
password = "1234"
db_name = "origin"

class BaseControl:
    @staticmethod
    def rows(show_rows, cursor):
        cursor.execute(show_rows)
        rows = cursor.fetchall()
        return rows