import psycopg2
import configSQL


def sql(sql_command):
    class connection:
        pass

    setattr(connection, 'close', lambda: None)
    try:
        connection = psycopg2.connect(
            host=configSQL.HOST,
            port=configSQL.PORT,
            user=configSQL.USER,
            password=configSQL.PASSWORD,
            database=configSQL.DATABASE,
        )
        connection.autocommit = True
        print('Connected')
        with connection.cursor() as cursor:
            cursor.execute(sql_command)
            try:
                return cursor.fetchall()
            except:
                pass

    except Exception as ex:
        print(ex)
    finally:
        connection.close()
        print('Closed')


def create_table():
    sql("CREATE TABLE comments (id serial PRIMARY KEY, name varchar(10) NOT NULL, email varchar(255) NOT NULL, "
        "text TEXT NOT NULL, date DATE NOT NULL, is_active boolean NOT NULL DEFAULT false)")


def create_comment(name, email, text, date):
    sql(f"INSERT INTO comments (name, email, text, date) VALUES ('{name}', '{email}', '{text}', '{date}')")


def select_comments():
    my_list = []
    result_list = sql(f"SELECT * FROM comments")
    for i in result_list:
        my_dict = dict()
        my_dict['name'] = i[1]
        my_dict['email'] = i[2]
        my_dict['text'] = i[3]
        my_dict['date'] = i[4]
        my_list.append(my_dict)
    return my_list


def del_comment(id_comment):
    sql(f"DELETE FROM comments WHERE id = '{id_comment}'")


def change_active(id_comment, value):
    sql(f"UPDATE comments SET is_active = '{value}' WHERE name = '{id_comment}'")


if __name__ == '__main__':
    print(select_comments())
