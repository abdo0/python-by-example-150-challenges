number_1 = int(input('Enter 1st number : '))
number_2 = int(input('Enter 2nd number : '))
total = number_2 + number_1
choose = str(input('Do you want to add another number y|n : '))
while choose == 'y':
    number = int(input('Enter number : '))
    total = total + number
    choose = str(input('Do you want to add another number y|n : '))
print(total)
