number = int(input('Enter number between (10 - 20) : '))
while  10 > number or number > 20:
    if number < 10:
        print('Too low')
    else:
        print('Too high')
    number = int(input('Try again, enter number between (10 - 20) : '))
print('Thank you')
