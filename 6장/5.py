lists = ['aba', 'xyz', 'abc', '121']
cnt = 0
for element in lists :
    if element[0] == element[-1] :
        cnt += 1
print(cnt)