infile = open("text_file/copy.txt")
outfile = open("output.txt","w")

i = 1

for line in infile :
    outfile.write(str(i) + ": " + line)
    i = i + 1

infile.close()
outfile.close()