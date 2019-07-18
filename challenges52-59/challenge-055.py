import random

choose = random.randint(1, 5)
ask = int(input('Choose number from (1-5) against computer! : '))
if choose > ask:
    print('Too low')
elif choose < ask:
    print('Too high')
else:
    print('Well done')
ask = int(input('Choose second number from (1-5) against computer! : '))
if choose == ask:
    print('Correct')
else:
    print('You lose')
