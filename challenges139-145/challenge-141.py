import sqlite3
from sqlite3 import Error


def create_connection(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)
    return None


def create_author_table(conn):
    try:
        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS authors (
                                        name text PRIMARY KEY,
                                        birth_place text
                                    ); """
        cur = conn.cursor()
        cur.execute(sql_create_projects_table)
        cur.close()
    except Error as e:
        print(e)


def create_books_table(conn):
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS books (
                                        id integer PRIMARY KEY,
                                        title text NOT NULL,
                                        author text,
                                        published_date text
                                    ); """
    cur = conn.cursor()
    cur.execute(sql_create_projects_table)
    cur.close()


def insert_to_authors(conn, authors):
    cur = conn.cursor()
    for author in authors:
        sql = 'INSERT INTO authors (name, birth_place) VALUES (?, ?)'
        cur.execute(sql, author)
        conn.commit()
    cur.close()


def insert_to_books(conn, books):
    cur = conn.cursor()
    for book in books:
        sql = 'INSERT INTO books (title, author, published_date) VALUES (?, ?, ?)'
        cur.execute(sql, book)
        print(cur.fetchone())
    cur.close()


def main():

    conn = create_connection('BookInfo.db')

    with conn:
        create_author_table(conn)
        create_books_table(conn)

        authors = [
            ['Agatha Christie', 'Torquay'],
            ['Cecelia Ahern', 'Dublin'],
            ['J.K, Rowling', 'Bristol'],
            ['Oscar Wilde', 'Dublin']
        ]

        insert_to_authors(conn, authors)

        books = [
            ['De Profundis', 'Oscar Wilde', '1905'],
            ['Harry Potter and the chamber of secrets', 'J.K. Rowling', '1998'],
            ['Harry Potter and the prisoner or Azkaban', 'J.K. Rowling', '1999'],
            ['Lyrebird', 'Cecelia Ahren', '2017'],
            ['Murder At the Orient Express', 'Agatha Christie', '1934'],
            ['Perfect', 'Cecelia Ahren', '2017'],
            ['The marble collector', 'Cecelia Ahren', '2016'],
            ['The murder on the links', 'Agatha Christie', '1923'],
            ['The picture of Dorian Gray', 'Oscar Wilde', '1890'],
            ['The secret adversary', 'Agatha Christie', '1921'],
            ['The seven dials mystery', 'Agatha Christie', '1929'],
            ['The year i met you', 'Cecelia Ahren', '2014']
        ]

        insert_to_books(conn, books)


main()
