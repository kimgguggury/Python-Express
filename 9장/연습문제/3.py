from tkinter import *

window = Tk()


for row in range(3) :
    for col in range(10) :
        Button(window, text=str(row)+"행, "+str(col)+"열").grid(row=row,column=col)

window.mainloop()     