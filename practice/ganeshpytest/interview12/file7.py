import re

fr=open("file2.txt","r")
country=""
mylist=[]
for i in fr:
    i=i.strip()
    exp1="^=+\s*([a-zA-Z]+)\s*=+$"
    o1=re.search(exp1,i)
    if o1:
        country=o1.group(1)
        mylist.clear()
    exp2="^[a-zA-Z]{3}\s*:\s*(\d+)$"
    o2=re.search(exp2,i)
    if o2:
        #print(o2.group(1))
        mylist.append(int(o2.group(1)))
    o3=re.search("^=+$",i)
    if o3:
        #print("end of the line")
        #mylist.clear()

        print(country,sum(mylist))


