import csv

file_read = list(csv.reader(open('Books.csv')))
count_row = 0
list = []
for row in file_read:
    print('Row  ' + str(count_row) + ' : ' + str(row))
    list.append(row)
    count_row += 1

ask = int(input('Enter row number to delete : '))
list.pop(ask)

count_row = 0
for row in list:
    print('Row  ' + str(count_row) + ' : ' + str(row))
    count_row += 1

ask = int(input('Enter row number to edit : '))
print('1) Edit book name')
print('2) Edit author')
print('3) Release Year ')
selection_input = int(input('Make a selection 1, 2 or 3 : '))
if selection_input == 1:
    ask_name = str(input('Enter Book Name : '))
    list[ask][0] = ask_name
elif selection_input == 2:
    ask_author = str(input('Enter Book Author : '))
    list[ask][1] = ask_author
elif selection_input == 3:
    ask_year = str(input('Enter Book Year Released : '))
    list[ask][2] = ask_year


i = 0
file_write = open('Books.csv', 'w')
for row in range(len(list)):
    file_write.write(list[i][0] + ', ' + list[i][1] + ', ' + list[i][2] + '\n')
    i += 1
file_write.close()
