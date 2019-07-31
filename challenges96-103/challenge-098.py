array_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print('       row0 row1 row2')
for i in array_list:
    print('column', i)
row_ask = int(input('Enter row number to display? : '))
print(array_list[row_ask])
add_ask = int(input('Enter number to add to array : '))
array_list[row_ask].append(add_ask)
print('       row0 row1 row2')
for i in array_list:
    print('column', i)
