name_list = []
for i in range(3):
    name_list.append(str(input('Enter name to invite to party : ')))
print(name_list)
add_more = str(input('Enter more people to party? yes|no : ').lower())
while add_more == 'yes':
    name_list.append(str(input('Enter name to invite to party : ')))
    add_more = str(input('Enter more people to party? yes|no : ').lower())
print(len(name_list))
