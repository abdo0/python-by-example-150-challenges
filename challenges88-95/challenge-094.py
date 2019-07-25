import array as arr

view_array = arr.array('i', [11, 22, 33, 44, 55])
print(view_array)
ask = int(input('Enter number to see index : '))
while ask not in view_array:
    ask = int(input('Enter number to see index : '))
print(view_array.index(ask))
