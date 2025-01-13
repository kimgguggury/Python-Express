import csv

f = open("csv_file/sample_data.csv", "r")
data = csv.reader(f)
header = next(data)
for row in data :
    print(row)
f.close()