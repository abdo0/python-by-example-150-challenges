file_read = open('Books.csv', 'r')
for row in file_read:
    print(row)
file_read.close()

ask_count_books = int(input('Enter how many books you want to add to file : '))
for i in range(ask_count_books):
    ask_name = str(input('Enter Book Name : '))
    ask_author = str(input('Enter Book Author : '))
    ask_year = str(input('Enter Book Year Released : '))
    file_write = open('Books.csv', 'a')
    file_write.write(ask_name + ', ' + ask_author + ', ' + ask_year + '\n')
    file_write.close()


ask_author_to_show = str(input('Enter Book Author to show : '))
file_read = open('Books.csv', 'r')
for row in file_read:
    if ask_author_to_show in row:
        print(row)
file_read.close()
