import random

color = ['red', 'blue', 'green', 'orange', 'black']
select_color = random.choice(color)
ask = 0
while select_color != ask:
    ask = str(input('Choose colour to guess computer colour! : '))
    if select_color != ask:
        print('You are probably feeling {0} right now'.format(select_color))
print('Well done')
