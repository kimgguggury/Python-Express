#내가 한 답
# import random

# infile = open("text_file/words.txt","r",encoding="utf-8")
# lists = []

# for line in infile :
#     s = line.strip()
#     lists.append(s)

# tries = 0
# problem = random.choice(lists)
# word = list(problem)

# showList = []
# for i in range(len(word)) :
#     showList.append("_")
#     print(showList[i],end="")
# print("")

# while tries < 10 :
#     answer = input("단어를 추측하시오")
#     if showList == word :
#         print("너가 이겼어!")
#         break
#     if answer in word :
#         print("맞아!")
#         idx = word.index(answer)
#         showList[idx] = answer
#     else :
#         tries += 1
#         print(str(10-tries)+"기회 남음")
    
#     for show in showList :
#         print(show,end="")
#     print()
    
#     if showList == word :
#         print("너가 이겼어!")
#         break

# infile.close()

import random

guesses = ''
turns = 10

infile = open("text_file/words.txt","r",encoding="utf-8")
lines = infile.readlines()

print(lines)
word = random.choice(lines)

while turns > 0 :
    failed = 0
    for char in word :
        if char in guesses :
            print(char, end="")
        else:
            print("_", end="")
            failed+=1
        
    if failed == 0 :
        print("사용자 승리")
        break
    print("")
    guess = input("단어를 추측하시오")
    guesses += guess
    if guess not in word :
        turns -= 1
        print("틀렸음!")
        print(str(turns)+"기회가 남았음!")
        if turns == 0: 
            print("사용자 패배 정답은 " +word)

infile.close()
        