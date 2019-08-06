import sqlite3
from sqlite3 import Error


def create_connection(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)
    return None


def create_phone_book_table(conn):
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS PhoneBook (
                                        id integer PRIMARY KEY,
                                        first_name text NOT NULL,
                                        surname text,
                                        phone integer
                                    ); """
    cur = conn.cursor()
    cur.execute(sql_create_projects_table)
    cur.close()


def create_phone_book_record(conn, phone_book):
    sql = ''' INSERT INTO PhoneBook(first_name,surname,phone)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, phone_book)
    cur.close()
    return cur.lastrowid


def main():
    conn = create_connection('python-by-example.db')

    with conn:
        create_phone_book_table(conn)

        phone_book_record_1 = ('Simon',  'Howels',  '01223349752')
        phone_book_record_2 = ('Karen',  'Philips', '01954295773')
        phone_book_record_3 = ('Darren', 'Smith',   '01583749012')
        phone_book_record_4 = ('Anne',   'Jones',   '01323567322')
        phone_book_record_5 = ('Mark',   'Smith',   '01223855534')

        create_phone_book_record(conn, phone_book_record_1)
        create_phone_book_record(conn, phone_book_record_2)
        create_phone_book_record(conn, phone_book_record_3)
        create_phone_book_record(conn, phone_book_record_4)
        create_phone_book_record(conn, phone_book_record_5)


main()
