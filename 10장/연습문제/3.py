f = input("파일 이름을 입력하시오")

infile = open(f"text_file/{f}","r",encoding="utf-8")
rowNum = int(input("행 번호를 입력하시오"))

cnt=0
for line in infile :  #0번째행 cnt 1, 1번째행 cnt=2, 2번째행 cnt==3, 4번째행
    if cnt == rowNum-1 :
        print(line)
        break
    else :
        cnt +=1

infile.close() 