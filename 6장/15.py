import random

lists = []
rememberCnt = []
cnt = 0
for i in range(10) :
    lists.append(random.randint(0,1))

print(lists)

for i in range(0,9) :
    if lists[i] == lists[i+1] :
        cnt += 1
    else :
        rememberCnt.append(cnt)
        cnt = 0
rememberCnt.append(cnt)
print("cnt기억한 리스트", rememberCnt)

print(f"최대 연속 길이 {max(rememberCnt)}")