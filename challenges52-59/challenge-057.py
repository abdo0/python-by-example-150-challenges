import random

choose = random.randint(1, 10)
ask = 0
while choose != ask:
    ask = int(input('Choose number from (1-10) to guess computer number ! : '))
    if choose > ask:
        print('Too low')
    elif choose < ask:
        print('Too high')
print('Correct number {0}'.format(choose))
