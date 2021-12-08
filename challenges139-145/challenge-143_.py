import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor=db.cursor()

selectionyear=int(input("Enter a year: "))
print()

cursor.execute("""SELECT Books.Title, Books.DatePublished, Books.Author 
FROM Books WHERE DatePublished >? ORDER BY DatePublished""", [selectionyear])

for x in cursor.fetchall():
    print(x)

db.close()