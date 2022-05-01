
import psycopg2

def limit(cursor):
    print('сколько пользователей вы хотите вывести')
    x=input()
    cursor.execute('SELECT * FROM contacts LIMIT '+x)
    records = cursor.fetchall()
    for i in records:
        print(i)

def multiadd(conn,cursor):
    hold=[]
    cursor.execute('SELECT * FROM contacts LIMIT 10')
    records = cursor.fetchall()
    not_corr=[]
    while True:
        x=input().split()
        if len(x)<4:
            not_corr.append(x)
            break
        else:
            hold.append(x)
    for i in hold:
        check=True
        for j in records:
            if i[1]== j[1]:
                check=False
                break
        if check:
            postgres_insert_query = """ INSERT INTO contacts (user_id,last_name,first_name,phone_number) VALUES (%s,%s,%s,%s)"""
            record_to_insert = (i[0], i[1], i[2], i[3])
            cursor.execute(postgres_insert_query, record_to_insert)
            conn.commit()
        else:
            not_corr.append(i)
    print('неверные данные')
    print(not_corr)
    return True


def pattern(cursor):
    print('введите начало шаблона имени')
    y=input()
    cursor.execute('SELECT * FROM contacts LIMIT 10')
    print('все совпадения')
    records=cursor.fetchall()
    for i in records:
        if i[1][:len(y)]==y:
            print(i)
    return True


def delete(conn,cursor):
    print('удаление по номеру 1, по имени 2')
    x=input()
    if x == '1':
        x=input()
        sql_delete_query = """Delete from contacts where phone_number= %s"""
        cursor.execute(sql_delete_query, (x,))
        conn.commit()
    else:
        x=input()
        sql_delete_query = """Delete from contacts where last_name= %s"""
        cursor.execute(sql_delete_query, (x,))
        conn.commit()
    print("Удаление произошло успешно")

def update(conn,cursor):
    print('Введите ID контакта которог хотите обновить')
    x=int(input())

    print('что вы хотите обновить?')

    print('имя,фамилие,номер')
    y=input()

    print('введите на что хотите изменить')
    z=input()

    if y=='имя':
        sql_update_query = """Update contacts set first_name = %s where user_id = %s"""
        cursor.execute(sql_update_query, (z, x))
        conn.commit()

    elif y=='фамилие':
        sql_update_query = """Update contacts set last_name = %s where user_id = %s"""
        cursor.execute(sql_update_query, (z, x))
        conn.commit()

    else:
        sql_update_query = """Update contacts set phone_number = %s where user_id = %s"""
        cursor.execute(sql_update_query, (z, x))
        conn.commit()

    print('УСПЕШНО!')

def show(cursor):
    print('Напишите что вы хотите вывести')
    print('1:ID')
    print('2:first_name')
    print('3:all')
    print('4: phone numbers')
    cursor.execute('SELECT * FROM contacts LIMIT 10')
    records = cursor.fetchall()
    k=int(input())
    if k == 1:
        for row in records:
            print(row[0])
    elif k == 2:
        for row in records:
            print(row[1])
    elif k==3:
        for row in records:
            print(row)
    else:
        for row in records:
            print(row[3])


def add(conn,cursor):
    print('Введите ID,имя, фамилию и номер пользователя')
    z=input().split()
    check=True
    cursor.execute('SELECT * FROM contacts')
    records = cursor.fetchall()
    for i in records:
        
        if z[1]==i[1]:
            sql_update_query = """Update contacts set user_id = %s,first_name=%s,phone_number=%s where last_name = %s"""
            cursor.execute(sql_update_query, (z[0],z[2],z[3],z[1] ))
            conn.commit()
            check=False
            break
    
    if check:
        postgres_insert_query = """INSERT INTO contacts (user_id,last_name,first_name,phone_number) VALUES (%s,%s,%s,%s)"""
        record_to_insert = (z[0], z[1], z[2], z[3])
        cursor.execute(postgres_insert_query, record_to_insert)
        conn.commit()

    print( "УСПЕШНО!")


conn = psycopg2.connect("dbname=postgres user=postgres password=Zhako2002")
cursor = conn.cursor()
print('Выберите что вы хотите сделать:')
print('1:Добавить контакт')
print('2:Удалить контакт')
print('3:Показать контакты')
print('4:Обновить контакт')
print('5:Шаблон')
print('6:mutliadd')
print('7:limit')
choose=input()
if choose == '2':
    delete(conn,cursor)
elif choose == '1':
    add(conn,cursor)
elif choose=='3':
    show(cursor)
elif choose=='4':
    update(conn,cursor)
elif choose == '5':
    pattern(cursor)
elif choose=='6':
    multiadd(conn,cursor)
elif choose=='7':
    limit(cursor)


cursor.close()
conn.close()
