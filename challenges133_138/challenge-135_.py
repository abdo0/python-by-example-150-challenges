from tkinter import *

def clicked():
    sel=selectcolour.get()
    window.configure(background=sel)

window=Tk()
window.title("background")
window.geometry("200x200")

selectcolour=StringVar(window)
selectcolour.set("Grey")

colourlist=OptionMenu(window,selectcolour, "Grey", "Red", "Blue", "Green", "Yellow")
colourlist.place(x=50,y=30)

clickme=Button(text="Click me", command=clicked)
clickme.place(x=50, y=150, width=60, height=30)

window.mainloop()