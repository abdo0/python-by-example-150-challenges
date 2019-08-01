count = 0
while count < 5:
    print('1) Create a new file')
    print('2) Display the file')
    print('3) Add a new item to the file ')
    selection_input = int(input('Make a selection 1, 2 or 3 : '))
    if selection_input == 1:
        file = open('Subject.txt', 'w')
        subject_name = str(input('Enter school subject name : '))
        file.write(subject_name + '\n')
        file.close()
    elif selection_input == 2:
        file = open('Subject.txt', 'r')
        print(file.read())
        file.close()
    elif selection_input == 3:
        file = open('Subject.txt', 'a')
        subject_name = str(input('Enter school subject name to add into file : '))
        file.write(subject_name + '\n')
        file.close()
    count = count + 1

file = open('Subject.txt', 'r')
print(file.read())
file.close()
