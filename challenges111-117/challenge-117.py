import csv
import random

score = 0

ask_name = str(input('Enter your name : '))
qustion_1_num_1 = random.randint(1, 100)
qustion_1_num_2= random.randint(1, 100)
answer_1 = qustion_1_num_1 + qustion_1_num_2
ask_answer_1 = int(input(str(qustion_1_num_1) + '+' + str(qustion_1_num_2) + '= '))
if answer_1 == ask_answer_1:
    score += 1

qustion_2_num_1 = random.randint(1, 100)
qustion_2_num_2 = random.randint(1, 100)
answer_2 = qustion_2_num_1 + qustion_2_num_2
ask_answer_2 = int(input(str(qustion_2_num_1) + '+' + str(qustion_2_num_2) + '= '))
if answer_2 == ask_answer_2:
    score += 1

file = open('QuizScore.csv', 'a')
file.write(ask_name + ', ' + str(ask_answer_1) + ', ' + str(answer_1) + ', ' + str(ask_answer_2) + ', ' + str(answer_2) + '\n')
file.close()
