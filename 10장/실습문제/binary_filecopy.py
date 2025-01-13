infile = open("photo/image.png", "rb")
outfile = open("photo/kkk.png", "wb")

while True :
    copy_buffer = infile.read(1024)
    if not copy_buffer :
        break
    outfile.write(copy_buffer)

print("image.png 파일을 kkk.png 파일로 복사하였습니다.")