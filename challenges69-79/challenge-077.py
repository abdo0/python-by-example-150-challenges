name_list = []
for i in range(3):
    name_list.append(str(input('Enter name to invite to party : ')))
print(name_list)
add_more = str(input('Enter more people to party? yes|no : ').lower())
while add_more == 'yes':
    name_list.append(str(input('Enter name to invite to party : ')))
    add_more = str(input('Enter more people to party? yes|no : ').lower())
print(name_list)
name_list_index = str(input('Enter name to show it position in list : '))
print(name_list.index(name_list_index))
name_list_index_remove = str(input('Would like this person to come to party? yes|no : '))
if name_list_index_remove == 'yes':
    name_list.remove(name_list_index)
print(name_list)
