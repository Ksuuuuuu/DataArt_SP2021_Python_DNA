import csv
name_csv=input("Введите имя файла с данными\n")
reader= csv.reader(open(name_csv))
D={}
for row in reader:
    key=row[0]
    D[key]=row[1:]
name_txt=input("Введите имя файла с днк искомого человека")
with open(name_txt, 'r') as file:
    str=file.read()
lst_count=[]
is_find_coloumn=D.get('Name')
for i in is_find_coloumn:
    count=0
    first_pos=str.find(i)
    if first_pos !=-1:
        count=1
        size=len(i)
        buffer=str[first_pos+size:first_pos+2*size-1]
        while i==buffer:
            count+=1
            buffer=str[first_pos+size*count:first_pos+size*count+size-1]
    lst_count.append(count) 
lst=D.items()
find=0
for i int lst:
    if i[1]==lst_count:
        print(i[0])
        find=1
if find==0:
    print('No match')
    

        
        
        
