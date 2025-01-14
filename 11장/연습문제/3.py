lists = [('국어',88), ('수학', 90), ('영어',99), ('자연', 82)]

revisedLists = sorted(lists, key = lambda item : item[1])
print(revisedLists)