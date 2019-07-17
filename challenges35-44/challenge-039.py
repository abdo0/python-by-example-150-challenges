number = int(input('Enter number between 1 and 12 : '))
for i in range(1, 13):
    result = i * number
    print('{0} x {1} is {2}'.format(i, number, result))
