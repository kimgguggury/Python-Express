# while True:
#         try:
#                 fname = input("  입력파일이름: ").strip()
#                 infile = open(fname, "r")
#                 print("오류가 아니면 여기도?") 
#                 break
#         except IOError:
#                 print(" 파일" + fname + "  이없습니다.  다시입력하시오.")
# print("  파일이성공적으로열렸습니다.")
# infile.close() 


def inputFile() :
    fName = input("입력 파일 이름:")
    infile = None
    try :
        infile = open(f"{fName}", "r")
        
    except IOError :
      
        print(f"{fName}이 없습니다. 다시 입력하시오.")
        inputFile()    
    else :
        print("파일이 성공적으로 열렸습니다.")
    finally :
        if infile:  
            infile.close()
inputFile()