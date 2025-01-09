from tkinter import *

window = Tk()

def changeStr() :
    label["text"] = "clicked"

label = Label(window,text="Hi!")
label.pack(side = LEFT)
button = Button(window, text="click me", command=changeStr)
button.pack(side=LEFT)
window.mainloop()