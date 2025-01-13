import re

password = input("패스워드를 입력하시오")

flag = 0

while True :
    if (len(password)<8) :
        flag = -1
        break
    elif not re.search("[a-z]", password) :
        flag = -1
        break
    elif not re.search("[A-Z]", password) :
        flag = -1
        break
    elif not re.search("[0-9]", password) :
        flag = -1
        break
    elif not re.search("[_@$]", password) :
        flag = -1
        break
    else :
        flag = 0
        print("유효한 패스워드")
        break
if flag == -1 :
    print("유효한 패스워드가 아닙니다.")
    
