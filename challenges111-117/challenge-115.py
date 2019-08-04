file_read = open('Books.csv', 'r')
count_row = 0
for row in file_read:
    print('Row  ' + str(count_row) + ' : '+row)
    count_row += 1
file_read.close()
