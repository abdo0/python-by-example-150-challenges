import random

def select_col():
    colours=["r", "b", "o", "y", "p", "g", "w"]
    c1=random.choice(colours)
    c2=random.choice(colours)
    c3=random.choice(colours)
    c4=random.choice(colours)
    data=(c1, c2, c3, c4)
    return data

def tryit(c1, c2, c3, c4):
    print("The colours are: (r)ed, (b)lue, (o)range, (y)ellow, (p)ink, (g)reen, (w)hite")
    try_again=True
    while try_again==True:
        u1=input("Enter your choice for place 1: ")
        u1=u1.lower()
        if u1 !="r" and u1 !="b" and u1 !="o" and u1 !="y" and u1 !="p" and u1 !="g" and u1 !="w":
            print("Incorrect selection")
        else:
            try_again=False

    try_again=True
    while try_again==True:
        u2=input("Enter your choice for place 2: ")
        u2=u2.lower()
        if u2 !="r" and u2 !="b" and u2 !="o" and u2 !="y" and u2 !="p" and u2 !="g" and u2 !="w":
            print("Incorrect selection")
        else:
            try_again=False

    try_again=True
    while try_again==True:
        u3=input("Enter your choice for place 3: ")
        u3=u3.lower()
        if u3 !="r" and u3 !="b" and u3 !="o" and u3 !="y" and u3 !="p" and u3 !="g" and u3 !="w":
            print("Incorrect selection")
        else:
            try_again=False

    try_again=True
    while try_again==True:
        u4=input("Enter your choice for place 4: ")
        u4=u4.lower()
        if u4 !="r" and u4 !="b" and u4 !="o" and u4 !="y" and u4 !="p" and u4 !="g" and u4 !="w":
            print("Incorrect selection")
        else:
            try_again=False
    
    correct=0
    wrong_place=0

    if c1==u1:
        correct=correct+1
    elif c1==u2 or c1==u3 or c1==u4:
        wrong_place=wrong_place+1

    if c2==u2:
        correct=correct+1
    elif c2==u1 or c2==u3 or c2==u4:
        wrong_place=wrong_place+1

    if c3==u3:
        correct=correct+1
    elif c3==u1 or c3==u2 or c3==u4:
        wrong_place=wrong_place+1

    if c4==u4:
        correct=correct+1
    elif c4==u1 or c4==u2 or c4==u3:
        wrong_place=wrong_place+1

    print("Correct colour in the correct place: ", correct)
    print("Correct colour but in the wrong place: ", wrong_place)
    print()

    data2=(correct, wrong_place)
    return data2

def main():
    (c1, c2, c3, c4) = select_col()
    score = 0
    play = True
    while play == True:
        (correct, wrong_place) = tryit(c1, c2, c3, c4)
        score=score+1
        if correct==4:
            play=False
    print("You win!")
    print("You took", score, "guesses")

main()