
# infile = open("text_file/sales.txt", "r")
# outfile = open("text_file/sales.txt", "a")
# sum = 0
# avg = 0
# cnt = 1
# line = infile.readline() 
# while line != "" :
#     sum += int(line)
#     cnt += 1
#     line = infile.readline() 
    
# avg = sum / cnt
# infile.close()

# outfile.write(f"총매출 = {sum}")
# outfile.write(f"평균 일매출 = {avg}")

# outfile.close()

infile = open("text_file/sales.txt", "r")
outfile = open("text_file/sales.txt", "a")  # 기존 파일에 내용 추가하려면 "a", 새로 쓰려면 "w"

sum = 0
cnt = 0
line = infile.readline()

while line != "":
    sum += int(line)
    cnt += 1
    line = infile.readline()

avg = sum / cnt

infile.close()

outfile.write(f"\ntotal sales = {sum}\n")
outfile.write(f"aveage sales for a day = {avg}\n")

outfile.close()
