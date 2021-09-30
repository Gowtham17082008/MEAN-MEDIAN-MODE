import csv
with open("SOCR-HeightWeight.csv",newline="")as f:
    r=csv.reader(f)
    l=list(r)

l.pop(0)
data=[]
for i in range(len(l)):
    num=l[i][1]
    data.append(float(num))

n=len(data)
total=0

for x in data:
    total=total+x
    
mean=total/n
print(mean)
