import random


def low_high_range():
    low = int(input('Enter low number : '))
    high = int(input('Enter high number : '))
    num = random.randint(low, high)
    print(num)
    return num


def user_ask():
    ask = int(input('I am thinking of a number... : '))
    return ask


def check(ask, comp_num):
    if ask == comp_num:
        return True
    else:
        return False


def main():
    comp_num = low_high_range()
    state = True
    while state:
        user_ask_int = user_ask()
        if check(user_ask_int, comp_num):
            state = False
            print('Correct, you win')
        else:
            if user_ask_int < comp_num:
                print('Too low')
            elif user_ask_int > comp_num:
                print('Too high')


main()
