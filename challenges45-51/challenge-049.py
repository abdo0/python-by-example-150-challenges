compnum = 50
count = 0
number = int(input('Enter number to guess : '))
while number != compnum:
    if number > compnum:
        print('The number is to high')
    else:
        print('The number is to low')
    count = count + 1
    number = int(input('Enter number to guess : '))
print('Well done, you took {0}'.format(count))
