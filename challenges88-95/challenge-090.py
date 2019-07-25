import array as arr

storeArray = arr.array('i', [])
loopNumber5 = True
while loopNumber5:
    storeNumber = int(input('Enter number to store in array : '))
    if 10 < storeNumber < 20:
        storeArray.append(storeNumber)
    else:
        print('Outside the range')

    if len(storeArray) == 5:
        loopNumber5 = False
print('Thank you')
for i in storeArray:
    print(i)
