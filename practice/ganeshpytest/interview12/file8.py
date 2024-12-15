import re
count=0
lw=""
length=0
words=0
chars=0
mylist=[]
fr=open("file3.txt","r")
for i in fr:
    i=i.strip()
    count=count+1
    exp="\d+[a-z]{2}([06])"
    o=re.search(exp,i)
    if o:
        #print(o.group(1))
        mylist.append(int(o.group(1)))
    i=i.split()
    words+=len(i)
    for w in i:
        w=w.strip()
        for j in w:
            chars+=1


fr.close()
print(count)
print(mylist)
print(words)
print(lw)
print(chars)


list1=[[10,20,30],[18,20,22],[100,20,30]]
l=[]
for i in list1:#[10,20,30]
    for j in i:
        l.append(j)

list1 = [[10, 20, 30], [18, 20, 22], [100, 20, 30]]
flattened_list = []

for sublist in list1:
    for item in sublist:
        flattened_list.append(item)

print(flattened_list)


out=list1[::-1]
print(out)
ll=[]
for i in list1:
    ll.append(i[::-1])
print(ll)

list1 = [[10, 20, 30], [18, 20, 22], [100, 20, 30]]
flattened_list = []

for sublist in list1:
    for item in sublist:
        flattened_list.append(item)
print(flattened_list)




