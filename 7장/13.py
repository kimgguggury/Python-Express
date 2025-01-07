str = input("문자열 입력")
dic = { "LETTERS" : 0, "DIGITS" : 0}
dic["LETTERS"] = sum(1 for x in str if x.isalpha())
dic["DIGITS"] = sum(1 for x in str if x.isdigit())
print(dic)

