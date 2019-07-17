answer = str(input('is it raining? yes|no : '))
answer = answer.lower()
if answer == 'yes':
    windy = str(input('is it windy! yes|no : '))
    windy = windy.lower()
    if windy == 'yes':
        print('It is too windy for umbrella')
    else:
        print('Take an umbrella')
else:
    print('Enjoy your day')
