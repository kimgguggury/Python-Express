#피보나치 수열(반복문 만으로 내 풀이)

# num = int(input("몇 번째 항까지 구할까요?"))

# num1 = 0
# num2 = 1
# print(f"{num1}, {num2}",end="")
# for i in range(num-1) :
#     num3 = num1 + num2
#     print(f", {num3}",end="")
#     num1 = num2
#     num2 = num3
    

#교재 풀이

nterms = int(input("몇 번째 항까지 구할까요"))

n1, n2 = 0, 1
count = 0

while count <= nterms :
    print(n1, end=" ")
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

