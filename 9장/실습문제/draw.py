from tkinter import *

WIDTH = 600
HEIGHT = 200

def displayRec() :
    canvas.create_rectangle(10, 10, WIDTH-10, HEIGHT-10)

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

frame = Frame(window)
frame.pack()

