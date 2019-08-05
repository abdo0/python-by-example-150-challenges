def add_name():
    ask_name = str(input('Enter name to add to names list : '))
    names.append(ask_name)
    print_names()


def change_name():
    print_names()
    row_ask = int(input('Enter row number to change name : '))
    ask_name = str(input('Enter name : '))
    names[row_ask] = ask_name
    print_names()


def delete_name():
    print_names()
    row_ask = int(input('Enter row number to delete name : '))
    names.pop(row_ask)
    print_names()


def print_names():
    count_row = 0
    for row in names:
        print('Row  ' + str(count_row) + ' : ' + str(row))
        count_row += 1


def main():
    state = True
    while state:
        print('1) Add name')
        print('2) Change name')
        print('3) Delete name')
        print('4) Quit')
        operation_ask = int(input('Enter action to do : '))
        if operation_ask == 1:
            add_name()
        elif operation_ask == 2:
            change_name()
        elif operation_ask == 3:
            delete_name()
        elif operation_ask == 4:
            print('Good bye')
            state = False
        else:
            print('Invalid input, please try again.')


names = ['abdullah', 'ahmed', 'hasanen', 'ali']
main()
