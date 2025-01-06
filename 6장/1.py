N = int(input("입력할 값의 개수"))
number = []
for i in range(N) :
    num = int(input())
    number.append(num)
print(f"값의 합계 = {sum(number)}")
