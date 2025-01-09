from tkinter import *

window = Tk()
total = 0
def up () :
    global total
    total += 1
    label['text'] = str(total)

def down() :
    global total
    total -= 1
    label['text'] = str(total)
    

downButton = Button(window,width=10, text="감소", command=down)
downButton.pack(side=LEFT)

label = Label(window,width=10, text=total)
label.pack(side=LEFT)

upButton = Button(window, width=10, text="증가", command=up)
upButton.pack(side=LEFT)
window.mainloop()
