array_list = {}
for i in range(4):
    name = str(input('Enter name to add : '))
    age = int(input('Enter age to add : '))
    shoe_size = int(input('Enter shoe size to add : '))
    array_list[name] = {}
    array_list[name]['age'] = age
    array_list[name]['shoe_size'] = shoe_size
for i in array_list:
    print(i)
name_ask = str(input('Enter name to remove : '))
del array_list[name_ask]
for i in array_list:
    print(i)
