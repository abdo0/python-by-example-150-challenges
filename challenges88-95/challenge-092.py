import array as arr
import random

array1 = arr.array('i', [])
array2 = arr.array('i', [])
for i in range(5):
    if i < 3:
        array1_number = int(input('Enter number to store in array : '))
        array1.append(array1_number)
    array2_number = random.randint(0, 100)
    array2.append(array2_number)
array1.extend(array2)
print(sorted(array1))
