import pymysql 
from config import host, user, password, db_name
import config

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

def show_all(cursor):
        show_rows = "SHOW TABLES FROM `origin`"
        rows = control.rows(show_rows, cursor)
        i = 1;
        print(" ")
        print("Tables list:")
        print('#'*25)
        for row in rows:
            print(row['Tables_in_origin'])
            i+=1
        print('#'*25)
        print(" ")

def find_in_base(name):
    has_strt = 0
    if name == "auto":
        show_rows = "SELECT * FROM `origin`.`auto`"
        rows = control.rows(show_rows, cursor)
        i = 1;
        print("Unicue number")
        print('#'*25)
        for row in rows:
            print(row["UnicueNumber"])
            i+=1
        print('#'*25)
    elif name == "brand":
        show_rows = "SELECT * FROM `origin`.`brand`"
        rows = control.rows(show_rows, cursor)
        i = 1;
        print(" ")
        print("Denomination")
        print('#'*25)
        for row in rows:
            print(row["denomination"])
            i+=1
        print('#'*25)
    elif name == "client":
        show_rows = "SELECT * FROM `origin`.`client`"
        rows = control.rows(show_rows, cursor)
        i = 1;
        print(" ")
        print("Name")
        print('#'*25)
        for row in rows:
            print(row["name"])
            i+=1
        print('#'*25)
    elif name == "manager":
        show_rows = "SELECT * FROM `origin`.`manager`"
        #cursor.execute(show_rows)
        #rows = cursor.fetchall()
        rows = control.rows(show_rows, cursor)
        i = 1;
        print(" ")
        print("Name")
        print('#'*25)
        for row in rows:
            print(row["name"])
            i+=1
        print('#'*25)
    elif name == "equipment":
        show_rows = "SELECT * FROM `origin`.`equipment`"
        rows = control.rows(show_rows, cursor)
        i = 1;
        print(" ")
        print("Cabin    Wheels    Transmission    Carcase    Climatic control")
        print('#'*25)
        for row in rows:
            print(row["cabin"], row["wheels"], row["transmission"], row["carcase"], row["climatic_control"])
            i+=1
        print('#'*25)
    elif name == "model":
        show_rows = "SELECT * FROM `origin`.`model`"
        rows = control.rows(show_rows, cursor)
        i = 1;
        print(" ")
        print("Denomination")
        print('#'*25)
        for row in rows:
            print(row["denomination"])
            i+=1
        print('#'*25)
    elif name == "position":
        show_rows = "SELECT * FROM `origin`.`position`"
        rows = control.rows(show_rows, cursor)
        i = 1;
        print(" ")
        print("Denomination")
        print('#'*25)
        for row in rows:
            print(row["denomenation"])
            i+=1
        print('#'*25)
    elif name == "delivery":
        show_rows = "SELECT * FROM `origin`.`delivery`"
        rows = control.rows(show_rows, cursor)
        i = 1;
        print(" ")
        print("Date")
        print('#'*25)
        for row in rows:
            print(row["date"])
            i+=1
        print('#'*25)
    elif name == "deal":
        show_rows = "SELECT * FROM `origin`.`deal`"
        rows = control.rows(show_rows, cursor)
        i = 1;
        print(" ")
        print("Date")
        print('#'*25)
        for row in rows:
            print(row["dateOfIssue"])
            i+=1
        print('#'*25)
    elif name == "engine":
        show_rows = "SELECT * FROM `origin`.`engine`" 
        rows = control.rows(show_rows, cursor)
        i = 1;
        print(" ")
        print("Fuel    Part number   Power")
        print('#'*25)
        for row in rows:
            print(row["fuel"], row["partNumber"], row["horsePower"])
            i+=1
        print('#'*25)
    elif name == "tipeofpayment":
        show_rows = "SELECT * FROM `origin`.`tipeofpayment`"
        rows = control.rows(show_rows, cursor)
        i = 1;
        print(" ")
        print("Type of pay   Manager bonus   Procent of sale")
        print('#'*25)
        for row in rows:
            print(row["denomination"], row["SizeOfManagersBonus"], row["ProcentOfSale"])
            i+=1
        print('#'*25)
    print(" ")

def change_table(naming):
    if naming == "1":
        print(" ")
        print("List of columns")
        print('#'*25)
        print("denomination")
        print('#'*25)
        print(" ")
        print("Введите новое значения denomination:")
        condition1 = input()
        print("Введите значение, которое хотите заменить:")
        mean = input()
        try:
            set_update = "update brand set denomination = '%s' where  denomination = '%s';"%(condition1, mean)
            #cursor.execute(set_update)
            control.rows(set_update, cursor)
            connect.commit()
        except Exception  as e:
            print("Ваш запрос синтаксически не правильный")
            print(e)
            print(" ")
    elif naming == "2":
        print(" ")
        print("List of columns")
        print('#'*25)
        print("denomination")
        print('#'*25)
        print(" ")
        print("Введите новое значения denomination:")
        condition1 = input()
        print("Введите значение, которое хотите заменить:")
        mean = input()
        try:
            set_update = "update model set denomination = '%s' where  denomination = '%s';"%(condition1, mean)
            control.rows(set_update, cursor)
            connect.commit()
        except Exception  as e:
            print("Ваш запрос синтаксически не правильный")
            print(e)
            print(" ")

def inserting_table(inp, man_id):
    if inp == "1":
        print(" ")
        print("List of columns")
        print('#'*25)
        print("name")
        print('#'*25)
        print(" ")
        print("Введите значения для новой записи в том же порядке что и указан в списке столбцов:")
        name = input()
        clientId = man_id
        try:
                man_id = man_id + 1
                set_update = "insert into origin.client(name, clientId) VALUES('%s',%s);"%(name, clientId)
                #cursor.execute(set_update)
                control.rows(set_update, cursor)
                connect.commit()
        except Exception  as e:
                print("Ваш запрос синтаксически не правильный")
                print(e)
                print(" ")
    elif inp == '2':
        print(" ")
        print("List of columns")
        print('#'*25)
        print("name position")
        print('#'*25)
        print(" ")
        print("Введите значения для новой записи в том же порядке что и указан в списке столбцов:")
        name = input()
        positionId = input()
        try:
                man_id = man_id + 1
                set_update = "insert into origin.manager(name, managerId, positionId) VALUES('%s',%s,%s);"%(name, man_id, positionId)
                #cursor.execute(set_update)
                control.rows(set_update, cursor)
                connect.commit()
        except Exception  as e:
                print("Ваш запрос синтаксически не правильный")
                print(e)
                print(" ")
    return man_id
        
def table_drop(inp):
    if inp == "1":
        print(" ")
        print("Введите значение для удаляемой записи(name):")
        name = input()
        try:
                set_update = "delete from origin.client where name = '%s';"%(name)
                #cursor.execute(set_update)
                control.rows(set_update, cursor)
                connect.commit()
        except Exception  as e:
                print("Ваш запрос синтаксически не правильный")
                print(e)
                print(" ")
    elif inp == '2':
        print(" ")
        print("Введите значение для удаляемой записи(name):")
        name = input()
        try:
                set_update = "delete from origin.manager where name = '%s';"%(name)
                #cursor.execute(set_update)
                control.rows(set_update, cursor)
                connect.commit()
        except Exception  as e:
                print("Ваш запрос синтаксически не правильный")
                print(e)
                print(" ")

def show_manager_cars(inp):
    try:
        set_update = "select brand.denomination, model.denomination from manager left join deal on manager.managerId = deal.managerId left join auto on deal.dealId = auto.autoId left join equipment on auto.unicueNumber = equipment.id left join model on equipment.modelId = model.modelId left join brand on model.brandId = brand.brandId where manager.name = '%s';"%(inp)
        rows = control.rows(set_update, cursor)
        i = 1;
        print(" ")
        print("List of cars")
        print('#'*25)
        for row in rows:
            print(row["denomination"], row["model.denomination"])
            i+=1
        print('#'*25)
        print(" ")
    except Exception  as e:
        print("Ваш запрос синтаксически не правильный")
        print(e)
        print(" ")

def show_models(mark):
    try:
        set_show = "select model.denomination from model right join brand on model.brandId=brand.brandId where brand.denomination='%s';"%mark
        rows = control.rows(set_show, cursor)
        print(" ")
        print("List of models")
        print('#'*25)
        for row in rows:
            print(row["denomination"])
        print('#'*25)
        print(" ")
    except Exception  as e:
        print("Ваш запрос синтаксически не правильный")
        print(e)
        print(" ")

def show_info_cars():
    set_show = "select brand.denomination, model.denomination, deal.dateOfIssue, equipment.transmission, engine.fuel, engine.horsePower from deal left join auto on deal.dealid = auto.autoId left join equipment on auto.UnicueNumber = equipment.id left join engine on equipment.engineId = engine.engineId left join model on equipment.modelId = model.modelId left join brand on model.brandId = brand.brandId;"
    rows = control.rows(set_show, cursor)
    print(" ")
    print("brand   model    date of issue    transmission   fuel    horse power")
    print('#'*50)
    for row in rows:
        print(row["denomination"], row['model.denomination'], row["dateOfIssue"], row["transmission"], row['fuel'], row["horsePower"])
    print('#'*50)
    print(" ")

def show_managers_bonus(inf):
    set_show = "select sum(SizeOfManagersBonus) from tipeofpayment left join deal on tipeofpayment.tipeOfPaymentId = deal.paymentId left join manager on deal.managerId = manager.managerId where name = '%s';"%(inf)
    rows = control.rows(set_show, cursor)
    print(" ")
    print("name          bonus")
    print('#'*25)
    for row in rows:
        print(inf, "  ", row['sum(SizeOfManagersBonus)'])
    print('#'*25)
    print(" ")

def show_position(inp):
    set_show = "select manager.name, position.denomenation from manager join position on manager.positionId = position.positionid where manager.name = '%s';"%(inp)
    rows = control.rows(set_show, cursor)
    print(" ")
    print("name          position")
    print('#'*25)
    for row in rows:
        print(row['name'], row['denomenation'])
    print('#'*25)
    print(" ")


play = 1
man_id = 11
connect = create_connection()
control = config.BaseControl()
with connect.cursor() as cursor:
        while play == 1:
            print(" ")
            print("Введите 0 чтобы увидеть список таблиц")
            print("Введите 1 чтобы редактировать одну из таблиц")
            print("Введите 2 чтобы добавить запись в одну из таблиц")
            print("Введите 3 чтобы удалить запись в одной из таблиц")
            print("Введите 4 чтобы узнать какие автомобили продал конкретный менеджер")
            print("Введите 5 чтобы узнать какие модели представлены у конкретного бренда")
            print("Введите 6 чтобы узнать информацию о каждом проданном автомобиле")
            print("Введите 7 чтобы узнать сколько бонусов заработал определенный менеджер")
            print("Введите 8 чтобы узнать должность определенного менеджера")
            print("Введите имя таблицы чтобы увидеть  ее название")
            print("Для выхода введитпе -1")
            try:
                inp = input()
                connect.commit()
                if inp == '0':
                    show_all(cursor)
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
                    man_id = inserting_table(inp, man_id)
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
                    find_in_base("brand")
                    print("Выберите бренд:")
                    inp = input()
                    show_models(inp)
                elif inp == '6':
                    show_info_cars()
                elif inp == '7':
                    find_in_base("manager")
                    print("Выберите имя менеджера:")
                    inp = input()
                    show_managers_bonus(inp)
                elif inp == '8':
                    find_in_base("manager")
                    print("Выберите имя менеджера:")
                    inp = input()
                    show_position(inp)
                elif isinstance(inp, str):
                    find_in_base(inp)
            except Exception  as e:
                print(" ")
connect.close()