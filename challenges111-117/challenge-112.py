file_read = open('Books.csv', 'r')
for row in file_read:
    print(row)
file_read.close()

ask_name = str(input('Enter Book Name : '))
ask_author = str(input('Enter Book Author : '))
ask_year = str(input('Enter Book Year Released : '))
file_write = open('Books.csv', 'a')
file_write.write(ask_name + ', ' + ask_author + ', ' + ask_year + '\n')
file_write.close()

file_read_last = open('Books.csv', 'r')
for row in file_read_last:
    print(row)
file_read_last.close()
