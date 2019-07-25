import array as arr
import random

newArray = arr.array('i', [])
for i in range(5):
    random_number = random.randint(0, 7234)
    newArray.append(random_number)
for j in newArray:
    print(j)
