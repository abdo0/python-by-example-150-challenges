from tkinter import *
import csv

def add_number():
    num=num_box.get()
    if num.isdigit():
        num_list.insert(END,num)
        num_box.delete(0,END)
        num_box.focus()
    else:
        num_box.delete(0,END)
        num_box.focus()

def clear_list():
    num_list.delete(0,END)
    num_box.focus()

def save_list():
    file=open("numbers.csv","w")
    tmp_list=num_list.get(0,END)
    item=0
    for x in tmp_list:
        newrecord=tmp_list[item]+"\n"
        file.write(str(newrecord))
        item=item+1
    file.close()

window=Tk()
window.title("Number list")
window.geometry("400x200")

label1=Label(text="Enter a number: ")
label1.place(x=20, y=20, width=100, height=25)

num_box=Entry(text=0)
num_box.place(x=120, y=20, width=100, height=25)
num_box.focus()

num_list=Listbox()
num_list.place(x=120, y=50, width=100, height=100)

button1=Button(text="Add to list", command=add_number)
button1.place(x=250, y=20, width=100, height=25)

button2=Button(text="Clear list", command=clear_list)
button2.place(x=250, y=50, width=100, height=25)

button3=Button(text="Save list", command=save_list)
button3.place(x=250, y=80, width=100, height=25)

window.mainloop()