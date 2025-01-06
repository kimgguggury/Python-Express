seats = []
rows = 10
cols = 10

for row in range(rows) :
    seats += [[0] * cols]

while True :
    choiceRow = int(input("원하시는 좌석의 행번호를 입력하세요(종료는 -1) : "))
    choiceCol = int(input("원하시는 좌석의 열번호를 입력하세요(종료는 -1) : "))
    if choiceRow == -1 or choiceCol == -1 :
        break
    elif seats[choiceRow][choiceCol] == 0 :
        seats[choiceRow][choiceCol] = 1
        print("예약이 완료됨")
    else :
        print("좌석이 차있음")
        
