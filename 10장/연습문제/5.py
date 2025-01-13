infile = open("text_file/subject.txt","r")
lists = infile.readlines()
print(lists)

print(lists)
lists.insert(2,"line 2-1\n")
print(lists)


infile.close()
outfile = open("text_file/copy.txt","w")
for line in lists :
    outfile.write(line)

outfile.close()