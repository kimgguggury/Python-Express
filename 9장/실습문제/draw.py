from tkinter import *

WIDTH = 600
HEIGHT = 200

def displayRec() :
    canvas.create_rectangle(10, 10, WIDTH-10, HEIGHT-10)

def displayOval() :
    canvas.create_oval(10,10,WIDTH-10,HEIGHT-10)

def displayArc() :
    canvas.create_arc(10, 10, WIDTH-10, HEIGHT-10, start = 0,
                      extent=120, width=10, fill='blue')
def displayPolygon() :
    canvas.create_polygon(10, 10, WIDTH-10, HEIGHT-10,200, 90, 300, 160)
def displayLine() :
    canvas.create_line(10, 10, WIDTH-10, HEIGHT - 10, fill="green")
def clearCanvas() :
    canvas.delete(ALL)

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

frame = Frame(window)
frame.pack()

btRectangle = Button(frame, text="Rectanle", command=displayRec).grid(row=1, column=2)
btOval = Button(frame, text="Oval", command=displayOval).grid(row = 1, column=3)
btArc = Button(frame, text="Arc", command=displayArc).grid(row=1,column=5)
btPolygon = Button(frame, text="Polygon", command=displayPolygon).grid(row=1,column=4)
btLine = Button(frame, text="Line",command=displayLine).grid(row=1,column=1)
btClear=Button(frame, text="Clear", command=clearCanvas).grid(row=1,column=7)

window.mainloop()