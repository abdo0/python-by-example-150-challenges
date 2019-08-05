import random


def addition():
    question_num_1 = random.randint(5, 20)
    question_num_2 = random.randint(5, 20)
    answer = question_num_1 + question_num_2
    ask_answer = int(input(str(question_num_1) + '+' + str(question_num_2) + '= '))
    data = (answer, ask_answer)
    return data


def subtraction():
    question_num_1 = random.randint(25, 50)
    question_num_2 = random.randint(1, 25)
    answer = question_num_1 + question_num_2
    ask_answer = int(input(str(question_num_1) + '+' + str(question_num_2) + '= '))
    data = (answer, ask_answer)
    return data


def check(data):
    rand_ans = data[0]
    user_ans = data[1]
    if rand_ans == user_ans:
        print('Correct')
    else:
        print('Incorrect, the answer is {0}'.format(rand_ans))


def main():
    print('1) Addition')
    print('2) Subtraction')
    operation_ask = int(input('Enter 1 or 2 : '))
    if operation_ask == 1:
        check(addition())
    else:
        check(subtraction())


main()
