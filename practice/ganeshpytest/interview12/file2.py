import re
fr=open("file1.txt")
# for i in fr:
#     exp="^\d{2}/\d{2}/\d{4}$"
#     #exp1=""
#     out=re.search(exp,i)
#     if out:
#         print(out.group())

exp="^\d{2}/\d{2}/\d{4}$"
exp1=".+\.com$"
exp2="^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

fw=open("ip.txt","w")
fw1=open("emails.txt","w")
fw2=open("dob.txt","w")
for i in fr:
    i=i.strip()
    w=i.split()
    for j in w:
        out=re.search(exp,j)
        if out:
            #print(out.group())
            fw2.write(out.group()+"\n")
        out=re.search(exp1,j)
        if out:
            fw1.write(out.group()+"\n")
        out=re.search(exp2,j)
        if out:
            g1=int(out.group(1))
            g2=int(out.group(2))
            g3=int(out.group(3))
            g4=int(out.group(4))
            if g1<256 and g2<256 and g3<256 and g4<256:
                fw.write(out.group()+"\n")
            #print(out.group())
fw.close()
fr.close()