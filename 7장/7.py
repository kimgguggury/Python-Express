dic = {}
for i in range(3) :
    date = input("날짜를 입력하시오")
    scedule = input("일정을 입력하시오")

    if date in dic :
        dic[date].append(scedule)
    else :
        dic[date] = []
        dic[date].append(scedule)

print(dic)
       
# myDic = {}
# for i in range(2) :
#     date = input("날짜를 입력하시오")
#     job = input("일정을 입력하시오")
    
#     if date in myDic :
#         myDic[date].append(job)
#     else :
#         myDic[date]= []
#         myDic[date].append(job)

# print(myDic)