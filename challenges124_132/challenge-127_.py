from tkinter import *

def add_name():
    name=name_box.get()
    name_list.insert(END,name)
    name_box.delete(0,END)
    name_box.focus()

def clear_list():
    name_list.delete(0,END)
    name_box.focus()

window=Tk()
window.title("Names list")
window.geometry("400x200")

label1=Label(text="Enter a name: ")
label1.place(x=20, y=20, width=100, height=25)

name_box=Entry(text=0)
name_box.place(x=120, y=20, width=100, height=25)
name_box.focus()

button1=Button(text="Add to list", command=add_name)
button1.place(x=250, y=20, width=100, height=25)

name_list=Listbox()
name_list.place(x=120, y=50, width=100, height=100)

button2=Button(text="Clear list", command=clear_list)
button2.place(x=250, y=50, width=100, height=25)

window.mainloop()