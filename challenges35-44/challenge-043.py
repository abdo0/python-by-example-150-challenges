direction = str(input('Enter direction? up|down : '))
if direction.lower() == 'up':
    top = int(input("Please enter top number to start count todow!"))
    for i in range(0, top+1):
        print(i)
elif direction.lower() == 'down':
    below = int(input('Please enter number below 20!'))
    for i in range(20, below-1, -1):
        print(i)
else:
    print('I don\'t understand')
