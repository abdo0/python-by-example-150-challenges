nums = []
count = 0
remove = False
while not remove:
    if count == 3:
        ask = str(input('Do you still want the last number they entered saved? yes|no : ')).lower()
        if ask == 'no':
            nums.pop(count-1)
        remove = True
    else:
        nums.append(int(input('Enter number : ')))
    count = count + 1
print(nums)
