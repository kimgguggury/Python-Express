# from collections import Counter

# infile = open("text_file/words.txt","r",encoding="utf-8")
# words = []
# ch = infile.read(1)


# while ch != "" :
#     words.append(ch)
#     ch = infile.read(1)    
 
# countDic = {}

# for word in words :
#     if word in countDic :
#         countDic[word] += 1
#     else :
#         countDic[word] = 1

# print(countDic)
# infile.close()

infile = open("text_file/words.txt","r",encoding="utf-8")

freqs = {}

for line in infile :
    for char in line.strip() :
        if char in freqs :
            freqs[char] += 1
        else :
            freqs[char] = 1

print(freqs)
infile.close() 