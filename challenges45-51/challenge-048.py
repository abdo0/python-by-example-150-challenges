count = 0
choose = str(input('Would you like to add person y|n : '))
while choose == 'y':
    name = str(input('Enter name : '))
    print('{0} has been invited'.format(name))
    count = count + 1
    choose = str(input('Do you want to add another person y|n : '))
print('The number of people that invited to party is {0}'.format(count))
