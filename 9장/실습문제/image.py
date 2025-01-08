from tkinter import *

window = Tk()

canvas = Canvas(window, width=1000, height=600)
canvas.pack()

img = PhotoImage(file="C:\Python Express\photo\image.png")
canvas.create_image(20, 20, anchor=NW, image=img)

window.mainloop()