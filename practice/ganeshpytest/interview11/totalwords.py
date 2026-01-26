line=0
words=0
fr=open("file1.txt")
for i in fr:
    i=i.strip()
    #line = line + 1
    if i=="":
        continue
    line = line + 1
    out=i.split()
    #print(out,len(out))
    words=words+len(out)

fr.close()
print(words)
print(line)