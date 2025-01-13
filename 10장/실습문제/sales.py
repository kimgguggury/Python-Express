
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

infile = open("text_file/sales.txt", "r", encoding="utf-8")
outfile = open("text_file/sales.txt", "a", encoding="utf-8")  # 기존 파일에 내용 추가하려면 "a", 새로 쓰려면 "w"

sum = 0
cnt = 0
line = infile.readline()

while line != "":
    sum += int(line)
    cnt += 1
    line = infile.readline()

avg = sum / cnt

infile.close()

outfile.write(f"\n총 매출액 = {sum}\n")
outfile.write(f"평균적인 매출액 = {avg}\n")

outfile.close()
