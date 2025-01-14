lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("원래 리스트 :")
print(lists)
print("세제곱된 값:")
result = list(map(lambda x : x**3,lists))
print(result)