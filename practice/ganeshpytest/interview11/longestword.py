#longest word
fr=open("file1.txt")
fr.close()
length=0
lw=""
w=["india","uk","germany","y"]
for i in w:
    out=len(i)
    if out>length:
        out=length
        lw=i
print(lw)

ll=0
lw=""
a=["yousuf","esuf","usuf"]
for i in a:
    q=len(i)
    if q>ll:
        q=ll
        lw=i
print(lw)