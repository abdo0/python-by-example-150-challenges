#Sometimes, it doesn't work with certain error message on Jupyter notebook.
#In case of error, restart IDE and that will do.

from tkinter import *

def clicked():
    num=selection.get()
    artref=num+".png"
    photo=PhotoImage(file=artref)
    photobox.image=photo
    photobox["image"]=photo
    photobox.update()

window=Tk()
window.title("Art")
window.geometry("400x350")

art=PhotoImage(file="1.png")
photobox=Label(window, image=art)
photobox.image=art
photobox.place(x=100, y=20, width=200, height=150)

label=Label(text="Select art number: ")
label.place(x=50, y=200, width=100, height=25)

selection=Entry(text="")
selection.place(x=200, y=200, width=100, height=25)
selection.focus()

clickme=Button(text="See art", command=clicked)
clickme.place(x=150, y=250, width=100, height=25)

window.mainloop()