name = str(input('Enter your name : '))
number = int(input('Enter number  : '))
if number < 10:
    for i in range(0, number):
        print(name)
else:
    print('Too high')
