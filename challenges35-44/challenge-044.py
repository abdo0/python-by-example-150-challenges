people = int(input('Please enter number of people want to invite to party : '))
if people < 10:
    for i in range(0, people):
        name = str(input('Please enter name : '))
        print('{0} has been invited'.format(name))
else:
    print('Too many people')
