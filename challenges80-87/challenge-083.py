string = str(input('Please enter word in upper case ? '))
is_upper = False
while not is_upper:
    if string.isupper():
        is_upper = True
    else:
        string = str(input('Sorry not all in upper case, please enter word in upper case ? '))
print(string)
