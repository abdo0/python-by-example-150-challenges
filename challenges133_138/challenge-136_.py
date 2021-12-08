from tkinter import *

def add_to_list():
    name=namebox.get()
    namebox.delete(0,END)
    genderselection = gender.get()
    gender.set("M/F")
    newdata = name + "," + genderselection + "\n"
    name_list.insert(END,newdata)
    namebox.focus()

window=Tk()
window.title("People list")
window.geometry("400x400")

namelbl=Label(text="Enter their name")
namelbl.place(x=50, y=50, width=100, height=25)

namebox=Entry(text="")
namebox.place(x=150, y=50, width=150, height=25)
namebox.focus()

genderlbl=Label(text="Select gender")
genderlbl.place(x=50, y=100, width=100, height=25)

gender=StringVar(window)
gender.set("M/F")

gendermenu=OptionMenu(window,gender, "M", "F")
gendermenu.place(x=150,y=100)

name_list=Listbox()
name_list.place(x=150, y=150, width=150, height=100)

addbtn=Button(text="Add to list", command=add_to_list)
addbtn.place(x=50, y=300, width=100, height=25)

window.mainloop()