infile = open("text_file/input.txt","r",encoding='UTF8')
cnt = 0

while cnt < 3 :
    line = infile.readline().strip()
    print(line)
    cnt+=1

infile.close()