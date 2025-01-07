str1 = input("첫 번째 문자열")
str2 = input("두 번째 문자열")

common = list(set(str1) & set(str2))

for element in common :
    if element.isalpha() :
        print(element, end=" ")
   

# s1 = input("첫 번째 문자열:")
# s2 = input("두 번째 문자열:")

# set1 = set(s1)
# set2 = set(s2)

# print("모두 포함된 글자 : ", set1 & set2)
