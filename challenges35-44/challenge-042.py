total = 0
sub_total = 0
for i in range(0, 5):
    number = int(input('Enter a number : '))
    sub_total = sub_total + number
choose = str(input('Would you like to add numbers to total?   yes|no   : '))
if choose.lower() == 'yes':
    total = total + sub_total
    print(total)
else:
    print(total)
