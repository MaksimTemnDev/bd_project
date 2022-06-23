import pymysql 
from config import host, user, password, db_name
#import mysql.connector
#from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = pymysql.connect(
            host=host,
            port = 3306,
            user=user,
            passwd=password,
            database = db_name,
            cursorclass = pymysql.cursors.DictCursor
        )
        print("Connection to MySQL DB successful")
    except Exception  as e:
        print("Connection refused...")
        print(e)
    return connection


play = 1
man_id = 11
connect = create_connection()
with connect.cursor() as cursor:
        while play == 1:
            print(" ")
            print("Введите 0 чтобы увидеть список таблиц")
            print("Введите 1 чтобы редактировать одну из таблиц")
            print("Введите 2 чтобы добавить запись в одну из таблиц")
            print("Введите 3 чтобы удалить запись в одной из таблиц")
            print("Введите 4 чтобы узнать какие автомобили продал конкретный менеджер")
            print("Введите 5 чтобы узнать какие модели представлены у конкретного бренда")
            print("Введите имя таблицы чтобы увидеть  ее название")
            print("Для выхода введитпе -1")
            inp = input()
            if inp == '0':
                show_all()
            elif inp == '-1':
                play = -1
            elif inp == '1':
                print("Выберите какую таблицу редактировать:")
                print("введите 1 для brand")
                print("введите 2 для model")
                inp = input()
                change_table(inp)
            elif inp == '2':
                print("Выберите в какую таблицу добавить:")
                print("введите 1 для client")
                print("введите 2 для manager")
                inp = input()
                inserting_table(inp, man_id)
            elif inp == '3':
                print("Выберите из какой таблицы удалять:")
                print("введите 1 для client")
                print("введите 2 для manager")
                inp = input()
                table_drop(inp)
            elif inp == '4':
                find_in_base("manager")
                print("Выберите имя менеджера:")
                inp = input()
                show_manager_cars(inp)
            elif inp == '5':
                print("Выберите бренд:")
                inp = input()
                show_models(inp)
            elif isinstance(inp, str):
                find_in_base(inp)
connect.close()