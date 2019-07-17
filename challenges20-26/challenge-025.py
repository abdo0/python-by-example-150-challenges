first_name = str(input('Enter your first name : '))
if len(first_name) < 5:
    surname = str(input('Enter your surname : '))
    compact = first_name.upper() + surname.upper()
    print(compact)
else:
    print(first_name.lower())
