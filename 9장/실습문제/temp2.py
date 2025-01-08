from tkinter import *

def process() :
    tf = float(e1.get())
    tc = (tf-32.0)*5.0/9.0
    e2.delete(0, END)
    e2.insert(0, str(tc))
    

window = Tk()
Label(window, text="화씨").grid(row = 0, column = 0)
Label(window, text="섭씨").grid(row = 1, column = 0)

e1 = Entry(window)  # Entry 객체를 생성하고
e1.grid(row=0, column=1)  # grid 메서드를 별도로 호출
e2 = Entry(window)
e2.grid(row=1, column=1)

button = Button(window, text="화씨 -> 섭씨", command=process).grid(row = 2, column = 1)
window.mainloop()   