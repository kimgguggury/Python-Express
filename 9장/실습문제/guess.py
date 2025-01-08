# from tkinter import *
# import random

# def tryFunc() :
#     global answer
#     ans = int(e.get())
#     if ans == answer :
#         label2["text"] ="정답!"
#     elif ans < answer :
#         label2["text"] = "업!"
#     elif ans > answer :
#         label2["text"] = "다운!"


# def resetFunc() :
#     global answer
#     answer = random.randint(1, 100)
#     label2["text"] = "1부터 100사이의 숫자를 입력하시오"
        
# answer = random.randint(1, 100)

# window = Tk()

# label1 = Label(window, text = "숫자 게임에 오신 것을 환영합니다.")
# label1.grid(row = 0, column=0,columnspan=2)

# e = Entry(window)
# e.grid(row=1, column=0)

# label2 = Label(window, text="1부터 100사이의 숫자를 입력하시오")
# label2.grid(row=1,column=3)

# tryButton = Button(window, text = "시도", fg = "green", command=tryFunc)
# tryButton.grid(row=1, column=1)

# resetButton = Button(window, text = "초기화", fg = "red", command = resetFunc)
# resetButton.grid(row=1, column=2)
# window.mainloop()

from tkinter import *
import random

def tryFunc():
    global answer
    ans = int(e.get())
    if ans == answer:
        label2["text"] = "정답!"
    elif ans < answer:
        label2["text"] = "업!"
    elif ans > answer:
        label2["text"] = "다운!"

def resetFunc():
    global answer
    answer = random.randint(1, 100)
    label2["text"] = "1부터 100사이의 숫자를 입력하시오"

answer = random.randint(1, 100)

window = Tk()

# 전체 열 수는 4로 가정하고 columnspan=4로 설정
label1 = Label(window, text="숫자 게임에 오신 것을 환영합니다.")
label1.grid(row=0, column=0, columnspan=4)  # sticky="we"로 좌우 가운데 정렬

e = Entry(window)
e.grid(row=1, column=0)

label2 = Label(window, text="1부터 100사이의 숫자를 입력하시오")
label2.grid(row=1, column=3)

tryButton = Button(window, text="시도", fg="green", command=tryFunc)
tryButton.grid(row=1, column=1)

resetButton = Button(window, text="초기화", fg="red", command=resetFunc)
resetButton.grid(row=1, column=2)

window.mainloop()
