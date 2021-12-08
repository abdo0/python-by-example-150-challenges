from tkinter import *
import random

def click():
    num=random.randint(1,6)
    answer["text"]=num

window=Tk()
window.title("Roll a dice")
window.geometry("100x120")

button1=Button(text="Roll", command=click)
button1.place(x=30, y=30, width=50, height=25)

answer=Message(text="")
answer.place(x=40, y=70, width=30, height=25)

window.mainloop()