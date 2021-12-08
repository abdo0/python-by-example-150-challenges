from tkinter import *

def convert1():
    mile=textbox2.get()
    mile=int(mile)
    message=mile/0.6214
    textbox1.delete(0,END)
    textbox1.insert(END, message)
    textbox1.insert(END, "km")

def convert2():
    km=textbox1.get()
    km=int(km)
    message=km*0.6214
    textbox2.delete(0,END)
    textbox2.insert(END, message)
    textbox2.insert(END, "miles")

window=Tk()
window.title("Distance")
window.geometry("260x200")

label1=Label(text="Enter the value you want to convert: ")
label1.place(x=30, y=20)

textbox1=Entry(text="")
textbox1.place(x=30, y=50, width=200, height=25)
textbox1["justify"]="center"
textbox1.focus()

convert1=Button(text="Convert miles to km", command=convert1 )
convert1.place(x=30, y=80, width=200, height=25)

convert2=Button(text="Convert km to mile", command=convert2 )
convert2.place(x=30, y=110, width=200, height=25)

textbox2=Entry(text="")
textbox2.place(x=30, y=140, width=200, height=25)
textbox2["justify"]="center"

window.mainloop()