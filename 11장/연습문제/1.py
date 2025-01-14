#3의 배수만 !!!
def myFilter(x) :
    return x % 3 == 0

list1 = [num for num in range(1,101)]
result = list(filter(myFilter, list1))
print(len(result))