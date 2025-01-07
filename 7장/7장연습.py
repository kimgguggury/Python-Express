# numbers = [10, 20, 30]
# numbers += (40, 50)

# print(numbers)
# numbers[4] = 2
# print(numbers)

# 실습문제 1 set

# str1 = input("첫 번째 문자열")
# str2 = input("두 번째 문자열")

# common = list(set(str1)&set(str2))
# print(f"공통된 문자열은",end="")
# for element in common :
#     print(element, end=" ")
# print("입니다.")

# 실습문제 2 set

# str = input("입력 텍스트")
# newStr = ""
# lists = []
# for s in str :
#     if s != ' ':
#         newStr += s
#     elif s == ' ' :
#         lists.append(newStr)
#         newStr = ''
# lists.append(newStr)
# print(lists)
# checkWord = set(lists)
# print(len(checkWord))

# txt = input("입력 텍스트")
# words = txt.split(" ")
# unique = set(words)
# print("사용된 단어의 개수 = ", len(unique))
# print(unique)

# capitals = { "korea" : "Seoul"}
# capitals.clear()

# if len(capitals) == 0 :
#     print("딕셔너리에 항목이 있음")
# else :
#     print("딕셔너리가 비어 있음")

# 영한사전 만들기 dictionary

# dic = {}
# dic["one"] = "하나"
# dic["two"] = "둘"
# dic["three"] = "셋"

# str = input("단어를 입력하시오")

# if str in dic :
#     print(f"{str}의 뜻은 {dic[str]}입니다")
# else:
#     print("사전에 등록 x")

# score_dic = {
#     "kim" : [99, 83, 95],
#     "Lee" : [68, 45, 78],
#     "Choi" : [25, 56, 69] }

# sum = 0

# for name, scores in score_dic.items() :
#     for score in scores :
#         sum += score 
#     print("%s 의 성적 평균은 %.2f" % (name,sum/3))
#     sum = 0


#단어 카운터 만들기
# dic = {}
# text = "Create the highest, grandest vision possible for your life, because you become what you believe"
# cnt = 0
# textLists = text.split(" ")
# for textList in textLists :
#     for str in textLists :
#         if str == textList :
#             cnt += 1

#     dic[textList] = cnt
#     cnt = 0

# print(dic)

# text = "Create the highest, grandest vision possible for your life, because you become what you believe"

# word_dic = {}
# for w in text.split() :
#     if w in word_dic :
#         word_dic[w] += 1
#     else :
#         word_dic[w] = 1

# for w, count in sorted(word_dic.items()) :
#     print(w, "의 등장 횟수 = ", count)


# s = "Hello, World!"
# p = s.split(", ")
# print(p)

# str = input("문자열을 입력하시오")
# lists = str.split()
# print(lists)
# for element in lists :
#     print(element[0], end="")

# email = input("이메일 주소를 입력하시오:")
# (id, domain) = email.split("@")

# print(f"아이디 :{id}")
# print(f"도메인:{domain}")

# str = input("문자열을 입력하시오")

# dic = {"digits" : 0, "spaces" : 0, "alphas" : 0}

# for element in str :
#     if element.isdigit() :
#         dic["digits"] += 1
#     elif element.isspace() :
#         dic["spaces"] += 1
#     elif element.isalpha() :
#         dic["alphas"] += 1

# print(dic)

# import random

# s = input("문자열을 입력하시오")
# sampleStr = random.sample(s, 4)
# print(sampleStr)
# print("".join(sampleStr))
