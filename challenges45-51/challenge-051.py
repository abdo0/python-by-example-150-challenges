number = 10
while number > 0:
    print('There are {0} green bottles hanging in the wall'.format(number))
    print('and if 1 green bottle should accidentally fall')
    number = number - 1
    answer = int(input('How many green bottles will be hanging on the wall?'))
    if answer == number:
        print('There will be {0} green bottles hanging on the wall')
    else:
        while answer != number:
            answer = int(input('No, try again : '))
print('There are no more green bottles hanging on the wall')
