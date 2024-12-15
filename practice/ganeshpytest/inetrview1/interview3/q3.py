#how to open 2 file using with keyword
#how to handle 2 files with with keyword]
import re
with open("data.txt") as fr , open("output.txt","w") as fw:
    for i in fr:
        i=i.strip()
        if i.isdigit():
            fw.write(f"{i}\n")

with open("data.txt") as fr,open("output1.txt","w")as fw:
    for i in fr:
        out=re.search("\w+.\.\w+",i)
        if out:
            fw.write(f"{i}\n")





