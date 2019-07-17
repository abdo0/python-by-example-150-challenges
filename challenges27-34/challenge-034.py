import math

print('1) Square\n2) Triangle')
choose = int(input('Enter a number : '))
if choose == 1:
    square = int(input('Enter square length side : '))
    area = square*square
    print('Square area is {0}'.format(area))
elif choose == 2:
    base = int(input('Enter triangle base : '))
    height = int(input('Enter triangle height : '))
    area = (base/2)*height
    print('Triangle area is {0}'.format(area))
else:
    print('Wrong choose')
