number_list = ['134', '762', '356']
for i in number_list:
    print(i)
append_to_list = int(input('Enter number to add to list : '))
if append_to_list not in number_list:
    print('This is not in the list')
    number_list.append(append_to_list)
else:
    print('This is in the list, could not add')
    print(number_list.index(append_to_list))
