import random

choose = random.choice(['h', 't'])
ask = str(input('Choose heads or tails against computer! h|t : '))
if choose == ask:
    print('You win')
else:
    print('Bad luck')
print('computer choose is {0}'.format(choose))
