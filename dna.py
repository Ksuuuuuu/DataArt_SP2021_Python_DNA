import csv
reader=csv.reader(open('databases/small.csv'))
result={}
for row in reader:
    key=row[1:]
    result[key]=row[0]
print result
