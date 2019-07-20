foods_list = {}
for i in range(4):
    j = i + 1
    foods_list[j] = str(input('Enter favourite food : '))
print(foods_list)
del foods_list[int(input('Enter food number to delete it : '))]
print(sorted(foods_list.keys()))
