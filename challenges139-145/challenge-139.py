import sqlite3

with sqlite3.connect('python-by-example') as db:
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
                                                    id integer PRIMARY KEY,
                                                    name text NOT NULL,
                                                    dept text NOT NULL,
                                                    salary integer);""")
    cursor.execute("""INSERT INTO employees(id,name,dept,salary)
                        VALUES("1","Bob","Sales","25000")""")
    db.commit()
