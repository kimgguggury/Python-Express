from tkinter import *

window = Tk()

Label(window, text = "너비").grid(row = 0, column = 0)
Label(window, text = "높이").grid(row = 1, column = 0)

e1 = Entry(window).grid(row = 0, column = 1)
e2 = Entry(window).grid(row = 1, column = 1)

photo = PhotoImage(file="C:\Python Express\photo\image.png")
label = Label(window, image=photo)
label.grid(row = 0, column = 2, columnspan = 2, rowspan = 2)

button1 = Button(window, text="이미지 저장").grid(row = 2, column = 0, columnspan=2)
button2 = Button(window, text="확대").grid(row = 2, column= 2)
button2 = Button(window, text="축소").grid(row = 2, column= 3)
window.mainloop()       