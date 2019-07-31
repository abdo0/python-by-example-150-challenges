array_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print('       row0 row1 row2')
for i in array_list:
    print('column', i)
column = int(input('Please select a COLUMN from array above : '))
row = int(input('Please select a ROW number from array above : '))
print('the value in [{0}][{1}] = {2}'.format(row, column, array_list[column][row]))
