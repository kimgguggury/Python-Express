import os 
arr = os.listdir()

for f in arr :
    infile = open(f, "r", encoding="utf-8")
    for line in infile :
        e = line.rstrip()
        if "python" in e :
            print(f,":",e)
    infile.close()