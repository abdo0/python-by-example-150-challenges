import sqlite3
from sqlite3 import Error


def create_connection(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)
    return None


def show_all_authors(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM authors")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def search_place_birth(conn, place):
    cur = conn.cursor()
    cur.execute(str("select books.title, books.published_date, authors.name from authors join books on books.author = authors.name where authors.birth_place = '" + place + "'"))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()


def main():

    conn = create_connection('BookInfo.db')

    with conn:
        print('\n\nMain Menu\n\n\n')
        print('1) List authors ')
        print('2) Search place of birth')
        print('3) Quit')
        operation_ask = int(input('Enter your selection : '))
        if operation_ask == 1:
            show_all_authors(conn)
        elif operation_ask == 2:
            ask_place = str(input('Enter place of birth : '))
            search_place_birth(conn, ask_place)
        else:
            print('Invalid input, please try again.')


main()
