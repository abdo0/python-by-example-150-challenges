import array as arr

store_array = arr.array('i', [])
for i in range(5):
    store_number = int(input('Enter number to store in array : '))
    store_array.append(store_number)
store_array = sorted(store_array)
print(store_array)
remove_number = int(input('Enter the number that'))
store_array.remove(remove_number)
