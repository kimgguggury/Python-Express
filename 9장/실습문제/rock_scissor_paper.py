import random
from tkinter import *

window = Tk()
Label(window, text="선택하세요", font=("Helvetica", "16")).pack()
frame = Frame(window)

rock_image = PhotoImage(file="C:\Python Express\photo\바위.png")
paper_image = PhotoImage(file="C:\Python Express\photo\보.png")
scissors_image = PhotoImage(file="C:\Python Express\photo\가위.png")

def pass_s():
    decide("가위")
def pass_r():
    decide("바위")
def pass_p():
    decide("보")
   
rock = Button(frame, image = rock_image, command= pass_r)
rock.pack(side="left")
paper = Button(frame, image = paper_image, command= pass_p)
paper.pack(side="left")
scissors = Button(frame, image = scissors_image, command= pass_s)
scissors.pack(side="left")

frame.pack()

Label(window, text = "컴퓨터는 다음을 선택하였습니다.", font=("Helvetica", "16")).pack()
computer_image = Label(window, image=rock_image)
computer_image.pack()
output = Label(window, text="", font=("Helvetica", "16"))
output.pack()

def decide(human) :
    computer = random.choice(["가위", "바위", "보"])
    if computer == "바위" :
        computer_image["image"] = rock_image
    elif computer == "보" :
        computer_image["image"] = paper_image
    else :
        computer_image["image"] = scissors_image


window.mainloop()