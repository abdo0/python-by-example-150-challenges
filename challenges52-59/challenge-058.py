import random

count = 0
point = 0
while count < 5:
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    result = number_1 + number_2
    answer = int(input('Enter the result for {0} + {1} = '.format(number_1, number_2)))
    if answer == result:
        point = point + 1
    count = count + 1
print('Your points is {0}/5'.format(point))
