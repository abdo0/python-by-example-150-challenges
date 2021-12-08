from tkinter import *

def add_on():
    num=enter_txt.get()
    num=int(num)
    answer=output_txt["text"]
    answer=int(answer)
    total=num+answer
    output_txt["text"]=total

def reset():
    total=0
    output_txt["text"]=0
    enter_txt.delete(0,END)
    enter_txt.focus()

total=0
num=0

window=Tk()
window.title("Adding Together")
window.geometry("450x100")

enter_lbl=Label(text="Enter a number: ")
enter_lbl.place(x=50, y=20, width=100, height=25)

enter_txt=Entry(text=0)
enter_txt.place(x=150, y=20, width=100, height=25)
enter_txt["justify"]="center"
enter_txt.focus()

add_btn=Button(text="Add", command=add_on)
add_btn.place(x=300, y=20, width=50, height=25)

output_lbl=Label(text="Answer= ")
output_lbl.place(x=50, y=50, width=100, height=25)

output_txt=Message(text=0)
output_txt.place(x=150, y=50, width=100, height=25)
output_txt["bg"]="white"
output_txt["relief"]="sunken"

clear_btn=Button(text="Clear", command=reset)
clear_btn.place(x=300, y=50, width=50, height=25)

window.mainloop()