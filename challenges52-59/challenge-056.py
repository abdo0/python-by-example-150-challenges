import random

choose = random.randint(1, 10)
ask = 0
while choose != ask:
    ask = int(input('Choose number from (1-10) to guess computer number ! : '))
print('Correct number {0}'.format(choose))
