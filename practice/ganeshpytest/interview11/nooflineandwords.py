#count number of lines-12  we can fr.readlines() and len of this
#how many woprds-
#longest words
#longest line-
#highest repeating word-india
#total no.of charecters:

#how to know no of.lines?
line=0
fr=open("file1.txt","r")
for i in fr:
    #i=10\n
    i=i.strip()
    line=line+1

fr.close()
print(f"lines are {line}")

#how to know no.of words?
a="10 20 30 40"
b=a.split()
#print(b)
print(f"no.of wprds are {len(b)}")
print("################")
#how in fille
line=0
words=0
fr=open("file1.txt","r")
for i in fr:
    #i=10\n
    i=i.strip()
    line = line + 1
    if i=="":
        continue
    w=i.split()
    #print(len(w))
    words=words+len(w)
    #print(words)




fr.close()
print(f"no.of words are {line}")

