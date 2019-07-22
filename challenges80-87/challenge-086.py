password = str(input('Enter password : '))
re_password = str(input('Re-enter password : '))
if password == re_password:
    print('Thank you')
elif password != re_password:
    print('They must be in the same case')
else:
    print('Incorrect')
