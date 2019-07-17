color = str(input('Enter you favourite colour : '))
if color == 'red':
    print('I like red too')
elif color == 'RED':
    print('I like red too')
elif color == 'Red':
    print('I like red too')
else:
    print('I don\'t like {0}, I prefer red'.format(color))
