file = open('Names.txt', 'r')
print(file.read())
file.close()
file2 = open('Names2.txt', 'w')
file2.close()
ask = str(input('Enter one of names : '))
with open('Names.txt', 'rt') as myFile:
    for myLine in myFile:
        if myLine != ask:
            file2 = open('Names2.txt', 'a')
            file2.write(myLine + '\n')
            file2.close()
myFile.close()
file = open('Names2.txt', 'r')
print(file.read())
