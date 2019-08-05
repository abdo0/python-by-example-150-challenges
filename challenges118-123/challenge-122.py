def add_to_file():
    name = str(input('Enter name : '))
    salary = str(input('Enter salary : '))
    file = open('Salaries.csv', 'a')
    file.write(str(name + ', ' + salary + '\n'))
    file.close()


def view_file():
    file = open('Salaries.csv', 'r')
    count_row = 0
    for row in file:
        print('Row  ' + str(count_row) + ' : ' + str(row))
        count_row += 1


def main():
    state = True
    count = 0
    while state:
        if count != 3:
            print('1) Add to file')
            print('2) View all records')
            print('3) Quit')
            operation_ask = int(input('Enter the number of your selection : '))
            if operation_ask == 1:
                add_to_file()
            elif operation_ask == 2:
                view_file()
            elif operation_ask == 3:
                print('Good bye')
                state = False
            else:
                print('Invalid input, please try again.')
        else:
            state = False


main()
