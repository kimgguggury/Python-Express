#최대 공약수 구하기 (내가 한 풀이)
# def findGreatestCommonFactor(first, second) :
#     divisor = (second if first >= second else first) 
    
#     greatestCommonFactor = 1

#     for i in range(1,divisor+1) :
#         if first % i == 0 and second % i == 0 :
#             if (greatestCommonFactor < i) :
#                 greatestCommonFactor = i
    
#     return greatestCommonFactor


# firstNum = int(input("첫 번째 정수:"))
# secondNum = int(input("두 번째 정수"))

# print(findGreatestCommonFactor(firstNum, secondNum))

#유클리드 호제법

def gcd(a, b) :
    if b == 0 :
        return a
    else :
        return gcd(b, a % b)

firstNum = int(input("첫 번째 정수:"))
secondNum = int(input("두 번째 정수:"))

print(gcd(firstNum, secondNum))

