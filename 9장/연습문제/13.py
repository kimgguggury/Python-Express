from tkinter import * 
def left(event):
    canvas.move(id, -5, 0)
def right(event):
    canvas.move(id, 5, 0)
def down(event):
    canvas.move(id, 0, 5)
def up(event):
    canvas.move(id, 0, -5)
window = Tk() 
frame = Frame(window, width=500, height=300)
frame.bind('<Left>', left)
frame.bind('<Right>', right)
frame.bind('<Up>', up)
frame.bind('<Down>', down)
frame.focus_set()
frame.pack()
canvas = Canvas(frame, bg = "white", width = 500, height = 300)
canvas.grid(row=0, column=0, columnspan=4)
id = canvas.create_rectangle(100, 100, 200, 200, fill = "blue")
window.mainloop() 