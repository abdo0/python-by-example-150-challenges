array_list = {
    'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
    'Tom':  {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
    'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
    'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
}
print('Regions are : N, S, E, W')
print('Names Are : ')
for i in array_list:
    print(i)
region_ask = str(input('Please enter region : ')).upper()
name_ask = str(input('Please enter name : ').capitalize())
print(array_list[name_ask][region_ask])
user_ask = str(input('Would like to change value of this position? yes|no : '))
if user_ask == 'yes':
    edit_ask = int(input('Enter number to replace for this position : '))
    array_list[name_ask][region_ask] = edit_ask
print(array_list[name_ask])
