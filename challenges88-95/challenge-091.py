import array as arr

store_array = arr.array('i', [])
for i in range(4):
    store_number = int(input('Enter number to add to array : '))
    store_array.append(store_number)
repeat_number = store_array[1]
store_array.append(repeat_number)
print(store_array)
check_number = int(input('Enter number from array to see how many it repeated! : '))
print(store_array.count(check_number))
