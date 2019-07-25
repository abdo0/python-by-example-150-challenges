import array as arr

new_array = arr.array('i', [])
for i in range(5):
    num = int(input('Enter number to add to array : '))
    new_array.append(num)
new_array = sorted(new_array)
new_array.reverse()
print(new_array)
