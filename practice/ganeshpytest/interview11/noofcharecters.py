#hoiw to know no.of charecters

chars=0
fr=open("file1.txt")
for i in fr:
    i=i.strip()
    for j in i:
        chars=chars+1
fr.close()
print(f"total no.of chars are {chars}")
#or
chars=0
fr=open("file1.txt")
for i in fr:
    i=i.strip()
    if i=="":
        continue
    chars=chars+len(i) #0+len("10")
fr.close()
print(chars)

