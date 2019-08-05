def enter_number():
    num = int(input('Please enter number : '))
    return num


def main():
    num = enter_number()
    for i in range(num):
        print(i)


main()
