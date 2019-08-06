import sqlite3
from sqlite3 import Error


def create_connection(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)
    return None


def show_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM PhoneBook")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def view_phone_book(conn, phone_id):
    cur = conn.cursor()
    cur.execute(str("SELECT * FROM PhoneBook WHERE id = " + str(phone_id)))
    print(cur.fetchone())
    cur.close()


def add_phone_book(conn, phone_book):
    sql = ''' INSERT INTO PhoneBook(first_name,surname,phone)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, phone_book)
    print(cur.fetchone())
    cur.close()


def surname_in_phone_book(conn, surname):
    sql = "SELECT * FROM  PhoneBook WHERE surname like '%" + surname + "%'"
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)


def delete_phone_book(conn, phone_id):
    cur = conn.cursor()
    cur.execute(str("DELETE FROM tasks WHERE id = " + str(phone_id)))
    cur.close()


def main():

    conn = create_connection('python-by-example.db')

    with conn:
        print('\n\nMain Menu\n\n\n')
        print('1) View phone book ')
        print('2) Add to phone book')
        print('3) Search for surname')
        print('4) Delete person from phone book')
        print('5) Quit')
        operation_ask = int(input('Enter your selection : '))
        if operation_ask == 1:
            ask_id = int(input('Enter id to show : '))
            view_phone_book(conn, ask_id)
        elif operation_ask == 2:
            ask_name = str(input('Enter name : '))
            ask_surname = str(input('Enter surname : '))
            ask_phone = str(input('Enter phone : '))
            phone_book = (ask_name, ask_surname, ask_phone)
            add_phone_book(conn, phone_book)
        elif operation_ask == 3:
            ask_surname = str(input('Enter surname to show : '))
            surname_in_phone_book(conn, ask_surname)
        elif operation_ask == 4:
            ask_id = int(input('Enter id to delete : '))
            delete_phone_book(conn, ask_id)
        else:
            print('Invalid input, please try again.')


main()
