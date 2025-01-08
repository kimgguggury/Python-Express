from tkinter import *

window = Tk()

w = Canvas(window, width=300, height=200)
w.pack()

i = w.create_rectangle(50, 25, 200, 100, fill="red")

w.coords(i, 0, 0, 100, 100)
w.itemconfig(i, fill="blue")

window.mainloop()